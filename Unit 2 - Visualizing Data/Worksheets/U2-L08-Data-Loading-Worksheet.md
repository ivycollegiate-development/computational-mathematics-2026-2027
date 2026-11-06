# U2 L08 — Data Loading Worksheet

Names: ___________________________  Date: ____

Closed notes. 20 minutes, then swap, grade with the key, and correct every miss in a second color. The corrections are the point.

## 1: The check

Section A — CSV & DictReader

1. `csv.reader` gives you a list of strings per row. `csv.DictReader` gives you a ______ per row.

2. A CSV has a header line: `Student,Hours,Score,Sleep`. After `r = next(reader)`, what is `r["Hours"]` for the first data row? What type is it?

3. Your CSV has a comment line starting with `#`. Does `csv.DictReader` skip it automatically? If not, how do you handle it?

4. The file has 1,000 rows + 1 header. `rows = list(csv.DictReader(f))` — what is `len(rows)`? What is `len(rows[0])`?

Section B — Type conversion & sanity

5. `r["Score"]` is the string `"87.5"`. Write the two-line pattern to convert it to `float` and return `None` if it fails.

6. Why does the pattern return `None` instead of raising? What does the caller do with `None`?

7. Sanity bounds for `Score` are `(0.0, 100.0)`. A row has `Score = "105"`. What happens in the cleaning loop?

8. A row has `Score = ""` (blank). Your `to_float` returns `None`. Your cleaner drops the row. You drop 50 of 1,000 rows. What have you silently changed about the dataset?

Section C — The audit trail

9. The rubric requires: "print the row count before and after cleaning." Why is *printing* required, not just computing?

10. Your provenance statement must include: original row count, rows dropped, reason for each drop category, and ______.

Section D — One fix-it (2 points)

11. This cleaner has two bugs. Name both:

```python
SANITY = {"Score": (0.0, 100.0)}
rows = list(csv.DictReader(f))
for r in rows:
    score = float(r["Score"])
    if not (0.0 <= score <= 100.0):
        rows.remove(r)
```

Bug 1: ______________________________________________________________

Bug 2: ______________________________________________________________

## 2: Swap and grade

Graded by: ___________________________  Score: ________ / 14

## 3: Corrections

For each miss, correct it in a second color and write one line: what I had in my head vs what is true.

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

## 4: Look ahead — the U2 L09 lab

In U2 L09 you build `clean_threats.py` for the campus network dataset. The dataset has columns: `date`, `failed_logins`, `phishing_reports`, `successful_logins`.

What column would you NOT use sanity bounds on, and why?

_________________________________________________________________________

Predict: the dataset has 500 rows. You expect to drop ~5%. How many rows would remain, and what must your provenance line say?

_________________________________________________________________________

## Hand-in

☐  Check sheet completed, graded by partner, corrections in a second color.

☐  Photo of the corrected check sheet submitted to the Classroom assignment by 11:59 PM tonight.

Keep the sheet — it is your study guide for the unit project and assessment.