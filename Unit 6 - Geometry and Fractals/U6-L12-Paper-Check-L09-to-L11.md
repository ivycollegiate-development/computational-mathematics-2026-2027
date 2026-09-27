# U6 L12 — Paper Check: L09–L11

**Date:** Tuesday, April 27, 2027
**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.6, 6.7 — defend a measurement's limits, and defend a threshold choice

---

**No laptop.** Pencil. Yesterday's eight-case table is the subject of the
lesson, and you will write a defense of your threshold today that goes into the
project README.

Three days ago you measured a dimension. Yesterday you thresholded it and it
was wrong on four of eight cases. Today you write down what that means.

## PART 1 — RECALL THE MEASUREMENT (10 min)

From Thursday, complete from memory, then check against your own `results.txt`.

1. Koch perimeter at `n = 3`: ______ segments, each of length ______,
   perimeter ______
2. The multiplier from one step to the next: ______
3. So the perimeter, in the limit, is: ______
4. Koch area, in the limit: ______
5. Sierpinski filled cells at depth 5: ______
6. Sierpinski `filled/side²` at depth 5: ______
7. Sierpinski true dimension `log2(3)`: ______
8. Your measured dimension at depth 5: ______
9. Absolute error: ______

- ☐  All nine right? ______ / 9
- ☐  Questions 3 and 4 are the contrast that the whole project rests on. State
     in one sentence why a shape can have one of those and not the other:
     ______

## PART 2 — THE FIGHT: WHICH ROW WAS CORRECT? (15 min)

Yesterday's table:

| case | measured | verdict at 1.2 | your call on whether that verdict was right |
|---|---|---|---|
| Sierpinski depth 5 | 1.5850 | FRACTAL | |
| Koch depth 3 | 1.3067 | FRACTAL | |
| Koch depth 4 | 1.3278 | FRACTAL | |
| solid circle | 1.7891 | FRACTAL | |
| thick diagonal | 1.0000 | not fractal | |
| random noise 30% | 1.6531 | FRACTAL | |
| random noise 55% | 1.8127 | FRACTAL | |
| sparse dots 2% | 0.4590 | not fractal | |

Mark each row **correct**, **false positive**, or **false negative**, and justify
the two you most expect to be argued about.

- ☐  The circle's 1.79 — the real answer is: ______
- ☐  The 30% noise's 1.65 — the real answer is: ______
- ☐  **Which misclassification is worse for a security detector, and why?**
     ______
- ☐  The sparse-dots row scored 0.459. Is that "not fractal" for the right
     reason, or for a reason that would embarrass you in a defense? ______

The last one is a trap and it is a fair one. A threshold caught it — but only
because 0.459 is far from 1.2. If those dots had been denser, the same case
would have been called fractal. **Being right for the wrong reason is not being
right.**

## PART 3 — DEFEND YOUR THRESHOLD (12 min)

Pick one number and write the paragraph. Three sentences minimum, and it goes
in the README nearly verbatim.

> I set the threshold at ______ . At that value, my detector correctly
> classifies ______ of my 8 cases, and misclassifies ______ . I chose it over
> the alternative of ______ because ______ . A reader should not use my
> detector to conclude that ______ , because ______ .

- ☐  My paragraph: ______

Now the harder one, and it is the sentence that separates a good submission
from a complete one:

> The **one** case where my detector is most likely to be wrong on real input
> is ______ , because ______ .

- ☐  My sentence: ______

## PART 4 — ERROR LOG (8 min)

- ☐  Every error from Parts 1 and 2 into the **Geometry Error Log**
- ☐  Tag each: **measurement**, **threshold**, **reasoning**, **recall**,
     **careless**
- ☐  Newest tag, and what it means: ______
- ☐  How many errors were **recall** (things you could not reproduce without
     notes)? ______
- ☐  That number is the one to watch. Recall you had yesterday is recall you
     keep.

## 🇹🇼 TAIWAN CONTEXT

Part 3 is a template worth keeping for any detection tool you ever build or
evaluate. The paragraph's structure — the threshold, the counts at that
threshold, the rejected alternative and why, and the explicit statement of what
a reader must **not** conclude — is what separates a report an engineer can act
on from a report that merely produces numbers. In practice the sentence people
skip is the last one, the "do not conclude that", and that is the one a reader
most needs, because the reader is usually an operator who will take your
threshold at face value and has no way to discover your false-positive cases for
themselves.

**Next:** L13, Wed Apr 28 — build day 3. Finish, tighten the defense, generate
the manifest. Tomorrow is the demo.
