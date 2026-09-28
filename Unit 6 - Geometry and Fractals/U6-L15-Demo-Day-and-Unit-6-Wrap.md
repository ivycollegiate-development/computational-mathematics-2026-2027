# U6 L15 — Demo Day and Unit 6 Wrap

**Date:** Friday, April 30, 2027
**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.7 — present a measurement, its limits, and defend them under question

---

**Laptop today.** Demos, then the unit closes.

## PART 1 — DEMOS (30 min)

Five minutes each, in order. Laptop, projector, live code.

**Your five minutes:**

| time | content |
|---|---|
| 0:00–0:45 | What the program computes, in one sentence |
| 0:45–1:30 | The generation: Koch table, Sierpinski cells |
| 1:30–3:00 | The measurement: box counting, live, with the real output |
| 3:00–4:00 | **The limits slide.** The four misclassifications, named out loud |
| 4:00–5:00 | Your question I did not expect |

**Rules, and they are not negotiable:**

- ☐  Run it live. If it crashes, that is part of the demo and you handle it in
     front of us
- ☐  **The limits slide is not optional and cannot be cut for time.** Four
     minutes of content, one of limits
- ☐  The sentence "my detector cannot distinguish a solid circle from a
     fractal" gets said out loud, in those words
- ☐  Questions get real answers, including "I don't know, and here's what I'd
     check"

## PART 2 — THE QUESTION ROUND (10 min)

I will ask two questions per student from the four prepared on Wednesday. The
ones that trip people up:

**"Your error was 0.000000. If the method is that good, why is it wrong on four
of eight cases?"**

The answer is that `0.000000` is a statement about a self-similar integer case
with no noise and no boundary. It is a *test case* being exact, not the method
being exact. The method is exact on the Sierpinski lattice and approximate
everywhere else, and the four failures are all cases where the method's
assumptions do not hold.

**"Give me a threshold that gets all eight cases right."**

There isn't one, and saying so clearly is the strongest answer available. The
circle and the noise score *higher* than either true fractal, so any threshold
low enough to catch the circle catches the noise. If you have found a number
that appears to work on these eight, it separates *these eight* and nothing
else — and proving that is the actual answer.

## PART 3 — UNIT 6 WRAP (5 min)

- ☐  **The unit's one idea**, in your own words, one sentence: ______
- ☐  **The skill you gained:** ______
- ☐  **The habit you gained:** ______
- ☐  **The number you now check twice** that you used not to: ______
- ☐  One question you still have, written down so I can answer it: ______

## UNIT 6 — FINAL GRADE

| component | due | weight |
|---|---|---|
| Paper checks L02, L04, L08, L12, L14 | as scheduled | 20% |
| Prediction audits (honesty scored) | as scheduled | 10% |
| Geometry Error Log, complete | Fri Apr 30 | 10% |
| Fractal Detection Models project | Fri Apr 23 | 45% |
| Demo | Fri Apr 30 | 15% |

**On the project and the demo:** the marks are not for a number that looks
right. They are for a number that is right, a stated limit that is the real
limit, and the discipline to put the false positives in the README where the
reader can see them. A project with a clean-looking detector and a hidden
false-positive table scores lower than a messy project that publishes its own
failures. I have graded enough of both to know the difference.

## WHERE UNIT 6 GOES NEXT

Unit 7 opens Monday, and it is a different subject wearing the same clothes.

Everything in Unit 6 was about **measuring a shape that already exists**. Unit 7
is about **fitting a curve to data that already exists, and then predicting what
comes next** — numerical derivatives, numerical integration, least-squares
regression, and then the hard part: knowing when your fit has stopped
describing the data and started describing your model.

The connection is direct and you will use it. **Fitting a straight line to
scattered data and measuring its residual pattern is the same arithmetic as
box counting**, and the failure modes rhyme exactly. A line fit whose residuals
alternate in sign is telling you the model is wrong in a structured way — just
as a circle measuring 1.79 was telling you box counting was wrong in a
structured way. **Read your residuals.** That is the sentence.

## 🇹🇼 TAIWAN CONTEXT

One last thing, and it is worth carrying out of this unit.

Fractal and self-similarity reasoning shows up in Taiwanese infrastructure work
in a specific and practical way: the same measurement idea is used on network
traffic baselines, where a daily or weekly rhythm in traffic is *self-similar
at a short scale* and therefore reads as "structured" under a naive measure
while being completely normal. A detector tuned on a synthetic fractal, with no
seasonality in its training data, will over-fire on every real weekday rhythm
in the country. **A model calibrated on a pattern that does not occur in the
wild produces confident nonsense.** Say that sentence out loud at your demo if
there is room. It is the most practical thing in the unit, and it sets up
the U7 L01 lesson better than any transition I could write.

Unit 7 begins Monday, May 3. Bring your laptop, your error log, and your
project defense. We start with derivatives you cannot take by hand, on purpose.
