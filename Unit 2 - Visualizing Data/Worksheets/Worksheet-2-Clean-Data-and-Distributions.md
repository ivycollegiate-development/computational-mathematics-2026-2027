# Unit 2: Visualizing Data — Worksheet 2

**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part A: Scatter Plot Relationships

For each pair of columns from our datasets, predict the relationship you expect (positive / negative / none) and which chart type you would use to check it:

| Columns | Predicted relationship | Chart type |
|---------|------------------------|-----------|
| `Study_Hours` vs `Test_Score` (dataset1) | | |
| `Sleep_Hours` vs `Test_Score` (dataset1) | | |
| `Stress_Level` vs `GPA` (dataset2) | | |
| `Hours_Exercise` vs `GPA` (dataset2) | | |
| `Extracurricular_Hours` vs `GPA` (dataset3) | | |

## Part B: Reading a Histogram

A histogram of `login_success_rate` over 60 days shows: most days bunched between 0.92 and 0.98, a small bar at 0.85–0.88, and one day down at 0.71.

**6.** What is the most common range of login success rates? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**7.** The day at 0.71 is called an **outlier**. Before you flag it to the security team, what two things should you check in the raw data?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**8.** If you chose only 3 bins for this histogram, what would you lose? What if you chose 200 bins?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part C: Missing Data Decisions

**9.** You load `u2_dataset1_study_habits.csv` and find 3 of the 52 rows have an empty `Sleep_Hours`. For each option below, write when it is the right choice and what it costs you:

| Option | When is it right? | What it costs |
|--------|-------------------|---------------|
| Delete the row | | |
| Fill in a guess | | |
| Leave it and let the chart show the gap | | |

**10.** Why is "fill in a guess" almost always the worst option for a security or research chart?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part D: Write the Code

**11.** Write code that loads `data/u2_dataset2_mental_health.csv`, skips rows with a missing `GPA`, and makes a scatter plot of `Hours_Exercise` (x) vs `GPA` (y) with all four chart elements. Save it as `exercise_gpa.png`:

```
# Your code here:

```

**12.** Write code that computes the average `GPA` for students with `Stress_Level` above 5 and below 5, and prints both averages:

```
# Your code here:

```

## Part E: Find the Bug

**13.**
```python
scores = []
for row in reader:
    scores.append(row["Test_Score"])
avg = sum(scores) / len(scores)
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**14.**
```python
plt.hist(success_rates, bins=10)
plt.savefig("hist.png")
plt.title("Login Success Rate")
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Checkout (before you leave)

Answer these to earn your exit check. **No notes — from memory.**

1. On a scatter plot, what does a positive relationship look like? What would `Stress_Level` vs `GPA` likely look like?
2. You find a row with a missing value. Name the two honest options for handling it.
3. Why does bin count change what a histogram seems to say?
4. In one sentence: why must cleaning happen before charting, not after?

---
**Teacher note:** Checkout is graded pass/fail (2 of 4 correct = pass). Record in the class tracker.
*Keep this for the Visualizing Threats project reference.*
