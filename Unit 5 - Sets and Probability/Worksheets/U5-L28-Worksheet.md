# U5 L28 — Confounding: When the Naive Association Lies

Names: ___________________________  Date: Mar 26

No laptop. Calculator allowed. This is the arithmetic you will use most often outside this course, because it is the arithmetic behind every headline that says an exposure is associated with an outcome.

Two lines of subtraction. That is the whole technique.

## The situation

A consultancy reviews its incident data across 400 former clients. It finds that remote administrative access was provisioned for some clients, that some clients suffered credential incidents, and that the two overlap suspiciously well. The conclusion the consultancy wants to publish:

> "Remote access is associated with a four-fold increase in credential incidents. Provisioning remote access should be restricted."

☐  Before anything else: is that conclusion supportable from these numbers: ______________

## 1: The naive association — 10 min

| credential incident     | remote access     | no remote access     | total       |
| ----------------------- | ----------------- | -------------------- | ----------- |
| yes                     | 96                | 56                   | 152         |
| no                      | 24                | 224                  | 248         |
| **total**               | **120**           | **280**              | **400**     |

☐  **N1.** `P(incident | remote) = 96/120 =` ______________

☐  **N2.** `P(incident | no remote) = 56/280 =` ______________

☐  **N3.** The ratio, which is the "four-fold increase" the consultancy wants to publish: ______________

☐  **N4.** The number that makes the whole thing suspect: how much more common is remote access among the incident group than among the clean group, as a ratio of `120/152` to `120/248`: ______________

☐  **N5.** The overall credential incident rate is `152/400 = 0.38`. Which of N1 and N2 is further from it, and why does that matter: ______________

N4 and N5 together are the whole lesson. Remote access is **far more common among the clients who had incidents** than among those who did not. That does not make it a cause; it makes it a characteristic shared by the group in which incidents occurred. The consultancy has measured a difference between two groups and reported it as an effect on an individual. N3 is a ratio of two group rates, and a ratio of group rates is a statement about groups.

## 2: Stratify — 20 min

The third factor is `already exposed` — the client's own network had already been compromised, independently of anything the consultancy did. Split by it.

**Stratum 1 — already exposed (280 clients):**

|                 | remote     | no remote     | total       |
| --------------- | ---------- | ------------- | ----------- |
| incident        | 68         | 28            | 96          |
| no incident     | 12         | 172           | 184         |
| **total**       | **80**     | **200**       | **280**     |

**Stratum 2 — not exposed (120 clients):**

|                 | remote     | no remote     | total       |
| --------------- | ---------- | ------------- | ----------- |
| incident        | 28         | 28            | 56          |
| no incident     | 12         | 52            | 64          |
| **total**       | **40**     | **80**        | **120**     |

☐  **S1.** `P(incident | remote, exposed) = 68/80 =` ______________

☐  **S2.** `P(incident | no remote, exposed) = 28/200 =` ______________

☐  **S3.** `P(incident | remote, not exposed) = 28/40 =` ______________

☐  **S4.** `P(incident | no remote, not exposed) = 28/80 =` ______________

☐  **S5.** The remote-access ratio **within** the exposed stratum, `(68/80) ÷ (28/200)` = ______________

☐  **S6.** And **within** the not-exposed stratum, `(28/40) ÷ (28/80)` = ______________

☐  **S7.** Two ratios, and they are not the same. Which is larger, and what does the difference between S3 and S4 tell you about the size of the association once the third factor is held fixed: ______________

**The answers are the point of the day.** The naive ratio is 4.00. The ratio within the not-exposed stratum is **2.00** — half the drama, and the direction of the effect survives. Meanwhile the ratio within the exposed stratum is about 6, *larger* than the naive figure. The remote-access effect is real, it is present in both strata, and it is **not the same size in both** — which is exactly what "confounded" means. The naive 4.00 was an average across strata that happened to land between a 2.00 and a 6.07 without corresponding to either.

A reader of the original report would conclude that remote access is dangerous. A reader of the stratified table concludes something more precise and more useful: **remote access roughly doubles the credential incident rate in a client that was not already exposed, and matters rather more in one that was — but the clients where it matters most were already in trouble, and remote access is part of how we recognise that rather than a cause of it.**

☐  **S8.** The not-exposed stratum is only 120 of the 400 clients. If the consultancy's actual clients are mostly unexposed, is the naive 4.00 an overstatement or an understatement **for that population**: ______________

☐  **S9.** Which single number in the original report would have changed the conclusion — and confirm it appears nowhere in the report: ______________

## 3: The arithmetic of the overstatement — 12 min

There is a two-line formula here and it is worth memorising.

Let the naive ratio be `R_naive = 4.00`. Let the ratio within the not-exposed stratum be `R_true = 2.00`. The overstatement is a property of the **ratios**, not of the raw rates.

☐  **O1.** In ratio terms, the naive figure overstates by a factor of `4.00 / 2.00 =` ______________

☐  **O2.** As a relative overstatement, that is ______________, i.e. the naive claim is ______________ times too large. In *rate* terms, the naive rate `0.80` exceeds the not-exposed remote rate `0.70` by ______________ percentage points: ______________

☐  **O3.** Which of those two ways of stating the overstatement is the more honest one for a report to carry, and why: ______________

☐  **O4.** Write the correction in the form a journalist could print it, in one sentence, without using the word "confounded": ______________

O3 is worth arguing about and there is a real trap in it. A factor-of-2 overstatement sounds severe; a 10-percentage-point difference in an absolute rate sounds mild. **Which one flatters the original claim depends entirely on the denominator.** The honest answer is that both are legitimate, a report should give the one its reader will actually use, and the failure is not choosing either — it is that the consultancy gave the ratio and withheld the rates, so its reader could not compute the other and had no way to know which was being flattered.

## 4: The argument — 8 min

The consultancy has published the four-fold claim. It has not been retracted.

☐  **A1.** Write the **three-sentence** correction, in the register of L27's response, naming the stratum and the corrected figure: ______________

☐  **A2.** What is the strongest thing the consultancy can say in reply, and is it actually a defence of the *claim* or only of the *method*: ______________

☐  **A3.** A restricted remote-access policy is a *cheap* control. Does the confounding analysis argue for or against implementing it, and why is that a different question from whether the claim was true: ______________

A3 is the item that separates analysis from advocacy, and it has a defensible answer: **the stratification shows the effect is smaller than claimed, not that it is absent, and a cheap control with a real but smaller benefit may still be worth adopting.** An analyst who arrives at "the claim was overstated" and stops has learned the technique and not the judgement. The recommendation and the effect size are separate quantities, and a correction to one is not a refutation of the other. The mistake in this area is treating a corrected effect size as a reason to do nothing.

## TURN IN — Confounding

1. Both tables, all of N1–N5, S1–S9, O1–O4
2. The three-sentence correction
3. The A3 answer
4. One paragraph: what would you have to measure, and how much of it, to separate the remote-access effect from the exposure effect: ______________
