# U3 L15 — Project Lab 2: The Privacy Filter

**LO:** implement the gate that blocks publication, and prove it blocks by feeding it data that must not be published.

You specified the requirements in L10. You measured what anonymization costs
in L12. Yesterday you built the engine. Today you build the thing that
decides whether anything gets published at all.

This is the most important file in the project. The dashboard is disposable —
it can be rewritten. **A filter that fails open leaks every member in the
dataset.**

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
git checkout u3-dashboard
```

Create `privacy_filter.py`. It will import from yesterday's file:

```python
from stats_engine import load, summarise, numeric
```

**Definition of done for today:** the filter blocks all three unsafe datasets
you will be given, and allows exactly one safe transformation — and you can
demonstrate both with output, not with claims.

## PART 1 — THE RULES (15 min)

Start with the vocabulary. These are sets of **column names**, not values, so
they work on any dataset.

```python
DIRECT_IDENTIFIERS = {
    "Member_ID", "First_Name", "Last_Name", "Name", "Patient_ID",
}
QUASI_IDENTIFIERS = {
    "Age", "Zip_Code", "City", "Signup_Date", "Visit_Date",
}
SENSITIVE = {"Membership_Tier", "Condition", "Insurance_Plan"}

MIN_K = 5
```

Note what `DIRECT_IDENTIFIERS` is: names, plus **codes**. `Member_ID` is
"M2001", not a name, and it is a perfect identifier. A rule that only
catches names catches nothing.

## PART 2 — CHECK ONE: IDENTIFIERS (15 min)

```python
def check_identifiers(rows):
    """Return a list of problems. Empty list means this check passed."""
    present = set(rows[0].keys())
    problems = []
    for col in sorted(DIRECT_IDENTIFIERS & present):
        problems.append(f"direct identifier present: {col!r}")
    quasi = sorted(QUASI_IDENTIFIERS & present)
    return problems, quasi
```

- Why return **two** things instead of one? (Because "there is a problem" and
  "here are the columns to think about" are different outputs, and the caller
  needs both.)
- Why sort the columns? (So the error message is deterministic. A filter whose
  output order changes run to run is impossible to test.)

```python
rows = load("/tmp/u3_datasets/u3_project_dataset.csv")
problems, quasi = check_identifiers(rows)
print("problems:", problems)
print("quasi-identifiers to handle:", quasi)
```

This reports **`Member_ID`, `First_Name`, and `Last_Name`**. All three must
be gone before publication.

## PART 3 — CHECK TWO: K-ANONYMITY (20 min)

The k check is the heart of it. From L12 you know that `Age + Zip_Code` is
unique for all 120 members.

```python
from collections import Counter

def k_value(rows, fields):
    """Smallest group size over the given fields. 0 if rows is empty."""
    if not rows:
        return 0
    return min(Counter(tuple(r[f] for f in fields) for r in rows).values())

def check_k(rows, published_fields, min_k=MIN_K):
    if not published_fields:
        return []
    k = k_value(rows, published_fields)
    if k >= min_k:
        return []
    counts = Counter(tuple(r[f] for f in published_fields) for r in rows)
    singles = [k_ for k_, c in counts.items() if c == 1]
    return [f"k={k} over {published_fields} is below k>={min_k}: "
            f"{len(singles)} individually identifiable rows"]

for fields in (["Age"], ["Age", "Zip_Code"], ["City"], ["Membership_Tier"],
               ["Age", "City", "Membership_Tier"]):
    probs = check_k(rows, fields)
    print(f"{str(fields):<40} {'PASS' if not probs else 'BLOCK'}")
    for p in probs:
        print("    ", p)
```

Answer in your notes:

1. Which of those five pass, and which block?
2. `Age` alone: 45 distinct ages, 13 of them unique to one person. Does it
   pass or block? (It **blocks** — k = 1.)
3. Why does `City` pass while `Age` does not, when both are "just a location
   or a number"? (Group sizes, not semantics. Five cities means twenty-plus
   people each.)

## PART 4 — CHECK THREE: SMALL CELLS (15 min)

Even a passing k check can leave one chart with a group of one. The k check
asks about *rows*; this asks about the *published groups*.

```python
def check_small_cells(rows, group_col, min_k=MIN_K):
    counts = Counter(r[group_col] for r in rows)
    return [f"small cell: {group_col}={name!r} has only {c} row(s)"
            for name, c in sorted(counts.items()) if c < min_k]
```

Test it against a grouping that must fail. The `Zip_Code` grouping from L12:

```python
print("zip cells:", check_small_cells(rows, "Zip_Code")[:3], "...")
print("city cells:", check_small_cells(rows, "City"))
print("tier cells:", check_small_cells(rows, "Membership_Tier"))
```

- `Zip_Code` produces a huge list of problems. `City` and `Membership_Tier`
  produce **none**.
- **Answer:** the project will group by `City` and `Membership_Tier` for its
  charts. Does that mean those groupings are safe? (Not by itself — the small
  cell check is a *floor*, and the k check is the one that catches
  combinations. You need both.)

## PART 5 — THE GATE (20 min)

Now combine. This is the function the dashboard calls **before** drawing
anything.

> **Where the code goes.** Every `def` and constant below belongs in
> `privacy_filter.py`. Every block from here on that *loads data and prints
> output* is a **demo** — put those in a separate `demo_gate.py`, inside a
> `if __name__ == "__main__":` guard.
>
> This is not tidiness. If a demo lives inside `privacy_filter.py`, then
> anyone who writes `from privacy_filter import privacy_gate` — which is
> exactly what `dashboard.py` does in L17 — runs your demos as a side
> effect. Their dashboard prints forty lines of your debugging before it
> draws anything, and if a demo raises, their chart never renders and the
> traceback points at the wrong file entirely. You will hit this. Separate
> them now and you will not debug it at 9pm on a Friday.

```python
def privacy_gate(rows, published_fields, group_cols, min_k=MIN_K):
    """Return (ok, problems, warnings).

    ok is False when ANY problem is found -- a warning alone does not block,
    but a warning is still reported so the report can mention it.
    The caller MUST NOT draw a chart when ok is False."""
    problems = []
    warnings = []
    if not rows:
        return False, ["no rows to publish"], []

    id_problems, quasi = check_identifiers(rows)
    problems.extend(id_problems)

    problems.extend(check_k(rows, published_fields, min_k))

    for col in group_cols:
        problems.extend(check_small_cells(rows, col, min_k))

    if quasi:
        warnings.append(
            f"quasi-identifiers still published: {quasi} -- "
            f"state in the report how each is generalised"
        )
    return (not problems), problems, warnings


def describe_result(ok, problems, warnings):
    if ok:
        out = ["Privacy check PASSED. Safe to publish."]
        for w in warnings:
            out.append(f"  note: {w}")
        return "\n".join(out)
    lines = ["Privacy check FAILED. Nothing will be published.", ""]
    lines += [f"  - {p}" for p in problems]
    lines += ["", "Fix the data or the report fields, then try again."]
    return "\n".join(lines)
```

Now the part that makes this real — **the fail-closed demo**. A gate that
nobody has watched block something is a gate nobody trusts.

```python
def anonymize(rows, age_width=15):
    out = []
    for r in rows:
        new = {k: v for k, v in r.items()
               if k not in ("First_Name", "Last_Name", "Member_ID",
                            "Zip_Code", "Signup_Date")}
        a = int(new["Age"]); lo = a // age_width * age_width
        new["Age"] = f"{lo}-{lo + age_width - 1}"
        out.append(new)
    return out

safe = anonymize(rows)
print("surviving columns:", list(safe[0].keys()))
print("k(Age band) =", k_value(safe, ["Age"]))          # 15
print("k(Age band + City) =", k_value(safe, ["Age", "City"]))  # 1 -- read this

ok, probs, warns = privacy_gate(safe, ["Age"], ["City", "Membership_Tier"])
print(describe_result(ok, probs, warns))
```

**Stop and read that output before moving on.** Two things happened, and only
one of them was expected.

`k(Age band)` alone is **15** — the 15-year band passes cleanly. But
`k(Age band + City)` is **1**: adding the city back on puts you right back
where you started. Try every band width and **no** width ever fixes it:

| age band | k (Age alone) | k (Age + City) | people still unique |
|---|---|---|---|
| 5-year | 3 | 1 | 17 |
| 10-year | 3 | 1 | 6 |
| 15-year | **15** | 1 | 2 |
| 25-year | **16** | 1 | 1 |
| 30-year | **15** | 1 | 2 |

**Generalizing the age does not fix this.** Banding harder reduces the
unique count from 17 to 1, but k = 1 means *somebody is still alone*, which
is exactly what k-anonymity forbids. One stubborn member in a thin corner of
the data defeats every age band you can pick.

This is the central design decision of your project, so do not paper over it.
**You cannot publish `Age` and `City` together at k ≥ 5.** Your filter must
choose one of these:

- publish the age band, drop the city from the identifying fields (the
  chart may still *group* by city — that is what the chart draws, not what
  identifies a person);
- publish the city, drop age;
- suppress the few offending rows so the remainder reaches k ≥ 5, and say in
  your report exactly how many rows you deleted to get there.

The code above takes the first option: `published_fields` is `["Age"]`, and
the small-cell check still covers `City` because the chart groups by it. The
gate passes.

Then prove the failure path, using the raw data:

```python
ok, probs, warns = privacy_gate(rows, ["Age", "Zip_Code"], ["Zip_Code"])
print(describe_result(ok, probs, warns))
```

Record both outputs in your notes. The second **must** block, and it must
name `First_Name`, `Last_Name`, `Member_ID`, the k failure, and a page of
small-cell failures — one for nearly every zip code in the file.

**And prove a third case that almost nobody gets right:** run the gate on the
*filtered* rows but with `["Age", "City"]` as the published fields.

```python
ok, probs, warns = privacy_gate(safe, ["Age", "City"], ["City", "Membership_Tier"])
print(describe_result(ok, probs, warns))
```

This blocks, even though you removed every name and banded every age. The
reason is the table above. A filter that only checks "are the names gone"
would have passed this dataset. Yours does not, because it checks the
*combination*.

**Answer in your notes:** why does `privacy_gate` return three values
instead of just `ok`? What would break if it returned only a boolean?

Then a second question, and this one has a trap. The gate also returns
`warnings`, and a warning does **not** set `ok` to False. Why?

Because a quasi-identifier that has been *generalised* is not a failure — it
is the thing you are supposed to be doing. `Age` after banding is a warning
("tell the report how you generalised it"), not a block. If you make
warnings block, then **no anonymized dataset can ever pass your filter**, and
the project is dead on arrival.

Try it: make `warnings` block, run the safe case, and watch a correctly
anonymized dataset get rejected. Then put it back. Knowing which failures
are fatal and which are notes is the whole job.

## PART 6 — THE WIRING (10 min)

Write the entry point that a dashboard will actually run. Note the order:
**gate first, then draw.**

```python
def publish(rows, draw):
    ok, probs, warns = privacy_gate(rows, ["Age"], ["City", "Membership_Tier"])
    if not ok:
        print(describe_result(ok, probs, warns))
        return False
    draw(rows)
    return True

# The call the dashboard will make:
# publish(filtered_rows, draw_all_charts)
```

- `draw` is a function you pass in. Why pass a function instead of calling a
  `draw_all_charts()` directly?
- Draw the control flow on paper: which box comes first, and what is the
  **only** path from "gate fails" to "no chart"? Is there any code path where
  a chart is drawn while `ok` is False? Prove it.

## PART 7 — SAVE + PUSH (last 10 min)

```bash
git add privacy_filter.py
git commit -m "U3 L15 privacy filter: identifier, k-anonymity, and small-cell gates, fail-closed"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `privacy_filter.py`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Your push message must include all four:

1. the three problems reported on the **raw** dataset
2. the k value the filtered dataset achieves over `["Age"]`
3. confirmation the safe dataset **passed**
4. confirmation the raw dataset **blocked**
5. one sentence naming the combination that blocks even after the names are
   gone (this is the question that separates a working filter from a
   checklist)

If any of the four is missing, the submission is incomplete — especially #4.

Keep the terminal open — spot-checks.
