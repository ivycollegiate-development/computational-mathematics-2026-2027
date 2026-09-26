# U3 L10 — Lab: PII — What Makes Data Identifying

**LO:** audit a real dataset for personally identifying information, and explain which columns are *directly* identifying, which are *quasi*-identifying, and which are safe.

The first half of this unit was mathematics. Today the mathematics meets a
responsibility. A clinic's visit data is not just numbers — a row is
somebody's medical history, and the columns you include decide whether an
anonymized report protects that person or exposes them.

This is the first of three security lessons. You will **not** publish
anything until you can prove it is safe.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

**Critical parsing note.** This file has a comment line, a real header, and
quoted fields containing commas — every name looks like `"Jordan, Haddad"`.
If you split on `","` you will get **9 fields instead of 8**, and every
column after `Name` will be silently shifted. That is not a crash; it is a
corrupted analysis. Use `csv`.

```python
import csv
from collections import Counter

with open("/tmp/u3_datasets/u3_clinic_visits.csv") as f:
    lines = [ln for ln in f.read().splitlines() if not ln.strip().startswith("#")]

rows = list(csv.DictReader(lines))
print(len(rows), "visits")
print("columns:", list(rows[0].keys()))
print("first row:", rows[0])
```

Prove the parsing is right before you trust anything:

```python
# The naive (wrong) way, for contrast -- use the FIRST DATA ROW, not the header:
first_data = lines[1]
naive = first_data.split(",")
print("naive field count on a data row:", len(naive))
print("correct field count:", len(rows[0]))
print("naive thinks Age is:", repr(naive[2]), "-- but csv says:", repr(rows[0]["Age"]))
```

You should see the naive count is **9** and the correct count is **8**. Worse,
the naive split has silently shifted every column: `naive[2]` holds
`' Haddad"'`, a fragment of the name, while the real `Age` is `'31'`. No error
is raised. The analysis is simply wrong from that point on.

## PART 1 — THE THREE TIERS OF IDENTIFYING INFORMATION (10 min)

Write these in your notes; they are the vocabulary for the rest of the unit.

| Tier | What it is | Clinic examples |
|---|---|---|
| **Direct identifier** | Names the person outright | `Name`, `Patient_ID` |
| **Quasi-identifier** | Not a name, but a combination that can single someone out | `Age`, `Zip_Code`, `Visit_Date`, `Condition` |
| **Sensitive** | Reveals something private about them | `Condition`, `Insurance_Plan` |
| **Non-identifying** | Safe in aggregate | `Visit_Count` (mostly) |

The key idea, and it is the whole lesson: **a single column is often safe
while a combination is fatal.** Neither `Age` nor `Zip_Code` alone identifies
anyone. Together, they very often do.

## PART 2 — THE DIRECT AUDIT (15 min)

For each column, classify it and count how many distinct values it has.
Distinct-value counts are the first hint: a column with 80 distinct values
in 80 rows is a unique identifier.

```python
for col in rows[0].keys():
    vals = [r[col] for r in rows]
    print(f"{col:<15} distinct={len(set(vals)):>3}  sample={vals[0]!r}")
```

Answer in your notes:

1. `Patient_ID` has **80 distinct values in 80 rows** — it identifies every
   single patient by itself, even though it is "just a code." A code is still
   an identifier.
2. `Name` has only **20 distinct values**, because 80 visits came from 20
   patients who returned. So a name alone pinpoints a person — but not
   uniquely *per row*. Now the interesting case: `Visit_Date` has **46**
   distinct values. A name plus a date usually does pin one visit exactly.
   That is the same re-identification idea as Part 3, arriving early.
3. `Zip_Code` has only **6** distinct values and `Condition` only **9**.
   Neither identifies anyone by itself. Hold that thought — Part 3 shows what
   happens when harmless columns are combined.

## PART 3 — THE RECONCILIATION PROBLEM (15 min)

This is the heart of the lesson. Suppose you remove `Name` and `Patient_ID`
and declare the data anonymized. Is it?

```python
# Can you re-identify a specific patient from "anonymous" data?
key = [(r["Name"], r["Visit_Date"], r["Condition"]) for r in rows]
print(f"distinct Name+Date+Condition combinations: {len(set(key))} of {len(rows)}")
```

- All **80** combinations are unique. So even with **no names at all**, the
  combination `Visit_Date + Condition` narrows to a single patient. If
  someone knows that on one date only one patient had a rare condition, they
  can name them without a single name in the file.
- Try a *weaker* attacker: one who knows a patient's age and zip and nothing
  else.

```python
qkey = [(r["Age"], r["Zip_Code"]) for r in rows]
print(f"distinct Age+Zip pairs: {len(set(qkey))} of {len(rows)}")
print(f"... of which appear exactly once: {sum(1 for k in set(qkey) if qkey.count(k) == 1)}")
```

- The output should read **72 distinct Age+Zip pairs out of 80 rows**, and
  **64 pairs appear exactly once**. Read that second number again: 64 of 80
  patients are pinned down to a single person by age and zip code alone —
  two columns that, separately, tell you almost nothing.
- Now the near-miss that makes this practical: a hospital **knows** its own
  patients' ages and zips. So "age 66, zip 40602" is a lookup, not a guess.

In your notes, answer plainly: **is removing the name column enough to make
this file anonymous?** One sentence, no hedging.

## PART 4 — THE CELL-SIZE PROBLEM (10 min)

Before publishing "Migraine: 19 patients, mean wait 11.4," someone has to ask
whether that cell is big enough to mean anything — and small enough to
identify someone.

```python
cond = Counter(r["Condition"] for r in rows)
for name, count in sorted(cond.items(), key=lambda kv: kv[1]):
    flag = "  <-- SMALL CELL" if count < 5 else ""
    print(f"{name:<18}{count:>3}{flag}")
```

- Four conditions have fewer than 5 patients: `Amyloidosis` (2),
  `Myelofibrosis` (2), `Von Hippel-Lindau` (1), `Dermatomyositis` (1).
- A cell of **1** is not a statistic. It is a person, standing alone in a
  row, described by a medical condition. Publishing "Von Hippel-Lindau: 1
  patient" tells the world that exactly one clinic patient has that
  diagnosis — and the clinic is small enough that people can guess who.
- This is why L12 will have a suppression rule. Write down: what threshold
  would you pick, and what would publishing a small cell reveal?

## PART 5 — THE PRIVACY FILTER SPEC (15 min)

The project labs build a **privacy filter**: a program that must run
*before* any chart is drawn. You do not build it today, but you write its
requirements, and this spec is what L15 implements.

**The filter must, in order:**

1. **Reject** any dataset containing a column in the direct-identifier list.
2. **Warn** on any column that is a known quasi-identifier.
3. **Count** rows in every group it is about to publish and **suppress**
   any group with fewer than **5** rows.
4. **Refuse to draw a chart** if steps 1–3 found anything unresolved, and
   say why in plain English.

```python
# Skeleton for L15 -- read it, do not run it yet
DIRECT_IDENTIFIERS = {"Name", "Patient_ID"}
QUASI_IDENTIFIERS = {"Age", "Zip_Code", "Visit_Date", "Condition"}
MIN_CELL = 5

def privacy_gate(rows, group_col):
    """Return (ok, problems). Never let a chart through while problems exist."""
    problems = []
    present = set(rows[0].keys())
    for col in DIRECT_IDENTIFIERS & present:
        problems.append(f"direct identifier present: {col}")
    counts = Counter(r[group_col] for r in rows)
    for name, c in counts.items():
        if c < MIN_CELL:
            problems.append(f"small cell in {group_col}={name!r}: {c} rows")
    return (not problems), problems
```

In your notes:

- What does the function return, and why a **tuple** rather than a boolean?
- The name `privacy_gate` matters: the **gate** comes before the chart, not
  after. Why is a "review the dashboard at the end" approach fundamentally
  weaker? (Think about what a chart library does if you hand it bad data.)
- One more requirement to add yourself: what should happen to a **quasi**-identifier
  — suppress it, generalize it (age 66 → age band 65+), or drop it? Give a
  reason for your choice.

## PART 6 — LOOK AHEAD: THE U3 L11 PAPER CHECK

Next lesson is a paper check covering percentiles, PII, and anonymization
together — the math and the security, in one assessment. Today you wrote the
filter's requirements; next you will defend them on paper.

## PART 7 — SAVE + PUSH (last 10 min)

```bash
git add privacy_audit.md
git commit -m "U3 L10 PII audit of clinic visits, three tiers, and privacy gate spec"
git push
```

Your `privacy_audit.md` should contain your Part 1 tier table filled in, your
answers to Part 2, 3, and 4, and the Part 5 requirements — this is the
document L15 implements.

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `privacy_audit.md`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Include these three numbers in the push message so I can spot-check:

1. distinct Name+Date+Condition combinations
2. how many conditions have fewer than 5 patients
3. the number of columns in the file

Keep the terminal open — spot-checks.
