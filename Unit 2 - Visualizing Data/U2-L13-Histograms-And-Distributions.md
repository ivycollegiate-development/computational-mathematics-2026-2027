# U2 L13 — Histograms and Distributions

**LO:** create histograms to understand data distributions — shape, spread, center, skew; choose bin count deliberately.

**Estimated time:** 85 minutes (was ~65). We move slower so the histogram vocabulary becomes fluent and bin-choice becomes a conscious decision.

---

Today is a code-along day, and the last lesson of the week. A scatter plot answers "how do two columns relate?" A histogram answers something different: **"what does one column *look like* — where is it centered, how spread out is it, and does it lean?"**

---

## PART 0 — SETUP: START FROM CLEAN DATA (15 min)

The U2 L11 `clean_data.py` produced a cleaned CSV. Use it — that is what it was for:

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

**Write the row count in your notes and compare it to the original 1,000.** Cleaning was not free — this chart sits on fewer students. The provenance statement you wrote in U2 L12 Part 5 should match this number.

**Why `newline=""` again:** Same reason as always — prevents line-ending bugs on Windows; harmless on Linux/macOS but makes your code portable.

---

## PART 1 — CODE-ALONG: YOUR FIRST HISTOGRAM (20 min)

A histogram buckets a single column and counts how many values fall in each bucket:

```python
math = [float(r["Math Score"]) for r in rows]

plt.hist(math, bins=20, color="steelblue", edgecolor="white")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.savefig("hist_math_bins20.png", dpi=150)
```

**Open `hist_math_bins20.png`.** Each bar is a bucket; its height is the count of students in that range.

**In your notes, answer before we discuss:**

1. Where is the tallest bar? That is roughly the **center** of the data.
2. How wide is the range of non-tiny bars? That is the **spread**.
3. Does the cloud of bars lean left, lean right, or sit even? That is the **skew**.

**What `bins=20` does:** Divides the data range (min to max) into 20 equal-width intervals. Each student falls into exactly one bin. The bar height = count of students in that bin.

**Why `edgecolor="white"`:** With 20 bins, bars touch. White edges separate them visually so you can see where one bin ends and the next begins.

---

## PART 2 — BINS ARE A CHOICE, NOT A SETTING (15 min)

Same data, three different bin counts. Run each and save all three:

```python
for b in [5, 20, 100]:
    plt.hist(math, bins=b, color="steelblue", edgecolor="white")
    plt.title(f"Math Scores — {b} bins")
    plt.xlabel("Math Score")
    plt.ylabel("Number of Students")
    plt.savefig(f"hist_math_bins{b}.png", dpi=150)
    plt.clf()   # CLEAR BETWEEN PLOTS
```

**Compare the three images side by side. Write in your notes:**

| Bin count | What you see | When it's useful |
|---|---|---|
| **5 bins** | Big blocks, easy summary, details hidden | Executive summary, very rough shape |
| **20 bins** | The shape is readable — usually the sweet spot | Standard exploration, showing skew/modes |
| **100 bins** | Spiky noise; single students make single bars | Almost never useful — overfits the sample |

**There is no "correct" bin count.** The rule: **Pick the smallest bin count that still shows the shape you care about.** Note your bin choice next to every histogram you ever share.

**Why this matters:** A histogram with 5 bins can hide bimodality (two peaks). A histogram with 100 bins creates phantom peaks from sampling noise. The *same data* tells different stories depending on bin choice — that's a choice *you* make, not a setting the computer picks.

---

## PART 3 — READING A HISTOGRAM: VOCABULARY (15 min)

Plot the other columns and classify each distribution with three words (center, spread, skew):

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

**The vocabulary — write one example of each from your own plots:**

| Term | Definition | Visual |
|---|---|---|
| **Center** | Where the bulk of the bars sit (the "typical" value) | GPA: tallest bar around 3.0 |
| **Spread** | How wide the bars range from lowest to highest | Math: bars from ~40 to ~100 |
| **Skew** | A long tail on one side | Right-skewed = tail stretches right (absence rates: most students low, thin tail of chronic absentees). Left-skewed = tail on the left. |
| **Outlier** | An isolated bar far from the rest | Note: your sanity-bound cleaning already threw out the *impossible* ones. Remaining outliers are *unusual but possible*. |

**Skew direction mnemonic:** "Right-skewed" = tail points right (positive direction). The mean gets pulled toward the tail, so mean > median in right-skewed data.

---

## PART 4 — TWO DISTRIBUTIONS SIDE BY SIDE (20 min)

The real power move: **compare** distributions. Do study groups move with scores? Plot both on the same axes, same bins, semi-transparent:

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

**Critical rules for comparison:**
1. **Same `bins` on both** — otherwise you are comparing apples to oranges (different bin widths = different shapes artificially).
2. **`alpha=0.5`** overlaps the two colors so both shapes stay visible. Without it, the second histogram covers the first.
3. **`label=` + `plt.legend()`** — an unlabeled two-color chart tells nobody anything.
4. **X-axis label = "Value"** because the two columns have different units (hours vs GPA points). For same-unit columns (Math vs English scores), the shared axis is meaningful — try that pair too and note the difference.

**In your notes:** Which distribution is centered higher? Which is more spread out? Do they have the same skew, or different?

---

## PART 5 — MINI-EXERCISE: DESCRIBE ONE COLUMN (20 min, in pairs)

With your partner, pick any column we have **not** histogrammed yet (Science Score, English Score, Sleep Hours, Extracurricular Activities, Parent Education Level), and:

1. Make the histogram with your chosen bin count (saved, titled, labeled).
2. Add a comment answering in one sentence each:
   - Where is the center, and how wide is the spread?
   - What skew does it show, and what real-world story does that skew tell?
3. Be ready to show your plot and read your description to the class.

**Example for Absence Rate (right-skewed):**
> "Center is near 0.05 (5% absence); spread goes to ~0.4. Right-skewed — most students attend regularly, but a long tail of chronic absentees pulls the mean up."

**Why the "real-world story" requirement:** A histogram without interpretation is just decoration. The skew *means* something about the population. Right-skewed absence = a few students miss a lot of school. Left-skewed test scores = most students did well, a few struggled.

**Milestone for today:** Three saved histograms (bins comparison: 5/20/100), one side-by-side comparison, one of your own with a written shape description.

---

## PART 6 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add hist_*.png
git commit -m "histograms: bins comparison, side-by-side, own column"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

1. Make sure all your histograms and your mini-exercise are saved and pushed (Part 6 commands above, plus `git add -A; git commit -m "mini-exercise"; git push` if needed).
2. Take one screenshot showing your bins-comparison images and your mini-exercise histogram open together in VS Code.
3. Confirm the push succeeded.

Submit the screenshot to the U2 L13 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS (the bigger picture)

**Histograms are the shape-revealers.** Every "what does this variable look like?" question starts here. The vocabulary you learned today — center, spread, skew, outlier, bin choice — is the language you'll use in:
- U2 L14: Reflection on audience (how much detail does your audience need?)
- U2 L15–L18: Unit 2 project (your threat visualizations will include histograms of threat frequency, severity, etc.)
- AP Statistics, college research, any job that looks at data

**The bin-choice discipline:** If you cannot explain *why* you chose 20 bins over 10 or 50, you are letting the default decide your story. Defaults are not neutral — they're someone else's choice.

**The side-by-side comparison discipline:** Comparing distributions is how you answer "does Group A look like Group B?" — the core question of A/B testing, clinical trials, and policy evaluation.

**Next:** U2 L14 — Reflection: Visualizing For An Audience  
[U2-L14-Reflection-Visualizing-For-An-Audience.md](U2-L14-Reflection-Visualizing-For-An-Audience.md)