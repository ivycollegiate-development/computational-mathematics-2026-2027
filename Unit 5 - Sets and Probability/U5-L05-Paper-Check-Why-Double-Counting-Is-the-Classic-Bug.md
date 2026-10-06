# U5 L05 — Paper Check L01–L04: Why Double-Counting Is the Classic Bug

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.1–5.4 — demonstrate fluency with set vocabulary, Venn regions, and
inclusion–exclusion under exam conditions

---

**No laptop today.** Closed-notes except for the single page of formulas you
are allowed at the bottom. Everything in this check was taught in the last four
days and can be done with a pencil.

This is not a quiz for its own sake. In U5 L06 you start computing conditional
probability, and conditional probability is where a sloppy set count turns into
a wrong denominator — which is where a wrong denominator becomes a wrong risk
decision.

## PART 1 — VOCABULARY UNDER PRESSURE (10 min)

Define each **in your own words**, in one sentence, and give one example that is
not a math example.

| term | your definition | your example |
|---|---|---|
| subset | | |
| proper subset | | |
| disjoint | | |
| complement | | |
| symmetric difference | | |

- ☐  Is the empty set a subset of every set? Proof in one line: ______
- ☐  Is the empty set a *proper* subset of the empty set? Why not: ______
- ☐  A set with exactly one element is called a **singleton**. Give a real
      singleton from your own life: ______

## PART 2 — THE SAME FIVE FACTS, THREE WAYS (14 min)

The CS club / chess club problem from L02, restated so you cannot pattern-match
it: **A** = students in the debate club, 15. **B** = students in the model
aircraft club, 22. **9** are in both. The school is 120.

Do it three times. The third time is the one that matters.

**(a) Region by region.**

| region | count |
|---|---|
| `A` only | |
| `B` only | |
| both | |
| neither | |
| **total = 120** | |

**(b) By the formulas, from `|A|`, `|B|`, `|A n B|` only.**

| quantity | formula | answer |
|---|---|---|
| union | | |
| intersection | | |
| exactly one | | |
| `A` only | | |
| `B` only | | |
| neither | | 120 − ______ |

**(c) The way a program would do it: build the sets, then operate.**

Write the code, do not run it. Predict the printed output.

```python
A = {"d%d" % i for i in range(1, 16)}          # 15 debaters
B = {"m%d" % i for i in range(1, 23)}          # 22 aircraft-club members
# 9 of the aircraft members are also debaters: m1..m9 are really d7..d15
for i in range(1, 10):
    B.remove("m%d" % i)
    B.add("d%d" % (i + 6))
print(len(A), len(B))
print(sorted(A & B))
print(len(A | B), len(A - B), len(A ^ B))
```

- ☐  `len(A)`: ______  `len(B)`: ______
- ☐  `A & B` is: ______
- ☐  `len(A | B)`, `len(A - B)`, `len(A ^ B)`: ______, ______, ______
- ☐  Did all three methods agree with (a) and (b)? If not, which one and why:
      ______

## PART 3 — WHY ADDING IS THE CLASSIC BUG (12 min)

Four scenarios. For each: name what was added, say which two groups could
overlap, and give the corrected number or say it cannot be corrected from the
information given.

1. A school reports "412 students in clubs this year, up from 388 last year, so
   club participation rose by 24 students." What is wrong with the comparison?
   ______
2. An admin counts 55 students in band and 38 in choir and reports "93 students
   in performing arts." Nothing is stated about overlap. What must be known to
   make 93 correct? ______
3. A security report says "the incident touched 3 servers, 12 accounts, and 4
   subnets — 19 affected entities." What is the name of the error, and what
   should the report have said instead? ______
4. A store counts 200 transactions on one day and 180 on the next, and the manager
   says "380 transactions over two days." Is that necessarily wrong? What would
   make it wrong? ______

- ☐  In which of the four is the error **most likely to be caught by a
      reviewer**, and why is that the dangerous one? ______
- ☐  Scenario 3 is the shape of a real incident report. What is the one sentence
      you would add to make it honest? ______

That last checkbox is a preview of the L13 defense requirement. The through-line
of this project is that the numbers are **assumptions the analyst chose**, and a
report that sums overlapping counts is a report making a claim it has not
earned.

## PART 4 — THE ERROR LOG (8 min)

Open your **Sets and Probability Error Log**, three columns: *what I wrote*,
*what it should have been*, *cause*. Tag each cause: **vocabulary**,
**double-count**, **region**, **formula**, **careless**.

- ☐  Every error from today is in, including the ones I marked wrong and you fixed
- ☐  At least three entries, and at least one from L02 or L03 that you have not
      thought about since
- ☐  Most common cause today: ______
- ☐  The single error in this log you think I will see again on the test:
      ______

## PART 5 — PREDICT U5 L06 (6 min)

U5 L06 is conditional probability from a contingency table. Write, in one
sentence each, in your own words and before seeing it:

- ☐  What a **conditional** probability asks, and how it differs from an ordinary
      one: ______
- ☐  Why the denominator is the part people get wrong: ______
- ☐  What a **contingency table** is, and what its row totals and column totals
      are for: ______

## TURN IN — Paper Check L01–L04

1. One photo of Parts 1–3, all work shown, no blank tables
2. One photo of the error log with causes tagged
3. Your three Part 5 sentences, written before U5 L06

**Grade this on the reasoning, not the arithmetic.** A wrong number with a
correct diagnosis of *why* it is wrong is worth more here than a right number
you got by guessing. Part 3 scenario 3 is the highest-value question on the
page; give it a real sentence.

## 📋 PREVIEW OF TOMORROW

**Next:** L06, Feb 24 — back to the machine, and the day conditional
probability arrives. You will build a contingency table, and the whole lesson
turns on one idea: **the conditional changes the denominator and nothing else.**

**Bring tomorrow:** laptop, and your error log. We start L06 by reading your logs.

## 🇹🇼 TAIWAN CONTEXT

Scenario 3 is not a hypothetical exercise. The ROC national CERT and the
Ministry of Digital Affairs have both had to correct public breach figures for
exactly this reason: an incident reported as a sum of affected hosts, accounts,
and segments produces a number several times larger than the number of distinct
real-world entities affected, and the correction reads in the press like
over-reporting rather than a counting error. No institution's reporting is
motivated to make itself look worse, which is precisely why the correction has
to come from outside.

The honest version of a count is one that says how the categories were defined
and whether they can overlap. That is not hedging. It is the difference between a
number a reader can use and a number a reader has to take on faith — and the
defense you write on L26 is graded on exactly that distinction.
