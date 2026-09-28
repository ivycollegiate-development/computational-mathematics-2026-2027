# U5 L11 — Paper Check: Conditionals, Bayes, and Expected Value

Names: ___________________________  Date: ____

Closed notes. Calculator allowed. 50 minutes. No laptop. The Unit 5 test is five pages of paper with no tools but this one, and the honesty audit in Part 4 is the graded item.

## 1: Conditionals and independence — Reconstruct the L06 mail-filter table from memory

|                      | allowed            | blocked            | row total          |
| -------------------- | ------------------ | ------------------ | ------------------ |
| benign               | 900                | 100                | ______________     |
| malicious            | 40                 | 60                 | ______________     |
| **column total**     | ______________     | ______________     | ______________     |

☐  Grand total: ______________

☐  `P(malicious)` = ______________

☐  `P(allowed | malicious)` = ______________ (show the fraction you divided by: ______________)

☐  `P(allowed | benign)` = ______________

☐  `P(blocked | malicious)` = ______________

☐  Is "allowed" independent of "malicious"? Show the check two ways, once with a conditional and once with the product rule: ______________

☐  The same condition in the other order, `P(malicious | allowed)` = ______________

☐  Which of your two answers is bigger, and by how much: ______________

☐  A classmate writes "malicious traffic is 40% likely to be allowed through." Which of your numbers is that, and what denominator did they use: ______________

## 2: Bayes, on paper, no notes — Base rate 1 in 1,000, sensitivity 99%, false-positive rate 2%

☐  Bayes' theorem from memory, with every symbol named: ______________

| branch                 | fraction           | number out of 1,000     |
| ---------------------- | ------------------ | ----------------------- |
| disease, test +        | ______________     | ______________          |
| disease, test −        | ______________     | ______________          |
| no disease, test +     | ______________     | ______________          |
| no disease, test −     | ______________     | ______________          |

☐  The posterior: ______________ as a fraction, ______________ as a percent

☐  The same problem with a **1%** false-positive rate: ______________ as a percent

☐  The same problem with a **0.1%** false-positive rate: ______________ as a percent

☐  The same problem with **100% sensitivity and 0% false positives**: ______________ as a percent

☐  Describe the shape of that sequence in one sentence, and say why it stops where it does: ______________

☐  The denominator question: someone tells you the answer is 11/233. Is that denominator counting 233 people, or 233 something else: ______________

☐  The security version, no setup help: a rule has a 2% false-positive rate, and the threat it watches for occurs 1 time in 400. Approximately what fraction of alerts are real? Show your arithmetic: ______________

## 3: Expected value — The arithmetic, then the sentence

**Section A — Part A, arithmetic. Show the multiplication.**

1. A fair coin pays 3 dollars on heads and loses 1 on tails. EV = ______________
2. A die pays the number shown. EV = ______________
3. A threat occurs with probability 1/50 a year and costs 90,000 to recover. EV = ______________
4. Two threats, independent: 1/20 at 4,000 and 1/100 at 15,000. Combined EV = ______________
5. A distribution `[(1/4, 0), (1/4, 500), (1/2, 1,000)]`. EV = ______________

☐  Which of the five is easiest to get wrong, and why: ______________

☐  Number 4 is arithmetically fine and conceptually wrong. What assumption does it make, and when would it fail: ______________

**Section B — Part B, the sentence that gets graded.**

6. Your simulator reports `expected loss = 810`. Write two sentences:

   One that states the number correctly, including what it is a mean over: ______________

   One that states what the number does not tell the reader: ______________

☐  A decision-maker reads `810` and spends 400 on a mitigation. Is that a defensible reading of the number alone: ______________

☐  What one additional statistic would put in the report to make the 400 obviously wrong: ______________

## 4: The honesty audit — For every number, can you say where it came from?

| #                   | number             | computed or assumed?     | if assumed, who chose it and why     |                    |
| ------------------- | ------------------ | ------------------------ | ------------------------------------ | ------------------ |
| 1                   | ______________     | ______________           | ______________                       |                    |
| 2                   | ______________     | ______________           | ______________                       |                    |
| 3                   | ______________     | ______________           | ______________                       |                    |
| 4                   | ______________     | ______________           | ______________                       |                    |
| 5                   | ______________     | ______________           | ______________                       |                    |
| Q1 `P(allowed\      | malicious)`        | ______________           | ______________                       | ______________     |
| Bayes posterior     | ______________     | ______________           | ______________                       |                    |

☐  Count the "assumed" rows: ______________

☐  The finding, in one sentence: in a risk model, the things that look most like measurements are actually ______________

☐  One thing you could do to turn one of those assumptions into a measurement before U5 L13: ______________

**TURN IN** — Parts 1–3 photographed with all work shown including the tables, the honesty audit with the finding sentence, and your error log updated with today's entries and causes tagged.
