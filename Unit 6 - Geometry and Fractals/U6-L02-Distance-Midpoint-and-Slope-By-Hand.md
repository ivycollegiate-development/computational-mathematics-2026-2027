# U6 L02 — Distance, Midpoint, and Slope, By Hand

**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.2 — compute distance, midpoint, and slope from first principles, and
predict the *form* the code will return for each

---

**No laptop today.** This is the one day in the unit where doing it by hand is
not nostalgia. Wednesday we write `geomkit.py`, and I want to see how many of
you can predict its output before you run it.

## PART 1 — DISTANCE, THREE TIMES (12 min)

Use the distance formula. Show the substitution, not just the answer.

1. `(0, 0)` to `(3, 4)`

   d² = ______  d = ______  predicted Python returns: ______

2. `(1, 1)` to `(4, 5)`

   d² = ______  d = ______  predicted Python returns: ______

3. `(0, 0)` to `(7, 24)`

   d² = ______  d = ______  predicted Python returns: ______

- ☐  Number 3 is a Pythagorean triple. **Will Python return exactly `25.0`, or
     something like `24.999999999999996`?** Write your prediction and your
     reason: ______
- ☐  Write the subtraction inside the square root for number 2, in order:
     ______

## PART 2 — MIDPOINT, AND WHY IT MATTERS (10 min)

4. Midpoint of `(0, 0)` and `(3, 4)`: ______
5. Midpoint of `(2, -5)` and `(7, 11)`: ______
6. Midpoint of `(0, 0)` and `(0, 10)`: ______

- ☐  A sensor sits at one end of a 100-metre cable and reports at the other
     end. The operator reads the midpoint as "the fault is halfway." In one
     sentence, why is a midpoint **not** a location of failure? ______
- ☐  What has to be assumed for the midpoint to mean anything at all?
     ______

## PART 3 — SLOPE, AND THE CASE THAT BREAKS (15 min)

7. Slope of `(0, 0)` to `(3, 4)`: ______
8. Slope of `(0, 0)` to `(4, 4)`: ______
9. Slope of `(2, 1)` to `(7, 1)`: ______
10. Slope of `(2, 1)` to `(2, 9)`: ______

**Number 10 is the important one.** A vertical line has no slope. Write down
what your function should do when it gets one — raise, return something, print
a message?

- ☐  My decision: ______
- ☐  Now the harder question: slope of `(0, 0)` to `(0.0000001, 5)` is a
     perfectly ordinary-looking number. Is that a real slope? ______
- ☐  So: a slope is only meaningful relative to what? ______

## PART 4 — PREDICT BEFORE YOU RUN (8 min)

Fill this in. Do not compute; predict. Tomorrow you will find out.

| quantity | value I predict | what **type** does Python give me? |
|---|---|---|
| `distance((0,0),(3,4))` | | |
| `distance((0,0),(7,24))` | | |
| `midpoint((0,0),(3,4))` | | |
| `slope((0,0),(3,4))` | | |
| `slope((0,0),(4,2))` | | |
| `slope((0,0),(4,1))` | | |

Now answer in writing:

- ☐  `slope((0,0),(4,2))` and `slope((0,0),(4,1))` are close. In decimal form
     they round to `0.5` and `0.2`-ish. Without rounding, how many digits will
     Python actually print? Predict: ______
- ☐  Which of my six predictions am I least sure about? ______

## 🇹🇼 TAIWAN CONTEXT

Slope is the whole game in hydrology and in terrain analysis, and Taiwan makes
the case sharply: the island's rivers run short and steep, and the **river
gradient** — drop over distance — is computed as a slope. The Pingshui River and
the Zhuoshui both have gradients in the range of a few percent, and that number
is what tells an engineer whether a stretch will erode in a typhoon. Get the
coordinate frame wrong on those and you get the wrong answer about whether a
channel floods.

**Next:** L03, Wed Apr 14 — laptop. We build `geomkit.py` and check every
prediction on the table above, one at a time, and I will call on people who
predicted wrong.
