# U2 L10 — Scatter Plots and Relationships

**LO:** create scatter plots to explore relationships between two numerical variables.

Today is a code-along day. You will build scatter plots from your own dataset,
learn to read the shape of a relationship, and — this is the new skill —
*describe* a relationship in words, not just point at dots.

## PART 0 — SETUP: GET INTO YOUR DATA LAB (first 10 min)

Open your terminal and get to the repo:

```bash
pwd
cd ~/compmath-u2-data-lab
ls data
```

Start Python in the REPL:

```bash
python3
```

Then load our workhorse imports:

```python
import csv
import matplotlib.pyplot as plt
```

Verify you can see the data directory from Python:

```python
with open("data/u2_student_performance_data.csv", newline="") as f:
    rows = list(csv.DictReader(f))

print(len(rows))          # how many students?
print(rows[0].keys())     # what columns exist?
```

Write the column names in your notes — you will pick from these list in the
mini-exercise later.

## PART 1 — CODE-ALONG: YOUR FIRST SCATTER (15 min)

A scatter plot puts one dot per row: x-position from one column, y-position
from another. We are asking: *as study hours go up, do math scores go up too?*

```python
hours = [float(r["Hours Studied Per Week"]) for r in rows]
math  = [float(r["Math Score"]) for r in rows]

plt.scatter(hours, math, s=10, alpha=0.4)
plt.title("Study Hours vs Math Score")
plt.xlabel("Hours Studied Per Week")
plt.ylabel("Math Score")
plt.savefig("scatter_study_vs_math.png", dpi=150)
```

- `s=10` makes the dots small — 1,000 big dots would be a blob.
- `alpha=0.4` makes them see-through, so dense areas look darker. Darker
  region = more students stacked in the same spot.
- Open `scatter_study_vs_math.png` from the file list on the left.

In your notes, answer *before* I say it: does this look like a positive
relationship, a negative one, or no relationship?

## PART 2 — THE THREE RELATIONSHIPS (10 min)

In the REPL, plot these three pairs and classify each:

```python
sleep  = [float(r["Sleep Hours Per Night"]) for r in rows]
gpa    = [float(r["Overall GPA"]) for r in rows]
absent = [float(r["Absence Rate"]) for r in rows]

plt.scatter(sleep, gpa, s=10, alpha=0.4)
plt.title("Sleep vs GPA")
plt.xlabel("Sleep Hours Per Night")
plt.ylabel("Overall GPA")
plt.savefig("scatter_sleep_vs_gpa.png", dpi=150)
plt.clf()   # clear the figure between plots!
```

The vocabulary — write one example of each from your own plots:

- **Positive:** x goes up, y tends to go up. (Cloud tilts up-right.)
- **Negative:** x goes up, y tends to go down. (Cloud tilts down-right.)
- **No relationship:** y looks like a random cloud at every x. (Flat fuzz.)

**Warning:** `plt.clf()` between plots, or your second `savefig` contains both
plots stacked — a classic and confusing bug.

## PART 3 — TREND BY EYE (15 min)

You do not need a formula yet to see a trend. Cover the middle of your plot
with your hand, look at the cloud, and ask: *if I had to draw one straight line
through this cloud, where would it go, and how far do the dots stray from it?*

In the REPL, sketch the idea by plotting your guess on top:

```python
plt.scatter(hours, math, s=10, alpha=0.4)
plt.plot([0, 20], [50, 90], color="red")   # my by-eye line: endpoints guessed
plt.title("Study Hours vs Math Score, with guessed trend")
plt.xlabel("Hours Studied Per Week")
plt.ylabel("Math Score")
plt.savefig("scatter_trend_guess.png", dpi=150)
```

Adjust the two endpoint pairs `[0, 20]` and `[50, 90]` until the red line
follows the cloud. Then answer in your notes:

- Roughly, how many math-score points do I gain per extra study hour?
- How wide is the *scatter* around the line? A tight cloud means the
  relationship is strong; a wide cloud means it is weak.

## PART 4 — MINI-EXERCISE: PICK YOUR OWN PAIR (in pairs, ~20 min)

With your partner, choose **any two numerical columns** from the column list
you wrote in Part 0 that we have **not** plotted yet, and:

1. Build the scatter plot (title, both axis labels, `savefig` with a filename
   that names both columns).
2. Add a comment at the top of your cell answering, in one sentence each:
   - What relationship do I see? (positive / negative / none, and how strong)
   - Is there any surprise in the cloud — an outlier, a cluster, a gap?
3. Be ready to show your plot and read your comment to the class.

**Milestone for today:** two saved scatter plots, one of your own choosing,
each with a one-sentence written description of the relationship.

## PART 5 — DISCUSSION: CORRELATION IS NOT CAUSATION (5 min)

Say it out loud once: **a scatter plot can show that two things move together.
It cannot show that one causes the other.** Ice cream sales and drowning deaths
rise together — summer causes both. Our data might show study hours and GPA
moving together; it cannot tell us whether studying *causes* the GPA, whether
a third thing causes both, or whether the arrow points the other way.

In your notes: for the pair you chose in Part 4, name one *other* explanation
for the relationship that is not "x causes y."

## PART 6 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add scatter_study_vs_math.png scatter_sleep_vs_gpa.png scatter_trend_guess.png
git commit -m "scatter plots: study vs math, sleep vs gpa, trend guess"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

1. Take one screenshot showing both your saved scatter plots open (or open
   them side by side and screenshot the whole VS Code window).
2. Make sure your mini-exercise pair, its plot, and its comment are saved and
   pushed.
3. Run the push loop and confirm it succeeded:

```bash
cd ~/compmath-u2-data-lab
git add -A
git commit -m "mini-exercise: my own scatter pair"
git push
```

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
