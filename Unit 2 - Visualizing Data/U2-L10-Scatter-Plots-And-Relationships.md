# U2 L10 — Scatter Plots and Relationships

**LO:** create scatter plots to explore relationships between two numerical variables; describe the direction, strength, and form of a relationship in words.

**Estimated time:** 85 minutes (was ~65). We move slower so the vocabulary of relationships becomes fluent.

---

Today is a code-along day. You will build scatter plots from your own dataset, learn to read the shape of a relationship, and — this is the new skill — *describe* a relationship in words, not just point at dots.

---

## PART 0 — SETUP: GET INTO YOUR DATA LAB (15 min)

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

**Write the column names in your notes** — you will pick from this list in the mini-exercise later.

**Why `newline=""` in `open()`:** On Windows, omitting this can cause `csv.DictReader` to misread line endings and produce extra empty rows. On macOS/Linux it's harmless but good habit. The VPS runs Linux, but this makes your code portable.

**Why `list(csv.DictReader(f))` instead of iterating directly:** We want to reuse `rows` multiple times (for different column pairs). Consuming the iterator once exhausts it — `list()` caches all rows in memory (1000 rows × 12 columns is tiny, ~100 KB).

---

## PART 1 — CODE-ALONG: YOUR FIRST SCATTER (20 min)

A scatter plot puts one dot per row: x-position from one column, y-position from another. We are asking: *as study hours go up, do math scores go up too?*

```python
hours = [float(r["Hours Studied Per Week"]) for r in rows]
math  = [float(r["Math Score"]) for r in rows]

plt.scatter(hours, math, s=10, alpha=0.4)
plt.title("Study Hours vs Math Score")
plt.xlabel("Hours Studied Per Week")
plt.ylabel("Math Score")
plt.savefig("scatter_study_vs_math.png", dpi=150)
```

**Breaking down the new parameters:**
- `s=10` makes the dots small (area in points²). Default is 20. With 1,000 points, `s=20` would be a solid blob — you can't see density. Small dots let overlapping points create darkness = density.
- `alpha=0.4` makes them semi-transparent (40% opaque). Where many dots overlap, the color darkens. **Darker region = more students stacked in the same spot.** This is how you see density without a heatmap.
- `plt.savefig(...)` before any `plt.show()` — we're in the REPL, so no window pops up unless you call it. The file is written to your current directory (`~/compmath-u2-data-lab/`).

**Open `scatter_study_vs_math.png` from the file list on the left (VS Code explorer).**

**In your notes, answer *before* we discuss:** Does this look like a positive relationship, a negative one, or no relationship?

> **What to look for:** If the cloud of dots tilts up-right (↗), it's positive. If it tilts down-right (↘), it's negative. If it's a round blob with no tilt, it's no relationship.

---

## PART 2 — THE THREE RELATIONSHIPS (15 min)

In the REPL, plot these three pairs and classify each. **Use `plt.clf()` between plots** — it clears the current figure so the next `savefig` doesn't contain both plots stacked (a classic and confusing bug).

```python
sleep  = [float(r["Sleep Hours Per Night"]) for r in rows]
gpa    = [float(r["Overall GPA"]) for r in rows]
absent = [float(r["Absence Rate"]) for r in rows]

# Pair 1: Sleep vs GPA
plt.scatter(sleep, gpa, s=10, alpha=0.4)
plt.title("Sleep vs GPA")
plt.xlabel("Sleep Hours Per Night")
plt.ylabel("Overall GPA")
plt.savefig("scatter_sleep_vs_gpa.png", dpi=150)
plt.clf()   # CLEAR THE FIGURE

# Pair 2: Absence Rate vs GPA
plt.scatter(absent, gpa, s=10, alpha=0.4)
plt.title("Absence Rate vs GPA")
plt.xlabel("Absence Rate")
plt.ylabel("Overall GPA")
plt.savefig("scatter_absent_vs_gpa.png", dpi=150)
plt.clf()

# Pair 3: Study Hours vs Absence Rate
plt.scatter(hours, absent, s=10, alpha=0.4)
plt.title("Study Hours vs Absence Rate")
plt.xlabel("Hours Studied Per Week")
plt.ylabel("Absence Rate")
plt.savefig("scatter_study_vs_absent.png", dpi=150)
```

**The vocabulary — write one example of each from your own plots:**

| Pattern | Description | Visual |
|---|---|---|
| **Positive** | x goes up, y *tends* to go up. Cloud tilts up-right (↗). | Study vs Math, Sleep vs GPA |
| **Negative** | x goes up, y *tends* to go down. Cloud tilts down-right (↘). | Absence vs GPA |
| **No relationship** | y looks like a random cloud at every x. Flat fuzz, no tilt. | Study vs Absence (likely) |

**Key phrase:** "*tends* to" — not every point follows the pattern. A relationship is a *tendency* across the cloud, not a rule for every dot.

**Check your understanding:**
1. Why `plt.clf()` between plots? What happens if you forget it?
2. In `scatter_sleep_vs_gpa.png`, is the relationship positive, negative, or none? How strong (tight cloud vs wide cloud)?
3. In `scatter_absent_vs_gpa.png`, what direction? Why does that make sense intuitively?

---

## PART 3 — TREND BY EYE (20 min)

You do not need a formula yet to see a trend. **Cover the middle of your plot with your hand, look at the cloud, and ask:** *If I had to draw one straight line through this cloud, where would it go, and how far do the dots stray from it?*

In the REPL, sketch the idea by plotting your guess on top:

```python
plt.scatter(hours, math, s=10, alpha=0.4)
plt.plot([0, 20], [50, 90], color="red")   # my by-eye line: endpoints guessed
plt.title("Study Hours vs Math Score, with guessed trend")
plt.xlabel("Hours Studied Per Week")
plt.ylabel("Math Score")
plt.savefig("scatter_trend_guess.png", dpi=150)
```

**How `plt.plot([0, 20], [50, 90], ...)` works:** It draws a line from (0, 50) to (20, 90). You're guessing the y-value at x=0 and x=20. Adjust the two endpoint pairs until the red line follows the cloud's center.

**Then answer in your notes:**

1. Roughly, how many math-score points do I gain per extra study hour?
   > *Estimate slope:* (90 - 50) / (20 - 0) = 40/20 = **2 points per hour**. Your numbers will differ.

2. How wide is the *scatter* around the line? A tight cloud means the relationship is strong; a wide cloud means it is weak.
   > *Visual estimate:* At 10 hours, do scores range 60–80 (wide) or 72–78 (tight)?

**Why this matters:** This "by-eye trend" is what linear regression formalizes next year. For now, the skill is *seeing* the line and *describing* the scatter width.

---

## PART 4 — MINI-EXERCISE: PICK YOUR OWN PAIR (25 min, in pairs)

With your partner, choose **any two numerical columns** from the column list you wrote in Part 0 that we have **not** plotted yet, and:

1. Build the scatter plot (title, both axis labels, `savefig` with a filename that names both columns).
2. Add a comment at the top of your code cell answering, in one sentence each:
   - What relationship do I see? (positive / negative / none, and how strong — tight or wide cloud)
   - Is there any surprise in the cloud — an outlier, a cluster, a gap?
3. Be ready to show your plot and read your comment to the class.

**Suggested unpicked pairs (from the 12 columns):**
- Science Score vs English Score (both scores — likely positive)
- Parent Education Level vs Overall GPA (ordinal vs numeric — treat education as numeric 1–5)
- Extracurricular Activities vs Absence Rate (count vs rate)
- Sleep Hours vs Math Score (similar to Sleep vs GPA but subject-specific)

**Milestone for today:** Two saved scatter plots (one from the code-along, one of your own choosing), each with a one-sentence written description of the relationship.

---

## PART 5 — DISCUSSION: CORRELATION IS NOT CAUSATION (10 min)

Say it out loud once: **A scatter plot can show that two things move together. It cannot show that one causes the other.**

**Classic example:** Ice cream sales and drowning deaths rise together — summer causes both. The correlation is real; the causation is not between them.

**Our data:** Study hours and GPA move together. The scatter plot *cannot* tell us whether:
- Studying *causes* higher GPA
- Higher GPA *causes* more studying (reverse causality)
- A third thing (parental pressure, natural aptitude, time management) causes both
- The arrow points the other way entirely

**In your notes:** For the pair you chose in Part 4, name **one other explanation** for the relationship that is not "x causes y."

> **Example:** "Sleep vs GPA is positive. Alternative: students with lighter course loads get more sleep *and* higher GPAs — course load is the third variable."

---

## PART 6 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add scatter_study_vs_math.png scatter_sleep_vs_gpa.png scatter_absent_vs_gpa.png scatter_study_vs_absent.png scatter_trend_guess.png
git commit -m "scatter plots: study vs math, sleep vs gpa, absent vs gpa, study vs absent, trend guess"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

1. Take one screenshot showing your saved scatter plots open (or open them side by side and screenshot the whole VS Code window).
2. Make sure your mini-exercise pair, its plot, and its comment are saved and pushed.
3. Run the push loop and confirm it succeeded:

```bash
cd ~/compmath-u2-data-lab
git add -A
git commit -m "mini-exercise: my own scatter pair"
git push
```

Submit the screenshot to the U2 L10 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS (the bigger picture)

**Scatter plots are the microscope of data science.** Every "does X relate to Y?" question starts here. The vocabulary you learned today — positive/negative/none, strong/weak, linear/curved, outliers/clusters/gaps — is the language you'll use in:
- U2 L11: Data Integrity (outliers as data quality signals)
- U2 L13: Histograms (distributions as the y-axis projection)
- U2 L15–L18: Unit 2 project (your threat visualizations will include scatter plots)
- AP Statistics, college research, any job that looks at data

**The one-sentence description discipline:** If you cannot describe a scatter plot in one sentence, you don't understand it well enough to present it. This constraint scales to dashboards, papers, and executive summaries.

**Next:** U2 L11 — Data Integrity and Clean Data  
[U2-L11-Data-Integrity-And-Clean-Data.md](U2-L11-Data-Integrity-And-Clean-Data.md)