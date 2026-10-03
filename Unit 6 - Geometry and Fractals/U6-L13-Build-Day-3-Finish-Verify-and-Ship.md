# U6 L13 — Build Day 3: Finish, Verify, and Ship

**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.6, 6.7 — finalise, verify reproducibility, and prepare a five-minute
defense

---

**Laptop today.** Tomorrow is the demo. Today is the day you stop adding
features and start proving the thing works.

## PART 1 — THE PRE-DEMO CHECKLIST (12 min)

Do these in order. Do not skip to the code.

- ☐  **Fresh clone test.** `git clone <url> /tmp/fp-check && cd /tmp/fp-check
     && python3 measure.py && python3 test_measure.py`. Output must match
     `data/results.txt` exactly
- ☐  **Manifest regenerated** and committed
- ☐  **`results.txt` in the repo is current** — not a version from Thursday
- ☐  `README.md` has all six defense questions from Friday, and the three
     sentences from Monday
- ☐  The false-positive section is still there and still names the circle and
     the noise
- ☐  Your Part 3 paragraph from yesterday is in the README
- ☐  No `TODO`, no `FIXME`, no commented-out experiments left in
     `measure.py`
- ☐  `detect.py` **imports** from `measure.py` — no copy-pasted duplicate

## PART 2 — ADD ONE TEST THAT MATTERS (12 min)

Your `test_measure.py` should prove the thing, not the code. Add these three:

- ☐  **A dimension sanity test.** `measure()` on a straight diagonal must come
     out at `1.0` within tolerance. It measured `1.0000` in the real run — is
     that exact or close? Pin the tolerance to what actually happened
- ☐  **A scale-invariance test.** The same shape at grid size 16 and 32 should
     measure the *same* dimension. Run it. Does it? Report the two numbers
- ☐  **A known-answer test.** Sierpinski depth 5 must measure `log2(3) =
     1.584963` to within `0.001`

- ☐  `python3 test_measure.py` prints `all tests passed` — paste it here:

  ______________________________________________________________________

**The second test is the interesting one and I expect it to fail or nearly
fail.** Box counting is sensitive to the grid size, and a measurement that
moves when you change the resolution is telling you something important about
the method's reliability. If your two numbers differ, that difference goes in
the README under limits. If they are identical, say so and explain why you think
that is luck rather than robustness.

## PART 3 — TIGHTEN THE DEFENSE (12 min)

Your README is a page. It must survive a hostile question. Prepare written
answers to these — I will ask at least two, and you will not be able to run
code while you answer.

1. "Your depth-5 error was `0.000000`. If the method is this good, why is it
   wrong on four of eight cases?"

   My answer: ________________________________________________________________

2. "Give me a threshold that gets all eight cases right."

   My answer: ________________________________________________________________

3. "Your Koch measurement was 1.3278, true is about 1.262. Walk me through the
   gap."

   My answer: ________________________________________________________________

4. "If I ran your detector on real network traffic, what would you expect to
   happen?"

   My answer: ________________________________________________________________

Question 2 is the one people try to bluff. **There isn't a single threshold that
gets all eight right**, because the circle and the noise score *higher* than
the true fractals. If you find a number that appears to work, you have found a
threshold that separates *these eight cases* and nothing else. Say that.

## PART 4 — THE DEMO, PLANNED (9 min)

Five minutes. Plan it:

| time | what you show | what you say |
|---|---|---|
| 0:00–0:45 | | |
| 0:45–1:30 | | |
| 1:30–3:00 | | |
| 3:00–4:00 | | |
| 4:00–5:00 | | |

- ☐  **The final slide is not your code.** It is your limits slide: the
     false-positive cases, named
- ☐  Plan to say the sentence "my detector cannot distinguish a solid circle
     from a fractal" out loud. That sentence is the project
- ☐  Plan your answer to the question you *don't* expect. Two minutes on
     "a reader should not use my detector to conclude that…" and stop

## TURN IN — Build Day 3 Checklist

1. All Part 1 items ticked, with the fresh-clone output pasted
2. Three new tests added; `all tests passed` pasted
3. Scale-invariance result reported honestly, **including if it failed**
4. Four written demo answers, all four
5. Five-minute demo plan filled in
6. Pushed to `main`, Classroom link working

## 🇹🇼 TAIWAN CONTEXT

The "a reader should not use this to conclude that" sentence is the one that
matters most in a report that leaves the building. The reason is specific and
local: in incident response the person reading your output is often someone
who has been awake for a day, reading a tool they did not build, under time
pressure. A detector that says "STRUCTURED" without saying "and also labels
solid circles as structured" will be believed. Every operational tool that
avoids harm does the same thing: it states the conditions under which its
output should not be trusted, in the output itself, not in a separate
document the reader will not open.

**Next:** L14, Thu Apr 29 — one clean reflection day after the project. Pencil.
We finish the unit by looking at what the project cost and what it bought.
