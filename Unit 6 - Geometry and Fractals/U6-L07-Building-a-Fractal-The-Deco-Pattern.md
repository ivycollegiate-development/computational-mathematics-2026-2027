# U6 L07 — Building a Fractal: The `deco` Pattern

**Date:** Tuesday, April 20, 2027
**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.5 — implement a recursive function-drawing routine and predict what
increasing the recursion depth does

---

**Laptop today.** No plotting library. We draw into a grid of characters,
because the grid *is* the image and you cannot hide behind a renderer.

**The security lens.** Self-similar structure is exactly what an attacker
produces and exactly what a naive detector misreads. Later this week you will
build a detector that cannot tell a fractal from random noise — because a
7-day moving average cannot either. Today's recursion is the engine under it.

## PART 1 — THE CANVAS (10 min)

No `matplotlib`, no `pip`. A character grid.

```python
SIZE = 57

class Canvas:
    def __init__(self, size=SIZE, ylo=0.0, yhi=1.0):
        self.size = size
        self.ylo, self.yhi = ylo, yhi
        self.grid = [[" "] * size for _ in range(size)]

    def set(self, x, y, ch="#"):
        col = int(round(x * (self.size - 1)))
        frac = (y - self.ylo) / (self.yhi - self.ylo)
        row = int(round((1.0 - frac) * (self.size - 1)))
        if 0 <= col < self.size and 0 <= row < self.size:
            self.grid[row][col] = ch

    def render(self):
        return "\n".join("".join(r) for r in self.grid)
```

Three things to notice, and all three are real engineering:

1. **`ylo`/`yhi` exist because `sin` is negative** and a canvas that assumes
   `0..1` silently clips half the function. Silent clipping is a bug class you
   already know from Unit 2.
2. **`row` is flipped** — row 0 is the *top* of the terminal, but `y = 0` is the
   *bottom* of the maths. Get this backwards and your graph is upside down,
   which is exactly what a coordinate-frame mix-up looks like.
3. **The bounds check prevents a crash.** Without it, one out-of-range `y` and
   you get an `IndexError` instead of a picture.

- ☐  You typed it
- ☐  You can say which line silently drops points, and why that is dangerous
- ☐  You can say what happens if you remove the bounds check

## PART 2 — `deco` (12 min)

This is the whole lesson in eight lines.

```python
def deco(f, lo, hi, steps, draw):
    if steps <= 0:
        span = hi - lo
        n = max(2, int(span * 400))
        for i in range(n + 1):
            t = lo + span * i / n
            draw(t, f(t))
        return
    third = (hi - lo) / 3.0
    deco(f, lo, lo + third, steps - 1, draw)
    deco(f, hi - third, hi, steps - 1, draw)

def plot(c, f, lo, hi, steps):
    deco(f, lo, hi, steps, c.set)
```

Read it as a sentence: *look at the ends, recurse into the outer thirds, and
when the budget runs out just sample the rest densely.*

This is the **divide-and-conquer** pattern — you will see it in merge sort, in
quicksort, in FFT, and in every parallel algorithm ever written. One shape,
many uses.

- ☐  Why does it recurse into the **outer** thirds and not all three? ______
- ☐  How many calls does `deco` make at `steps = 4`? ______
- ☐  What is the base case protecting against? ______

## PART 3 — THE REAL PICTURES (13 min)

Actual output from the run, `y = x^2` with 5 levels. One honesty note before
you read it: **trailing spaces have been stripped from the right edge of these
pictures**, so the blocks are ragged. The `#` characters are exactly where the
program put them. Nothing else has been changed.

```text
y = x^2, deco with 5 levels
                                                        #
                                                       ##

                                                      ##
                                                      #

                                                    #
                                                   #

                                                  #
                                                  #

                                           ##
                                           #
                                          #
                                         ##

                                       #
                                       #
                                      #
                                     ##

                  ##
                 #
              ##
            ###

      #
### ##
```

- ☐  The picture is *sparse*. Why? The recursion only samples the outer thirds
     at the top level — what part of the curve is being under-drawn, and does
     that matter? ______
- ☐  Predict before running: with `steps = 7`, how much more detail appears at
     the top of the curve? ______
- ☐  Now run it. Did your prediction hold? ______

Here is `sin` over `0..2π`, the same routine, 5 levels:

```text
sin(x) over 0..2pi, deco with 5 levels
   ##
   #
  #
 ##

            ##
            #
          #
         ##

                              #
                             ##
                           #
                          ##

                                       #
                                      ##

   ##
   #
 #
##
```

- ☐  Notice the sine is drawn **backwards** in places — the peak is not
     resolved. Is that a bug, or a consequence of the pattern? ______
- ☐  How would you fix it *without* changing the recursion? ______

The last one matters: the fix is to recurse into all three thirds, or to
increase the sample count in the base case. **The pattern did not lie to you;
it did exactly what it says.** That is the virtue of a small honest function.

## PART 4 — SELF-SIMILARITY, MADE VISIBLE (10 min)

The real output that justifies the entire unit:

```text
|sin(3*pi*t)| - self-similar arches, deco with 5 levels
      #     ##                             ##     #
      #      #                             #      #
      #      #                             #      #

     #        #                           #        #

    #         #                           #         #
    #          #                         #          #

  #              #                     #              #
 #               #                     #               #

 #                #                   #                #
#                 #                   #                 #
#                  #                 #                  #
```

- ☐  Describe the pattern in one sentence. ______
- ☐  Now the geometric question: the function is
     `|sin(3πt)|`. Its **period** is ______, and on `[0,1]` that means it
     completes ______ arches.
- ☐  If the whole function on `[0,1]` is the motif, what is the motif on
     `[0, 1/3]`? ______
- ☐  That answer — *the piece is the whole, shrunk* — is the definition of
     **self-similarity**, and it is why the next three days are about
     measuring it.

## TURN IN — `deco` Checklist

1. `fractal_lab.py` with `Canvas`, `deco`, and `plot` committed
2. Three rendered pictures pasted: `x^2`, `sin`, `|sin(3πt)|`, all at 5 levels
3. Your count of how many calls `deco` makes at `steps = 1, 2, 3, 4` — run it,
   do not extrapolate
4. The 57×57 grid, explained: why is it square, and what happens if it is not?
5. One sentence on what `steps` is actually a *budget* for

## 🇹🇼 TAIWAN CONTEXT

Recursion that earns its keep: the recursive descent that parses nested
configuration — think of the layered rule sets in network and firewall policy
evaluation, where a rule can contain a sub-policy that contains a rule — is the
same shape as `deco`. Evaluate the outer structure, recurse into the nested
part, and keep a hard depth budget. The budget is the lesson. A policy engine
with no depth limit turns a deeply nested rule set into a crash, and a policy
engine with too small a budget silently refuses a legitimate policy. Both
failures have happened; the second is worse, because it looks like a
configuration error rather than a bug.

**Next:** L08, Wed Apr 21 — paper check on L05–L07, and the return of the
prediction audit.
