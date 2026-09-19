# U2 L15 — Project Launch: Visualizing Threats

**LO:** begin the Unit 2 project — create a data visualization that explores a security-related dataset.

Today you launch the Unit 2 project. You build it in **your own data-lab repo**
(`~/compmath-u2-data-lab`) — no new repo today, no new invitations. Everything you
make — code, charts, writing — goes into that repo.

## PART 0 — OPEN YOUR DATA-LAB REPO (first 10 minutes)

In your VS Code workspace terminal — start with `pwd`:

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
ls
```

- If your clone lives somewhere else, `cd ~` first and check with `ls` — the
  repo is `compmath-u2-data-lab` inside `~`.
- `git pull` first, always — grab anything you pushed from another machine.
- Confirm `u2_campus_threat_daily.csv` is sitting in your repo's `data/` folder.
  That is **the** dataset for this project.

## PART 1 — THE PROJECT, IN ONE SCREEN (~15 min)

**The question:** what is happening on our campus network, and what would each
audience need to see to understand it?

**Your audience is your choice** — security team, principal, or parents — but you
must *say who it is* in your analysis, because that choice decides your titles,
your wording, and what you highlight.

**Three required visualizations**, all built from **cleaned** data, each saved as a
PNG, each with a 1-paragraph written analysis:

1. **Daily timeline** — a line chart of `phishing_reports` and `failed_logins`
   over the dates in the file. Does trouble spike on certain days? Do the two
   lines move together?
2. **Weekday vs weekend** — a bar chart comparing average values on weekdays
   against weekends. Is the attack activity a school-week pattern?
3. **Login success rate** — a histogram of `login_success_rate`. Where do most
   days sit, and are there suspicious outliers on the low end?

## PART 2 — SET UP THE FILES (~20 min)

Inside your repo, create:

```bash
touch project.py analysis.md
```

Skeleton for `project.py` — you already own every piece of this from last week:

```python
import csv
import matplotlib.pyplot as plt

# 1. LOAD — csv.DictReader from data/u2_campus_threat_daily.csv
# 2. CLEAN — skip/fix bad rows BEFORE any charting (L13 lesson)
# 3. CHART 1 — daily timeline line chart, plt.savefig("timeline.png")
# 4. CHART 2 — weekday vs weekend bar chart, plt.savefig("weekday.png")
# 5. CHART 3 — login_success_rate histogram, plt.savefig("histogram.png")
```

Rules for every chart, no exceptions:

- ☐  title, x-axis label, y-axis label — every time
- ☐  legend when more than one line or bar series appears
- ☐  `plt.savefig("name.png")` **before** `plt.show()`, or your PNG comes out blank
- ☐  a short comment above each chart's code saying what it shows

## PART 3 — START BUILDING (~40 min)

Work through the pipeline in order. **Clean first, chart second** — a chart built
on dirty data is a lie with axes.

- ☐  Load the CSV and print how many rows you got, before and after cleaning
- ☐  Chart 1 working and saved as a PNG
- ☐  Chart 2 working and saved as a PNG
- ☐  Chart 3 working and saved as a PNG

Do not write any of `analysis.md` yet — first make all three charts exist. The
writing comes tomorrow (U2 L16) once the charts are real.

## PART 4 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add project.py
git commit -m "start project: load, clean, first charts"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

**Milestone for today:** `project.py` in your repo, data loading and cleaning
working, at least Chart 1 saved as a PNG.

## TURN IN — COMMIT YOUR LAUNCH (due 11:59 PM tonight)

1. Push your `project.py` with data loading, cleaning, and at least one chart
   working.
2. Verify on github.com that your latest commit shows the file — open the file in
   the browser and check it is the version you wrote.

Submit your repo link to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

Early finishers: get all three charts done early, or add a fourth "audience
choice" chart — the one visualization *you* think your chosen audience most needs.
