# U5 L05 — Paper Check: Why Double-Counting Is the Classic Bug

Names: ___________________________  Date: ____

Closed notes except the single page of formulas at the back. 50 minutes. No laptop. Graded on the reasoning, not the arithmetic: a wrong number with a correct diagnosis of why it is wrong scores higher than a right number obtained by guessing.

## 1: Vocabulary under pressure — Define, then give a non-math example

| term                     | your definition     | your example       |
| ------------------------ | ------------------- | ------------------ |
| subset                   | ______________      | ______________     |
| proper subset            | ______________      | ______________     |
| disjoint                 | ______________      | ______________     |
| complement               | ______________      | ______________     |
| symmetric difference     | ______________      | ______________     |

☐  Is the empty set a subset of every set? One-line proof: ______________

☐  Is the empty set a *proper* subset of the empty set, and why not: ______________

☐  Give a real singleton from your own life: ______________

## 2: The same five facts, three ways — Debate club 15, aircraft club 22, 9 in both, school of 120

**Section A — Region by region.**

| region              | count              |
| ------------------- | ------------------ |
| `A` only            | ______________     |
| `B` only            | ______________     |
| both                | ______________     |
| neither             | ______________     |
| **total = 120**     | ______________     |

**Section B — By the formulas, from `|A|`, `|B|`, `|A n B|` only.**

| quantity         | formula                  | answer             |
| ---------------- | ------------------------ | ------------------ |
| union            | ______________           | ______________     |
| intersection     | ______________           | ______________     |
| exactly one      | ______________           | ______________     |
| `A` only         | ______________           | ______________     |
| `B` only         | ______________           | ______________     |
| neither          | 120 − ______________     | ______________     |

**Section C — The way a program would do it.** Write the code; do not run it. Predict the printed output.

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

☐  `len(A)`: ______________  `len(B)`: ______________

☐  `A & B` is: ______________

☐  `len(A | B)`, `len(A - B)`, `len(A ^ B)`: ______________, ______________, ______________

☐  Did all three methods agree with (a) and (b)? If not, which one, and why: ______________

## 3: Why adding is the classic bug — Four scenarios

For each: name what was added, say which two groups could overlap, and give the corrected number or say it cannot be corrected from the information given.

1. A school reports "412 students in clubs this year, up from 388 last year, so participation rose by 24 students." What is wrong with the comparison: ______________
2. An admin counts 55 in band and 38 in choir and reports "93 in performing arts." Nothing states the overlap. What must be known for 93 to be correct: ______________
3. A security report says "the incident touched 3 servers, 12 accounts, and 4 subnets — 19 affected entities." Name the error and say what the report should have said instead: ______________
4. A store counts 200 transactions one day and 180 the next, and the manager says "380 over two days." Is that necessarily wrong, and what would make it wrong: ______________

☐  In which of the four is the error most likely to be caught by a reviewer, and why is that the dangerous one: ______________

☐  Scenario 3 is the shape of a real incident report. Write the one sentence that would make it honest: ______________

## 4: The error log — Three columns, causes tagged

Open your Sets and Probability Error Log: *what I wrote*, *what it should have been*, *cause*. Tag each cause **vocabulary**, **double-count**, **region**, **formula**, or **careless**.

☐  Every error from today is in, including the ones marked wrong and fixed: ______________

☐  At least three entries, including at least one from L02 or L03 you have not revisited: ______________

☐  Most common cause today: ______________

☐  The single error in this log you expect to see again on the test: ______________

## 5: Predict U5 L06 — Written before you see conditional probability

☐  What a **conditional** probability asks, and how it differs from an ordinary one: ______________

☐  Why the denominator is the part people get wrong: ______________

☐  What a **contingency table** is, and what its row and column totals are for: ______________

**TURN IN** — One photo of Parts 1–3 with all work shown and no blank tables, one photo of the error log with causes tagged, and your three Part 5 sentences as written before U5 L06.
