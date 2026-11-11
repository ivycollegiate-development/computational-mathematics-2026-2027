**U2 L16 — Project Lab: Build Visualizations Worksheet**
Computational Mathematics     Name: ____________________     Date: ______________
Check off every step. You are done when all ☐ boxes are ☑.

**SECTION 1 — PROVE THE AUDIT**
**☐  cd ~/compmath-u2-data-lab && git pull**
**☐  python3 clean_threats.py → 6 [PASS] lines, Rows out: 60, Rows dropped: 0**
**☐  python3 clean_threats.py --drill → 3 DROP lines (blank, impossible, bad date), then DRILL PASSED**
☐  SCREENSHOT the drill terminal output (graded evidence for rubric D)
**☐  python3 project_charts.py regenerates chart1_timeline.png**

__________________________________________________________________________________

**SECTION 2 — CHART 2: WEEKDAY VS WEEKEND**
☐  Add Chart 2 block to project_charts.py (bar chart, weekday vs weekend avg phishing reports)
☐  Verify arithmetic: Weekday 7.98 (44 days) | Weekend 2.88 (16 days)
**☐  Title states finding, not subject; y-axis starts at 0; averages printed on bars; plt.clf() after**
☐  Write Chart 2 paragraph in analysis.md (audience, key number, limitation: 44 vs 16 days)

__________________________________________________________________________________

**SECTION 3 — CHART 3: LOGIN SUCCESS RATE**
**☐  Add Chart 3 block to project_charts.py (histogram, bins=15, edgecolor="white")**
☐  Honest finding: Median ~0.56, 4/60 days >0.90, one day at 0.0
☐  Title reflects actual distribution, not "near-total success"
☐  Write Chart 3 paragraph in analysis.md (audience, key number, limitation: outlier drives left tail)

__________________________________________________________________________________

**SECTION 4 — PARTNER GLANCE**
☐  Partner reads Chart 3 only → answers: what does it say? who is it for?
☐  One specific compliment, one specific suggestion → fix before commit

__________________________________________________________________________________

**SECTION 5 — PUSH**
**☐  git add clean_threats.py project_charts.py analysis.md chart2_weekday_weekend.png chart3_success_rate.png**
**☐  git commit -m "project: drill proven, chart2 weekday vs weekend, chart3 success rate"**
**☐  git push (PAT entered, not password)**

__________________________________________________________________________________

**SECTION 6 — TURN IN (submit to U2 L16 Classroom assignment)**
☐  1. Drill screenshot — 3 DROP lines, 3 different reasons, DRILL PASSED
☐  2. chart2_weekday_weekend.png and chart3_success_rate.png pushed, each with paragraph in analysis.md
☐  3. Pull request link submitted

__________________________________________________________________________________

**SECTION 7 — SELF-CHECK (run before submitting)**
**☐  python3 self_check.py → all 5 checks PASS**
    ☐  clean_threats.py audits real file
    ☐  data/u2_campus_threat_daily_clean.csv = 60 rows, 5 cols, no blanks
    ☐  clean_threats.py --drill drops 3 rows
    ☐  All 3 chart PNGs exist, not blank
    ☐  analysis.md has 3 substantial paragraphs (>120 chars each)

__________________________________________________________________________________

**KEY NUMBERS TO REMEMBER**
| Chart | Expected Result |
|-------|-----------------|
| Chart 1 (L15) | Timeline: 2 lines, legend, alpha=0.7, y-axis at 0 |
| Chart 2 | Weekday avg 7.98 (44 days) | Weekend avg 2.88 (16 days) |
| Chart 3 | Median 0.56, 4 days >0.90, one day 0.0 |

__________________________________________________________________________________

**COMMON PITFALLS**
**☐  plt.savefig() BEFORE plt.show() or plt.clf() (blank PNG otherwise)**
**☐  bins=15 on Chart 3 (not default 10)**
☐  Title = finding for your audience, not column names
☐  Y-axis starts at 0 (honest axis)
☐  analysis.md paragraphs >120 chars each
☐  Drill screenshot shows 3 different drop reasons