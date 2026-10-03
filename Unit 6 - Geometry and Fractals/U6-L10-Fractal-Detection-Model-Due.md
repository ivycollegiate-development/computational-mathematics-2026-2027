# U6 L10 — Fractal Detection Model Due

**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.6 — submit a measured, reproducible artifact; state its limits

---

**Due tonight, 11:59 PM.** This is a submission day, not a teaching day. The
45 minutes are for finishing and submitting cleanly.

You have the generate-and-measure half from yesterday. What you are turning in
today is that half **plus a one-page defense**, and the defense is where the
marks are.

## PART 1 — WHAT MUST BE IN THE REPO (10 min)

```
fractal-project/
├── README.md            # the defense, one page
├── generate.py          # Koch table, Sierpinski cells
├── measure.py           # box counting + least-squares slope
├── test_measure.py      # your own tests
├── data/
│   └── results.txt      # the real run output, committed
└── manifest.sha256      # generated
```

- ☐  All files committed to `main`
- ☐  `python3 measure.py` in a **fresh clone** reproduces `results.txt`
- ☐  `python3 test_measure.py` prints `all tests passed`
- ☐  `manifest.sha256` generated and committed

## PART 2 — THE DEFENSE, SIX QUESTIONS (20 min)

This goes in `README.md`. Rough is fine — you revise on Wed Apr 28. **Answer
all six.**

1. Your `measure.py` fits a slope to `log(N)` against `log(k)`. **State that
   slope is a dimension in one sentence**, and say what a value of `1.0` and a
   value of `2.0` would each mean.

2. On the depth-5 Sierpinski your error was `0.000000`. **Explain why that
   number is not representative** of what your program does on real input.

3. Box counting needs a choice of box sizes. You used `(2, 4, 8, 16, 32)`. What
   happens to the measured dimension if you use only `(16, 32)`? Justify your
   answer before you run it — then run it: ______

4. Your Koch perimeter table uses `fractions.Fraction`. **What would change if
   you used floats**, and which of the two would you trust for a claim in
   writing?

5. Pick one:

   - *I will not measure the boundary, because …* or
   - *I will measure the boundary, and it will be wrong for a fractal because …*

6. **The sentence your project exists to support:**

   > My program computes ______, which is ______, and it is **not** ______.

The third clause is the graded one. A defense that only describes what the
program does is a README. A defense that names what it cannot do is an
argument.

## PART 3 — SUBMIT (15 min)

- ☐  Push, then **clone to a fresh directory** and run it there. If it fails in
     the fresh clone, it does not count as done
- ☐  Submit the Classroom link with the repo URL in the description
- ☐  Attach `results.txt` and the SHA-256 of `measure.py` itself
- ☐  By tonight, also confirm: **Mon Apr 26 you will be adding the detector,
     and it is going to produce false positives.** Do not write a defense that
     claims your current numbers are the finished result

## TURN IN — Due Tonight

1. Repo with `generate.py`, `measure.py`, `test_measure.py`, `results.txt`
2. `test_measure.py` prints `all tests passed` in a fresh clone
3. `manifest.sha256` committed
4. `README.md` with all six defense questions answered — **all six**
5. Question 3 answered with the *predicted* value written **before** you ran
   it, then the real one
6. Classroom submission, 11:59 PM

**Grade the honesty.** If you can show me the exact sentence your program does
*not* support, this is a strong submission. If `README.md` is a description of
the code, it is an incomplete one.

## 🇹🇼 TAIWAN CONTEXT

The reason the boundary-versus-area question in Part 2.5 is not pedantic: real
capture data has a size limit. A packet capture, a log window, a flow export —
each has a maximum resolution you can ever observe. A boundary-measurement
detector run on a truncated capture will systematically **under**-report
structure, and the under-report looks like "nothing unusual here." The safe
operational posture is to state the capture window in the output, so that a
reader can tell a genuinely quiet period from a period where you simply could
not see far enough. That is not a limitation you hide; it is a condition you
publish.

**Next:** L11, Mon Apr 26 — build day 2, and the false-positive problem. Bring
your laptop and your defense draft.
