"""Generate Unit 3 Comp Math datasets. Fixed seed for reproducibility.

Specs come from the Unit 3 lesson plan (rows 80-111 of the 2026 Jones Lesson
Plans sheet, '26-27 Computational Mathematics') and the lesson sequence:

  L03  mean/median/mode  -> u3_donations.txt        (needs a real even-count case)
  L05  range/variance/sd -> u3_donations.txt        (same file, deeper)
  L08  percentiles / five-number -> u3_survey_times.csv (n large enough to interpolate)
  L09  misleading stats   -> u3_wage_comparison.csv (two groups, a real gap to exaggerate)
  L10  PII / k-anonymity  -> u3_clinic_visits.csv   (identifying columns present on purpose)
  L12  anonymization      -> u3_clinic_visits.csv   (small cells to suppress)
  L14  stats engine lab   -> u3_project_dataset.csv (the students' own CSV)
  L21  outliers / IQR     -> u3_project_dataset.csv (injected outliers with a reason)

Stdlib only -- students never see pandas here (matches the Unit 2 rule).
"""
import csv as _c
import datetime as dt
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUT, exist_ok=True)
rng = random.Random(20261116)  # fixed seed: the Nov 16 Unit 3 opener


def w(name, header, rows, preamble=None, plain=False):
    """Write a dataset. A leading '#' comment is immediately followed by the
    real header -- the same layout Unit 2's L11 taught, so students already
    know to strip comments before parsing."""
    if preamble and "\n" in preamble.strip():
        raise ValueError(f"{name}: preamble must be ONE line -- U2 L11 teaches "
                         "raw[0]=comment, raw[1]=real header, and a second comment "
                         "line would be read as the header.")
    p = os.path.join(OUT, name)
    with open(p, "w", newline="") as f:
        if preamble:
            f.write(preamble + "\n")
        if plain:
            for r in rows:
                f.write(f"{r}\n")
        else:
            wr = _c.writer(f)
            wr.writerow(header)
            wr.writerows(rows)
    if plain:
        n = len(rows)
    else:
        # Count data rows by PARSING, never by line arithmetic, and skip the
        # '#' preamble (csv.reader would otherwise count each comment as data).
        with open(p) as f:
            n = len([r for r in _c.reader(f) if not r[0].startswith("#")]) - 1
    extra = f" +{len(preamble.splitlines())} comment" if preamble else ""
    print(f"  {name}: {n} data rows{extra}")


# ---------- 1. u3_donations.txt -- L03, L05 ----------
# One value per line, no header. 200 entries so percentiles and spread are
# meaningful. Right-skewed on purpose: the mean must visibly disagree with
# the median, which is the whole point of L02's predict-then-reveal preview
# and L06's "which statistic for which claim".
#
# The single 90,000.00 outlier at the end is a mis-keyed entry (a real charity
# typo). It is the pivot for L05 (does sd survive it?) and L21 (IQR rule).
donations = []
for _ in range(199):          # 199 + 1 outlier = 200, an EVEN count
    g = round(rng.lognormvariate(5.5, 0.42), 2)
    donations.append(max(25.0, min(1200.0, g)))
donations += [90000.00]         # the mis-keyed outlier (one extra zero)
rng.shuffle(donations)
w("u3_donations.txt", None, [f"{d:.2f}" for d in donations],
  preamble=("# Alumni donation amounts, one per line, USD. 200 entries. ONE ENTRY IS A MIS-KEY (90000.00) -- it should not be here."),
  plain=True)

# ---------- 2. u3_survey_times.csv -- L08 ----------
# 240 responses so the 90th percentile genuinely falls BETWEEN two values and
# students must interpolate. Includes a '#' comment so comment-stripping is
# still a live skill.
h2 = ["Response_ID", "Wait_Minutes", "Day_Of_Week", "Counter", "Satisfied"]
r2 = []
dow = ["Mon", "Tue", "Wed", "Thu", "Fri"]
for i in range(1, 241):
    base = {"Mon": 14, "Tue": 11, "Wed": 12, "Thu": 16, "Fri": 9}[dow[i % 5]]
    wait = max(2, int(rng.gauss(base, 5)))
    r2.append([f"R{4000+i}", wait, dow[i % 5],
               f"C{1 + i % 4}", "Y" if rng.random() < 0.78 else "N"])
w("u3_survey_times.csv", h2, r2,
  preamble="# Office-hours queue survey. Wait_Minutes is whole minutes, measured at check-in.")

# ---------- 3. u3_wage_comparison.csv -- L09 ----------
# Two job families with a real but modest median gap, and a handful of
# extreme high earners. L09 asks students to build the three ways to
# overstate this gap: truncated y-axis, mean-only, cherry-picked window.
h3 = ["Employee_ID", "Job_Family", "Annual_USD", "Years_Experience", "Region"]
r3 = []
for i in range(1, 121):
    fam = "Analyst" if i % 2 else "Coordinator"
    base = 78000 if fam == "Analyst" else 61000
    pay = rng.gauss(base, 11000)
    r3.append([f"E{7000+i}", fam, int(max(32000, pay)),
               rng.randrange(0, 22),
               rng.choice(["North", "South", "East", "West"])])
# A handful of extreme earners, added after the main loop so the size of the
# distortion is exact rather than whatever the RNG happened to produce.
# Four in the Analyst family, two in Coordinator. These are what a mean-only
# chart hides and what a truncated y-axis exaggerates -- the whole of L09.
for _i in (0, 2, 4, 6):                       # 1-based rows 1,3,5,7 -> Analyst
    r3[_i][2] = int(r3[_i][2] + rng.uniform(230000, 260000))
for _i in (1, 5):                             # 1-based rows 2,6 -> Coordinator
    r3[_i][2] = int(r3[_i][2] + rng.uniform(140000, 160000))
w("u3_wage_comparison.csv", h3, r3,
  preamble="# Anonymized payroll extract, 120 employees. Annual_USD is gross, USD.")

# ---------- 4. u3_clinic_visits.csv -- L10, L12 ----------
# THE PII FILE. Identifying columns are here ON PURPOSE: this is the dataset
# students audit in L10 and then strip in L12.
#   Name + Visit_Date + Rare_Condition together are re-identifying.
# Small cells (n<5) exist on purpose so L12's suppression rule has real work.
h4 = ["Patient_ID", "Name", "Age", "Visit_Date", "Condition",
      "Zip_Code", "Visit_Count", "Insurance_Plan"]
r4 = []
first = ["Avery", "Jordan", "Riley", "Casey", "Morgan", "Quinn", "Hayden", "Skyler",
         "Rowan", "Emerson", "Finley", "Harper", "Kendall", "Logan", "Marley",
         "Nico", "Parker", "Reese", "Sage", "Tatum"]
last = ["Alvarez", "Brennan", "Chen", "Duarte", "Espinoza", "Farah", "Gomez",
        "Haddad", "Ibrahim", "Jensen", "Kowalski", "Lindqvist", "Moreau",
        "Nakamura", "Okafor", "Park", "Quintero", "Rossi", "Singh", "Tran"]
# rare conditions are deliberately infrequent -> small cells for L12
rare = ["Dermatomyositis", "Amyloidosis", "Myelofibrosis", "Von Hippel-Lindau"]
common = ["Hypertension", "Type 2 Diabetes", "Asthma", "Migraine", "ACL Injury"]
base = dt.date(2026, 9, 1)
for i in range(1, 81):
    cond = rare[i % len(rare)] if i % 13 == 0 else rng.choice(common)
    d = base + dt.timedelta(days=rng.randrange(0, 58))
    r4.append([f"P{9000+i}", f"{first[i % 20]}, {last[(i * 7) % 20]}",
               rng.randrange(15, 78), d.isoformat(), cond,
               rng.choice(["40601", "40604", "40605", "40649", "40660", "40602"]),
               rng.choice([1, 1, 1, 2, 2, 3, 5, 8]),
               rng.choice(["PPO-A", "PPO-B", "HMO-C", "Medicaid-D"])])
w("u3_clinic_visits.csv", h4, r4,
  preamble=("# Clinic visit log, 80 visits. CONTAINS DIRECT IDENTIFIERS: Name + Visit_Date + Condition can re-identify a patient. Used in U3 L10 (audit) and L12 (anonymize)."))

# ---------- 5. u3_project_dataset.csv -- L14, L17, L21 ----------
# The students' own project CSV for the Privacy-Aware Stats Dashboard.
# Deliberately contains the same PII shape as the clinic file so the
# project's privacy pass is a real task, not a formality.
h5 = ["Member_ID", "First_Name", "Last_Name", "Age", "City", "Zip_Code",
      "Monthly_Visits", "Spend_USD", "Membership_Tier", "Signup_Date"]
r5 = []
cities = [("Taichung", "402"), ("Taichung", "404"), ("Tainan", "700"),
          ("Kaohsiung", "800"), ("Hsinchu", "300"), ("Taoyuan", "320")]
tiers = ["Basic", "Standard", "Premium", "Enterprise"]
for i in range(1, 121):
    city, zpre = cities[i % len(cities)]
    tier = tiers[(i * 3) % len(tiers)]
    base_spend = {"Basic": 12, "Standard": 28, "Premium": 64, "Enterprise": 140}[tier]
    visits = rng.choice([1, 1, 2, 2, 3, 4, 6, 9])
    sd = dt.date(2025, 9, 1) + dt.timedelta(days=rng.randrange(0, 400))
    r5.append([f"M{2000+i}", first[i % 20], last[(i * 11) % 20],
               rng.randrange(18, 71), city, zpre + str(rng.randrange(1, 99)).zfill(2),
               visits, round(base_spend * visits * rng.uniform(0.7, 1.35), 2),
               tier, sd.isoformat()])
# Three outliers with defensible explanations -- L21 asks students to decide
# KEEP / REPORT / REMOVE and defend it, so each one has a different answer.
r5[7][7] = 18500.00    # Corporate account, one bulk order  -> KEEP, annotate
r5[42][7] = 0.00       # Trial account, never billed         -> REPORT as a real zero
r5[73][7] = 4750.00    # Data-entry error: 47.50 typed 4750   -> REMOVE or correct
w("u3_project_dataset.csv", h5, r5,
  preamble=("# Project dataset for the Privacy-Aware Stats Dashboard (U3 L14/L17/L21). 120 members. Contains First_Name/Last_Name/City/Zip_Code/Signup_Date: run the L12 anonymization pass BEFORE you publish anything."))

print("\nUnit 3 datasets written to:", OUT)
