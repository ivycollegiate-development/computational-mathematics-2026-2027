# U7 L15 — Anomaly Trend Analyzer Due

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.5 — submit a detector whose thresholds, limits, and coverage are
stated

---

**Submit today.** No new build. The deliverable is an artifact and a defense,
and the grading is weighted toward the honesty of the claims rather than the
sophistication of the code.

## WHAT IS DUE

### 1. The program

- `atkit.py` with: `moving_average`, `lsq_line`, `dow_offsets`,
  `seasonal_trend`, `mad`, `stdev`, `evaluate`, and a `main` that takes a CSV
  path as an argument
- A `README` with: what it does, what it does not do, how to run it
- `test_atkit.py` with at least five tests

**Guards required** (these are graded, not optional):

| guard | behaviour required |
|---|---|
| fewer than `MIN_POINTS` points | print a coverage refusal, not "no anomalies" |
| constant series | MAD collapses to 0 and so does the threshold — see below |
| empty or single-point input | refuse with a clear message |
| `n` odd, if Simpson is used | raise, as in L05 |
| import failure | `raise SystemExit` with a human message and **no pip** |

- ☐  Confirm: does your `evaluate` print the coverage refusal? ______
- ☐  Confirm: does a near-constant series get refused rather than returning
     `threshold 0`? ______

The second one is a genuine edge case, and its real behaviour is more subtle
than "it flags everything." I ran it. On a constant series of 70 points the
residuals are **exactly** zero, the MAD is exactly `0.000000`, and the
threshold comes out `0.0`:

```text
constant series: spread mad=0.000000 sd=0.000000
all residuals zero? True
k=2 threshold -> 0.0
flagged with abs(r) > threshold: 0
```

So the strict-inequality test happens to flag **nothing** — correct by luck,
because the residuals are precisely zero and `0 > 0` is false.

- ☐  **Now consider what happens with floating-point noise instead of exact
     zeros.** A "constant" series in production is never exactly constant; it is
     constant plus `1e-16` of representation noise, the MAD becomes a tiny
     nonzero number rather than zero, the threshold becomes tiny too, and the
     comparison now depends entirely on whether residuals land above or below
     that threshold. The correct answer is not knowable from the code. ______
- ☐  So what is the robust handling? ______

The robust handling is to treat a **near-zero** spread, not just an exactly-zero
one, as a degenerate case and refuse. A MAD below some floor — say `1e-9` — means
"there is no measurable variation here," and the honest output is a statement
about the data, not a verdict. Comparing floating-point values against a
threshold that was computed from the same floating-point noise is the kind of
thing that passes in testing and reverses on someone else's machine.

**A degenerate statistic must be detected, not divided by.** And the general
point: an answer derived from a zero-scale quantity is not a confident answer,
it is an answer with no information in it.

### 2. The written defense — one page, four required statements

**a. What it detects.** What the threshold is, and in what units.

**b. What it costs.** False alerts per day, stated as a rate, and who absorbs
them.

**c. What it cannot do.** The assumption most likely to break, and what the
output looks like when it does.

**d. What would make it better.** The specific data or labelling you would need,
and which of your parameters is currently a judgement rather than a measurement.

- ☐  Which of (a)–(d) is your weakest? ______
- ☐  Can you strengthen it today? ______

### 3. The parameter table

Reproduce the one you committed to on paper in L12, with the reasons, and report
the measured outcome for each choice.

| parameter | chosen | reason | measured outcome |
|---|---|---|---|
| detrending method | | | |
| scale estimator | | | |
| `k` | | | |
| one/two-sided | | | |
| `MIN_POINTS` | | | |

## GRADING

| criterion | weight |
|---|---|
| Guards behave correctly, including the refusal paths | 25% |
| Thresholds and rates reported honestly, in checkable units | 20% |
| Limits stated before they are asked for | 20% |
| Tests that would actually fail if the code broke | 15% |
| README completeness | 10% |
| Residual structure diagnosed, not just fitted | 10% |

**On the tests, specifically.** A test suite that passes tells the reader
nothing. What matters is whether your tests *can* fail — a test that passes
against a deliberately broken version of the function is worthless, and the way
to know is to break it on purpose and watch the test fail. Do that for at least
one test and say so in the README.

- ☐  Which test did you deliberately break, and did it fail? ______
- ☐  Which test do you suspect would not fail if the code broke? ______

## SELF-CHECK BEFORE YOU SUBMIT

Run these. Each one is a way a submission gets returned.

- ☐  1. Run it on a **different CSV** than the one you developed against. Does
       it still work, or is it hardcoded to your data?
- ☐  2. Run it on a **series with no events**. Does it report zero false
       positives, and is that claim supported?
- ☐  3. Run it on a **series with one huge event**. Does it catch it?
- ☐  4. Run it on a **5-point series**. Does it refuse?
- ☐  5. Run it on a **constant series**. Does it refuse?
- ☐  6. Every number in your defense — can you reproduce it by running the
       program, right now, in front of someone?
- ☐  7. Does the README state the day-of-week assumption?
- ☐  8. Is there any `pip install` in your code? It must be zero.

Question 6 is the one that catches people. **If a number in your write-up
cannot be regenerated by running your program in front of the reader, it is not a
result, it is a memory** — and you should not defend it.

## 🇹🇼 TAIWAN CONTEXT

The self-check list is the local lesson. Points 1 and 2 are the ones that
separate a tool from a script: a detector that only works on the data it was
built against is not a detector, and the test that proves it is simply running
it on something else. Locally that means testing on a **different** site's data,
a **different** metric, or a different month — the point being to find the
assumption that was silently tuned to one series. Anything tuned to one dataset
without being labelled as such will produce confident nonsense on the next one,
and the confident part is the dangerous part.

Point 5 deserves one more line, because it recurs in local infrastructure: a
steady, boring series makes several standard statistics degenerate, and a
degenerate statistic is the one that produces an enormous, confident, entirely
wrong count of "anomalies". Any service that is genuinely healthy generates
exactly this input, so the healthy case is the one most likely to break your
detector — and it is the case nobody tests, because nothing is happening, so
nobody is looking. **Test the boring case deliberately.** A tool is not
trustworthy until it has been shown to behave sanely when there is nothing to
report.

**Next:** L16, Mon May 24 — machine day. Polish, manifest, integrity check, and
the demo script.
