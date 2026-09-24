# U2 L16 — Project Lab: Build Your Visualizations

**LO:** work day — build your three required visualizations with clean data.

Today is a work day. Everything stays in **your own data-lab repo** — you should
walk out with all three charts saved as PNGs and their analysis written.

## PART 0 — OPEN YOUR REPO AND CHECK YESTERDAY (first 10 minutes)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
python3 project.py
```

- Confirm all three PNGs appear (or note exactly which ones are missing — that is
  your first job today).
- Confirm your cleaning step reports the row count **before and after** cleaning.
  If it does not, add that first: you cannot chart data you have not audited.

## PART 1 — THE CHECKLIST (~45 min of work)

Work through this top to bottom. Do not write analysis for a chart that does not
exist yet.

**Data cleaning:**

- ☐  `csv.DictReader` loads `data/u2_campus_threat_daily.csv`
- ☐  bad or missing rows are skipped or fixed, and I print how many I dropped
- ☐  dates parse into a consistent order (the timeline chart must be chronological)

**Chart 1 — daily timeline (line chart):**

- ☐  `phishing_reports` and `failed_logins` plotted over the dates
- ☐  legend shows which line is which
- ☐  title and axis labels present, saved as a PNG

**Chart 2 — weekday vs weekend (bar chart):**

- ☐  averages computed separately for weekdays and weekends
- ☐  two bars (or bar groups), clearly labeled
- ☐  title and axis labels present, saved as a PNG

**Chart 3 — login success rate (histogram):**

- ☐  `login_success_rate` binned sensibly (pick bin count on purpose, not default)
- ☐  title and axis labels present, saved as a PNG

**Writing — one paragraph per chart in `analysis.md`:**

- ☐  what the chart shows, in plain words, for **your named audience**
- ☐  the one number or pattern you most want that audience to notice
- ☐  one honest limitation (a gap in the data, a small sample, an outlier)

## PART 2 — COMMON PITFALLS (~10 min, then back to work)

The three ways this project goes wrong, in order of how often I see them:

1. **Charting uncleaned data.** One blank or malformed row and your timeline has
   a hole or your histogram a phantom bin. Clean first, always.
2. **Missing labels.** An untitled chart is a picture, not an analysis. If I have
   to guess what an axis means, the chart fails.
3. **Uncommented chart code.** Each chart's block needs a one-line comment saying
   what it shows — future-you (and your reviewer tomorrow) needs the map.

If your PNGs are blank: you called `plt.show()` before `plt.savefig()`, or you
closed the figure before saving. Fix the order — save **then** show.

## PART 3 — PARTNER SANITY-CHECK (~15 min)

Swap repos with your partner — read their pushed code on github.com, and open one
of their PNGs:

- Can you tell, from the chart alone, what it shows? No explanation allowed first.
- Does the row count they print match what the cleaning should drop?
- Give one specific compliment and one specific suggestion. "Looks good" is
  not a review.

Fix anything your partner caught **before** you commit.

## PART 4 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add project.py analysis.md
git commit -m "complete three required visualizations with analysis"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

**Milestone for today:** three PNGs + three analysis paragraphs, all in your repo
and pushed.

## TURN IN — PULL REQUEST LINK (due Sunday, 11:59 PM)

1. Push your final `project.py`, `analysis.md`, and all three PNGs.
2. On github.com, open or update a Pull Request from your repo back to the
   original repo (Contribute → Open pull request).

Submit the PR link to this assignment on Google Classroom.

Early finishers: add the fourth "audience choice" chart from Thursday, or write a
second version of one chart for a *different* audience and compare the two.
