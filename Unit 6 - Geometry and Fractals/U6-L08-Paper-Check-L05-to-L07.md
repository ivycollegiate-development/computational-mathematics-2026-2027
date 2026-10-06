# U6 L08 — Paper Check: L05–L07

**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.4, 6.5 — trace recursion by hand, and audit your predictions about
depth and cost

---

**No laptop.** Pencil. U6 L07's `deco` and the U6 L09 recursion argument are the
raw material.

Today's paper day is not a break from the machine work — it is the check that
you can *read* recursion without running it, because that is the skill that
survives when the terminal is not there.

## PART 1 — TRACE IT (15 min)

Here is `deco`, the base case and the recursive call only:

```python
def deco(lo, hi, steps, cells):
    """Drop one more cell into each third, `steps` times over."""
    if steps <= 0:
        cells.append((lo, hi))
        return
    third = (hi - lo) / 3.0
    deco(lo, lo + third, steps - 1, cells)
    deco(hi - third, hi, steps - 1, cells)

cells = []
deco(0.0, 9.0, 2, cells)
print("segments drawn:", len(cells))
for lo, hi in cells:
    print("  [%5.1f, %5.1f]" % (lo, hi))
```

Real output — and note that at `steps = 2` the four segments are four
**different** cells, not duplicates:

```text
segments drawn: 4
  [  0.0,   1.0]
  [  2.0,   3.0]
  [  6.0,   7.0]
  [  8.0,   9.0]
```

Those are the first and last thirds of each of the two outer thirds — the middle
third of each is left blank, which is exactly what makes the gap pattern.

1. Trace every call for `deco(lo=0, hi=9, steps=2)`. List them in the order
   they are *entered*, with their `lo`, `hi`, and `steps`:

   | # | lo | hi | steps |
   |---|---|---|---|
   | 1 | | | |
   | 2 | | | |
   | 3 | | | |
   | 4 | | | |
   | 5 | | | |
   | 6 | | | |
   | 7 | | | |

- ☐  How many calls is that? ______
- ☐  How many of them hit the base case? ______
- ☐  For `steps = 3`, how many calls total? ______
- ☐  Write the general formula for the number of calls as a function of
     `steps`: ______

The last one is the whole point. It is `2^(steps+1) - 1`. Check yours against
the `steps=2` case: at `steps = 2` that gives 7, which should match your table.

2. Same trace for `countdown_rec(3)` from U6 L05. How many calls, and how many
   hit the base case? ______

- ☐  `countdown_rec` makes `n+1` calls. `deco` makes `2^(s+1) - 1`. Which one
     grows catastrophically, and what is the practical consequence for a
     detector that runs on a large input? ______

## PART 2 — PREDICT THE PICTURE (12 min)

Without running anything, sketch (or describe precisely) what each produces at
the stated depth. Words are fine; "a line from x=0 rising to about y=1, with
the top quarter blank" is a better answer than a bad drawing.

3. `plot(c, lambda t: t*t, 0, 1, 1)` — one level. What is drawn, and what is
   *not*? ______
4. `plot(c, lambda t: t*t, 0, 1, 5)` — the one from U6 L07. Which part of the
   curve is best resolved? ______
5. `plot(c, math.sin, 0, 6.28, 5)` — name the part of the plot that the U6 L07
   output failed to resolve: ______
6. `plot(c, lambda t: abs(math.sin(3*math.pi*t)), 0, 1, 5)` — how many arches
     do you see, and why that number? ______

- ☐  Question 6 is the important one. The number of arches is a *property of
     the function*, and it is the same property that makes the picture
     self-similar. State the connection in one sentence: ______

## PART 3 — PREDICTION AUDIT (8 min)

- ☐  In U6 L07 you predicted what increasing `steps` would do. Did it do that?
     ______
- ☐  A prediction I got wrong: ______ because ______
- ☐  the U6 L07 `deco` call-count question — my answer was ______, the real
     answer is ______

## PART 4 — ERROR LOG (5 min)

- ☐  Every error from Parts 1 and 2 into the **Geometry Error Log**
- ☐  Tag each: **off-by-one**, **base case**, **recursion depth**, **formula**,
     **careless**
- ☐  New tag introduced today, if any: ______
- ☐  Most common tag: ______

## PART 5 — WHAT "FRACTAL" MEANS, IN WRITING (5 min)

One sentence, no jargon:

> A fractal is a shape ______

- ☐  My sentence: ______
- ☐  Give one example from the U6 L07 output: ______

## 🇹🇼 TAIWAN CONTEXT

Recursive descent over a hierarchy is how configuration and policy are
evaluated in production network stacks, and the depth budget from U6 L07 is a
real operational parameter, not a teaching device. When the budget is set too
small, a legitimately nested policy fails to load and the failure surfaces as
"policy rejected" with no indication of why — which costs an engineer an
afternoon. When it is set unbounded, a crafted deeply nested input is a cheap
denial of service. Choosing the budget is a risk decision, and like every
decision in this course, it should be written down with a reason attached.

**Next:** L09, Apr 22 — project build day 1. Generate the fractals and
measure them. This is the first day of the Fractal Detection Models project.
