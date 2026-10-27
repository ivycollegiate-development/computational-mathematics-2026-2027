# U2 L11 — Data Integrity and Clean Data Worksheet

**Name:** _________________________  
**Date:** _________________________  
**Partner:** _________________________  

---

## PART 0 — See the Mess First

☐  I opened `data/u2_student_performance_data.csv` in VS Code and identified the four problem types:

| Problem type | What it looks like | Why it breaks things |
|---|---|---|
| Blank cells | | |
| Impossible values | | |
| Type traps | | |
| Comment lines above header | | |

---

## PART 1 — Missing Data: Detect, Then Decide

☐  I ran the blank-detection code and recorded my results:

**My output:**

```
total blank cells: __________
blanks by column: _______________________________________
```

☐  For each column with blanks, I decided **drop** or **fill** and wrote my reasoning:

| Column | Blanks | My choice (drop/fill) | Reasoning |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

**Rule I'm following for plot-axis columns:** _______________________________________________

---

## PART 2 — Outliers: Sanity Bounds

☐  I defined my `SANITY` bounds and ran the impossibility counter:

**My output (counts per column):**

| Column | Impossible values found |
|---|---|
| Age | |
| Math Score | |
| Science Score | |
| English Score | |
| Overall GPA | |
| Hours Studied Per Week | |
| Sleep Hours Per Night | |
| Absence Rate | |

☐  **Why does GPA 9 get thrown out but GPA 0.5 get kept?**

________________________________________________________________________________
________________________________________________________________________________

---

## PART 3 — Type Traps: Convert Deliberately

☐  I tested the `to_float` helper:

**Test cases I ran:**

| Input | `to_float` output | Why |
|---|---|---|
| `"87.5"` | | |
| `""` | | |
| `"N/A"` | | |
| `"unknown"` | | |
| `None` | | |
| `"0"` | | |

☐  **Why is `float(value) if value else None` not robust?**

________________________________________________________________________________
________________________________________________________________________________

---

## PART 4 — Build `clean_data.py`

☐  I created `clean_data.py` in my repo and ran it:

```
Rows in: ________
Rows out: ________
Rows dropped: ________
Dropped by reason: _______________________________________
```

☐  The `assert` passed (counts add up): ☐ Yes  ☐ No

☐  I verified `data/u2_student_performance_clean.csv`:
- ☐ No blank cells in numeric columns
- ☐ Header row matches original
- ☐ All values look reasonable

---

## PART 5 — The Cost of Cleaning

☐  A situation where dropping rows would **distort** a conclusion:

________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________

---

## PART 6 — Save and Submit

☐  I committed and pushed my work:

```bash
cd ~/compmath-u2-data-lab
**git add** clean_data.py data/u2_student_performance_clean.csv
**git commit** -m "clean_data.py: blanks, outliers, type traps"
**git push**
```

☐  I took two screenshots for Classroom submission:
1. ☐ Terminal output showing rows in/out/dropped adding up
2. ☐ VS Code showing first lines of `data/u2_student_performance_clean.csv`

☐  I confirmed the push succeeded on GitHub.

---

## REFLECTION (answer in your notes)

1. **What was the hardest cleaning decision you made today? Why?**

________________________________________________________________________________
________________________________________________________________________________

2. **If you had 10,000 rows instead of ~1,000, what would you automate differently?**

________________________________________________________________________________
________________________________________________________________________________

3. **How does the "counts must add up" assert protect you from silent bugs?**

________________________________________________________________________________
________________________________________________________________________________