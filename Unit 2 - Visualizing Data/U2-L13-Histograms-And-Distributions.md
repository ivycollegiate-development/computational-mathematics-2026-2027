# U2 L13 — Histograms and Distributions

**LO:** create histograms to understand data distributions — shape, spread, center.

Today is a code-along day, and the last lesson of the week. A scatter plot
answers "how do two columns relate?" A histogram answers something different:
"what does one column *look like* — where is it centered, how spread out is
it, and does it lean?"

## PART 0 — SETUP: START FROM CLEAN DATA (first 10 min)

Monday's `clean_data.py` produced a cleaned CSV. Use it — that is what it
was for:

```bash
pwd
cd ~/compmath-u2-data-lab
ls data
python3 clean_data.py        # rerun if the _clean file is missing
python3
```

Then in the REPL:

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_student_performance_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

print(len(rows))   # rows in — write this number in your notes
```

Write the row count in your notes and compare it to the original 1,000.
Cleaning was not free — this chart sits on fewer students.

## PART 1 — CODE-ALONG: YOUR FIRST HISTOGRAM (15 min)

A histogram buckets a single column and counts how many values fall in each
bucket:

```python
math = [float(r["Math Score"]) for r in rows]

plt.hist(math, bins=20, color="steelblue", edgecolor="white")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.savefig("hist_math_bins20.png", dpi=150)
```

Open `hist_math_bins20.png`. Each bar is a bucket; its height is the count of
students in that range. In your notes, answer before I say it:

- Where is the tallest bar? That is roughly the **center** of the data.
- How wide is the range of non-tiny bars? That is the **spread**.
- Does the cloud of bars lean left, lean right, or sit even? That is the
  **skew**.

## PART 2 — BINS ARE A CHOICE, NOT A SETTING (10 min)

Same data, three different bin counts. Run each and save all three:

```python
for b in [5, 20, 100]:
    plt.hist(math, bins=b, color="steelblue", edgecolor="white")
    plt.title(f"Math Scores — {b} bins")
    plt.xlabel("Math Score")
    plt.ylabel("Number of Students")
    plt.savefig(f"hist_math_bins{b}.png", dpi=150)
    plt.clf()
```

Compare the three images side by side. Write in your notes:

- With **5 bins**: big blocks, easy summary, details hidden.
- With **20 bins**: the shape is readable — usually the sweet spot.
- With **100 bins**: spiky noise; single students make single bars.

There is no "correct" bin count. The rule: **pick the smallest bin count that
still shows the shape you care about.** Note your bin choice next to every
histogram you ever share.

## PART 3 — READING A HISTOGRAM: VOCABULARY (10 min)

Plot the other columns and classify each distribution with three words
(center, spread, skew):

```python
gpa   = [float(r["Overall GPA"]) for r in rows]
absent = [float(r["Absence Rate"]) for r in rows]

plt.hist(gpa, bins=20, color="seagreen", edgecolor="white")
plt.title("Distribution of Overall GPA")
plt.xlabel("Overall GPA")
plt.ylabel("Number of Students")
plt.savefig("hist_gpa.png", dpi=150)
plt.clf()

plt.hist(absent, bins=20, color="indianred", edgecolor="white")
plt.title("Distribution of Absence Rate")
plt.xlabel("Absence Rate")
plt.ylabel("Number of Students")
plt.savefig("hist_absence.png", dpi=150)
```

The vocabulary — write one example of each from your own plots:

- **Center:** where the bulk of the bars sit (the "typical" value).
- **Spread:** how wide the bars range from lowest to highest.
- **Skew:** a long tail on one side. *Right-skewed* = tail stretches right
  (absence rates usually look like this: most students low, a long thin tail
  of chronic absentees). *Left-skewed* = tail on the left.
- **Outlier:** an isolated bar far from the rest — and remember, your
  sanity-bound cleaning already threw out the impossible ones.

## PART 4 — TWO DISTRIBUTIONS SIDE BY SIDE (15 min)

The real power move: **compare** distributions. Do study groups move with
scores? Plot both on the same axes, same bins, semi-transparent:

```python
hours = [float(r["Hours Studied Per Week"]) for r in rows]

plt.hist(hours, bins=20, alpha=0.5, label="Study Hours", color="steelblue")
plt.hist(gpa,   bins=20, alpha=0.5, label="GPA", color="seagreen")
plt.title("Study Hours vs GPA — side by side")
plt.xlabel("Value")
plt.ylabel("Number of Students")
plt.legend()
plt.savefig("hist_study_vs_gpa.png", dpi=150)
```

- Same `bins` on both — otherwise you are comparing apples to oranges.
- `alpha=0.5` overlaps the two colors so both shapes stay visible.
- `label=` + `plt.legend()` — an unlabeled two-color chart tells nobody
  anything.

In your notes: which distribution is centered higher? Which is more spread
out? Do they have the same skew, or different? (Note: these two columns have
different units — that is why the x-axis just says "Value." For an honest
shape comparison of two *similar* columns, like Math vs English scores, the
shared axis is meaningful. Try that pair too, and note the difference.)

## PART 5 — MINI-EXERCISE: DESCRIBE ONE COLUMN (in pairs, ~15 min)

With your partner, pick any column we have **not** histogrammed yet, and:

1. Make the histogram with your chosen bin count (saved, titled, labeled).
2. Add a comment answering in one sentence each:
   - Where is the center, and how wide is the spread?
   - What skew does it show, and what real-world story does that skew tell?
3. Be ready to show your plot and read your description to the class.

**Milestone for today:** three saved histograms (bins comparison), one
side-by-side comparison, one of your own with a written shape description.

## PART 6 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add hist_*.png
git commit -m "histograms: bins comparison, side-by-side, own column"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

1. Make sure all your histograms and your mini-exercise are saved and pushed
   (PART 6 commands above, plus `git add -A; git commit -m "mini-exercise";
   git push` if needed).
2. Take one screenshot showing your bins-comparison images and your
   mini-exercise histogram open together in VS Code.
3. Confirm the push succeeded.

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
