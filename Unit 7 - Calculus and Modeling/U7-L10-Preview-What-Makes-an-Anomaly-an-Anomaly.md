# U7 L10 — Preview: What Makes an Anomaly an Anomaly

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.5 — state the definition of an anomaly precisely enough to implement

---

**No laptop.** Pencil. Monday builds the detector; today you decide what it will
look for, on paper, before any of it is written.

## PART 1 — FOUR DEFINITIONS, FOUR DIFFERENT DETECTORS (15 min)

Anomaly detection has no single definition, and picking one *is* the design
decision. For each definition: say what it flags, and say what it would miss.

**D1. "Far from the mean."** Something whose value differs from the mean by a
lot.
- ☐  Flags: ______
- ☐  **Misses:** ______
- ☐  If the series has a strong trend, does this work at all? ______

**D2. "Far from the recent past."** A big change from a short window.
- ☐  Flags: ______
- ☐  **Misses:** ______
- ☐  The "recent" window is a parameter. What happens if it is too short vs too
     long? ______

**D3. "Unusual for this day of the week, at this level of trend."** The
residual after removing both.
- ☐  Flags: ______
- ☐  **Misses:** ______
- ☐  This is the definition your project uses. Why does it need the most work
     to implement, and is the extra work worth it? ______

**D4. "Unusual in a way that was not predicted."** A residual from a full model
of the expected series.
- ☐  Flags: ______
- ☐  **Misses:** ______
- ☐  Is D4 meaningfully better than D3, or just more code? ______

The D1 answer to "misses" is the important one: a mean-based detector is
**defeated by a trend**. If the series climbs steadily, the mean sits in the
middle of the historical range and the *recent* points are far from it — so a
normal, healthy, growing system flags constantly, while a single catastrophic
dip to a value typical of six months ago looks unremarkable. This is a real
failure mode, not a hypothetical one.

- ☐  So is D1 ever the right choice? Give a case where it is: ______
- ☐  And what is the cost of choosing it? ______

## PART 2 — WHAT MAKES A THRESHOLD DEFENSIBLE (12 min)

Write down the words you will use in the U7 L11 defense. This is the deliverable.

7. A threshold is defensible when it is set relative to ______ and reviewed
   against ______
8. Why is a hardcoded absolute number — say "alert above 80 requests" — a
   weak threshold? Give **two** reasons: ______
9. Why is a percentage-of-the-mean threshold also weak? ______
10. What are the two numbers that must appear in the **same sentence** to
    defend a threshold? ______
11. Name the quantity that tells you how often the detector fires on
    uneventful data. ______
12. Name the quantity that tells you how often it fails on real events.
     ______
13. Can you choose the first without knowing the second? ______

Question 13's honest answer is **no**, and that is uncomfortable. You cannot
tune a threshold for precision without a labelled sample telling you what the
recalled events look like. In this project you get to cheat — you planted the
two events, so you know where they are. Say that explicitly in the defense:

- ☐  "Our threshold was tuned against a **labelled** sample of two known
     events. On unlabelled production data we would not have this, and the
     threshold would have to be chosen on a stated assumption instead. That
     assumption is: ______"
- ☐  Is that a weakness or a strength of the writeup? ______

It is a strength, and the framing is the point: **stating the basis of a
threshold is what makes it a choice rather than a constant.** The failure mode
is not a tuned number; it is a tuned number nobody can account for.

## PART 3 — THE TWO-SIDED PROBLEM (12 min)

14. Our two planted events are `+25.5` and `−25.0`. **Should a detector fire on
     both?** A traffic spike and a traffic collapse are both worth knowing
     about — but argue it: ______
15. What if a business only cares about capacity, and a collapse means
     "server down, we already know"? What does one-sided detection cost you,
     and what is the risk of it? ______
16. Name the two ways to handle this in code, and pick one: ______
17. You choose `k = 3`. Your detector fires on nothing. **What did you just
     learn about the data, and what did you possibly break?** ______
18. The same detector at `k = 2` fires on 4 points, of which 2 are false. **Name
     the trade you are making in one word.** ______

Question 18 is the whole unit in one word: **sensitivity**. You can have recall
or precision; you cannot have both for free; and every threshold is a purchase
with both prices on the receipt. The honest defense of a threshold states which
one you bought and what you gave up.

- ☐  Which error is worse in a monitoring system you must trust — a missed
     event, or a false alarm? Defend it in one sentence: ______
- ☐  Does your answer change if the alert has been firing 40 times a day for a
     month? ______

That last one is the real-world answer and it is yes. A detector that is too
sensitive does not merely add noise; it **teaches the humans to ignore it**, and
that habit persists after the noise is fixed. Which of the two errors is worse
depends entirely on whether anyone is still reading the output.

## PART 4 — ERROR LOG (6 min)

- ☐  Record slips
- ☐  Tags: **definition**, **threshold**, **sensitivity**, **one-sided**
- ☐  Newest tag: ______

## 🇹🇼 TAIWAN CONTEXT

The two-sided question in Part 3 is not academic locally, and the asymmetry is
sharp. Service capacity planning cares overwhelmingly about the **upward**
direction — sustained or burst overage is what saturates links, fills queues, and
degrades users. The downward direction matters for a much smaller set of
reasons: a sudden drop usually means a partial outage, a misrouted path, or a
sensor that has failed rather than a quiet system.

So a defensible one-sided design here is usually **asymmetric thresholds**: fire
on a smaller upward deviation than downward. A drop of 25 units and a rise of 25
units are the same magnitude and should not get the same priority. If you are
building anything real, encode the direction into the threshold rather than
defaulting to symmetry, and state in the defense which direction you weighted
and why. A symmetric threshold is a decision, and if you make it by not
deciding, you have made one.

The second locally relevant point is question 17, and it has bitten real
deployments: the habit of raising a threshold until an alert stops firing is
extremely common and almost never written down. When the alert goes quiet,
nobody records whether that was because the problem was solved or because the
sensitivity was destroyed. **Every threshold change needs a line in the
changelog with a reason**, and "it was firing too much" is not a sufficient
reason, because it does not distinguish a bad model from a bad threshold.

**Next:** L11, Mon May 17 — laptop. The detector exists, and now you find out
what it costs when it is wrong.
