# U5 L27 — Someone Else's Model: Find the Error in a Plausible Report

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (50 minutes)
**LO:** 5.4, 5.9 — critique an external risk model; locate the error that
produced a wrong number; write the correction

---

**No laptop.** Calculator allowed. This is the hardest day in the unit and there
is no code on it.

You are handed a model produced by another organisation. It is competent, it is
well-formatted, it has a table and a confidence statement and a
recommendation. It is also **wrong**, and the wrongness is not in the code — it
never was. Your job is to find the assumption, state the correction, and write
the response.

## THE REPORT YOU HAVE BEEN SENT

> **Security Risk Assessment — Ardent Logistics Ltd**
> Prepared for the board. March 2027.
>
> Four threat vectors were identified and modelled. Each was assigned an annual
> likelihood and a financial impact, derived from a sector benchmark study of
> logistics firms of comparable size.
>
> | vector | annual likelihood | impact | expected loss |
> |---|---|---|---|
> | T1 credential phishing | 0.20 | 3,000 | 600 |
> | T2 ransomware on file server | 0.15 | 45,000 | 6,750 |
> | T3 network misconfiguration | 0.20 | 12,000 | 2,400 |
> | T4 credential phishing, second vector | 0.05 | 3,000 | 150 |
>
> **Total expected annual loss: 9,900**
> **Probability of at least one vector firing: 0.20 + 0.15 + 0.20 + 0.05 = 0.60**
> **Confidence: moderate. Figures are drawn from sector benchmark data rather
> than the firm's own incident history, which comprises a single incident in
> three years.**
>
> **Recommendation: proceed with the proposed backup programme.**

## PART 1 — READ IT AS A SKEPTIC, NOT A USER (10 min)

Do not start by judging the recommendation. Start by asking what the document
has actually established.

- ☐  **Q1.** The report says `P(at least one) = 0.60`. Is that a valid
      probability? Compute the exact value by inclusion–exclusion and say whether
      the report's number is an overstatement, an understatement, or a
      coincidence: ______
- ☐  **Q2.** `Total expected annual loss: 9,900`. Check the arithmetic of the
      four rows. Does the column add up: ______
- ☐  **Q3.** The four rows produce two pairs that look like they describe the
      same thing. Identify them: ______
- ☐  **Q4.** The board recommendation is to spend money. **Which of the four
      vectors would have to be true for that recommendation to be right, and
      does the report support it:** ______

Q4 is the question that matters. The recommendation to spend is a decision about
the worst plausible outcome, not about the average, and the report offers one
number. Before you reject the report, note that the recommendation may still be
correct — a model can produce a wrong number and a right answer. Say so
explicitly in Q4, because a critique that only finds errors is not a critique,
it is an objection.

## PART 2 — FIND THE ERROR (20 min)

There are at least four problems. Find as many as you can, and for each one
separate the **symptom** (what looks wrong) from the **cause** (the assumption
that produced it).

**P1 — the probability.** T1 and T4 are described as two vectors but the
likelihoods are `0.20` and `0.05` against the same 3,000 impact.
- ☐  If they are the same threat measured twice, what is the correct treatment:
      ______
- ☐  If they are genuinely distinct vectors, the report still owes the reader an
      independence assumption and does not state one. Which section of your own
      manifest should have contained it: ______
- ☐  Is `0.60` reachable at all? Explain why four probabilities can sum past 1
      and what that tells you about adding them: ______

**P2 — the impacts.** T2 and T3 both land on the file server. T2 costs 45,000;
T3 costs 12,000.
- ☐  Which of the two is the *asset* and which is the *event*: ______
- ☐  If ransomware destroys the server, is the misconfiguration's 12,000 an
      additional loss or a description of the same loss: ______
- ☐  Write the correct expected loss for the file server as a single expression,
      using `P` and `A` for the file-server probability and its value: ______
- ☐  **This is the L20 bug, in someone else's report, produced by someone else's
      code.** Say in one sentence how you would describe the error to them
      without condescension: ______

**P3 — the confidence statement.** "Sector benchmark data rather than the firm's
own incident history, which comprises a single incident in three years."
- ☐  Is 1 in 3 years evidence *against* the model's 0.15? ______
- ☐  A single observation has an enormous error bar. Roughly what fraction of
      plausible annual rates does one incident in three years leave open: ______
- ☐  So does the report's own history support or undermine the benchmark — and
      is the answer "it depends on how the observation is treated": ______

**P4 — the recommendation.**
- ☐  The report gives an expected loss and recommends spending. What quantity
      would actually decide the question, and does the report contain it:
      ______
- ☐  What is missing that no arithmetic in the report could supply: ______

## PART 3 — WRITE THE RESPONSE (15 min)

The consultant who wrote this report is competent and is not your enemy. Write
to them.

**Constraints:**
- ☐  **250 words maximum.** Every word costs you.
- ☐  Open by naming the one thing the report got right. This is not a courtesy;
  it is what makes the rest credible.
- ☐  Name the errors, in order of consequence, with the corrected figure where
    you have one
- ☐  Do **not** claim the report's recommendation is wrong. Claim that the
    document does not support it. You do not have the information to overrule
    them, and saying otherwise is the fastest way to lose an argument you are
    right about.
- ☐  End with the one change that would most improve the model

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

- ☐  Word count: ______
- ☐  Did you lead with what they got right, or did you open with the first
      error? Which would you have preferred to receive, and does that match what
      you wrote: ______

## PART 4 — THE META-QUESTION (5 min)

- ☐  This report has a table, a total, a confidence statement, a citation to a
      methodology, and a recommendation. What is the probability that a reader
      in a hurry accepts it without the critique you just wrote — and what does
      that tell you about why polished documents are more dangerous than rough
      ones: ______
- ☐  Your own README has a similar structure. **Name the one section of your own
      document where the same class of error would be hardest for a reader to
      catch:** ______
- ☐  In one sentence: what is the cheapest defence against a wrong report that
      looks right: ______

## TURN IN — Critique

1. Part 1, all four questions
2. Part 2, all four problems, symptom and cause separated
3. **The 250-word response**
4. The Part 4 answer
5. A note on which of your own model's numbers you now trust least: ______

## 📋 PREVIEW OF FRIDAY

**Next:** L28, Fri Mar 26 — **paper, and the hardest arithmetic in the unit.**
Conditional probability under confounding, in the form you will actually meet
it: an exposure that causes an outcome *and* is associated with a second factor
that causes the same outcome. The result is that the naive association
overstates the effect, sometimes by a lot, and the arithmetic for quantifying
how much is two lines.

**Bring Friday:** calculator, and the L06 contingency table fresh in your mind —
we are going to need both margins and a third layer.

## 🇹🇼 TAIWAN CONTEXT

The Ardent Logistics report is a genre that exists in quantity here, and the
reason is institutional rather than cultural: sector benchmark figures are
easier to obtain than internal measurement, and a report that cites a benchmark
audits more smoothly than one that says "we do not know and here is what we
would need to find out." The confidence statement is the tell. Note what it
actually concedes — the figure is not calibrated to this firm — while appearing
to strengthen the report by acknowledging a limitation.

The ROC national CERT's advisory guidance on small and medium organisations is
direct on this point, and the pattern it describes matches the report precisely:
**sector averages imported as firm-specific figures, and a stated confidence
level that reflects the writer's appetite for the document rather than the
quality of the evidence.** The national CERT's own practice is to treat an
uncalibrated figure as a placeholder requiring a measurement plan, not as an
input to a funding decision. Where a decision has real money behind it, the
guidance requires the figure be recalibrated against the organisation's own
exposure — which for a firm of Ardent's size is a day's work, and is the single
highest-value action available.

P3 is the sharpest version of this. **One incident in three years is not weak
evidence in a firm with three years of history — it is the only evidence there
is**, and the fact that the report prefers a sector benchmark to it is a choice
that was made silently. The report's own sentence contains the evidence that
would have improved the model, and sets it aside because it is inconvenient and
hard to calibrate. That is the failure the manifest's `CALIBRATION` block is
designed to make visible: not to make a number correct, but to make the
decision about where the number came from an explicit one.
