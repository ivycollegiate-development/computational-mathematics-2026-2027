# U3 L12 — Lab: Anonymization — Suppression and Generalization

**LO:** apply k-anonymity to a real dataset, and choose defensible suppression and generalization rules.

In L10 you audited the clinic file and found that removing the name column
does **not** make it anonymous. Today you build the two techniques that
actually do something about it, and you measure how much protection each one
buys.

Both techniques trade a little accuracy for a lot of privacy. Your job is to
decide how much trade is right, and to be able to defend it.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

```python
import csv
import statistics as st
from collections import Counter

with open("/tmp/u3_datasets/u3_project_dataset.csv") as f:
    lines = [ln for ln in f.read().splitlines() if not ln.strip().startswith("#")]

rows = list(csv.DictReader(lines))
print(len(rows), "members")
print("columns:", list(rows[0].keys()))
```

The comment line in this file tells you it "contains identifying
information." That is not a warning, it is the assignment.

## PART 1 — THE TARGET: K-ANONYMITY (15 min)

**k-anonymity** is a rule with a single number attached: *every person in your
published data must be indistinguishable from at least **k** other people.*
The **k-anonymity** of a dataset is the smallest size of any group of people
that shares your published identifying attributes.

```python
def k_value(rows, fields):
    """Smallest group size when we publish exactly these fields.
    k=1 means every single person is uniquely identified.
    Returns 0 for an empty result, so suppression can never crash."""
    if not rows:
        return 0
    counts = Counter(tuple(r[f] for f in fields) for r in rows)
    return min(counts.values())

combos = [
    (["Zip_Code"],                 "zip code alone"),
    (["Age"],                      "age alone"),
    (["Age", "Zip_Code"],          "age + zip"),
    (["City", "Age", "Zip_Code"],  "city + age + zip"),
    (["Age", "City", "Membership_Tier"], "age + city + tier"),
]
for fields, label in combos:
    c = Counter(tuple(r[f] for f in fields) for r in rows)
    singles = sum(1 for k in c if c[k] == 1)
    print(f"{label:<22} groups={len(c):>4}  k={min(c.values()):>3}  unique people={singles:>3}")
```

Write these in your notes:

1. `Zip_Code` alone: how many distinct values, and what is *k*? (109
   distinct, so **k = 1**.)
2. `Age + Zip_Code`: how many groups, and what is *k*? (This is the one to
   stare at. **120 groups from 120 rows, k = 1** — every single member is
   unique on age and zip together.)
3. `Age` alone: *k* = ______ (45 distinct ages across 120 members, and 13 of
   those ages belong to exactly one person. So k = 1 here too — just via a
   different route.)

**The lesson:** a column can be harmless by itself and lethal in combination.
Zip alone is 109 values; age alone is 45. Together they identify all 120
people. Neither is a name.

## PART 2 — TECHNIQUE 1: SUPPRESSION (15 min)

**Suppression** means dropping rows or cells that are too small. If a group
has fewer than *k* members, you do not publish it at all.

```python
MIN_K = 5

def suppress(rows, field, min_k=MIN_K):
    counts = Counter(r[field] for r in rows)
    keep = [r for r in rows if counts[r[field]] >= min_k]
    dropped = len(rows) - len(keep)
    return keep, dropped

for field in ("City", "Membership_Tier", "Zip_Code", "Age"):
    kept, dropped = suppress(rows, field)
    print(f"group by {field:<16} keep {len(kept):>3} drop {dropped:>3}  "
          f"k_now={k_value(kept, [field])}")
```

- Grouping by `City` drops **0** rows and leaves k = 20. Nothing to do.
- Grouping by `Zip_Code` drops **all 120 rows** — the `k` printed is **0**,
  not a number, because the list is empty. That is the most important line in
  this lab. Read the lesson: *no zip code appears more than 5 times*, so a
  k≥5 rule on zip keeps nothing at all. You did not anonymize the data; you
  deleted it.
- By `Age` it drops **91** rows and keeps 29, leaving k = 5. Partly working.

Then: what is the *right* threshold? Try a rule of `k >= 5` and a stricter
`k >= 10` and compare what survives.

```python
for rule in (3, 5, 10):
    kept, dropped = suppress(rows, "Zip_Code", rule)
    print(f"k>={rule:<3} keep {len(kept):>3} drop {dropped:>3}")
```

4. For a rule of **k ≥ 5**, how many rows survive grouping by `Zip_Code`?
   (**Zero**.) Now try **k ≥ 3**: you keep just **3** rows out of 120. Is a
   3-person dataset a privacy win? What have you actually produced?
5. Why is a big drop a *warning sign* rather than a *success*? What does a
   120-row drop tell you about the column you grouped on? (It tells you the
   column was unique per person, so it should have been *dropped as a column*
   in L10 — not filtered row by row.)

## PART 3 — TECHNIQUE 2: GENERALIZATION (20 min)

Suppression throws data away. **Generalization** keeps every row but makes
each one less specific. The row still exists; it just describes a bigger
group of people.

```python
def age_band(age_str, width=10):
    a = int(age_str)
    lo = a // width * width
    return f"{lo}-{lo + width - 1}"

def zip_prefix(zip_str, digits=3):
    return zip_str[:digits]

banded = [dict(r, Age_Band=age_band(r["Age"]), Zip3=zip_prefix(r["Zip_Code"])) for r in rows]
print("Age_Band values:", sorted(Counter(b["Age_Band"] for b in banded)))
print("Zip3 values:", sorted(Counter(b["Zip3"] for b in banded)))

for fields, label in ((["Age_Band"],               "age band (10-wide)"),
                      (["Zip3"],                   "zip prefix (3)"),
                      (["Age_Band", "City"],       "age band + city"),
                      (["Age_Band", "City", "Membership_Tier"], "age band + city + tier")):
    c = Counter(tuple(b[f] for f in fields) for b in banded)
    singles = sum(1 for k in c if c[k] == 1)
    print(f"{label:<26} groups={len(c):>3}  k={min(c.values()):>3}  unique={singles:>3}")

# Question 9: is Zip3 actually different from City?
cross = Counter((b["Zip3"], b["City"]) for b in banded)
for (z, city), n in sorted(cross.items()):
    print(f"  {z} -> {city:<10} {n}")
```

Notice that **every** `Zip3` appears with exactly one `City`. Now you see why.

Answer in your notes:

6. Read the table honestly: a 10-year age band alone gives k = **3** — still
   below 5. Band + city gives k = **1** with **6** people still unique. Band
   + city + tier gives k = **1** with **14** unique.
   **None of these reach k ≥ 5.** Stop and look at that, because it is the
   surprise of this lab: **adding** a column made anonymity *worse*.
7. Try a wider band. A **15-year** band alone gives k = **15** — comfortably
   above 5. But adding tier back on drops it to k = **1** with 1 person
   unique. A **25-year** band gives k = **16** alone, and k = **3** with tier.
   So: how many of the 120 members remain individually identifiable under
   your best option? Write the number down. (The honest answer is *some*,
   unless you give up a whole dimension.)
8. Try a **5-year** age band instead of 10. Does *k* go up or down, and why?
   Is a narrower band more private? (It is *less* private — every extra year
   of precision is a chance to become unique. You are trading accuracy for
   privacy, and both directions cost something.)
9. What happened to `Zip3`? It produced only **6** values, so k = 20 and
   nothing looks unique. But check what those six prefixes actually are:
   print the crosstab of `Zip3` against `City`.
   Every `Zip3` maps to exactly **one** city, and Taichung owns two of them.
   **`Zip3` is just `City` wearing a disguise.** Keeping both is publishing
   the same fact twice and pretending you anonymized one of them. Did you
   gain privacy? No.

## PART 4 — YOUR ANONYMIZATION PASS (20 min)

Now build the function the project will actually use. Write
`anonymize.py` in your repo with this design:

```python
import csv
from collections import Counter

DIRECT_IDENTIFIERS = {"First_Name", "Last_Name", "Member_ID"}
QUASI_IDENTIFIERS = {"Age", "Zip_Code", "City", "Signup_Date"}
MIN_K = 5

def load(path):
    with open(path) as f:
        lines = [l for l in f.read().splitlines() if not l.strip().startswith("#")]
    return list(csv.DictReader(lines))

def drop_direct(rows):
    return [{k: v for k, v in r.items() if k not in DIRECT_IDENTIFIERS} for r in rows]

def generalize(rows, age_width=10, zip_digits=3):
    out = []
    for r in rows:
        new = dict(r)
        if "Age" in new:
            a = int(new["Age"]); lo = a // age_width * age_width
            new["Age"] = f"{lo}-{lo + age_width - 1}"
        if "Zip_Code" in new:
            new["Zip_Code"] = new["Zip_Code"][:zip_digits]
        out.append(new)
    return out

def k_value(rows, fields):
    if not rows:
        return 0
    return min(Counter(tuple(r[f] for f in fields) for r in rows).values())
```

Your job: make it work end to end and **report**, in a file
`anonymization_report.md`:

1. The *k* before and after, using `["Age", "Zip_Code", "City"]` as the
   published identifying fields. (Before: k = 1 with 120 unique. After: report
   what you actually got — and if it is still 1, say so plainly. An honest
   k = 1 with a written explanation is a better report than a k you got by
   deleting rows until the number looked good.)
2. Whether any direct identifier survives (there must be none).
3. What each transformation cost in accuracy — one sentence per technique.
4. Your final recommendation for `age_width` and `zip_digits`, with a
   reason. Justify it from the *k* values you measured, not from taste.

## PART 5 — THE LIMITATION YOU MUST STATE (10 min)

Generalization is not a guarantee. Answer in your notes:

- After banding ages into 10-year groups, what can you still say about an
  individual member? Could someone combine the *published* fields with
  outside knowledge (this is a 120-member company in five known cities) to
  re-identify someone? How?
- State honestly in one sentence what your anonymized dashboard does and
  does not protect against. "We removed the names" is not an acceptable
  answer.

## PART 6 — SAVE + PUSH (last 10 min)

```bash
git add anonymize.py anonymization_report.md
git commit -m "U3 L12 anonymization pass: suppression, generalization, measured k"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `anonymize.py` and `anonymization_report.md`, pushed above, are the
turn-in. Submit the **push confirmation line** as a screenshot to this
assignment on Google Classroom.

Include these numbers in the push message so I can spot-check:

1. *k* for `Age + Zip_Code` before anonymization
2. *k* for your best generalized combination
3. how many members remain individually identifiable after your pass

Keep the terminal open — spot-checks.
