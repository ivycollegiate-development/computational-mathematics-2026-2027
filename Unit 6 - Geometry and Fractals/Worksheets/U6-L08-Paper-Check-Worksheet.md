# U6 L08 — Paper Check: Iteration, Recursion, and Fractals

Names: ___________________________  Date: ____

Closed notes. Pencil. 45 minutes. Today you read recursion without running it, and you predict pictures you have not drawn. Real output from U6 L07's `deco` is printed below; use it.

## 1: Trace it

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

Real output at `steps = 2`:

```text
segments drawn: 4
  [  0.0,   1.0]
  [  2.0,   3.0]
  [  6.0,   7.0]
  [  8.0,   9.0]
```

**Section A — Trace `deco(lo=0, hi=9, steps=2)`.** List every call in the order it is *entered*.

| Call number | Argument | Your trace | What you notice |
| ----------- | -------- | ---------- | --------------- |
| 2           |          |            |                 |
| 3           |          |            |                 |
| 4           |          |            |                 |
| 5           |          |            |                 |
| 6           |          |            |                 |
| 7           |          |            |                 |

**Section B — The counts.**

1. How many calls is that? __________

2. How many of them hit the base case? __________

3. For `steps = 3`, how many calls in total? __________

4. Write the general formula for the number of calls as a function of `steps`: __________

Check yours against the `steps = 2` case, where the answer is `2^(steps+1) - 1`.

**Section C — Compare the two growth rates.**

5. `countdown_rec(3)` from U6 L05: how many calls, and how many hit the base case? __________

6. `countdown_rec` makes `n+1` calls and `deco` makes `2^(s+1) - 1`. Which grows catastrophically, and what is the practical consequence for a detector running on a large input? _______

## 2: Predict the picture

Describe each precisely. Words beat a bad drawing.

**Section A — The four curves.**

7. `plot(c, lambda t: t*t, 0, 1, 1)` at one level: what is drawn, and what is *not*? _______

8. `plot(c, lambda t: t*t, 0, 1, 5)`: which part of the curve is best resolved? _______

9. `plot(c, math.sin, 0, 6.28, 5)`: name the part of the plot that U6 L07's lower depth failed to resolve. _______

10. `plot(c, lambda t: abs(math.sin(3*math.pi*t)), 0, 1, 5)`: how many arches do you see, and why that number? _______

**Section B — The connection.**

11. The number of arches in question 10 is a property of the function, and it is the same property that makes the picture self-similar. State the connection in one sentence: _______

## 3: Prediction audit

**Section A — Compare against what actually happened.**

- ☐  In U6 L07 you predicted what increasing `steps` would do. Did it do that? _______
- ☐  One prediction you got wrong: _______ because _______
- ☐  U6 L07's `deco` call-count question — your answer was ________, the real answer is ________

## 4: Error log

**Section A — Record it.**

- ☐  Every error from Parts 1 and 2 into the **Geometry Error Log**
- ☐  Tag each: **off-by-one**, **base case**, **recursion depth**, **formula**, **careless**
- ☐  New tag introduced today, if any: _______
- ☐  Most common tag: _______

## 5: What "fractal" means

**Section A — One sentence, no jargon.**

> A fractal is a shape __________

12. Write the sentence: _______

13. Give one example from U6 L07's output: _______

___

**TURN IN** — This sheet, completed, with the trace table filled in full.
