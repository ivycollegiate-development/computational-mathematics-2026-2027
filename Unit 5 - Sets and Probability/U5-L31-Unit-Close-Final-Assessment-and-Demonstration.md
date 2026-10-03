# U5 L31 — Unit Close: Final Assessment and Demonstration

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (final assessment, 50 minutes)
**LO:** 5.1–5.10 — final assessment; demonstrate the artefact to a reader who
has not seen it

---

**Paper for the assessment. Laptop afterwards, for the demonstration.**

This is the last session of the unit. The assessment is worth the most of
anything you will hand in, and the demonstration is the part where you find out
whether the project actually works when someone else is holding it.

## PART 1 — FINAL ASSESSMENT (30 minutes, closed book)

Calculator allowed. Write your name. Do not write anything on the cover sheet.

### SECTION A — SETS (15 points)

**A1.** Two sets, universe of 90 students: `P` is the set of students taking
physics, 54. `Q` is the set taking chemistry, 36. 18 take both. Find `|P − Q|`,
`|P △ Q|`, and the number taking neither. Show the work for the last one. ______

**A2.** A three-set problem in a universe of 260: `|X| = 150`, `|Y| = 120`,
`|Z| = 90`, `|X∩Y| = 60`, `|X∩Z| = 45`, `|Y∩Z| = 30`, `|X∩Y∩Z| = 20`. Find
`|(X ∪ Y ∪ Z)ᶜ|`, showing the eight terms. ______

**A3.** In one sentence each: why `|A ∪ B| ≠ |A| + |B|` in general, and what
quantity is missing from the sum. ______

### SECTION B — PROBABILITY (20 points)

**B1.** A table of 300 email messages:

| | blocked | delivered |
|---|---|---|
| phishing | 12 | 18 |
| legitimate | 8 | 252 |

Find `P(phishing)`, `P(blocked | phishing)`, and `P(phishing | blocked)`. **Then
state which of the two conditional probabilities is larger and why the
direction of that inequality is the operationally important one.** ______

**B2.** A rare condition, 1 in 900. A test is 95% sensitive, 4% false-positive
rate. Set up Bayes' theorem and give the posterior as a fraction and a
percentage. ______

**B3.** One sentence: why is the posterior here so much lower than the
sensitivity, and name the phenomenon: ______

### SECTION C — EXPECTED VALUE AND RISK (25 points)

**C1.** Outcomes `(1/2, 4,000)`, `(1/2, −2,000)`. EV = ______ variance = ______

**C2.** Two investments, both with EV 800:

| | outcomes |
|---|---|
| I | `800` for certain |
| II | `5,000` with p = 1/5, `0` with p = 4/5 |

Variance of II = ______. **For a fund that cannot absorb a 5,000 loss in one
year, which do you recommend, and what is the one-sentence argument for the
recommendation:** ______

**C3.** Your model reports `expected annual loss 5,047.48` and
`p_any_loss 0.5913`. A manager asks whether to fund a 5,000 annual backup. Write
the **three-sentence** response, and state which statistic in your report should
have decided the question instead. ______

### SECTION D — THE HARD PART (20 points)

**D1.** An external report states `P(at least one threat) = 0.20 + 0.15 + 0.20 =
0.55`. Name the error, state the correct method, and say whether the report's
number is too high, too low, or possibly too low. ______

**D2.** Two of those three threats compromise the same 12,000 asset. The report's
total expected loss is 10,350. Compute the correct expected loss for that
asset, and give the one-line formula for the difference. ______

**D3.** A fourth factor is found to be associated with both the exposure and the
outcome, and the naive effect size is exactly 4.00 while the stratified figure
is exactly 2.00. Name the phenomenon, state the direction of the error, and
write the one sentence you would use to tell a non-technical reader that the
claim is overstated **without** dismissing the underlying recommendation:
______

## PART 2 — THE DEMONSTRATION (20 minutes, laptop)

I will run your repository. Not you — I will run it, from a clean checkout, on
this machine, in front of the class. You will talk me through it.

This is deliberately the hardest possible version of the test. A demonstration
where you control the machine is a rehearsal. A demonstration where someone else
operates it, on a machine you have never seen, in front of a room, is the only
version that reveals whether the artefact actually stands on its own.

**Before we start, confirm:**

- ☐  The repository runs from a **clean checkout** with one command
- ☐  You have **deleted every absolute path**
- ☐  Every output in the README is **live output**
- ☐  You have **not committed** — you will show me the working tree

**During the demonstration I will ask, and you will answer without opening the
code:**

1. ☐  What does this model, in one sentence?
2. ☐  Whose risk is it about?
3. ☐  What is the single number, and what is it a mean over?
4. ☐  What does it *not* model?
5. ☐  Where did the `3/20` come from?
6. ☐  What was the bug on L20, and what test now guards it?
7. ☐  **If I set the file-server value to 50,000, does the expected loss double?**

Question 7 is not arbitrary and it is the one I care about most. **It does not
double, and the reason is worth more than every other answer combined.** The
file server contributes `8/25 × 12,000`, and the staff inboxes contribute
separately; doubling the file-server value doubles *its* contribution, which is
about 76% of the total, not 100%. And if you answer that correctly without
opening the code, you understand the model rather than the program.

- ☐  After the demonstration, write one paragraph: **what would you change first
      if you had another week?** ______

## TURN IN — Unit Close

1. **The assessment**, both pages, in my hand
2. **The repository**, working, uncommitted
3. **`README.md`**
4. **"What this model does not know"**, the one page from L30
5. **The L27 critique** and **the L28 correction** — I am returning these with
   comments today
6. **Your error log**, complete. Thirty-one days of it.

## WHAT THE UNIT WAS

Thirty-one days, four ideas, and the ideas are not the ones the title suggests.

**Sets** taught you to write down what an object is before computing with it,
and the price of skipping that discipline was the L20 bug: a function whose
signature could not represent the fact that mattered, which produced a number
that was wrong and passed every test.

**Probability** taught you that the conditional and the marginal are different
quantities, that the direction of a Bayes result is set by the base rate and not
by the accuracy of the test, and that a stratified effect size is a different
claim from an unstratified one.

**Expected value** taught you that a mean is a summary of many years and that
organisations are destroyed in one, so the mean describes the model and not the
risk.

**And the whole thing** turned on one distinction you did not have on L03: a
test verifies that the code implements the model, and nothing verifies that the
model describes the world. `v1` was a perfect implementation of a wrong claim,
`p_worst_case` was a correct number about a world that does not exist, and the
only exit from that chain is evidence from outside it.

That is the transferable skill, and it is not a computational mathematics one.
It is the thing that separates an analyst from a recipient of a number.

## 🇹🇼 TAIWAN CONTEXT

This unit has been about a specific habit, and it is a habit this environment
rewards more than most.

The pattern here is institutional. Risk figures arrive from sector benchmarks
because they are available, from vendors because they are attached to a purchase,
and from a firm's own history when neither of those has been obtained. Each
carries a different provenance, and **the number is almost always presented the
same way** — a single figure, unqualified, in a table. The provenance is the
thing that distinguishes an estimate from a guess, and it is the thing that
disappears in transmission.

The ROC national CERT's advisory guidance and the Ministry of Digital Affairs'
framework both address this the same way, and the requirement is unglamorous:
name the population the figure was calibrated against, state the period it is a
mean over, and distinguish what was assessed from what was not in scope. A
figure without those three is not wrong. It is **unreadable**, and an unreadable
figure in a decision gets acted on anyway.

So the closing thought for the unit is the one the manifest was built for. Your
`expected_annual_loss` of 5,047.48 is a competent number, produced by a
simulation that agrees with its own closed form to within a fifth of a percent,
with a test suite that catches the bug that once inflated it. It is also, on its
own, a number about nothing — about a model, for a population, under five
assumptions, from a seed, over a year, in a currency.

What you can do with it, and what you have learned to do with every other number
you will meet in this field, is the thing the national CERT's own reviewers do
and what this unit has been teaching for thirty-one days: **say where it came
from, say what it is not, and say what would change it.** The number is the easy
part. The sentence around it is the work, and the sentence is what the reader
actually receives.
