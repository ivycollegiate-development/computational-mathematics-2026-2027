# U7 L04 — Paper Check: Difference Quotients and Step Size

Names: ___________________________  Date: May 6

Closed notes. Pencil. 45 minutes. Wednesday's `h` table is the raw material. There is one thing in this unit you must be able to do without a computer: read an error curve.

## 1: Recall the table

**Section A — From memory, then check.**

1. Forward difference at `h = 1e-3` for `x²` at 2: __________

2. True derivative there: __________

3. The `h` that minimised the forward error: __________

4. The error at that `h`: __________

5. Central difference at `h = 1e-4`, and its error: __________ , __________

6. Between `h = 1e-9`, `1e-10`, and `1e-11`, the forward answer was __________

7. Name the two error sources: _______

8. Which one grows as `h` grows, and which as `h` shrinks? _______

**Section B — Score it.**

- ☐  How many did you get without notes: ________ / 8
- ☐  Question 6 is the interesting one. Why was the answer identical for all three values of `h`? _______

## 2: Draw the error curve

This is the deliverable. On the axes below, sketch `|error|` against `h`, log scale on both axes.

**Section A — Mark these points.**

- ☐  `h = 1e-1`, error `0.1`
- ☐  `h = 1e-8`, error `2.43e-08` — the minimum
- ☐  `h = 1e-12`, error `3.56e-04`
- ☐  the label **truncation error** on the descending arm
- ☐  the label **round-off error** on the ascending arm
- ☐  the two arms as straight lines — justify that: _______
- ☐  the flat shelf you observed across `h = 1e-9` to `1e-11`, drawn flat along the bottom

**Section B — The two questions the drawing answers.**

1. At `h = 1e-3` the error is `1e-3`, about ten thousand times worse than the minimum. Which error source dominates there? _______

2. At `h = 1e-11` the error is `3.31e-07`, also far above the minimum. Which dominates there? _______

3. The general rule, in one sentence: to make the estimate better you __________ the `h` until __________ , and then you must __________ instead. _______

## 3: The adequacy question

**Section A — Both alarms.**

4. An alarm triggers when a rate of change exceeds **1%**. Forward difference at `h = 1e-3` on the `x²` data has error `1e-3` absolute on a value of 4 — that is `0.025%` relative. Adequate? _______

5. An alarm triggers on a change of **0.00001**. Forward difference at `h = 1e-5` on the `exp` data is off by `1.36e-05`. Adequate? _______

6. In case 5, which `h` would you actually choose, and would it be the one with the smallest error? _______

**Section B — The principle.**

7. State the general principle in one sentence, in your own words: _______

## 4: Error log

**Section A — Start the Calculus Error Log, sectioned per unit.**

- ☐  Every error from Parts 1 and 2 goes in
- ☐  New tags for this unit: **step size**, **error order**, **log scale**, **sign of derivative**
- ☐  Most common tag so far today: _______
- ☐  Which of your Part 1 misses would a unit of **paper** have caught rather than running the code? _______

___

**TURN IN** — This sheet, completed, with the error curve drawn and labelled on both arms.
