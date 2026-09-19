# U2 L11 — Data Integrity and Clean Data

**LO:** handle missing data, outliers, and formatting issues before visualization.

Today's lesson is about the unglamorous 80% of data work: **cleaning**. The
CSVs in your data lab have been deliberately left messy — blank cells,
impossible values, numbers stored as text. You will write a program that
detects and repairs every problem, and outputs a clean CSV.

## PART 0 — SEE THE MESS FIRST (first 10 min)

```bash
pwd
cd ~/compmath-u2-data-lab
ls data
```

Open `data/u2_student_performance_data.csv` in VS Code and scroll slowly. Write
down every kind of damage you can spot. Then check yourself against the list
below — your lab file contains examples of all four:

- **Blank cells** — a value that simply is not there.
- **Impossible values** — an Age of 3 in a high-school dataset. A GPA of 9,
  when GPAs stop at 4.0.
- **Type traps** — a column that *looks* numeric but holds a stray string,
  so `float()` crashes halfway through your list comprehension.
- **Extra files with their own quirks** — `u2_dataset2_mental_health.csv` and
  `u2_dataset3_activities.csv` start with a `#` comment line *above* the
  header row. `csv.DictReader` would treat the comment line as the header.

That last one is worth seeing in the REPL:

```python
import csv

with open("data/u2_dataset2_mental_health.csv", newline="") as f:
    raw = f.read().splitlines()

print(raw[0])   # the comment line — starts with '#'
print(raw[1])   # the real header
```

## PART 1 — MISSING DATA: DETECT, THEN DECIDE (15 min)

Load the main dataset and hunt for blanks:

```python
import csv

with open("data/u2_student_performance_data.csv", newline="") as f:
    rows = list(csv.DictReader(f))

def is_blank(value):
    return value is None or str(value).strip() == ""

blanks = 0
for r in rows:
    for key, value in r.items():
        if is_blank(value):
            blanks += 1
print("blank cells:", blanks)
```

For each blank you find, you have exactly two choices — write the tradeoff in
your notes:

- **Drop the row.** Safest, but you lose a whole student because of one hole.
- **Fix the value.** Fill with a sensible number (the column average, a
  neutral value) — but a fill is a *guess*, and every chart you make later is
  built partly on guesses.

Rule of thumb for today: drop rows with missing **label-type** data we plot;
for plain numbers we may fill with the column average. Say which rule you are
applying, in a comment, every time.

## PART 2 — OUTLIERS: SANITY BOUNDS (15 min)

An outlier is a value far from the rest. Some are real and interesting; some
are typos or junk. Today we use **sanity bounds** — fixed rules that say what
is physically possible, independent of the data:

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

In the REPL, count how many values break these bounds:

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

In your notes: why a GPA of 9 gets thrown out (impossible) but a legitimately
low 0.5 GPA gets kept (possible, just rare). **The rule rejects what cannot be
true, never what is merely surprising.**

## PART 3 — TYPE TRAPS: CONVERT DELIBERATELY (10 min)

`csv.DictReader` gives back **strings**. Everything numeric must be converted,
and the conversion can fail. The safe pattern:

```python
def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None    # blank or junk — signal it, don't crash
```

Note the difference: a crash stops your whole program; `None` marks the one
bad cell and lets you keep working. Return `None`, then handle it where you
decide to drop or fill.

## PART 4 — BUILD `clean_data.py` (in pairs, ~25 min)

In your repo, create `clean_data.py` that:

1. Reads `data/u2_student_performance_data.csv` with `csv.DictReader`.
2. For each numeric column: converts with the `to_float` pattern, drops rows
   with blanks in columns you chose to drop on, and replaces impossible
   values (sanity bounds) by dropping the row — with a `print` saying how many
   rows were dropped and why.
3. Writes the cleaned result to `data/u2_student_performance_clean.csv` with
   `csv.writer`, keeping the original header row.
4. Prints, at the end: rows in, rows out, rows dropped — and the counts must
   add up. If they don't, your cleaning has a bug.

Skeleton to start from:

```python
import csv

SANITY = {
    "Age": (10, 22),
    "Overall GPA": (0.0, 4.0),
    # ... finish the rest from Part 2
}

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

# 1. read  2. clean  3. write  4. report
```

**Milestone for today:** `clean_data.py` runs with no crash, produces a
`_clean.csv`, and its in/out/dropped counts add up exactly.

## PART 5 — DISCUSSION: THE COST OF CLEANING (5 min)

If we dropped 50 of our 1,000 rows, every chart we make this week is built on
the remaining 950. Cleaning is not free — it silently changes your sample. In
your notes: name one situation where dropping rows would distort a conclusion
rather than improve it.

## PART 6 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add clean_data.py data/u2_student_performance_clean.csv
git commit -m "clean_data.py: blanks, outliers, type traps"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

1. Run `python3 clean_data.py` one final time and screenshot the full terminal
   output — rows in, rows out, rows dropped, counts adding up.
2. Screenshot the first few lines of `data/u2_student_performance_clean.csv`
   open in VS Code, showing it is readable and has no blank cells.
3. Confirm the push succeeded (see PART 6 commands above).

Submit the screenshots to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
