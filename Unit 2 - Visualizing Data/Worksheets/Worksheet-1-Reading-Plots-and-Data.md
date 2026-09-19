# Unit 2: Visualizing Data — Worksheet 1

**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part A: Plot Anatomy

For each chart element, write what it does and what happens if you leave it out:

| Element | What it does | If missing, the reader... |
|---------|-------------|--------------------------|
| Title | | |
| X-axis label | | |
| Y-axis label | | |
| Legend | | |
| Units on an axis | | |

## Part B: Chart Type Match

Match each question to the best chart type (line chart, bar chart, histogram):

1. "How did phishing reports change day by day over two months?" → \_\_\_\_\_\_\_\_
2. "How do weekdays compare to weekends on failed logins?" → \_\_\_\_\_\_\_\_
3. "What values of login success rate are most common?" → \_\_\_\_\_\_\_\_
4. "How many days had more than 40 phishing reports?" → \_\_\_\_\_\_\_\_
5. "Which of the three score columns (math, science, English) has the higher average?" → \_\_\_\_\_\_\_\_

## Part C: csv.DictReader Practice

**6.** Given a CSV with columns `Student_ID, Study_Hours, Test_Score, Attendance, Sleep_Hours`, write code that opens `data/u2_dataset1_study_habits.csv` and prints the `Test_Score` of every student who studied more than 10 hours:

```
# Your code here:

```

**7.** What does each row of a `csv.DictReader` loop give you? Circle one:

a) a list of values  b) a dictionary keyed by column name  c) a string  d) a file object

**8.** In `u2_dataset1_study_habits.csv`, line 1 starts with `#`. What will happen if you feed the file straight into `csv.DictReader`, and how do you fix it?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part D: Find the Bug

Each snippet has a bug. Circle the problem and write the fix:

**9.**
```python
import matplotlib.pyplot as plt
plt.plot(dates, scores)
plt.savefig("chart1.png")
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**10.**
```python
plt.plot(dates, phishing_reports)
plt.plot(dates, failed_logins)
plt.savefig("timeline.png")
plt.show()
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**11.**
```python
with open("data/u2_campus_threat_daily.csv") as f:
    rows = list(csv.DictReader(f))
total = sum(row["failed_logins"])
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part E: Reading Plots

**12.** A line chart of daily phishing reports over 60 days shows two sharp spikes on consecutive Thursdays, with flat days in between. In 2-3 sentences, what would you tell the security team — and what would you check in the raw data before you said it?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**13.** Two students chart the same data. One's y-axis runs 0–100; the other's runs 40–50, making a small change look dramatic. Who is being dishonest — or are they? Explain.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Checkout (before you leave)

Answer these to earn your exit check. **No notes — from memory.**

1. What does `csv.DictReader` give you for each row, and how do you reach one value in it?
2. Name the four chart elements every chart you submit must have.
3. Why must `plt.savefig()` come before `plt.show()`?
4. In one sentence: why does the same data need a different chart for different audiences?

---
**Teacher note:** Checkout is graded pass/fail (2 of 4 correct = pass). Record in the class tracker.
*Save this! We'll refer back for the Visualizing Threats project.*
