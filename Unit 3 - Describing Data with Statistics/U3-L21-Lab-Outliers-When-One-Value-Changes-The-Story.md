# U3 L21 — Lab: Outliers — When One Value Changes the Story

**LO:** find outliers with a defensible method, decide whether removing them is honest, and say which statistics survive the removal.

Every previous lab assumed one thing: the data is mostly the same. Today we
stop assuming, and we deal with the values that are not.

## PART 0 — GET THE DATA (5 min)

```bash
mkdir -p /tmp/u3_datasets
cp /tmp/lab-data/u3_project_dataset.csv /tmp/u3_datasets/
```

```python
import csv
import math

def load(path):
    lines = open(path).read().splitlines()
    lines = [l for l in lines if l.strip() and not l.startswith("#")]
    return list(csv.DictReader(lines))

def numeric(rows, col):
    out = []
    for r in rows:
        try:
            out.append(float(r[col]))
        except (ValueError, KeyError):
            pass
    return out
```

## PART 1 — BUILD THE FENCE (15 min)

```python
def percentile(values, p):
    s = sorted(values)
    k = (len(s) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(s) - 1)
    if lo == hi:
        return s[lo]
    return s[lo] + (s[hi] - s[lo]) * (k - lo)

def five_number(values):
    return {
        "min":  min(values),
        "q1":   percentile(values, 0.25),
        "median": percentile(values, 0.50),
        "q3":   percentile(values, 0.75),
        "max":  max(values),
    }

def iqr_fences(values):
    f = five_number(values)
    iqr = f["q3"] - f["q1"]
    return f, f["q1"] - 1.5 * iqr, f["q3"] + 1.5 * iqr

def outliers(values):
    f, lo, hi = iqr_fences(values)
    return [v for v in values if v < lo or v > hi]
```

This is the same `percentile` you wrote in U3 L08 and U3 L14. Reuse is the
point — one implementation, tested once.

Now run it on the three numeric columns and **write the actual output here**:

```python
rows = load("/tmp/u3_datasets/u3_project_dataset.csv")

for col in ["Age", "Monthly_Visits", "Spend_USD"]:
    v = numeric(rows, col)
    f, lo, hi = iqr_fences(v)
    print(f"{col:15} n={len(v)} median={f['median']:.2f} IQR={f['q3']-f['q1']:.2f} "
          f"fence=({lo:.2f}, {hi:.2f}) outliers={len(outliers(v))}")
```

| column | n | median | IQR | upper fence | # outliers |
|---|---|---|---|---|---|
| Age | | | | | |
| Monthly_Visits | | | | | |
| Spend_USD | | | | | |

**Do not fill this in from expectation. Run it and copy the numbers.**

## PART 2 — THE UNCOMFORTABLE PART (15 min)

Look at the `Monthly_Visits` row. The fence's upper bound is **8.50**, and
there are **12** values flagged — all of them exactly `9`.

Now answer, in writing:

1. Is it plausible that exactly 12 of 120 members visit **9 times a month**,
   and that **none** of the other 108 visit between 9 and 8.5? Describe what
   that dataset is actually shaped like. ______
2. Your IQR rule flagged 12 values as "outliers." The rule is a **symmetric**
   rule — it assumes values spread out roughly evenly around the median. Does
   that assumption hold for `Monthly_Visits`? ______
3. Here is the test. Compare the IQR rule to a rule that is not symmetric —
   one that only looks at the *upper* tail, at **2 standard deviations** above
   the mean:

   ```python
   def stdev_population(values):
       m = sum(values) / len(values)
       return math.sqrt(sum((v - m) ** 2 for v in values) / len(values))

   def high_outliers_2sd(values):
       m = sum(values) / len(values)
       cut = m + 2 * stdev_population(values)
       return [v for v in values if v > cut]

   for col in ["Monthly_Visits", "Spend_USD"]:
       v = numeric(rows, col)
       print(col, "IQR flags:", len(outliers(v)),
             " 2SD-above-mean flags:", len(high_outliers_2sd(v)))
   ```

   Run it and record what you get. Your two rules should disagree — on
   `Monthly_Visits` they will both flag 12, and on `Spend_USD` they will not
   agree at all:

   | column | IQR flags | 2-sd-above-mean flags |
   |---|---|---|
   | Monthly_Visits | | |
   | Spend_USD | | |

   Your `Spend_USD` row is the interesting one. The IQR fence is built from
   the middle half of the data, so one enormous value **inflates q3** and
   **pushes the fence up to swallow its neighbours** — which is why it flags
   fourteen values including perfectly ordinary ones like 510.87 and 544.98.
   The 2-sd rule is anchored to the mean instead, and a single huge value
   drags the mean *and* the standard deviation up together, so it flags only
   the genuinely extreme tail. Neither rule is stupid; one is
   self-referential in a way the other is not.

4. **Neither rule is correct and both are defensible.** In one sentence each,
   say when you would trust the IQR fence and when you would trust the 2-sd
   rule. ______
   (Guidance: IQR is a *shape* rule — it asks "is this far from the middle
   half of the data?" 2-sd is a *spread* rule — it asks "is this far from
   typical, given how much everything else varies?" Neither is a truth test.)
   (Guidance: IQR is a *shape* rule — it asks "is this far from the middle
   half of the data?" 2-sd is a *spread* rule — it asks "is this far from
   typical, given how much everything else varies?" Neither is a truth test.)

## PART 3 — THE REMOVAL PROBLEM (20 min)

`Spend_USD` has one value of `18,500.00` and one of `0.00` in a column whose
median is 94.71. You have now seen what these do to a mean. So: do you remove
them?

**First, measure.** Do not argue about it — get the numbers:

```python
def mean_of(values):  return sum(values) / len(values)

spend = numeric(rows, "Spend_USD")
flagged = outliers(spend)
kept = [v for v in spend if v not in flagged]

print("original   n=%3d  mean=%9.2f  median=%8.2f" % (len(spend),  mean_of(spend),  percentile(spend, 0.5)))
print("flagged    n=%3d  values=%s" % (len(flagged), sorted(flagged)))
print("kept       n=%3d  mean=%9.2f  median=%8.2f" % (len(kept),     mean_of(kept),     percentile(kept, 0.5)))
print("MEAN  moved from %.2f to %.2f  = %.1f%%" % (
    mean_of(spend), mean_of(kept),
    100 * (mean_of(kept) - mean_of(spend)) / mean_of(spend)))
print("MEDIAN moved from %.2f to %.2f  = %.1f%%" % (
    percentile(spend, 0.5), percentile(kept, 0.5),
    100 * (percentile(kept, 0.5) - percentile(spend, 0.5)) / percentile(spend, 0.5)))
```

Record the four outputs. Expect the mean to fall a long way and the median to
move much less, and **check whether that gap is the real lesson of today**:
a rule that flags 14 values and then deletes them has silently deleted a
fourteenth of your dataset. ______

5. Which statistic moved more — the mean or the median? By what factor? ______
6. Here is the rule I want you to use, and it is strict: **you may not delete
   a data point because it makes your chart look better.** You may delete one
   only if you can name an error that put it there — a decimal shifted, a
   duplicate row, a unit mistake. Based only on the numbers in front of you,
   is `18,500.00` an error? ______
7. So what do you do with it? Choose one and defend it:
   - **(a)** Report the median as the headline, keep the outlier, and note the
     14 IQR flags in a footnote.
   - **(b)** Report both, side by side, and label which is which.
   - **(c)** Report the trimmed mean and say what fraction was trimmed.

   Your choice, and the sentence justifying it: ______
8. Now the one that separates a report from a cover-up. In your chosen
   option, could a reader **misread** your result as "the typical member spends
   94.71"? What single sentence in your report prevents that? ______

## PART 4 — YOUR OWN OUTLIER (15 min)

The 18,500.00 was built in on purpose. Find out how:

```bash
cd ~/Projects/computational-mathematics-2026-2027
grep -n "18500" "Unit 3 - Describing Data with Statistics/build_datasets.py"
```

9. How was that value introduced — as a plausible member, or as a deliberate
   anomaly? Paste the relevant line: ______
10. Here is the useful part: **the outlier in `Spend_USD` is real data, not a
    typo.** The donations dataset has a similar value at the other extreme.
    Recall the donation lesson (U3 L02/L03): what was the value, and what was
    the point of including it? ______
11. Finally, a question about your own judgement. You are now able to delete a
    value that ruins your result. Give one concrete situation where a
    reasonable, honest analyst would still be wrong to delete. ______

## TURN IN — OUTLIER REPORT (due 11:59 PM tonight)

A short report, five to eight sentences, plain prose. It must contain:

1. the **IQR fence** for `Spend_USD` and the **count** it flags (14)
2. the **mean before and after** removing the flagged values, from your own run
3. the **median before and after**
4. your answer to question 7 — which option you chose
5. your answer to question 8 — the sentence that stops a misreading
6. one sentence on the situation from question 11 where deletion is the wrong
   call

**Item 6 is the graded one.** Anyone can compute a fence. The question is
whether you know when *not* to use the delete button, and that is the skill
that carries into the statistics-engine lab in U3 L23.

Keep the terminal open — spot-checks.
