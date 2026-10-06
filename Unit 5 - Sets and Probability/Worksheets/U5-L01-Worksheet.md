# U5 L01 — Unit Launch: Set Vocabulary and the Risk Simulator

Names: ___________________________  Date: ____

Closed notes. 50 minutes. No laptop today. Parts 1–4 are graded on the precision of your language; the project repository is created and linked in Classroom, and it may stay empty until L14.

## 1: Vocabulary — Define each in your own words, with an example from your own life

**Section A — The nine terms.**

| term                              | your definition     | a concrete example from your own life    |
| --------------------------------- | ------------------- | ---------------------------------------- |
| element / member                  | ______________      | ______________                           |
| set                               | ______________      | ______________                           |
| belongs to (`in`)                 | ______________      | ______________                           |
| does not belong to (`not in`)     | ______________      | ______________                           |
| subset (`<=`)                     | ______________      | ______________                           |
| proper subset (`<`)               | ______________      | ______________                           |
| universal set `U`                 | ______________      | ______________                           |
| complement `A'`                   | ______________      | ______________                           |
| disjoint / mutually exclusive     | ______________      | ______________                           |

**Section B — The three questions.**

☐  A set can be written as a roster `{1, 2, 3}`, a range `1..3`, in words, or in set-builder form `x for x in 1..3`. Which form is clearest for a set of 10,000 email addresses, and why: ______________

☐  Is `2` an element of the set of even numbers, or a subset of it? State which question each one asks: ______________

☐  A set has no order and no repeats. Name one thing that breaks if a collection called a "set" keeps its order: ______________

## 2: Real questions — Find the set question hiding inside each sentence

1. "Which of our 340 students take Mandarin, and how many is that?"
   Set question: ______________  Answer type (roster / count / both): ______________
2. "Do *any* of these three servers run an unpatched OS?"
   Set question: ______________  This is asking about ______________ (union / intersection / complement)
3. "How many of our students take Mandarin *but not* French?"
   Set question: ______________  This is ______________ minus ______________
4. "Every one of our students takes at least one language. What is the complement of 'takes Mandarin'?"
   ______________

☐  Which of those four is most painful to answer by counting one at a time, and why: ______________

☐  Name a case where the roster is the answer you need and a bare count is useless: ______________

## 3: Subset traps — Yes, no, or not enough information

| #          | A                     | B                        | verdict     | why        |
| ---------- | --------------------- | ------------------------ | ----------- | ---------- |
| 1          | `{1, 2, 3}`           | `{1, 2, 3, 4, 5}`        | ______      | ______     |
| 2          | `{1, 2, 3}`           | `{1, 2, 3}`              | ______      | ______     |
| 3          | `{2, 4, 6}`           | `{1, 2, 3, 4, 5, 6}`     | ______      | ______     |
| 4          | all even integers     | all integers             | ______      | ______     |
| 5          | `{apple, banana}`     | all fruits               | ______      | ______     |
| 6          | `{apple, banana}`     | all foods                | ______      | ______     |
| 7          | `{}`                  | `{1, 2, 3}`              | ______      | ______     |
| 8          | all prime numbers     | all integers             | ______      | ______     |

☐  Which single row do people argue about, and why is it arguable: ______________

☐  Row 5 versus row 6: what does the difference between "fruit" and "food" do to the set relationship: ______________

☐  Write a set that is a subset of *every* set: ______________

☐  Can two sets be subsets of each other without being equal: ______________

## 4: Counts versus sets — Why the parts do not add

A software team has 9 laptops, each running exactly one OS.

| OS          | machines     |
| ----------- | ------------ |
| Windows     | ______       |
| macOS       | ______       |
| Linux       | ______       |

They merge with a second team of 5 machines: 3 Windows and 2 Linux.

☐  Windows machines after the merge: ______________

☐  Linux machines after the merge: ______________

☐  Total machines after the merge: ______________

☐  Could you get "total" by adding the OS counts alone? If not, why not: ______________

☐  Rewrite the last question so its answer is a set — "which ______________ ?": ______________

## 5: The project — Risk Simulator, announced

You will build a program that takes a threat model as data (assets, threats, likelihoods, impacts), computes the expected loss, and runs a Monte Carlo simulation of the same model.

| When           | What                                     |
| -------------- | ---------------------------------------- |
| Mar 17     | paper design of the threat model, in class |
| Mar 26     | Risk Simulator due, 11:59 PM             |
| Mar 31     | Demo. Unit 5 complete                    |

☐  In one sentence, a set question you actually needed this week: ______________

☐  Repository `compmath-u5-risk-simulator` created, public, default branch `main`, linked in Classroom (empty is fine): ______________

☐  Read this before you leave: the likelihoods and impact values in the model are assumptions the analyst chose, not measurements, and your defense must say so in writing: ______________

**TURN IN** — Parts 1–4 photographed with every table filled in, the one-sentence set question, and the repository link.

___

## Tonight, 10 minutes, on your own machine

Open a Python prompt. Type these eight lines with `A = {1, 2, 3, 4, 5}` and `B = {4, 5, 6, 7}` and record what each one prints. Do not analyze them; just look.

| expression                | predicted output     | type (set / list / bool / int)     |                    |
| ------------------------- | -------------------- | ---------------------------------- | ------------------ |
| `A & B`                   | ______________       | ______________                     |                    |
| `A \                      | B`                   | ______________                     | ______________     |
| `A - B`                   | ______________       | ______________                     |                    |
| `A ^ B`                   | ______________       | ______________                     |                    |
| `len(A & B)`              | ______________       | ______________                     |                    |
| `A & B == {4, 5}`         | ______________       | ______________                     |                    |
| `A <= B`                  | ______________       | ______________                     |                    |
| `set(range(1,8)) - A`     | ______________       | ______________                     |                    |

Bring the filled table to L03. Python has a name for "in exactly one of these two sets" that you had to draw two circles for on L02.
