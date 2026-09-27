# U7 L08 — Paper Check: Quadrature and Residuals

Names: ___________________________  Date: May 12

Closed notes. Pencil. 45 minutes. Monday's Part 3 predictions are graded first and unrevised. No code, no notes for the first four questions in Part 2.

## 1: The prediction audit

**Section A — Monday's Part 3, predicted before running anything.**

| ---------- | ------------------------ | ---------------- | ------------------------ | ---------------- |
| -------- | -------- | -------------- | -------- | -------- |
| 16       |          | 0.333984375    |          | 6.51e-04 |
| 64       |          | 0.333374023    |          | 4.07e-05 |

Exact value is `1/3 = 0.3333333333333333`.

**Section B — Score the audit.**

- ☐  Did you predict **above** 1/3, as asked? _______
- ☐  Did you get the **sign** of the error right? _______
- ☐  Did you predict the factor of **16** for each quadrupling of `n`? _______
- ☐  The sign check matters more than the digits. Why? _______
- ☐  On a scale of 1–5, how well did Monday's hand-derivation let you predict? _______
- ☐  What specifically would have improved it? _______

## 2: Convergence, by hand

No code, no notes for questions 1 through 4. Exact value is `1/3 = 0.3333333333333333`.

**Section A — Four rules at `n = 8` on `x²` over `[0,1]`.**

1. Left rectangle: value __________ , error __________

2. Midpoint: value __________ , error __________

3. Trapezoid: value __________ , error __________

4. Simpson: value __________ , error __________

**Section B — Read your own numbers.**

5. Which of the four has the **highest** order, and how could you tell from the table that the answer was already exact? _______

6. Midpoint error goes to zero as `h` __________ (fill: `^2` or higher)

7. Trapezoid error goes to zero as `h` __________

8. The predicted improvement factor when you **double** `n`, for either of those: __________

9. The same factor when you **quadruple** `n`: __________

## 3: Diagnose from residuals, no data

A least-squares line was fitted to 30 daily request counts. Describe the shape of the residuals in each case.

**Case A.** Residuals scatter above and below zero, roughly symmetric, no visible run of the same sign longer than two.

- ☐  Diagnosis: _______
- ☐  Is there unmodelled structure? _______
- ☐  What do you do next? _______

**Case B.** Residuals run positive for the first 12 points, negative for 6, then positive for 12.

- ☐  Diagnosis: _______
- ☐  Name a concrete physical cause: _______
- ☐  What does the fit's slope mean, in this case? _______

**Case C.** Residuals get steadily larger as `x` increases — small at the left, three times bigger at the right.

- ☐  Diagnosis: _______
- ☐  Is the error order affected? _______
- ☐  What one summary number would have hidden this completely? _______

**Case D.** Residuals are all tiny, and the mean residual is exactly zero.

- ☐  Diagnosis: _______
- ☐  What can you conclude from this, and what specifically can you not? _______
- ☐  Could this case be hiding the worst of the others? _______

**Section B — The shared principle.**

10. State the principle all four cases share: _______

## 4: Error log

**Section A — Record it.**

- ☐  Every error from Parts 1 through 3
- ☐  New tags: **prediction audit**, **sign of error**, **pooled statistic**, **guaranteed property**
- ☐  Which tag caught an error that pure code execution would have missed? _______
- ☐  Most common tag this unit so far: _______

___

**TURN IN** — This sheet, with the Part 1 audit table filled in and all four Part 2 values computed by hand.
