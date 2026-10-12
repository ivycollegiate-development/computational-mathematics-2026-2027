# U2 L16 — Project Lab: Build Your Visualizations

**LO:** work day — build your three required visualizations with clean data; write audience-aware analysis for each.

**Estimated time:** 85 minutes (was ~65). We move slower so every chart is built on clean data, labeled correctly, and explained for its audience.

---

Today is a work day. Everything stays in **your own data-lab repo** — you should walk out with all three charts saved as PNGs and their analysis written in `analysis.md`.

---

## PART 0 — OPEN YOUR REPO AND RE-READ THE LAUNCH (15 min)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
```

**First, verify your foundation from U2 L15:**

1. `data/u2_campus_threat_daily_clean.csv` exists and has rows.
2. Run your cleaning script and confirm the row counts:

```bash
python3 clean_threats.py
```

**Write the output in your notes:**
- Rows in: ______
- Rows out: ______
- Rows dropped: ______

3. Open `project_charts.py` — confirm Chart 1 (timeline) code is there and runs:

```bash
python3 project_charts.py
```

**Confirm `chart1_timeline.png` appears and looks correct.**

If any of these are missing, **that is your first job today.** You cannot build Charts 2 and 3 on a broken foundation.

---

## PART 1 — THE CHECKLIST (55 min of work)

Work through this top to bottom. Do not write analysis for a chart that does not exist yet.

### Data cleaning (must be done before any chart)

- ☐ `csv.DictReader` loads `data/u2_campus_threat_daily.csv`
- ☐ Comment lines (starting with `#`) are stripped before parsing
- ☐ Bad or missing rows are skipped or fixed, and you **print how many you dropped and why** (blank, impossible, unparseable)
- ☐ Dates parse into a consistent order (the timeline chart must be chronological — the CSV is already sorted, but verify)

### Chart 1 — Daily timeline (line chart) — should be done from U2 L15

- ☐ `phishing_reports` and `failed_logins` plotted over the dates (two lines)
- ☐ Different markers (`marker="o"`, `marker="s"`) and `alpha=0.7` so both are visible
- ☐ Legend shows which line is which (`label=` + `plt.legend()`)
- ☐ Title states the finding, audience-aware (e.g., "Phishing Reports Spike on Weekdays — Security Team Alert" vs "Campus Network Attacks Follow School Schedule — Parents' View")
- ☐ X-axis label: "Date", Y-axis label: "Count"
- ☐ `plt.xticks(rotation=45)` + `plt.tight_layout()` so dates don't overlap
- ☐ Y-axis starts at 0 (honest axis) — add `plt.ylim(bottom=0)` if needed
- ☐ Saved as `chart1_timeline.png` with `plt.savefig()` **before** any `plt.show()`
- ☐ `plt.clf()` after saving

### Chart 2 — Weekday vs weekend (bar chart)

- ☐ Compute averages separately for weekdays and weekends:
  ```python
  # Parse date string to determine weekday/weekend
  from datetime import datetime
  def is_weekend(date_str):
      return datetime.strptime(date_str, "%Y-%m-%d").weekday() >= 5  # 5=Sat, 6=Sun
  ```
- ☐ Accumulate sums and counts for each group, then average (float division `/`, not `//`)
- ☐ Two bars (or grouped bars if showing both phishing and failed logins), clearly labeled
- ☐ Title states the finding, audience-aware
- ☐ X-axis label: "Day type", Y-axis label: "Average count" (or "Average failed logins")
- ☐ Saved as `chart2_weekday_weekend.png`
- ☐ `plt.clf()` after saving

### Chart 3 — Login success rate (histogram)

- ☐ Extract `login_success_rate` values from clean rows
- ☐ Choose bin count **on purpose** (not default): `bins=15` is a good starting point for 0–1 rates
- ☐ Title states the finding, audience-aware (e.g., "Most Days Near 100% Login Success — But 3 Days Drop Below 90%")
- ☐ X-axis label: "Login success rate", Y-axis label: "Number of days"
- ☐ `edgecolor="white"` so bins are separable
- ☐ Saved as `chart3_success_rate.png`
- ☐ `plt.clf()` after saving

### Writing — one paragraph per chart in `analysis.md`

Create `analysis.md` in your repo. For **each chart**, write one paragraph that includes:

1. **What the chart shows, in plain words, for your named audience** — no jargon if audience is parents; technical terms OK for security team.
2. **The one number or pattern you most want that audience to notice** — be specific: "The Monday spike to 12 phishing reports (vs 3–4 on other days)" not "there are spikes."
3. **One honest limitation** — a gap in the data, a small sample (60 days), an outlier that might be noise, the synthetic nature of the data.

**Example paragraph for Chart 1 (security team audience):**

> This timeline shows daily phishing reports (blue circles) and failed logins (orange squares) across 57 clean days in October 2026. The pattern is clear: both metrics spike on Mondays and Tuesdays, with phishing reports averaging 11 on Mondays vs 3–4 on Wed–Fri, and failed logins following a similar but noisier trend. The weekend drop-off is sharp — near zero for both. The one number the security team should note: Monday phishing reports are 3× the Wednesday baseline, suggesting automated campaigns target the start of the work week. Limitation: this is 60 days of synthetic data — real traffic would have more variance and longer attack sequences.

---

## PART 2 — COMMON PITFALLS (10 min, then back to work)

The three ways this project goes wrong, in order of how often I see them:

1. **Charting uncleaned data.** One blank or malformed row and your timeline has a hole or your histogram a phantom bin. **Clean first, always.** Your `clean_threats.py` output is the proof you did it.
2. **Missing labels.** An untitled chart is a picture, not an analysis. If I have to guess what an axis means, the chart fails. **Title, x-label, y-label — every time.**
3. **Uncommented chart code.** Each chart's block needs a one-line comment saying what it shows — future-you (and your reviewer tomorrow) needs the map.

**If your PNGs are blank:** You called `plt.show()` before `plt.savefig()`, or you closed the figure before saving. Fix the order — **save then show**.

---

## PART 3 — PARTNER SANITY-CHECK (15 min)

Swap repos with your partner — read their pushed code on github.com, and open one of their PNGs:

- Can you tell, from the chart alone, what it shows? **No explanation allowed first.**
- Does the row count they print match what the cleaning should drop?
- Give **one specific compliment** and **one specific suggestion**. "Looks good" is not a review.

**Fix anything your partner caught BEFORE you commit.**

---

## PART 4 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add project_charts.py analysis.md chart1_timeline.png chart2_weekday_weekend.png chart3_success_rate.png
git commit -m "complete three required visualizations with analysis"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

**Milestone for today:** Three PNGs + three analysis paragraphs, all in your repo and pushed.

---

## TURN IN — PULL REQUEST LINK (due 23:59 tonight)

1. Push your final `project_charts.py`, `analysis.md`, and all three PNGs.
2. On github.com, open or update a Pull Request from your repo back to the original repo (Contribute → Open pull request).

Submit the PR link to the U2 L16 assignment on Google Classroom.

**Early finishers:** Add the fourth "audience choice" chart from U2 L14, or write a second version of one chart for a *different* audience and compare the two.

---

## WHY THIS MATTERS (the bigger picture)

**The project is an argument, not an art show.** Every chart is a premise; the analysis paragraphs are the reasoning; the cleaning script is the evidence that the premises are sound. If you skip the cleaning audit, the argument has no foundation. If you skip the analysis, the chart is just decoration.

**U2 L17 (tomorrow) is peer review:** You will read a partner's full project and they will read yours. The review form asks: *Does the evidence support the claim? Is the cleaning auditable? Are the charts honest for the stated audience?* If your work today cannot answer "yes" to those, tomorrow's review will expose it.

**Next:** U2 L17 — Reflection: Peer Review Of Visualizations  
[U2-L17-Reflection-Peer-Review-Of-Visualizations.md](U2-L17-Reflection-Peer-Review-Of-Visualizations.md)