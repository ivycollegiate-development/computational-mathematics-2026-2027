# U3 L16 — Paper Check: Percentiles, PII, and Anonymization

**LO:** demonstrate on paper the percentile, k-anonymity, and generalization methods from U3 L08, L10, and L12.

**Closed notes. Paper only. No laptop.** Show your arithmetic and cite the
lesson number for any rule you apply. A right answer with no method does not
earn the point. Total 50 points.

## PART 1 — PERCENTILES BY HAND (15 pts)

The first 20 rows of the survey file, `Wait_Minutes` in minutes:

```text
  9   8  16  13  10   8  22  22   7   6
 14  10  18   8  17   9  15  19   3  15
```

Use the L08 linear-interpolation method: for a sorted list of length *n*, the
percentile at fraction *p* is at index *k* = (*n* − 1) × *p*.

1. *n* = 20, so for p25, k = 19 × 0.25 = ______
2. Sort the 20 values. Write the sorted list in your answer.
3. p25 = ______ (name the two values you used and the fraction between them)
4. p50 = ______
5. For p75, k = 19 × 0.75 = ______
6. p75 = ______
7. IQR = p75 − p25 = ______
8. Upper fence = p75 + 1.5 × IQR = ______
9. List every value that falls **beyond** the upper fence. (Careful — the
   answer is **none of them**, even though the 22s are more than double the
   p25. Your upper fence should land somewhere near 28, which is *above*
   every value in the list. Work out why a value can look extreme to your eye
   and still sit safely inside the fence.)
10. The mean of these 20 values is 12.45 and the median is 11.50. The mean is
    **higher** than the median. In one sentence, why? Point at the specific
    values that pull it up.

## PART 2 — k-ANONYMITY BY HAND (15 pts)

A table of 12 members has these rows. `Age` and `Zip` are the only
identifying columns that would be published.

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

11. Count the distinct values of `Age` alone, and of `Zip` alone.
    Age: ______  Zip: ______
12. Count the distinct **(Age, Zip)** **combinations**. There are 12 rows, so
    there are at most 12 combinations. The number is ______
13. What is the **k** of this table over `["Age", "Zip"]`?
    k = ______
14. Is the k over `Age` alone higher, lower, or the same as over
    `["Age", "Zip"]`? By how much? ______
15. Name **one** change to the *published fields* that would raise k over
    `Age + Zip` to at least 2, and explain in one sentence why dropping
    `Zip` works. (Do not propose deleting rows — the L12 lesson showed what
    that does.)

## PART 3 — SUPPRESSION AND GENERALIZATION (20 pts)

This is the same 12-member table.

16. Count the members in each `Zip` group:
    10001 = ______,  10002 = ______,  10003 = ______,  10004 = ______
17. You apply a suppression rule of **k ≥ 3** to the `Zip` column. How many
    rows survive? ______ Now apply a stricter **k ≥ 4**. How many survive
    now? ______
    Which threshold is right, and what is the thing you have to weigh
    against the strictness? (U3 L12: a rule that is too strict does not
    protect anyone, it just deletes the data.)
18. Now **generalize** instead: replace `Age` with a **20-year** band and
    recompute k over the banded `Age` **plus** `Zip`. Your bands are
    0–19, 20–39, 40–59, 60–79 — work out which band each age falls in before
    you count. Give k = ______ and the number of individually identifiable
    people = ______
19. Question 18 is the interesting one, and the answer is uncomfortable.
    Your k from **13** (over `Age + Zip`) was 1, with **3** people
    individually identifiable — the three rows that are the only member of
    their (age, zip) pair. Your k from **18** (over a 20-year band + `Zip`)
    is also 1, with **2** people identifiable.
    a. In one or two sentences: did generalization make this dataset
       **safe**? ______
    b. The number of identifiable people fell from 3 to 2, so it made some
       improvement. But k = 1 before and after. Does reducing the number of
       exposed people from 3 to 2 count as protecting them? ______
20. From U3 L12: `Zip3` (the 3-digit prefix) maps to exactly one `City`, and
    no age-band width makes `Age + City` reach k ≥ 5. State in one sentence
    what that tells you about a generalization scheme that *looks* like it
    is reducing detail. ______
21. One more, and this is the hardest question on the paper. In Part 3 you
    banded ages and the identifiable count went **down** (3 → 2), but k stayed
    at 1. Suppose you had a rule that said "publish anyway, we only have 2
    people at risk out of 12." Give the one-sentence reason that rule is
    wrong, using the word **k**. ______
    A second rule is equally tempting: "band wider and the problem goes
    away." Recompute k over (band + `Zip`) for 10-, 20-, 40-, and 60-year
    bands. Fill this in — you should find k = 1 at **every** one:

    | band width | k over (band + Zip) | people still unique |
    |---|---|---|
    | 10 | | |
    | 20 | | |
    | 40 | | |
    | 60 | | |

    So widening the band does not fix the problem — it just moves *which*
    people are exposed. Explain in one sentence why a wider band that still
    gives k = 1 is not an improvement, even though the band is less
    detailed. ______
    (Keep going until the band is so wide it covers everyone, e.g. 0–100.
    Now k passes — and you have published no age information whatsoever.
    That is the trap: you can always make k = 5 by deleting all the
    information. k is a floor, not a goal.)

## TURN IN

Hand in this paper at the end of the period. Marked out of 50.

Every rule you use should be traceable: name the lesson (**U3 L08**, **U3
L10**, or **U3 L12**) when you apply one. If you cannot remember whether
suppression is applied per column or per row, write down what you tried and
where you got stuck — a stated uncertainty tells me what to reteach, and a
blank tells me nothing.
