# U6 L03 — Coordinate Geometry in Code: Build `geomkit.py`

**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.3 — implement distance, midpoint, and slope as a reusable module with
explicit error handling, and verify it against hand calculations

---

**Laptop today.** Yesterday's prediction table is the assignment: you are going
to check every line of it against real output, and the ones you got wrong are
the interesting part.

The security lens for today: a monitoring tool that computes "how far is that
device from the last known good position" is doing exactly what your
`distance` function does. **If the error handling is wrong, the tool reports a
zero distance and says everything is fine.** That is the failure mode.

## PART 1 — THE STARTER (12 min)

Type this in. Do not copy-paste — the muscle memory is part of the lesson.

```python
import math

def distance(p, q):
    return math.hypot(q[0] - p[0], q[1] - p[1])

def midpoint(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)

def slope(p, q):
    if q[0] == p[0]:
        raise ValueError("vertical segment has no slope")
    return (q[1] - p[1]) / (q[0] - p[0])
```

Note `math.hypot` rather than `sqrt(dx**2 + dy**2)`. `hypot` is written to
avoid overflow on large inputs. This matters in exactly the situations you care
about later: if you are computing distances across a campus in metres, or
accumulating path length, the naive form can overflow where `hypot` does not.

- ☐  You typed it
- ☐  You can explain what `math.hypot` returns for a zero-length vector
- ☐  You can say why `slope` raises rather than returning `None`

## PART 2 — RUN IT, AND CHECK AGAINST YESTERDAY (12 min)

This is the real output, copied from a run, not predicted:

```text
A = (0, 0)  B = (3, 4)
distance      = 5.0
distance hex  = 0x4c4b40
midpoint      = (1.5, 2.0)
slope         = 1.3333333333333333
slope of 5/12 = 0.4166666666666667
dist (0,0)-(7,24) = 25.0
  exact?           True
vertical segment -> vertical segment has no slope
```

That third line is the one to look at. It is the raw IEEE-754 bits of `5.0`,
and they are **not** zero — they are `0x4c4b40`. So `5.0` is not the same thing
as the integer 5 in the machine, it is the nearest representable double to it.
Precision is a property of the representation. Remember this in Unit 7.

- ☐  `distance((0,0),(7,24))` came back **exactly** `25.0` and
     `== 25.0` is `True`. Why did you predict it might not? ______
- ☐  Mark your prediction table from yesterday: how many of the six were right?
     ______ / 6

## PART 3 — THE EDGE CASES (12 min)

Real output from running the functions on the awkward inputs:

```text
perimeter of the 3-segment polyline:
  seg 0 5.0
  seg 1 4.0
  total = 9.0
```

The points were `(0,0)`, `(4,3)`, `(4,7)`. Note the last two share an x
coordinate, so `distance` is fine but `slope` on that pair would raise.

**Do these now, with real output, and paste it in:**

- ☐  `distance((0,0),(0,0))` → ______
- ☐  `slope((5,2),(5,9))` → what exactly gets printed? ______
- ☐  A caller does `slope(a, b)` and catches `ValueError`, then **silently
     substitutes 0.0**. What does that do to a "distance from last good
     position" alert? ______

That last one is the security finding of the day, and it is a real bug class:
catching an error and substituting a *plausible default* is how a monitoring
system goes quiet exactly when it should be loud. **A refused measurement must
be loud, not zero.**

## PART 4 — LEAST SQUARES, THE CHEAP VERSION (9 min)

You will need this in Unit 7 for fitting a trend line. Here it is in four lines,
and here is its real output:

```text
least-squares slope = 0.6
intercept           = 2.2
```

For the points `(1,2) (2,4) (3,5) (4,4) (5,5)`.

- ☐  Write the two sums that produce `0.6`, in full: ______
- ☐  Is the slope the average of the individual slopes? Compute the average
     and say why it differs: ______

## TURN IN — `geomkit.py` Checklist

1. `geomkit.py` committed with `distance`, `midpoint`, `slope`
2. `slope` raises a clear `ValueError` on a vertical segment — no traceback
   leaks to a caller who catches it
3. Real output pasted for: the six-part prediction check, the three edge cases,
   the zero-length vector
4. The five points from Part 4, with your least-squares work shown
5. A `README` line stating what `geomkit.py` does **not** do (hint: it does not
   validate that your inputs are really coordinates)

## 🇹🇼 TAIWAN CONTEXT

The zero-substitution bug above is not hypothetical in Taiwanese infrastructure
monitoring. Fibre and power route monitoring, and the SCADA systems behind water
and power utilities, all consume position data that is sometimes missing. A
sensor that reports no reading and a sensor that reports "unchanged" must never
look identical to the operator on shift — a technician working from a dashboard
at 3am cannot tell them apart if you have flattened the exception. The
convention that costs nothing and saves the incident: **refuse loudly, and
carry an explicit "unknown" state through every layer above you.**

**Next:** L04, Apr 15 — paper check on L01–L03. Pencil, and we find out
which of us was actually doing the geometry.
