# U2 L08 — Reading Data From Files

**LO:** load data from CSV files into Python, handle real-world messiness (comment lines, missing values), and prepare clean lists ready for visualization.

**Estimated time:** 90 minutes (was ~75). We move slower so the data-loading habits become automatic.

---

Today you get YOUR OWN copy of the **data lab** repo — a different one from U2 L07's. Real datasets, including a 1000-row performance file, and the honest truth about real data: it is messy. By the end you will have a clean per-row list ready to plot in U2 L10.

---

## PART 0 — GET YOUR DATA-LAB REPO (first 15 minutes)

**Step 1:** Check your school Gmail — accept the invitation to your own private repo. (If you don't see it, check Spam/Promotions, then ask.)

**Step 2:** Your repo is named `compmath-u2-data-lab-<your-name>_student` under the `ivycollegiate-development` organization.

**Step 3:** Clone it. Start with `pwd` — always know where you are.

```bash
pwd
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-data-lab-$(whoami)_student.git compmath-u2-data-lab
cd compmath-u2-data-lab
ls
ls data/
```

**Why this sequence:** Same as U2 L07 — `pwd` confirms location, `cd ~` guarantees predictable path, `$(whoami)` matches your username to the repo suffix, `ls` verifies.

**The star of today:** `data/u2_student_performance_data.csv` — **1000 rows** with these columns:
- Student ID, Gender, Age, Parent Education Level
- Hours Studied Per Week, Sleep Hours Per Night, Extracurricular Activities
- Math Score, Science Score, English Score, Overall GPA, Absence Rate

---

## PART 1 — CODE-ALONG: `csv.DictReader` END TO END (20 min)

Create your working file:

```bash
touch load_scores.py
```

No pandas, no pip installs — matplotlib and `csv` are preinstalled on the VPS (Python 3.10+, matplotlib 3.10.9).

Start with the minimal load:

```python
import csv

with open("data/u2_student_performance_data.csv") as f:
    rows = list(csv.DictReader(f))

print(len(rows))          # 1000
print(rows[0].keys())     # the column names
print(rows[0]["Overall GPA"])
```

**What just happened:**
- `csv.DictReader(f)` reads the **first row as the keys** (column names) and hands you every subsequent row as a `dict`.
- `list(...)` consumes the iterator into a list so you can index it (`rows[0]`, `len(rows)`).
- **Critical catch:** Every value arrives as a **string**, even numbers. `"3.7"` not `3.7`. You **must** convert: `gpa = float(row["Overall GPA"])`.

**In the REPL (`python3`), first answer, then test:**

1. What type is `rows[0]["Age"]` before you convert it?
   > **Answer:** `str` — `"16"` not `16`.

2. What happens with `float("")` — and what error name is that?
   > **Answer:** `ValueError: could not convert string to float: ''`. Empty strings crash `float()`. Real data has holes — you'll handle this in Part 4.

**Why `DictReader` over `reader`:** `reader` gives you lists (you'd need to remember column indices). `DictReader` gives you dicts with names — self-documenting and robust to column reordering.

---

## PART 2 — CODE-ALONG: SELECT, FILTER, AGGREGATE (25 min)

Three moves, all with plain dicts and lists. Append to `load_scores.py` as we go.

### Select — columns you care about (skip the rest)

```python
records = [{"gpa": float(r["Overall GPA"]),
            "study": float(r["Hours Studied Per Week"]),
            "sleep": float(r["Sleep Hours Per Night"])}
           for r in rows]
```

**What this does:** Builds a new list of *smaller* dicts with only the three columns you need, and converts them to `float` immediately. The original `rows` list (1000 dicts × 12 keys) is still there if you need other columns later.

**Why not modify in place?** Keeping the raw `rows` separate from the cleaned `records` lets you restart the cleaning without re-reading the file.

### Filter — keep only what you need

```python
heavy = [r for r in records if r["study"] >= 10]
print(len(heavy))   # how many study 10+ hours/week?
```

**What this does:** List comprehension with an `if` clause. Reads as "keep `r` if `r['study'] >= 10`."

### Aggregate — group and summarize (same pattern as U2 L07 lab)

```python
by_study = {}   # study-hours -> [gpa_sum, count]
for r in records:
    band = int(r["study"])   # 0, 1, 2, ... hours studied
    if band not in by_study:
        by_study[band] = [0.0, 0]
    by_study[band][0] += r["gpa"]
    by_study[band][1] += 1

avg_by_study = {h: s / n for h, (s, n) in by_study.items()}
```

**Walkthrough:**
- `by_study` maps integer study hours → `[running_sum, running_count]`
- `int(r["study"])` truncates decimals (6.5 → 6). This is a *choice* — we're binning by whole hours.
- The `if band not in by_study` guard initializes the accumulator for a new band.
- `s / n` uses **float division** (`/`), not `//`. Integer division would truncate the average.

**Answer in your notes:** Which of these three outputs (`records`, `heavy`, `avg_by_study`) is the one you would hand to `plt.plot` next week, and in what form?

> **Expected answer:** `avg_by_study` — but `plt.plot` needs two parallel lists: sorted keys (x) and averages in the same order (y).
> ```python
> x = sorted(avg_by_study)
> y = [avg_by_study[k] for k in x]
> ```

---

## PART 3 — THE MESSY FILES: REAL DATA IS MESSY (25 min)

Now `ls data/` again. Not every file is as tidy as the 1000-row file. Compare:

```bash
head -2 data/u2_dataset1_study_habits.csv
head -2 data/u2_dataset2_mental_health.csv
```

**The difference:**
- `u2_dataset1_study_habits.csv` goes straight to a header row.
- `u2_dataset2_mental_health.csv` starts with a **`#` comment line** — a note someone left in the file explaining the units.

**If you hand that to `csv.DictReader` blindly:** Your "first row" becomes the comment text (e.g., `# Mental health survey, GPA on 4.0 scale`). Every column name after it is garbage. You don't get a crash — you get **wrong answers** silently.

**The fix:** Strip comment lines before parsing.

```python
def load_csv(path):
    with open(path) as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    return list(csv.DictReader(lines))
```

**What this does:**
- Reads the file line by line
- Keeps only lines that don't start with `#`
- Passes the filtered lines to `csv.DictReader` — which still sees the *real* header row first

**Test it on all three files:**

```python
print(len(load_csv("data/u2_dataset1_study_habits.csv")))   # expect 52
print(len(load_csv("data/u2_dataset2_mental_health.csv")))  # expect 60
print(len(load_csv("data/u2_dataset3_activities.csv")))     # expect 50

# Print keys of first row of each — should be real column names
print(list(load_csv("data/u2_dataset1_study_habits.csv")[0].keys()))
print(list(load_csv("data/u2_dataset2_mental_health.csv")[0].keys()))
print(list(load_csv("data/u2_dataset3_activities.csv")[0].keys()))
```

**Now the part worth writing down:** Run the mental-health file **WITHOUT** the fix.

```python
rows = list(csv.DictReader(open("data/u2_dataset2_mental_health.csv")))
print(list(rows[0].keys()))
```

**What you see:** No crash. The comment text becomes a column name (e.g., `'# Mental health survey, GPA on 4.0 scale'`). A real column (`GPA`) has been pushed out of your dict entirely.

**In your notes:** Why is a wrong first row worse than a crash?

> **Answer:** A crash tells you something is wrong *immediately*. A wrong first row tells you everything is fine while you build a chart on corrupted data — the U2 L07 "quietly wrong" bug, again. This is the most dangerous kind of bug because it doesn't announce itself.

---

## PART 4 — BUILD YOUR PLOT-READY LIST (25 min, on your own)

**Goal:** One list, clean and ordered, ready for a chart. In `load_scores.py`:

1. Load the 1000-row file with `DictReader`.
2. **Filter out any row with a missing or empty GPA** (real datasets have holes).
3. Convert GPA and Sleep Hours to floats.
4. Group by sleep band and compute average GPA per band — accumulate in a dict, exactly like Part 2.

   **Sleep bands:**
   - `"under 6"` for sleep < 6
   - `"6–7"` for 6 ≤ sleep < 7
   - `"7–8"` for 7 ≤ sleep < 8
   - `"over 8"` for sleep ≥ 8

5. End the script by printing two parallel lists:

```python
bands = sorted(avg_by_sleep)
avgs = [avg_by_sleep[b] for b in bands]
print(bands)
print(avgs)
```

**The missing-GPA filter (add inside your loop):**

```python
gpa_str = row["Overall GPA"]
if not gpa_str:        # empty string
    continue           # skip this row
gpa = float(gpa_str)
```

**The sleep band function (define before the loop):**

```python
def sleep_band(hours):
    if hours < 6:
        return "under 6"
    elif hours < 7:
        return "6–7"
    elif hours < 8:
        return "7–8"
    else:
        return "over 8"
```

**Why this order of `elif`:** A value of 6.5 passes `hours < 6`? No. Passes `hours < 7`? Yes → returns `"6–7"`. Correct. If you wrote `hours < 8` first, 6.5 would match that and return `"7–8"` — wrong band. **Order matters.**

**That pair of lists (`bands`, `avgs`) is U2 L10's bar chart.** If the script runs clean and prints both with the same length, you have won today.

---

## PART 5 — TURN IN (5 min)

```bash
cd ~/compmath-u2-data-lab
git add load_scores.py
git commit -m "load csv, filter and aggregate gpa by sleep band"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

**Spot-check before submitting:** Run `python3 load_scores.py` one last time and confirm:
- [ ] The two printed lists have the **same length** (4 bands each)
- [ ] The messy-file loader reports 52 rows for `u2_dataset1_study_habits.csv`
- [ ] No `ValueError` crashes on empty strings

Then submit your repo link to the U2 L08 assignment on Google Classroom.

**Early finishers:** Add a guard that rejects rows where GPA isn't parseable (`try/except ValueError`) and counts how many you dropped; or extend the grouping to Math Score vs. Parent Education Level.

---

## WHY THIS MATTERS (the bigger picture)

This lesson teaches the **data hygiene habits** that separate toy exercises from real analysis:

| Habit | Why it matters |
|-------|----------------|
| `DictReader` + immediate `float()` conversion | Prevents string-vs-number bugs downstream |
| Separate `records` from raw `rows` | Lets you re-clean without re-reading |
| Strip comment lines (`#`) before parsing | Silent corruption is the worst kind |
| Filter missing values *before* converting | `float("")` crashes; `if not val: continue` doesn't |
| Explicit banding function with ordered `elif` | Prevents off-by-one binning errors |
| Parallel lists for plotting | `plt.bar`/`plt.plot` need matching x/y sequences |

Every subsequent lab (U2 L10, U2 L13, U2 L15–L18) assumes you can load, clean, and structure data this way without hand-holding. The column names change; the discipline doesn't.

**Next:** U2 L09 — Reflection: What Makes Data Real?  
[U2-L09-Reflection-What-Makes-Data-Real.md](U2-L09-Reflection-What-Makes-Data-Real.md)