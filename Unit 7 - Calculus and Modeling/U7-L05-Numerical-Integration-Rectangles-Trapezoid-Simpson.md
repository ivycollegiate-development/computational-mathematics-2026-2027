# U7 L05 — Numerical Integration: Rectangles, Trapezoid, Simpson

**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.3 — implement three quadrature rules and identify each one's error
order empirically

---

**Laptop today.** `calckit.py` grows an integration half.

**The security lens:** integration is a *summary*. A daily total, a mean rate, a
cumulative count — all of them are integrals. And an integral is exactly where
a smooth average hides a spike.

## PART 1 — THREE RULES, THREE IDEAS (12 min)

```python
import math

def left_rect(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))

def midpoint(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))

def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2.0 * f(a + i * h)
    return h * s / 2.0

def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson's rule needs an even number of panels")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return h * s / 3.0
```

Three ideas, not three formulas:

- ☐  `left_rect` uses the **left endpoint** of every panel
- ☐  `midpoint` uses the **middle** of every panel — same `n` function calls as
     left rectangle, but a better place to sample
- ☐  `trapezoid` uses **both** endpoints of each panel, which is why it wins
- ☐  `simpson` is a trapezoid rule with a **correction term**, and the
     correction is what buys the extra order of accuracy

**On the guard in `simpson`:** that `raise` is not defensive decoration. Simpson
weights assume an even panel count; pass an odd `n` and the weights are wrong in
a way that produces a plausible-looking number that is simply not the integral.
Compare it to the `slope` guard in Unit 6: **a wrong-but-plausible answer is
worse than a refusal**, and the guard is what converts one into the other.

## PART 2 — THE TABLES (13 min)

Here is the real output for `f(x) = x²` on `[0, 1]`, where the exact answer is
`1/3 = 0.333333…`. All three rules, all eight panel counts:

| `n` | midpoint | abs err | trapezoid | abs err | Simpson | abs err |
|---|---|---|---|---|---|---|
| 2 | 0.312500000 | 2.08e-02 | 0.375000000 | 4.17e-02 | 0.333333333 | 0.00e+00 |
| 4 | 0.328125000 | 5.21e-03 | 0.343750000 | 1.04e-02 | 0.333333333 | 0.00e+00 |
| 8 | 0.332031250 | 1.30e-03 | 0.335937500 | 2.60e-03 | 0.333333333 | 0.00e+00 |
| 16 | 0.333007812 | 3.26e-04 | 0.333984375 | 6.51e-04 | 0.333333333 | 0.00e+00 |
| 32 | 0.333251953 | 8.14e-05 | 0.333496094 | 1.63e-04 | 0.333333333 | 0.00e+00 |
| 64 | 0.333312988 | 2.03e-05 | 0.333374023 | 4.07e-05 | 0.333333333 | 0.00e+00 |
| 128 | 0.333328247 | 5.09e-06 | 0.333343506 | 1.02e-05 | 0.333333333 | 0.00e+00 |
| 256 | 0.333332062 | 1.27e-06 | 0.333335876 | 2.54e-06 | 0.333333333 | 0.00e+00 |

Three things to read off, and they are three different lessons:

1. **Simpson's error column is `0.00e+00` on every single row.** That is not a
   formatting artifact and not a display problem — the computed value is
   bit-for-bit the nearest double to 1/3, and **no double is any closer**. On a
   cubic, Simpson is exact in exact arithmetic; `x²` is a cubic; so the entire
   remaining error is the machine's, and the machine is out of room.
   - ☐  Why is the Simpson error *exactly* zero rather than merely tiny?
     ______
   - ☐  **Warning, and this matters:** this is the most flattering table in the
        unit. Simpson looks perfect here because the test function happens to
        be a cubic and Simpson is built for cubics. On a function that is not
        smooth, or not a cubic, the error column will be ordinary. Keep that
        in mind for question 6
   - ☐  Give a function on `[0,1]` for which Simpson's `n = 2` answer is
        **terrible**, not perfect: ______ (a spike, or a kink, will do)

2. **Midpoint and trapezoid both improve by a factor of 4 per doubling of `n`.**
   Midpoint: `1.30e-03` → `3.26e-04` is a factor of 4.0; then
   `3.26e-04` → `8.14e-05` is 4.0. Trapezoid: `2.60e-03` → `6.51e-04` is 4.0.
   Every ratio in both columns is 4.0 to three figures, start to finish.
   - ☐  So these two are **second order**: error ∝ `h²`. State the predicted
        factor for a doubling of `n`: ______
   - ☐  Both columns hit it *exactly* here, not approximately. Why is the
        agreement cleaner than it was in the differentiation table?
         ______
   - ☐  From what you know about `x²`: what is special about a polynomial of
        degree 3 for a rule that approximates with quadratics? ______

3. **Trapezoid is also second order**, which surprises people who assume
   trapezoid is worse than left rectangle.
   - ☐  Compare trapezoid to midpoint at `n = 32`: errors `1.63e-04` and
        `8.14e-05`. Midpoint is better by a factor of about ______
   - ☐  At `n = 4` the two are `1.04e-02` and `5.21e-03`, also a factor of 2.
        So the ratio between them is **constant at 2** across the whole table.
        What does a constant ratio tell you? ______
   - ☐  Why does the trapezoid rule get an extra order? It uses **both**
        endpoints, so the first-order `h` term cancels. In one sentence:
         ______

The constant factor of 2 is the clean result: midpoint and trapezoid differ
only in *where* they sample, and for a quadratic both are exact to second order,
so their errors differ by a constant and not by a power of `h`. Same order,
constant factor. That is what "both are second order" looks like in practice.

## PART 3 — THE HONEST TEST (10 min)

3. Compare Simpson against trapezoid at `n = 16`: `0.00e+00` versus `6.51e-04`.
   **What does that ratio tell you, and what does it fail to tell you?**
   ______
4. **But** Simpson needs `2n` function evaluations to reach the same accuracy as
   a trapezoid with `n` panels. On the trapezoid column, at what `n` does the
   error first drop below `1e-3`? ______
5. So which is actually cheaper in *function calls* for a target error of
   `1e-3`? ______
6. **Now the real question.** Simpson's advantage above is partly the function.
   Write a function where Simpson's extra order does **not** save you, run it,
   and report the numbers: ______

For question 6, here is one I tried, so you know whether your answer is in the
right region. `f(x) = abs(x - 0.5)` on `[0,1]`, a **kink** in the middle:

```text
  kink |x-0.5| n=4    trap 0.25000000 simpson 0.25000000
  kink |x-0.5| n=8    trap 0.25000000 simpson 0.25000000
  kink |x-0.5| n=64   trap 0.25000000 simpson 0.25000000
  kink |x-0.5| n=256  trap 0.25000000 simpson 0.25000000
  true kink integral: 0.25
```

**Both rules are exact at every `n`.** No kink penalty at all.

- ☐  Why? `|x − 0.5|` is not a cubic, so Simpson's exactness-on-cubics argument
     should not apply. What saves it? ______

The answer: `|x − 0.5|` is **piecewise linear**, and both rules are exact on
linear functions. Any panel that happens to straddle the kink gets an
approximation, and any panel entirely on one side gets the exact answer — and
as `n` grows, panels straddling the kink contribute `O(h²)` in total, which
keeps the overall order. So the kink argument is *wrong*, and I would rather
show you a wrong argument that fails under test than have you build a
conclusion on my say-so. **Try it, watch it fail, and use that instead.** Now
go find a function that actually defeats Simpson.

## PART 4 — THE SPIKE, WHICH IS THE POINT (8 min)

This one does defeat every rule in the lesson. `f` is 1 across `[0,1]` with a
spike of height 100 over a width of 0.01, centred:

```text
true spike integral: 1.99
  midpoint n=10     -> 1.000000
  midpoint n=100    -> 2.980000
  midpoint n=1000   -> 1.990000
  midpoint n=10000  -> 1.990000
```

Read those four lines carefully, because they contain two different failures and
only the first one is intuitive.

- ☐  At `n = 10` the answer is `1.000000`. The true value is `1.99`. **What
     happened to the spike?** ______
- ☐  At `n = 100` the answer is `2.980000` — it **overshot by 50%**. Explain a
     result that is worse than being blind: ______
- ☐  So quadrature can be wrong in **both directions** — too low by skipping
     the spike, too high by catching a panel at the spike's shoulder. Which is
     more dangerous in a system that only alerts on "too high"? ______
- ☐  From `n = 1000` on, it is right. **So is "use a bigger `n`" the fix?** Why
     not? ______

The overshoot is the interesting one and it deserves a sentence. At `n = 100` the
panel width is `0.01` — the same as the spike's width — so panels straddle the
spike's edges. Midpoint samples a point just off the shoulder of a step of
height 100, contributing `100 × 0.01 = 1.0` of spurious area, and the true spike
contributes only `0.99`. **The method gets worse before it gets better**, and
any threshold set on this integral would fire at the wrong `n`.

- ☐  What is the actual fix, and why is it not "sample finer"? ______
- ☐  Write it as a README sentence: ______

The fix is to **report the per-panel maximum, not only the sum.** A single panel
contributing `1.0` out of a `1.99` total is glaring in the parts and completely
invisible in the sum. Same data, one extra statistic, and the failure mode
disappears. **A summary statistic hides its own evidence, and you have to
compute the evidence separately to see it.**

## TURN IN — Integration Checklist

1. All four rules in `calckit.py`, with the `simpson` guard
2. The full `x²` table, all three rules, all eight `n` values, pasted
3. **A second function** — not `x²` — with its own table and its own
   convergence factor
4. Your answer to question 6, with the numbers you actually got
5. The spike argument, written as a README sentence
6. `test_calckit.py`: `simpson` with an odd `n` raises; `left_rect` at `n = 1`
   on `x²` returns `0.0`

## 🇹🇼 TAIWAN CONTEXT

Part 4 is not a trick and the failure is common in real operational reporting.
Any "daily total" or "mean rate" that is computed by quadrature over time-series
data has the same blind spot, and in infrastructure the blind spot is where the
interesting events are: a short burst of traffic, a brief load spike, a
one-minute flood of connection attempts. A daily total that looks entirely
normal is exactly what you get when a short, large event is averaged into a
long, quiet baseline.

The honest engineering practice, and it is worth stating as a habit: **report
the maximum alongside the mean, every time.** A reader who sees `mean 0.4,
max 100` learns something; a reader who sees `mean 0.4` learns nothing about
whether anything happened. Same data, one extra number, and the entire failure
mode disappears. This is cheap and it is not standard practice, which is
precisely why it is worth forming the habit now.

**Next:** L06, Mon May 10 — paper check on L04–L05, and we build the error
order table by hand from your own output.
