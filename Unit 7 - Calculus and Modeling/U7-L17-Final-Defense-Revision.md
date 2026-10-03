# U7 L17 — Final Defense Revision

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.5 — rehearse and tighten a five-minute technical defense

---

**No laptop.** Pencil. The talk is written, not improvised. Bring your draft.

## PART 1 — WRITE THE TALK, ALL FIVE MINUTES (18 min)

Five sections, with a word budget. 5 minutes ≈ 650 spoken words at a calm pace.
Budget accordingly.

| # | section | words | your draft |
|---|---|---|---|
| 1 | Opening claim | 70 | |
| 2 | How it works (2 sentences) | 110 | |
| 3 | The numbers | 150 | |
| 4 | **Limits** | 180 | |
| 5 | What I'd need next | 140 | |
| | **total** | **650** | |

- ☐  Section 1, in one sentence: what does it do? ______
- ☐  Section 2: name the two model components. ______
- ☐  Section 3: threshold, caught, false-alerts-per-day. All three. ______
- ☐  Section 4: the assumption most likely to break, and the output shape when
     it does. ______
- ☐  Section 5: the data you lack. ______
- ☐  **Actual word count of your draft: ______**

## PART 2 — CUT IT (12 min)

Your draft is too long. Everyone's is. Cut to 500 words and see what survives.

- ☐  Which two sentences can go entirely, and why those two? ______
- ☐  Section 2 was budgeted 110 words. **What is the shortest honest way to
     explain detrending?** ______
- ☐  Section 4 is 180 words and is the one you are most tempted to shorten to 40.
     **Resist.** Why? ______
- ☐  After cutting, word count: ______
- ☐  What did you keep that you had expected to cut? ______

The last question has a predictable answer: you keep the limits. That is correct,
and it is the last time I will tell you so — you should be able to defend the
choice without me.

## PART 3 — THE HOSTILE QUESTIONS (10 min)

Answer these in writing, briefly. Each one is a real question that gets asked.

**Q1. "You planted the events. So you tested against the answer key. Isn't that
circular?"**

- ☐  My answer: ______

**Q2. "Your threshold of 3 was chosen by argument, not by the data. Why should I
believe it?"**

- ☐  My answer: ______

**Q3. "Your detector found nothing on 8 points. How do I know it isn't broken?"**

- ☐  My answer: ______

**Q4. "What happens on a series with a step change in level?"**

- ☐  My answer: ______

**Q5. "Would this work on a metric with a different shape?"**

- ☐  My answer: ______

Q1 and Q2 are the ones that matter, and the good answer to both is the same
shape: **yes, and here is exactly what that does and does not license me to
claim.** Conceding the circularity while stating what remains valid is far more
persuasive than defending the method as though the test were independent. The
reader is checking whether you know the difference between "the program works on
data where I knew the answer" and "the program works." Naming the first is what
buys you credibility for the rest.

- ☐  Which of the five was hardest to answer honestly? ______
- ☐  Did any answer require you to admit a real limit? ______

## PART 4 — ERROR LOG (5 min)

- ☐  Record slips
- ☐  Tags: **verbosity**, **overclaiming**, **hostile question**
- ☐  Newest tag: ______

## 🇹🇼 TAIWAN CONTEXT

Q3 is not an academic question, and locally it is the one that most often gets
the honest answer **omitted**. Any locally deployed monitor that reports "no
anomalies" during a window too short to contain a meaningful signal is
technically correct and operationally misleading, and the habit of printing the
sample size next to the verdict is the difference between a monitor people trust
and one they learn to refresh without reading. If you are asked how you would
detect a broken monitor, the answer that lands well is concrete: **it reports
its own coverage, it refuses below a minimum, and it has a test that asserts the
refusal fires.** A monitor that cannot tell you it is blind is not a monitor
someone can rely on at 3am.

Q5 is worth preparing for a local reason specifically. Metrics here span
request counts, latency in milliseconds, temperatures, byte counts, and
percentage utilisations, and a detector tuned on a symmetric, roughly-Gaussian
metric does not transfer to a heavily right-skewed one. The MAD survives that
transfer better than a standard deviation does — which is, if you think about
it, exactly the same argument you made in L11 and it is worth connecting the two
places where it applies. A percentage metric bounded above and below behaves
differently again, and the honest answer is that the pipeline would need the
metric's distribution checked before its threshold was trusted.

**Next:** L18, Wed May 26 — paper. Demo prep: the five-minute talk, dry run.
