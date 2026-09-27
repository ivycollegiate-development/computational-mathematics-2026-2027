# U5 L23 — Final Rehearsal, Then the Build

Names: ___________________________  Date: Mar 19

Closed notes for the first 25 minutes. Then laptops open. Keep the paper; you will be looking at it again.

## Part 1: The test, in the shape it will arrive — 25 minutes

**A. Sets (three items, no working shown needed on A1).**

A1. Set-builder notation for the integers strictly between 0 and 10 inclusive. ______________

A2. `A = {1,3,5,7}`, `B = {3,4,5,6}`. Give `A u B`, `A n B`, `A − B`, `A △ B`. ______________

A3. Why is `A − B` not the same as `A n B'`, when `B'` is taken inside the universe: ______________

**B. Probability.**

B1. A club has 48 members, 30 in band, 24 in choir, and exactly one member is in both and in neither club. How many are in exactly one club? ______________

B2. A detector has a 4% false-positive rate. A flagged item is malicious with probability 1 in 250. Set up Bayes' theorem and give the answer. ______________

B3. State the difference between `P(malicious | allowed)` and `P(allowed | malicious)` in one sentence each. ______________

**C. Expected value and variance.**

C1. A threat with `P = 1/300` per year costs 90,000 to recover. EV = ______________  What does that number not say: ______________

C2. Outcomes `(1/2, 4,000)`, `(1/2, −2,000)`. EV = ______________  variance = ______________  standard deviation = ______________

C3. Outcomes `(1/5, 5,000)`, `(4/5, 0)`. EV = ______________  variance = ______________  Does your EV agree with the number a reader would expect from these two outcomes? Reconcile any discrepancy: ______________

**D. Modelling judgment. This one is half the paper.**

D1. Your model gives `p = 0.55` for "some loss this year." `P(A or B) = P(A) + P(B) − P(A n B)`, and you substituted `p = 0.30 + 0.35`. What is wrong with the substitution, and which direction does it push the answer: ______________

D2. Your model gives 0.15 for a ransomware threat and 0.20 for a phishing threat, both hitting one file server at different times of year. The naive sum is 0.35. The correct value is lower. Write the exact arithmetic, and state the number the subtraction gives: ______________

D3. True value `p = 0.15`, `q = 0.20`. Write the identity that gives the correction without assuming independence at all, and the value of the correction: ______________

D4. Your report must state one expected loss. Write the one sentence that makes that number unquotable on its own. ______________

D5. Name the assumption your model makes that is hardest to defend, and say what evidence would settle it: ______________

## Part 2: The build — 25 minutes, laptops open

☐  1. Take your simulation spec from L15 and your model from L19. The bug the engine reported on L20 was not arithmetic. Read your `independence_assumed` line and decide whether it is true. ______________

☐  2. Fix the shared-asset overlap using the identity from D3, not by assuming independence. Write the line you changed: ______________

☐  3. Rerun with your usual seed and record the corrected figure: ______________

☐  4. Check it against the closed form. The gap should now be about 0.1%, and it was 0.15% before. What does that tell you: ______________

☐  5. Update the sentence from D4 to describe the fixed model. ______________

**TURN IN** — The paper, both parts, photographed with all work shown. The first part graded. On the second part, graded on whether the identity from D3 appears in the fix and on whether the sentence from D4 changed to match what the model now claims.
