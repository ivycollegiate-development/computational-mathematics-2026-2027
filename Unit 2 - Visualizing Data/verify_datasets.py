import csv, os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")
ok=lambda c,m: print(("  PASS  " if c else "  FAIL  ")+m)

print("== L02/L03: raw csv.reader on study_habits (must not crash) ==")
with open(f"{D}/u2_dataset1_study_habits.csv") as f: rows=list(csv.reader(f))
ok(len(rows)==53, f"53 lines = header + 52 students (got {len(rows)})")
ok(rows[0][0]=="Student_ID", f"header row[0] == Student_ID (got {rows[0][0]})")
ok(len(rows[1])==5, f"5 columns (got {len(rows[1])})")

print("\n== L07: DictReader + band_of + averaging (the lab's own logic) ==")
with open(f"{D}/u2_dataset1_study_habits.csv") as f: d=list(csv.DictReader(f))
ok(len(d)==52, f"L08 expects len==52 (got {len(d)})")
SANITY={"A":(90,100),"B":(80,89.99),"C":(70,79.99),"Below":(0,69.99)}
def band_of(a):
    if a>=90: return "A"
    if a>=80: return "B"
    if a>=70: return "C"
    return "Below"
tot={}
for r in d:
    b=band_of(float(r["Attendance"])); s=float(r["Test_Score"])
    tot.setdefault(b,[0.0,0]); tot[b][0]+=s; tot[b][1]+=1
avg={b:s/n for b,(s,n) in tot.items()}
print("   band averages:", {k:round(v,2) for k,v in sorted(avg.items())})
ok(len(avg)>=3, f"at least 3 bands populated (got {len(avg)})")
ok(all(0<=v<=100 for v in avg.values()), "all band averages within 0-100")
# the lesson says integer division // truncates; confirm / differs so the bug is real
trunc={b:int(s/n) for b,(s,n) in tot.items()}
ok(any(trunc[b]!=avg[b] for b in avg), "// vs / actually differ somewhere (the L07 bug is real)")
ok(all(0<=v<=100 for v in trunc.values()), "truncated averages still 0-100 (so bug is subtle)")

print("\n== L08: the '#' comment trap on datasets 2 and 3 ==")
for name in ["u2_dataset2_mental_health.csv","u2_dataset3_activities.csv"]:
    with open(f"{D}/{name}",newline="") as f: raw=f.read().splitlines()
    ok(raw[0].startswith("#"), f"{name}: raw[0] starts with '#' ({raw[0][:40]}...)")
    ok(not raw[1].startswith("#"), f"{name}: raw[1] is the real header ({raw[1][:40]})")
    # L11 lines 39-40 assert raw[0]=comment, raw[1]=real header -- NO blank line.
    ok(not raw[2].startswith("#") and "," in raw[2], f"{name}: data starts at raw[2] ({raw[2][:40]})")
    # the lesson's fix: skip leading '#' lines
    lines=[l for l in raw if not l.startswith("#")]
    got=list(csv.DictReader(lines))
    ok(len(got)>0 and "Student_ID" in got[0], f"{name}: fix yields real keys ({list(got[0].keys())[:3]})")

print("\n== L08/L11: performance file — 1000 rows, 12 cols, 4 damage kinds ==")
with open(f"{D}/u2_student_performance_data.csv",newline="") as f: p=list(csv.DictReader(f))
ok(len(p)==1000, f"1000 rows (got {len(p)})")
cols=["Student ID","Gender","Age","Parent Education Level","Hours Studied Per Week",
      "Sleep Hours Per Night","Extracurricular Activities","Math Score","Science Score",
      "English Score","Overall GPA","Absence Rate"]
ok(list(p[0].keys())==cols, "column names match the L08 listing exactly")
blank=sum(1 for r in p for v in r.values() if v is None or str(v).strip()=="")
ok(blank>0, f"(a) blank cells present: {blank}")
SAN={"Age":(10,22),"Math Score":(0,100),"Science Score":(0,100),"English Score":(0,100),
     "Overall GPA":(0.0,4.0),"Hours Studied Per Week":(0,60),"Sleep Hours Per Night":(0,14),
     "Absence Rate":(0.0,1.0)}
imposs={c:0 for c in SAN}
for r in p:
    for c,(lo,hi) in SAN.items():
        try: v=float(r[c])
        except ValueError: continue
        if not (lo<=v<=hi): imposs[c]+=1
ok(sum(imposs.values())>0, f"(b) impossible values present: {sum(imposs.values())} -> {({k:v for k,v in imposs.items() if v})})")
traps=0
for r in p:
    for c in ["Math Score","Hours Studied Per Week","Overall GPA","Age"]:
        v=r[c]
        if v and v.strip():
            try: float(v)
            except ValueError: traps+=1
ok(traps>0, f"(c) type traps present (float() would raise): {traps}")
ok("Age of 3" or any(float(r['Age'])<10 for r in p if r['Age'].replace('.','').isdigit()), "L11's 'Age of 3' example actually exists")

print("\n== L15/L16: campus threat project dataset ==")
with open(f"{D}/u2_campus_threat_daily.csv",newline="") as f: c=list(csv.DictReader(f))
for col in ["Date","Phishing_Reports","Failed_Logins","Successful_Logins","Login_Success_Rate","Day_Type"]:
    ok(col in c[0], f"has {col}")
ok(all(float(r["Login_Success_Rate"])==round(int(r["Successful_Logins"])/(int(r["Successful_Logins"])+int(r["Failed_Logins"])),3) for r in c), "Login_Success_Rate is internally consistent")
import datetime as dt
dates=[dt.date.fromisoformat(r["Date"]) for r in c]
ok(dates==sorted(dates), "dates are chronological (L16 requires this)")
ok(dates[-1]>=dt.date(2026,11,11), f"covers the Nov 9-11 project build (last={dates[-1]})")
wd=[float(r["Phishing_Reports"]) for r in c if r["Day_Type"]=="Weekday"]
we=[float(r["Phishing_Reports"]) for r in c if r["Day_Type"]=="Weekend"]
ok(sum(wd)/len(wd) > sum(we)/len(we), f"weekday phishing > weekend ({sum(wd)/len(wd):.1f} vs {sum(we)/len(we):.1f}) — L16's school-week pattern is real")
ok(all(float(r['Login_Success_Rate'])<0.98 for r in c), "no impossible success rates")
lows=[r for r in c if float(r["Login_Success_Rate"])<0.80]
ok(len(lows)>0, f"outliers on the low end exist for the L16 histogram ({len(lows)} days < 0.80)")
print("\n   lowest 3 success rates:", sorted((float(r['Login_Success_Rate']),r['Date']) for r in c)[:3])
