# Unit 2 Assessment — Computational Mathematics
**Schedule:** Unit 2 Assessment + Reflection
**Time:** 30 minutes assessment + 20 minutes reflection = 50 minutes total
**Conditions:** Closed computer for assessment portion. Pen and paper only. No notes, no phone, no neighbors. Reflection portion: open notes allowed.

Print double-sided. Do not write your name inside the body — write it on the coversheet only.

Total: 50 points (35 assessment / 15 reflection).

---

## COVERSHEET

Before you start, on the cover of your paper write:

- Your name
- One thing from Unit 2 you feel confident about
- One thing you hope is **NOT** on this test

The coversheet is not graded. The third answer is the useful one — it tells me where to spend review time in Unit 3.

---

## RULES

- Answer in complete sentences where the question asks *why*.
- A value or a word is fine where the question asks *what*.
- **Answer the verb.** "What happens when…" wants the actual error, not the fix. "Why" wants a sentence, not a value. Most lost points on this test come from answering a different question than the one asked.
- Show your work on every code question. Partial credit is real.
- If you finish early, review. There is no extra credit for finishing fast.

---

## PART 1 — ASSESSMENT (30 minutes, 35 points)

### SECTION A — SHORT RESPONSE (7 questions, 3 points each = 21 points)

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

### SECTION B — CODE READING (1 problem, 8 points)

*You do not run this code. You read it the way a debugger would.*

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

**a.** A row has `"Age": "N/A"`. Trace through the loop: which `if` block triggers, what is printed, and what happens to that row? (2 pts)

**b.** A row has `"Overall GPA": "3.8"` and `"Absence Rate": "1.5"`. Which `if` block triggers, what is printed, and what happens to that row? (2 pts)

**c.** The `assert rows_in == rows_out + rows_dropped` at the end of the full script would catch what bug that a simple `print` would miss? (2 pts)

**d.** Why does `to_float` catch **both** `ValueError` and `TypeError`? Give one input that triggers each. (2 pts)

### SECTION C — DATA INTEGRITY & HONESTY (1 problem, 6 points)

Your unit had exactly three integrity principles. Use them.

**8.** You cleaned 1,000 rows down to 947. The dropped rows were disproportionately low-GPA students who left GPA blank.

```python
SANITY = {
    "Overall GPA": (0.0, 4.0),
    "Age": (10, 22),
    "Absence Rate": (0.0, 1.0),
}
```

**a.** Write the one-sentence **provenance statement** you would put in your project `analysis.md`. (2 pts)

**b.** In one sentence: why does dropping blank-GPA rows *bias* the average GPA upward? (2 pts)

**c.** A histogram of `login_success_rate` shows most days near 0.95, with a thin tail to 0.60. Your partner says "those are outliers, drop them." You say "no, they're the story." Who is right, and why? (2 pts)

---

## PART 2 — REFLECTION (20 minutes, 15 points)

*Open notes allowed. Write on this paper or separate sheets — staple to assessment.*

**9. Project Themes (5 pts)** — Name **three distinct themes** from your Unit 2 project (e.g., data cleaning choices, chart type decisions, audience adaptation, privacy considerations). For each, write one sentence explaining why it mattered.

1. Theme: ____________________________________________________________
   Why it mattered: _____________________________________________________

2. Theme: ____________________________________________________________
   Why it mattered: _____________________________________________________

3. Theme: ____________________________________________________________
   Why it mattered: _____________________________________________________

**10. Gallery Security Questions (5 pts)** — During the L16 gallery walk, you saw classmates' projects. Pick **one** project (not yours) and answer:

- What chart choice made their data honest (or dishonest)?
- What privacy risk did their visualization create (or avoid)?
- One question you would ask the author about their data pipeline.

**11. Personal Principle (5 pts)** — Based on everything in Unit 2 (cleaning, charting, gallery, privacy), write **one defensible principle** you will carry into Unit 3. One paragraph. It must be specific enough to apply to a new dataset tomorrow.

---

## FINISHING

Turn your paper face down and wait quietly.