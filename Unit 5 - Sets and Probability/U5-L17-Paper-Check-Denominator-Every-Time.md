# U5 L17 — Paper Check: Can You Write a Number and Its Denominator?

**Date:** Thursday, March 11, 2027
**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.1–5.10 — cumulative retrieval across the unit, with emphasis on
stating the population, the period, and the mean for every number reported

---

**No laptop today.** Calculator allowed. The Unit 5 test is six days away and
this is the last full paper check before it, so today is retrieval across the
whole unit rather than new depth anywhere.

The through-line of the check is one sentence: **a number without its
denominator, its period, and its mean is not a claim.**

## PART 1 — RAPID RETRIEVAL (16 min)

Nine questions, no notes, roughly ninety seconds each. Do not stop to correct
yourself — mark it and move on, and fix the errors in Part 4.

1. Write inclusion–exclusion for three sets. ______
2. A club has 55 in band, 38 in choir, 12 in both. How many in exactly one?
   ______
3. The complement of `A` inside a universe of 100, where `|A| = 34`: ______
4. `P(X|Y) = ?` in words, and what part of it changes: ______
5. A threat with a 5% posterior; the prior was 1%. Did knowing the test result
   move the probability up or down, and why: ______
6. `P(A|B) = P(A)`, for what relationship: ______
7. EV of `[(1/4, 100), (1/2, 0), (1/4, −100)]`: ______
8. Two books, EV both 500, variances 0 and 10,000. Which is riskier and by
   which statistic: ______
9. Sample mean error scales as: ______ The standard error of a mean is: ______

- ☐  All nine
- ☐  Which did you not get in ninety seconds: ______
- ☐  Which did you get *wrong* but quickly: ______

## PART 2 — THE DENOMINATOR, EVERY TIME (16 min)

Ten numbers. For each, write the three qualifiers. This is the graded part.

| # | number | population / denominator | period | a mean over what? |
|---|---|---|---|---|
| 1 | 40% of messages were blocked | | | |
| 2 | P = 0.592 | | | |
| 3 | EV = −6,750 | | | |
| 4 | stdev = 1,484.8 | | | |
| 5 | 9% false-positive rate | | | |
| 6 | 0.15 of years had a loss | | | |
| 7 | n = 10,000 | | | |
| 8 | 0.16 standard errors | | | |
| 9 | 2,401 of 200,000 years hit the worst case | | | |
| 10 | "accuracy 99%" | | | |

- ☐  Fill all ten. Some rows want you to say **"this does not have one"**, and
      those are the interesting ones.
- ☐  Row 10 is a trap. "Accuracy 99%" is missing at least two of the three
      qualifiers. Say which: ______
- ☐  Row 6: is "of years" the right population, or is there a better one that
      your model actually describes: ______
- ☐  Now write the shortest complete sentence that would make row 1 publishable:
      ______

The row 6 checkbox is the one to think about. "0.15 of years" is a
*within-horizon* rate; the model describes a per-threat, per-year probability,
and those are different quantities that a careless reader will treat as
interchangeable. A rate stated in years is already a modelling choice, not an
observation.

## PART 3 — TWO PARAGRAPHS (18 min)

**Paragraph A: the report.** Your simulator reports a probability and an
expected loss. Write the paragraph that goes with them, following the spec you
wrote on L15. It must state what was sampled, what the two headline numbers
mean, and one limit.

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

**Paragraph B: the caveat.** Now write a *second* paragraph, for a reader who
has been quoted a headline number out of your report and wants to know what was
left out. Different audience, different paragraph — the point of this question
is that there is no single paragraph that serves both.

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

- ☐  Both paragraphs
- ☐  Count the numbers in each that are stated **with** their qualifiers:
      Paragraph A: ______ / ______  Paragraph B: ______ / ______
- ☐  Which paragraph is harder to write, and what makes it harder: ______
- ☐  Does either paragraph contain a sentence that would be embarrassing if the
      model turned out to be wrong? ______ (Be honest. This is the one that
      teaches the most.)

## TURN IN — Cumulative Paper Check

1. Parts 1–2 photographed, all work shown
2. Both paragraphs from Part 3
3. Your error log updated, with causes tagged
4. **A revised version of the L13 Part 4 paragraph.** You have now written that
   paragraph three times. The third is the one that gets graded on the exam and
   it should be visibly better than the first — say in one line what you
   changed and why: ______

## 📋 PREVIEW OF FRIDAY

**Next:** L18, Fri Mar 12 — back to the machine, and the biggest build of the
unit so far. You write the Monte Carlo engine: sample years, compare against the
closed form, watch the empirical rate converge on 0.592, and then look at the
distribution of annual loss — which is the first time you see your own model as
a **shape** rather than a number. The build is about 40 lines and every one of
them is on the spec you wrote Monday.

**Bring Friday:** laptop, your simulation spec from L15, and the paragraph. We
start by reading three specs.

## 🇹🇼 TAIWAN CONTEXT

Row 10 is the row worth arguing about with me in a staff meeting. "99% accuracy"
is the single most common figure quoted in security procurement in this country
and in most others, and it is *structurally* incomplete rather than merely
imprecise — the phrase has no population, no period, and no statement of what is
being classified correctly. The ROC national CERT's advisories and the Ministry
of Digital Affairs' guidance both push toward the conditional formulation for
exactly this reason: the vendor's 99% is measured over *their own test set*,
and the number that matters operationally is the rate of true events among
alerts, in *your* environment, over a stated period.

The cost of the shorthand is not abstract. Taiwan's SME sector is where the
mismatch does the most damage, because the buyer is the least able to
reconstruct the population: a clinic choosing an endpoint product on a vendor's
accuracy figure has no way to ask which base rate the accuracy was measured
against, and therefore no way to notice that a well-performing rule can still
send 95% of its alerts to the harmless traffic. The recovery cost lands on an
organization that cannot absorb it, and the security budget is the first thing
cut afterwards.

That is why the ten rows above are the graded part and not the nine questions
in Part 1. Anyone in this room can compute `1/4 + 1/2 - 1/2`. Almost nobody
arrives at a committee having asked what the number was measured *over*. The
question is not a technicality you will be thanked for; it is the job.
