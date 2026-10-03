# U5 L06 — Conditional Probability from a Contingency Table

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.5 — read and build a contingency table; compute conditional
probabilities and test independence from the table

---

## TODAY'S PURPOSE

One idea today, and it is the idea the whole rest of the unit runs on:

> **A conditional probability changes the denominator and nothing else.**

The numerator stays the same *kind* of thing. You are asking about a smaller
sample, so you divide by a smaller total. Everything else — the vocabulary, the
arithmetic, the traps — follows from that sentence.

A contingency table is where this becomes visible, because the denominator is a
**cell you can point at** instead of a number you have to remember.

## PART 1 — THE TABLE, AND WHY THE DENOMINATOR IS A CELL (10 min)

A mail filter looked at 1,100 messages:

|  | allowed through | blocked |
|---|---|---|
| benign | 900 | 100 |
| malicious | 40 | 60 |

```python
try:
    from sympy import Rational
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

rows = ["benign", "malicious"]
cols = ["allowed", "blocked"]
table = {("benign", "allowed"): 900, ("benign", "blocked"): 100,
         ("malicious", "allowed"): 40, ("malicious", "blocked"): 60}
total = sum(table.values())
print("total:", total)

def cell(row, col):
    return table[(row, col)]

def row_total(row):
    return sum(table[(row, c)] for c in cols)

def col_total(col):
    return sum(table[(r, col)] for r in rows)

print("row totals:", [row_total(r) for r in rows])
print("col totals:", [col_total(c) for c in cols])
```

Real output:

```
total: 1100
row totals: [1000, 100]
col totals: [940, 160]
```

There are only **two** denominators in this whole lesson and they are both row
totals: 1,000 and 100. Write them on your hand. Every conditional probability
below is one of those two numbers.

- ☐  If instead you asked "given that it was **allowed**, was it malicious?", the
      denominator would be a ______ total. Which one: ______
- ☐  Why is a mail filter table a genuine contingency table and not just a
      multiplication chart? One sentence: ______

## PART 2 — THE CONDITIONALS (12 min)

```python
try:
    from sympy import Rational
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

rows = ["benign", "malicious"]
cols = ["allowed", "blocked"]
table = {("benign", "allowed"): 900, ("benign", "blocked"): 100,
         ("malicious", "allowed"): 40, ("malicious", "blocked"): 60}
def cell(row, col):
    return table[(row, col)]
def row_total(row):
    return sum(table[(row, c)] for c in cols)
def col_total(col):
    return sum(table[(r, col)] for r in rows)
total = sum(table.values())

print("P(malicious):", Rational(cell("malicious", "allowed") + cell("malicious", "blocked"), total))
print("P(allowed | malicious):", Rational(cell("malicious", "allowed"), row_total("malicious")))
print("P(allowed | benign):", Rational(cell("benign", "allowed"), row_total("benign")))
```

Real output:

```
1/11
2/5
9/10
```

`2/5` means something precise: **of the 100 messages that were actually
malicious, 40 got through.** Not 40 out of 1,100. 40 out of 100. SymPy gave you
the reduced fraction because that is what a conditional probability actually is
and pretending it is a decimal hides the denominator.

- ☐  Verify `2/5` by hand from the table: 40 / ______ = 2/5
- ☐  Now write `P(blocked | benign)` and reduce it: ______
- ☐  A student writes "40% of the messages that got through were malicious."
      Which conditional did they actually compute, and what is the right one: ______

That last one is the swap error and it is worth four points on the test. The
**word order of the condition is the definition.** "Malicious given allowed" and
"allowed given malicious" have different denominators and, as you will see in
three weeks, wildly different numbers.

## PART 3 — INDEPENDENCE, FROM THE TABLE (12 min)

Two events are **independent** if knowing one changes nothing about the other:
`P(B|A) = P(B)`. The table lets you check it without computing a conditional
twice.

```python
try:
    from sympy import Rational
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

rows = ["benign", "malicious"]
cols = ["allowed", "blocked"]
table = {("benign", "allowed"): 900, ("benign", "blocked"): 100,
         ("malicious", "allowed"): 40, ("malicious", "blocked"): 60}
def cell(row, col):
    return table[(row, col)]
def row_total(row):
    return sum(table[(row, c)] for c in cols)
def col_total(col):
    return sum(table[(r, col)] for r in rows)
total = sum(table.values())

p_a = Rational(col_total("allowed"), total)
p_b = Rational(row_total("malicious"), total)
print("product:", p_a * p_b, "actual:", Rational(cell("malicious", "allowed"), total))
print("independent?", p_a * p_b == Rational(cell("malicious", "allowed"), total))
```

Real output:

```
product: 47/605 actual: 2/55
independent? False
```

`47/605` is about 0.0777. `2/55` is about 0.0364. The actual rate of
"malicious **and** allowed" is less than half what independence would predict.

**Read that direction carefully, because it is a security finding.** A filter
that is *better* than independent at blocking is one where the two variables are
positively related — when the message is malicious you block it more often than
your base rate would suggest. `P(allowed | malicious) = 2/5` is **lower** than
`P(allowed) = 940/1100`, which is what "the filter has signal" looks like. A
filter where the two came out *independent* would be one whose blocking
decisions carry no information about maliciousness at all.

- ☐  `P(allowed)` as a fraction of 1,100: ______  Is `2/5` bigger or smaller
      than it? ______
- ☐  Which direction of the comparison tells you the filter is doing its job?
      ______
- ☐  Write the sentence a security analyst would write from this table. One
      sentence, no jargon: ______

## PART 4 — BUILD `contingency.py` (8 min)

- ☐  A function that takes a dict table plus row and column names and returns the
      grand total, both row totals, both column totals, and both conditionals in
      each direction — as exact `Fraction`s, never floats
- ☐  A function `is_independent(table)` returning a bool, computed as
      `cell/grand == row_frac * col_frac` with exact arithmetic
- ☐  A `ValueError` if any cell is negative, and one if the table is not
      rectangular — a missing cell is a bug, not a zero
- ☐  Docstrings on everything. This is the file you will reuse on L08.

- ☐  Write one line of code that would make a float sneak in, and say why you
      forbade it: ______

## PART 5 — CLOSE (3 min)

- ☐  `contingency.py` imports cleanly and passes the mail-filter table
- ☐  You can say, without looking, what the condition does to the denominator
- ☐  **In writing: one conditional probability from your own life, stated
      correctly with its denominator.** ______

## TURN IN — Conditional Probability

1. `contingency.py` in the repo, with the four functions and their guards
2. The Part 2 and Part 3 outputs, run live
3. Your security sentence from Part 3, in writing — this is graded on clarity,
   not on vocabulary
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

The independence test in Part 3 is not a statistics exercise in this field — it
is the shape of most anomaly detection. A SIEM that flags a login as "suspicious"
produces a contingency table every morning: flagged or not, malicious or not. If
"flagged" and "malicious" come out **independent**, the rule is generating
noise, and the team is paying analysts to read alerts that carry no information.
The ROC national CERT's guidance on log monitoring lands on this point
constantly: the operational question is not "how many alerts did we get" but
"what is the rate of true malicious events given an alert, versus our base
rate" — and only the conditional answers it.

The denominator discipline is the whole of that. A dashboard that reports "4.2%
of events are malicious" is answering a different question from "of the events
your rule flagged, 31% are malicious", and the second is the one that tells you
whether to keep the rule. You will build a Risk Simulator in three weeks whose
entire job is being explicit about which denominator each of its numbers uses.
A number whose denominator is unstated is not a small gap in the analysis; it is
the analysis, missing.
