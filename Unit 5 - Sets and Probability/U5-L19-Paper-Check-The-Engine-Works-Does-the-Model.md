# U5 L19 — Paper Check: The Engine Works. Does the Model?

**Date:** Monday, March 15, 2027
**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.9–5.10 — separate implementation correctness from model validity; audit
a Monte Carlo result for assumptions rather than for agreement

---

**No laptop today.** Calculator allowed. Tomorrow you will find a bug in a
program that passes every test, so today is the paper rehearsal: **the engine
running correctly tells you nothing about the model being right.**

That distinction is worth more than any single formula in this unit, and it is
what separates a number you may publish from a number you may only preview.

## PART 1 — THREE QUESTIONS ABOUT A RESULT (14 min)

Your engine reports, for the three-threat model:

- `p_any_closed_form = 0.592`
- `p_any_empirical = 0.591` (100,000 years)
- `ev_closed_form = 10350`
- `ev_empirical = 10402.1`
- `worst_case = 60000`, occurring in 1.2% of years

- ☐  **Q1:** The engine agrees with the closed form to within 0.001. What does
      that establish? ______
- ☐  **Q1 again:** What does it *not* establish? ______
- ☐  **Q2:** Suppose the true likelihoods are each half what you entered. What
      happens to `p_any_closed_form`, roughly, and why: ______
- ☐  **Q3:** The engine would still agree with the closed form in that case. So
      what is the engine actually a test *of*: ______

The Q3 answer, precisely: the engine is a test of the **implementation** — that
the code implements the algebra you intended. The algebra is a test of
**nothing at all**, because it is just a restatement of your own assumptions.
The entire chain can be perfectly self-consistent and completely wrong about
the world, and nothing in the code will ever tell you so.

- ☐  Write that as one sentence suitable for your report: ______

## PART 2 — THE ASSUMPTION AUDIT (16 min)

Every assumption in the model, with its status. Fill in from your own work.

| # | assumption | status | evidence | what breaks if false |
|---|---|---|---|---|
| 1 | T-phish fires with p = 2/5 a year | | | |
| 2 | T-ransom fires with p = 3/20 a year | | | |
| 3 | T-doxs fires with p = 2/10 a year | | | |
| 4 | the three are independent | | | |
| 5 | each costs exactly its stated impact | | | |
| 6 | at most one occurrence per threat per year | | | |
| 7 | impacts do not interact with each other | | | |
| 8 | a year is the right horizon | | | |

- ☐  Fill all eight
- ☐  Which assumption is doing the most work in the final number? ______
- ☐  Which is doing the least, and would you bother to justify it in the
      report: ______
- ☐  **Assumption 5 deserves more than you gave it.** An impact of exactly 45,000
      is a number with no spread at all. Real losses have a distribution, and
      so does the EV. Does that weaken the EV, and by how much — does it double
      it, inflate it, or leave it alone? ______
- ☐  **Assumption 8: is a year the right horizon?** Consider a threat whose
      likelihood is per-year but whose response takes eighteen months. Which of
      your eight rows breaks: ______

The assumption 5 checkbox is the one most students get backwards. A loss
distribution with a mean of 45,000 produces an expected loss of exactly 45,000.
The EV is unchanged. What changes is the **variance and the tail**, so the
figure 45,000 is right as a mean and misleading as a *typical* outcome. That is
the L12 lesson reappearing at the level of the input rather than the output, and
it is worth noticing that the same statistics argument applies one level down.

## PART 3 — WHAT WOULD CHANGE YOUR MIND (10 min)

For each of these, say whether it would change your model, and if so how:

1. A scan shows the misconfigured share is reachable from two internal
   subnets, not one. ______
2. A CERT advisory reports a 90% ransomware rate in your sector, against your
   15% assumption. ______
3. Your org's actual incident history is 1 in 6 years, against your 1 in 20. ______
4. A vendor's tool claims 99% accuracy. ______
5. A peer organisation of the same size and sector reports 1 in 4. ______
6. Nothing new; you simply have more confidence now. ______

- ☐  All six, with your reasoning
- ☐  Which single item would move your model most, and why that one: ______
- ☐  Item 4: does a vendor claim change your likelihood at all? ______ What
      *would* you need before it did: ______
- ☐  Item 6 is the one that catches people. **How do you tell the difference
      between gaining confidence and merely wanting to be right?** ______

That last checkbox is worth real marks. The honest answer involves something
falsifiable: confidence that increased because you ran a check, versus
confidence that increased because the number now agrees with what you hoped. The
second is not confidence, it is motivated reasoning, and in a written defence
the two are indistinguishable unless you say which evidence moved you.

## PART 4 — THE TWO-SENTENCE VERSION (10 min)

Your model will be read by someone who sees one paragraph. Write it.

- ☐  Sentence 1: what the model says, in one sentence with the number and its
      qualifiers.
- ☐  Sentence 2: what the model does not know, in one sentence.

> ________________________________________________________________
> ________________________________________________________________

- ☐  Is sentence 2 something you would be willing to put in a document that
      goes to a lawyer? ______
- ☐  **Now write the sentence you left out on purpose**, the one you think is
      the most important caveat but that no reader has asked for: ______
- ☐  Why did you leave it out? ______

## TURN IN — Paper Check L09–L18

1. Parts 1–3 photographed, all work shown
2. The eight-row assumption audit
3. Your two-sentence version, plus the sentence you left out
4. Your error log updated
5. **A note on tomorrow, before tomorrow:** predict in writing what the bug on
   L20 will be, given that your code has passed every test. Where do you think
   the error will be — in the arithmetic, in the implementation, or in an
   assumption nobody encoded? ______

That last item is not busywork. I collect these before the lesson and I read
them after, and the gap between the predictions and the truth is the clearest
possible picture of what you actually understand about where errors come from.

## 📋 PREVIEW OF TOMORROW

**Next:** L20, Tue Mar 16 — back to the machine, and this is the lesson I have
been building toward since L04. We will take a correct-looking risk aggregator,
give it a full test suite, run it, **watch every test pass**, and then discover
it overstates the risk — because the model it implements is wrong about the
world while the code is right about the model. This is the most important day of
the unit.

**Bring tomorrow:** laptop, and the prediction you just wrote. I want it sealed
before we start.

## 🇹🇼 TAIWAN CONTEXT

The assumption audit in Part 2 is the item an external assessor would do first,
and the pattern in Part 3 is the pattern in the ROC national CERT's own
post-incident reviews: **the models that fail are the ones whose peer
comparison was never performed.** An organisation modelling 1-in-20 for its
sector, when comparable organisations in the same size band report 1-in-4, has
not miscalculated — it has modelled an environment that does not exist.

The national CERT's published methodology and the Ministry of Digital Affairs'
framework both make peer and sector calibration explicit, and both treat a
figure without a stated comparison population as incomplete rather than merely
rough. This is the same requirement as the `likelihood_source` field from L14
and the same requirement as row 10 in the U5 L17 check: **a probability must
name the population it was calibrated against, or a reader cannot tell whether
it is conservative or fantasy.**

Item 3 in Part 3 is the uncomfortable one, and it is the one worth arguing
about. Your own incident history — 1 in 6 years over a small sample — is a
*genuine* observation, and it is also a much weaker basis than a sector figure,
because the sample is small and the observation period is short. The correct
response to both of your inputs is to say what each one is, not to pick the
one you prefer. An organisation that quietly prefers its own favourable number
over an unfavourable sector number has made a decision it cannot defend, and the
reason it cannot be defended is that the comparison was available and was
suppressed.
