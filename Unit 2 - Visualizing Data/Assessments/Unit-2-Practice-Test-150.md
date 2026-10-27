# Unit 2 Practice Test (150% Review Version) — Computational Mathematics

**Time:** 50 minutes (1.5× the real test)
**Conditions:** Closed computer. Pen and paper only. No notes, no phone, no neighbors.

This is an **oversize review version** — 150% of the real test length. Use it to find your gaps.
The real test will be 50 points, 35 minutes, with DIFFERENT questions (zero overlap).

Total: 75 points.

---

## COVERSHEET

Before you start, on the cover of your paper write:

- Your name
- One thing from Unit 2 you feel confident about
- One thing you hope is **NOT** on the test

---

## RULES

- Answer in complete sentences where the question asks *why*.
- A value or a word is fine where the question asks *what*.
- **Answer the verb.** "What happens when…" wants the actual error, not the fix.
- Show your work on every code question. Partial credit is real.
- If you finish early, review. There is no extra credit for finishing fast.

---

## SECTION A — SHORT RESPONSE (15 questions, 2 points each = 30 points)

**1.** Complete the table from memory:

| Chart type | Use when... | x-axis | y-axis | Key function |
|------------|-------------|--------|--------|--------------|
| Line plot  |             |        |        | `plt.plot()` |
| Bar chart  |             |        |        | `plt.bar()`  |
| Scatter plot |           |        |        | `plt.scatter()` |
| Histogram  |             |        |        | `plt.hist()` |

**2.** `plt.plot(x, y, marker="o", linestyle="--", color="steelblue")` — What does each argument change?

**3.** `plt.bar(categories, values, color=["#c0392b", "#e67e22", "#27ae60"])` — Why pass a list of colors?

**4.** `plt.scatter(x, y, s=10, alpha=0.4)` — What does `s=` control? What does `alpha=` control? Why use `s=10, alpha=0.4` for 1,000 points but `s=40` for 6 points?

**5.** `plt.hist(data, bins=20, edgecolor="white")` — What does `bins=20` do? What does `edgecolor="white"` do? Why is there no "correct" bin count?

**6.** `plt.figure()` — When do you call it? What happens if you skip it when drawing a second chart?

**7.** `plt.savefig("file.png", dpi=150, bbox_inches="tight")` — What does `dpi=150` do? What does `bbox_inches="tight"` do? **Critical rule:** `savefig` must come **before** or **after** `plt.show()`?

**8.** `csv.DictReader(f)` — What does it return? What is the type of each row? What is the type of every value inside that row?

**9.** A CSV file starts with `# Mental health survey, GPA on 4.0 scale` as its first line. What happens if you pass this file directly to `csv.DictReader`? Why is this "worse than a crash"?

**10.** **Sanity bounds vs statistical outliers** — Why use sanity bounds instead of 1.5×IQR? Give two reasons.

**11.** `plt.legend()` — What must each plotted element have for the legend to show it? What happens if you omit `label=` on one series?

**12.** `plt.grid(True, alpha=0.3)` — What does `alpha=0.3` change? Why not `alpha=1.0`?

**13.** `plt.clf()` — What does it do? In the histogram lesson, why is it called inside the loop over bin counts?

**14.** **Three relationship types** a scatter plot can show (name all three).

**15.** In a scatter with `alpha=0.4`, what does a **darker region of dots** mean?

---

## SECTION B — CODE READING (3 problems, 5 points each = 15 points)

### Problem 16

```python
import csv

SANITY = {
    "Age": (10, 22),
    "Overall GPA": (0.0, 4.0),
    "Hours Studied": (0, 60),
}

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

with open("data/students.csv", newline="") as f:
    rows = list(csv.DictReader(f))

clean_rows = []
dropped = {"blank": 0, "impossible": 0, "unparseable": 0}

for r in rows:
    drop_reason = None
    for col in SANITY:
        if r[col] == "":
            drop_reason = f"blank {col}"
            dropped["blank"] += 1
            break
        val = to_float(r[col])
        if val is None:
            drop_reason = f"unparseable {col}"
            dropped["unparseable"] += 1
            break
        low, high = SANITY[col]
        if not (low <= val <= high):
            drop_reason = f"impossible {col}={val}"
            dropped["impossible"] += 1
            break
        r[col] = val
    if drop_reason:
        print(f"Dropped row: {drop_reason}")
        continue
    clean_rows.append(r)

rows_in = len(rows)
rows_out = len(clean_rows)
rows_dropped = sum(dropped.values())
assert rows_in == rows_out + rows_dropped, "Count mismatch"
```

**a.** A row has `"Age": "fifteen"`. Trace: which `if` triggers, what prints, what happens to the row?

**b.** A row has `"Overall GPA": "4.5"`. Trace: which `if` triggers, what prints, what happens?

**c.** The `dropped` dict has three keys. Why is `rows_dropped = sum(dropped.values())` correct here but `rows_dropped = rows_in - rows_out` would also work? What would it mean if they disagreed?

**d.** Why does the `break` belong in *each* `if` block? What bug would appear if the second `if` (unparseable) had no `break`?

**e.** The `assert` at the end — what specific logic bug would it catch that the `print` statements would not?

---

### Problem 17

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

**a.** Bug: saved PNG is blank. Fix it (one line change).

**b.** Y-axis doesn't start at 0. One line to fix.

**c.** X-axis labels still overlap after `rotation=45`. Two fixes (one already in code, one missing).

**d.** Title uses "Phishing reports" — rewrite for a **parent audience**.

**e.** The `alpha=0.7` on both lines — why is transparency useful when plotting two lines on the same axes?

---

### Problem 18

```python
import csv

with open("data/survey.csv", newline="") as f:
    rows = list(csv.DictReader(f))

# Student writes this to compute average GPA:
gpas = [float(r["Overall GPA"]) for r in rows]
avg = sum(gpas) / len(gpas)
print("Average GPA:", avg)
```

**a.** This crashes on a blank GPA cell. What exception? Why does the crash happen?

**b.** The fix uses `to_float` with `try/except`. Why catch **both** `ValueError` and `TypeError`?

**c.** Even after fixing the crash, the average is wrong if low-GPA students leave GPA blank. Why? What is the name of this bias?

**d.** Write the one-sentence **provenance statement** for: 1,000 rows → 947 clean, 53 dropped (31 blank GPA, 12 impossible Absence Rate, 10 unparseable Age).

**e.** A histogram of `login_success_rate` has a thin tail to 0.60. Partner says "drop outliers." You say "they're the story." Who is right? Why?

---

## SECTION C — DATA INTEGRITY & HONESTY (2 problems, 10 points each = 20 points)

### Problem 19

You cleaned a dataset. For each scenario, name the **principle** and the **fix**.

**a.** A bar chart of phishing reports by class period lets someone guess which class fell for them.
   - Principle: ________________________________________
   - Fix: ________________________________________

**b.** Your histogram shows days with login success rate below 0.75. You name the exact dates in your write-up.
   - Principle: ________________________________________
   - Fix: ________________________________________

**c.** You dropped 50 rows with blank GPA. The cleaned average GPA is 3.4; the true population average is 2.9.
   - Principle: ________________________________________
   - Fix: ________________________________________

**d.** A scatter plot of study hours vs GPA shows a correlation. You conclude "studying more causes higher GPA."
   - Principle: ________________________________________
   - Fix: ________________________________________

**e.** Your y-axis starts at 85 instead of 0. A 5% difference looks like a 50% difference.
   - Principle: ________________________________________
   - Fix: ________________________________________

---

### Problem 20

**Histogram vocabulary** — match each term to its definition:

| Term | Definition |
|------|------------|
| Center | |
| Spread | |
| Skew | |
| Outlier | |

A. Where the bulk of the bars sit (the "typical" value)
B. How wide the bars range from lowest to highest
C. A long tail on one side (right-skewed = tail right)
D. An isolated bar far from the rest

**Right-skewed absence rates** — most students near 0.05, thin tail to 0.4.
- What does this mean in real-world words?
- What happens to mean vs median?

---

## SECTION D — WRITE CODE (2 problems, 5 points each = 10 points)

### Problem 21

Write a function `make_histogram(data, bins, title, xlabel, ylabel, filename)` that:
- creates a new figure
- plots a histogram of `data` with the given `bins`
- sets title, x-label, y-label
- adds white edgecolor on bars
- saves to `filename` with `dpi=150, bbox_inches="tight"`
- calls `plt.clf()` after saving
- does **not** call `plt.show()`

### Problem 22

Write a function `load_csv_strip_comments(csv_path)` that:
- opens the file at `csv_path`
- strips lines starting with `#`
- returns `list(csv.DictReader(...))` on the stripped lines

---

## FINISHING

Turn your paper face down. When done, compare your answers to the key and mark every problem **got it** or **not yet**. For each **not yet**, write one sentence: what specifically confused you? This is your study list for the real test.