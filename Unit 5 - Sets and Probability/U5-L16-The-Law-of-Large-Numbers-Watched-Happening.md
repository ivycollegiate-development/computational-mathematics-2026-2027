# U5 L16 — The Law of Large Numbers, Watched Happening

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.10 — observe convergence of the sample mean; distinguish sampling
noise from model error; read a result in the units of its standard error

---

## TODAY'S PURPOSE

The claim you are going to make in your report is *the simulation gives
approximately X*. That claim is only defensible if you know **how approximately**,
and that number is the standard error — which is the Law of Large Numbers turned
into a quantity with units.

Today you watch convergence happen and then quantify it. Friday you simulate
the thing you actually care about.

## PART 1 — WATCH IT CONVERGE (12 min)

Same experiment, five sample sizes. The true answer is 50.5, because the
outcomes run 0 to 100 uniformly and the mean of that is `101/2`.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random

rng = Random(20270304)

def uniform_trials(n, lo=0, hi=100):
    return [rng.randrange(lo, hi + 1) for _ in range(n)]

for n in (10, 100, 1000, 10000, 100000):
    acc = 0
    reps = 5
    for _ in range(reps):
        acc += F(sum(uniform_trials(n)), n)
    print("n=%-7d mean of %d reps: %s" % (n, reps, round(float(acc / reps), 3)))

print("true mean of uniform 0..100 is 101/2 =", F(101, 2))
```

Real output:

```
n=10      mean of 5 reps: 57.18
n=100     mean of 5 reps: 49.356
n=1000    mean of 5 reps: 50.243
n=10000   mean of 5 reps: 50.002
n=100000  mean of 5 reps: 50.033
true mean of uniform 0..100 is 101/2 = 101/2
```

That is the Law of Large Numbers happening, and you should be able to point at
it in the output. At `n=10` the estimate is 6.68 away from the truth. At
`n=100000` it is 0.03 away. **The error shrank by a factor of about 200 while
the sample grew by a factor of 10,000** — because the sample mean's error goes
as `1/√n`, not as `1/n`.

That relationship is the one thing to carry out of today. √100 is 10; if the
sample grows 100×, the error shrinks 10×. n grows 10,000×, error shrinks 100×.

- ☐  Error at n=10: ______ Error at n=100000: ______ Ratio: ______
- ☐  Predicted ratio if the error went as `1/n` instead of `1/√n`: ______
  Does the output match your prediction: ______
- ☐  Why is n=10 so bad? What is the smallest n here that would get you within
      1.0 of the truth, from the pattern above: ______

## PART 2 — TURN `1/√n` INTO A UNITS (12 min)

The convergence rate is not decorative. It tells you how many samples you need
for a given precision, and that is a budget decision.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random
from math import sqrt

TRUE_MEAN = 50.5          # uniform 0..100
SIGMA = 100.0 ** 0.5 / (12 ** 0.5)   # population sd of a uniform 0..100

def standard_error(n):
    """How far the sample mean is typically from the truth, for sample size n."""
    return SIGMA / (n ** 0.5)

print("population sd of uniform 0..100:", round(SIGMA, 4))
for target in (10.0, 1.0, 0.1, 0.01):
    n = int((SIGMA / target) ** 2) + 1
    print("to be within %-6s you need n >= %d" % (target, n))
print("check, n=10000:", round(standard_error(10000), 4))
rng = Random(11)
xs = [rng.randrange(0, 101) for _ in range(10000)]
m = float(F(sum(xs), 10000))
print("observed n=10000 mean:", round(m, 3), "error", round(abs(m - TRUE_MEAN), 3),
      "which is", round(abs(m - TRUE_MEAN) / standard_error(10000), 2), "standard errors")
```

Real output:

```
population sd of uniform 0..100: 28.8675
to be within 10.0 you need n >= 84
to be within 1.0 you need n >= 834
to be within 0.1 you need n >= 8334
to be within 0.01 you need n >= 833344
check, n=10000: 0.2887
observed n=10000 mean: 50.455 error 0.045 which is 0.16 standard errors
```

**The budget table is the point of this lesson.** Getting to within 10 dollars of
the truth costs 84 samples. To within one *cent* costs 833,344 — a thousand
times the compute for a hundredth of the precision. **Precision is expensive and
its cost grows as the square**, so there is a point past which another hour of
sampling buys less than the hour was worth.

The last line is what "within" means numerically: the observed error is 0.16
standard errors, which is unremarkable. Had it been 3, you would suspect
something about the generator.

- ☐  To be within 0.5 of the truth, you need n ≥ ______
- ☐  Going from n=100,000 to n=400,000 costs 4× the compute and buys you an
      error reduction by a factor of ______
- ☐  Your result is 0.16 standard errors from the truth. Is that surprising?
      ______
- ☐  **At what n does the standard error drop below 0.01, and what does that
      number tell you about a project with a Friday deadline?** ______

## PART 3 — THE BAD SEED, AND WHAT IT IS FOR (10 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random

r2 = Random(7)
samples = [r2.randrange(1, 7) for _ in range(6)]
print("six dice, seed 7:", samples, "mean", float(F(sum(samples), 6)))
print("six identical dice, seed 7:", [7] * 6, "mean 7.0 -- a real outcome, not a bug")

# the same generator, six times over, to show the seed is not the culprit
for seed in (1, 2, 3, 4, 5):
    r = Random(seed)
    xs = [r.randrange(1, 7) for _ in range(6)]
    print("seed %d -> %-28s mean %s" % (seed, xs, round(float(F(sum(xs), 6)), 3)))
```

Real output:

```
six dice, seed 7: [3, 2, 4, 6, 1, 1] mean 2.8333333333333335
six identical dice, seed 7: [7, 7, 7, 7, 7, 7] mean 7.0 -- a real outcome, not a bug
seed 1 -> [1, 3, 1, 7, 3, 7]          mean 3.667
seed 2 -> [3, 4, 2, 2, 3, 1]          mean 2.5
seed 3 -> [5, 3, 3, 2, 3, 3]          mean 3.167
seed 4 -> [1, 5, 5, 2, 6, 2]          mean 3.5
seed 5 -> [5, 1, 2, 4, 4, 2]          mean 3.5
```

A fixed seed gives you **reproducibility** and a single run gives you **one
draw**. `7` on six dice is a real, possible outcome — the generator is not
broken, and if you "fixed" it you would have broken the thing that makes
simulations auditable.

The seeds in the loop show the actual issue: at n=6 the mean moves from 2.5 to
3.667 depending on the seed. **At small n, the seed is most of the answer.**

- ☐  Which of the six seeds gave the highest mean? ______ Lowest: ______
- ☐  If you had run only seed 1 and reported 3.667 as "the mean of a die", what
      would you have claimed, and what is the true value? ______
- ☐  The correct fix is not a different seed. What is it? ______
- ☐  Why must a seed be a parameter with a documented default, not a constant
      in the file? Answer in the context of an audit: ______

That last checkbox is the one that matters for your project. **A buried seed
means a reader cannot tell whether you ran once and reported what happened, or
ran many times and reported the good one.** The second is not a result, it is a
selection, and the defence on L26 is graded partly on whether your numbers are
reproducible by someone who runs your code once.

## PART 4 — BUILD IT (8 min)

Add to `riskkit.py`:

- ☐  `standard_error(sd, n)` — raises `ValueError` for `n <= 0`
- ☐  `samples_needed(sd, tolerance)` — the inverse, `n = ceil((sd/tolerance)²)`,
      returning an `int` and rejecting a non-positive tolerance
- ☐  `simulate_mean(rng, draw, n)` — a function that draws `n` values from
      `draw(rng)` and returns the mean as a `Fraction`. **`rng` is a parameter,
      never a module global.**
- ☐  A test asserting that `samples_needed(sd, t) * t >= sd / sqrt(2)`, so the
      bound is checked and not just printed
- ☐  Docstrings with the units: "tolerance is in the same units as sd"

- ☐  Using your own simulator's real sd, compute how many samples you need for
      a probability accurate to 0.001. Write the number: ______
- ☐  Is that number something you could run before a Friday deadline? ______

## PART 5 — CLOSE (3 min)

- ☐  The `rng` parameter is threaded through every function that samples
- ☐  You can state, without looking, why the error goes as `1/√n` and not `1/n`
- ☐  **In writing: one sentence separating sampling noise from model error for
      your own project.** Sampling noise is ______; model error is ______; only
      the first shrinks when you add samples.

## TURN IN — Law of Large Numbers

1. `riskkit.py` with `standard_error`, `samples_needed`, `simulate_mean`, and
   the bound test
2. The Part 1, Part 2, and Part 3 outputs, run live
3. Your two sentences from Part 5
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

The budget table in Part 2 is the honest core of any defensible security
measurement, and it is where reporting in this field most often misleads. An
organization that reports "we simulate threat scenarios and our model puts the
annual probability of a successful intrusion at 4.7%" has, in the language of
today, claimed a precision that corresponds to a very large number of samples —
and the precision came from the **assumed likelihoods**, not from the sampling.
Run the identical simulation with a different base rate and the figure moves by
a factor of ten, while the standard error is unchanged at 0.01.

This is precisely the failure mode the Ministry of Digital Affairs' framework
and the national CERT's post-incident reviews warn against: a number whose
precision has been silently transferred from the appearance of computation to
the apparent reliability of the underlying model. The ROC guidance's phrase
"calibrated against observed incidents" is doing the same work your
`likelihood_source` field does on L14 — it is a claim about **provenance**, and
provenance, not the decimal places, is what makes a figure usable.

Practically: a small organization should sample enough to know the shape of its
exposure and then say plainly that the magnitude rests on external calibration.
Sampling harder to reduce a 0.01 standard error on a model whose parameters are
judgement calls buys a rounding error and costs the credibility that a caveated
number keeps.
