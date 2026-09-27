# U7 L13 — Build Day 3: The False-Positive Problem, Honestly Handled

**Date:** Wednesday, May 19, 2027
**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.5 — quantify false positives, state the cost of a threshold, and make
the detector report its own coverage

---

**Laptop today.** Your parameters are committed. Today you build the reporting,
because a detector that is quietly wrong is worse than no detector.

## PART 1 — BUILD THE EVALUATION HARNESS (12 min)

The harness is the point of the day. Before any threshold argument, you need the
thing that makes arguments falsifiable.

```python
# this is a FRAGMENT: it needs seasonal_trend, mad, stdev and TRUTH from
# atkit.py, which you built on Monday. Verified against Monday's numbers.
def evaluate(series, k, use_std=False, points=None):
    """Return a dict of caught / false / total, plus the flagged list."""
    pts = points if points is not None else len(series)
    base = seasonal_trend(series)[3]
    resid = [v - b for v, b in zip(series, base)]
    spread = (stdev(resid) if use_std else 1.4826 * mad(resid))
    thresh = k * spread
    flagged = [i for i, r in enumerate(resid) if abs(r) > thresh]
    caught = sorted(TRUTH & set(flagged))
    false = sorted(set(flagged) - TRUTH)
    return {"k": k, "spread": spread, "thresh": thresh, "n_points": pts,
            "flagged": flagged, "caught": caught, "false": false}
```

- ☐  Type it, then verify it reproduces Monday's table for `k = 2` and `k = 3`.
     Does it? ______
- ☐  **Why does the harness take a `points` argument at all**, rather than
     slicing internally? ______
- ☐  Why is `caught` computed with `&` (set intersection) and `false` with `-`
     (set difference), rather than both by a loop? ______

The third is a correctness question disguised as a style question. `TRUTH &
set(flagged)` keeps only what is in both. `set(flagged) - TRUTH` keeps only what
is flagged and *not* in TRUTH. If you compute "false" as "everything flagged,
minus what was caught" with the wrong set, a point that is in TRUTH but was
*not* flagged gets counted as a false positive, and your error rate silently
rises.

## PART 2 — THE SWEEP, AND THE HONEST ARITHMETIC (12 min)

```text
--- detrended, k=2.0, MAD
    spread 2.7490 (1.4826*MAD)   threshold 2.0x = 5.4979
    flagged 4: t=20(+25.5), t=34(-5.6), t=36(+5.8), t=45(-25.0)
    caught 2/2 real events   false positives 2
--- detrended, k=3.0, MAD
    spread 2.7490 (1.4826*MAD)   threshold 3.0x = 8.2469
    flagged 2: t=20(+25.5), t=45(-25.0)
    caught 2/2 real events   false positives 0
```

- ☐  At `k = 2`, 4 points flagged of 70 total. **What fraction of all points
     is that, and is that number the right thing to report?** ______
- ☐  **It is not.** A false-positive *rate* per point is not what an operator
     cares about. An operator cares about: ______
- ☐  So report **false alerts per day**, given 70 points ≈ 70 days: at
     `k = 2` that is about ______ per day; at `k = 3`, ______
- ☐  Now the sentence for the defense: "At our threshold, a quiet week produces
     about ______ false alerts. We consider that acceptable because ______"

Two false positives in seventy days is **0.2 per day — about one false alert
every five days.** That is a genuinely cheap detector, and the blank deserves an
answer that recognises it. The honest version names a cost in a form the reader
can check: "0.2 false alerts per day means our expected false-alert burden is
about one per week, and on-call can absorb that." The dishonest version writes
"acceptable" and moves on.

Note the trap in the arithmetic here. The *count* is 2, which sounds alarming;
the *rate* is 0.2/day, which is not. Reporting the count alone either frightens
people unnecessarily or — if you round it to "0 false positives" — hides a real
number. Always convert to a rate before judging, and say which unit you used.

- ☐  What number would you state if the answer were 5 per day? ______
- ☐  At what level would you say the detector has become useless, and why is
     that not the same as the level where people stop reading it? ______

That distinction is worth having on the page. A detector that fires 50 times a
day is not *more* useless than one that fires 5 times a day — it is the same
useless, and it got there gradually, which is exactly why nobody notices the
decline. Habituation is a property of the human, not of the threshold.

## PART 3 — MAKE THE DETECTOR REPORT ITS OWN COVERAGE (12 min)

From Monday, the short-window failure:

```text
--- FIRST 8 POINTS ONLY, k=3, MAD
    spread 2.7341 (1.4826*MAD)   threshold 3.0x = 8.2022
    flagged 0: nothing
    caught 0/2 real events   false positives 0
```

- ☐  The detector prints `flagged 0: nothing` and `false positives 0`. **Read
     those as an operator would.** What do they suggest happened? ______
- ☐  What is actually true? ______
- ☐  So the output is **actively misleading**, not merely incomplete. Name the
     distinction: an output that says "nothing" when it means "I was not
     watching" is a ______ error, not a ______ one
- ☐  The fix, from Monday's paper commit: the output must include
     `n_points_seen` and ______

The missing field is a **coverage or confidence statement** — something that
says how much data backed this conclusion. "No anomalies detected in 8 points"
and "No anomalies detected in 70 points" are different claims, and the first
should not be printed in the same shape as the second.

```python
MIN_POINTS = 20
n_points = 8

if n_points < MIN_POINTS:
    print("INSUFFICIENT DATA: %d points, need %d. No conclusion drawn."
          % (n_points, MIN_POINTS))
else:
    print("no anomalies in %d points" % n_points)
```

Real output — note it does **not** say "no anomalies":

```text
INSUFFICIENT DATA: 8 points, need 20. No conclusion drawn.
```

- ☐  Choose `MIN_POINTS`. What is the argument for your number? ______
- ☐  What is the **cost** of setting it too high? ______
- ☐  And too low? ______

- ☐  **Refusal to report is a feature.** Does that connect to the `slope` guard
     in Unit 6 and the `simpson` guard in Unit 7? ______

It does, and it is the same principle three lessons running: **a wrong or
meaningless answer is worse than no answer**, and a guard that converts one into
the other is worth more than clever code around it. A detector that says "I
cannot tell" has behaved correctly. A detector that says "nothing" because it
lacked data has lied, and it lied confidently.

## PART 4 — THE SELF-CRITIQUE (9 min)

- ☐  **27.** Name one way this detector would fail on real data that it cannot
     fail on today's synthetic series: ______
- ☐  **28.** Name one way it would fail on *real* data that is not in this list
     and that you have not addressed: ______
- ☐  **29.** What data would you need to run this in production that you do not
     have? ______
- ☐  **30.** What is the single most load-bearing assumption in the whole
     pipeline? ______
- ☐  **31.** If that assumption is wrong, what does the output look like?
     ______

Question 31 is the one to get right. "A missed assumption" is a hedge; "here is
what the output looks like when it is wrong" is a diagnosis. If the day-of-week
model is wrong — a holiday, a level shift from a deploy, a new service — the
output does not go quiet, it goes **permanently biased**, and the bias will
absorb genuine events up to its own size. The detector reports "nothing" while
reporting it every single day.

## TURN IN — Build Day 3 Checklist

1. `evaluate()` in `atkit.py`, verified against Monday's numbers
2. The full sweep, with **false alerts per day** reported alongside counts
3. `MIN_POINTS` implemented, with a refusal path that prints a coverage warning
4. A test that a 5-point series produces the refusal message, not "nothing"
5. Your answers to 27–31, in writing
6. `test_atkit.py`: `evaluate` on a series containing a 25-unit spike at a known
   index returns that index in `caught`

## 🇹🇼 TAIWAN CONTEXT

The habit in Part 2 — reporting a rate an operator can act on rather than a
per-point fraction — is the difference between a threshold that can be reviewed
and one that cannot. A rate of "1.4% of points" invites no decision at all. A
rate of "about 2 false alerts per night, each requiring someone to wake up and
check" invites a real one, and locally the honest answer is usually that a
detector nobody trusts is worth less than a slightly less sensitive one. The
institutional version of this is a well-known and expensive pattern: a
high-volume alert channel gets progressively filtered until only the loudest
events remain, and the filtering is never written down anywhere.

Part 3's coverage rule has an obvious local analogue, and it is worth stating
plainly because the failure is common with **any metric that is only computed
after the fact**. A daily aggregate that is produced from a partial day looks
exactly like a complete quiet day, and the difference is invisible in the
output. Systems that get this wrong produce dashboards that are calm every
morning and alarming every evening, and the morning calm is not a fact about the
system — it is a fact about the window. Always print the sample size with the
figure, and never let a partial window be compared against a full-period
baseline. That single habit would prevent a large fraction of the "why did
nobody notice until the incident was an hour old" conversations that this unit
is really about.

**Next:** L14, Thu May 20 — paper reflection on modeling and its limits, and the
final write-up plan for Friday.
