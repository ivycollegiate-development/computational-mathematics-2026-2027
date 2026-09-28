# U5 L29 — The Whole Unit on One Page: What Connects to What

Names: ___________________________  Date: ____

No laptop. This is the consolidation day. Twenty-nine lessons, and if you cannot draw the connections then you have thirty separate techniques rather than one subject. You have four tests' worth of material left and two days.

**The goal is not to review the content. It is to see the shape.**

## 1: The dependency structure — 15 min

Draw this. Do not look at it first; reconstruct it from memory, then compare.

```
              L04 inclusion-exclusion
                       |
   L03 sets -----------+------------ L20 the shared-asset bug
      |                |                        |
      +--> L06 conditional <--- L08 Bayes <------+
                |                              |
                +----------> L10 expected value
                                      |
                              L12 variance
                                      |
                        L14 data --> L16 LLN --> L18 Monte Carlo
```

☐  Draw it from memory. What was missing, and what did you add: ______________

☐  The single most important node is inclusion–exclusion, and it appears three separate times. Name the three: ______________

☐  Everything below L10 is *reporting*, not *calculating*. State that distinction in one sentence: ______________

☐  `L03 sets` has no arrow into `L18`. Is that right, and if so, why does a set-library lesson sit at the start of a probability unit: ______________

That last checkbox is a genuine question and the answer is that the set lessons were not really about sets. They were about **"which of these"** — membership, uniqueness, the discipline of writing down what an object is before computing with it. That is the same skill as writing a threat model as data, and the `v1`/`v3` bug on L20 is what happens when the modelling discipline is skipped.

## 2: The three ideas that carry the most weight — 20 min

Everything in this unit is either arithmetic or judgement. These three are judgement, they are worth more than any formula, and they are what a reader will test you on.

### Idea 1 — Overcounting, in three disguises

☐  Where does it appear, and what is the overstatement in each case: ______________

☐  The three cases are: ______________

☐  Write the one sentence that unifies them: ______________

☐  Which of the three is easiest to *see*, and why did a whole lesson have to be built around the third: ______________

The three: inclusion–exclusion on overlapping sets, adding two probabilities without subtracting the intersection, and charging a shared asset once per threat. All three are the same error and all three err in the same direction — **they overstate.** Every instance in this unit that added something twice made the risk look worse. That is a fact about the direction of the mistake, and it is worth being able to state, because it tells a reader which of your numbers is most likely to be wrong.

### Idea 2 — A correct number is not a finding

☐  Give the four half-sentences that turn a number into a finding. You have met all four: ______________

☐  For each, name the lesson: ______________

☐  The test: here is `expected_annual_loss: 5047.48`. What are the four additions, and which single one is most often omitted: ______________

The four: the period it is a mean over; the population it describes; the assumptions it rests on; and what it does not model. The one most often omitted is the population, because it is the only one that requires the author to have decided something rather than to have computed something — and computation is comfortable while deciding is not.

### Idea 3 — The distinction between the model and the implementation

☐  The `v1` bug: which was wrong, the code or the model: ______________

☐  Explain why the test suite could not catch it: ______________

☐  The simulation agreed with the closed form to 0.15%. What did that verify, and what did it not: ______________

☐  The general form of this lesson, in one sentence: ______________

That last one: **a test verifies that the code implements the model; nothing verifies that the model describes the world.** A chain of implementations can be internally perfect and externally false, and no amount of testing within the chain will say so. The only exit is external evidence — a measured restore time, a sector comparison, an incident history — and that is why L25's "what would I need to check this" is the most valuable sentence in the project.

☐  Name one thing in your own model where you are relying on evidence, and one where you are relying on judgement. Which is load-bearing: ______________

## 3: The unit in one page — 15 min

Write it. This is the sheet you take into the final test, and if you can produce it unaided you have the unit.

**Section 1 — the five formulas.** For each: what it computes, what it needs, and what it silently assumes.

☐  inclusion–exclusion, two sets

☐  inclusion–exclusion, three sets

☐  conditional probability

☐  Bayes

☐  expected value

☐  a sixth if you can justify it: ______________

**Section 2 — the five errors.** For each: the symptom, the cause, the direction of the error.

☐  using a marginal where a conditional was needed

☐  adding probabilities without subtracting

☐  ______________

☐  ______________

☐  ______________

**Section 3 — the three sentences.** One each for Ideas 1, 2, 3 above.

☐  ______________

☐  ______________

☐  ______________

## TURN IN — The One-Page Sheet

1. Part 1, drawn from memory and then corrected
2. Part 2, all three ideas
3. The one-page sheet. This is what you will use tomorrow and on the test, and if you wrote it honestly — marking the parts you are unsure of — it will tell you exactly where to spend tomorrow morning.
