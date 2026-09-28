# U3 L16 — Paper Check: Percentiles, PII, and Anonymization

Names: ___________________________  Date: ____

Closed notes. Paper only, no laptop. Show your arithmetic and cite the lesson number for any rule you apply — a right answer with no method does not earn the point. Marked out of 50. Hand this paper in at the end of the period.

## 1: Percentiles by hand (15 pts)

The first 20 rows of the survey file, `Wait_Minutes`:

```text
  9   8  16  13  10   8  22  22   7   6
 14  10  18   8  17   9  15  19   3  15
```

Linear interpolation from U3 L08: for a sorted list of length *n*, the percentile at fraction *p* is at index *k* = (n − 1) × *p*.

1. For p25, k = 19 × 0.25 = ______________
2. The sorted list:

   ____________________________________________________________

3. p25 = ______________ (name the two values and the fraction between them)
4. p50 = ______________
5. For p75, k = 19 × 0.75 = ______________
6. p75 = ______________
7. IQR = p75 − p25 = ______________
8. Upper fence = p75 + 1.5 × IQR = ______________
9. List every value beyond the upper fence. A value can look extreme to your eye and still sit safely inside the fence; write why:

   _____________________________________________________________________

10. The mean of these 20 values is 12.45 and the median is 11.50. The mean is **higher** than the median. In one sentence, why? Point at the specific values that pull it up.

   _____________________________________________________________________

## 2: k-anonymity by hand (15 pts)

`Age` and `Zip` are the only identifying columns that would be published.

```text
 Age  Zip
  22  10001
  22  10001
  31  10001
  31  10002
  45  10002
  45  10002
  19  10003
  19  10003
  19  10003
  67  10004
  67  10004
  22  10004
```

11. Distinct `Age` alone = ______________   Distinct `Zip` alone = ______________
12. Distinct **(Age, Zip)** combinations = ______________
13. k over `["Age", "Zip"]` = ______________
14. Is k over `Age` alone higher, lower, or the same? By how much? ______________
15. Name **one** change to the *published fields* that would raise k over `Age + Zip` to at least 2, and explain in one sentence why it works. Do not propose deleting rows.

   _____________________________________________________________________

## 3: Suppression and generalization (20 pts)

Same 12-member table.

16. Members per `Zip` group:  10001 = __________  10002 = __________  10003 = __________  10004 = __________

17. Apply a suppression rule of **k ≥ 3** to the `Zip` column. Rows surviving = ______________  Now **k ≥ 4**. Rows surviving = ______________

   Which threshold is right, and what do you weigh against the strictness? (U3 L12: a rule that is too strict does not protect anyone, it just deletes the data.)

   _____________________________________________________________________

18. **Generalize** instead: replace `Age` with a 20-year band (0–19, 20–39, 40–59, 60–79) and recompute k over banded `Age` plus `Zip`. Work out each band before you count.

   k = ______________   People individually identifiable = ______________

19. Question 18 is the uncomfortable one.

   a. Did generalization make this dataset safe? ______________________

   b. The identifiable count fell from 3 to 2, but k was 1 before and after. Does reducing the number of exposed people from 3 to 2 count as protecting them?

   _____________________________________________________________________

20. From U3 L12: `Zip3` maps to exactly one `City`, and no age-band width makes `Age + City` reach k ≥ 5. State in one sentence what that tells you about a generalization scheme that *looks* like it is reducing detail.

   _____________________________________________________________________

21. The hardest question on the paper.

   a. A rule says "publish anyway, we only have 2 people at risk out of 12." Give the one-sentence reason that rule is wrong, using the word **k**.

   _____________________________________________________________________

   b. A second rule says "band wider and the problem goes away." Recompute k over (band + `Zip`):

| band width     | k over (band + Zip)     | people still unique     |
| -------------- | ----------------------- | ----------------------- |
| 10             | __________              | __________              |
| 20             | __________              | __________              |
| 40             | __________              | __________              |
| 60             | __________              | __________              |

   Explain in one sentence why a wider band that still gives k = 1 is not an improvement.

   _____________________________________________________________________

   Keep widening until the band covers everyone, e.g. 0–100. Now k passes — and you have published no age information whatsoever. In one sentence, state why that is the trap k sets:

   _____________________________________________________________________

**TURN IN** — this paper at the end of the period, with all working shown and lesson numbers cited.
