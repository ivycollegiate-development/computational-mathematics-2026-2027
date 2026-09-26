# U3 L08 — Lab: Percentiles and the Five-Number Summary

**LO:** compute percentiles, quartiles, and the five-number summary, and describe a distribution's shape and spread from five numbers.

The mean and median each give you one number about the middle. Percentiles
give you the whole shape. Today you build a five-number description of a
dataset and learn that **five numbers can be enough to describe hundreds** —
if you know how to read them.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

```python
import csv
import statistics as st

with open("/tmp/u3_datasets/u3_survey_times.csv") as f:
    lines = [ln for ln in f.read().splitlines() if not ln.strip().startswith("#")]

rows = list(csv.DictReader(lines))
waits = sorted(int(r["Wait_Minutes"]) for r in rows)
n = len(waits)
print(f"{n} responses, min {waits[0]}, max {waits[-1]}")
```

## PART 1 — WHAT A PERCENTILE MEANS (10 min)

**Read this carefully: the 90th percentile is the value that 90% of the data
is at or below.** It is a *position in the data*, not a percentage of the
maximum. Say it back to yourself: the 90th percentile of wait times is the
wait time that 90% of patients did not exceed.

- Which is bigger, the 10th or the 90th percentile? Why must it be?
- If a percentile is a value, and we have 240 values sorted, where does the
  90th percentile sit? (Not exactly on a value — compute it.)

## PART 2 — COMPUTE IT YOURSELF (15 min)

There are several percentile methods, and they disagree slightly. We use the
**linear interpolation** method, which is also what `numpy.percentile` and
Excel's `PERCENTILE` do. It uses a fractional index:

```python
def percentile(values, p):
    """Linear interpolation between the two nearest ranks.
    p is a fraction: 0.25 for the 25th percentile, 0.90 for the 90th."""
    s = sorted(values)
    k = (len(s) - 1) * p
    low = int(k)
    high = min(low + 1, len(s) - 1)
    if low == high:
        return s[low]
    return s[low] + (s[high] - s[low]) * (k - low)

for p in (0.10, 0.25, 0.50, 0.75, 0.90):
    print(f"  p{int(p*100):>3}: {percentile(waits, p):>6.2f}")
```

In your notes:

- The correct answers are: p10 = **4.00**, p25 = **7.00**, p50 = **11.00**,
  p75 = **15.00**, p90 = **18.00**. Compare yours against these before you go
  on — and if p50 is not 11.00, find your bug first.
- Why does p50 come out to the median? (Look at the formula: at p=0.5 with
  an even count, it averages the two middle values — exactly the median.)
- **Q1, Q2, Q3 are just p25, p50, p75.** Confirm that Q1 and Q3 from this
  function match the values in yesterday's paper check method as closely as
  you can get by hand. Which agreement do you have to be careful about, and
  why? (There is no single right answer for quartiles on a small dataset.)

## PART 3 — THE FIVE-NUMBER SUMMARY (10 min)

The five-number summary is: **minimum, Q1, median, Q3, maximum.** It is a
complete shape description in five numbers.

```python
five = [min(waits), percentile(waits, 0.25), percentile(waits, 0.50),
        percentile(waits, 0.75), max(waits)]
labels = ["min", "Q1", "median", "Q3", "max"]
for lab, val in zip(labels, five):
    print(f"{lab:<7}{val:>7.2f}")
iqr = five[3] - five[1]
print(f"IQR = {iqr:.2f}")
print(f"upper fence = {five[3] + 1.5*iqr:.2f}")
print(f"lower fence = {five[1] - 1.5*iqr:.2f}")
```

In your notes:

- The five numbers are: ______ and the IQR is ______.
- The fences are around ______ and ______. Is **26** (the max) beyond the
  upper fence? (No.) So the 26-minute wait is **not** an outlier by the IQR
  rule — it is the tail of a normal-ish dataset. Contrast with the donations
  file, where the 90,000 was 159x past its fence.
- Why is the IQR the *robust* measure of spread, and the range the fragile
  one? (Answer it in terms of "how many values does it depend on.")

## PART 4 — READING SHAPE FROM FIVE NUMBERS (10 min)

The five numbers also tell you the **shape** of the distribution.

- If `Q1 to median` ≈ `median to Q3`, the middle half is roughly symmetric.
- If `Q3 to max` >> `Q1 to min`, the right (high) tail is **longer** — the
  data is **right-skewed**.

Compute these and answer:

```python
lower_half = five[2] - five[1]      # median - Q1
upper_half = five[3] - five[2]      # Q3 - median
tails = five[4] - five[3], five[1] - five[0]
print(f"median-Q1={lower_half:.2f}  Q3-median={upper_half:.2f}")
print(f"Q3-to-max={tails[0]:.2f}  min-to-Q1={tails[1]:.2f}")
```

- Is the middle half symmetric? (Q1→median is 4.00 and median→Q3 is 4.00 —
  yes.)
- Are the tails symmetric? (Q3→max is 11.00 but min→Q1 is 5.00 — **no**.)
- So what is the shape of wait times? Write it in one sentence: *"wait times
  are ________-skewed because ________."*
- Now do the same for the **donations** from L05, and confirm it is
  right-skewed. This is a Unit 3 pattern: most real-world data is
  right-skewed, because a small number of people have extreme values.

## PART 5 — HOW THE SUMMARY COMPARES DATASETS (10 min)

This is what five numbers are *for*. Compare the two waits distributions by
counter and by day.

```python
from collections import Counter

for day in ("Mon", "Tue", "Wed", "Thu", "Fri"):
    vals = sorted(int(r["Wait_Minutes"]) for r in rows if r["Day_Of_Week"] == day)
    if vals:
        f = [min(vals), percentile(vals, 0.25), percentile(vals, 0.50),
             percentile(vals, 0.75), max(vals)]
        print(f"{day}: min={f[0]:>3} Q1={f[1]:>6.2f} med={f[2]:>6.2f} "
              f"Q3={f[3]:>6.2f} max={f[4]:>3}")
```

- Do any two days look meaningfully different? Is the spread within days
  bigger or smaller than the spread across all five days?
- **The real lesson:** a single overall five-number summary *hides* the
  per-day variation. In the project dashboard you must decide whether to
  show the whole, the parts, or both — and now you know what each choice
  costs.

## PART 6 — LOOK AHEAD: THE U3 L09 LAB

Next lesson: misleading statistics and the truncated axis. You now have
everything needed to spot the most common dishonest chart in the world — and
to see why the five-number summary is often the *best* defense against it.

## PART 7 — SAVE + PUSH (last 10 min)

```bash
git add percentiles.py
git commit -m "U3 L08 percentiles, five-number summary, and distribution shape"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `percentiles.py`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Include these four numbers in the push message so I can spot-check:

1. the 25th percentile of wait times
2. the median wait (p50)
3. the IQR
4. the upper outlier fence

Keep the terminal open — spot-checks.
