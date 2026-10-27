# U2 L07 — Lab Worksheet: Bar Charts and Categorical Data

Names: ___________________________  Date: ____

Fill this in **as you work**, not at the end. Every blank wants the thing you actually saw on your screen — the value your code printed, the count the self-check gave you, the exact labels you typed.

## Part 0 — Get your lab repo (5 min)

```bash
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-$(whoami)_student.git compmath-u2-viz-basics
cd compmath-u2-viz-basics
ls
ls data/
```

| Checkpoint | What I saw |
|------------|------------|
| `ls` showed a `.py` script, a self-check, and a `data/` folder | |
| Charting script name | |
| `ls data/` — how many CSV files? | |

## Part 1 — Meet the data (5 min)

Open `data/u2_dataset1_study_habits.csv` and read the first 6 lines. **The first line starts with `#` and there's a blank line before the real header.** Why would that break `csv.DictReader`?

_________________________________________________________________________

In `charts.py` (around line 13), the loader filters those lines out. Write the filter condition:

_________________________________________________________________________

**Classify each column** — quantitative (averagable) or categorical (label/group). `Student_ID` is done.

| Column | Quantitative or categorical? | Note |
|--------|------------------------------|------|
| Student_ID | categorical | it is an ID, not a real group — numbers that mean nothing |
| Study_Hours | | |
| Test_Score | | |
| Attendance | | |
| Sleep_Hours | | |

**The bar chart groups students into bands:** `10-15h`, `15-20h`, `20-25h`, `25-30h`, `30-35h`, `35+h`.  
Those bands are: (circle one) **quantitative** / **categorical**

## Part 2 — Run → check → fix → re-check (30 min)

Run the script and self-check. Record exact numbers.

```bash
python3 charts.py
python3 self_check.py
```

| Check | What the self-check printed |
|-------|----------------------------|
| Check 1 | ______ / 4 passing |
| Check 2 | Two chart files saved: 1. ________________  2. ________________ |
| Check 3 | Charts are missing: _________________________________________ |
| Check 4 | Which chart is missing its title? _____________________________ |

---

### Fix 1: scatter chart (`chart_study_vs_score.png`)

| Check | Answer |
|-------|--------|
| As study hours go up, test scores tend to: | go up / go down / stay flat |
| Axis labels added (exact lines, units included): | |
| x-axis | `_________________________________________________________________` |
| y-axis | `_________________________________________________________________` |
| x-axis units: | ________________________________________________ |
| y-axis units: | ________________________________________________ |

---

### Fix 2: bar chart (`chart_study_bands.png`)

| Check | Answer |
|-------|--------|
| x-axis shows: | (the six bands) ______________________________________ |
| y-axis is a: | score / time / **count of students** (circle one) |
| Title line added: | `_________________________________________________________________` |
| x-label line added: | `_________________________________________________________________` |
| y-label line added: | `_________________________________________________________________` |

**Count bar heights:**

| Band | How many students? (read the bar) |
|------|-----------------------------------|
| `10-15h` | |
| `15-20h` | |
| `20-25h` | |
| `25-30h` | |
| `30-35h` | |
| `35+h` | |

Which band has the most students? _______________________________

**Real data range — run this:**

```bash
python3 -c "import csv;f=open('data/u2_dataset1_study_habits.csv');v=[float(r['Study_Hours']) for r in csv.DictReader(l for l in f if l.strip() and not l.startswith('#'))];print(min(v),max(v))"
```

minimum study hours: __________   maximum: __________

**Honest-chart call** — these bands cover the data range and spread students across several bars. Is this an honest picture? One sentence.

_________________________________________________________________________

_________________________________________________________________________

---

### Verify 4/4

Re-run self-check after fixes:

```bash
python3 charts.py
python3 self_check.py
```

| After I fixed the labels, self-check says | ______ / 4 |
|-------------------------------------------|------------|
| If not 4 yet, which check fails? | |

**Why does the last check (work committed) still fail until you push?** One sentence.

_________________________________________________________________________

## Part 3 — Save and submit (5 min)

```bash
cd ~/compmath-u2-viz-basics
git add charts.py chart_study_vs_score.png chart_study_bands.png
git commit -m "add chart titles and axis labels, self-check 4 of 4"
git push
```

| Checkpoint | Result |
|------------|--------|
| Self-check after push = ___ / 4 | |
| Latest commit on github.com shows changed files | |
| Git asked for password? (if yes → PAT issue) | |

## Extension (only if you already have 4/4)

Re-band by `Sleep_Hours` — your own bands, e.g. `6.0-6.5`, `6.5-7.0`, `7.0-7.5`, `7.5-8.0` — and re-chart. One line: does the shape look different from the study-hours chart?

_________________________________________________________________________

## TURN IN

☐  Parts 0–3 complete — every blank filled with what you actually saw.  
☐  Screenshot to the U2 L07 Classroom assignment by 11:59 PM tonight showing: this completed worksheet, both chart PNGs, and `self_check.py` printing 4 of 4.  
☐  Your repo link submitted on the U2 L07 assignment.

Keep this sheet. Labeling a chart is not extra credit — an unlabeled chart is not finished.