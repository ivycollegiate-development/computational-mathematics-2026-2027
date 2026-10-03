# U5 L22 — Paper Check: Full-Unit Rehearsal, Part Two

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.9–5.10 — timed rehearsal of the modelling and defence sections of the
Unit 5 test

---

**No laptop today. No calculator for Sections D and E.** That restriction is
the point. When you defend a number to someone who is questioning it, you will
not have a calculator and you will not have your notes, and what you say in the
first thirty seconds determines whether anyone asks a second question.

Sections A–C were yesterday. Today is the half of the paper that is worth more
points and that almost nobody practises.

## THE PAPER — PART TWO (30 minutes)

### Section D: The Model (40 points)

Your simulator, in its current state, has three threats, two assets, and a
`shape_report` that returns `ev`, `p_any_loss`, `mean_loss_given_loss`,
`worst_case`, `p_worst_case`, `n_years`, `seed`, and
`independence_assumed`.

**D1.** The report's `ev` reads 5,047.48. Write the **one sentence** that
accompanies that number in a report, stating what it is a mean over and what it
is not. ______

**D2.** List every assumption your model makes. A correct answer has at least
six. ______

**D3.** Your `T-ransom` likelihood is `3/20`, sourced to "analyst judgement: RDP
exposed on 6 of 9 hosts." A reader asks: *why not `1/5`?* Write your answer in
two sentences, honestly, without inventing evidence you do not have. ______

**D4.** The report says `independence_assumed: within-asset threats independent`.
Your two file-server threats — ransomware and the misconfigured share — both
require the same reachable share point. Is the independence claim true? ______

**D5.** The simulation ran 200,000 years and the empirical EV was 5,047.48
against a closed form of 5,040. What does the 0.15% gap establish, and what
does it not establish? ______

### Section E: The Defence (30 points)

**E1.** Your number is `p_any_loss = 0.59`. A reader says: "59% of years have
some loss — that is a terrible number." Write the response that is accurate
rather than merely reassuring. ______

**E2.** The same reader says: "then we should spend 6,000 a year to eliminate
it." Why is that a bad inference, and what is the correct first question to
answer instead? ______

**E3.** Write the **two sentences** you would put at the foot of the report,
naming the single most important limitation and what would improve it. ______

**E4.** A reader says: "you assumed 1 in 6. Our own history says 1 in 6. So your
model adds nothing." What is the strongest counter-argument? ______

## THE REVIEW — 20 MINUTES

- ☐  D1: does your sentence say what the number is a mean **over**, or only that
      it is a mean? The first is a specification, the second is a disclaimer:
      ______
- ☐  D2: count your assumptions. Six or fewer means you have stopped at the
      parameters and not reached the structure: ______
- ☐  D3: reread your answer. Did you invent evidence? Inventing a source to
      survive a challenge is the failure this section is testing: ______
- ☐  D4: this one has a right answer, and it is uncomfortable. The claim is
      false, the `independence_assumed` string is where the falsehood lives, and
      the correct response is to say so: ______
- ☐  E1: did you reassure, or did you inform? Both are acceptable; only one is
      honest: ______
- ☐  E4: the best counter-argument is not "my model is better." It is about
      what a five-year history can and cannot distinguish. Did you find it:
      ______

## TURN IN — Rehearsal, Part Two

1. Both pages photographed, work shown, **times written**
2. Your self-marking
3. **D3, rewritten.** If you invented evidence in your first attempt, keep the
   first attempt and write the honest version underneath. The gap is the lesson
   and I grade the revision.

## 📋 PREVIEW OF FRIDAY

**Next:** L23, Fri Mar 19 — **paper, one more time, and then we build.** The
final rehearsal is a single scenario end to end, and then we spend the last
hour of the week assembling `riskkit.py` into the artefact it is meant to be.
Bring everything you have written in the last three days.

**Bring Friday:** both rehearsal papers, your error log, and `riskkit.py`.
