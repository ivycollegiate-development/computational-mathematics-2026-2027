# U7 L09 — Anomaly Trend Analyzer Build Day 1: Ingest and Smooth

**Date:** Thursday, May 13, 2027
**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.5 — ingest a series, estimate a baseline, and justify the detrending
method

---

**Laptop today.** The Anomaly Trend Analyzer starts. 60 days of synthetic
request counts, with two real events planted at `t = 20` and `t = 45`.

**The security lens:** the first and hardest question in detection is not "what
is the threshold" but "what is normal". Today you build the normal, and you will
discover that the obvious way to build it does not work.

## PART 1 — THE DATA AND THE GUARD (8 min)

```python
import math

def moving_average(series, k):
    out = []
    for i in range(len(series)):
        lo = max(0, i - k + 1)
        out.append(sum(series[lo:i + 1]) / (i - lo + 1))
    return out
```

- ☐  Note the `max(0, i - k + 1)` and the matching denominator. **Why must the
     denominator vary at the edges?** ______
- ☐  What would happen if you divided by `k` throughout? ______

The second is the classic edge bug: a fixed denominator near the start silently
*shrinks* the average, creating a fake trough at the left edge. It is the same
shape as a real anomaly and it is entirely an artifact of the code. Since
you will build a detector on this baseline, a fake trough at the edge becomes a
false positive at the edge.

## PART 2 — THE BASELINE, AND TWO EVENTS VISIBLE (10 min)

Real output. `raw − baseline` is the column to read:

```text
   t      raw   7-day avg   baseline   raw - baseline
   0     47.55      56.91      51.12     -3.57  -###
   1     60.49      54.24      62.08     -1.59  -#
   2     64.39      51.85      64.09     +0.30  +
   3     55.23      50.68      55.11     +0.12  +
   4     43.53      51.70      47.02     -3.49  -###
   5     39.92      51.59      41.84     -1.92  -#
   6     43.67      51.29      48.00     -4.32  -####
   7     54.65      51.99      53.26     +1.39  +#
   8     59.75      52.85      64.22     -4.47  -####
  19     42.67      61.01      46.12     -3.45  -###
  20     77.81      60.61      52.28    +25.53  +#########################
  21     57.64      61.12      57.54     +0.10  +
  44     77.31      61.63      76.93     +0.37  +
  45     42.94      62.32      67.95    -25.01  -#########################
  46     62.02      62.55      59.87     +2.15  +##
```

- ☐  Two rows jump out: `t = 20` at `+25.53` and `t = 45` at `−25.01`. These
     are the two planted events. **Which direction is each, and does that matter
     to a detector?** ______
- ☐  Every other row shown is under `|5|`. **What is the ratio** between the
     smallest event and the largest non-event? ______
- ☐  So where is the threshold, roughly, and how much margin do you have?
     ______
- ☐  **Look at `t = 44` and `t = 46`, one day either side of the second
     event.** Their residuals are `+0.37` and `+2.15`. Why is `t = 44` so
     small when the event at `t = 45` is 25 units tall? ______

That last question is the cost of smoothing, and it is the first real trade in
the project. A 7-day average centred on `t = 44` **includes the spike at
`t = 45`**, so the baseline absorbs part of the event. The smoother is not just
blurring the signal, it is *contaminating itself with the event it is supposed to
reveal*.

- ☐  This is **masking**, and it means an event near the middle of your window
     is measured against a baseline that has already risen. Restate: a rolling
     mean makes large events look ______ and it makes the noise look ______

## PART 3 — WHY A PLAIN MOVING AVERAGE IS NOT ENOUGH (10 min)

Here is the result that should end the plain-moving-average approach. I ran a
**pure weekly sine** — no trend, no noise, no events — through the same
7-day average:

```text
a 7-day moving average of a PURE weekly sine leaves sd = 8.4438
  the window lags by 3 days, so a sinusoid comes out the other
  side of the subtraction instead of cancelling.
```

- ☐  The 7-day average is *centred* on each day, so it represents day `t` using
     days `t−3` through `t+3` — the middle of that window is **`t` itself**.
     Does that *really* mean it lags by 3 days, or is the script's comment
     about the tail (days 0–2) bleeding into its claim about the whole series?
     Read the residual evidence in Part 2 and decide. ______

That is worth slowing down, because the comment in the code is **wrong** and the
number proves it. In Part 2 the interior residuals are small — `+0.30`, `+0.12`,
`+1.39`, `−3.45`, `+0.10` — nowhere near `8.44`. If a centred window genuinely
lagged by 3 days, the interior residuals would be *full size sine amplitude*.
They are not.

- ☐  So what does `sd = 8.4438` actually measure? **Read which days are
     included in that average.** ______
- ☐  Days 0, 1, 2 and 58, 59 have no full window. At the left edge the window
     is one-sided and genuinely lags. **How many such days are there, out of
     60, and can a handful of them drag a whole-series standard deviation up
     to 8.4?** ______

**That is the real lesson, and it is a security lesson.** The `8.4438` is
**edge contamination contaminating a global statistic**. Seven or eight
one-sided boundary days — where the "centred" window is not centred and does
lag — have dragged a global number that is then used to set a threshold for
every point in the series. A handful of artifacts at the boundary are silently
setting the sensitivity of the entire detector.

- ☐  Two ways to fix it: **(a)** never compute the window statistic over
     boundary days, and **(b)** report the spread over the interior only. Which
     does today's code do, and what should it do? ______
- ☐  Which of these does the real detector in the next two days do, and how can
     you tell? ______

## PART 4 — DAY-OF-WEEK OFFSETS (12 min)

If a centred 7-day average removes a weekly cycle in the interior, the residual
structure left in Part 2 is the trend's fault, not the week's. So model the
week directly: learn one offset per day-of-week from the data, subtract it, then
fit the trend.

```text
day-of-week offsets learned from the data:
    day 0:  -0.716
    day 1:  +9.940
    day 2: +11.645
    day 3:  +2.357
    day 4:  -6.033
    day 5: -11.524
    day 6:  -5.670

trend recovered: +0.3058/day   (I built in +0.35)
```

- ☐  Seven offsets, one per weekday. The largest is day 2 at `+11.645`. **Name
     the day** (day 0 = Monday): ______
- ☐  The offsets are a clean sinusoid — high midweek, low at the weekend. **Does
     that make sense for request counts?** ______
- ☐  The recovered trend is `+0.3058/day`; I built in `+0.35`. So the recovery
     is about ______ % off
- ☐  **Why is it off at all**, given the sine is now fully modelled? ______
- ☐  Now: with the weekly cycle removed *by day-of-week* rather than by a
     moving average, is there any window lag left? ______

That last question is the design decision, and the answer is **no** — there is no
window, so there is nothing to lag, and therefore no edge days, and therefore no
edge contamination. The day-of-week model is a *parametric* subtraction rather
than a *windowed* smoothing, and it does not have the failure mode Part 3 just
exposed. That is why the project uses it.

- ☐  What assumption does the day-of-week model make that a moving average does
     not? ______
- ☐  When would that assumption break, and what would the residuals look like
     when it does? ______

## PART 5 — WRITE IT UP (5 min)

- ☐  A `README` section: **why day-of-week detrending, not a rolling mean**
- ☐  One sentence on the edge-contamination finding, with the `8.4438` number
- ☐  The one assumption your method makes, stated as a limitation

## TURN IN — Build Day 1 Checklist

1. `atkit.py` with `moving_average` and the variable-length edge denominator
2. The Part 2 table for **all 60 days**, not the excerpt
3. The Part 3 experiment: a pure sine through the same smoother, plus your
   written correction of the lag claim
4. `dow_offsets()` implemented and the seven offsets printed
5. The trend line, with the recovery error reported
6. Your README section on the choice of detrending method
7. `test_atkit.py`: `moving_average([5, 3, 1], 2) == [5.0, 4.0, 2.0]`, and a
   constant series returns a constant

## 🇹🇼 TAIWAN CONTEXT

The day-of-week offsets in Part 4 are exactly the shape you see in local
network and service data, and the weekend trough in particular is strong enough
to dominate a naive baseline. That matters operationally because **the quiet
weekend is when the threshold should be tightest and most people set it
uniformly**. A detector that treats a Saturday like a Wednesday is either blind
on weekdays or drowning in weekend false positives, depending on which day you
tuned it on. The correct move is a per-day-of-week threshold, and the offsets
you printed today are the first half of building one.

The other locally relevant piece: holidays and long weekends break the
day-of-week model in a way a plain weekly cycle cannot express. A public holiday
in the middle of the week looks like a very large negative offset on one
specific date, and there is no way to learn that from seven repeating offsets —
it is a one-off, not a pattern. If you deploy anything like this, the honest
version subtracts known holiday dates explicitly, and the residuals get checked
against the calendar before anything else. That check is the same one from L08's
Taiwan context, and it is still the highest-value five minutes in the analysis.

**Next:** L10, Fri May 14 — paper. What actually makes an anomaly an anomaly,
before we pick a number.
