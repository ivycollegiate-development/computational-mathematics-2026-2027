"""Verify the Unit 3 datasets against what the LESSONS actually need.

This deliberately tests statistical properties, not just row counts: a lesson
that says 'the mean and the median must visibly disagree' fails if the data
happens to be symmetric. Counts alone would have passed a useless file.
"""
import csv as _c
import os
import statistics as st

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
P = F = 0


def chk(cond, label, detail=""):
    global P, F
    if cond:
        P += 1
        print(f"  PASS  {label}" + (f"  ({detail})" if detail else ""))
    else:
        F += 1
        print(f"  FAIL  {label}" + (f"  ({detail})" if detail else ""))


def raw(name):
    """Read exactly the way U2 L11 taught: strip '#' lines, then the real
    header is the next row and data begins after it. Returns (header, rows)
    where rows are dicts keyed by the header -- so a column rename in the
    lesson cannot silently produce an empty list."""
    with open(os.path.join(OUT, name)) as f:
        rows = [ln.rstrip("\n") for ln in f]
    body = [r for r in rows if not r.startswith("#")]
    cols = next(_c.reader([body[0]]))
    return body[0], [dict(zip(cols, rec)) for rec in _c.reader(body[1:])]


print("=== u3_donations.txt (L03 mean/median/mode, L05 spread, L21 outliers) ===")
raws = open(os.path.join(OUT, "u3_donations.txt")).read().splitlines()
body = [r for r in raws if not r.startswith("#")]
vals = [float(r) for r in body]
chk(len(vals) == 200, "200 donation entries", f"got {len(vals)}")
chk(len(vals) % 2 == 0, "even count -> L03's interpolated median case is live")
med2 = (sorted(vals)[99] + sorted(vals)[100]) / 2
chk(all(v > 0 for v in vals), "all values positive")
m = st.mean(vals)
chk(m > st.median(vals) * 1.15,
    "right-skewed: mean exceeds median by >15%",
    f"mean {m:.2f} vs median {st.median(vals):.2f}")
chk(90000.0 in vals, "the 90,000.00 mis-key is present and labelled")
clean = [v for v in vals if v < 5000]
chk(abs(st.mean(clean) - m) > 100,
    "the 90,000.00 outlier moves the mean by >100 (L05's whole point)",
    f"mean with {m:.2f} vs without {st.mean(clean):.2f}")
q1, q3 = st.quantiles(clean, n=4)[0], st.quantiles(clean, n=4)[2]
iqr = q3 - q1
chk(90000.0 > q3 + 1.5 * iqr, "IQR rule flags the 90,000.00 outlier (L21)",
    f"Q3+1.5*IQR = {q3 + 1.5*iqr:.2f}")
chk(len(set(vals)) > 180, "values are not mostly-duplicated", f"{len(set(vals))} distinct")

print("\n=== u3_survey_times.csv (L08 percentiles / five-number summary) ===")
hdr, rows = raw("u3_survey_times.csv")
chk(hdr.startswith("Response_ID"), "real header is row 0 after stripping '#'", hdr[:34])
chk(len(rows) == 240, "240 responses", f"got {len(rows)}")
waits = sorted(int(r["Wait_Minutes"]) for r in rows)
# the lesson's interpolation question is only real if P90 falls between values
lo, hi = waits[int(0.90 * len(waits)) - 1], waits[int(0.90 * len(waits))]
chk(lo <= hi and lo > 0, "P90 is computable and positive", f"P90 between {lo} and {hi}")
chk(len(set(waits)) >= 8, "spread is wide enough for a real five-number summary",
    f"{len(set(waits))} distinct wait values")
five = [min(waits), st.quantiles(waits, n=4)[0], st.median(waits),
        st.quantiles(waits, n=4)[2], max(waits)]
chk(five == sorted(five), "five-number summary is monotone", str(five))
chk(five[0] >= 1, "min wait is plausible (>=1 min)", str(five[0]))

print("\n=== u3_wage_comparison.csv (L09 misleading statistics) ===")
hdr, rows = raw("u3_wage_comparison.csv")
chk(len(rows) == 120, "120 employees", f"got {len(rows)}")
d = rows
an = [int(r["Annual_USD"]) for r in d if r["Job_Family"] == "Analyst"]
co = [int(r["Annual_USD"]) for r in d if r["Job_Family"] == "Coordinator"]
chk(len(an) == 60 and len(co) == 60, "60 per job family")
chk(st.median(an) > st.median(co), "Analyst median exceeds Coordinator (the real gap)")
gap_median = st.median(an) - st.median(co)
gap_mean = st.mean(an) - st.mean(co)
chk(gap_mean > gap_median * 1.15,
    "mean gap OVERSTATES the median gap by >15% (L09's truncation lesson)",
    f"mean gap {gap_mean:.0f} vs median gap {gap_median:.0f}")
chk(max(an) > 150000 and max(co) > 150000,
    "both families have extreme high earners a mean-only chart would hide")
chk(all(32000 <= int(r["Annual_USD"]) for r in d), "no negative or absurd salaries")

print("\n=== u3_clinic_visits.csv (L10 PII audit, L12 anonymization) ===")
hdr, rows = raw("u3_clinic_visits.csv")
chk(len(rows) == 80, "80 visits", f"got {len(rows)}")
d = rows
for col in ("Name", "Patient_ID", "Zip_Code", "Visit_Date", "Condition"):
    chk(col in hdr.split(","), f"PII column present: {col}")
names = [r["Name"] for r in d]
chk(len(set(names)) >= 15, "many distinct names -> a name column IS identifying",
    f"{len(set(names))} distinct names")
rare_n = sum(1 for r in d if r["Condition"] in
             ("Dermatomyositis", "Amyloidosis", "Myelofibrosis", "Von Hippel-Lindau"))
chk(0 < rare_n < 20, "rare conditions form SMALL CELLS for L12 suppression",
    f"{rare_n} rare-condition rows")
by_cond = {}
for r in d:
    by_cond[r["Condition"]] = by_cond.get(r["Condition"], 0) + 1
small = [c for c, n in by_cond.items() if n < 5]
chk(len(small) >= 1, "at least one condition has n<5 (suppression has real work)",
    f"small cells: {small}")
chk(len(set(r["Zip_Code"] for r in d)) <= 8, "few zips -> quasi-identifiers exist",
    f"{len(set(r['Zip_Code'] for r in d))} zips")
chk(len(set(r["Name"] + r["Visit_Date"] + r["Condition"] for r in d)) == len(d),
    "Name+Date+Condition is UNIQUE per row -> genuinely re-identifying")

print("\n=== u3_project_dataset.csv (L14 engine, L17 dashboard, L21 outliers) ===")
hdr, rows = raw("u3_project_dataset.csv")
chk(len(rows) == 120, "120 members", f"got {len(rows)}")
d = rows
chk(len(set(r["Member_ID"] for r in d)) == len(d), "Member_ID is unique (a key)")
spend = [float(r["Spend_USD"]) for r in d]
chk(len(set(spend)) > 100, "spend values are mostly distinct", f"{len(set(spend))} distinct")
srt = sorted(spend)
q1, q3 = st.quantiles(srt, n=4)[0], st.quantiles(srt, n=4)[2]
fence = q3 + 1.5 * (q3 - q1)
outs = [v for v in spend if v > fence]
chk(len(outs) >= 3, "IQR rule flags >=3 outliers for L21 to adjudicate",
    f"{len(outs)} above {fence:.2f}: {sorted(outs)[-4:]}")
chk(0.0 in spend, "a legitimate 0.00 exists (L21: report, do not delete)")
chk(any(v > 10000 for v in spend), "a legitimate bulk-order outlier exists (L21: keep)")
zips = [r["Zip_Code"] for r in d]
small_cells = {}
for z in zips:
    small_cells[z] = small_cells.get(z, 0) + 1
chk(min(small_cells.values()) < 20, "at least one zip has a small cell (L15 privacy pass)",
    f"smallest zip cell n={min(small_cells.values())}")
for col in ("First_Name", "Last_Name", "City", "Zip_Code", "Signup_Date"):
    chk(col in hdr, f"identifying column present for the privacy pass: {col}")
chk(all(18 <= int(r["Age"]) <= 70 for r in d), "ages are plausible")

print("\n=== L11 PARSE CONTRACT (raw[0]=comment, raw[1]=real header) ===")
# U2 L11 taught: comment at raw[0], REAL header at raw[1], data at raw[2].
# A two-line preamble would put a comment in the header slot and break every
# student parser, so this is checked on every generated file.
for _fn in sorted(os.listdir(OUT)):
    if _fn.endswith(".txt"):
        continue
    with open(os.path.join(OUT, _fn)) as f:
        _raw = [ln.rstrip("\n") for ln in f]
    chk(len(_raw) >= 3, f"{_fn}: has at least comment+header+1 data row")
    chk(_raw[0].startswith("#"), f"{_fn}: raw[0] IS the comment", _raw[0][:40])
    chk(not _raw[1].startswith("#"),
        f"{_fn}: raw[1] is the REAL header, not a second comment", _raw[1][:40])
    _h = next(_c.reader([_raw[1]]))
    _r = next(_c.reader([_raw[2]]))
    chk(len(_h) == len(_r) and all(c.strip() for c in _h),
        f"{_fn}: header width matches row 2 width ({len(_h)} cols)", f"{_h[:3]}")

print(f"\n{'='*56}\nchecks run: {P+F}   passed: {P}   failed: {F}")
print("ALL DATASETS OK" if F == 0 else "FIX THE FAILURES ABOVE")
