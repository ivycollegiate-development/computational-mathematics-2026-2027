# U2 L03 — Launch: What Makes a Good Visualization

**LO:** understand the purpose of data visualization and produce your first matplotlib plot with a title, axis labels, and units.

Yesterday numbers became information. Today information becomes a **picture**.
We meet `matplotlib` — the standard Python plotting library — and make our
first chart. matplotlib 3.10 is already installed on your workspace; you never
need to install anything.

## PART 1 — WHY PICTURES BEAT TABLES (10 min)

Here are two views of the same data:

```text
Table:   Mon 12, Tue 18, Wed 9, Thu 22, Fri 30, Sat 25, Sun 15
```

Now picture it as a line climbing and dipping through the week. In your
notes, before any code:

- Which took longer to absorb — reading the table or imagining the line?
- From the table alone: how fast can you find the biggest two-day jump?
  From a line chart? This is the actual superpower: **shape**.

Key ideas to write down:

- A table stores values; a chart exposes **shape, trend, and outliers**.
- A chart is an *argument* — someone chose what to plot. We'll spend
  Thursday learning to question that choice.

## PART 2 — CODE-ALONG: YOUR FIRST PLOT (15 min)

Open your workspace. First command, always:

```bash
pwd
```

Then the REPL:

```bash
python3
```

The import everyone in the data world uses:

```python
import matplotlib.pyplot as plt
```

(`pyplot` is matplotlib's drawing toolbox; everyone shortens it to `plt`.
Never type the long name again.)

A line chart is just x-values and y-values:

```python
days  = [1, 2, 3, 4, 5, 6, 7]
temps = [12, 18, 9, 22, 30, 25, 15]

plt.plot(days, temps)
plt.show()
```

A window opens with your first chart. Now answer in your notes, then try:

- Swap the lists: `plt.plot(temps, days)`. What broke, and what does that
  tell you about which list is x and which is y?
- Add a second call `plt.plot(days, [t + 5 for t in temps])` before
  `plt.show()`. What happens?

## PART 3 — ANATOMY OF A PLOT: THE PARTS EVERY CHART NEEDS (15 min)

A chart without labels is a guess. A complete chart has:

1. a **title** — what question does this chart answer?
2. an **x-axis label with units** — what is along the bottom?
3. a **y-axis label with units** — what is along the side?

Rebuild your chart properly:

```python
plt.plot(days, temps, marker="o")
plt.title("Daily High Temperature, One Week (°C)")
plt.xlabel("Day of Week (1 = Monday)")
plt.ylabel("High Temperature (°C)")
plt.grid(True)
plt.show()
```

In your notes, then verify:

- What did `marker="o"` change? When would you want it, when not?
- Why does every axis label here carry a unit? What is the chart *saying*
  that a bare line could not?
- Try `plt.plot(days, temps, marker="o", linestyle="--")`. Describe the
  change in one sentence.

## PART 4 — PLOT OUR REAL DATA: STUDY HOURS (15 min)

Yesterday's dataset, today as a picture. Still in the REPL (or open a file
`first_plot.py` in VS Code if you prefer):

```python
import csv
import matplotlib.pyplot as plt

with open("/tmp/u2_datasets/u2_dataset1_study_habits.csv") as f:
    rows = list(csv.reader(f))

data = rows[2:]                       # skip comment line + header
hours  = [float(r[1]) for r in data]
scores = [float(r[2]) for r in data]

plt.scatter(hours, scores, s=15)
plt.title("Test Score vs. Study Hours (52 Students)")
plt.xlabel("Weekly Study Hours (hrs)")
plt.ylabel("Test Score (points)")
plt.grid(True)
plt.show()
```

In your notes:

- Why `scatter` here instead of `plot`? (Each student is one *point*, not a
  step in a sequence.)
- Does the cloud of points lean which way? What does the lean suggest?
- Find in your mind's eye where a point at (1.0, 95) would sit. Would it
  fit the pattern? That's an **outlier** — Thursday's whole topic.

## PART 5 — SAVEFIG: MAKE IT A TURN-IN (10 min)

`plt.show()` puts a chart on a screen; `plt.savefig()` writes it to a file
you can submit and keep:

```python
plt.savefig("score_vs_hours.png", dpi=150)
```

(Run it *before* or instead of `show()` in a script — after the window
closes, the figure is gone.)

Back in the terminal, check it exists:

```bash
ls -lh score_vs_hours.png
```

In your notes: what does `dpi=150` change, and why does a crisp image matter
when someone else grades your chart?

## PART 6 — DISCUSSION: WHAT MAKES A CHART GOOD? (5 min)

With your table, rank these sins from worst to least-worst and defend it:

- no title
- no axis labels
- no units
- y-axis starting at a weird number to exaggerate a trend
- rainbow colors on a black background

One sentence each in your notes. Thursday we judge a real news chart
against exactly this list.

## PART 7 — SAVE YOUR WORK + PUSH (last 10 min)

Put your script and image in your lab repo:

```bash
cd ~/compmath-lab
git add first_plot.py score_vs_hours.png
git commit -m "first matplotlib plot with labeled axes"
git push
```

- **Asked for a username/password?** GitHub username + PAT, never your
  password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 3 labeled temperature chart on screen
2. your Part 4 scatter plot of the real dataset
3. `ls -lh score_vs_hours.png` proving the file exists
4. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

Early finishers: add a second series to the scatter (Sleep_Hours vs.
Test_Score) in a different color with `label=` and `plt.legend()`, and save
a second PNG.
