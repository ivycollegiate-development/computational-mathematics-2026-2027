# U7 L02 — The Difference Quotient, By Hand Until It Obvious

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.2 — construct a difference quotient and predict its limiting behaviour
before computing anything

---

**No laptop.** Pencil. Today we do the arithmetic that tomorrow's code
automates, and you will not understand tomorrow's code if you skip it.

Everything in numerical differentiation is the definition of the derivative:
the slope of a secant line, approached. Today you will watch the approach
happen on paper, in a table, and see the two failure modes arrive.

## PART 1 — SECANT, THEN TANGENT (15 min)

The slope of the line through `(x, f(x))` and `(x+h, f(x+h))` is

> **(f(x+h) − f(x)) / h**

1. For `f(x) = x²`, compute the slope from `x = 2` to `x = 3`: ______
2. From `x = 2` to `x = 2.5`: ______
3. From `x = 2` to `x = 2.1`: ______
4. From `x = 2` to `x = 2.01`: ______
5. The true slope of `x²` at `x = 2` is `2x = 4`. **Write out the algebra**
   showing the quotient simplifies to `2x + h`, and say what it becomes as
   `h → 0`: ______

So the sequence of secant slopes is 5, 4.4, 4.2, 4.04… approaching 4. Every
number you computed is an *approximation with an error attached*, and the error
has a name: `h`.

- ☐  What is the relationship between `h` and the error? ______
- ☐  So why not just take `h` as small as possible? **Think about how this
     would be done on a real sensor, not a textbook.** ______

That last question is the whole lesson and it has a concrete answer on
Wednesday. Hold onto it.

## PART 2 — TWO WAYS TO BE WRONG (15 min)

Consider a difference quotient used on **measured** data, not exact maths.

6. Suppose your readings are accurate to 0.01. The numerator
   `f(x+h) − f(x)` is a **difference of two nearly equal numbers**. If `h` is
   very small, that difference is small and the 0.01 error is a *large fraction
   of it*. What happens to the quotient? ______
7. Name the two ways the estimate can go wrong and say which one you get from a
   too-large `h` and which from a too-small `h`:
   ______
8. Does a smaller `h` always improve the answer? ______
9. Draw the shape of the error as a function of `h`. It should have a minimum
   and rise on **both** ends. Label both ends. ______

- ☐  Where is the sweet spot, roughly? ______
- ☐  **This is the single most useful sentence in the unit:** a too-large `h`
     is a **modeling** error, a too-small `h` is a **measurement** error.
     Which one is worse in a security system, and why? ______

Question 9 is why the optimisation exists. The best `h` is not a matter of
taste; it is where the two curves cross.

## PART 3 — PREDICT THE TABLE (10 min)

Tomorrow you will run a script that does this for several `h` values. Predict
the *shape* of the answer before you see numbers.

For `f(x) = x²` at `x = 2`, the true derivative is `4`. Fill in:

| `h` | predicted quotient | better or worse than the one above it? |
|---|---|---|
| 1 | | |
| 0.1 | | |
| 0.01 | | |
| 0.001 | | |
| 1e-6 | | |
| 1e-9 | | |
| 1e-12 | | |

- ☐  The accuracy should **improve** down to some `h`, then get **worse**. Which
     row is the bottom? ______
- ☐  What is the quotient at `h = 1e-12`? Predict the actual number: ______
- ☐  **Why will that number be absurd?** ______

The last one is not a trick. At tiny `h` the quotient is dominated by floating
point round-off, and it can return values like `3.9999...` or even a number
that looks like noise. This is not a bug in the script; it is the limit of what
the representation can hold, and it is the same lesson as `0x4c4b40` from
Unit 6 L03.

## PART 4 — THE FORWARD/BACKWARD/CENTRAL QUESTION (5 min)

11. The **central** difference uses `(f(x+h) − f(x−h)) / 2h`. Why does it
     usually beat the forward difference? ______
12. What does it cost you? ______

- ☐  My answer to 11: ______
- ☐  My answer to 12: ______

## 🇹🇼 TAIWAN CONTEXT

The too-small-`h` failure is not academic anywhere; it is the standard failure
of any derivative-based monitor on noisy data. A vibration-threshold detector
for rotating machinery, or a rate-of-change monitor on a power-distribution
measurement, differentiates a signal that carries sensor noise. Differentiation
amplifies high frequencies, and sensor noise is mostly high frequency. Turn the
gain up far enough to catch a real ramp and the monitor reports a violent
transient on every sample — the classic "flat line with spikes on it" output.

The operational response is not a smaller step. It is **filtering first, then
differentiating the filtered signal**, and stating the filter's own smoothing
time in the output, because a derivative you have smoothed is measuring a
different thing than the raw signal's derivative. The trade is not hidden — it
is disclosed, in the same place you put the units.

**Next:** L03, Wed May 5 — laptop. We build `calckit.py` and check every row of
Part 3, and I want to see which of you guessed the bottom row correctly.
