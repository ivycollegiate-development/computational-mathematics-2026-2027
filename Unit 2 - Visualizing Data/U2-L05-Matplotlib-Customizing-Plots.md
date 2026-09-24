# U2 L05 — Matplotlib: Customizing Plots

**LO:** create line plots, bar charts, and scatter plots with appropriate labels, colors, and formatting.

Monday you made your first plots (U2 L03). Today we make them *readable* —
titles, labels, colors, grids, legends — and save them as image files. Three
chart types, one script, zero `pip install` (matplotlib 3.10 is already on your
machine).

## PART 0 — GET ORIENTED (5 min)

First command, always:

```bash
pwd
```

Then make a folder for today's work and open it in VS Code:

```bash
cd ~
mkdir -p u2-l05
cd u2-l05
touch charts.py
```

Everything today goes in `charts.py`. Run it after every part with
`python3 charts.py` — you should watch your three charts appear and improve
each time.

## PART 1 — CODE-ALONG: LINE PLOT (15 min)

A line plot answers: *how does one thing change as another increases?*

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [62, 68, 71, 79, 84, 91]

plt.plot(hours, scores, color="steelblue", marker="o")
plt.title("Test Score vs. Study Hours")
plt.xlabel("Hours studied per week")
plt.ylabel("Test score")
plt.grid(True, alpha=0.3)
plt.show()
```

First answer in your notes, then run and check:

- What does `marker="o"` change about the line?
- What does `alpha=0.3` do to the grid lines?
- Delete the `xlabel` and `ylabel` lines, run it again, and imagine you are
  showing this chart to someone who was not in class. Could they read it?

**Rule for the rest of the year:** every plot gets a title, an x-label, and a
y-label. A chart without labels is a rumor, not evidence.

## PART 2 — CODE-ALONG: BAR CHART (10 min)

A bar chart compares *categories*.

```python
groups = ["Low sleep", "Mid sleep", "High sleep"]
avg_scores = [70.2, 78.5, 83.1]

plt.bar(groups, avg_scores, color=["#c0392b", "#e67e22", "#27ae60"])
plt.title("Average Score by Sleep Group")
plt.xlabel("Sleep group")
plt.ylabel("Average test score")
plt.show()
```

In your notes:

- Why did we pass a *list* of colors? What would happen with just one?
- Which axis carries the categories, and which carries the numbers?

## PART 3 — CODE-ALONG: SCATTER PLOT (10 min)

A scatter plot answers: *is there a relationship between two number columns?*

```python
sleep = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5]
gpa = [2.1, 2.4, 2.6, 2.9, 3.2, 3.1, 3.6, 3.8]

plt.scatter(sleep, gpa, color="purple", s=40)
plt.title("GPA vs. Sleep Hours")
plt.xlabel("Hours of sleep per night")
plt.ylabel("GPA")
plt.show()
```

In your notes:

- Line vs. bar vs. scatter: which one would you use for (a) GPA vs. study
  hours, (b) average score per grade level, (c) temperature across one day?
- A scatter shows a pattern — but does a pattern *prove* one thing caused the
  other? (Hold that thought — it comes back later this unit.)

## PART 4 — LEGENDS AND SAVING (10 min)

When one figure holds two datasets, readers need a legend:

```python
plt.scatter(hours, scores, color="steelblue", label="Class A")
plt.scatter(hours, [s - 6 for s in scores], color="crimson", label="Class B")
plt.title("Scores: Class A vs. Class B")
plt.xlabel("Hours studied")
plt.ylabel("Test score")
plt.legend()
plt.savefig("two_classes.png", dpi=150, bbox_inches="tight")
plt.show()
```

- `label=` + `plt.legend()` is the pair that names your datasets.
- `plt.savefig("name.png", dpi=150)` writes a PNG into your folder — open it
  and check it looks right. Save the file **before** `plt.show()`, or you will
  save a blank image (ask me how many times I have done that).

## PART 5 — MINI-EXERCISE: YOUR OWN CHART (15 min, on your own)

Here are the first 5 rows of the study-habits dataset you will meet in Monday's
lab:

```python
students = ["S01", "S02", "S03", "S04", "S05"]
study = [6.5, 2.0, 9.0, 4.5, 12.0]
scores = [71, 58, 84, 66, 95]
sleep  = [7.0, 5.5, 6.0, 8.5, 6.5]
```

In `charts.py`, build **one chart of your choice** from this data — your pick of
line, bar, or scatter, your pick of columns, your pick of colors. It must have:

- a title that says what the chart shows (not "Chart 1")
- an x-label and a y-label with units where relevant
- a `savefig` call writing `my_chart.png`

Then answer in your notes: what does your chart actually show, in one
sentence? If you cannot say it in one sentence, the chart is not done.

## PART 6 — TURN IN

Add today's work to the lab repo you already have (the one from Unit 1 —
`~/compmath-lab`). Copy your files in, then in the terminal:

```bash
cp ~/u2-l05/charts.py ~/u2-l05/my_chart.png ~/compmath-lab/
cd ~/compmath-lab
git add charts.py my_chart.png
git commit -m "U2 L05 three chart types plus custom chart"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

**Spot-check before you say you're done:** open `my_chart.png` and confirm it
has a real title, both axis labels, and a color you chose on purpose — not the
matplotlib default blue.
