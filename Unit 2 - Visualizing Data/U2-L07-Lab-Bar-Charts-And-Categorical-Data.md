# U2 L07 — LAB: Bar Charts and Categorical Data

**LO:** apply matplotlib skills to real data from a repo; fix two *label-rule* bugs in a charting script and get a self-check from 2/4 to 4/4; recognize when a bar chart's bands, not its labels, are the problem.

**Estimated time:** 85 minutes. We move slower so the debugging process teaches, not just the result.

---

Today you get YOUR OWN copy of a lab repo. It comes with real data files, a charting script with **two `FIX ME` bugs**, and a self-check that starts at **2/4 passing**. Your job: fix the bugs and make it **4/4**.

The paper check you took in U2 L06 covered chart choice, the **label rule**, and reading matplotlib output. That is the foundation for everything below — the two bugs in this lab are both label-rule bugs.

---

## PART 0 — GET YOUR LAB REPO (first 10 minutes)

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

**What you should see.** `ls` shows the charting script `charts.py`, the graders' `self_check.py`, a `README.md`, and a `data/` folder. `ls data/` shows five CSV files, including the three Unit 2 datasets you previewed in U2 L05:

- `u2_dataset1_study_habits.csv`
- `u2_dataset2_mental_health.csv`
- `u2_dataset3_activities.csv`

Today we work with the first one.

---

## PART 1 — MEET THE DATA (10 min)

The study-habits file has **50 rows**, one per student. Its columns:

```
Student_ID, Study_Hours, Test_Score, Attendance, Sleep_Hours
```

Peek at the top of the file:

```bash
head -6 data/u2_dataset1_study_habits.csv
```

**Look closely at the first lines.** The very first line starts with a `#` (a comment), and there is a **blank line** before the real header row. If you hand that file straight to `csv.DictReader`, the reader treats the *comment* as the header, and every column name comes out wrong. Open `charts.py` and find how it guards against this — the loading block near the top filters the file before reading:

```python
lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
```

**In your notes, answer:**

1. Which columns are **numbers** (quantitative) and which is a **category** (categorical)?
   - *Hint:* What would it mean to take an average of it? You can average `Study_Hours` (6.5 hours makes sense). You cannot average `Student_ID` ("S01" + "S02" ÷ 2 = nonsense).
2. From U2 L05: what chart type compares *categories*?

**Expected reasoning:**
- **Quantitative:** `Study_Hours`, `Test_Score`, `Attendance`, `Sleep_Hours` — all are quantities you can add, average, compare with `<`/`>`
- **Categorical:** `Student_ID` — it's an identifier, not a quantity
- **Chart type for comparing categories:** Bar chart (U2 L05 Part 2)

**Why this matters:** The bar chart in this lab takes a *derived* categorical column — study-hour **bands** (`<1h`, `1-2h`, `2-3h`, `3h+`) — and counts how many students fall in each. The number on the y-axis is a **count of students**, not a score. If you confuse the types, you'll label the axis wrong. (That is literally Bug 2.)

---

## PART 2 — SEE IT FAIL (10 min)

Run the charting script:

```bash
python3 charts.py
```

It runs without crashing and saves two files:
- `chart_study_vs_score.png` — a scatter plot of study hours vs test score
- `chart_study_bands.png` — a bar chart counting students by study-hour band

Open both. Notice what's wrong:
- The scatter plot has a title but **no axis labels** — you can't tell what either axis measures.
- The bar chart has **no title and no axis labels at all** — and its y-axis counts *students*, which nothing on the chart says.

Then run the self-check:

```bash
python3 self_check.py
```

You should see **2/4 passing**. Your goal today: **all 4 passing**.

**What the self-check tests (you don't need to read the file, but this is what it verifies):**
1. Both chart files exist (`chart_study_vs_score.png`, `chart_study_bands.png`)
2. The charts have **2 titles and 3 or more axis labels** (the label rule)
3. `charts.py` runs without errors
4. Your work is committed

---

## PART 3 — FIX IT (in pairs, ~45 min)

Open `charts.py`. There are two `FIX ME` comments. We'll tackle them one at a time. **Neither bug makes the script crash** — that is the whole lesson today.

### Bug 1 — The scatter chart has no axis labels

Find the scatter block:

```python
plt.scatter(xs, ys, color="tab:blue")
# FIX ME #1: a chart with no labels is unreadable.
# Add a title and axis labels (what would you call each axis? include units)
plt.title("Study Hours vs Test Score")
```

The title is there, but the **two axes are unlabeled**. Apply the label rule from U2 L06: **every axis gets a label, and the label carries its units.**

- x-axis is study hours → label it with the unit, e.g. `"Study Hours (hours per week)"`
- y-axis is test score → label it with the unit, e.g. `"Test Score (points)"`

Add `plt.xlabel(...)` and `plt.ylabel(...)` right after the title.

**The honest-title upgrade (still Bug 1):** the starter title `"Study Hours vs Test Score"` just names the columns. L06's label rule says the title should **state the finding**. After you look at the scatter, improve it — e.g. `"More Study Hours Go With Higher Test Scores"`.

### Bug 2 — The bar chart has no title and no axis labels

Find the bar-chart block:

```python
plt.figure()
plt.bar(list(bands.keys()), list(bands.values()), color="tab:orange")
# FIX ME #2: this chart should label its axes too -- and the y-axis
# here counts STUDENTS, so make that obvious. Add title + both labels.
```

This chart has none of the three. Add all three:
- **Title** that states the finding
- **x-label** — what the bars *are* (the study-hour band)
- **y-label** — a count of students, and it must **say "students"**, because a reader who sees an unlabeled y-axis will guess it's a score or a time

**Run `python3 self_check.py` after each fix.** Each PASS is a guardrail — don't move to the next fix until the current one passes. After both label fixes you should be at **3/4**; the last check stays red until you commit.

### Look harder at the bar chart (the real point of the day)

Once the labels are on, read the bars. Count how many students are in each band. You will find three of the four bars are **empty** and one bar holds **all 50**.

That is not a labeling problem — the labels are now correct. It is a **band** problem: the bands were written for students who study 0–3+ hours, but run this and look at the real range:

```bash
python3 -c "import csv;f=open('data/u2_dataset1_study_habits.csv');v=[float(r['Study_Hours']) for r in csv.DictReader(l for l in f if l.strip() and not l.startswith('#'))];print(min(v),max(v))"
```

Every student studies between **12.5 and 35.2** hours a week. So a chart with one bar and three blanks is *technically honest but useless*. **In your notes:** if you were allowed to change the band cut-offs, where would you put them? Be ready to defend it.

### Milestone for today: 4/4 passing

And both saved charts must satisfy the label rule:
- **Scatter:** title that states the finding, x-label with units, y-label with units
- **Bar:** title that states the finding, x-label (the band), y-label that names the count of students
- **Honest y-axis:** a bar chart's y-axis starts at 0. A truncated y-axis exaggerates differences between bars.

---

## PART 4 — EXTENSION (if 4/4 early)

- Re-band by `Sleep_Hours` instead of `Study_Hours` — define your own bands (e.g. `6.0–6.5`, `6.5–7.0`, `7.0–7.5`, `7.5–8.0`) and re-chart. Does the shape look different? Do your bands leave empty bars too?
- Add the second dataset (`u2_dataset2_mental_health.csv`: `Stress_Level`, `Hours_Exercise`, `GPA`, `Social_Hours`) and chart GPA grouped by stress level.
- No pandas, no pip installs — matplotlib and `csv` are all you need.

---

## PART 5 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-viz-basics
git add charts.py chart_study_vs_score.png chart_study_bands.png
git commit -m "add chart titles and axis labels, self-check 4 of 4"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.** If you don't have a PAT, stop and ask — do not use your account password.

---

## TURN IN — REPO LINK (due 23:59 tonight)

1. Push your final `charts.py` and both chart PNGs (self-check 4/4).
2. Confirm the push landed: on github.com, open **your** repo and check the latest commit shows the changed files.

**Spot-check before submitting:** Open the charts and verify:
- [ ] The scatter chart has a title, an x-label, and a y-label (units included)
- [ ] The bar chart has a title, an x-label, and a y-label that names the count of students
- [ ] The bar chart's y-axis starts at 0
- [ ] The title states the finding, not just the column names
- [ ] The PNG files are not 0 bytes

Then submit your repo link to the U2 L07 assignment on Google Classroom.

**Early finishers:** Re-cut the study-hour bands so the bars spread out (see Part 3), or reorder the bars from most-studied to least-studied with an explicit list.

---

## WHY THIS MATTERS (the bigger picture)

This lab teaches the **full data-to-viz pipeline** you'll use all year:

1. **Get data** — clone repo, verify CSV structure (and dodge the comment/blank-line trap)
2. **Read data** — `csv.DictReader`, convert strings to numbers
3. **Transform data** — derive categories from numbers (banding)
4. **Aggregate data** — group by category, count (or average) within each group
5. **Visualize** — chart with proper labels and an honest axis
6. **Verify** — self-check guards, visual spot-check
7. **Publish** — git commit, push, submit link

The deepest lesson today is the last one in Part 3: **a chart can run perfectly and still lie.** No error message will ever tell you a bar chart has one bar and three blanks, or that its axes are unlabeled. The self-check catches the missing labels; *you* are the only check on whether the chart tells the truth.

Every subsequent lab (U2 L08, U2 L10, U2 L13, and the Unit 2 project U2 L15–L18) follows this same skeleton. The column names and chart types change; the pipeline doesn't.

**Next:** U2 L08 — Reading Data From Files
[U2-L08-Reading-Data-From-Files.md](U2-L08-Reading-Data-From-Files.md)
