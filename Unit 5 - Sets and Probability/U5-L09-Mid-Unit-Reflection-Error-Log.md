# U5 L09 — Mid-Unit Reflection: Reading Your Own Error Log

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (reflection, 50 minutes)
**LO:** 5.1–5.6 — diagnose your own error patterns and name which of them will
cost you points on the Unit 5 test

---

## TODAY'S PURPOSE

You are eight lessons into the unit with a test in ten days. Today is not new
content. Today is the day you look at the last eight days' work with the
specific question: **which of my mistakes is a symptom, and which of them is
the symptom of something?**

A sign error that happened once is noise. A sign error that happened four times
is a fact about how you read, and the difference between those two is the whole
difference between fixing a habit and noticing a habit.

## PART 1 — THE LOG, IN FULL (12 min)

Lay out every entry from L03, L05, and L08 on one page. Then sort them.

| cause tag | entries | the earliest one | the most recent one |
|---|---|---|---|
| vocabulary | | | |
| double-count | | | |
| region | | | |
| formula | | | |
| careful | | | |

- ☐  Total entries: ______  Days covered: ______
- ☐  Most common tag: ______
- ☐  Which tag did you *stop* making? ______ When: ______
- ☐  Which tag is still live? ______

- ☐  Pick the single entry you would most want back. Not the one that cost the
      most points — the one whose *cause* was not what you wrote at the time.
      Write it here and write the better diagnosis underneath:
      ______

## PART 2 — SYMPTOM VERSUS HABIT (14 min)

The distinction: a **symptom** is a specific mistake. A **habit** is the reading
practice that produces it repeatedly. Treatment looks different for each.

| error you made | what you wrote as the cause | what it actually was |
|---|---|---|
| added `A` and `B` without subtracting the overlap | | |
| used the column total where the row total belonged | | |
| wrote `P(allowed \| malicious)` meaning the reverse | | |
| got 3/400 as the "both" probability and used it as a union | | |
| predicted Python would return a list and it returned a set | | |
| dropped the `+ abc` term in a three-set region | | |

- ☐  Fill the right-hand column. At least three of these should turn out to be
      the same underlying habit wearing different clothes. Which ones, and what
      is the habit: ______
- ☐  Name the habit in a phrase you will remember on March 19. ______
- ☐  Which of your logged errors is *not* on this list — something only you
      made? ______

## PART 3 — THE THREE QUESTIONS THE TEST WILL ASK (14 min)

You now know what is coming. Write your answers in full sentences, closed notes,
in the time you would have in the test.

**Q1.** A club has 40 members. 25 are in the band, 18 are in the choir, and 12
are in both. How many are in at least one club? Show the set expression and the
arithmetic.

**Q2.** A threat is stated to have a 3% chance of occurring in a year. If it
occurs, the loss is 50,000. What is the expected loss, and — the part that
matters — what does that number **not** tell you?

**Q3.** A detection rule has a 2% false-positive rate. A given alert is
malicious with probability 1 in 400. Roughly what fraction of alerts are
malicious? Set up the arithmetic; you may leave it as a fraction.

- ☐  Answer each in full.
- ☐  Q1 is a formula recall. How confident are you, 1–5? ______
- ☐  Q2 has a second half that is about honesty rather than arithmetic. How
      confident are you that you will write it? ______
- ☐  Q3 is a Bayes setup. Did you reach for the right denominator without
      hesitating? ______

- ☐  **Now score yourself honestly** using the audit you ran on L03: for each
      question, did you get the *value* right, the *form* right, both, or
      neither?

| Q | value right? | form right? | both? |
|---|---|---|---|
| Q1 | | | |
| Q2 | | | |
| Q3 | | | |

## PART 4 — WHAT YOU ARE NOT SURE ABOUT (10 min)

This is the part I read most carefully.

- ☐  List three things from L01–L08 that you do not yet understand well enough to
      use without looking them up:

  1. ______
  2. ______
  3. ______

- ☐  For each: is it a **concept** you do not get, a **notation** you are fuzzy
      on, or a **case** you have not seen? Label them.

  | # | concept / notation / case | what would settle it |
  |---|---|---|
  | 1 | | |
  | 2 | | |
  | 3 | | |

- ☐  Which of the three can be settled by five minutes with the textbook, and
      which needs a conversation with me? ______
- ☐  Write down the actual question for the ones that need me. Not "I don't get
      Bayes." The real question: ______

## TURN IN — Mid-Unit Reflection

1. One page: the sorted error log (Part 1)
2. The symptom-versus-habit table (Part 2), including the one only you made
3. Your three test questions answered, plus the honest self-score table
4. Your three uncertainties, labelled concept / notation / case, with a real
   question written for the ones that need me

**This is graded on honesty, not on being right.** A reflection that says "I am
confident about everything" is either a student who will discover something on
March 19, or a reflection that was not written honestly. Both score zero here.

## 📋 PREVIEW OF TOMORROW

**Next:** L10, Tue Mar 2 — back to the machine, and the topic you have been
dodging: **expected value.** The question the whole project is built on, and the
one where a single wrong assumption about a probability becomes a wrong dollar
figure. `riskkit.py` gets started today.

**Bring tomorrow:** laptop, and your Part 4 list. I will go through the "needs a
conversation" ones at the start.

## 🇹🇼 TAIWAN CONTEXT

The habit you identified in Part 2 has a name outside mathematics, and it is
called a **denominator error**: reporting a rate without the population it was
measured against. It is endemic in institutional reporting, because the
institution is being evaluated on the number and not on the population.

Taiwan's national cybersecurity exercises and CERT reporting are a live example
of the discomfort this causes. An agency that reports "we blocked 40,000
malicious attempts this quarter" has produced a count with no denominator at
all, and it means nothing without knowing the traffic volume it was drawn from.
The same agency reporting "0.4% of inbound connections were malicious, and 31%
of the connections our rule flagged were malicious" has produced something a
reader can act on. Both are honest counts. Only one is usable.

That is the sentence to carry into your Risk Simulator defense. Your likelihood
figures are the same kind of claim: a number that is only meaningful next to the
population it was chosen for, which is the environment you are modelling. The
analyst who writes "3% likelihood" without saying *3% of what, in what period,
against what exposure* has done the reporting equivalent of adding overlapping
counts.
