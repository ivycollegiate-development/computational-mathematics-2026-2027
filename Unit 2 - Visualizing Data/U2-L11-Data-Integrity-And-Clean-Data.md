# U2 L11 — Data Integrity and Clean Data

**LO:** handle missing data, outliers, and formatting issues before visualization; build a reproducible cleaning pipeline that documents every change.

**Estimated time:** 85 minutes (was ~65). We move slower so the cleaning habits become disciplined, not haphazard.

---

Today's lesson is about the unglamorous 80% of data work: **cleaning**. The CSVs in your data lab have been deliberately left messy — blank cells, impossible values, numbers stored as text. You will write a program that detects and repairs every problem, and outputs a clean CSV.

**Key principle:** Every cleaning decision is a choice that changes your data. You must be able to defend each choice. "I dropped the bad rows" is not a method — it's a decision with consequences.

---

## PART 0 — SEE THE MESS FIRST (15 min)

```bash
pwd
cd ~/compmath-u2-data-lab
ls data
```

Open `data/u2_student_performance_data.csv` in VS Code and scroll slowly. Write down every kind of damage you can spot. Then check yourself against the list below — your lab file contains examples of all four:

| Problem type | What it looks like | Why it breaks things |
|---|---|---|
| **Blank cells** | A value that simply is not there (`,,` in the CSV) | `float("")` → `ValueError`; missing x/y breaks plotting |
| **Impossible values** | Age of 3 in a high-school dataset; GPA of 9.0 (max is 4.0) | Skews averages, makes charts misleading |
| **Type traps** | A column that *looks* numeric but holds a stray string ("N/A", "unknown") | `float()` crashes halfway through your list comprehension |
| **Comment lines above header** | `u2_dataset2_mental_health.csv` and `u2_dataset3_activities.csv` start with `#` comment line | `csv.DictReader` treats the comment as the header → all column names wrong |

**That last one is worth seeing in the REPL:**

```python
import csv

with open("data/u2_dataset2_mental_health.csv", newline="") as f:
    raw = f.read().splitlines()

print(raw[0])   # the comment line — starts with '#'
print(raw[1])   # the real header
```

**Why this matters:** A crash tells you something is wrong. A silently wrong header (the comment-line bug) tells you everything is fine while you build charts on corrupted columns. This is the "quietly wrong" pattern from U2 L07 and U2 L08 — the most dangerous kind of bug.

---

## PART 1 — MISSING DATA: DETECT, THEN DECIDE (20 min)

Load the main dataset and hunt for blanks:

```python
import csv

with open("data/u2_student_performance_data.csv", newline="") as f:
    rows = list(csv.DictReader(f))

def is_blank(value):
    return value is None or str(value).strip() == ""

blanks = 0
blank_by_column = {}
for r in rows:
    for key, value in r.items():
        if is_blank(value):
            blanks += 1
            blank_by_column[key] = blank_by_column.get(key, 0) + 1

print("total blank cells:", blanks)
print("blanks by column:", blank_by_column)
```

**For each blank you find, you have exactly two choices — write the tradeoff in your notes:**

| Choice | When it makes sense | The cost |
|---|---|---|
| **Drop the row** | The missing value is in a column you're plotting (x or y) | You lose a whole student because of one hole; if missingness is systematic (e.g., low-GPA students skip GPA), you bias your sample |
| **Fill the value** (impute) | The column is not plotted, or missingness looks random | A fill is a *guess*; every chart built later is built partly on guesses |

**Rule of thumb for today:**
- Drop rows with missing **label-type** data we plot (x-axis or y-axis columns)
- For plain numbers not used as plot axes, you *may* fill with the column average — but **say which rule you are applying, in a comment, every time**

**Why document the rule:** Future you (and your grader) needs to know *why* row 847 disappeared. "I dropped it" is not reproducible. "Dropped: blank GPA (plot axis)" is.

---

## PART 2 — OUTLIERS: SANITY BOUNDS (20 min)

An outlier is a value far from the rest. Some are real and interesting; some are typos or junk. Today we use **sanity bounds** — fixed rules that say what is physically possible, independent of the data distribution:

```python
SANITY = {
    "Age": (10, 22),
    "Math Score": (0, 100),
    "Science Score": (0, 100),
    "English Score": (0, 100),
    "Overall GPA": (0.0, 4.0),
    "Hours Studied Per Week": (0, 60),
    "Sleep Hours Per Night": (0, 14),
    "Absence Rate": (0.0, 1.0),
}

def is_impossible(column, value):
    low, high = SANITY[column]
    return not (low <= value <= high)
```

**Why sanity bounds over statistical outliers (e.g., 1.5×IQR)?**
- Statistical outliers depend on *this* dataset — a real extreme value in a small sample gets flagged
- Sanity bounds encode *domain knowledge* — a GPA of 9.0 is impossible in *any* 4.0-scale system, regardless of what the rest of the data looks like
- Sanity bounds are auditable: anyone can read the dict and agree or disagree with the bounds

**In the REPL, count how many values break these bounds:**

```python
bad = {}
for col, (low, high) in SANITY.items():
    n = 0
    for r in rows:
        try:
            v = float(r[col])
        except ValueError:
            continue        # type trap — handled in Part 3
        if not (low <= v <= high):
            n += 1
    bad[col] = n
print(bad)
```

**In your notes:** Why does a GPA of 9 get thrown out (impossible) but a legitimately low 0.5 GPA get kept (possible, just rare)?

> **Answer:** The rule rejects what **cannot be true**, never what is merely **surprising**. 0.5 GPA exists — it's a struggling student. 9.0 GPA cannot exist on a 4.0 scale — it's a data entry error or a different scale mixed in.

---

## PART 3 — TYPE TRAPS: CONVERT DELIBERATELY (15 min)

`csv.DictReader` gives back **strings**. Everything numeric must be converted, and the conversion can fail. The safe pattern:

```python
def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None    # blank or junk — signal it, don't crash
```

**Why this pattern:**
- `ValueError`: `float("N/A")`, `float("")` — string isn't a number
- `TypeError`: `float(None)` — missing value propagated
- **Returns `None` instead of crashing** — marks the one bad cell and lets you keep working
- **Handle `None` where you decide to drop or fill** — explicit, not implicit

**Why not `float(value) if value else None`:** Empty string `""` is falsy, but `"0"` is also falsy in some contexts, and `"N/A"` is truthy but not a number. The `try/except` is the only robust way.

---

## PART 4 — BUILD `clean_data.py` (in pairs, ~35 min)

In your repo, create `clean_data.py` that:

1. **Reads** `data/u2_student_performance_data.csv` with `csv.DictReader`.
2. **For each numeric column:** converts with the `to_float` pattern, drops rows with blanks in columns you chose to drop on, and replaces impossible values (sanity bounds) by dropping the row — with a `print` saying how many rows were dropped and why.
3. **Writes** the cleaned result to `data/u2_student_performance_clean.csv` with `csv.writer`, keeping the original header row.
4. **Prints, at the end:** rows in, rows out, rows dropped — and the counts must add up. If they don't, your cleaning has a bug.

**Skeleton to start from:**

```python
import csv

SANITY = {
    "Age": (10, 22),
    "Math Score": (0, 100),
    "Science Score": (0, 100),
    "English Score": (0, 100),
    "Overall GPA": (0.0, 4.0),
    "Hours Studied Per Week": (0, 60),
    "Sleep Hours Per Night": (0, 14),
    "Absence Rate": (0.0, 1.0),
}

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def is_blank(value):
    return value is None or str(value).strip() == ""

def is_impossible(column, value):
    if column not in SANITY:
        return False
    low, high = SANITY[column]
    return not (low <= value <= high)

# 1. READ
with open("data/u2_student_performance_data.csv", newline="") as f:
    rows = list(csv.DictReader(f))

rows_in = len(rows)
print(f"Rows in: {rows_in}")

# 2. CLEAN
clean_rows = []
dropped_counts = {"blank": 0, "impossible": 0}

for r in rows:
    drop_reason = None

    # Convert numeric columns, track blanks and impossibles
    for col in SANITY:
        if is_blank(r[col]):
            drop_reason = f"blank {col}"
            dropped_counts["blank"] += 1
            break
        val = to_float(r[col])
        if val is None:
            drop_reason = f"unparseable {col}"
            dropped_counts["impossible"] += 1
            break
        if is_impossible(col, val):
            drop_reason = f"impossible {col}={val}"
            dropped_counts["impossible"] += 1
            break
        r[col] = val  # replace string with float

    if drop_reason:
        print(f"Dropped row: {drop_reason}")
        continue

    clean_rows.append(r)

rows_out = len(clean_rows)
rows_dropped = rows_in - rows_out
print(f"Rows out: {rows_out}")
print(f"Rows dropped: {rows_dropped}")
print(f"Dropped by reason: {dropped_counts}")

# Sanity check: counts must add up
assert rows_in == rows_out + rows_dropped, "Count mismatch — cleaning logic bug"

# 3. WRITE
header = list(rows[0].keys())  # original header order
with open("data/u2_student_performance_clean.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in clean_rows:
        writer.writerow([r[col] for col in header])

print("Wrote data/u2_student_performance_clean.csv")
```

**Key details explained:**
- `newline=""` in both `open()` calls — prevents extra blank lines on Windows
- `csv.writer` (not `DictWriter`) because we want exact column order matching the original header
- `[r[col] for col in header]` pulls values in header order, not dict order (dict order is insertion-ordered in Python 3.7+ but explicit is safer)
- The `assert` at the end is a **guardrail** — if in/out/dropped don't add up, you have a logic bug (e.g., a row counted as dropped twice, or a row silently duplicated)

**Milestone for today:** `clean_data.py` runs with no crash, produces a `_clean.csv`, and its in/out/dropped counts add up exactly.

---

## PART 5 — DISCUSSION: THE COST OF CLEANING (10 min)

If we dropped 50 of our 1,000 rows, every chart we make this week is built on the remaining 950. Cleaning is not free — it silently changes your sample.

**In your notes:** Name one situation where dropping rows would *distort* a conclusion rather than improve it.

> **Example:** "If low-GPA students are more likely to leave GPA blank (embarrassment/privacy), dropping blank-GPA rows removes the struggling students and makes the average GPA look higher than it really is. The cleaned data *looks* better but *is* more biased."

---

## PART 6 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add clean_data.py data/u2_student_performance_clean.csv
git commit -m "clean_data.py: blanks, outliers, type traps"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

1. Run `python3 clean_data.py` one final time and screenshot the full terminal output — rows in, rows out, rows dropped, counts adding up.
2. Screenshot the first few lines of `data/u2_student_performance_clean.csv` open in VS Code, showing it is readable and has no blank cells.
3. Confirm the push succeeded (see Part 6 commands above).

Submit the screenshots to the U2 L11 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS (the bigger picture)

**Cleaning is not a prelude to analysis — it IS analysis.** Every decision in `clean_data.py` shapes what your charts can say. The Unit 2 project (U2 L15–L18) will require you to submit your cleaning script alongside your visualizations, with a written justification for every drop/fill choice.

**The reproducible pipeline you built today:**
```
raw CSV → detect blanks → convert types → apply sanity bounds → drop/fill with logged reasons → clean CSV → counts audit
```

This pattern scales to 1M-row datasets, SQL pipelines, and production ML. The column names change; the discipline doesn't.

**Next:** U2 L12 — Paper Check: Relationships and Clean Data  
[U2-L12-Paper-Check-Relationships-And-Clean-Data.md](U2-L12-Paper-Check-Relationships-And-Clean-Data.md)