# U7 L07 — Least Squares, and Reading the Residuals

**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.4 — fit a least-squares line and diagnose model adequacy from the
residual structure

---

**Laptop today.** This is the pivot of the unit. Everything before it was
numerical method; everything after it is *judgement about a model*.

**The security lens, and it is the whole lesson:** a fit that looks perfect
will happily hide a real pattern. The fit is not the evidence. **The residuals
are the evidence.**

## PART 1 — THE FIT (12 min)

```python
def lsq_line(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    slope = sxy / sxx
    return slope, my - slope * mx
```

Six lines. No library. The derivation is the usual one: minimise the sum of
squared vertical distances, differentiate, set to zero, and the `mx`/`my` terms
appear because the derivative of a sum of squares pulls in a mean.

- ☐  You typed it
- ☐  You can say what `sxx` is and why it is in the denominator
- ☐  **What happens if every `x` is identical?** Do not fix it — just say what
     breaks: ______

The last one is a division by zero that returns `inf` or a `ZeroDivisionError`
depending on the values, and it is the same class of failure as Unit 6's
vertical `slope`. A column of constant values is a legitimate input in real
data — a sensor that only ever reports one reading, a feature that was
degenerate — and the fit should **refuse loudly** rather than return a number
that looks like a slope.

## PART 2 — THE REAL FIT, AND THE FIRST DISAGREEMENT (13 min)

25 points, a trend plus a sine wobble plus small noise. The real output:

```text
data: 25 points, a real trend, a sine wobble, and small noise
least squares fit: y = 2.437966 * x + 41.581726
the trend I built in was slope 2.5, intercept 40.0
```

- ☐  The fit found slope `2.437966`. The truth is `2.5`. Error: ______
- ☐  The fit found intercept `41.581726`. The truth is `40.0`. Error: ______
- ☐  **The intercept is off by 4%, the slope by 2.5%.** Why is the intercept
     worse in relative terms? ______
- ☐  Now the important question: **the data contains a sine wobble the line
     cannot hold.** So the fit is fitting a straight line to curved data. The
     slope error is therefore *not* only about noise. In one sentence, what is
     the fit actually averaging? ______

The last one is the key insight and it is worth labouring. A least-squares fit to
curved data returns **the average slope of the curve over the range you gave
it**, not the slope anywhere in particular. Change the range, change the
answer, even though the underlying function is unchanged. A trend line fitted
over January gives a different number from the same function fitted over June,
and neither is lying.

- ☐  So: is `2.437966` a property of the data, or of the data **plus the range
     I chose**? ______
- ☐  What would you have to report alongside the slope to make it
     interpretable? ______

## PART 3 — READ THE RESIDUALS (15 min)

Here is the residual table, real output, with a bar for each so you can see
shape rather than compute:

| `x` | actual | predicted | residual | bar |
|---|---|---|---|---|
| 0 | 39.4413 | 41.5817 | −2.1404 | -#### |
| 1 | 45.0417 | 44.0197 | 1.0220 | +## |
| 2 | 50.0823 | 46.4577 | 3.6247 | +####### |
| 3 | 51.7107 | 48.8956 | 2.8151 | +##### |
| 4 | 53.5056 | 51.3336 | 2.1720 | +#### |
| 5 | 58.5606 | 53.7716 | 4.7891 | +######### |
| 6 | 60.1931 | 56.2095 | 3.9835 | +####### |
| 7 | 62.2393 | 58.6475 | 3.5918 | +####### |
| 8 | 63.2694 | 61.0855 | 2.1839 | +#### |
| 9 | 63.6463 | 63.5234 | 0.1229 | + |
| 10 | 63.1061 | 65.9614 | −2.8553 | -##### |
| 11 | 64.7242 | 68.3994 | −3.6751 | -####### |
| 12 | 64.6833 | 70.8373 | −6.1540 | -############ |
| 13 | 65.0848 | 73.2753 | −8.1905 | -################ |
| 14 | 69.7047 | 75.7133 | −6.0085 | -############ |
| 15 | 71.8984 | 78.1512 | −6.2528 | -############ |
| 16 | 74.3750 | 80.5892 | −6.2142 | -############ |
| 17 | 80.5311 | 83.0272 | −2.4961 | -#### |
| 18 | 83.7682 | 85.4651 | −1.6969 | -### |
| 19 | 88.0292 | 87.9031 | 0.1261 | + |
| 20 | 91.6701 | 90.3410 | 1.3291 | +## |
| 21 | 95.0095 | 92.7790 | 2.2305 | +#### |
| 22 | 101.0335 | 95.2170 | 5.8165 | +########### |
| 23 | 103.8277 | 97.6549 | 6.1728 | +############ |
| 24 | 105.7968 | 100.0929 | 5.7039 | +########### |

The summary numbers:

```text
RMSE = 4.236331
largest |residual| = 8.190497
mean residual = -1.279e-14 (should be near 0 -- that is what least squares does)
adjacent residuals flip sign 3 times out of 24
```

- ☐  **The residuals are positive for `x = 1..9`, negative for `x = 10..18`,
     positive for `x = 19..24`.** Three blocks. Is that noise? ______
- ☐  Count the sign flips: **3 out of 24**. For genuine random noise you would
     expect about half, roughly 12. What does 3 out of 24 tell you? ______
- ☐  The mean residual is `-1.279e-14`, essentially zero. **That is guaranteed
     by least squares and tells you nothing at all.** Why is a guaranteed
     property a useless diagnostic? ______
- ☐  So we have a fit whose residuals are *not* random, arranged in three long
     blocks, and whose one guaranteed property is holding perfectly. **What is
     the model doing, and what should it have been?** ______

The last one is the entire lesson. **The residual pattern is a block of
negative values in the middle** — the sine the line could not follow. The fit
swallowed the sine's overall effect into the slope and left the oscillation
behind as structure. A model that is *wrong in a structured way* is much more
dangerous than one that is wrong randomly, because structure is repeatable and
therefore exploitable — and it is exactly what an anomaly detector will later
misread as a real event.

The framing to memorise: **a residual pattern is a description of what your
model is blind to.** Random residuals mean the model is blind to nothing in
particular. Blocked residuals mean the model is blind to a specific, real
phenomenon you have not named yet.

## PART 4 — PROVE IT (5 min)

The real output that confirms the diagnosis:

```text
the sine term is the part the line cannot hold:
   x    actual   trend only   trend+sine   residual vs trend+sine
   0     39.441        40.000         40.000              -0.5587
   1     45.042        42.500         44.463               0.5785
   2     50.082        45.000         48.710               1.3721
   3     51.711        47.500         52.549              -0.8381
   4     53.506        50.000         55.832              -2.3261
   5     58.561        52.500         58.472               0.0882
   6     60.193        55.000         60.456              -0.2627
   7     62.239        57.500         61.839               0.4008
```

- ☐  Look at the "trend only" column. Is the straight-line prediction
     systematically **above** the actual at small `x` and **below** at large
     `x`? ______
- ☐  Look at "residual vs trend+sine" for the first few points. Are they
     smaller than the original residuals? ______
- ☐  **So the fix is not a better line. The fix is a model with a sine term in
     it.** State that, and state what it implies about your original
     specification: ______

The last one is the specification lesson from Unit 7 L01 arriving on schedule.
You fitted a line to data that had a cycle in it. Nothing in the arithmetic
noticed. Only the residuals did.

## TURN IN — Regression Checklist

1. `lsq_line` in `calckit.py`, written by hand, no library fit
2. A guard for the all-same-`x` case that **raises**, per Part 1
3. The 25-row residual table, pasted, with the bars
4. The four summary statistics: RMSE, largest residual, mean residual, sign
   flips
5. **A written diagnosis of the residual pattern** in three sentences, naming
   the block structure and what it means
6. A plot of the residuals against `x` — or, if you are not plotting, a text
   sketch of what it looks like, and an argument for why the shape matters
7. `test_calckit.py`: a line through exactly two points recovers them exactly

## 🇹🇼 TAIWAN CONTEXT

Part 3's blocked residuals are the single most common real finding in
infrastructure analysis, and it is a specification failure dressed as a data
failure. Fit a straight line to a month of throughput that contains a weekly
cycle and the residuals will arrange themselves into seven-day blocks, exactly
as today's do in three blocks. The line is not wrong. The line is just blind to
the rhythm, and the rhythm is real, strong, and completely predictable.

The operational consequence is nasty and worth knowing before you hit it: the
residuals from a misspecified fit are *systematically* large at predictable
times, and an anomaly detector built on those residuals will fire every week at
the same hour. Teams then learn that the alert is noise, and they mute it — and
the mute is permanent, and it survives the week a real event occurs inside that
same window. **A detector trained on a misspecified model does not just fail to
help; it teaches people to ignore it.** Specify the model correctly first, and
the residual-based alarm becomes trustworthy. That ordering is not a detail.

**Next:** L08, Wed May 12 — paper check on L06–L07, and we diagnose residual
patterns from paper sketches alone.
