# Unit 2 Practice Test (Real-Size, Version B) — Computational Mathematics

**Time:** 35 minutes
**Conditions:** Closed computer. Pen and paper only. No notes, no phone, no neighbors.

This is a **practice version** — same size as the real test (50 points), but with **ZERO question overlap**.
Use it as a final dress rehearsal.

Total: 50 points.

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

## SECTION A — SHORT RESPONSE (10 questions, 2 points each = 20 points)

**1.** Match each chart type to its use case (draw lines):

| Chart Type | Use Case |
|------------|----------|
| Line plot | A. Distribution of ONE numeric variable |
| Bar chart | B. Two numeric variables, looking for relationship |
| Scatter plot | C. Continuous/sequential x (time, ordered categories) |
| Histogram | D. Categorical x |

**2.** `plt.scatter(x, y, s=50, alpha=0.6, c="red")` — What does each argument do?
- `s=50`:
- `alpha=0.6`:
- `c="red"`:

**3.** `plt.bar(["Mon","Tue","Wed"], [10,15,8], width=0.6, edgecolor="black")` — What does `width=0.6` do? What does `edgecolor="black"` do?

**4.** `plt.plot(dates, values, marker="o")` — The x-axis labels overlap. You add `plt.xticks(rotation=45)` but they still overlap. What **second** fix is needed?

**5.** `plt.savefig("chart.png", dpi=300, bbox_inches="tight")` vs `plt.savefig("chart.png")` — What two things do the extra arguments change?

**6.** `csv.writer(f)` vs `csv.DictWriter(f, fieldnames)` — When do we use `writer` (as in `clean_data.py`), and why does `[r[col] for col in header]` matter?

**7.** `newline=""` in `open("file.csv", newline="")` — What bug does it prevent on Windows? Is it harmless on Linux/macOS?

**8.** **Sanity bounds dictionary** — Why does `SANITY["Overall GPA"] = (0.0, 4.0)` reject a 9.0 but keep a 0.5? One sentence.

**9.** **Audit assertion** — `assert rows_in == rows_out + rows_dropped, "Count mismatch"` — What bug would this catch that a simple `print` would miss?

**10.** **Correlation ≠ causation** — A scatter of `phishing_reports` vs `failed_logins` shows a positive trend. Write one sentence explaining why you cannot conclude "phishing causes failed logins."

---

## SECTION B — CODE READING (2 problems, 5 points each = 10 points)

### Problem 11

```python
import csv
import matplotlib.pyplot as plt

with open("data/weekday_data.csv", newline="") as f:
    rows = list(csv.DictReader(f))

weekday = []
weekend = []
for r in rows:
    if r["day_type"] == "weekday":
        weekday.append(float(r["phishing_reports"]))
    else:
        weekend.append(float(r["phishing_reports"]))

categories = ["Weekday", "Weekend"]
values = [sum(weekday)/len(weekday), sum(weekend)/len(weekend)]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=["#3498db", "#e74c3c"], edgecolor="white")
plt.title("Average Phishing Reports: Weekday vs Weekend")
plt.xlabel("Day Type")
plt.ylabel("Average Reports")
plt.ylim(bottom=0)
plt.savefig("weekday_weekend.png", dpi=150, bbox_inches="tight")
plt.clf()
```

**a.** The data has 30 weekdays and 8 weekends. Is the average comparison fair? Why or why not?

**b.** The bars are different colors (`#3498db` and `#e74c3c`). Why pass a **list** of colors instead of one string?

**c.** `plt.ylim(bottom=0)` is included. What principle does this enforce?

**d.** The chart is for a **security team** audience. The current title is fine. What would you change if the audience were **parents**?

**e.** `plt.clf()` at the end — what does it do? Why is it needed in a script that makes multiple charts?

---

### Problem 12

```python
import csv

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

SANITY = {
    "phishing_reports": (0, 100),
    "failed_logins": (0, 5000),
}

with open("data/threats.csv", newline="") as f:
    lines = [ln for ln in f if not ln.startswith("#")]
rows = list(csv.DictReader(lines))

clean = []
for r in rows:
    drop = None
    for col, (low, high) in SANITY.items():
        if r[col] == "":
            drop = f"blank {col}"
            break
        val = to_int(r[col])
        if val is None or not (low <= val <= high):
            drop = f"impossible {col}={r[col]}"
            break
        r[col] = val
    if drop:
        print(f"Dropped: {drop}")
        continue
    clean.append(r)

print(f"In: {len(rows)} Out: {len(clean)} Dropped: {len(rows)-len(clean)}")
```

**a.** A row has `"phishing_reports": "2.5"`. Trace: `to_int("2.5")` returns what? Which `if` triggers? What prints?

**b.** A row has `"failed_logins": "-10"`. Trace: `to_int("-10")` returns what? Which `if` triggers? What prints?

**c.** The comment-stripping line `[ln for ln in f if not ln.startswith("#")]` — what happens if a data row has a `#` in the *middle* of a field (not at line start)?

**d.** The `break` in each `if` block — what loop does it exit? What would happen without it on a row with TWO bad columns?

**e.** The final `print` shows `In: 60 Out: 52 Dropped: 8`. If the `assert` version were added, what would it verify?

---

## SECTION C — DATA INTEGRITY & HONESTY (1 problem, 10 points)

### Problem 13

Your Unit 2 project used `u2_campus_threat_daily.csv` (60 rows). You cleaned it and made three charts.

**a.** Write the **provenance statement** for: 60 raw rows → 54 clean, 6 dropped (3 blank `failed_logins`, 2 impossible `login_success_rate` > 1.0, 1 unparseable `phishing_reports`).

**b.** The 3 blank `failed_logins` rows were all Fridays. Does dropping them bias the weekday vs weekend comparison? Why or why not?

**c.** Your login success rate histogram has a tail at 0.60–0.70. A classmate says "drop them, they're outliers." You keep them. **Defend your choice in one sentence** using Unit 2 vocabulary.

**d.** Your timeline chart shows a spike on "Oct 14". The security team wants the date; parents don't need it. What do you do?

---

## SECTION D — WRITE CODE (1 problem, 10 points)

### Problem 14

Write a function `make_bar_chart(categories, values, title, xlabel, ylabel, filename, colors=None)` that:
- creates a new figure
- plots a bar chart of `categories` vs `values`
- if `colors` is provided (a list), uses it; otherwise uses a single default color
- sets title, x-label, y-label
- adds `edgecolor="white"` on bars
- forces y-axis to start at 0 (honest axis)
- saves to `filename` with `dpi=150, bbox_inches="tight"`
- calls `plt.clf()` after saving
- does **not** call `plt.show()`

Write the whole function. You may not use `eval()`.

---

## FINISHING

Turn your paper face down and wait quietly.