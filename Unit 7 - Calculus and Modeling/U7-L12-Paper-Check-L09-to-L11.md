# U7 L12 — Paper Check: L09–L11

**Date:** Tuesday, May 18, 2027
**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.5 — defend a detrending method, a scale estimator, and a threshold,
on paper

---

**No laptop.** Pencil. Today you commit to the detector's parameters **on
paper**, with reasons, before the U7 L15 deadline. That ordering is deliberate:
the decisions are yours, the code just implements them.

## PART 1 — RECALL THE NUMBERS (12 min)

From Monday, from memory, then check.

1. The two planted event times: ______ , and their signed magnitudes: ______
2. The detrended MAD spread: ______
3. The raw-series MAD spread: ______
4. The ratio between those two spreads: ______
5. At `k = 2`, which two points are false positives? ______
6. At `k = 3, 4, 5`, how many points are flagged? ______
7. The standard-deviation spread: ______
8. The spread with the two events deleted: ______
9. The `sd/mad` ratio with events, and without: ______
10. The first-8-points experiment: how many events caught? ______
11. The pure-sine `sd` from L09: ______
12. The recovered trend per day: ______ (built-in value: ______)

- ☐  Score: ______ / 12
- ☐  Question 8 is the one that matters most. If you cannot recall it, you have
     not absorbed **why** the MAD is used rather than the standard deviation.

## PART 2 — DEFEND THE DETRENDING CHOICE (12 min)

13. Name two methods for establishing a baseline: ______ , ______
14. Why does a 7-day moving average fail on this data? ______
15. What specifically is the `8.4438` from L09 measuring? ______
16. So the day-of-week method is better because ______
17. What does the day-of-week method **assume** that a moving average does not?
     ______
18. Give one real situation where assumption 17 fails: ______

Question 15 has a precise answer and it is worth writing exactly: the `8.4438`
is the standard deviation of a **pure sine** after a centred 7-day average, and
it is dominated by the handful of **boundary days** where the window is
one-sided and does lag. It is not evidence that the interior residuals are large
— L09's Part 2 shows interior residuals under 5.

- ☐  So the general lesson is: **a global statistic computed over a series with
     defective edges is partly measuring the defect.** State that as a rule you
     will follow: ______

## PART 3 — COMMIT TO YOUR PARAMETERS (14 min)

This is the deliverable. Write these down as final answers, with a one-line
reason each. You will use them Friday.

| parameter | my choice | reason (one line) |
|---|---|---|
| detrending method | | |
| scale estimator | | |
| `k` | | |
| one-sided or two-sided | | |
| minimum points to report | | |

- ☐  **19.** For `k`, you know `k=3`, `k=4`, and `k=5` all give identical flags
     on this data. So what is your *actual* basis for choosing? ______
- ☐  **20.** Write the sentence that goes in the defense, filling in your number:
     "We set the threshold at ______ times the MAD-based spread, giving
     ______, which flags ______ of our 2 labelled events with ______ false
     positives. The choice of ______ is not determined by this dataset — the
     data cannot distinguish it from alternatives — so we chose it because
     ______"
- ☐  **21.** What would you need in order to choose `k` on evidence rather than
     argument? ______
- ☐  **22.** And if you could not get that, what is the honest fallback? ______

Questions 19 through 22 are the honest core of the project. The data genuinely
cannot tell you whether `k = 3` is right; it can only tell you it is
*consistent*. Being able to state that a parameter is a judgement rather than a
measurement — and to say what would make it a measurement — is the difference
between a threshold you own and a threshold you copied.

- ☐  **23.** From L09's Part 3: the detector was blind on 8 points. What must
     your output print so a reader can tell "quiet" from "not enough data"?
     ______

## PART 4 — ERROR LOG (7 min)

- ☐  All errors from Parts 1 through 3
- ☐  Tags: **edge effects**, **contaminated statistic**, **coverage**,
     **judgement call**
- ☐  Newest tag, defined in your own words: ______
- ☐  Which of today's numbers would you want a *test* on, rather than a
     comment about? ______

## 🇹🇼 TAIWAN CONTEXT

Part 3.20 is where a threshold stops being a number and becomes a commitment, and
the discipline to say "this is a judgement, here is why" is worth more locally
than the number itself. Monitoring thresholds in local operations are very
often inherited rather than chosen — set once by whoever built the dashboard,
carried forward for years, never revisited, and defended in a review with "that
is what the system uses." The review question that actually helps is not "why
is it 3?" but "what was true when you picked it, and is it still true?" That is
the sentence in Part 3.20, and it is the one that turns a constant into a
defensible choice.

The coverage point in 23 is the locally dangerous one, and it has a direct
analogue in capacity reporting. Reports generated over a short window — "today so
far", a partial month, a rolling 24 hours — get read as complete, and a partial
period that looks calm is one of the most common reasons a degradation window
goes unnoticed. The reporting rule that follows from Part 4 is simple and worth
adopting: **every windowed figure states its own sample size, and refuses to
compare against a full-period baseline when it is materially short.** A number
without its denominator is not a measurement; it is a feeling.

**Next:** L13, Wed May 19 — laptop. The false-positive problem, handled
honestly, using the parameters you committed to on paper.
