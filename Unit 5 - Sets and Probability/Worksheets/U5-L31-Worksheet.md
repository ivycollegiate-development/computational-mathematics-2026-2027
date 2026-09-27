# U5 L31 — Unit Close: Final Assessment and Demonstration

Names: ___________________________  Date: Mar 31

Calculator allowed. Write your name. Do not write anything on the cover sheet.

## Section A: Sets — 15 points

**A1.** Two sets, universe of 90 students: `P` is the set of students taking physics, 54. `Q` is the set taking chemistry, 36. 18 take both. Find `|P − Q|`, `|P △ Q|`, and the number taking neither. Show the work for the last one. ______________

**A2.** A three-set problem in a universe of 260: `|X| = 150`, `|Y| = 120`, `|Z| = 90`, `|X∩Y| = 60`, `|X∩Z| = 45`, `|Y∩Z| = 30`, `|X∩Y∩Z| = 20`. Find `|(X ∪ Y ∪ Z)ᶜ|`, showing the eight terms. ______________

**A3.** In one sentence each: why `|A ∪ B| ≠ |A| + |B|` in general, and what quantity is missing from the sum. ______________

## Section B: Probability — 20 points

**B1.** A table of 300 email messages:

|                      | blocked            | delivered          | row total          |
| -------------------- | ------------------ | ------------------ | ------------------ |
| phishing             | 12                 | 18                 | ______________     |
| legitimate           | 8                  | 262                | ______________     |
| **column total**     | ______________     | ______________     | ______________     |

Find `P(phishing)`, `P(blocked | phishing)`, and `P(phishing | blocked)`. Then state which of the two conditional probabilities is larger and why the direction of that inequality is the operationally important one. ______________

**B2.** A rare condition, 1 in 900. A test is 95% sensitive, 4% false-positive rate. Set up Bayes' theorem and give the posterior as a fraction and a percentage. ______________

**B3.** One sentence: why is the posterior here so much lower than the sensitivity, and name the phenomenon: ______________

## Section C: Expected value and risk — 25 points

**C1.** Outcomes `(1/2, 4,000)`, `(1/2, −2,000)`. EV = ______________  variance = ______________

**C2.** Two investments, both with EV 800:

|            | outcomes                                 | EV                 | variance           |
| ---------- | ---------------------------------------- | ------------------ | ------------------ |
| I          | `800` for certain                        | ______________     | ______________     |
| II         | `4,000` with p = 1/5, `0` with p = 4/5   | ______________     | ______________     |

For a fund that cannot absorb a 4,000 loss in one year, which do you recommend, and what is the one-sentence argument for the recommendation: ______________

**C3.** Your model reports `expected annual loss 5,047.48` and `p_any_loss 0.5913`. A manager asks whether to fund a 5,000 annual backup. Write the **three-sentence** response, and state which statistic in your report should have decided the question instead. ______________

## Section D: The hard part — 20 points

**D1.** An external report states `P(at least one threat) = 0.20 + 0.15 + 0.20 = 0.55`. Name the error, state the correct method, and say whether the report's number is too high, too low, or possibly too low. ______________

**D2.** Two of those three threats compromise the same 12,000 asset: ransomware at likelihood 0.15 and network misconfiguration at 0.20, assumed independent. The report charges the asset `0.20 × 12,000`. Compute the correct expected loss for that asset, and give the one-line formula for the difference. ______________

**D3.** A fourth factor is found to be associated with both the exposure and the outcome, and the naive effect size is exactly 4.00 while the stratified figure is exactly 2.00. Name the phenomenon, state the direction of the error, and write the one sentence you would use to tell a non-technical reader that the claim is overstated **without** dismissing the underlying recommendation: ______________

## Part 2: The Demonstration — 20 minutes, laptop

I will run your repository. Not you — I will run it, from a clean checkout, on this machine, in front of the class. You will talk me through it.

This is deliberately the hardest possible version of the test. A demonstration where you control the machine is a rehearsal. A demonstration where someone else operates it, on a machine you have never seen, in front of a room, is the only version that reveals whether the artefact actually stands on its own.

**Before we start, confirm:**

☐  The repository runs from a **clean checkout** with one command

☐  You have **deleted every absolute path**

☐  Every output in the README is **live output**

☐  You have **not committed** — you will show me the working tree

**During the demonstration I will ask, and you will answer without opening the code:**

☐  1. What does this model, in one sentence?

☐  2. Whose risk is it about?

☐  3. What is the single number, and what is it a mean over?

☐  4. What does it *not* model?

☐  5. Where did the `3/20` come from?

☐  6. What was the bug on L20, and what test now guards it?

☐  7. **If I set the file-server value to 50,000, does the expected loss double?**

Question 7 is not arbitrary and it is the one I care about most. **It does not double, and the reason is worth more than every other answer combined.** The file server contributes `8/25 × 12,000`, and the staff inboxes contribute separately; doubling the file-server value doubles *its* contribution, which is about 76% of the total, not 100%. And if you answer that correctly without opening the code, you understand the model rather than the program.

☐  After the demonstration, write one paragraph: **what would you change first if you had another week?** ______________

## TURN IN — Unit Close

1. **The assessment**, both pages, in my hand
2. **The repository**, working, uncommitted
3. **`README.md`**
4. **"What this model does not know"**, the one page from L30
5. **The L27 critique** and **the L28 correction** — I am returning these with comments today
6. **Your error log**, complete. Thirty-one days of it.
