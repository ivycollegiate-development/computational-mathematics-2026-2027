# U5 L01 — Unit Launch: Sets as the Language of "Which of These"

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (unit launch, 50 minutes)
**LO:** 5.1 — state membership, inclusion, and exclusion precisely, and explain why
sets are the right tool for "which of these" questions

---

## TODAY'S PURPOSE

Unit 4 was algebra: manipulate symbols until an answer falls out. Unit 5 is a
different kind of day. **Nothing gets solved.** Today you learn a way of
*talking* precisely about membership — who is in, who is out, who is in both,
who is in neither — and that turns out to be the thing probability is built on.

You already do this informally. "Which students are in both the CS club and
chess club?" is a set question. "How many distinct pieces of software are in
this build?" is a set question. The unit's whole first move is to stop being
informal about it.

**The project is announced at the end.** Read that section before you leave.

## PART 1 — THE VOCABULARY, WRITTEN DOWN (12 min)

Fill in the definition in your own words, not the glossary's.

| term | your definition | a concrete example from your own life |
|---|---|---|
| element / member | | |
| set | | |
| belongs to (`in`) | | |
| does not belong to (`not in`) | | |
| subset (`<=`) | | |
| proper subset (`<`) | | |
| universal set `U` | | |
| complement `A'` | | |
| disjoint / mutually exclusive | | |

- ☐  Write a set three different ways and say when you would use each.
      `{1, 2, 3}` / roster / `1..3` / "the integers from 1 to 3" / **set-builder**
      `x for x in 1..3` — which is clearest for a set of 10,000 emails? ______
- ☐  Is `2` an element of the set of even numbers, or a subset of it? Which
      question are you actually asking? ______
- ☐  A set has no order and no repeats. Why does that matter — what breaks if a
      "set" keeps its order? ______

## PART 2 — THREE WORDS, THREE REAL QUESTIONS (12 min)

Read each sentence and write the set question hiding inside it.

1. "Which of our 340 students take Mandarin, and how many is that?"
   Set question: ______  Answer type: roster / count / both
2. "Do *any* of these three servers run an unpatched OS?"
   Set question: ______  This is asking about ______ (union / intersection /
   complement)
3. "How many of our students take Mandarin *but not* French?"
   Set question: ______  This is ______ minus ______
4. "Every one of our students takes at least one language. What is the
   complement of 'takes Mandarin'?"
   ______

- ☐  Which of those four would be *painful* to answer by counting one at a time,
      and why? ______
- ☐  A set question with a roster answer and a set question with a count answer
      are the same question. Name a case where the roster is useless to you.
      ______

That is the whole reason this unit exists: **a count answer is a set answer
you have thrown away information about.** In six weeks you will be defending
numbers, and a number with no roster behind it cannot be checked.

## PART 3 — SUBSET TRAPS (10 min)

For each pair, decide: is the first a subset of the second? Answer yes, no, or
*not enough information*.

| # | A | B | verdict | why |
|---|---|---|---|---|
| 1 | `{1, 2, 3}` | `{1, 2, 3, 4, 5}` | | |
| 2 | `{1, 2, 3}` | `{1, 2, 3}` | | |
| 3 | `{2, 4, 6}` | `{1, 2, 3, 4, 5, 6}` | | |
| 4 | all even integers | all integers | | |
| 5 | `{apple, banana}` | all fruits | | |
| 6 | `{apple, banana}` | all foods | | |
| 7 | `{}` | `{1, 2, 3}` | | |
| 8 | all prime numbers | all integers | | |

- ☐  Which single row is the one people argue about? ______ Why is it arguable?
- ☐  Row 5 vs row 6: what does the difference between "fruit" and "food" have
     to do with sets? ______
- ☐  Write a set that is a subset of *every* set. ______
- ☐  Can two sets be subsets of each other without being equal? ______

## PART 4 — WHY SETS, NOT COUNTS (10 min)

A software team has 9 laptops. Each machine runs exactly one OS.

| OS | machines |
|---|---|
| Windows | 4 |
| macOS | 3 |
| Linux | 2 |

Now they merge with a second team: 5 more machines, 3 Windows and 2 Linux.

- ☐  Windows machines after the merge: ______
- ☐  Linux machines after the merge: ______
- ☐  Total machines after the merge: ______
- ☐  Could you have computed "total" by adding the two OS counts? ______
      If not, why not? ______
- ☐  Rewrite the question so the answer is a set: "which ______ ?" ______

The trap in this exercise: **counts of parts do not add to a count of the
whole** unless the parts are known to be disjoint. A set states the disjointness;
a bare number does not. This is the same error the Unit 4 cipher project ran
into when it counted letters across ciphers.

## PART 5 — THE PROJECT, ANNOUNCED (6 min)

**Risk Simulator.** You will build a program that takes a threat model *as
data* — assets, threats, likelihoods, impacts — computes the expected loss, and
runs a Monte Carlo simulation of the same model.

| When | What |
|---|---|
| Mar 17 | paper design of the threat model, in class |
| Mar 26 | **Risk Simulator due, 11:59 PM** |
| Mar 31 | **Demo. Unit 5 complete** |

Two things to say out loud now, because they are the whole grade:

- The likelihoods and impact values are **assumptions the analyst chose.** They
  are not measurements. Your defense must say so explicitly, in writing.
- Everything you need for the build is already installed: the standard library
  and SymPy. **No pip installs. Tell me if something is missing.**

## TURN IN — Unit 5 Launch

1. Parts 1–4, photographed, all tables filled in
2. One sentence: *a set question I actually needed this week was ______*
3. A repository created for `compmath-u5-risk-simulator`, public, default branch
   `main`, linked in Classroom — **empty is fine**, we fill it on L14

**Graded on precision of language.** If your definition of "subset" would let
someone argue with it, rewrite it.

## 📋 TONIGHT, 10 MINUTES

Type a set and look at what Python does with it. No analysis, just look:

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
print(sorted(A & B))
print(sorted(A | B))
print(sorted(A - B))
print(sorted(B - A))
print(sorted(A ^ B))
print(sorted(set(range(1, 8)) - A))
print(A <= {1, 2, 3, 4, 5})
print(len(A & B))
```

Real output:

```
[4, 5]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3]
[6, 7]
[1, 2, 3, 6, 7]
[6, 7]
True
2
```

Do not memorize it. Just notice that `A ^ B` is "in exactly one" and that
Python has a name for it, which is a thing you had to draw two circles for on
paper.

## 📋 PREVIEW OF TOMORROW

**Next:** L02, Feb 18 — still paper. You draw the circles by hand: union,
intersection, difference, and the symmetric difference, and you fill in the
region-by-region counts that the U5 L03 code will have to reproduce exactly.

**Bring tomorrow:** pencil, ruler, notebook. No laptop.

## 🇹🇼 TAIWAN CONTEXT

"Which of these" is not a math-game question in Taiwan, it is the shape of
almost every public-sector form. Student records systems at universities and
hospitals are built as set unions across campuses: the same person exists in
three databases and a naive query that concatenates the tables produces
duplicates, not members. The `A ^ B` you met tonight — "in exactly one of these
two systems and not both" — is the reconciliation query that a records team
runs to find accounts that exist on only one side. Duplicates are the counting
version of that same idea, and this unit is nine days from showing you exactly
how much money a duplicate costs.
