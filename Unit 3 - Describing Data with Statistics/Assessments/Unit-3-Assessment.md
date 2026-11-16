# Unit 3 Assessment (Paper)

**Unit:** 3 — Describing Data with Statistics
**Type:** Paper, closed-book, no computer
**Time:** 45 minutes
**Points:** 50
**Status:** NOT SCHEDULED. Retained as source for the Unit 3 section of the Jan 18-21 cumulative midterm. Not a standalone paper day in 2026-27.
**Version:** v2, 16 November 2026 — rebalanced. Hand computation 30 → 20 points; statistical judgement and privacy 10 → 20 points. Raw values added to B so the outlier item is answerable; the stated standard deviation corrected.

**LO:** demonstrate mastery of Unit 3 — centres, spread, percentiles, outliers, misleading statistics, and the privacy decisions that govern what a dataset may be used to say.

---

## COVERSHEET

Name: ______________________________

One thing from Unit 3 you feel confident about: ______________________________

One thing you hope is NOT on this test: ______________________________

(This does not change the test. It tells me where to spend Unit 4 review time.)

---

## TODAY'S PURPOSE

50 points. Everything on this paper is something we built, broke, or debugged together in Unit 3. Sections A and B are the arithmetic you have done by hand four times. Sections C and D are the part that matters outside this room: which number you are allowed to report, and what you must refuse to publish.

Put everything away except a pen or pencil.

---

## SECTION A — CENTRES & SPREAD (10 points)

**A1. (4 pts)** Dataset, n = 11: `12, 15, 14, 13, 16, 14, 15, 14, 13, 14, 200`
- Mean = ______
- Median = ______
- Mode = ______
- Which measure of centre is most honest for this dataset, and why? ______

**A2. (3 pts)** Same dataset.
- Range = ______
- Variance = ______
- Standard deviation = ______

Use the sample convention (divide by n − 1). State it on your paper.

**A3. (3 pts)** Two production lines, both n = 10:
- Line X: mean = 50, sd = 2
- Line Y: mean = 50, sd = 15

The process spec requires output between 45 and 55. Which line meets spec, and why? ______

---

## SECTION B — PERCENTILES & OUTLIERS (10 points)

**B1. (4 pts)** Your `percentile(v, p)` uses `k = (n−1)·p` with linear interpolation. For n = 21, p = 0.25:
- `k` = ______
- `lo` = ______
- `hi` = ______
- If `v[5] = 12` and `v[6] = 14`, the 25th percentile = ______

**B2. (3 pts)** Dataset, n = 11, sorted:

`2, 3, 4, 6, 7, 8, 9, 11, 13, 14, 25`

- Five-number summary = ______
- IQR = ______
- Lower fence = ______
- Upper fence = ______
- Outliers = ______

**B3. (3 pts)** Drop the outlier from B2. For each of the five numbers, say whether it changes, and give its new value.

| | changes? | new value |
|---|---|---|
| min | | |
| q1 | | |
| median | | |
| q3 | | |
| max | | |

- One sentence: why did the min survive and the others not? ______

---

## SECTION C — MISLEADING STATISTICS & PRIVACY (20 points)

**C1. (5 pts)** A report states: "Average response time = 1.2 seconds." The data:
`0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 50.0`
- Is the mean 1.2? ______
- What is the median? ______
- What one word describes the effect of 50.0 on the mean? ______
- What should the report have said instead? ______

**C2. (5 pts)** A table has columns: `student_id, birthdate, gender, grade, zipcode`.
- Direct identifier(s): ______
- Quasi-identifier(s): ______
- You generalise `zipcode` to its first 3 digits and `birthdate` to year only. Is the resulting table k-anonymous for k = 5? Answer yes or no, then explain in one sentence. ______

**C3. (5 pts)** This table has already been generalised to two quasi-identifiers. Each row is one person.

| zip3 | birth decade |
|---|---|
| 404 | 1980s |
| 404 | 1980s |
| 404 | 1990s |
| 404 | 1990s |
| 404 | 1990s |
| 406 | 1980s |
| 406 | 1990s |
| 406 | 1990s |
| 406 | 1990s |
| 406 | 1990s |
| 407 | 1980s |
| 407 | 1980s |

- List every equivalence class and its size: ______
- Is this table k-anonymous for k = 3? ______
- Name the smallest generalisation that would make it k = 5, and give the new class sizes: ______

**C4. (5 pts)** The principal asks you to publish, on the school website, *average absence days by grade and by home district*. Your privacy filter refuses to publish any group smaller than 5. There are 12 students in all; district 407 has 11 of them spread across three grades.
- What will you actually publish? ______
- Which rule are you applying, and where did it come from? ______
- Write the two-sentence reply to the principal. It must state plainly what you will not publish, and offer an alternative. ______

---

## SECTION D — WRITE CODE (10 points)

**D1. (10 pts)** Write `five_number(v)` — takes a list of numbers, returns the tuple `(min, q1, median, q3, max)` using the `(n−1)·p` interpolation convention. No imports except `math` if needed. It must not modify the caller's list, and it must not crash on a single-element list.

```python
def five_number(v):
    pass  # your code here
```

---

## TURN IN

The assessment paper, handed in before you leave. Name on every page.
