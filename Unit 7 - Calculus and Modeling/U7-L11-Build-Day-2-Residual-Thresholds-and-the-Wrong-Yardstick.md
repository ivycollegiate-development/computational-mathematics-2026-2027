# U7 L11 — Build Day 2: Residual Thresholds, and the Wrong Yardstick

**Date:** Monday, May 17, 2027
**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.5 — set an anomaly threshold and justify it against a stated false-
positive cost

---

**Laptop today.** The detector exists. Today you pick its number, and you will
see the number **zero** do more damage than you expected.

## PART 1 — THE WRONG YARDSTICK (10 min)

First, the obvious approach, run so you can see it fail. Threshold the series
*without* removing the weekly cycle:

```text
thresholding the RAW series without removing the weekly cycle:
--- raw residuals, k=2.0, MAD
    spread 12.2364 (1.4826*MAD)   threshold 2.0x = 24.4729
    flagged 0: nothing
    caught 0/2 real events   false positives 0
--- raw residuals, k=3.0, MAD
    spread 12.2364 (1.4826*MAD)   threshold 3.0x = 36.7093
    flagged 0: nothing
    caught 0/2 real events   false positives 0
```

- ☐  **Zero events caught, at both thresholds.** Not one. Read that again.
- ☐  The spread is `12.2364`. A real event is about `25`. So the events are
     roughly ______ times the spread
- ☐  Yet at `k = 2` the threshold is `24.4729`, and the event at `t = 20` is
     `+25.5`. **That clears the bar — so why was nothing flagged?** ______
- ☐  Because the *residual* of the raw series is not the raw deviation. Work
     out what "raw residual" means here before the weekly cycle is removed,
     and why its spread is so much larger than the events: ______

That last one is the important catch. `24.4729 < 25.5`, so a naive reading says
the event *should* have fired. The reason it did not is that the threshold is
measured against the **variance of the residual series**, and the residual of a
raw series still contains the whole weekly swing — so the yardstick is fattened
by the very structure you were supposed to remove. **A spread computed over
unmodelled structure measures the structure, not the noise.**

- ☐  State the general principle: a threshold's *scale estimate* must be
     computed from residuals that contain only noise, or the scale measures
     ______ instead

## PART 2 — THE DETRENDED YARDSTICK (12 min)

Now detrend, and sweep the threshold. Same data, same model, one number changed:

```text
--- detrended, k=2.0, MAD
    spread 2.7490 (1.4826*MAD)   threshold 2.0x = 5.4979
    flagged 4: t=20(+25.5), t=34(-5.6), t=36(+5.8), t=45(-25.0)
    caught 2/2 real events   false positives 2
--- detrended, k=3.0, MAD
    spread 2.7490 (1.4826*MAD)   threshold 3.0x = 8.2469
    flagged 2: t=20(+25.5), t=45(-25.0)
    caught 2/2 real events   false positives 0
--- detrended, k=4.0, MAD
    spread 2.7490 (1.4826*MAD)   threshold 4.0x = 10.9959
    flagged 2: t=20(+25.5), t=45(-25.0)
    caught 2/2 real events   false positives 0
--- detrended, k=5.0, MAD
    spread 2.7490 (1.4826*MAD)   threshold 5.0x = 13.7448
    flagged 2: t=20(+25.5), t=45(-25.0)
    caught 2/2 real events   false positives 0
```

The spread collapsed from `12.2364` to `2.7490` — a factor of 4.5 — purely by
removing the weekly cycle. **The events did not change. The yardstick did.**

- ☐  At `k = 2`, `t = 34` and `t = 36` fire. **Why two, when the two planted
     events are far apart in time at 20 and 45?** ______
- ☐  Look at the residuals around the second event: `t = 44` is `+0.37` and
     `t = 46` is `+2.15`. **What is happening at 34 and 36?** ______
- ☐  The spread is `2.7490`; the false positives are `−5.6` and `+5.8`, just
     over `2.0 × 2.7490 = 5.4979`. **Are they extreme, or is the threshold just
     too low?** ______
- ☐  So at `k = 2` the detector is correct about the events and correct about
     the false positives. **Is the detector wrong, or is the threshold
     wrong?** ______

The last one is the distinction worth a whole lesson. `t = 34` and `t = 36` are
not anomalies. The model produced a residual distribution whose typical
magnitude is 2.75, and a 2× yardstick is inside the ordinary range. The
detector is doing exactly what it was asked; the request was wrong.

- ☐  From `k = 3` upward the flags are **identical**. So the choice between
     `k = 3`, `k = 4`, and `k = 5` is ______ — the data does not distinguish
     them

That is a real and slightly uncomfortable result: you have **no evidence** to
distinguish `k = 3` from `k = 5`. Any of them is equally consistent with the
data you have. You pick one, and you say why, and the "why" has to come from
somewhere other than this dataset.

## PART 3 — MAD VS STANDARD DEVIATION (10 min)

A second choice, and a nastier one:

```text
--- detrended, k=2.0, STANDARD DEV
    spread 4.9596 (standard dev)   threshold 2.0x = 9.9191
    flagged 2: t=20(+25.5), t=45(-25.0)
    caught 2/2 real events   false positives 0
--- detrended, k=3.0, STANDARD DEV
    spread 4.9596 (standard dev)   threshold 3.0x = 14.8787
    flagged 2: t=20(+25.5), t=45(-25.0)
    caught 2/2 real events   false positives 0
```

- ☐  The standard deviation is `4.9596`; the MAD-based spread was `2.7490`.
     The standard deviation is ______ times larger
- ☐  **Why?** A standard deviation uses every residual's magnitude, so the two
     planted events at `±25` are inside the very statistic being used to judge
     them. The events are polluting their own yardstick. The name for that is
     ______

Here is the experiment that proves it rather than asserting it. I computed both
statistics twice — once on all 70 residuals, once with the two event points
**deleted**:

```text
ALL      n=70 sd=4.9596 mad=2.7490 ratio=1.804
NOEVENTS n=68 sd=2.5572 mad=2.7007 ratio=0.947
event residuals: [25.53, -25.01]
```

Read the two sd values: **`4.9596` with the events, `2.5572` without.** Removing
just two points out of seventy nearly halves the standard deviation. Those two
points alone contribute about half the variance of the whole series.

And read the two MAD values: `2.7490` → `2.7007`, a change of under 2%. The MAD
barely notices the events were there.

- ☐  So removing 2 of 70 points changes the standard deviation by ______ %
     and the MAD by ______ %
- ☐  The `sd/mad` ratio is `1.804` with the events and `0.947` without. **For
     genuinely clean symmetric noise that ratio should be about 1.0 — so what
     does the 0.947 tell you about the event-free residuals?** ______
- ☐  So with the standard deviation, even `k = 2` gives zero false positives.
     **Does that make the standard deviation the better choice?** ______

That last question is a trap and the answer is **no**, and the reason is a
timetable. With only two labelled events, those events are a large fraction of
the series, so any contaminated statistic looks fine. The MAD is preferred
because it *would still be right* when events are 1% of the data instead of 3%.
Today's data cannot tell you which is better; the robustness argument can.

- ☐  Write the honest justification: "We used the MAD because ______, and today's
     data does not demonstrate the difference because ______"

## PART 4 — TOO LITTLE DATA (8 min)

The failure that should worry you most:

```text
--- FIRST 8 POINTS ONLY, k=3, MAD
    spread 2.7341 (1.4826*MAD)   threshold 3.0x = 8.2022
    flagged 0: nothing
    caught 0/2 real events   false positives 0
```

- ☐  The spread is `2.7341`, almost identical to the full-series `2.7490`. **So
     why is the detector blind?** ______
- ☐  The threshold is `8.2022`, and the events are `±25`. **The threshold did
     not change. So what did?** ______

The answer is the most useful thing in today's lesson. **The threshold was
never small — the data being thresholded was missing.** With only 8 points there
are no events in the window at all, so there is nothing to catch, and the
detector reports "nothing" with exactly the same confidence as it would if the
series were quiet. A detector over a short window cannot tell you "nothing
happened" apart from "I was not watching."

- ☐  So what must the output contain so a reader can tell those two apart?
     ______
- ☐  Write that as a one-line requirement for your `run()`: it must report
     `n_points_seen` and ______

## TURN IN — Build Day 2 Checklist

1. `atkit.py` with the MAD-based scale estimate and a `THRESHOLD_K` constant
2. **The complete sweep** — `k = 2, 3, 4, 5` — with caught/false counts
3. The standard-deviation comparison, with the inflation factor computed
4. The short-window experiment (first 8 points) and your written diagnosis
5. A `n_points_seen` field in the output, and a stated minimum
6. Your justification for MAD over standard deviation, in two sentences
7. `test_atkit.py`: a series with no events flags nothing; a series with a
   single large spike flags exactly one point

## 🇹🇼 TAIWAN CONTEXT

Part 4 is the failure that matters most in practice, and it is a direct
consequence of how monitoring windows get chosen. A dashboard that recomputes
"normal" from the last hour, and a dashboard that recomputes from the last year,
have the same code and wildly different reliability — and when the first one goes
blank during an incident, the difference between a quiet system and a blind
system is invisible in the UI. **A detector that cannot report its own coverage
will be read as confident when it is ignorant**, and that is how alerts get
missed: not by failing, but by correctly reporting that it found nothing in a
window too small to contain the thing.

The habit worth forming: **make the sample size part of the alert.** A finding
that depends on 8 points and a finding that depends on 800 are not the same
finding, and nothing in a bare number tells you which you have. Report the count
next to the result, refuse to report below a stated minimum, and let the reader
see the difference between "quiet" and "not enough data to say."

The second locally relevant point is the MAD argument in Part 3, which is not
abstract here. Event-driven systems produce exactly the contaminated-statistics
case: the incidents you most want to detect are the ones that, once detected,
dominate the very baseline used to detect them. Locally that shows up whenever
a monthly report is generated *after* a spike month — the spike inflates the
reported average and the following month looks anomalously quiet, which is
exactly the manufactured dip discussed in the Unit 6 detector work. Median-based
statistics are the practical defence, and knowing why is worth more than
remembering that they are.

**Next:** L12, Tue May 18 — paper check, and you decide the threshold out loud
with the evidence from today on the table.
