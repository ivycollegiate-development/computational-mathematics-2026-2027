# U5 L13 — Paper Check L11–L12: The Mean Is Not a Risk Description

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.7–5.8 — compute and interpret EV, variance, and standard deviation;
distinguish a mean that is decision-relevant from one that is not

---

**No laptop today.** Calculator allowed. Two of today's five questions have no
arithmetic in them at all, and those are the two I will grade hardest.

## PART 1 — ARITHMETIC, FAST (12 min)

Do these in order without pausing. Speed matters today; the check is partly
whether you can get to an answer you trust quickly.

1. Outcomes `(1/3, 0), (1/3, 90), (1/3, 180)`. EV = ______
2. Outcomes `(1/2, +400), (1/2, −400)`. EV = ______ variance = ______
3. A threat with `P = 1/4` and impact 16,000. EV = ______
4. Four books, each EV = 500, variances: 0, 900, 4,100, 25,000. Rank by
   expected value, then by risk. Write both rankings: ______
5. For a distribution `[(9/10, −200), (1/10, 1,800)]`: `P(loss)` = ______,
   mean outcome when it loses = ______, standard deviation = ______

- ☐  All five, with the multiplication shown
- ☐  Question 4: your two rankings differ for every book except the first. Which
      is the correct one to report, and to whom: ______
- ☐  Question 5: which of your three numbers describes the *typical* year for
      this risk, and which describes the *bad* year? ______

## PART 2 — THE TWO NON-NUMERICAL QUESTIONS (16 min)

**Q6.** Your simulator's `shape_report` returns this:

```
{'ev': 810, 'variance': 2205400, 'stdev': 1484.8, 'p_loss': 0.30,
 'mean_loss_given_loss': -2700, 'best': 0, 'worst': -2700, 'n_outcomes': 2}
```

A decision-maker reads `ev: 810` and declines to spend 400 on a mitigation.

- ☐  Is that decision defensible on the numbers above? ______
- ☐  Which single key would have changed their mind, and why that one: ______
- ☐  Rewrite the report's `ev` key so that nobody can quote it alone. One line
      of code: ______

**Q7.** You have a `variance` of 2,205,400 and an expected value of −810, and
you are asked "how risky is this?". Write the answer a decision-maker should
hear, in three sentences, using the right statistics and saying what is still
missing.

- ☐  Your three sentences: ______
- ☐  What statistic is *absent* from the report that you would need before
      answering confidently: ______
- ☐  The 30% probability of a loss: is that high or low for a risk like this?
      Answer: ______ Why you cannot just say "high" or "low": ______

That last checkbox is the hardest thing in the check. **"High" and "low" are not
properties of a probability; they are properties of a probability and a
reference class.** 30% per year is alarming for a data-centre power failure and
unremarkable for a consumer laptop. If you cannot name the reference class, you
do not yet know whether the number is good or bad — and that is exactly the
condition under which most risk figures get misread.

## PART 3 — TEST-TIME FORM (10 min)

The Unit 5 test is eight days away. This is the shape it will take. Rehearse
the shape now, in the time you would have.

| # | section | what it asks | points |
|---|---|---|---|
| 1–3 | set vocabulary and Venn regions | define, build, count | 12 |
| 4 | inclusion–exclusion, three sets | the full formula | 10 |
| 5–6 | contingency table and conditionals | one direction, then the *other* | 14 |
| 7 | Bayes | setup, and the base-rate comment | 14 |
| 8–9 | expected value, variance, interpretation | the number, then the sentence | 20 |
| 10 | modelling judgment | *why these assumptions* | 30 |

- ☐  The last row is worth half the paper. Confirm you understand that: ______
- ☐  Which of rows 1–9 is your weakest, and what specifically will you practise:
      ______
- ☐  Question 4 is the full three-set formula with all six pairwise terms. Have
      you got it? Write it now, from memory: ______
- ☐  Question 6 will give you the condition in the order that is the *opposite*
      of the natural reading. What will you do to protect yourself: ______

## PART 4 — WHAT I'LL ASK YOU (12 min)

Not a question sheet. One prompt, then you write for eight minutes without
stopping.

> **You have a model. Its numbers are all reasonable. It will be read by someone
> who will act on it. Write the paragraph that goes with it.**

- ☐  It must include: what each likelihood figure means, where at least one of
      them came from, and what the expected value does not tell the reader.
- ☐  It must be readable by someone who does not know what a distribution is.

Write it here:

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

- ☐  Re-read it once. Would you sign your name to it? ______
- ☐  Count the sentences that state a *number* without stating what the number
      is a mean over: ______
- ☐  This paragraph is 60% of this unit's final grade. You have just written a
      draft of it. Revise it once now, in the margins, and keep the revision:
      ______

## TURN IN — Paper Check L11–L12

1. Parts 1–3 photographed, work shown
2. Q6 and Q7 answered in full
3. **The paragraph from Part 4, plus your margin revision.** This is the graded
   artifact and I will read it more carefully than the arithmetic.
4. Your error log updated

## 📋 PREVIEW OF U5 L14

**Next:** L14, Mar 8 — back to the machine, and `riskkit.py` gets real
content for the first time. You will enter a threat model as **data**, with a
likelihood and an impact and, in a string field, the reason you believe that
number. The data structure is the assignment. Everything you compute later will
be as honest as the metadata you attach here.

**Bring U5 L14:** laptop, and the paragraph. I want to see which sentence you
revised.

## 🇹🇼 TAIWAN CONTEXT

Q7's "reference class" is the vocabulary you need for a conversation you will
probably have. Taiwan's national CERT publishes threat advisories with
likelihood figures attached, and those figures are *calibrated against observed
incidents in a stated population and period* — that is what makes them usable.
A vendor's "90% of ransomware campaigns now begin with an exposed remote
desktop port" is a statement about a population, and a defensible one; a
security blog's "ransomware is up 300%" is a statement about a comparison the
reader cannot reconstruct, and it is the kind of number that ends up in a board
deck with no author attached.

The Ministry of Digital Affairs' cybersecurity framework for smaller
organisations asks for exactly this discipline, and the difficulty is not the
mathematics. It is that **a defensible likelihood is boring**: 2% a year,
calibrated, with the exposure counted. It is far less compelling in a briefing
than a figure derived from a headline. Your paragraph is graded on choosing the
boring number and saying where it came from, because that is the entire skill
the role requires and it is not teachable any other way.
