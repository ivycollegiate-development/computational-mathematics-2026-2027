# U6 L11 — Build Day 2: The Detector, and Its False Positives

**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.7 — apply a measured threshold to classify inputs, and demonstrate
that the threshold produces false positives

---

**Laptop today.** This is the most important day in the unit. Everything before
it was measurement. Today you make a decision, and the decision is wrong in an
instructive way.

## PART 1 — THE DETECTOR (12 min)

Take the box-counting dimension and threshold it. That is the entire detector.

```python
import math
import random

def sierpinski_cells(depth):
    cells = {(0, 0)}
    for _ in range(depth):
        nxt = set()
        for (r, c) in cells:
            for dr, dc in ((0, 0), (0, 1), (1, 0)):
                nxt.add((r * 2 + dr, c * 2 + dc))
        cells = nxt
    return cells

def measure(cells, n, boxes=(2, 4, 8, 16, 32)):
    hit_by = []
    for k in boxes:
        if k > n:
            continue
        hit = set()
        for (r, c) in cells:
            hit.add((r * k // n, c * k // n))
        hit_by.append((k, len(hit)))
    xs = [math.log(k) for k, _ in hit_by]
    ys = [math.log(v) for _, v in hit_by]
    m = len(xs)
    mx, my = sum(xs) / m, sum(ys) / m
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = sum((a - mx) ** 2 for a in xs)
    return num / den, hit_by
```

Note the sign convention: I regress `log(N)` on `log(k)`, both increasing, so
the slope comes out **positive** for a dimension. In U6 L10 I briefly had it
negative because I regressed on `log(1/k)`. Same data, same regression, sign
flipped by the axis convention. **That is worth a paragraph in your defense.**

- ☐  You typed it
- ☐  You can explain why `hit.add` uses `//` and not `/`

## PART 2 — RUN IT ON EVERYTHING (15 min)

Here is the real output, and I am not going to editorialise yet:

```text
box-counting dimension, threshold = 1.2
true dimensions: Sierpinski 1.585, Koch 1.262, circle 1.000, line 1.000

 case                  cells   measured   verdict
 Sierpinski depth 5       243      1.5850   FRACTAL
 Koch depth 3              79      1.3067   FRACTAL
 Koch depth 4              85      1.3278   FRACTAL
 solid circle             616      1.7891   FRACTAL
 thick diagonal            32      1.0000   not fractal
 random noise 30%         343      1.6531   FRACTAL
 random noise 55%         547      1.8127   FRACTAL
 sparse dots 2%           17      0.4590   not fractal
```

Now sit with that table for a minute before reading on. **A solid circle scored
1.79 and was called a fractal. Random noise scored 1.65 and was called a
fractal.** The detector's two cleanest true positives are not even its most
striking results.

- ☐  The circle is a **smooth** shape. Its true dimension is 1.0. Why did it
     measure 1.79? ______
- ☐  The 30% noise has no structure at all. Why did it measure 1.65? ______
- ☐  Koch scored 1.31–1.33, and its true dimension is about 1.26. Is that
     within 0.1 of truth? Is that *good enough* for your detector? ______
- ☐  Which of the eight rows would you defend as a **correct** classification?
     ______

The circle answer is the box-counting failure mode: a filled disc of 616 cells in
a 32×32 grid touches a lot of boxes at every scale, and the least-squares slope
picks up the **edge effect** — the boundary runs along box edges differently at
different scales. A smooth shape with a hard boundary produces a high measured
dimension. That is a systematic error, not noise.

The noise answer is simpler: random scatter touches more distinct boxes at every
scale than a smooth curve does, because it has no tendency to stay in a
neighbouring box. **High measured dimension is a statement about how the shape
fills boxes, not about whether it has structure.**

## PART 3 — MAKE IT WORSE ON PURPOSE (10 min)

Now the experiment. Change `THRESHOLD` and rerun all eight cases. The full
measured values, so you can predict before you run:

| case | measured |
|---|---|
| Sierpinski depth 5 | 1.5850 |
| Koch depth 3 | 1.3067 |
| Koch depth 4 | 1.3278 |
| solid circle | 1.7891 |
| thick diagonal | 1.0000 |
| random noise 30% | 1.6531 |
| random noise 55% | 1.8127 |
| sparse dots 2% | 0.4590 |

- ☐  **`THRESHOLD = 1.05`** — which rows change verdict, compared to 1.2?
     ______
- ☐  **`THRESHOLD = 1.9`** — which rows change? ______
- ☐  At 1.9, how many rows are still called fractal? ______
- ☐  **Write down the threshold that gives the most *accurate* classification
     on these eight cases, and the one that gives the most *flattering* result
     for a fractal detector.** ______
- ☐  A threshold above 1.82 classifies nothing as a fractal. It has zero false
     positives. Is it a good detector? ______

That last one is the whole lesson. **A detector that finds nothing has no false
positives, and that is not a defence of it.** Accuracy and usefulness are
different quantities and the confusion between them is one of the most common
errors in real monitoring.

## PART 4 — WRITE IT DOWN (8 min)

Add a section to your `README.md`. Three sentences, no more:

1. My threshold is ______, chosen because ______.
2. My detector **cannot** distinguish ______ from ______. (You have the
   evidence; the table above is it.)
3. If I were deploying this, I would add ______ to reduce the false positives.

## TURN IN — Build Day 2 Checklist

1. `detect.py` committed, importing `measure.py` — not a copy of it
2. The eight-case table pasted, **with the false positives visible**
3. `THRESHOLD` run at three values, output pasted for all three
4. A **false positive section** in `README.md` naming the circle case and the
   noise case explicitly
5. Your three-sentence statement from Part 4
6. `test_measure.py` still green after all these changes

**Do not remove the false positives from your README to make the project look
better.** That edit is the single thing most likely to cost you the project.

## 🇹🇼 TAIWAN CONTEXT

This is the most directly transferable lesson in the course, so it is worth
saying plainly. Anomaly and intrusion detection systems are routinely evaluated
on a metric that rewards a high true-positive count, and the failure mode is
well documented in practice: a detector tuned to catch everything also fires on
every normal day, and the analyst tunes it down until the alerts stop. The
circle and the noise field are the two shapes that should worry you in a real
traffic baseline — a smooth diurnal rhythm (your circle) and a genuinely
random-looking high-entropy flow (your noise). Both read as "structured" under
naive box-counting measures. The published practice is to report the
false-positive rate on a *known-clean* window alongside the detection rate,
because the clean-window rate is the number an operator will actually feel, and
it is the one nobody reports unless asked.

**Next:** L12, Apr 27 — paper check on L09–L11, and you will defend your
threshold choice in writing.
