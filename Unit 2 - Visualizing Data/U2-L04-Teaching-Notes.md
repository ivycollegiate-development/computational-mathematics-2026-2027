# U2 L04 — Teaching Notes: Walking Students Through the Review

**Lesson:** U2 L04 — Review: From Data to Visualization  
**Date:** Monday Oct 12 (Period 1: 8:00, Period 2: 8:55)  
**Duration:** 55 min  
**Goal:** Students leave with confidence that L02/L03 concepts are solid before L05 adds customization.

---

## CLASS FLOW (minute-by-minute)

| Time | Segment | Teacher Moves |
|------|---------|---------------|
| 0:00–0:05 | **Settle + Frame** | "Friday we built our first scatter plot from real data. Today we prove we can do it cold. No new syntax — just retrieval and transfer." |
| 0:05–0:20 | **Part 1: Concept Check (closed notes)** | Project the 10 questions. Read each aloud. 60–90 sec per question. Collect papers at 0:20 sharp. |
| 0:20–0:40 | **Part 2: Live Rebuild (open notes allowed)** | "Open your lab repo, pull, start python3. Rebuild the L03 scatter plot from memory. I'll circulate." |
| 0:40–0:50 | **Part 3: Extension — Second Series** | "Same dataset, add Sleep_Hours. Different color, label=, legend(). Save as review_two_series.png." |
| 0:50–0:55 | **Part 4 + 5: Paper Check Preview + Journal Push** | Quick pair-share for check questions. Touch journal template. Remind: screenshot + push due 11:59 PM. |

---

## PART 1 — CONCEPT CHECK: TALKING POINTS & EXPECTED ANSWERS

### A. Data vs. Numbers (L02)

| Q | Expected Answer | Key Language to Hear |
|---|-----------------|----------------------|
| 1. Number vs. data | "Data is numbers **plus context** — what, from whom, when measured." | "context", "measured", "meaning" |
| 2. 53 lines, 52 students | "Line 1 is the **header row** (column names), not a student." | "header", "skip", "rows[1:]" |
| 3. mental-health crash | "Line 1 is a **comment** (`# ...`). `messy[0][1]` tried to index into the comment string." | "comment line", "skip line 1", "messy[2:]" |

**If they miss #3:** "The `#` line is documentation *inside* the file. Real data is messy — always inspect line 1 before assuming it's a header."

---

### B. CSV Reading Mechanics (L02)

| Q | Expected Answer | Key Language |
|---|-----------------|--------------|
| 4. `csv.reader` returns | "A **list of strings** for each row." | "list", "strings", "each column" |
| 5. Comment + header → slice | "`[2:]` — skips line 0 (comment) and line 1 (header)." | "index 2", "skip both" |

**Probe:** "What would `[1:]` give you?" → "The header row as if it were data → crash on float conversion."

---

### C. First Visualization (L03)

| Q | Expected Answer | Key Language |
|---|-----------------|--------------|
| 6. line chart call | `plt.plot(days, temps)` | "plot", "sequence", "connected" |
| 7. Three required labels | "**Title, x-label with units, y-label with units**" (exact L03 rule) | All three named |
| 8. Why scatter for Test_Score vs Study_Hours | "Each student is **one independent point**, not a step in a sequence." | "independent", "not a sequence" |
| 9. savefig vs show | "`savefig` writes a **file** you can submit/keep; `show` only displays on screen." | "file", "submit", "persist" |

---

### D. Quick Apply (2 pts)

| Bug | Expected Answer |
|-----|-----------------|
| 1 | `plt.legend()` called but no series has `label=` → empty legend box |
| 2 | **y-axis has no label** (`plt.ylabel()` missing) |

**Say:** "Two bugs, not one. The legend is a distractor — the real problem is the missing y-label. A chart without units on both axes is a rumor."

---

## PART 2 — LIVE REBUILD: CIRCULATION CHEAT SHEET

**Target script (what they should produce):**

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_dataset1_study_habits.csv") as f:
    rows = list(csv.reader(f))

data = rows[1:]           # skip header
hours  = [float(r[1]) for r in data]   # column 1 = Study_Hours
scores = [float(r[2]) for r in data]   # column 2 = Test_Score

plt.scatter(hours, scores, s=15)
plt.title("Test Score vs. Study Hours (52 Students)")
plt.xlabel("Weekly Study Hours (hrs)")
plt.ylabel("Test Score (points)")
plt.grid(True)
plt.savefig("review_scatter.png", dpi=150)
plt.show()
```

### Common Stuck Points & Prompts

| Stuck Moment | Prompt (don't give the answer) |
|--------------|--------------------------------|
| "How do I open the file?" | "What mode does `open` default to? What does `with` buy you?" |
| "Which column is which?" | "Print `rows[0]` — what does the header tell you?" |
| "Index error on `r[2]`" | "How many columns per row? Check `len(rows[0])`." |
| "Points all overlap" | "What does `s=15` control? Try `s=1`." |
| "Nothing shows" | "Did you call `plt.show()`? Did you call `savefig` *before* `show()`?" |
| "File not found" | "`pwd` — where are you? `ls data/` — is the CSV there?" |

**If a student finishes early:** "Add a trend line: `import numpy as np; z = np.polyfit(hours, scores, 1); plt.plot(hours, np.poly1d(z)(hours), 'r--')`"

---

## PART 3 — EXTENSION: SECOND SERIES

**Target addition:**

```python
sleep = [float(r[3]) for r in data]   # column 3 = Sleep_Hours
plt.scatter(sleep, scores, color="orange", label="Sleep vs Score", s=15)
plt.legend()
plt.savefig("review_two_series.png", dpi=150)
```

**Discussion prompt (while circulating):** "Does Sleep_Hours show the same lean as Study_Hours? What would a third series (Attendance) look like?"

---

## PART 4 — PAPER CHECK PREVIEW (pair share, 5 min)

**Project these three prompts. Pairs write one question each.**

| Topic | Sample Student Questions (if they need seeding) |
|-------|------------------------------------------------|
| CSV reading | "A file has two comment lines then a header. What slice skips to data?" |
| Chart anatomy | "A chart has title and x-label but no y-label. What specific question can the reader NOT answer?" |
| Chart type choice | "You have monthly revenue for 12 months. Line, bar, or scatter — and why?" |

**Collect or photo for your test bank.**

---

## PART 5 — JOURNAL TEMPLATE (project or hand out)

```markdown
# U2 L04 Journal

1. Shakiest concept today:
   What I did to firm it up:

2. One matplotlib thing that still surprises me:

3. `ls -lh` output:
   (paste here)
```

---

## SCREENSHOT CHECKLIST (what you'll grade tonight)

| # | Must Appear In Screenshot | Points |
|---|---------------------------|--------|
| 1 | Part 1 answers (1–10) | 10 |
| 2 | Part 2 REPL session (rebuilt scatter working) | 10 |
| 3 | Part 3 two-series plot on screen | 5 |
| 4 | `ls -lh review_scatter.png review_two_series.png` | 5 |
| 5 | Successful `git push` | 5 |
| **Total** | | **35** |

---

## DIFFERENTIATION NOTES

| Student Profile | Adjustment |
|-----------------|------------|
| **Struggling with CSV** | Pre-load `rows = list(csv.reader(open(...)))` in a starter file; they only do extraction + plot. |
| **Forgot matplotlib syntax** | Allow open notes for Part 2 (not Part 1). |
| **Fast finishers** | Challenge: plot Attendance (col 4) vs Test_Score as third series, different marker. |
| **No lab repo** | Pair with a neighbor; both names on submission. |

---

## TIMING RISKS & CONTINGENCIES

| Risk | Contingency |
|------|-------------|
| Part 1 runs long | Cut Q10 (apply) — collect 9 questions, grade 9. |
| Git push fails (PAT issues) | "Screenshot the error, push from home, email me the PNG." |
| Several students can't find CSV | `cd ~/compmath-u2-data-lab && git pull` as whole-class reset. |
| Fire drill / short period | Skip Part 3; journal becomes homework. |

---

## POST-CLASS ACTIONS

1. **Grade Part 1 papers** before Tuesday — identifies reteach targets for L06 paper check.
2. **Scan screenshots** for: missing y-label, wrong column index, savefig after show.
3. **Update L05 do-now** based on Part 1 misses (e.g., if many missed Q3, add comment-line drill to L05 opener).

---

## QUICK REFERENCE: L02→L03→L04→L05 THREAD

| Lesson | Core Skill | L04 Checks | L05 Builds On |
|--------|------------|------------|---------------|
| L02 | CSV reading, header vs comment, mean/split | Q2, Q3, Q4, Q5 | — |
| L03 | First plot, anatomy (3 labels), scatter vs plot, savefig | Q6, Q7, Q8, Q9 | Customization (colors, legends, bar/line/scatter choice) |
| L04 | Retrieval + transfer (cold rebuild) | All | Fluency for L05 mini-exercise |
| L05 | **New:** colors, markers, legends, bar/line/scatter choice, savefig order | — | L06 paper check, L07 lab |

---

**Last updated:** 2026-10-11  
**File:** `U2-L04-Teaching-Notes.md` (same folder as lesson)