# U5 L15 — Designing the Simulation: What Are You Actually Sampling?

**Date:** Tuesday, March 9, 2027
**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (50 minutes)
**LO:** 5.9–5.10 — specify a simulation in writing: population, sample, sampling
procedure, and the exact question the simulation is meant to answer

---

**No laptop today, and the reason is specific.** On Friday you will write a
Monte Carlo engine, and the single most common way it fails is not a bug. It is
answering a question nobody asked, correctly, about the wrong population.

**A simulation is a specification that runs.** Today you write the
specification. The code is downstream of this page.

## PART 1 — FOUR QUESTIONS BEFORE ANY CODE (14 min)

You have a laptop-loss problem: you modelled "drive fails at some point in the
year." Before you sample, answer all four.

1. **What is the population?** Not "the laptop." The population is a *set of
   possible years*, each one being a yes-or-no about this drive, this year. Write
   yours: ______
2. **What is the sample?** ______
3. **What is the sampling procedure?** One year = one coin weighted 3/20. The
   question is: does one year of a coin actually look like one year of your
   drive? Name one thing the coin gets wrong: ______
4. **What is the exact question the simulation answers?** Not "how risky is my
   laptop." A number with a unit. Write it: ______

- ☐  Question 3's answer, named concretely: ______
- ☐  Rewrite question 4 so its answer is a **number**: ______
- ☐  Now the honest version: what does the simulation answer that is *weaker*
      than the question you actually have? ______

That last checkbox is the habit. A simulation run 10,000 times against a
two-outcome model gives you back, to within sampling noise, **the two numbers you
typed in.** It is a way of computing `3/20 × 45,000` while pretending to do
something more interesting. That is not useless — validating an implementation
against a closed-form answer is real work, and it is what the U5 L16 first hour is
for — but it is not simulation of anything real, and you should be able to say
so in one sentence.

## PART 2 — WHAT MAKES IT WORTH SAMPLING (12 min)

The engine earns its keep when the closed-form answer is not available. For each
of these, say whether you would use exact arithmetic, simulation, or both — and
why.

| question | exact? | sim? | both? | why |
|---|---|---|---|---|
| A coin weighted 3/20 fires once a year. Over 5 years, chance of at least one? | | | | |
| Four threats, independent, each with its own likelihood. Chance none fire? | | | | |
| Two threats hit the *same* server. Chance the server is down at least once? | | | | |
| The impact of a breach depends on how many records leaked, which depends on a chain of attacker choices. | | | | |
| 5-year expected total loss across four threats, counting only the worst outcome per year. | | | | |

- ☐  Fill the table. Two of these should be "both" and the reason is the same in
      both: ______
- ☐  Rows 3 and 5 are the ones your project needs. What extra information does
      the model require before either can be answered at all: ______
- ☐  Row 3: what is the "down at least once" event, in set language? ______

That last checkbox connects to the U5 L14 bug. If two threats hit the same
server, the events are **not independent**, and multiplying their likelihoods is
the exact same class of error as adding overlapping counts on L04. You will
build that error on purpose on L20 and it will pass every test you write.

## PART 3 — WHAT SIMULATION CANNOT DO (14 min)

Three limits. For each, say what a simulation result licenses you to claim, and
what it does not.

**Limit 1: the sample is not the population.**
Ten thousand years of coin flips is not ten thousand years of your drive.

- ☐  What can you claim from 10,000 samples? ______
- ☐  What can you *not* claim? ______
- ☐  A result of "0.151" from 10,000 samples. Is the true value 0.151? ______
  What is it, approximately? ______

**Limit 2: the model is the assumption, not the result.**
The simulation faithfully reproduces whatever your parameters say.

- ☐  Run the engine 1,000,000 times and your likelihood is still 3/20. Does
      more sampling make the assumption more true? ______
- ☐  So where does the uncertainty in your answer actually live — in the
      sampling, or in the inputs? ______
- ☐  Write the sentence that makes this safe to publish: ______

**Limit 3: the seed.**
A fixed seed makes results reproducible and a single run is a single draw.

- ☐  If you report one number from one seed and it happens to be high, is that a
      finding or noise? How would you tell: ______
- ☐  Your simulation produces 0.31. The closed form says 0.30. Is that within
      noise, and how do you check without guessing: ______
- ☐  Why should a seed be a *parameter* you can pass in, not a constant
      buried in the file? ______

That last one matters more than it looks. A buried seed is a code smell and
also an audit problem: a reader cannot tell whether you ran once and reported the
number, or ran many times and reported the best one. The latter is not a
simulation result, it is a selection.

## PART 4 — WRITE THE SPEC (10 min)

This is the artifact Friday implements. Write it as if handing it to a
programmer who has never met you and will not ask questions.

```
PURPOSE
  The one question, with units:

POPULATION
  What a single unit of observation is:

SAMPLE
  How many units, and why that many:

INPUTS
  Each parameter, its value, and its provenance:

SAMPLING PROCEDURE
  Exactly what happens to produce one unit:

ASSUMPTIONS
  Independence where assumed, and the consequence if wrong:

OUTPUT
  The exact number to be produced, and its expected precision:

KNOWN LIMITS
  The two sentences you would put under the result in a report:
```

- ☐  Fill it in, in full, on paper
- ☐  The `KNOWN LIMITS` section: your two sentences. These are the sentences
      that go in the report, and they are the ones most models omit:
      1. ________________________________________________________________
      2. ________________________________________________________________
- ☐  Read the `OUTPUT` line. Does it name a number, or a question? ______

## TURN IN — The Simulation Spec

1. The completed spec sheet (Part 4)
2. The Part 2 table with the three-way "why" column filled
3. Your two `KNOWN LIMITS` sentences
4. One paragraph: **why a simulation of a two-outcome model is mostly a way of
   checking your own arithmetic, and what would make yours a real simulation**
   ______

**No laptop today.** The spec is the deliverable; The U5 L16 code will be graded
on whether it does what this page says.

## 📋 PREVIEW OF TOMORROW

**Next:** L16, Wed Mar 10 — back to the machine, and the day the Law of Large
Numbers becomes a thing you have watched happen. You will run the same experiment
at 10, 100, 1,000, 10,000, and 100,000 samples and watch the sample mean
converge — and watch how badly a bad seed misleads you in the first two lines
of output. The specification you wrote today is what you will implement on
Friday.

**Bring tomorrow:** laptop, and the spec. I will go through two of them at the
start of class.

## 🇹🇼 TAIWAN CONTEXT

The `KNOWN LIMITS` sentences are the deliverable a real incident report
actually turns on, and the failure mode here is well documented in the
post-mortems that follow Taiwan's major breaches. Reports that present a
modelled probability as a finding — *there is a 30% chance this configuration
would have been compromised* — without stating the population it was calibrated
against get read as measurements and are later quoted in litigation and in
legislative hearings as though they were. The national CERT's published
post-incident review practice is pointed about this: the review states the
assumptions first, then the numbers, and it is explicit that the assumptions are
the analyst's and the numbers merely inherit them.

The second limit, *more sampling does not make the assumption truer*, is the one
that matters for an institution with a small sample of its own incidents. An
organization with four incidents in three years cannot calibrate a likelihood
figure to three decimal places, no matter how much simulation it runs on top of
those four points. The honest position — and the one the ROC's guidance takes —
is to publish the figure as **calibrated against a named external population**,
to state that it is a proxy, and to say what would improve it. That is not a
weakness in the write-up. It is the write-up.
