# U2 L07 — LAB: Bar Charts and Categorical Data

**LO:** apply matplotlib skills to real categorical data from datasets.

Today you get YOUR OWN copy of a data-lab repo. It comes with real data files
and a self-check that starts at **2/4 passing**. Your job: finish the bar chart
and make it **4/4**.

## PART 0 — GET YOUR LAB REPO (first 10 minutes)

1. Check your school Gmail — you have an invitation to collaborate on your own
   private repo. Accept it.
2. Your repo is `compmath-u2-viz-basics-<your-name>` under the
   `ivycollegiate-development` organization.
3. Clone it (start with `pwd` — know where you are):

```bash
pwd
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-$(whoami)_student.git compmath-u2-viz-basics
cd compmath-u2-viz-basics
ls
```

(If the clone fails, re-copy the exact URL from the invitation email — that is
always the fix.) Inside, look at `ls data/`: you should see
`u2_dataset1_study_habits.csv`, `u2_dataset2_mental_health.csv`, and
`u2_dataset3_activities.csv`.

## PART 1 — MEET THE DATA (10 min)

The study-habits file has 52 rows, one per student:

```
Student_ID, Study_Hours, Test_Score, Attendance, Sleep_Hours
```

Peek at the top three rows with:

```bash
head -4 data/u2_dataset1_study_habits.csv
```

In your notes:

- Which columns are **numbers** and which is a **category** here? (Hint: what
  would it mean to take an average of it?)
- Friday's lesson: what chart type compares *categories*?

## PART 2 — SEE IT FAIL (10 min)

```bash
python3 chart_bars.py
```

It runs but the chart is not done — the attendance bands are placeholders and
the averages are wrong. Then run the self-check:

```bash
python3 self_check.py
```

You should see **2/4 passing**. Your goal today: **all 4 passing**.

## PART 3 — FIX IT (in pairs, ~40 min)

Open `chart_bars.py`. There are two `FIX ME` bugs:

1. **Band assignment.** The code has a `band_of(attendance)` function that is
   supposed to bucket each student's attendance % into `"A"` (90+), `"B"`
   (80–89), `"C"` (70–79), `"Below"` (under 70). It is assigning bands wrong —
   compare the thresholds against the comment above the function. This one is
   quietly wrong, not crashing.
2. **Averaging.** The averages are computed with integer division `//`, so
   every band's average comes out truncated. Use `/` and check one band by
   hand against the raw rows.

Use `stdlib csv` — same patterns as Unit 1:

```python
import csv

rows = []
with open("data/u2_dataset1_study_habits.csv") as f:
    for row in csv.DictReader(f):
        rows.append(row)
```

Then build the averages with a plain dict:

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

Run `python3 self_check.py` after each fix — each PASS is a guardrail.

**Milestone for today:** 4/4 passing, and the saved bar chart
(`attendance_scores.png`) showing average score per attendance band with title,
axis labels, and an honest y-axis starting at 0 (Friday's lesson applies —
a truncated bar axis here would be exactly the sin of Monday).

## PART 4 — EXTENSION (if 4/4 early)

- Redo the chart with `Sleep_Hours` bands instead — does the shape look
  different?
- Add the second dataset (`u2_dataset2_mental_health.csv`: Stress_Level,
  Hours_Exercise, GPA, Social_Hours) and chart GPA grouped by stress level.
- No pandas, no pip installs — matplotlib 3.10 and `csv` are all you need.

## PART 5 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-viz-basics
git add chart_bars.py attendance_scores.png
git commit -m "fix band assignment and averaging, chart 4 of 4 passing"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## TURN IN

1. Push your final `chart_bars.py` and `attendance_scores.png` (self-check
   4/4).
2. Confirm the push landed: on github.com, open **your** repo and check the
   latest commit shows both files.

**Spot-check:** open `attendance_scores.png` and verify (a) the y-axis starts
at 0, (b) every bar has a band label, (c) the title states the finding, not
just the columns. Then submit your repo link to this assignment on Google
Classroom.

Early finishers: reorder the bands left-to-right (A → Below) with an explicit
list, or add a second series (Attendance-band averages for a different score
column) with a legend.
