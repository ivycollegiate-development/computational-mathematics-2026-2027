# U6 L04 — Paper Check: L01–L03

**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.1, 6.2, 6.3 — verify hand computation against code output, and keep an
error log

---

**No laptop.** Pencil. Your `geomkit.py` is on your screen at home and you will
want it tonight.

Three days, one theme: **a coordinate is a claim, and the arithmetic that
follows the claim can be perfectly correct and still useless.** Today we find
out who checked.

## PART 1 — SOLVE IT, THEN PREDICT (15 min)

Do the work by hand. Then, for each, write what you predict `geomkit.py`
returns — the **value** and the **form**.

1. `distance((0, 0), (3, 4))`

   by hand = ______  predicted value = ______  predicted form = ______

2. `distance((0, 0), (7, 24))`

   by hand = ______  predicted value = ______  predicted form = ______

3. `distance((2, 1), (2, 9))`

   by hand = ______  predicted value = ______  predicted form = ______

4. `midpoint((-4, 8), (6, -2))`

   by hand = ______  predicted value = ______  predicted form = ______

5. `slope((-1, -1), (3, 3))`

   by hand = ______  predicted value = ______  predicted form = ______

6. `slope((0, 0), (3, 3))`

   by hand = ______  predicted value = ______  predicted form = ______

**Numbers 5 and 6 are the same slope and they are not supposed to look the
same.** Write out what Python actually prints for each, character for character,
as best you can:

- ☐  number 5 prints ______
- ☐  number 6 prints ______
- ☐  Why? ______

7. Least squares through `(1,2) (2,4) (3,5) (4,4) (5,5)`:

   slope = ______  intercept = ______

## PART 2 — PREDICTION AUDIT (10 min)

| quantity | predicted | actually right? | if wrong, what did you expect and why |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |

- ☐  Predictions right: ______ / 7
- ☐  Were my **values** better or my **forms**? Evidence: ______
- ☐  The single prediction I was most wrong about was number ______, because
     ______

**Grade this on prediction honesty.** A wrong prediction you can explain is
worth more than a right one. If every row is right, I will assume you filled
the column in afterwards and Part 2 is a zero.

## PART 3 — THE ERROR LOG (10 min)

Open your **Geometry Error Log**. Two columns: *what I wrote* and *what it
should have been*.

- ☐  Every error from Parts 1 and 2 goes in, including the ones you caught
- ☐  Tag each: **sign**, **subtraction order**, **formula**, **float form**,
     **careless**
- ☐  How many of today's errors were about *form* rather than *value*? ______
- ☐  Most common tag: ______

The float form is the new tag and it is the one that will follow you into Unit
7. `2.2` is not `2.2` as a printed string; it is the nearest double to it. A
residual you print with `:.2f` can hide an error of a completely different size.

## PART 4 — ONE MORE BY HAND (10 min)

A device is at `(120, 80)`. A second device is at `(150, 120)`.

1. Distance between them: ______
2. Midpoint: ______
3. Slope of the line joining them: ______
4. **The device at `(120, 80)` is re-deployed to `(121, 80)`.** New distance
   between the two devices: ______
5. Did the second device move at all? ______
6. Is the change in the distance (from your answer to 1) a big change or a small
   one? Say which, and why the distinction matters for an alerting system:
   ______

Question 6 is the one that matters. A system that alerts on *absolute* distance
went quiet; a system that alerts on *change in* distance fired. Both are
defensible. Choosing between them is the analyst's job, and it is exactly the
kind of choice a model forces you to make out loud.

## 🇹🇼 TAIWAN CONTEXT

Rounding and units bite in Taiwanese practice more than students expect, because
the country uses **metric with legacy Chinese units still in daily speech** —
distance gets quoted in 公里, 公尺, and sometimes 尺 in conversation while every
sensor logs metres. A tool that ingests a human-entered field and assumes
metres will be off by a factor of 3.3 for anything someone typed in 尺, and
nothing in the arithmetic will look wrong. Unit conversion is a security
control, not a convenience.

**Next:** L05, Fri Apr 16 — back to the machine, and recursion finally arrives.
We watch it run before we believe it.
