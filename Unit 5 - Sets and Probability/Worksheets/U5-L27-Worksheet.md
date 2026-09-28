# U5 L27 — Someone Else's Model: Find the Error in a Plausible Report

Names: ___________________________  Date: ____

No laptop. Calculator allowed. This is the hardest day in the unit and there is no code on it.

You are handed a model produced by another organisation. It is competent, it is well-formatted, it has a table and a confidence statement and a recommendation. It is also **wrong**, and the wrongness is not in the code — it never was. Your job is to find the assumption, state the correction, and write the response.

## The report you have been sent

> **Security Risk Assessment — Ardent Logistics Ltd**
> Prepared for the board. March 2027.
>
> Four threat vectors were identified and modelled. Each was assigned an annual likelihood and a financial impact, derived from a sector benchmark study of logistics firms of comparable size.

| vector                                   | annual likelihood     | impact     | expected loss     |
| ---------------------------------------- | --------------------- | ---------- | ----------------- |
| T1 credential phishing                   | 0.20                  | 3,000      | 600               |
| T2 ransomware on file server             | 0.15                  | 45,000     | 6,750             |
| T3 network misconfiguration              | 0.20                  | 12,000     | 2,400             |
| T4 credential phishing, second vector    | 0.05                  | 3,000      | 150               |

> **Total expected annual loss: 9,900**
> **Probability of at least one vector firing: 0.20 + 0.15 + 0.20 + 0.05 = 0.60**
> **Confidence: moderate. Figures are drawn from sector benchmark data rather than the firm's own incident history, which comprises a single incident in three years.**
>
> **Recommendation: proceed with the proposed backup programme.**

## 1: Read it as a skeptic, not a user — 10 min

Do not start by judging the recommendation. Start by asking what the document has actually established.

☐  **Q1.** The report says `P(at least one) = 0.60`. Is that a valid probability? Compute the exact value by inclusion–exclusion and say whether the report's number is an overstatement, an understatement, or a coincidence: ______________

☐  **Q2.** `Total expected annual loss: 9,900`. Check the arithmetic of the four rows. Does the column add up: ______________

☐  **Q3.** The four rows produce two pairs that look like they describe the same thing. Identify them: ______________

☐  **Q4.** The board recommendation is to spend money. Which of the four vectors would have to be true for that recommendation to be right, and does the report support it: ______________

Q4 is the question that matters. The recommendation to spend is a decision about the worst plausible outcome, not about the average, and the report offers one number. Before you reject the report, note that the recommendation may still be correct: a model can produce a wrong number and a right answer. Say so explicitly in Q4, because a critique that only finds errors is not a critique, it is an objection.

## 2: Find the error — 20 min

There are at least four problems. Find as many as you can, and for each separate the **symptom** (what looks wrong) from the **cause** (the assumption that produced it).

**P1 — the probability.** T1 and T4 are described as two vectors but the likelihoods are `0.20` and `0.05` against the same 3,000 impact.

☐  If they are the same threat measured twice, what is the correct treatment: ______________

☐  If they are genuinely distinct vectors, the report still owes the reader an independence assumption and does not state one. Which section of your own manifest should have contained it: ______________

☐  Is `0.60` reachable at all? Explain why four probabilities can sum past 1 and what that tells you about adding them: ______________

**P2 — the impacts.** T2 and T3 both land on the file server. T2 costs 45,000; T3 costs 12,000.

☐  Which of the two is the *asset* and which is the *event*: ______________

☐  If ransomware destroys the server, is the misconfiguration's 12,000 an additional loss or a description of the same loss: ______________

☐  Write the correct expected loss for the file server as a single expression, using `P` and `A` for the file-server probability and its value: ______________

☐  This is the L20 bug, in someone else's report, produced by someone else's code. Say in one sentence how you would describe the error to them without condescension: ______________

**P3 — the confidence statement.** "Sector benchmark data rather than the firm's own incident history, which comprises a single incident in three years."

☐  Is 1 in 3 years evidence *against* the model's 0.15: ______________

☐  A single observation has an enormous error bar. Roughly what fraction of plausible annual rates does one incident in three years leave open: ______________

☐  So does the report's own history support or undermine the benchmark — and is the answer "it depends on how the observation is treated": ______________

**P4 — the recommendation.**

☐  The report gives an expected loss and recommends spending. What quantity would actually decide the question, and does the report contain it: ______________

☐  What is missing that no arithmetic in the report could supply: ______________

## 3: Write the response — 15 min

The consultant who wrote this report is competent and is not your enemy. Write to them.

☐  250 words maximum. Every word costs you.

☐  Open by naming the one thing the report got right. This is not a courtesy; it is what makes the rest credible.

☐  Name the errors, in order of consequence, with the corrected figure where you have one

☐  Do **not** claim the report's recommendation is wrong. Claim that the document does not support it. You do not have the information to overrule them, and saying otherwise is the fastest way to lose an argument you are right about.

☐  End with the one change that would most improve the model

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

☐  Word count: ______________

☐  Did you lead with what they got right, or did you open with the first error? Which would you have preferred to receive, and does that match what you wrote: ______________

## 4: The meta-question — 5 min

☐  This report has a table, a total, a confidence statement, a citation to a methodology, and a recommendation. What is the probability that a reader in a hurry accepts it without the critique you just wrote — and what does that tell you about why polished documents are more dangerous than rough ones: ______________

☐  Your own README has a similar structure. Name the one section of your own document where the same class of error would be hardest for a reader to catch: ______________

☐  In one sentence: what is the cheapest defence against a wrong report that looks right: ______________

## TURN IN — Critique

1. Part 1, all four questions
2. Part 2, all four problems, symptom and cause separated
3. The 250-word response
4. The Part 4 answer
5. A note on which of your own model's numbers you now trust least: ______________
