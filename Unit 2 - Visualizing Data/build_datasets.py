"""Generate Unit 2 Comp Math datasets. Fixed seed for reproducibility.
Specs are taken verbatim from the lesson files (U2 L07, L08, L10, L11, L13, L15, L16).
"""
import csv, os, random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUT, exist_ok=True)
rng = random.Random(20261019)  # fixed seed: the Oct 19 lab date

def w(name, header, rows, preamble=None):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="") as f:
        if preamble:
            # L11 line 39-40 shows raw[0] = comment, raw[1] = REAL header.
            # No blank line between them, and the lesson's fix only filters '#'.
            f.write(preamble + "\n")
        wr = csv.writer(f)
        wr.writerow(header)
        wr.writerows(rows)
    n = sum(1 for _ in open(p)) - 1 - (1 if preamble else 0)
    print(f"  {name}: {n} data rows (+1 header{' +1 comment' if preamble else ''})")

# ---------- 1. u2_dataset1_study_habits.csv — 52 rows (L07 asserts 52) ----------
h1 = ["Student_ID","Study_Hours","Test_Score","Attendance","Sleep_Hours"]
r1 = []
for i in range(1, 53):
    study = round(rng.uniform(0, 40), 1)
    sleep  = round(rng.uniform(3, 11), 1)
    # correlation: more study + sleep -> better score, so the bar chart shows a real story
    score = round(min(100, max(0, 45 + study*0.9 + sleep*1.4 + rng.gauss(0,6))), 1)
    att   = round(min(100, max(0, 70 + study*0.5 + rng.gauss(0,8))), 1)
    r1.append([f"S{1000+i}", study, score, att, sleep])
w("u2_dataset1_study_habits.csv", h1, r1)
# NOTE: this file must be CLEAN — it is the L07 lab data and L08 tests it for len==52
# but L08 also says all three "messy files" have quirks. L08 expects 52 exactly here.

# ---------- 2. u2_dataset2_mental_health.csv — '#' comment line (L11) ----------
h2 = ["Student_ID","Stress_Level","Hours_Exercise","GPA","Social_Hours"]
r2 = []
for i in range(1, 61):
    stress = rng.choice(["Low","Moderate","High"])
    r2.append([f"M{2000+i}", stress,
               round(rng.uniform(0,12),1), round(rng.uniform(2.0,4.0),2),
               round(rng.uniform(0,10),1)])
w("u2_dataset2_mental_health.csv", h2, r2,
  preamble="# Mental health and academic load survey. Units: exercise=hours/week, social=hours/week, GPA on 4.0 scale.")

# ---------- 3. u2_dataset3_activities.csv — '#' comment line (L11) ----------
h3 = ["Student_ID","Activity","Minutes_Per_Week","Team_Or_Individual"]
r3 = []
acts = ["Soccer","Basketball","Music","Robotics","Debate","Art","Track","None"]
for i in range(1, 51):
    a = rng.choice(acts)
    r3.append([f"A{3000+i}", a,
               0 if a=="None" else rng.randrange(60, 900, 15),
               "Individual" if a in ("Music","Art","None") else "Team"])
w("u2_dataset3_activities.csv", h3, r3,
  preamble="# Extracurricular activity log. Minutes_Per_Week is student-reported.")

# ---------- 4. u2_student_performance_data.csv — 1000 rows, DIRTY on purpose ----------
# Columns exactly as listed in U2 L08 line 27-29.
h4 = ["Student ID","Gender","Age","Parent Education Level","Hours Studied Per Week",
      "Sleep Hours Per Night","Extracurricular Activities","Math Score","Science Score",
      "English Score","Overall GPA","Absence Rate"]
edu = ["Some College","Bachelor's Degree","Master's Degree","Doctorate","High School"]
genders = ["Female","Male"]
r4 = []
for i in range(1, 1001):
    study = rng.uniform(0, 60)
    sleep  = rng.uniform(3, 12)
    base   = 40 + study*0.7 + sleep*1.1 + rng.gauss(0, 9)
    math   = round(min(100, max(0, base + rng.gauss(0,5))), 1)
    sci    = round(min(100, max(0, base + rng.gauss(0,7))), 1)
    eng    = round(min(100, max(0, base + rng.gauss(0,6))), 1)
    gpa    = round(min(4.0, max(0.0, (math+sci+eng)/300*4.0 + rng.gauss(0,0.2))), 2)
    r4.append([f"STU{i:04d}", rng.choice(genders), rng.randint(14,18),
               rng.choice(edu), round(study,1), round(sleep,1),
               rng.randint(0,4), math, sci, eng, gpa,
               round(rng.uniform(0, 0.25), 3)])
# --- inject the four kinds of damage U2 L11 promises ---
inj = 0
# (a) blank cells  (L11 Part 1: is_blank / drop-or-fill)
for idx in rng.sample(range(1000), 60):
    col = rng.choice(h4[1:])
    r4[idx][h4.index(col)] = ""
    inj += 1
# (b) impossible values (L11 Part 2 SANITY bounds: Age 3, GPA 9)
for idx in rng.sample(range(1000), 25):
    r4[idx][h4.index("Age")] = rng.choice([3, 4, 7, 99])
    inj += 1
for idx in rng.sample(range(1000), 12):
    r4[idx][h4.index("Overall GPA")] = rng.choice([9, 9.5, 4.7, -1])
    inj += 1
for idx in rng.sample(range(1000), 8):
    r4[idx][h4.index("Absence Rate")] = rng.choice([1.8, 2.4, -0.3])
    inj += 1
# (c) type traps: a stray STRING in a numeric column so float() raises ValueError
for idx in rng.sample(range(1000), 15):
    r4[idx][h4.index("Math Score")] = rng.choice(["N/A","unknown","--","tbd"])
    inj += 1
for idx in rng.sample(range(1000), 8):
    r4[idx][h4.index("Hours Studied Per Week")] = rng.choice(["a lot","none","??"])
    inj += 1
# (d) impossible study/sleep outliers
for idx in rng.sample(range(1000), 6):
    r4[idx][h4.index("Hours Studied Per Week")] = round(rng.uniform(70, 200), 1)
    inj += 1
w("u2_student_performance_data.csv", h4, r4)
print(f"    injected {inj} damaged cells (blank/impossible/type-trap)")

# ---------- 5. u2_campus_threat_daily.csv — the Unit 2 PROJECT dataset (L15/L16) ----------
# Needs: phishing_reports, failed_logins, login_success_rate, dates.
# L16 requires weekday-vs-weekend to show a school-week pattern -> weekend dip.
h5 = ["Date","Phishing_Reports","Failed_Logins","Successful_Logins","Login_Success_Rate","Day_Type"]
r5 = []
import datetime as dt
d = dt.date(2026, 9, 1)
end = dt.date(2026, 11, 11)   # covers the Nov 9-11 project build; L19 is no-electronics
while d <= end:
    weekend = d.weekday() >= 5
    phish  = rng.randint(4, 12) if weekend else rng.randint(10, 26)
    failed = rng.randint(6, 14) if weekend else rng.randint(18, 48)
    ok     = rng.randint(40, 90) if weekend else rng.randint(150, 400)
    # Incident days: login success collapses, failed logins spike. L16 requires
    # a bimodal/skewed distribution for the histogram and a real outlier story.
    if d in {dt.date(2026,9,17), dt.date(2026,10,2), dt.date(2026,10,27)}:
        failed = rng.randint(120, 180)
        ok     = rng.randint(25, 55)
    rate   = round(ok/(ok+failed), 3)
    r5.append([d.isoformat(), phish, failed, ok, rate, "Weekend" if weekend else "Weekday"])
    d += dt.timedelta(days=1)
w("u2_campus_threat_daily.csv", h5, r5)
print("\nAll datasets written to", OUT)
