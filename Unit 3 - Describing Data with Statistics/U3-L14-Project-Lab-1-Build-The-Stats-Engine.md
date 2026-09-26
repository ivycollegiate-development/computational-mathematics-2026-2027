# U3 L14 — Project Lab 1: Build the Stats Engine

**LO:** build a reusable module that loads, validates, summarises, and describes a dataset, so the dashboard never computes statistics ad hoc.

This is the first of four project labs. Today you build the **engine**. It
has no charts and no privacy logic — tomorrow's lab adds the gate, and the
day after adds the charts. The point of doing it this way is that every
number your dashboard shows comes from **one** tested function, not from
something you typed into a chart call at 11pm.

**Definition of done for today:** `stats_engine.py` imports cleanly, runs on
`u3_project_dataset.csv`, prints a summary block, and every number in that
block is checked by an assertion.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
git checkout -b u3-dashboard
pwd
```

Create `stats_engine.py` in your repo. Everything today goes in that one file.

## PART 1 — THE LOADER (15 min)

You have written this parsing pattern three times now. This time it becomes a
function, and it gets a guard.

```python
import csv

COMMENT = "#"

def load(path):
    """Load a data file that has a comment preamble, then a real header.
    Returns a list of dicts. Raises on a file with no data rows."""
    with open(path) as f:
        lines = [ln for ln in f.read().splitlines()
                 if ln.strip() and not ln.strip().startswith(COMMENT)]
    if len(lines) < 2:
        raise ValueError(f"{path}: need a header and at least one data row")
    rows = list(csv.DictReader(lines))
    if not rows:
        raise ValueError(f"{path}: header present but no data rows")
    return rows
```

- Why is the check `len(lines) < 2` and not `== 0`? (Because the header
  itself is a line. A file with only a comment has 0 lines; a file with a
  comment and a header but no data has 1.)
- What does `csv.DictReader` do that `open().read().split(",")` does not?
  (Quoted fields containing commas. Use the clinic file to remind yourself.)

## PART 2 — THE STATISTICS (20 min)

Write these as small, single-purpose functions. Every one takes a list of
numbers and returns a number — none of them touches a file or prints
anything. That is what makes them testable.

```python
def mean(values):
    if not values:
        raise ValueError("mean of empty list")
    return sum(values) / len(values)

def median(values):
    s = sorted(values)
    if not s:
        raise ValueError("median of empty list")
    mid = len(s) // 2
    if len(s) % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2

def percentile(values, p):
    """Linear interpolation, matching the L08 lab and st.quantiles."""
    s = sorted(values)
    if not s:
        raise ValueError("percentile of empty list")
    k = (len(s) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(s) - 1)
    if lo == hi:
        return s[lo]
    return s[lo] + (s[hi] - s[lo]) * (k - lo)

def stdev(values):
    """Population standard deviation."""
    if not values:
        raise ValueError("stdev of empty list")
    m = mean(values)
    return (sum((x - m) ** 2 for x in values) / len(values)) ** 0.5

def five_number(values):
    s = sorted(values)
    return {
        "min": s[0],
        "Q1": percentile(s, 0.25),
        "median": percentile(s, 0.50),
        "Q3": percentile(s, 0.75),
        "max": s[-1],
    }
```

Then, deliberately, one function for the **outlier fence**, because L21 will
need it and because the dashboard should flag extreme values rather than
quietly average them in:

```python
def fence(five):
    """Return (lower, upper) IQR outlier fences from a five-number summary."""
    iqr = five["Q3"] - five["Q1"]
    return five["Q1"] - 1.5 * iqr, five["Q3"] + 1.5 * iqr

def outside_fence(values, five):
    lo, hi = fence(five)
    return [v for v in values if v < lo or v > hi]
```

## PART 3 — THE SUMMARY (15 min)

Now the function the dashboard will actually call. It should take **rows and
a column name**, so it can summarise any column without being rewritten.

```python
def numeric(rows, col):
    """Extract a column as floats, skipping anything non-numeric."""
    out = []
    for r in rows:
        try:
            out.append(float(r[col]))
        except (ValueError, TypeError):
            continue
    return out

def summarise(rows, col):
    """Five-number summary + spread + outliers for one numeric column."""
    values = numeric(rows, col)
    if not values:
        raise ValueError(f"no numeric values in {col}")
    five = five_number(values)
    lo, hi = fence(five)
    return {
        "column": col,
        "n": len(values),
        "mean": mean(values),
        "median": five["median"],
        "min": five["min"],
        "max": five["max"],
        "stdev": stdev(values),
        "iqr": five["Q3"] - five["Q1"],
        "fences": (lo, hi),
        "outliers": outside_fence(values, five),
        "skew": "right" if five["Q3"] - five["median"] > five["median"] - five["Q1"] else "left/flat",
    }

def group_summary(rows, col, by):
    """Summarise col for each value of by, in a stable order."""
    groups = {}
    for r in rows:
        groups.setdefault(r[by], []).append(r)
    return {key: summarise(grp, col) for key, grp in sorted(groups.items())}
```

Run it on the project data and **write the output in your notes**:

```python
rows = load("/tmp/u3_datasets/u3_project_dataset.csv")
print(f"{len(rows)} members, {len(rows[0])} columns\n")

for col in ("Age", "Monthly_Visits", "Spend_USD"):
    s = summarise(rows, col)
    print(f"== {col} ==")
    print(f"   n={s['n']} mean={s['mean']:.2f} median={s['median']:.2f}")
    print(f"   min={s['min']:.2f} max={s['max']:.2f} stdev={s['stdev']:.2f}")
    print(f"   IQR={s['iqr']:.2f} fences=({s['fences'][0]:.2f}, {s['fences'][1]:.2f})")
    print(f"   outliers={s['outliers']}  skew={s['skew']}")
```

### The fence is loud. That is expected.

Run the code above and you will see that the fence flags **14** values in
`Spend_USD` as outliers, not the 3 you were expecting. Before you go looking
for a bug, check this is right:

- The `Spend_USD` distribution is strongly right-skewed. Its upper fence is
  **490.48** while the max is **18,500.00** — the fence sits far below the
  tail because the middle 50% of members spend very little.
- With a skewed dataset the IQR fence flags the whole upper tail, not just
  the extreme values. `Monthly_Visits` does the same thing: fence at 8.50,
  and all **12** members with 9 visits get flagged, even though 9 visits is
  not remarkable, just uncommon.
- `Age` has **0** outliers, and its fence even runs below zero at −4.50.

**Do not "fix" this by loosening the fence.** Write in your notes which
column's outlier list you would actually trust, and one sentence on why a
rule tuned for symmetric data behaves badly on skewed data. L21 comes back
to this.

## PART 4 — ASSERT YOUR ENGINE (20 min)

This is the part that separates a working program from a *reliable* one. A
test that asserts is a claim you can check. Print the real expected values
from the run above, then write assertions for them.

```python
def test_engine():
    # known-answer tests on tiny inputs you can verify by eye
    assert mean([1, 2, 3, 4]) == 2.5
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 2, 3]) == 2
    assert percentile([1, 2, 3, 4], 0.5) == 2.5
    assert stdev([2, 4, 4, 4, 5, 5, 7, 9]) == 2.0   # the classic worked example
    five = five_number([4, 7, 9, 12, 15, 19, 22, 26, 31, 38, 44, 55])
    assert five["median"] == 20.5
    lo, hi = fence(five)
    assert lo == -21.0 and hi == 65.0

    # error paths: the engine must complain, not return None silently
    for bad in ([], [1, "x", "y"]):
        try:
            mean(numeric([{"c": v} for v in bad], "c"))
        except ValueError:
            pass
        else:
            raise AssertionError("mean() should have raised on no numeric values")

    print("all engine tests passed")

test_engine()
```

Then add **three assertions of your own** based on the real project data —
one for `Spend_USD`, one for `Age`, one that checks an outlier is detected.
Use the printed values.

**Answer in your notes:** why is `median([1,2,3,4])` returning `2.5` correct
even though `2.5` is not in the list? When is that acceptable, and when would
it be wrong to report it?

## PART 5 — LOOK AHEAD (5 min)

Tomorrow you build `privacy_filter.py`. It will import `load` and
`summarise` from this file. Write down **one** thing your engine is missing
that the filter will need — something that would force you to rewrite
`summarise` if you noticed it too late.

## PART 6 — SAVE + PUSH (last 10 min)

```bash
git add stats_engine.py
git commit -m "U3 L14 stats engine: load, summarise, group, fence, with assertions"
git push -u origin u3-dashboard
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `stats_engine.py`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Your push message must include:

1. the mean and median of `Spend_USD`
2. how many outliers the fence found in `Spend_USD` (and whether you agree
   that count is meaningful)
3. confirmation that `test_engine()` printed "all engine tests passed"

If your push message does not contain all three, your submission is
incomplete. Keep the terminal open — spot-checks.
