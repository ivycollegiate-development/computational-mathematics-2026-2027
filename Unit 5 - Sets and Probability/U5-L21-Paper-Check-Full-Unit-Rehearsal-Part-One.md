# U5 L21 — Paper Check: Full-Unit Rehearsal, Part One

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.1–5.8 — timed rehearsal of the whole unit under exam conditions

---

**No laptop today.** Calculator allowed. This is a **timed rehearsal of the
Unit 5 test**, split across two days. Today you do the computational half; the
modelling half is U5 L22. Both are graded, and U5 L22 is the one that is
harder to practise.

Time yourself. Twenty-eight minutes of work, twenty-two to review. Do not let
the review eat the work.

## THE PAPER — PART ONE (28 minutes)

### Section A: Sets (20 points)

**A1.** Give the set-builder notation for the even integers. ______

**A2.** Let `U = {1,…,12}`, `A = {2,4,6,8,10,12}`, `B = {3,6,9,12}`. List
`A ∪ B`, `A ∩ B`, `A − B`, `A △ B`, and `U \ (A ∪ B)`. ______

**A3.** How many regions does a two-circle Venn diagram have, and name them. ______

**A4.** Three sets, universe 200. `|A| = 118`, `|B| = 72`, `|C| = 44`,
`|A∩B| = 28`, `|A∩C| = 16`, `|B∩C| = 12`, `|A∩B∩C| = 6`. Find `|A ∪ B ∪ C|`,
write all seven in-set regions, and state how many of the 200 are in none of
them. ______

**A5.** Explain in one sentence why `|A △ B| = |A| + |B| − 2|A ∩ B|`. ______

### Section B: Probability (30 points)

**B1.** A contingency table: rows are *passed / failed*, columns are *studied /
crammed*. Passed-and-studied 140, passed-and-crammed 30, failed-and-studied
50, failed-and-crammed 80. Find `P(passed | studied)`, `P(studied | passed)`,
and state which is larger with a reason. ______

**B2.** Are *passed* and *studied* independent in that table? Show the check
numerically. ______

**B3.** A condition affects 1 in 500. A test is 97% sensitive and has a 3%
false-positive rate. Set up Bayes' theorem for the posterior, then give the
answer as a fraction of 1 and as a percentage. ______

**B4.** A colleague says: "the test is 97% accurate, so a positive result means
97%." State precisely what is wrong with that, in one sentence. ______

### Section C: Expected Value (30 points)

**C1.** Outcomes `(2/5, −500)`, `(3/5, 1,200)`. EV = ______

**C2.** Outcomes `(1/3, 0)`, `(1/3, 6,000)`, `(1/3, 12,000)`. EV = ______
variance = ______ standard deviation = ______

**C3.** Two risks, both EV `−4,000`:

| risk | outcomes |
|---|---|
| R1 | `−4,000` for certain |
| R2 | `−40,000` with p = 1/10, `0` with p = 9/10 |

Variance of R2 = ______. For an organisation that would be closed by a 40,000
loss, which is safer, and what statistic says so: ______

**C4.** Your report will state one expected loss. Write the exact sentence that
makes that number unquotable on its own. ______

## THE REVIEW — 22 MINUTES

- ☐  Mark every answer: correct, right-method-wrong-number, or wrong
- ☐  A4 is the one to check twice. Write out the seven regions, confirm they sum
      to `|A ∪ B ∪ C|`, then confirm `200 − that` is the outside count: ______
- ☐  B1: confirm you used the row total for the first and the column total for
      the second. If you did not, that is the same error you made on L06 and it
      is now a habit: ______
- ☐  B3: check your fraction against the Part 3 of L08. A 1-in-500 prior with a
      3% false-positive rate should give a posterior well under 10%: ______
- ☐  C2: is your standard deviation in dollars? ______
- ☐  C4: does your sentence say what the number is a mean over, or only that it
      is a mean? ______

## TURN IN — Rehearsal, Part One

1. Both pages photographed, **with the time you spent written on them**
2. Your self-marking
3. The A4 eight-region table, verified
4. One paragraph: **which of A–C you would most want back, and what the error
   pattern behind it tells you about how you read** ______

## 📋 PREVIEW OF THURSDAY

**Next:** L22, Thu Mar 18 — **paper again, and the second half of the
rehearsal.** The modelling section: the assumptions, the base rate, and the
defence paragraph. No calculator allowed for the prose sections, because you will
not have one when you are defending a number to someone who is questioning it.

**Bring Thursday:** today's marked paper, and your L20 fix. Friday I will
rehearse the defence itself.

## 🇹🇼 TAIWAN CONTEXT

B4 is the question to take seriously, because it is the one a procurement
committee cannot answer and will therefore accept. When a vendor states a
detection rate in the abstract, the natural reading — and the reading the
vendor's marketing is engineered to produce — is that a positive result means
that probability of compromise. The number is a **likelihood**, not a posterior,
and turning one into the other requires a base rate the vendor has not supplied.
The conditional is not equal to the marginal, and a 97% sensitivity against a
1-in-500 threat population yields a posterior far below 97% — around 6%, by the
same arithmetic as L08.

This is not a quibble about wording. The ROC national CERT's advisories and the
Ministry of Digital Affairs' guidance both treat the substitution of a
sensitivity figure for a predictive value as a recurring and consequential error,
because it is the error that determines whether an organisation deploys a tool,
and the deployment decision is made on the number that was wrong. The recovery
cost of a false sense of coverage falls on the same budget as the false sense
itself, and in a small organisation that budget is the one that gets cut after
the next incident.

So the sentence you write for B4 is not pedantry. It is the sentence that
distinguishes an analyst from a recipient of a brochure, and it is the sentence
your defence paragraph will be built out of on Friday.
