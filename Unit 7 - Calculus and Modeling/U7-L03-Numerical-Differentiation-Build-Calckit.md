# U7 L03 — Numerical Differentiation: Build `calckit.py`

**Date:** Wednesday, May 5, 2027
**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.2 — implement forward, backward, and central differences and find the
step size that minimises error

---

**Laptop today.** Yesterday you predicted the shape of a table. Today you find
out where the bottom is.

**The security lens, stated once and then applied every lesson in this unit:**
a rate-of-change monitor — "this is climbing faster than it should be" — is
exactly a derivative. Everything today is about not building one that cries
wolf.

## PART 1 — THE TOOLKIT (12 min)

No sympy needed for this one. Pure stdlib.

```python
import math

def fwd_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def bwd_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)
```

- ☐  You typed it
- ☐  You can say, without running it, which of the three needs `f` at three
     points and which at two
- ☐  You can say why `central_diff` divides by `2.0 * h` and not by `h`

That last one is worth a moment. The numerator is `f(x+h) − f(x−h)`, a span of
`2h`, and the tangent of that slope is the derivative. Dividing by `h` would
double your answer.

## PART 2 — THE TRUTH, AND THE TABLE (12 min)

The exact derivatives of your test functions:

```text
exact derivatives at the test points
  x^2       at 2.0   exact =  4.0
  sin(x)    at 0.0   exact =  1.0
  exp(x)    at 1.0   exact =  2.718281828459045
```

Now the real table. True value for `x²` at 2 is `4.0`. All three columns
printed together because the comparison is the lesson:

| `h` | forward | abs err | central | abs err |
|---|---|---|---|---|
| 1e-01 | 4.1 | 0.1 | 4 | 8.88e-16 |
| 1e-02 | 4.01 | 0.01 | 4 | 6.31e-14 |
| 1e-03 | 4.001 | 0.001 | 4 | 4.41e-13 |
| 1e-04 | 4.00010000001 | 0.0001 | 4 | 4e-12 |
| 1e-05 | 4.00001000003 | 1e-05 | 4.00000000003 | 2.62e-11 |
| 1e-06 | 4.00000100065 | 1e-06 | 4.00000000012 | 1.15e-10 |
| 1e-07 | 4.00000009115 | 9.12e-08 | 3.99999999567 | 4.33e-09 |
| 1e-08 | 3.99999997569 | **2.43e-08** | 3.99999997569 | 2.43e-08 |
| 1e-09 | 4.00000033096 | 3.31e-07 | 4.00000033096 | 3.31e-07 |
| 1e-10 | 4.00000033096 | 3.31e-07 | 4.00000033096 | 3.31e-07 |
| 1e-11 | 4.00000033096 | 3.31e-07 | 4.00000033096 | 3.31e-07 |
| 1e-12 | 4.00035560233 | 0.000356 | 4.00035560233 | 0.000356 |

- ☐  **The forward minimum is at `h = 1e-08`, error `2.43e-08`.** Write it
     down. What did you predict yesterday? ______
- ☐  From `h = 1e-01` down to `1e-08`, the error falls from `0.1` to `2.43e-08`
     — about a factor of ______ over eight decades of `h`. Why does the
     improvement **slow down** as it goes? ______
- ☐  After the minimum, the error grows. From `1e-08` to `1e-12` it goes
     `2.43e-08` → `3.56e-04`, a factor of about ______ in four decades. The
     growth is **not** a clean power law here, and the reason is: ______
- ☐  Look at rows `1e-08` through `1e-11`. The forward and central errors are
     **identical**, and the forward value stops changing at all. What is going
     on? ______

That last one is not a mistake and it is the best observation in the table.
Below about `1e-8` on this function at this scale, the difference `f(x+h) − f(x)`
becomes **smaller than the gap between representable doubles near 4.0**, so the
subtraction returns the same answer every time. The forward and central
differences are then literally computing the same thing, from the same
quantised inputs, and the error floor is `2.43e-08` — the size of one unit in
the last place at that magnitude. **The method has hit the representation, not
a limit of the mathematics.** That is the same lesson as `0x4c4b40` in Unit 6
L03, and it is the reason a smaller `h` is not a strictly better `h`.

The two error sources are: **truncation error**, growing linearly in `h`, from
using a finite difference instead of the true tangent; and **round-off error**,
growing as `1/h`, from the finite number of bits in each double. They cross,
and the crossing is the minimum. There is no formula worth memorising; the
answer depends on the function, the scale, and the machine.

## PART 3 — CENTRAL IS BETTER (10 min)

The central column above, read against the forward column. Two things to notice
and they point in opposite directions:

- ☐  At **`h = 1e-01`**, central error is `8.88e-16` and forward error is
     `0.1`. That is a factor of about ______ — and it is *more* than the 100×
     that `h²` versus `h` predicts at `h = 0.1`. Why is the improvement
     **better** than the theory suggests? ______
- ☐  At **`h = 1e-05`**, central error is `2.62e-11` and forward is `1e-05`. A
     factor of about ______ — roughly 100×, as `h²` versus `h` predicts at this
     `h` since `h = 1e-5` gives `(1e-5)² = 1e-10`. Consistent
- ☐  At **`h = 1e-04`**, central is `4e-12` and forward is `1e-4`. Factor of
     about ______ — and the theory predicts `1e-8`, so central is doing
     **worse** than its own error order. What has taken over? ______

The answer to the last one is round-off: by `1e-4` the `h²` term has shrunk far
enough that the round-off floor is larger. Central difference has a better
truncation error *and* the same round-off floor, so it is better in the middle
of the range and **identical at the bottom**, because at the bottom both methods
are limited by the same quantisation.

- ☐  Central difference is clearly better in the middle of the range. **What
     does it cost?** ______

The cost: two function evaluations instead of one, and — decisively in
production — the two evaluations straddle your point, so it wants
`f(x+h) − f(x−h)`. If your data only runs to `x = 10` and you ask for the
derivative at `10`, central difference wants a reading at `10 + h` that does
not exist. **That is the real reason forward difference survives in production
code** — not accuracy taste, but the edge of the data.

## PART 4 — READ THE OUTPUT LIKE AN ENGINEER (11 min)

At `h = 1e-5`, the real output:

```text
sin at 0:  fwd=0.9999999999833332 central=0.9999999999833332 exact=1.0
exp at 1:  fwd=2.7182954199567173 central=2.718281828517632 exact=2.718281828459045
```

- ☐  For `exp` at 1, the forward answer is `2.7182954199567173` and the exact is
     `2.718281828459045`. They agree through `2.71828` and then diverge — about
     ______ correct decimal places
- ☐  The central answer `2.718281828517632` agrees with the exact to about
     ______ decimal places
- ☐  **Notice something odd in the `sin` row:** forward and central printed the
     *identical* value `0.9999999999833332`, and it is **not** 1.0. Why are
     they the same here when they differ in the `x²` table? ______
- ☐  **Now the important one.** If you were shipping a rate-of-change alarm
     with a 1% error, would you notice either of these errors? ______
- ☐  If you were triggering on a change of 0.00001 in a value — and note the
     `exp` forward answer is off by `1.36e-05` — would you? ______

The `sin` row deserves a sentence. Central and forward agree exactly because at
`x = 0`, `sin` is antisymmetric: `sin(−h) = −sin(h)`, so the central numerator
`sin(h) − sin(−h)` is `2 sin(h)` and the forward numerator `sin(h) − 0` is
`sin(h)`. Divide by the same `2h` vs `h` and you get the identical value. For
an odd function at a point where `f(0) = 0`, the two methods coincide exactly —
not approximately, exactly. It is a structural coincidence, and it is why you
cannot reason about a method's accuracy from a single lucky test case.

That is the point of the whole lesson. **A derivative method can be visibly
wrong on paper and completely adequate for the job** — and the fact that it is
adequate is a property of *your alarm threshold*, not of the method. You have
to check the error against the decision you are trying to make. Nobody does
this, and the reason is that it requires asking the awkward question.

## TURN IN — `calckit.py` Checklist

1. `calckit.py` with all three difference functions committed
2. The full `h` table for **two** functions, not one, pasted
3. The minimum-error `h` identified for each, with the number
4. The growth factors of 10 in both directions, computed from your own output —
   not copied from this page
5. A written sentence: "for an alarm threshold of ___, method ___ is adequate
   because ___" — the engineer's answer from Part 4
6. `test_calckit.py` with at least one test at a known derivative

## 🇹🇼 TAIWAN CONTEXT

The Part 4 question is the deployment question, and it has a sharp local edge.
Any derivative-based threshold on real infrastructure data is operating on
sensor readings with known accuracy specifications, and the method error must be
compared against the *threshold* rather than against the true derivative. A
first-order forward difference at `h = 1e-3` on a well-conditioned signal gives
you a relative error near `1e-3` — and for a rate-of-change alarm set at, say,
5% change over 15 minutes, that is invisible. The method is adequate. Nobody
needs the central difference and its extra function evaluations, and using it
would cost an evaluation at the data boundary where the reading does not exist.

The real failures come from the other direction: a monitor whose `h` is small
*and* whose input is noisy, which is the `1e-12` row of today's table in the
field. Publish the filter, publish the step, and compare both against the
threshold in the same sentence. An alarm whose accuracy is not stated next to
its threshold is not a specification, it is a hope.

**Next:** L04, Thu May 6 — paper check on L01–L03, and we do the error-curve
drawing properly.
