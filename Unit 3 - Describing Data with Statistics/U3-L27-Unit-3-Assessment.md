# U3 L27 — Unit 3 Assessment (Paper)

**Unit:** 3 — Describing Data with Statistics
**Type:** Paper (closed-book assessment, 50 minutes)
**LO:** demonstrate mastery of Unit 3: centers, spread, percentiles, outliers, misleading stats, PII/anonymization

---

## TODAY'S PURPOSE

The Unit 3 assessment. 50 points, 35 minutes, closed book, no computer. Everything on this paper is something we built or debugged together in Unit 3.

---

## PART 1 — BEFORE YOU START (5 min)

Put everything away except a pen or pencil. On the cover of your paper, write:
- your name
- one thing from Unit 3 you feel confident about
- one thing you hope is NOT on the test (be honest — it won't change the test, but it tells me where to spend review time in Unit 4)

Then close your notes. Deep breath. You have seen every problem type below.

---

## PART 2 — WRITTEN ASSESSMENT (35 min)

**50 points. Show work for partial credit.**

### SECTION A — CENTERS & SPREAD (15 points)

**A1.** Dataset (11 values): `12, 15, 14, 13, 16, 14, 15, 14, 13, 14, 200`
- Mean = ______
- Median = ______
- Mode = ______
- Which measure of center is most honest for this dataset? Why? ______

**A2.** Same dataset. Range = ______, Variance = ______, StdDev = ______.
- The stddev is 56.2. The range is 188. What does the stddev tell you that the range doesn't? (One sentence) ______

**A3.** Two datasets, both n=10:
- Set X: mean=50, stddev=2
- Set Y: mean=50, stddev=15
A process spec requires output between 45 and 55. Which set meets spec? Why? ______

### SECTION B — PERCENTILES & OUTLIERS (15 points)

**B1.** 21 values sorted. Your `percentile(v, p)` uses `k = (n-1)*p`, linear interpolation.
For `p=0.25`, `n=21`: `k = ______`. `lo = ______`, `hi = ______`.
If `v[5]=12` and `v[6]=14`, the 25th percentile = ______.

**B2.** Five-number summary: `min=2, q1=5, median=8, q3=12, max=25`.
- IQR = ______
- Lower fence = ______
- Upper fence = ______
- Outliers: ______ (list any values outside fences)

**B3.** You drop the outliers from B2. Which of the five numbers change? Which do not? Why? ______

### SECTION C — MISLEADING STATISTICS & PII (10 points)

**C1.** A report states: "Average response time = 1.2 seconds." The data: `[0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 50.0]`.
- Is the mean 1.2? ______
- What is the median? ______
- What one word describes the effect of the 50.0 on the mean? ______
- What should the report have said instead? ______

**C2.** A dataset has columns: `student_id`, `birthdate`, `gender`, `grade`, `zipcode`.
- Which column(s) are direct identifiers? ______
- Which column(s) are quasi-identifiers? ______
- You generalize `zipcode` to first 3 digits and suppress `birthdate` to `YYYY` only. Is this k-anonymity for k=5? Explain in one sentence. ______

### SECTION D — WRITE CODE (10 points)

**D1.** Write the function `five_number(v)` that takes a list of numbers and returns a tuple `(min, q1, median, q3, max)` using your `(n-1)*p` interpolation convention. No imports except `math` if needed.

```python
def five_number(v):
    # your code here
```

---

## PART 3 — GRADE RELEASE WALKTHROUGH (10 min, after assessment)

We go over the answer key together. For every problem you mark **not yet**, write one sentence: *what specifically confused me?*

---

## TURN IN

**The assessment paper** — handed to me before you leave. Name on every page.

---

## 📋 TOMORROW

**Next:** U3 L28 — Assessment Walkthrough & Reflection. We grade together, then you reflect.

---

## 🇹🇼 TAIWAN CONTEXT

This assessment mirrors the kinds of questions on Taiwan's information security certification: given a dataset with an outlier, which statistic do you report? Given a table with quasi-identifiers, what generalization achieves k-anonymity? The math is the same; the stakes are higher.