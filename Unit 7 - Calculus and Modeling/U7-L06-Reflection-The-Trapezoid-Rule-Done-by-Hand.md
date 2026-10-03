# U7 L06 — Reflection: The Trapezoid Rule, Done by Hand

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.3 — derive the trapezoid rule from first principles and predict its
error order before computing

---

**No laptop.** Pencil and graph paper. Friday you ran the trapezoid rule; today
you derive it, and then you predict its behaviour without running anything.

## PART 1 — BUILD IT FROM A PICTURE (15 min)

Draw `f(x) = x²` on `[0, 1]` and lay **two** trapezoid panels under it, at
`x = 0, 0.5, 1`.

- ☐  On the drawing, label each panel's parallel sides and its width
- ☐  Write the area of the first panel as a formula in terms of
     `f(0)`, `f(0.5)`, and the width: ______
- ☐  Write the second: ______
- ☐  Add them. What is the general formula? ______

The general form, which you should now be able to derive from memory:

> trapezoid ≈ (width / 2) × [ f(left) + 2·f(middle) + … + f(right) ]

- ☐  Where did the `2` in front of the middle values come from? ______
- ☐  Compare that with the rectangle rule, which is just (width) × f(left).
    What is the rectangle rule, in the same language? ______

The rectangle rule is the trapezoid rule with the middle values dropped and the
left value used once. So the trapezoid rule is *the rectangle rule plus
information*. That is a useful way to hold it: it is not a different method, it
is the same method with the extra data that the endpoints give you for free.

## PART 2 — WHY IT IS SECOND ORDER (12 min)

Now do the algebra, and it is short. Taylor-expand `f` about the midpoint of a
panel of width `h`:

- ☐  Write `f(left) = f(m) − (h/2)f′ + (h²/8)f″ − …`: ______
- ☐  Write `f(right) = f(m) + (h/2)f′ + (h²/8)f″ + …`: ______
- ☐  **Add them.** Which term cancels? ______
- ☐  Which is the first to survive, and what power of `h` is it? ______
- ☐  So the panel error is `O(h³)`, there are `1/h` panels, and the total
     error is `O(h²)`. Write that reasoning in one line: ______

The `f′` term cancels because you evaluate at **both** ends of the panel. That is
the entire reason the trapezoid rule is second order, and it is the same reason
the central difference beat the forward difference in Unit 7 L03: **sampling on
both sides of your target kills the first-order term.** Two lessons, one
mechanism.

- ☐  So if you had sampled at the left endpoint and the middle instead of both
     endpoints, what order would you get? ______
- ☐  And is that the **midpoint rule**? Which one wins, and by how much? ______

## PART 3 — PREDICT BEFORE YOU COMPUTE (10 min)

No laptop. Predict the shape of each answer, then write what you predict for
`n = 4`, `16`, `64`.

7. Trapezoid on `x²` over `[0,1]`, `n = 4`. **Predict the value**: ______
8. Trapezoid on the same, `n = 16`: ______
9. Trapezoid on the same, `n = 64`: ______
10. Does the predicted value approach 1/3 from **above or below**? ______
11. By roughly what factor does the error drop each time `n` quadruples?
     ______
12. Bonus: does Simpson's rule being exact on cubics surprise you given that
    trapezoid is only exact on straight lines? ______

**No run today.** These go into the paper check on Wednesday against your own
output, which is the only honest way to do a prediction audit.

## PART 4 — ERROR LOG (8 min)

- ☐  Record every arithmetic slip in Parts 1 and 2
- ☐  Tag: **panel width**, **double counting**, **sign**, **order**,
     **careless**
- ☐  One tag that is new since the last paper check: ______
- ☐  **Write down your Part 3 predictions somewhere you cannot revise them.**
     You will find out on Wednesday whether the *sign* of your error was right,
     which is a different and more useful check than the exact digits

## 🇹🇼 TAIWAN CONTEXT

The mechanism in Part 2 — sampling both ends of an interval so the first-order
term cancels — is the same idea behind the trapezoidal rule used to integrate
flow records and rainfall totals over irregular time intervals. When readings
arrive at uneven intervals, the honest integration is not a uniform-panel rule
at all; it is a weighted average where **each panel is weighted by its own
width**. Assuming a uniform interval when the sensors actually reported
irregularly is a specification error that quietly biases the total, and it
produces exactly the signature from Friday: a summary that looks reasonable and
is systematically off in a direction nobody can see.

It is worth knowing the local detail: rainfall and flow gauges in Taiwan
station networks report at mixed cadences depending on station class and on
whether telemetry is available, and any aggregation that assumes uniform
sampling will be wrong. The defensible version of the computation weights by
actual elapsed time. The undWeighted version is the one that ends up in
spreadsheets.

**Next:** L07, Tue May 11 — laptop. We fit a model to data and read what the fit
leaves behind. Predictions from Part 3 get graded first.
