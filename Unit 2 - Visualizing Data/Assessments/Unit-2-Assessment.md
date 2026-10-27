# Unit 2 Assessment — Computational Mathematics
**Schedule:** Unit 2 Assessment (Half Day)
**Time:** 35 minutes
**Conditions:** Closed computer. Pen and paper only. No notes, no phone, no neighbors.

Print double-sided. Do not write your name inside the body — write it on the
coversheet only.

Total: 50 points.

---

## COVERSHEET

Before you start, on the cover of your paper write:

- Your name
- One thing from Unit 2 you feel confident about
- One thing you hope is **NOT** on this test

The coversheet is not graded. The third answer is the useful one — it tells me
where to spend review time in Unit 3.

---

## RULES

- Answer in complete sentences where the question asks *why*.
- A value or a word is fine where the question asks *what*.
- **Answer the verb.** "What happens when…" wants the actual error, not the fix.
  "Why" wants a sentence, not a value. Most lost points on this test come from
  answering a different question than the one asked.
- Show your work on every code question. Partial credit is real.
- If you finish early, review. There is no extra credit for finishing fast.

---

## SECTION A — SHORT RESPONSE (10 questions, 2 points each = 20 points)

**1.** Complete the table from memory:

| Chart type | Use when... | x-axis | y-axis | Key function |
|------------|-------------|--------|--------|--------------|
| Line plot  |             |        |        | `plt.plot()` |
| Bar chart  |             |        |        | `plt.bar()`  |
| Scatter plot |           |        |        | `plt.scatter()` |
| Histogram  |             |        |        | `plt.hist()` |

**2.** `plt.plot(x, y, marker="o", linestyle="--", color="steelblue")` — What does each argument change? (One phrase per argument.)

**3.** `plt.bar(categories, values, color=["#c0392b", "#e67e22", "#27ae60"])` — Why pass a *list* of colors instead of one string?

**4.** `plt.scatter(x, y, s=10, alpha=0.4)` — What does `s=` control? What does `alpha=` control? Why use `s=10, alpha=0.4` for 1,000 points but `s=40` for 6 points?

**5.** `plt.hist(data, bins=20, edgecolor="white")` — What does `bins=20` do? What does `edgecolor="white"` do? Why is there no "correct" bin count?

**6.** `plt.figure()` — When do you call it? What happens if you skip it when drawing a second chart in the same script?

**7.** `plt.savefig("file.png", dpi=150, bbox_inches="tight")` — What does `dpi=150` do? What does `bbox_inches="tight"` do? **Critical rule:** `savefig` must come **before** or **after** `plt.show()`?

**8.** `csv.DictReader(f)` — What does it return? What is the type of each row? What is the type of every value inside that row?

**9.** A CSV file starts with `# Mental health survey, GPA on 4.0 scale` as its first line. What happens if you pass this file directly to `csv.DictReader`? Why is this "worse than a crash"?

**10.** **Sanity bounds vs statistical outliers** — Why use sanity bounds (fixed domain rules like `GPA: (0.0, 4.0)`) instead of statistical outliers (e.g., 1.5×IQR)? Give two reasons.

---

## SECTION B — CODE READING (2 problems, 5 points each = 10 points)

*You do not run this code. You read it the way a debugger would.*

### Problem 11

```python
import csv

SANITY = {
    "Age": (10, 22),
    "Overall GPA": (0.0, 4.0),
    "Absence Rate": (0.0, 1.0),
}

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def is_impossible(column, value):
    low, high = SANITY[column]
    return not (low <= value <= high)

with open("data/students.csv", newline="") as f:
    rows = list(csv.DictReader(f))

clean_rows = []
for r in rows:
    drop_reason = None
    for col in SANITY:
        if r[col] == "":
            drop_reason = f"blank {col}"
            break
        val = to_float(r[col])
        if val is None:
            drop_reason = f"unparseable {col}"
            break
        if is_impossible(col, val):
            drop_reason = f"impossible {col}={val}"
            break
        r[col] = val
    if drop_reason:
        print(f"Dropped row: {drop_reason}")
        continue
    clean_rows.append(r)
```

**a.** A row has `"Age": "N/A"`. Trace through the loop: which `if` block triggers, what is printed, and what happens to that row?

**b.** A row has `"Overall GPA": "3.8"` and `"Absence Rate": "1.5"`. Which `if` block triggers, what is printed, and what happens to that row?

**c.** The `assert rows_in == rows_out + rows_dropped` at the end of the full script would catch what bug that a simple `print` would miss?

**d.** Why does `to_float` catch **both** `ValueError` and `TypeError`? Give one input that triggers each.

**e.** The `break` inside each `if` block — what does it do? What would happen if it were missing?

---

### Problem 12

```python
import csv
import matplotlib.pyplot as plt

with open("data/threats_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

dates = [r["date"] for r in rows]
phishing = [r["phishing_reports"] for r in rows]
failed = [r["failed_logins"] for r in rows]

plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, marker="o", label="Phishing reports", alpha=0.7)
plt.plot(dates, failed, marker="s", label="Failed logins", alpha=0.7)
plt.title("Daily Phishing Reports and Failed Logins — Oct 2026")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig("timeline.png", dpi=150)
```

**a.** There is one bug that makes the saved PNG **blank**. Find it and write the corrected line.

**b.** The y-axis starts at a non-zero value. What one line would you add to make it an honest axis?

**c.** The x-axis labels overlap. The code includes `plt.xticks(rotation=45)` — why might they *still* overlap, and what else is needed?

**d.** One sentence: why is bug (a) worse than bug (b)?

**e.** The chart is for a **parent audience**. The current title uses jargon ("Phishing reports"). Rewrite the title for parents.

---

## SECTION C — DATA INTEGRITY & HONESTY (1 problem, 10 points)

Your unit had exactly three integrity principles. Use them.

**13.** You cleaned 1,000 rows down to 947. The dropped rows were disproportionately low-GPA students who left GPA blank.

```python
SANITY = {
    "Overall GPA": (0.0, 4.0),
    "Age": (10, 22),
    "Absence Rate": (0.0, 1.0),
}
```

**a.** Write the one-sentence **provenance statement** you would put in your project `analysis.md`. (3 points)

**b.** In one sentence: why does dropping blank-GPA rows *bias* the average GPA upward? (2 points)

**c.** A histogram of `login_success_rate` shows most days near 0.95, with a thin tail to 0.60. Your partner says "those are outliers, drop them." You say "no, they're the story." Who is right, and why? (2 points)

**d.** A chart of phishing reports by class period could let someone guess *which class* fell for them. What change to the chart fixes this risk? Name the principle. (3 points)

---

## SECTION D — WRITE CODE (1 problem, 10 points)

**14.** Write a function called `load_and_clean(csv_path, sanity_dict)` that:

- reads the CSV at `csv_path` with `csv.DictReader`
- **strips comment lines** (lines starting with `#`) before parsing
- for each column in `sanity_dict`: converts to `float`, drops rows with blank or unparseable values, drops rows where the value is outside the `(low, high)` bounds
- prints each dropped row's reason (e.g., `"Dropped row: blank Overall GPA"`)
- returns the list of cleaned rows (each row is a dict with numeric values as `float`)
- includes the **audit assertion** at the end: `assert rows_in == rows_out + rows_dropped, "Count mismatch"`

You may assume `sanity_dict` maps column names to `(low, high)` tuples. Do not use `eval()`. Do not add features that were not asked for.

Write the whole function.

---

## FINISHING

Turn your paper face down and wait quietly.