# U5 L15 — Designing the Simulation: What Are You Actually Sampling?

Names: ___________________________  Date: Mar 9

Closed notes. 50 minutes. No laptop. The spec you write today is the artefact Friday's engine is graded against. A simulation run against a two-outcome model gives you back the two numbers you typed in.

## 1: Four questions before any code — The laptop-loss problem

You modelled "the drive fails at some point in the year." Before you sample, answer all four.

1. What is the **population**? Not "the laptop." A set of possible years, each a yes-or-no about this drive, this year. Yours: ______________
2. What is the **sample**? ______________
3. What is the **sampling procedure**? One year = one coin weighted 3/20. Does one year of a coin look like one year of your drive? Name one thing the coin gets wrong: ______________
4. What is the **exact question** the simulation answers, with a unit? ______________

☐  Rewrite question 4 so its answer is a number: ______________

☐  Now the honest version: what does the simulation answer that is weaker than the question you actually have: ______________

## 2: What makes it worth sampling — Exact, simulation, or both

| question                                 | exact?     | sim?       | both?      | why        |
| ---------------------------------------- | ---------- | ---------- | ---------- | ---------- |
| A coin weighted 3/20 fires once a year. Over 5 years, chance of at least one? | ______     | ______     | ______     | ______     |
| Four threats, independent, each with its own likelihood. Chance none fire? | ______     | ______     | ______     | ______     |
| Two threats hit the *same* server. Chance the server is down at least once? | ______     | ______     | ______     | ______     |
| The impact of a breach depends on how many records leaked, which depends on a chain of attacker choices. | ______     | ______     | ______     | ______     |
| 5-year expected total loss across four threats, counting only the worst outcome per year. | ______     | ______     | ______     | ______     |

☐  Two of these should be "both," and the reason is the same in both: ______________

☐  Rows 3 and 5 are the ones your project needs. What extra information does the model require before either can be answered at all: ______________

☐  Row 3: what is the "down at least once" event, in set language: ______________

## 3: What simulation cannot do — Three limits

**Limit 1: the sample is not the population.**

☐  What can you claim from 10,000 samples: ______________

☐  What can you not claim: ______________

☐  A result of "0.151" from 10,000 samples. Is the true value 0.151, and what is it approximately: ______________

**Limit 2: the model is the assumption, not the result.**

☐  Run the engine 1,000,000 times and your likelihood is still 3/20. Does more sampling make the assumption more true: ______________

☐  So where does the uncertainty in your answer actually live, in the sampling or in the inputs: ______________

☐  The sentence that makes this safe to publish: ______________

**Limit 3: the seed.**

☐  You report one number from one seed and it happens to be high. Is that a finding or noise, and how would you tell: ______________

☐  Your simulation produces 0.31 and the closed form says 0.30. Is that within noise, and how do you check without guessing: ______________

☐  Why must a seed be a parameter you can pass in rather than a constant buried in the file: ______________

## 4: Write the spec — The artefact Friday implements

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

☐  The spec, filled in in full: ______________

☐  Your two `KNOWN LIMITS` sentences:
   1. ________________________________________________________________
   2. ________________________________________________________________

☐  Read the `OUTPUT` line. Does it name a number or a question: ______________

**TURN IN** — The completed spec sheet, the Part 2 table with the "why" column filled, your two `KNOWN LIMITS` sentences, and one paragraph on why a simulation of a two-outcome model is mostly a way of checking your own arithmetic and what would make yours a real simulation: ______________
