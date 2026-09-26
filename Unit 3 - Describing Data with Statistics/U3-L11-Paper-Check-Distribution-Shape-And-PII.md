# U3 L11 — Paper Check: Distribution Shape and PII

**LO:** compute percentiles by hand, describe distribution shape, and classify data as identifying or safe — then defend a publication decision.

**Closed notes. Paper only. No laptop.** Show your arithmetic; a bare
answer is not evidence. Every part below is checkable, so check your own work
before you hand it in. Total 50 points.

## PART 1 — PERCENTILES BY HAND (15 pts)

The dataset is a 12-row list of monthly wait times:

```text
  4   7   9  12  15  19  22  26  31  38  44  55
```

Use the linear-interpolation method from L08: with a sorted list of length
*n*, the percentile at fraction *p* sits at index *k* = (*n* − 1) × *p*. Take
the two neighbouring values and interpolate.

1. *n* = 12. For p25, k = 11 × 0.25 = ______
2. p25 = ______ (show the two values you used and the fraction between them)
3. p50 = ______
4. For p75, k = 11 × 0.75 = ______
5. p75 = ______
6. IQR = Q3 − Q1 = ______
7. Upper fence = Q3 + 1.5 × IQR = ______
8. Lower fence = Q1 − 1.5 × IQR = ______
9. Are **any** of the 12 values beyond a fence? List them, or write "none."
10. Is the distribution left-skewed, right-skewed, or roughly symmetric? Show
    the comparison that decides it: Q3−Q2 = ______ versus Q2−Q1 = ______, and
    the tails: max−Q3 = ______ versus Q1−min = ______.

## PART 2 — HAND-COMPUTED SPREAD (10 pts)

Compute the mean of the same 12 values, then the population standard
deviation. Show one line of work.

11. mean = ______ (sum ÷ 12; your sum = ______)
12. variance = ______ (mean of the 12 squared deviations)
13. standard deviation = ______ (square root, to 2 decimal places)
14. Is the standard deviation bigger or smaller than the IQR from Part 1?
    (Careful — the answer is **not** what most people expect. Your sd is
    about 15.21 and your IQR is 21.50, so the sd is **smaller**.)
    Both are in minutes, but they answer different questions: the sd is a
    typical distance from the mean, while the IQR is the width of the middle
    half. Explain in one sentence why a single enormous value inflates the sd
    but cannot inflate the IQR.

## PART 3 — CLASSIFY THE COLUMNS (15 pts)

A members' table has these columns. For each, mark **D** (direct identifier),
**Q** (quasi-identifier), **S** (sensitive), or **N** (non-identifying), and
justify in a few words.

| Column | D / Q / S / N | Why |
|---|---|---|
| `Member_ID` | | |
| `First_Name` | | |
| `Last_Name` | | |
| `Age` | | |
| `City` | | |
| `Zip_Code` | | |
| `Monthly_Visits` | | |
| `Spend_USD` | | |
| `Membership_Tier` | | |

15. Two of these columns are dangerous *only in combination*. Name the pair
    and explain in one sentence what the combination reveals that neither
    column reveals alone.

## PART 4 — THE PUBLICATION DECISION (10 pts)

A colleague wants to publish a chart of **average spend by membership tier**.
The file contains 120 members, 4 tiers, 30 members each.

16. Should this chart be published? Your answer must be **yes**, **no**, or
    **yes with conditions** — and if the conditions, state exactly what
    changes before publication.
17. The **Basic** tier has 30 members. The total of their `Spend_USD` values
    is **19,440.75**, and one single member in that tier has **18,500.00** of
    it.
    a. Average spend for the Basic tier = 19,440.75 ÷ 30 = ______
    b. The average of the other 29 Basic members = ______
       (subtract first, then divide by 29)
    c. A draft chart shows Basic with the *highest* average spend of all four
       tiers. In two or three sentences, explain why that is true and why it
       is misleading. Your answer should mention the difference between the
       member in (a) and the *typical* member.
18. Name **one** change to the chart that would make it honest, and say which
    statistic or display you would use instead.

## TURN IN

Hand in this paper at the end of the period. Marked out of 50.

Show all working. If you are unsure, write down what you tried — partial
method with a wrong number scores higher than a right number with no method.
