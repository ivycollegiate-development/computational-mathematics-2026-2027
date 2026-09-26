# U3 L09 — Lab: Misleading Statistics and the Truncated Axis

**LO:** identify the specific statistical choice that makes a claim misleading, and construct an honest alternative.

Unit 2 you learned what makes a good visualization. Now you have statistics,
and that is dangerous in a new way: **you can now choose a statistic that
makes a true-sounding claim come out the way you wanted.** Today you practice
both sides — spotting the cheat, and then doing it deliberately so you can
recognize it in the wild.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

```python
import csv
import statistics as st

with open("/tmp/u3_datasets/u3_wage_comparison.csv") as f:
    lines = [ln for ln in f.read().splitlines() if not ln.strip().startswith("#")]
rows = list(csv.DictReader(lines))

def wages(family):
    return sorted(int(r["Annual_USD"]) for r in rows if r["Job_Family"] == family)

analyst = wages("Analyst")
coord   = wages("Coordinator")
print("loaded", len(analyst), len(coord))
```

## PART 1 — THE HONEST VERSION FIRST (10 min)

Before you learn to cheat, establish the truth:

```python
for label, v in (("Analyst", analyst), ("Coordinator", coord)):
    print(f"{label:<12} mean={st.mean(v):>10.2f} median={st.median(v):>10.2f} "
          f"min={min(v):>9.2f} max={max(v):>9.2f}")
```

```text
Analyst       mean  92862.77  median  78467.50
Coordinator   mean  65391.27  median  61826.50
```

The honest claim: *Analysts are paid more than Coordinators.* Both means and
both medians agree, so that claim is safe. Note how much the mean and median
differ **within** each group (Analyst: 92,863 vs 78,468 — a 14,000 gap)
even though both support the same conclusion. Keep that in mind.

## PART 2 — FOUR WAYS TO MISLEAD, ALL WITH TRUE DATA (20 min)

Each of these is a real technique used in real arguments. For each one, write
the sentence a dishonest person would produce, and then the honest version.

**A. Pick the flattering statistic.**

```python
print(f"mean gap:   {st.mean(analyst) - st.mean(coord):.2f}")
print(f"median gap: {st.median(analyst) - st.median(coord):.2f}")
```

The mean gap is **27,471.50**; the median gap is **16,641.00**. Which one
would you use to make "Analysts earn much more" sound strongest? Neither is
a lie. Why is the gap between the two gaps a problem for the reader, and not
for you?

**B. Truncate the axis.**

```python
# The same 60 Analyst salaries, y-axis starting at 80,000
truncated = [v for v in analyst if v >= 80000]
print(f"Analysts at or above 80,000: {len(truncated)} of {len(analyst)}")
print(f"their range: {max(truncated) - min(truncated):.2f}")
print(f"full range:  {max(analyst) - min(analyst):.2f}")
```

Draw two bar charts of Analyst salaries, one y-axis from **0** and one from
**80,000**. On the truncated version, four salaries above 300,000 look like a
gentle slope. On the honest version, they are spikes. Same data. Which one
would make you argue for a raise? Which one is truthful about spread?

The rule you are learning: **a bar chart's baseline must be zero.** A *line*
chart of a time series may use a nonzero baseline, but bars encode length,
and length is meaningless without a zero.

**C. Cherry-pick the time window or subgroup.**

```python
exp = [int(r["Years_Experience"]) for r in rows if r["Job_Family"] == "Analyst"]
west = [int(r["Annual_USD"]) for r in rows
        if r["Job_Family"] == "Analyst" and r["Region"] == "West"]
print(f"Analysts in West: n={len(west)} mean={st.mean(west):.2f}")
print(f"All Analysts:     n={len(analyst)} mean={st.mean(analyst):.2f}")
```

Report only the West-region number, and don't mention the other regions. Is
it a lie? What makes it misleading? (Hint: the *omission* is the
misleading part, not the number.)

**D. Let one value do the work.**

```python
print(f"Analyst mean with    top earner: {st.mean(analyst):.2f}")
trimmed = analyst[:-1]
print(f"Analyst mean without top earner: {st.mean(trimmed):.2f}")
print(f"difference: {st.mean(analyst) - st.mean(trimmed):.2f}")
```

Removing the single highest earner drops the Analyst mean from **92,862.77**
to **88,873.44** — about 4,000 dollars, 4.3%. That sounds small, but it is
the *top* person removed; four analysts sit above 300,000. Now remove all four:

```python
body = [v for v in analyst if v <= 200000]
print(f"mean of the other {len(body)}: {st.mean(body):.2f}")
print(f"median of the other {len(body)}: {st.median(body):.2f}")
```

The mean falls to **76,700.21** — a drop of **16,162.55**, or **17.4%**, from
removing just 4 people out of 60. The median over those same 56 people is
**77,570.00**, barely different from the 78,467.50 median of all 60. That is
the whole unit in one comparison: a handful of people can move the mean, and
essentially nothing can move the median.

## PART 3 — THE FIVE-NUMBER DEFENSE (10 min)

The five-number summary from L08 is the best defense against all four tricks,
because it shows spread without being destroyed by one value.

```python
def percentile(values, p):
    s = sorted(values)
    k = (len(s) - 1) * p
    lo = int(k); hi = min(lo + 1, len(s) - 1)
    return s[lo] if lo == hi else s[lo] + (s[hi] - s[lo]) * (k - lo)

for label, v in (("Analyst", analyst), ("Coordinator", coord)):
    print(f"{label:<12} min={min(v):>9.2f} Q1={percentile(v,.25):>9.2f} "
          f"med={percentile(v,.50):>9.2f} Q3={percentile(v,.75):>9.2f} "
          f"max={max(v):>9.2f}")
```

In your notes:

- Compare the Analyst `median` to the Coordinator `max`. The median Analyst
  is **78,467.50**; the highest-paid Coordinator is **212,989.00**. The two
  groups **overlap enormously**. What does that overlap do to the
  "Analysts earn more" claim, if you are honest about it?
- Which trick from Part 2 would a five-number summary make hardest to pull
  off, and why? (Think about the *max* in a five-number summary — is it a
  gift to the deceiver or a check on them?)

## PART 4 — REBUILD THE CLAIM HONESTLY (15 min)

Write `honest_wages.md` in your repo with a short memo that survives
scrutiny. It must contain:

1. The headline claim, in one sentence, with the **median** gap and not the
   mean gap.
2. The five-number summary for both groups.
3. One sentence on the **overlap** between the groups — because omitting it
   is itself a form of misleading.
4. One sentence naming the sample size and where the data came from.
5. A **limitations** section: two things this data cannot tell you. (Ideas:
   experience, region, job level, or whether the six high earners are
   outliers or a real senior tier.)

Then, in a second section titled "What I deliberately did not do," list the
Part 2 tricks you declined to use, one line each. This section is worth
more than the memo.

## PART 5 — THE ETHICS, IN ONE PARAGRAPH (10 min)

Answer in your notes: *A statistic is technically accurate but is used to
deceive. Is that lying?* Give a reason, and say who is responsible — the
person who runs the analysis, the person who publishes the chart, or the
reader. Be specific. There is no single right answer, but a vague one will
earn a zero.

## PART 6 — SAVE + PUSH (last 10 min)

```bash
git add honest_wages.md
git commit -m "U3 L09 honest wage memo, with limitations and rejected tricks"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `honest_wages.md`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Include these three numbers in the push message:

1. the mean gap between families
2. the median gap between families
3. the highest-paid Coordinator's salary

Keep the terminal open — spot-checks.
