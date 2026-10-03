# U7 L04 — Paper Check: L01–L03

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.1, 7.2 — locate the minimum of an error curve, and explain it

---

**No laptop.** Pencil. The U7 L03 table is the raw material, and there is
exactly one thing in this unit I want you to be able to do without a computer.

## PART 1 — RECALL THE TABLE (12 min)

From memory, then check against your own notes.

1. Forward difference at `h = 1e-3` for `x²` at 2: ______
2. True derivative there: ______
3. The `h` that minimised the forward error on Wednesday: ______
4. The error at that `h`: ______
5. Central difference at `h = 1e-4`, error: ______
6. Between `h = 1e-9`, `1e-10`, and `1e-11`, the forward answer was ______
7. Name the two error sources: ______
8. Which one grows as `h` grows, and which grows as `h` shrinks? ______

- ☐  How many of the eight without notes? ______ / 8
- ☐  Question 6 is the interesting one. Why was the answer **identical** for
     those three values of `h`? ______

## PART 2 — DRAW THE ERROR CURVE (15 min)

This is the deliverable of the unit so far. On the axes below, sketch
`|error|` against `h` on a **log scale for both**. Mark:

- ☐  The `h = 1e-1` end, error `0.1`
- ☐  The `h = 1e-8` minimum, error `2.43e-8`
- ☐  The `h = 1e-12` end, error `3.56e-4`
- ☐  The label **truncation error** on the descending arm
- ☐  The label **round-off error** on the ascending arm
- ☐  The two arms as **straight lines** — justify that: ______
- ☐  The `h = 1e-9` to `1e-11` **flat shelf** you observed, drawn as a flat
     section across the bottom

Now the two questions the drawing is for:

1. At `h = 1e-3` the error is `1e-3`, about ten thousand times worse than the
   minimum. **Which error source dominates there?** ______
2. At `h = 1e-11` the error is `3.31e-7`, also far above the minimum. **Which
   dominates there?** ______

- ☐  The general rule, in one sentence: to make the estimate better, you
     ______ the `h` until ______, and then you must ______ instead. ______

## PART 3 — THE ADEQUACY QUESTION (10 min)

The U7 L03 Part 4 asked whether these errors would matter for a real alarm.
Answer it now, for both.

3. An alarm triggers when a rate of change exceeds **1%**. Forward difference
   at `h = 1e-3` on the `x²` data has error `1e-3` absolute on a value of 4 —
   that is `0.025%` relative. Adequate? ______
4. An alarm triggers on a change of **0.00001**. Forward difference at
   `h = 1e-5` on the `exp` data is off by `1.36e-05`. Adequate? ______
5. Now the question that matters. In case 4, **which `h` would you actually
   choose**, and would it be the one with the smallest error? ______

- ☐  My answer to 5: ______
- ☐  State the general principle in one sentence, in your own words: ______

The principle is: *the best numerical method is the one whose error is small
relative to the decision you are making.* The minimum-error `h` is an
engineering choice, not a mathematical fact, and it is made by comparing
against a threshold that comes from somewhere else entirely.

## PART 4 — ERROR LOG (8 min)

Start a new log if you have not already: **Calculus Error Log**, sections per
unit.

- ☐  Every error from Parts 1 and 2 goes in
- ☐  New tags for this unit: **step size**, **error order**, **log scale**,
     **sign of derivative**
- ☐  Most common tag so far today: ______
- ☐  Which of your Part 1 misses would have been caught by a unit of **paper**
     rather than by running the code? ______

## PART 5 — PREDICT TUESDAY (bonus, 5 min)

Next lesson is numerical integration. Predict, with no more than two sentences
of reasoning each:

6. If you double the number of rectangles in a left-endpoint sum, by roughly
   what factor does the error drop? ______
7. The trapezoid rule is more accurate than left-rectangle at the same `n`.
   Why? ______
8. Simpson's rule uses **two** function values per panel. It should therefore
   be roughly ______ times as accurate as a rule using one. ______

Answer 8 carefully — "4" is the expected answer and the reason is not obvious.
Carry it to Tuesday.

## 🇹🇼 TAIWAN CONTEXT

The Part 3 principle is the operational version of something that gets quoted
constantly in monitoring work and rarely obeyed: **the alert threshold is a
design choice, and the measurement error is a design choice, and they have to
be chosen relative to each other.**

The failure in the field is a threshold set to `0.001` on a signal whose
measurement chain has `0.01` of noise, which produces an alarm that fires
constantly and gets muted within a day. The threshold was not wrong in the
abstract; it was wrong *relative to the instrument*. And the converse failure is
rarer and worse: a threshold set far above the noise to stop the false alarms,
which then fails to fire on a real event. Both are the same mistake — choosing
the number without looking at the other number — and both are avoidable by
writing the two figures next to each other in the same sentence.

**Next:** L05, Fri May 7 — laptop. `calckit.py` grows an integration half, and
we find out whether Simpson's rule really is worth the extra function calls.
