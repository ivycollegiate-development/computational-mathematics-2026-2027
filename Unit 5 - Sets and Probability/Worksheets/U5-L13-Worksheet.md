# U5 L13 — Paper Check: The Mean Is Not a Risk Description

Names: ___________________________  Date: ____

Closed notes. Calculator allowed. 50 minutes. No laptop. Two of today's five questions have no arithmetic in them, and those are graded hardest. The Part 4 paragraph is the graded artefact and is worth more than the arithmetic.

## 1: Arithmetic, fast — In order, without pausing

1. Outcomes `(1/3, 0), (1/3, 90), (1/3, 180)`. EV = ______________
2. Outcomes `(1/2, +400), (1/2, −400)`. EV = ______________  variance = ______________
3. A threat with `P = 1/4` and impact 16,000. EV = ______________
4. Four books, each EV = 500, variances: 0, 900, 4,100, 25,000. Ranking by expected value: ______________  Ranking by risk: ______________
5. For `[(9/10, −200), (1/10, 1,800)]`: `P(loss)` = ______________, mean outcome when it loses = ______________, standard deviation = ______________

☐  Question 4: your two rankings differ for every book except the first. Which is correct to report, and to whom: ______________

☐  Question 5: which of your three numbers describes the typical year, and which describes the bad year: ______________

## 2: The two non-numerical questions

**Q6.** Your simulator's `shape_report` returns this:

```
{'ev': 810, 'variance': 2205400, 'stdev': 1484.8, 'p_loss': 0.30,
 'mean_loss_given_loss': -2700, 'best': 0, 'worst': -2700, 'n_outcomes': 2}
```

A decision-maker reads `ev: 810` and declines to spend 400 on a mitigation.

☐  Is that decision defensible on the numbers above: ______________

☐  Which single key would have changed their mind, and why that one: ______________

☐  Rewrite the report's `ev` key so nobody can quote it alone. One line of code: ______________

**Q7.** You have a `variance` of 2,205,400 and an expected value of −810, and you are asked "how risky is this?" Write the answer a decision-maker should hear, in three sentences, using the right statistics and saying what is still missing.

☐  Your three sentences: ______________

☐  What statistic is absent from the report that you would need before answering confidently: ______________

☐  The 30% probability of a loss: is that high or low for a risk like this, and why can you not simply say "high" or "low": ______________

## 3: Test-time form — The shape the Unit 5 test will take

| #          | section                                  | what it asks                         | points     |
| ---------- | ---------------------------------------- | ------------------------------------ | ---------- |
| 1–3        | set vocabulary and Venn regions          | define, build, count                 | 12         |
| 4          | inclusion–exclusion, three sets          | the full formula                     | 10         |
| 5–6        | contingency table and conditionals       | one direction, then the *other*      | 14         |
| 7          | Bayes                                    | setup, and the base-rate comment     | 14         |
| 8–9        | expected value, variance, interpretation | the number, then the sentence        | 20         |
| 10         | modelling judgment                       | *why these assumptions*              | 30         |

☐  The last row is worth half the paper. Confirm you understand that: ______________

☐  Which of rows 1–9 is your weakest, and what specifically will you practise: ______________

☐  Write the full three-set formula with all six pairwise terms, from memory: ______________

☐  Question 6 will give you the condition in the order opposite to the natural reading. What will you do to protect yourself: ______________

## 4: What I'll ask you — Write for eight minutes without stopping

> You have a model. Its numbers are all reasonable. It will be read by someone who will act on it. Write the paragraph that goes with it.

The paragraph must say what each likelihood figure means, where at least one of them came from, and what the expected value does not tell the reader. It must be readable by someone who does not know what a distribution is.

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

☐  Re-read it once. Would you sign your name to it: ______________

☐  Count the sentences that state a number without saying what the number is a mean over: ______________

☐  Revise it once now, in the margins, and keep the revision. The paragraph is 60% of this unit's final grade: ______________

**TURN IN** — Parts 1–3 photographed with work shown, Q6 and Q7 answered in full, the Part 4 paragraph with your margin revision, and your error log updated.
