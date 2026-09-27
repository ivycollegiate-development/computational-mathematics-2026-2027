# U2 L15 — Project Launch + Fall Break Prep (Half Day)

**Date:** Oct 30 (Fri) — **HALF DAY, dismissal 12:30**
**LO:** launch the Unit 2 project and set up a clean break so the Nov 9–11 build days are productive.

This is a half day, so the launch is deliberately shorter than a normal period and
nothing is due tonight. You do the setup work here, then you pick the dataset and
write your claim **over the break**. When you come back on Nov 9 you build.

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

## PART 2 — OPEN YOUR REPO AND LOOK AT THE DATA (~15 min)

Not a lab today — just a look. In your VS Code workspace terminal:

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
ls data/
```

- If your clone lives somewhere else, `cd ~` first and check with `ls`.
- The dataset for this project is `data/u2_campus_threat_daily.csv`.
- **Open it and read the header row.** Know your column names before the break —
  this is the single thing that makes Nov 9 fast.

## PART 3 — 🍂 FALL BREAK ASSIGNMENT (launched now, due Nov 8)

**No code over the break. No repo work. This is paper.**

Before you come back on Nov 9, do exactly this, on paper:

1. **Choose your dataset** from `data/`. Options:
   - `u2_campus_threat_daily.csv` (the campus network — 60 days)
   - `dataset1_study_habits.csv`
   - `dataset2_mental_health.csv`
   - `dataset3_activities.csv`
   - `student_performance_data.csv`

2. **Open it once.** Look at the columns and roughly how many rows. Write down
   the column names you will use.

3. **Write the one sentence** your three charts will prove. Not a topic — a claim.
   - Too vague: *"my chart is about logins."*
   - Good: *"Failed logins spike on Monday mornings, so the attack pattern follows the school week, not chance."*
   - Also fine: *"Weekend login success rates are higher than weekday rates, so automated attacks run on the schedule where defenders are not watching."*

4. **Sketch your three charts** on paper — rough boxes, labelled axes, one line
   of notes on what each shows. Ten minutes of sketching saves you an hour of
   coding on Nov 9.

**Turn in:** one photo of the page — your dataset name, the one-sentence claim,
and the three chart sketches. Upload to Google Classroom. **Due 11:59 PM Sunday
Nov 8.**

## PART 4 — ON NOV 9, THIS IS WHAT YOU ALREADY HAVE DONE

- ☐  You picked your dataset
- ☐  You know your column names
- ☐  You have a claim to prove
- ☐  You have three sketched charts
- ☐  Now you just build them

That is why the break work exists. Do not spend Nov 9 choosing a dataset.

## NO TURN-IN TONIGHT

Nothing is due tonight — it is a half day and the break starts tomorrow. Just
make sure you have the assignment above written down or photographed so you
remember it.

## 🇹🇼 BREAK CONTEXT

**Fall Break: Oct 31 – Nov 8.** Classes resume Monday Nov 9. For AP Cybersecurity
the break assignment is a home physical-security audit — also paper, also not a
laptop. The break is ten days. Use the first week to rest and the last two days
to do the work.

## 🧩 SATURDAY CTF

No Saturday sessions in the fall — the CTF series runs in spring 2027. If you
already have a CTF writeup repo, keep it tidy this break. Nothing is required.

## 📋 CHART RULES (for Nov 9 onward — not today)

When you do build, these apply to every chart, no exceptions:

- ☐  title, x-axis label, y-axis label — every time
- ☐  legend when more than one line or bar series appears
- ☐  `plt.savefig("name.png")` **before** `plt.show()`, or your PNG comes out blank
- ☐  a short comment above each chart's code saying what it shows
- ☐  clean the data **before** charting — a chart built on dirty data is a lie with axes
