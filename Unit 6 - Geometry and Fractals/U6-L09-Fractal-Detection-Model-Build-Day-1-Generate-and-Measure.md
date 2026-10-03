# U6 L09 — Fractal Detection Model, Build Day 1: Generate and Measure

**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.6 — generate fractal structures and measure their dimension by box
counting, and verify the measurement against a known answer

---

**Laptop today.** Project work begins.

## THE PROJECT

**Fractal Detection Models** — build a program that measures how "fractal" a
structure is, and defend the limits of what your number means.

| milestone | when |
|---|---|
| generate + measure | Thu Apr 22 (today) |
| **due** | **Fri Apr 23, 11:59 PM** |
| build day 2: the detector, and its false positives | Mon Apr 26 |
| build day 3: finish, manifest, defense | Wed Apr 28 |
| **demo** | **Fri Apr 30** |

The deliverable is a program plus a one-page defense. Today is the *measurement*
half. The honest half.

## PART 1 — THE TRUTH IS EXACT HERE (12 min)

For the Koch curve, the arithmetic is exact if you use `fractions.Fraction`
instead of floats. Run this:

```python
from fractions import Fraction

def koch_table(n_max=6):
    seg = Fraction(1)
    rows = []
    for n in range(0, n_max + 1):
        total = seg * (4 ** n)
        rows.append((n, 4 ** n, seg, total))
        seg = seg / 3
    return rows

def show_koch():
    print("Koch side: start from one segment of length 1")
    print(" n   segments   segment length        perimeter    x previous")
    prev = None
    for n, count, seg, total in koch_table(6):
        x = "-" if prev is None else f"{float(total / prev):.6f}"
        print(f"{n:2d}   {count:8d}   {str(seg):16s}   {str(total):14s}   {x:>9s}")
        prev = total
    last = koch_table(6)[-1][3]
    print(f"  at n = 6 the perimeter is only {last}")
    print("  but every step multiplies it by 4/3, so the limit is infinite.")
    print("  area, by contrast, is bounded: it converges.")

show_koch()
```

Real output:

```text
Koch side: start from one segment of length 1
 n   segments   segment length        perimeter    x previous
 0          1   1                  1                        -
 1          4   1/3                4/3               1.333333
 2         16   1/9                16/9              1.333333
 3         64   1/27               64/27             1.333333
 4        256   1/81               256/81            1.333333
 5       1024   1/243              1024/243          1.333333
 6       4096   1/729              4096/729          1.333333
  at n = 6 the perimeter is only 4096/729
  but every step multiplies it by 4/3, so the limit is infinite.
  area, by contrast, is bounded: it converges.
```

- ☐  Read the `x previous` column. It is **1.333333 every single time.** What
     does that constant multiplier tell you about the limit? ______
- ☐  `4/3 > 1` and it is applied forever. So what happens to the perimeter?
     ______
- ☐  Why did I use `Fraction` instead of `1/3` as a float? ______

The last one matters: `0.333...` is not representable in binary, so a float
`seg = seg / 3` accumulates error that *looks* like the numbers drifting. Using
`Fraction` means the only numbers in the table are the true ones, and any
disagreement with theory is a bug in my reasoning rather than rounding. **You
cannot debug a model whose inputs are already wrong.**

## PART 2 — THE OTHER HALF: BOUNDED AREA (10 min)

The same fractal, same code, area instead of perimeter:

```text
  after 0 bumps: area = 0.2500000000
  after 1 bumps: area = 0.2500000000
  after 2 bumps: area = 0.3333333333
  after 3 bumps: area = 0.3796296296
  after 4 bumps: area = 0.4012345679
  after 5 bumps: area = 0.4109510745
  after 6 bumps: area = 0.4152822232
  the series converges. perimeter diverges, area does not.
```

- ☐  Perimeter diverges, area converges. Both are true of the *same object*.
     How? ______
- ☐  The gaps between successive areas: 0, 0.0833, 0.0463, 0.0216, 0.0097,
     0.0043. What is happening to them, and what does that imply? ______
- ☐  **This is the intuition you need for the project:** a fractal boundary can
     be "infinitely long" while the region it encloses stays small. A detector
     that measures boundary length will blow up on a fractal. One that measures
     *area* will not. Which do you want, and why? ______

## PART 3 — BOX COUNTING, THE MEASUREMENT (15 min)

Now measure instead of assume. Box counting: cover the shape with `k × k` boxes,
count how many are non-empty, and watch how that count grows with `k`.

```text
Sierpinski triangle: filled cells inside the bounding square
 depth    filled      side       filled/side^2    log2(side)   depth*log2(3)
    0          1         1         1.000000       0.0000          0.0000
    1          3         2         0.750000       1.0000          1.5850
    2          9         4         0.562500       2.0000          3.1699
    3         27         8         0.421875       3.0000          4.7549
    4         81        16         0.316406       4.0000          6.3399
    5        243        32         0.237305       5.0000          7.9248
    6        729        64         0.177979       6.0000          9.5098
    7       2187       128         0.133484       7.0000         11.0947
    8       6561       256         0.100113       8.0000         12.6797
```

- ☐  The `filled` column is `3^depth`. Confirm at depth 8: ______
- ☐  The `filled/side^2` column is **falling**. What does that mean about the
     fraction of the square the triangle occupies as it gets finer? ______
- ☐  Predict: at depth 20, will that fraction approach zero, or settle at some
     positive number? ______

**It approaches zero.** The Sierpinski triangle has *zero area*. You can see it
coming in the last column of the table.

## PART 4 — THE DIMENSION ITSELF (8 min)

```text
box counting, depth-5 Sierpinski in a 32x32 grid
  box size   2  ->      3 non-empty boxes
  box size   4  ->      9 non-empty boxes
  box size   8  ->     27 non-empty boxes
  box size  16  ->     81 non-empty boxes
  box size  32  ->    243 non-empty boxes

measured dimension  = 1.584963
true log2(3)        = 1.584963
absolute error      = 0.000000
```

Count the non-empty boxes: 3, 9, 27, 81, 243. Each is **3× the last**, because
each doubling of box size is one halving of the grid.

- ☐  The dimension is `log(3) / log(2)` = ______
- ☐  Why is the error exactly `0.000000` here, when real measurements are
     never that clean? ______

The last one is the honest caveat: this is a **self-similar integer** case with
no noise. Monday you will measure things that are not clean at all, and the
error will not be zero. **Do not report this number as if it were typical.**

## TURN IN — Build Day 1 Checklist

1. `fractal_project/` repo, public, default branch `main`, linked in Classroom
2. `generate.py` — produces the Koch table and the Sierpinski cell set
3. `measure.py` — box counting, with the least-squares slope, written from
   scratch (no library fit)
4. Real output pasted for all four tables in this lesson
5. A `README` stub with the project name and one sentence on what it does
6. **One sentence in the README stating where your measurement is exact and
   where it is not.** This is the seed of the whole defense.

## 🇹🇼 TAIWAN CONTEXT

The self-similar-pattern intuition is not decoration in this field. Network
traffic from a single scanner, or from a bot that has found one working path and
replays it, produces address and timing patterns that are *measurably*
self-similar at a short scale even though nothing about the scan is random. That
is why entropy- and dimension-based measures appear in traffic analysis: a
pattern that repeats at every scale is a pattern, and a random one is not. The
caution from today applies directly — a measure that is exact on a lattice test
case will be considerably less tidy on a real capture, and a detector tuned on
the tidy case will over-fire on the real one. That is the U6 L10 lesson.
