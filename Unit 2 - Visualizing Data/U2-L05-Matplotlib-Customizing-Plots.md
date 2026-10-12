# U2 L05 — Matplotlib: Customizing Plots

**LO:** create line plots, bar charts, and scatter plots with appropriate labels, colors, and formatting.

**Estimated time:** 75 minutes (was ~50). We move slower so each piece lands.

---

In U2 L03 you made your first plots. Today we make them *readable* — titles, labels, colors, grids, legends — and save them as image files. Three chart types, one script, zero `pip install` (matplotlib 3.10 is already on your machine).

---

## PART 0 — GET ORIENTED (10 min)

First command, always:

```bash
pwd
```

This tells you where you are. If the output does not end with your home directory (`/home/yourname` or `/Users/yourname`), you are not where you think you are — stop and ask.

Then make a folder for today's work and open it in VS Code:

```bash
cd ~
mkdir -p u2-l05
cd u2-l05
touch charts.py
code .
```

**Why this sequence:** `cd ~` guarantees you start from home. `mkdir -p` creates the folder (the `-p` means "no error if it already exists"). `touch charts.py` creates an empty file so VS Code has something to open. `code .` opens the *folder* in VS Code, not just the file — this matters later when you have multiple files.

Everything today goes in `charts.py`. Run it after every part with `python3 charts.py` — you should watch your three charts appear and improve each time.

**Common mistake:** typing `python charts.py` (no `3`). On the VPS, `python` may point to Python 2, which will fail. Always use `python3`.

---

## PART 1 — CODE-ALONG: LINE PLOT (20 min)

A line plot answers: *how does one thing change as another increases?*

We will build this step by step. After each step, run the file and look at the window that pops up.

### Step 1 — Just the data and the plot call

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [62, 68, 71, 79, 84, 91]

plt.plot(hours, scores)
plt.show()
```

Run it. You should see a plain blue line connecting six points. No labels, no title, no grid.

**What just happened:**
- `import matplotlib.pyplot as plt` brings in the plotting interface. The `as plt` part is a convention — you *could* call it `import matplotlib.pyplot as mpl` and then write `mpl.plot(...)` everywhere, but everyone uses `plt` so we do too.
- `plt.plot(hours, scores)` draws a line connecting the points (1,62), (2,68), (3,71), (4,79), (5,84), (6,91). The first list is x-values, the second is y-values. **They must be the same length** — try changing `hours` to 5 items and you will get a `ValueError`.
- `plt.show()` opens the window and blocks until you close it. Your script pauses here.

### Step 2 — Add markers

```python
plt.plot(hours, scores, color="steelblue", marker="o")
```

Run it. Now each data point has a circle on it.

**Why `marker="o"`:** Without it, you only see the line. With it, you see exactly where the measurements were taken. This matters when data is sparse — if you only measured at hours 1, 3, and 6, the line would imply smooth change between them, but the markers show you only have three real observations.

**Why `color="steelblue"`:** The default blue is fine, but `steelblue` is a named color that reads well on white backgrounds and is colorblind-safe. Matplotlib knows ~150 named colors (try `print(plt.colormaps())` later). You can also use hex codes like `"#4A90D9"`.

### Step 3 — Add title and axis labels

```python
plt.title("Test Score vs. Study Hours")
plt.xlabel("Hours studied per week")
plt.ylabel("Test score")
```

Run it. Now the chart tells a complete story on its own.

**Why every plot needs all three:**
- **Title** = the question the chart answers
- **x-label** = what the horizontal axis measures, including units
- **y-label** = what the vertical axis measures, including units

A chart without labels is a rumor, not evidence. If you hand this to someone who was not in class, they should understand it in 5 seconds without you explaining.

### Step 4 — Add a subtle grid

```python
plt.grid(True, alpha=0.3)
```

Run it. Faint gray lines appear behind the data.

**Why `alpha=0.3`:** `alpha` controls transparency (0 = invisible, 1 = solid). The grid should help the eye trace values, not compete with the data. `0.3` is a good default — visible enough to use, faint enough to ignore.

### Complete Part 1 code so far

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

**Check your understanding (write in notes, then discuss):**
1. What happens if `hours` and `scores` have different lengths?
2. What does `alpha=0.3` do to the grid lines?
3. Delete the `xlabel` and `ylabel` lines, run it again — could a stranger read this chart?
4. Change `marker="o"` to `marker="s"` (square) or `marker="^"` (triangle up). What changes?

---

## PART 2 — CODE-ALONG: BAR CHART (15 min)

A bar chart compares *categories*. The key difference from a line plot: the x-axis holds **labels**, not numbers.

```python
# Add this AFTER your line plot code (or in a new cell if using Jupyter)
groups = ["Low sleep", "Mid sleep", "High sleep"]
avg_scores = [70.2, 78.5, 83.1]

plt.bar(groups, avg_scores, color=["#c0392b", "#e67e22", "#27ae60"])
plt.title("Average Score by Sleep Group")
plt.xlabel("Sleep group")
plt.ylabel("Average test score")
plt.show()
```

Run it. Three bars, three different colors.

**Why a list of colors?** `plt.bar` accepts either a single color (all bars same) or a list (one per bar). We passed a list so each group gets its own color — red for low sleep, orange for mid, green for high. This is a *semantic* choice: the colors encode meaning (bad → okay → good), not just decoration.

**Which axis carries what?**
- x-axis = categories (the group names). These are **nominal** — no inherent order, though we ordered them logically.
- y-axis = numbers (average scores). This is **quantitative** — the height means something.

**Common mistake:** passing numbers as strings on the x-axis for a line plot, or passing categories to a line plot. `plt.plot` expects numbers on both axes. `plt.bar` expects categories on x, numbers on y. `plt.scatter` expects numbers on both.

**Check your understanding:**
1. What would happen if we passed just `color="#c0392b"` (one string) instead of the list?
2. Swap `groups` and `avg_scores` in the `plt.bar` call. What breaks? Why?
3. In your own words: when do you use a bar chart vs. a line plot?

---

## PART 3 — CODE-ALONG: SCATTER PLOT (15 min)

A scatter plot answers: *is there a relationship between two number columns?* Unlike a line plot, it does not connect the dots — each point stands alone.

```python
sleep = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5]
gpa = [2.1, 2.4, 2.6, 2.9, 3.2, 3.1, 3.6, 3.8]

plt.scatter(sleep, gpa, color="purple", s=40)
plt.title("GPA vs. Sleep Hours")
plt.xlabel("Hours of sleep per night")
plt.ylabel("GPA")
plt.show()
```

Run it. Eight purple dots, no lines.

**What `s=40` does:** `s` stands for "size" (area in points²). Default is 20. Larger dots are easier to see when points overlap; smaller dots work better for dense data. Try `s=10` and `s=100` to see the difference.

**Why no line?** A line implies *order* and *continuity* — "when x increases, y follows this path." A scatter makes no such claim. It just shows pairs. If the points form a cloud sloping upward, there's a positive association. If they're a blob, there isn't.

**Check your understanding:**
1. Line vs. bar vs. scatter: which one would you use for (a) GPA vs. study hours, (b) average score per grade level, (c) temperature across one day?
2. A scatter shows a pattern — but does a pattern *prove* one thing caused the other? (Hold that thought — it comes back in U2 L10 and U2 L11.)
3. What would happen if `sleep` and `gpa` had different lengths?

---

## PART 4 — LEGENDS AND SAVING (15 min)

When one figure holds two datasets, readers need a legend to tell them apart.

```python
# New figure — start fresh so the legend only applies to these two
plt.figure()

plt.scatter(hours, scores, color="steelblue", label="Class A")
plt.scatter(hours, [s - 6 for s in scores], color="crimson", label="Class B")
plt.title("Scores: Class A vs. Class B")
plt.xlabel("Hours studied")
plt.ylabel("Test score")
plt.legend()
plt.savefig("two_classes.png", dpi=150, bbox_inches="tight")
plt.show()
```

Run it. Two scatter clouds, a legend in the upper right, and a file `two_classes.png` appears in your folder.

### Breaking down the new pieces

**`plt.figure()`** — creates a fresh, empty figure. Without it, the new scatter plots would draw on top of whatever was in the previous window (your bar chart or line plot). Always call `plt.figure()` when you want a clean slate.

**`label=` + `plt.legend()`** — the pair that names your datasets. Every artist (line, scatter, bar) that has a `label=` argument gets an entry in the legend. `plt.legend()` with no arguments places it automatically (usually upper right). You can control position: `plt.legend(loc="lower right")`, `plt.legend(loc="center left")`, etc.

**`plt.savefig("two_classes.png", dpi=150, bbox_inches="tight")`** — writes a PNG into your folder.
- `dpi=150` = dots per inch. 150 is good for documents; 300 for print; 72 for web-only.
- `bbox_inches="tight"` = trims whitespace around the figure. Without it, you often get a wide margin.

**Critical ordering:** `savefig` **must come before** `plt.show()`. `plt.show()` closes the figure and clears it — if you save after, you save a blank image. (Ask me how many times I've done that — it's not zero.)

**Check your understanding:**
1. What happens if you omit `label=` on one of the scatter calls?
2. Move `plt.savefig(...)` after `plt.show()` and run it. What does the PNG look like?
3. Open `two_classes.png` in your file browser. Does it look like the window?

---

## PART 5 — MINI-EXERCISE: YOUR OWN CHART (20 min)

Here are the first 5 rows of the study-habits dataset you will meet in the U2 L07 lab:

```python
students = ["S01", "S02", "S03", "S04", "S05"]
study = [6.5, 2.0, 9.0, 4.5, 12.0]
scores = [71, 58, 84, 66, 95]
sleep  = [7.0, 5.5, 6.0, 8.5, 6.5]
```

In `charts.py`, build **one chart of your choice** from this data — your pick of line, bar, or scatter, your pick of columns, your pick of colors. It must have:

- a title that says what the chart shows (not "Chart 1")
- an x-label and a y-label with units where relevant
- a `savefig` call writing `my_chart.png`

**Suggestions if you're stuck:**
- Scatter: `study` vs `scores` — does more study associate with higher scores?
- Bar: `students` on x, `scores` on y — compare the five students
- Line: only makes sense if `students` has an order (it doesn't really, but you could plot `scores` in order of `study` sorted)

**After you save it, answer in your notes:**
- What does your chart actually show, in one sentence?
- If you cannot say it in one sentence, the chart is not done — revise until you can.

**Why this constraint:** A chart that takes a paragraph to explain is a failed chart. The best visualizations make their point instantly.

---

## PART 6 — TURN IN (15 min)

Add today's work to the lab repo you already have (the one from Unit 1 — `~/compmath-lab`). Copy your files in, then in the terminal:

```bash
cp ~/u2-l05/charts.py ~/u2-l05/my_chart.png ~/compmath-lab/
cd ~/compmath-lab
git add charts.py my_chart.png
git commit -m "U2 L05 three chart types plus custom chart"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.** If you don't have a PAT yet, stop and ask — do not use your account password.

### Spot-check before you say you're done

Open `my_chart.png` and confirm it has:
- [ ] A real title (describes the data, not "Chart 1")
- [ ] Both axis labels with units where relevant
- [ ] A color you chose on purpose — not the matplotlib default blue
- [ ] The file actually opens and is not 0 bytes

If any check fails, fix it and `git add/commit/push` again.

---

## WHY THIS MATTERS (the bigger picture)

You now have the three foundational chart types in your toolkit:

| Chart type | Use when... | x-axis | y-axis |
|------------|-------------|--------|--------|
| Line plot | Showing change over a continuous variable (time, dose, temperature) | **Numeric** | **Numeric** |
| Bar chart | Comparing categories (groups, conditions, labels) | **Categorical** | **Numeric** |
| Scatter plot | Looking for a relationship between two numeric variables | **Numeric** | **Numeric** |

Every visualization you build this year — including the Unit 2 project (U2 L15–L18) — will use these three as building blocks. The customization skills (colors, markers, labels, legends, saving) transfer directly.

**Next:** U2 L06 — Paper Check: Charts So Far  
[U2-L06-Paper-Check-Charts.md](U2-L06-Paper-Check-Charts.md)