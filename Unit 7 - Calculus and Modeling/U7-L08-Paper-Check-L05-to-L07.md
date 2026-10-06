# U7 L08 — Paper Check: L05–L07

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.3, 7.4 — audit your own predictions, and diagnose a model from
residuals alone

---

**No laptop.** Pencil. The U7 L07 Part 3 predictions are graded first and
unrevised, which is the whole point of writing them down.

## PART 1 — THE PREDICTION AUDIT (15 min)

From L06, Part 3, predicted before running anything:

| `n` | your predicted value | actual value | your predicted error | actual error |
|---|---|---|---|---|
| 4 | | 0.343750000 | | 1.04e-02 |
| 16 | | 0.333984375 | | 6.51e-04 |
| 64 | | 0.333374023 | | 4.07e-05 |

Exact value is `1/3 = 0.3333333333333333`.

- ☐  Did you predict **above** 1/3, as asked? ______
- ☐  Did you get the **sign** of the error right? That is the meaningful check:
     ______
- ☐  Did you predict the factor of **16** for each quadrupling of `n`? ______
     (from 1.04e-02 to 6.51e-04 is a factor of 16.0; and 6.51e-04 to 4.07e-05 is
     16.0)
- ☐  **The sign check matters more than the digits.** Why? ______

The last one is the point of doing prediction audits at all. You can guess exact
digits by interpolating a trend you already believe in — that is circular and
proves nothing. Predicting the *direction* of an error requires knowing something
about the geometry or the algebra that you had to work out first. A right sign
with sloppy digits is a better paper than wrong digits with lucky interpolation.

- ☐  On a scale of 1–5, how well did your hand-derivation in the U7 L07 Parts 1
     and 2 let you predict? ______
- ☐  What specifically would have improved it? ______

## PART 2 — CONVERGENCE, BY HAND (12 min)

No code, no notes, for the first four.

2. Left rectangle on `x²`, `[0,1]`, `n = 8`: value ______ , error ______
3. Midpoint at the same `n`: value ______ , error ______
4. Trapezoid at the same `n`: value ______ , error ______
5. Simpson at the same `n`: value ______ , error ______
6. Which of the four has the **highest** order, and how could you tell from the
   table that the answer was already exact? ______
7. Midpoint error goes to zero as `h` ______ (fill: `^2` or higher)
8. Trapezoid error goes to zero as `h` ______
9. The predicted improvement factor when you **double** `n`, for either of
   those: ______
10. The same factor when you **quadruple** `n`: ______

## PART 3 — DIAGNOSE FROM RESIDUALS, NO DATA (10 min)

Here is the diagnostic, on paper, with no table in front of you. A least-squares
line was fitted to 30 daily request counts. Describe the shape of the residuals
in each case.

**Case A.** Residuals scatter above and below zero, roughly symmetric, no
visible run of the same sign longer than two.
- ☐  Diagnosis: ______
- ☐  Is there unmodelled structure? ______
- ☐  What do you do next? ______

**Case B.** Residuals run positive for the first 12 points, negative for 6, then
positive for 12.
- ☐  Diagnosis: ______
- ☐  Name a concrete physical cause: ______
- ☐  What does the fit's slope mean, in this case? ______

**Case C.** Residuals get steadily larger as `x` increases — small at the left,
three times bigger at the right.
- ☐  Diagnosis: ______
- ☐  Is the error order affected? ______
- ☐  What one summary number would have hidden this completely? ______

**Case D.** Residuals are all tiny, and the mean residual is exactly zero.
- ☐  Diagnosis: ______
- ☐  **What can you conclude from this, and what specifically can you not?**
     ______
- ☐  Could this case be hiding the worst of the others? ______

Case C's third question and Case D are related, and both are the trap. A single
RMSE pools residuals of wildly different sizes into one number that is
dominated by the large ones, so it can look acceptable while the fit is poor
where you care. And a mean residual of zero is a **guarantee of the method**,
not a finding — every least-squares fit in existence satisfies it, so it carries
no information at all.

- ☐  State the general principle these four cases share: ______

**The principle:** *the fit is not the evidence; the residual pattern is.* And
more sharply — **guaranteed properties of your method are not diagnostics, and
pooled summary statistics destroy exactly the information you need.** You need
the per-point residuals, always, and you should be suspicious of any summary
number that arrives without them.

## PART 4 — ERROR LOG (8 min)

- ☐  Every error from Parts 1 through 3
- ☐  New tags: **prediction audit**, **sign of error**, **pooled statistic**,
     **guaranteed property**
- ☐  Which tag caught an error that pure code execution would have missed?
     ______
- ☐  Most common tag this unit so far: ______

## 🇹🇼 TAIWAN CONTEXT

Part 3 Case B is the most common shape in local operational data and it is
almost always calendar, not noise. Daily counts with a weekly cycle produce
exactly that blocked residual pattern, and the practical consequence is the one
from the Taiwan context in U7 L07: an anomaly threshold derived from those
residuals fires on schedule every week, gets tuned until it stops, and in
becoming tuned it has quietly stopped being capable of detecting anything real.

The habit worth building from this: **when you fit a trend, always plot or print
the residuals per interval, and check the residuals against the calendar before
you check them against anything else.** If the blocks line up with days of the
week, you have found a specification gap, not a detection problem. Checking the
calendar first costs five minutes and prevents a tuning mistake that is very hard
to see later, because a detector that has been tuned to never fire looks exactly
like a detector that has nothing to report.

**Next:** L09 — laptop. The Anomaly Trend Analyzer begins: ingest,
smooth, and the moment you get something you can look at.
