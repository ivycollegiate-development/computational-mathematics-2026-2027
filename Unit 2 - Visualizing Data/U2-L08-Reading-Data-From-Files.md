# U2 L08 — Reading Data From Files

**LO:** load data from CSV files into Python and prepare it for visualization.

Today you get YOUR OWN copy of the **data lab** repo — a different one from
Monday's. Real datasets, including a 1000-row performance file, and the
honest truth about real data: it is messy. By the end you will have a clean
per-row list ready to plot next week.

## PART 0 — GET YOUR DATA-LAB REPO (first 10 minutes)

1. Check your school Gmail — accept the invitation to your own private repo.
2. Your repo is `compmath-u2-data-lab-<your-name>` under the
   `ivycollegiate-development` organization.
3. Clone it:

```bash
pwd
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-data-lab-$(whoami)_student.git compmath-u2-data-lab
cd compmath-u2-data-lab
ls
ls data/
```

The star of today is `data/u2_student_performance_data.csv` — **1000 rows**:
Student ID, Gender, Age, Parent Education Level, Hours Studied Per Week, Sleep
Hours Per Night, Extracurricular Activities, Math Score, Science Score, English
Score, Overall GPA, Absence Rate.

## PART 1 — CODE-ALONG: `csv.DictReader` END TO END (15 min)

```bash
touch load_scores.py
```

No pandas, no pip installs — matplotlib and `csv` are preinstalled. Start:

```python
import csv

with open("data/u2_student_performance_data.csv") as f:
    rows = list(csv.DictReader(f))

print(len(rows))          # 1000
print(rows[0].keys())     # the column names
print(rows[0]["Overall GPA"])
```

- `DictReader` reads the **first row as the keys** and hands you every row as a
  dict. One catch: every value arrives as a **string**, even numbers.
- Convert on the way through: `gpa = float(row["Overall GPA"])`.

In the REPL (`python3`), first answer, then test:

- What type is `rows[0]["Age"]` before you convert it?
- What happens with `float("")` — and what error name is that?

## PART 2 — CODE-ALONG: SELECT, FILTER, AGGREGATE (20 min)

Three moves, all with plain dicts — append to `load_scores.py` as we go.

**Select** columns you care about (skip the rest):

```python
records = [{"gpa": float(r["Overall GPA"]),
            "study": float(r["Hours Studied Per Week"]),
            "sleep": float(r["Sleep Hours Per Night"])}
           for r in rows]
```

**Filter** with a plain `if`:

```python
heavy = [r for r in records if r["study"] >= 10]
print(len(heavy))   # how many study 10+ hours/week?
```

**Aggregate** with a dict of accumulators (same pattern as Monday's lab):

```python
by_study = {}   # study-hours -> [gpa_sum, count]
for r in records:
    band = int(r["study"])   # 0, 1, 2, ... hours studied
    if band not in by_study:
        by_study[band] = [0.0, 0]
    by_study[band][0] += r["gpa"]
    by_study[band][1] += 1

avg_by_study = {h: s / n for h, (s, n) in by_study.items()}
```

Answer in your notes: which of these three outputs is the one you would hand
to `plt.plot` next week, and in what form? (Two parallel lists: sorted keys,
and averages in the same order.)

## PART 3 — THE MESSY FILES: REAL DATA IS MESSY (20 min)

Now `ls data/` again. Three of these files are *not* clean:

```bash
head -4 data/u2_dataset1_study_habits.csv
```

Line 1 is a **`#` comment line** — a note someone left in the file. If you hand
that to `csv.DictReader` blindly, your "first row" becomes `# comment text` and
every row is garbage.

The fix: strip comment lines before parsing.

```python
def load_csv(path):
    with open(path) as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    return list(csv.DictReader(lines))
```

Test it on all three messy files (`u2_dataset1_study_habits.csv`,
`u2_dataset2_mental_health.csv`, `u2_dataset3_activities.csv`):

- `print(len(load_csv("data/u2_dataset1_study_habits.csv")))` — expect **52**,
  not 53.
- Print the keys of the first row — they should be the real column names, not
  comment text.

In your notes: what would have gone silently wrong if you had *not* stripped
the comment, and why is a wrong first row worse than a crash? (Monday's
quietly-wrong bug, again.)

## PART 4 — BUILD YOUR PLOT-READY LIST (20 min, on your own)

Goal: one list, clean and ordered, ready for a chart. In `load_scores.py`:

1. Load the 1000-row file with `DictReader`.
2. Filter out any row with a missing or empty GPA (real datasets have holes).
3. Convert GPA and Sleep Hours to floats.
4. Group by sleep band (under 6, 6–7, 7–8, over 8) and compute average GPA
   per band — accumulate in a dict, exactly like Part 2.
5. End the script by printing two parallel lists, e.g.:

```python
bands = sorted(avg_by_sleep)
avgs = [avg_by_sleep[b] for b in bands]
print(bands)
print(avgs)
```

That pair of lists is next week's bar chart. If the script runs clean and
prints both, you have won today.

## PART 5 — TURN IN

```bash
cd ~/compmath-u2-data-lab
git add load_scores.py
git commit -m "load csv, filter and aggregate gpa by sleep band"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

**Spot-check:** run `python3 load_scores.py` one last time and confirm the two
printed lists have the **same length**, and that the messy-file loader reports
52 rows. Then submit your repo link to this assignment on Google Classroom.

Early finishers: add a guard that rejects rows where GPA isn't parseable
(`try/except ValueError`) and counts how many you dropped; or extend the
grouping to Math Score vs. Parent Education Level.
