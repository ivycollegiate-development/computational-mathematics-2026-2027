# U5 L11 — Paper Check L06–L10

**Date:** Wednesday, March 3, 2027
**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.5–5.7 — compute conditional probabilities, posteriors, and expected
values on paper under exam conditions; write EV claims with their assumptions

---

**No laptop today.** Calculator allowed. The contingency table, Bayes, and EV
all fit on one page, and that is the constraint you should be practising: the
Unit 5 test is five pages of paper with no tools but this one.

## PART 1 — CONDITIONALS AND INDEPENDENCE (14 min)

Use the mail-filter table from L06. **Do not look it up** — reconstruct it, then
answer.

|  | allowed | blocked | row total |
|---|---|---|---|
| benign | 900 | 100 | |
| malicious | 40 | 60 | |
| **column total** | | | |

- ☐  Both row totals, both column totals, the grand total
- ☐  `P(malicious)` = ______
- ☐  `P(allowed | malicious)` = ______ (show the fraction you divided by)
- ☐  `P(allowed | benign)` = ______
- ☐  `P(blocked | malicious)` = ______
- ☐  **Independence:** is "allowed" independent of "malicious"? Show the check
      two ways — one with a conditional, one with the product rule. ______

- ☐  Here is the same question with the condition written in the other order:
      `P(malicious | allowed)` = ______
- ☐  Which of your two answers is bigger, and by how much? ______
- ☐  **A classmate writes: "malicious traffic is 40% likely to be allowed
      through."** Which of your numbers is that, and what is the denominator
      they used? ______

That last one is worth four points. The English sentence is ambiguous about
which number it means, and the two candidate numbers differ by a factor of
about ten. **A probability without its denominator is not a claim; it is a
rounding error waiting to be quoted.**

## PART 2 — BAYES, ON PAPER, NO NOTES (14 min)

The L07 disease problem: base rate 1 in 1,000, sensitivity 99%, false-positive
rate 2%. A positive test.

- ☐  Write Bayes' theorem from memory, with every symbol named: ______
- ☐  Fill in the four numbers, as fractions of 1,000 people:

| branch | fraction | number out of 1,000 |
|---|---|---|
| disease, test + | | |
| disease, test − | | |
| no disease, test + | | |
| no disease, test − | | |

- ☐  The posterior: ______ as a fraction, ______ as a percent
- ☐  The same problem with a **1%** false-positive rate: ______ as a percent
- ☐  The same problem with a **0.1%** false-positive rate: ______ as a percent
- ☐  The same problem with a **100% sensitivity, 0% false positives**:
      ______ as a percent

- ☐  Describe the shape of that sequence in one sentence. What is happening to
      the answer as the false-positive rate falls toward zero, and why does it
      stop where it does: ______
- ☐  **The denominator question.** Someone tells you the answer is 11/233. What
      is that denominator counting — 233 people, or 233 *something else*?
      ______

- ☐  Now the security version, no setup help. A rule has a 2% false-positive
      rate. The threat it watches for occurs 1 time in 400. Approximately what
      fraction of alerts are real? Show your arithmetic: ______

## PART 3 — EXPECTED VALUE, AND THE SENTENCE (14 min)

**Part A, arithmetic.**

1. A fair coin pays 3 dollars on heads and loses 1 on tails. EV = ______
2. A die pays the number shown. EV = ______
3. A threat occurs with probability 1/50 a year and costs 90,000 to recover.
   EV = ______
4. Two threats, independent: 1/20 at 4,000 and 1/100 at 15,000. Combined EV = ______
5. A distribution `[(1/4, 0), (1/4, 500), (1/2, 1,000)]`. EV = ______

- ☐  All five, with the multiplication shown
- ☐  Which of the five is easiest to get wrong, and why: ______
- ☐  Number 4 is *arithmetically* fine and *conceptually* wrong. What assumption
      does it make, and when would it fail: ______

**Part B, the sentence that gets graded.**

6. Your simulator reports: `expected loss = 810`. Write **two** sentences:

  - One that states the number correctly, including what it is a mean over: ______
  - One that states what the number does **not** tell the reader: ______

- ☐  Then: a decision-maker reads `810` and spends 400 on a mitigation. Is that
      a defensible reading of the number alone? ______
- ☐  What one additional statistic would you put in the report to make the 400
      obviously wrong? ______

## PART 4 — THE HONESTY AUDIT (8 min)

For every number you produced today, mark whether you can say where it came
from:

| # | number | computed or assumed? | if assumed, who chose it and why |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| Q1 `P(allowed\|malicious)` | | | |
| Bayes posterior | | | |

- ☐  Count the "assumed" rows: ______
- ☐  **The finding, in one sentence:** in a risk model, the things that look
      most like measurements are actually: ______
- ☐  One thing you could do to turn one of those assumptions into a measurement
      by next Friday: ______

## TURN IN — Paper Check L06–L10

1. Parts 1–3 photographed, all work shown, including the tables
2. The honesty audit, with the finding sentence
3. Your error log updated with today's entries, causes tagged

**The honesty audit is the graded item.** A student who computes every number
correctly and cannot say which four of them are guesses has not learned the
thing this project is actually about. A student who computes three correctly,
misses one, and correctly identifies every assumption gets the higher mark.

## 📋 PREVIEW OF TOMORROW

**Next:** L12, Thu Mar 4 — back to the machine, and the day you find out that
expected value is not enough. Four gambles, all with EV = 1,000, and they are
not remotely the same bet. `riskkit.py` gets `variance` and a function that
reports the shape, not just the mean.

**Bring tomorrow:** laptop, and today's honesty audit. I want to see the
"one thing you could measure" line.

## 🇹🇼 TAIWAN CONTEXT

The security version in Part 2 is the number that matters most in this field,
and it is the one that is almost never published. "Our SIEM produces 4,000
alerts a week" is a number every organization can produce. "Of those alerts,
2.3% correspond to a confirmed incident" is a number that tells a budget meeting
something actionable, and publishing it commits the organization to a position
that a vendor can then attack — which is precisely why the number stays inside
the security team.

The ROC national CERT's guidance on detection maturity makes the same
observation from the other side: an organization cannot improve what it does not
measure, and the measurement that matters is the conditional rate, not the
volume. An organization drowning in alerts has a base-rate problem, and a
base-rate problem cannot be fixed by buying more detection — it is fixed by
narrowing what the rules watch for until the conditional rate means something.
Your Risk Simulator is a model of exactly that decision, which is why the
defense has to state the base rate and not only the expected value.
