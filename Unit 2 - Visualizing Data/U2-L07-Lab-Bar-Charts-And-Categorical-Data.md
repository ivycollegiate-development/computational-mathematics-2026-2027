# U2 L07 — LAB: Bar Charts and Categorical Data

**LO:** apply matplotlib skills to real categorical data from datasets; debug band assignment and averaging logic.

**Estimated time:** 85 minutes (was ~65). We move slower so the debugging process teaches, not just the result.

---

Today you get YOUR OWN copy of a data-lab repo. It comes with real data files and a self-check that starts at **2/4 passing**. Your job: finish the bar chart and make it **4/4**.

The paper check you took in U2 L06 covered chart choice, the label rule, and reading matplotlib output. That is the foundation for everything below — if a question comes back on the label rule, it is because the bars you build today are read by a real audience.

---

## PART 0 — GET YOUR LAB REPO (first 15 minutes)

**Step 1:** Check your school Gmail — you have an invitation to collaborate on your own private repo. Accept it. (If you don't see it, check Spam/Promotions, then ask.)

**Step 2:** Your repo is named `compmath-u2-viz-basics-<your-name>_student` under the `ivycollegiate-development` organization. The `<your-name>` part matches your GitHub username.

**Step 3:** Clone it. Start with `pwd` — always know where you are.

```bash
pwd
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-$(whoami)_student.git compmath-u2-viz-basics
cd compmath-u2-viz-basics
ls
```

**Why this sequence:**
- `pwd` confirms you're in your home directory before cloning
- `cd ~` guarantees the clone lands in a predictable place (`~/compmath-u2-viz-basics`)
- The `$(whoami)` expands to your system username, which matches the repo suffix
- `ls` lets you verify the clone worked

**If the clone fails:** Re-copy the exact URL from the invitation email — that is always the fix. Typos in the org name (`ivycollegiate-development`) or the `_student` suffix are the most common causes.

**Inside, look at `ls data/`:** You should see:
- `u2_dataset1_study_habits.csv`
- `u2_dataset2_mental_health.csv`
- `u2_dataset3_activities.csv`

These are the same CSV files you saw previews of in U2 L05. Today we work with the first one.

---

## PART 1 — MEET THE DATA (15 min)

The study-habits file has 52 rows, one per student:

```
Student_ID, Study_Hours, Test_Score, Attendance, Sleep_Hours
```

Peek at the top three rows with:

```bash
head -4 data/u2_dataset1_study_habits.csv
```

(The `-4` shows the header + 3 data rows.)

**In your notes, answer:**

1. Which columns are **numbers** (quantitative) and which is a **category** (categorical)?
   - *Hint:* What would it mean to take an average of it? You can average `Study_Hours` (6.5 hours makes sense). You cannot average `Student_ID` ("S01" + "S02" ÷ 2 = nonsense).

2. From U2 L05: what chart type compares *categories*?

**Expected reasoning:**
- **Numerical:** `Study_Hours`, `Test_Score`, `Attendance`, `Sleep_Hours` — all are quantities you can add, average, compare with `<`/`>`
- **Categorical:** `Student_ID` — it's an identifier, not a quantity
- **Chart type for comparing categories:** Bar chart (U2 L05 Part 2)

**Why this matters:** The whole lab is about taking a numerical column (`Test_Score`), grouping it by a *derived* categorical column (attendance bands we'll create from the numerical `Attendance`), and comparing the group averages with a bar chart. If you confuse the types, you'll pick the wrong chart.

---

## PART 2 — SEE IT FAIL (15 min)

Run the starter script:

```bash
python3 chart_bars.py
```

It runs without crashing but the chart is not done — the attendance bands are placeholders and the averages are wrong. Look at the saved `attendance_scores.png` (it should appear in the repo folder). Notice:
- The x-axis has band labels but they're wrong
- The y-axis values look too low (truncated)

Then run the self-check:

```bash
python3 self_check.py
```

You should see **2/4 passing**. Your goal today: **all 4 passing**.

**What the self-check tests (you don't need to read the file, but this is what it verifies):**
1. Band assignment logic is correct (A/B/C/Below thresholds)
2. Averages use float division, not integer division
3. Chart saves as `attendance_scores.png`
4. Chart has title, x-label, y-label (the label rule)

---

## PART 3 — FIX IT (in pairs, ~45 min)

Open `chart_bars.py`. There are two `FIX ME` bugs. We'll tackle them one at a time.

### Bug 1 — Band assignment (quietly wrong, not crashing)

Find the `band_of(attendance)` function. It's supposed to bucket each student's attendance percentage into:
- `"A"` for 90% and above
- `"B"` for 80–89%
- `"C"` for 70–79%
- `"Below"` for under 70%

**The bug:** The thresholds in the code don't match the comment above the function. This is a *silent* bug — no error, just wrong bands.

**How to debug it:**
1. Read the function carefully. Trace through with a test value: `attendance = 85`. What band does it return? What *should* it return?
2. Add a temporary print to verify:

```python
print(band_of(95))  # should be "A"
print(band_of(85))  # should be "B"
print(band_of(75))  # should be "C"
print(band_of(65))  # should be "Below"
```

Run `python3 chart_bars.py` and check the output. Fix the thresholds until all four print correctly.

**Why this is tricky:** The conditions are likely written as `if attendance >= 90:` then `elif attendance >= 80:` etc. But if the order is wrong (e.g., checking `>= 70` before `>= 80`), values 80–89 get caught by the 70-check and misclassified as "C". **Order of `elif` matters.**

### Bug 2 — Averaging (integer division truncates)

Find where the averages are computed. Look for `//` (integer division / floor division).

**The bug:** `//` truncates the decimal. If a band's scores are 71, 73, 74, the sum is 218, count is 3. `218 // 3 = 72` (truncated). `218 / 3 = 72.666...` (correct).

**How to debug it:**
1. Change `//` to `/`
2. Pick one band and verify by hand against the raw rows:
   - `grep '"A"' data/u2_dataset1_study_habits.csv` (or whatever band you're checking)
   - Average the `Test_Score` column manually
   - Compare to what your script prints

**The reading pattern (same as Unit 1):**

```python
import csv

rows = []
with open("data/u2_dataset1_study_habits.csv") as f:
    for row in csv.DictReader(f):
        rows.append(row)
```

**Why `csv.DictReader`:** It reads the header row and gives you each row as a `dict` with column names as keys. So `row["Attendance"]` gives you the attendance string, `row["Test_Score"]` gives the score string. You must convert with `float()`.

**The aggregation pattern:**

```python
totals = {}   # band -> [score_sum, count]
for row in rows:
    band = band_of(float(row["Attendance"]))
    score = float(row["Test_Score"])
    if band not in totals:
        totals[band] = [0.0, 0]
    totals[band][0] += score
    totals[band][1] += 1

avg = {band: s / n for band, (s, n) in totals.items()}
```

**Walkthrough:**
- `totals` maps band name → `[running_sum, running_count]`
- For each row: compute band, convert score to float, add to that band's sum and count
- After the loop: `avg` builds a dict of band → average (sum / count) using a dict comprehension
- **Crucial:** `s / n` uses float division (`/`), not `//`

**Run `python3 self_check.py` after each fix.** Each PASS is a guardrail — don't move to the next fix until the current one passes.

### Milestone for today: 4/4 passing

And the saved bar chart (`attendance_scores.png`) must show:
- Average score per attendance band
- **Title** that states the finding (not just "Attendance vs Score")
- **x-label:** "Attendance band"
- **y-label:** "Average test score"
- **Honest y-axis starting at 0** — the label rule from U2 L05 applies. A truncated y-axis (starting at 60, for example) would exaggerate the differences between bands. We want honest comparison.

---

## PART 4 — EXTENSION (if 4/4 early)

- Redo the chart with `Sleep_Hours` bands instead — does the shape look different? (Define your own bands: e.g., `<6`, `6–7`, `7–8`, `8+`)
- Add the second dataset (`u2_dataset2_mental_health.csv`: `Stress_Level`, `Hours_Exercise`, `GPA`, `Social_Hours`) and chart GPA grouped by stress level.
- No pandas, no pip installs — matplotlib 3.10 and `csv` are all you need.

---

## PART 5 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-viz-basics
git add chart_bars.py attendance_scores.png
git commit -m "fix band assignment and averaging, chart 4 of 4 passing"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.** If you don't have a PAT, stop and ask — do not use your account password.

---

## TURN IN — PULL REQUEST LINK (due 23:59 tonight)

1. Push your final `chart_bars.py` and `attendance_scores.png` (self-check 4/4).
2. Confirm the push landed: on github.com, open **your** repo and check the latest commit shows both files.

**Spot-check before submitting:** Open `attendance_scores.png` and verify:
- [ ] The y-axis starts at 0
- [ ] Every bar has a band label (A, B, C, Below)
- [ ] The title states the finding, not just the columns (e.g., "Average Test Score by Attendance Band — A-band students score 15 points higher than Below-band")
- [ ] The file is not 0 bytes

Then submit your repo link to the U2 L07 assignment on Google Classroom.

**Early finishers:** Reorder the bands left-to-right (A → Below) with an explicit list, or add a second series (Attendance-band averages for a different score column) with a legend.

---

## WHY THIS MATTERS (the bigger picture)

This lab teaches the **full data-to-viz pipeline** you'll use all year:
1. **Get data** — clone repo, verify CSV structure
2. **Read data** — `csv.DictReader`, convert strings to numbers
3. **Transform data** — derive categories from numbers (banding)
4. **Aggregate data** — group by category, compute summary statistics
5. **Visualize** — bar chart with proper labels, honest axis
6. **Verify** — self-check guards, visual spot-check
7. **Publish** — git commit, push, submit link

Every subsequent lab (U2 L08, U2 L10, U2 L13, and the Unit 2 project U2 L15–L18) follows this same skeleton. The column names and chart types change; the pipeline doesn't.

**Next:** U2 L08 — Reading Data From Files  
[U2-L08-Reading-Data-From-Files.md](U2-L08-Reading-Data-From-Files.md)