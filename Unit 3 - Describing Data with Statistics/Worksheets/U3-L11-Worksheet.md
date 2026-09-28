# U3 L11 — Paper Check: Distribution Shape and PII

Names: ___________________________  Date: ____

Closed notes. Paper only, no laptop. Show your arithmetic; a bare answer is not evidence. Marked out of 50. Name the lesson (**U3 L08**, **U3 L10**) for any rule you apply. Hand this sheet in at the end of the period.

## 1: Percentiles by hand (15 pts)

The dataset is a 12-row list of monthly wait times:

```text
  4   7   9  12  15  19  22  26  31  38  44  55
```

Linear interpolation: with a sorted list of length *n*, the percentile at fraction *p* sits at index *k* = (n − 1) × *p*. Name the two bracketing values and the fraction between them.

1. For p25, k = 11 × 0.25 = ______________
2. Bracketing values: ______________ and ______________ at fraction ______________   →  p25 = ______________
3. p50 = ______________
4. For p75, k = 11 × 0.75 = ______________
5. p75 = ______________
6. IQR = Q3 − Q1 = ______________
7. Upper fence = Q3 + 1.5 × IQR = ______________
8. Lower fence = Q1 − 1.5 × IQR = ______________
9. Are **any** of the 12 values beyond a fence? List them, or write "none."
10. Is the distribution left-skewed, right-skewed, or roughly symmetric? Show both comparisons:

   Q3 − Q2 = ______________ versus Q2 − Q1 = ______________

   max − Q3 = ______________ versus Q1 − min = ______________

   Verdict: ______________________

## 2: Hand-computed spread (10 pts)

Same 12 values.

11. Sum = ______________   Mean = sum ÷ 12 = ______________
12. Variance, as the mean of the 12 squared deviations = ______________
13. Standard deviation, square root of that, to 2 decimals = ______________
14. Compare your standard deviation with your IQR from Section 1. Which is larger, and why does one enormous value inflate the sd but not the IQR? Answer in one sentence.

   _____________________________________________________________________

## 3: Classify the columns (15 pts)

A members' table has these columns. Mark each **D** (direct identifier), **Q** (quasi-identifier), **S** (sensitive), or **N** (non-identifying), and justify in a few words.

| Column                | D / Q / S / N     | Why                        |
| --------------------- | ----------------- | -------------------------- |
| `Member_ID`           | __________        | ______________________     |
| `First_Name`          | __________        | ______________________     |
| `Last_Name`           | __________        | ______________________     |
| `Age`                 | __________        | ______________________     |
| `City`                | __________        | ______________________     |
| `Zip_Code`            | __________        | ______________________     |
| `Monthly_Visits`      | __________        | ______________________     |
| `Spend_USD`           | __________        | ______________________     |
| `Membership_Tier`     | __________        | ______________________     |

15. Name the pair of columns that is dangerous *only in combination*, and explain in one sentence what the combination reveals that neither column reveals alone.

   _____________________________________________________________________

## 4: The publication decision (10 pts)

A colleague wants to publish a chart of **average spend by membership tier**. The file contains 120 members, 4 tiers, 30 members each.

16. Should this chart be published? Answer **yes**, **no**, or **yes with conditions** — and if conditions, state exactly what changes before publication.

   _____________________________________________________________________

17. The **Basic** tier has 30 members. The total of their `Spend_USD` values is **19,440.75**, and one single member in that tier has **18,500.00** of it.

   a. Average spend for the Basic tier = 19,440.75 ÷ 30 = ______________

   b. Average of the other 29 Basic members = ______________ (subtract first, then divide by 29)

   c. A draft chart shows Basic with the *highest* average spend of all four tiers. In two or three sentences, explain why that is true and why it is misleading. Name the difference between the member in (a) and the *typical* member.

   _____________________________________________________________________

   _____________________________________________________________________

18. Name **one** change to the chart that would make it honest, and say which statistic or display you would use instead.

   _____________________________________________________________________

**TURN IN** — this paper at the end of the period, with all working shown.
