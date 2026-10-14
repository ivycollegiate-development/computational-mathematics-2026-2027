# U2 L07 — Lab Worksheet: Bar Charts and Categorical Data

Names: ___________________________  Date: ____

Fill this in **as you work**, not at the end. Every blank wants the thing you actually saw on your screen — the value your code printed, the count the self-check gave you, the exact labels you typed. This sheet is your record of how you debugged it.

## Part 0 — Get your lab repo (10 min)

Clone your copy of the lab, then look around before you touch anything.

```bash
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-viz-basics-$(whoami)_student.git compmath-u2-viz-basics
cd compmath-u2-viz-basics
ls
ls data/
```

| Checkpoint | What I saw |
|------------|------------|
| `ls` showed a `.py` script, a self-check, and a `data/` folder     |                                        |
| The name of the charting script is                                 |                                        |
| `ls data/` showed how many CSV files?                              |                                        |

## Part 1 — Meet the data (10 min)

Run this and paste the first six lines:

```bash
head -6 data/u2_dataset1_study_habits.csv
```

   _________________________________________________________________________

   _________________________________________________________________________

   _________________________________________________________________________

**Look closely at the top of that file.** The very first line starts with a `#`, and there is a blank line before the real header. Why would that break a script that reads the file with `csv.DictReader`?

   _________________________________________________________________________

Now open `charts.py` and find the lines that load the data (around line 13). They filter those lines out. Write the filter condition you see:

   _________________________________________________________________________

**Classify each column.** Write **quantitative** (a number you can average) or **categorical** (a label / group). `Student_ID` is done for you.

| Column | Quantitative or categorical? | Note |
|--------|------------------------------|------|
| Student_ID                                                                | categorical                            | it is an ID, not a real group — numbers that mean nothing |
| Study_Hours                                                                |                                        |                                        |
| Test_Score                                                                |                                        |                                        |
| Attendance                                                                |                                        |                                        |
| Sleep_Hours                                                                |                                        |                                        |

**The bar chart in this lab groups students into bands** (`<1h`, `1-2h`, `2-3h`, `3h+`). Those bands are:

   (circle one)   quantitative          categorical

## Part 2 — See it fail (10 min)

Run the charting script, then the self-check. Record the exact numbers.

```bash
python3 charts.py
python3 self_check.py
```

**Check 1.** The self-check printed ______ / 4 passing.

**Check 2.** `charts.py` saved two files. Name them:

   1. _________________________________________________________________________

   2. _________________________________________________________________________

**Check 3.** The self-check says the charts are missing something. In your own words, what?

   _________________________________________________________________________

   _________________________________________________________________________

**Check 4 — predict.** One chart already has a title; the other has none. Which chart is missing its title?

   _________________________________________________________________________

## Part 3 — Fix 1: the scatter chart

Open the saved file `chart_study_vs_score.png`. Read the scatter plot and answer from the picture, not from the numbers.

**Check 1.** As study hours go up, test scores tend to (circle one):   go up / go down / stay flat.

**Check 2.** The plot's title is there, but the two **axes are unlabeled**. That breaks the label rule from L06. Add them in `charts.py` right after the scatter line.

Write the exact label lines you added (units included):

| Axis | The line I typed |
|------|------------------|
| x | _________________________________________________________________________ |
| y | _________________________________________________________________________ |

**Check 3.** What are the units on each axis? Be specific.

   x-axis units: ______________________________________________________________

   y-axis units: ______________________________________________________________

## Part 4 — Fix 2: the bar chart

Open `chart_study_bands.png`. This one has no title and no axis labels at all.

**Check 1.** What is on the x-axis? (the four bands) ______________________________________

**Check 2.** What is on the y-axis — a *score*, a *time*, or a *count of students*?

   _________________________________________________________________________

That matters: a y-axis that counts students must say so, or the reader will guess wrong.

Write the three label lines you added:

| Element | The line I typed |
|---------|------------------|
| title | _________________________________________________________________________ |
| x-label | _________________________________________________________________________ |
| y-label | _________________________________________________________________________ |

**Check 3 — look hard at the chart.** Count how many bars actually have height.

| Band | How many students fell in it? (read the bar) |
|------|----------------------------------------------|
| `<1h` |                                        |
| `1-2h` |                                        |
| `2-3h` |                                        |
| `3h+` |                                        |

**Check 4.** Every student landed in one band. Which one? __________________

**Check 5.** The bands were written for 0–3+ hours, but run this and write the real range:

```bash
python3 -c "import csv;f=open('data/u2_dataset1_study_habits.csv');v=[float(r['Study_Hours']) for r in csv.DictReader(l for l in f if l.strip() and not l.startswith('#'))];print(min(v),max(v))"
```

   minimum study hours: __________   maximum: __________

**Check 6 — the honest-chart question.** Given that range, is a band chart with three empty bars a fair picture of this data? One sentence, your call.

   _________________________________________________________________________

   _________________________________________________________________________

## Part 5 — Verify 4/4 (5 min)

Re-run the self-check.

```bash
python3 charts.py
python3 self_check.py
```

| After I fixed the labels, the self-check says | ______ / 4 |
|-----------------------------------------------|------------|
| If it is not 4 yet, what check is still failing? |                                        |

**Why does the last check (work committed) still fail until you push?** One sentence.

   _________________________________________________________________________

## Part 6 — Save and submit (5 min)

```bash
cd ~/compmath-u2-viz-basics
git add charts.py chart_study_vs_score.png chart_study_bands.png
git commit -m "add chart titles and axis labels, self-check 4 of 4"
git push
```

| Checkpoint | Result |
|------------|--------|
| Self-check after the push = ___ / 4                                  |                                        |
| My latest commit on github.com shows the changed files              |                                        |
| Did git ask for a password? (if yes, stop and ask — PAT issue)       |                                        |

## Part 7 — Reflection (in your journal, `journal-u2l07.md`)

1. A chart that runs without errors can still be wrong — it just doesn't tell you. Which was harder to notice today: a broken script, or a chart that ran fine but said nothing on its axes?

   _________________________________________________________________________

   _________________________________________________________________________

2. Why does the y-axis of a *count* chart need its own label, when the scatter chart's y-axis was a score?

   _________________________________________________________________________

3. In Check 6 of Part 4 you judged whether the bands fit the data. What would you change about the bands to make the chart more useful?

   _________________________________________________________________________

4. Next time I open a chart I made and it "looks fine," the first thing I will check is:

   _________________________________________________________________________

## Extension (only if you already have 4/4)

Re-band by `Sleep_Hours` instead — your own bands, e.g. `<6`, `6–7`, `7–8`, `8+` — and re-chart. One line: does the shape look different from the study-hours chart?

   _________________________________________________________________________

## TURN IN

☐  Parts 0–6 complete on this sheet — every blank filled with what you actually saw.
☐  `journal-u2l07.md` created in your lab repo, Part 7 answered, `git push` confirmed.
☐  Screenshot to the U2 L07 Classroom assignment by 11:59 PM tonight showing: this completed worksheet, both chart PNGs, and `self_check.py` printing 4 of 4.
☐  Your repo link submitted on the U2 L07 assignment.

Keep this sheet. Labeling a chart is not extra credit — an unlabeled chart is not finished.
