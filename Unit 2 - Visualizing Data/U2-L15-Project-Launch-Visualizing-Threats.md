# U2 L15 — Project Launch: Visualizing Threats

**LO:** launch the Unit 2 project; set up the repo and clean the threat dataset; write a claim and sketch three charts.

**Estimated time:** 85 minutes (was ~65). We move slower so the project foundation is solid before build days.

---

This is the **project launch day**. The break assignment (U2 L14 Part 3) was paper-only — you chose a dataset, wrote a claim, and sketched three charts. Today you turn those sketches into a working repo and a clean dataset.

**Your audience is your choice** — security team, principal, or parents — but you must *say who it is* in your analysis, because that choice decides your titles, your wording, and what you highlight.

**Three required visualizations**, all built from **cleaned** data, each saved as a PNG, each with a 1-paragraph written analysis:

1. **Daily timeline** — a line chart of `phishing_reports` and `failed_logins` over the dates in the file. Does trouble spike on certain days? Do the two lines move together?
2. **Weekday vs weekend** — a bar chart comparing average values on weekdays against weekends. Is the attack activity a school-week pattern?
3. **Login success rate** — a histogram of `login_success_rate`. Where do most days sit, and are there suspicious outliers on the low end?

---

## PART 0 — SETUP: REPO READY (15 min)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
ls data/
```

- If your clone lives somewhere else, `cd ~` first and check with `ls`.
- The dataset for this project is `data/u2_campus_threat_daily.csv` (60 rows, synthetic, seed 20261027).

**Open it and read the header row.** Know your column names before you write code — this is the single thing that makes the build days fast.

**Expected columns (verify in your file):**
```
date, phishing_reports, failed_logins, total_logins, login_success_rate
```

**Why this dataset is different:** It has a `date` column (string, ISO format `YYYY-MM-DD`). You will need to parse it for the timeline chart — but `matplotlib` can plot strings directly as categories, so `plt.plot(dates, values)` works if `dates` is a list of strings in order.

---

## PART 1 — CLEAN THE THREAT DATA (25 min)

Create `clean_threats.py` in your repo. This is your **project cleaning script** — it will be submitted alongside your charts.

The threat data is synthetic and deliberately includes:
- Blank cells in `phishing_reports` and `failed_logins`
- Impossible values: `login_success_rate` > 1.0 or < 0.0, negative `failed_logins`
- A comment line at the top (starts with `#`)

**Skeleton for `clean_threats.py`:**

```python
import csv

SANITY = {
    "phishing_reports": (0, 100),
    "failed_logins": (0, 5000),
    "total_logins": (1, 10000),
    "login_success_rate": (0.0, 1.0),
}

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def is_blank(value):
    return value is None or str(value).strip() == ""

# 1. READ (strip comment lines)
with open("data/u2_campus_threat_daily.csv", newline="") as f:
    lines = [ln for ln in f if not ln.startswith("#")]
rows = list(csv.DictReader(lines))

rows_in = len(rows)
print(f"Rows in: {rows_in}")

# 2. CLEAN
clean_rows = []
dropped = {"blank": 0, "impossible": 0, "unparseable": 0}

for r in rows:
    drop_reason = None

    # phishing_reports
    if is_blank(r["phishing_reports"]):
        drop_reason = "blank phishing_reports"
        dropped["blank"] += 1
    else:
        val = to_int(r["phishing_reports"])
        if val is None or not (SANITY["phishing_reports"][0] <= val <= SANITY["phishing_reports"][1]):
            drop_reason = f"impossible phishing_reports={r['phishing_reports']}"
            dropped["impossible"] += 1
        else:
            r["phishing_reports"] = val

    # failed_logins
    if is_blank(r["failed_logins"]):
        drop_reason = "blank failed_logins"
        dropped["blank"] += 1
    else:
        val = to_int(r["failed_logins"])
        if val is None or not (SANITY["failed_logins"][0] <= val <= SANITY["failed_logins"][1]):
            drop_reason = f"impossible failed_logins={r['failed_logins']}"
            dropped["impossible"] += 1
        else:
            r["failed_logins"] = val

    # total_logins
    if is_blank(r["total_logins"]):
        drop_reason = "blank total_logins"
        dropped["blank"] += 1
    else:
        val = to_int(r["total_logins"])
        if val is None or not (SANITY["total_logins"][0] <= val <= SANITY["total_logins"][1]):
            drop_reason = f"impossible total_logins={r['total_logins']}"
            dropped["impossible"] += 1
        else:
            r["total_logins"] = val

    # login_success_rate
    if is_blank(r["login_success_rate"]):
        drop_reason = "blank login_success_rate"
        dropped["blank"] += 1
    else:
        val = to_float(r["login_success_rate"])
        if val is None or not (SANITY["login_success_rate"][0] <= val <= SANITY["login_success_rate"][1]):
            drop_reason = f"impossible login_success_rate={r['login_success_rate']}"
            dropped["impossible"] += 1
        else:
            r["login_success_rate"] = val

    # date stays as string (we don't parse it for sanity)
    if drop_reason:
        print(f"Dropped row {r.get('date', '?')}: {drop_reason}")
        continue

    clean_rows.append(r)

rows_out = len(clean_rows)
rows_dropped = rows_in - rows_out
print(f"Rows out: {rows_out}")
print(f"Rows dropped: {rows_dropped}")
print(f"Dropped by reason: {dropped}")

# Sanity check
assert rows_in == rows_out + rows_dropped, "Count mismatch — cleaning logic bug"

# 3. WRITE
header = ["date", "phishing_reports", "failed_logins", "total_logins", "login_success_rate"]
with open("data/u2_campus_threat_daily_clean.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in clean_rows:
        writer.writerow([r[col] for col in header])

print("Wrote data/u2_campus_threat_daily_clean.csv")
```

**Run it:**
```bash
python3 clean_threats.py
```

**Verify the output:**
- Rows in = 60 (original)
- Rows out + dropped = 60 (assert passes)
- `data/u2_campus_threat_daily_clean.csv` exists and has no blank cells, no impossible values

**Why this matters:** A chart built on dirty data is a lie with axes. Your project submission will include this cleaning script, and I will check that your visualizations use the clean file, not the raw one.

---

## PART 2 — WRITE YOUR CLAIM AND PLAN (15 min)

On paper (your break notes or fresh), finalize:

**My audience:** ______________________ (security team / principal / parents)

**My dataset:** `u2_campus_threat_daily_clean.csv`

**My one-sentence claim:** ________________________________________________

**Three charts:**
1. **Daily timeline** — line chart: x = date, y = phishing_reports AND failed_logins (two lines, legend, alpha=0.7)
2. **Weekday vs weekend** — bar chart: x = ["Weekday", "Weekend"], y = average phishing_reports (and/or failed_logins) — decide which metric supports your claim
3. **Login success rate** — histogram: x = login_success_rate (bins=15), y = count of days

**For each chart, write the exact title you will use** (audience-aware, from U2 L14).

---

## PART 3 — BUILD CHART 1: DAILY TIMELINE (25 min)

Create `project_charts.py` in your repo. Start with Chart 1:

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_campus_threat_daily_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

# Data is already sorted by date in the file
dates = [r["date"] for r in rows]
phishing = [r["phishing_reports"] for r in rows]
failed = [r["failed_logins"] for r in rows]

plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, marker="o", label="Phishing reports", alpha=0.7)
plt.plot(dates, failed, marker="s", label="Failed logins", alpha=0.7)
plt.title("Daily Phishing Reports and Failed Logins — Oct 2026")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.xticks(rotation=45)   # angle the date labels so they don't overlap
plt.tight_layout()        # prevents label cutoff
plt.savefig("chart1_timeline.png", dpi=150)
plt.clf()
```

**Run it:** `python3 project_charts.py`

**Open `chart1_timeline.png` and verify:**
- Two lines, different markers, both visible (alpha=0.7)
- Legend shows both labels
- X-axis dates readable (rotated 45°)
- Title states the finding, not just the columns
- **Y-axis starts at 0** (honest axis — `plt.ylim(bottom=0)` if needed)

**Audience check:** If your audience is parents, is the title jargon-free? If security team, does it highlight the spikes?

---

## PART 4 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add clean_threats.py data/u2_campus_threat_daily_clean.csv project_charts.py chart1_timeline.png
git commit -m "project: clean threats, chart1 timeline"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

1. Screenshot showing `clean_threats.py` terminal output (rows in/out/dropped counts).
2. Screenshot of `chart1_timeline.png` open in VS Code.
3. Your written claim and audience choice (photo of paper or text in a file).

Submit to the U2 L15 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## CHART RULES (for the rest of the project — no exceptions)

- ☐ Title, x-axis label, y-axis label — every time
- ☐ Legend when more than one line or bar series appears
- ☐ `plt.savefig("name.png")` **before** `plt.show()`, or your PNG comes out blank
- ☐ A short comment above each chart's code saying what it shows
- ☐ Clean the data **before** charting — a chart built on dirty data is a lie with axes

---

## WHY THIS MATTERS (the bigger picture)

**The project is not "make three charts" — it is "answer a question with evidence."** The claim you wrote in Part 2 is the hypothesis. The three charts are the evidence. The cleaning script is the audit trail. If any piece is missing, the argument collapses.

**Build days (U2 L16–L17):** You will have two full lab periods to build Charts 2 and 3, write the three analyses, and polish. Students who finish Chart 1 today with a clean dataset and a clear claim will build Charts 2 and 3 in one period each. Students who don't will spend both periods debugging data issues.

**Next:** U2 L16 — Project Lab: Build Your Visualizations  
[U2-L16-Project-Lab-Build-Your-Visualizations.md](U2-L16-Project-Lab-Build-Your-Visualizations.md)