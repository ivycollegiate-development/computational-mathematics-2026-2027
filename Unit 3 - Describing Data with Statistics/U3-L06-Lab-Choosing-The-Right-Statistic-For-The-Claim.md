# U3 L06 — Lab: Choosing the Right Statistic for the Claim

**LO:** pick the statistic that fits a claim, and state plainly what your choice hides.

You now have five statistics and every one of them lies in a different way.
Today is the skill that matters most in real life: given a sentence someone
wants to say, decide which numbers can honestly support it — and name what
you are choosing not to show.

Today's dataset is employee wages, and the question is a real one someone
will actually ask you.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

The wage file has a comment line, a header, then 120 employees. Note it
contains **quoted fields** — `"Jordan, Haddad"`-style names appear in a
sibling file — so read it with `csv`, never with `split(",")`.

```python
import csv
import statistics as st

with open("/tmp/u3_datasets/u3_wage_comparison.csv") as f:
    lines = [ln for ln in f.read().splitlines() if not ln.strip().startswith("#")]

rows = list(csv.DictReader(lines))
print(len(rows), "employees")
print(rows[0])
```

Two job families, 60 people each: **Analyst** and **Coordinator**.

## PART 1 — THE CLAIM UNDER TEST (10 min)

Someone writes this memo:

> *Our data shows the Analyst role is substantially more
> well-compensated than the Coordinator role. The average Analyst earns
> about $93,000 versus $65,000 for Coordinators — a gap of roughly $28,000,
> which we consider decisive.*

Their number is the **mean**. Before you judge it, do this: compute the same
claim with every statistic you own.

```python
def wages(family):
    return [int(r["Annual_USD"]) for r in rows if r["Job_Family"] == family]

analyst = wages("Analyst")
coord   = wages("Coordinator")

for label, vals in (("Analyst", analyst), ("Coordinator", coord)):
    print(f"{label:<12} n={len(vals)} mean={st.mean(vals):>10.2f} "
          f"median={st.median(vals):>10.2f} "
          f"range={max(vals)-min(vals):>9.2f} "
          f"stdev={st.pstdev(vals):>9.2f}")
```

In your notes:

| Statistic | Analyst | Coordinator | The gap |
|---|---|---|---|
| mean | | | |
| median | | | |
| min | | | |
| max | | | |
| 25th percentile | | | |

- The mean gap is **27,471.50**. The median gap is **16,641.00**. The memo
  calls its gap "decisive." Is the mean gap or the median gap the better
  description of the typical difference between the roles?
- By how much does the mean gap **overstate** the median gap? (It is about
  1.65x.) Why does the mean gap exceed the median gap here? (Hint: look at
  the largest salaries before you answer.)

## PART 2 — FIND THE REASON (10 min)

```python
print("Analyst  top 6:", sorted(analyst)[-6:])
print("Coord    top 6:", sorted(coord)[-6:])
print("Analyst  over 200k:", sum(1 for v in analyst if v > 200000))
print("Coord    over 200k:", sum(1 for v in coord if v > 200000))
print("Analyst  under 200k top:", sorted([v for v in analyst if v <= 200000])[-3:])
```

In your notes:

- Look at the Analyst top 6: four values sit at roughly 310,000–328,000, then
  a **cliff** down to 94,073. That is not a smooth distribution — it is 4
  people and then 56 others.
- The Coordinator top 6 has the same shape, smaller: two values near
  203,902–212,989, then a cliff to 92,028.
- The memo's claim rests almost entirely on those **six people** out of 120.
  Restate the claim honestly: is "Analysts earn more" true? Is "the typical
  Analyst earns $28,000 more" true?
- Now check the medians. **Do the two families overlap heavily?** Compare
  `max(coordinator)` and `max(analyst)` to the other family's median. What
  does that overlap say about how much a *specific* person could earn
  without the memo's story being true of them?

## PART 3 — THE RANGE AND STANDARD DEVIATION (10 min)

From your Part 1 table:

- Which statistic in that table is largest for Analyst, and why does that
  tell you almost nothing about a typical Analyst?
- The standard deviation is **61,434.75** for Analyst — two thirds of a mean
  of 92,862.77. Write the sentence: *"the typical Analyst salary is not a
  number, it is a number plus or minus nearly as much."* That is the honest
  form of any average salary claim.
- Would you report the range in the memo? Explain in one sentence what
  range says and what it hides.

## PART 4 — BUILD THE HONEST MEMO (15 min)

Now write two memos. Real sentences, in your notes.

**Memo A — the mean version.** Keep the mean gap and the word "average."
It is not a lie, but:

- Add one sentence naming what the average conceals.
- Add one sentence a skeptical reader should demand before you act on it.

**Memo B — the honest version.** Use the median, and report the spread
alongside it.

- What is the honest headline number?
- What additional number makes the comparison trustworthy, and why that one?
- What can Memo B *no longer* claim that Memo A could? (Something is
  always lost by choosing robust statistics. Name it.)

## PART 5 — THE RULES YOU WILL USE (10 min)

Write these four rules in your notebook. They govern every number you
publish for the rest of this unit:

1. **Match the statistic to the claim.** "Average pay" means the mean.
   "Typical pay" means the median. "How much does it vary" means the
   standard deviation. Never let a word imply a statistic you did not use.
2. **Report the spread with the center.** A number alone is half an answer.
3. **Show the extremes when they drive the result.** If six values out of
   120 create the headline, say so.
4. **Prefer the robust measure when extremes are untrustworthy or
   uninformative.** One bad record should not be able to move your report.

Then apply rule 1 to a sentence of your own choosing — take a statistic you
have seen in the news, and rewrite it so the verb and the number agree.

## PART 6 — LOOK AHEAD: THE U3 L07 PAPER CHECK

Next lesson is a paper check on everything so far — centers and spread, by
hand, closed notes. Part 1's table is the most likely question, so know your
four numbers cold: mean, median, min, max for both families.

## PART 7 — SAVE + PUSH (last 10 min)

```bash
git add memo_wages.md
git commit -m "U3 L06 statistic choice and honest memo for the wage claim"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `memo_wages.md`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Include these four numbers in the push message so I can spot-check:

1. mean Analyst
2. median Analyst
3. mean gap minus median gap
4. how many employees earn over 200,000 in total

Keep the terminal open — spot-checks.
