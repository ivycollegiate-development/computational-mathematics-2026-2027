# U5 L18 — The Monte Carlo Engine, and Your Model as a Shape

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.10 — implement a Monte Carlo engine for a threat model; validate it
against the closed form; read the resulting distribution rather than its mean

---

## TODAY'S PURPOSE

You have been quoting a mean since L10. Today you get the whole distribution,
and it turns out to contain information the mean cannot reach.

We build the engine against your spec from L15, then check it two ways: against
the closed-form answer (does the code compute the right thing?) and against the
distribution (does the code compute the *right kind* of thing?).

## PART 1 — THE CLOSED FORM FIRST (8 min)

Before simulating anything, write the answer you expect. If the simulation
disagrees with the algebra, one of them is wrong and you need to know which.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

THREATS = [
    {"id": "T-phish", "likelihood": F(4, 10), "impact": 3000},
    {"id": "T-ransom", "likelihood": F(3, 20), "impact": 45000},
    {"id": "T-doxs", "likelihood": F(2, 10), "impact": 12000},
]

def closed_form_p_any(threats):
    """P(at least one fires in a year) treating threats as independent."""
    p_none = 1
    for t in threats:
        p_none *= (1 - t["likelihood"])
    return 1 - p_none

cf = closed_form_p_any(THREATS)
print("closed form P(any):", cf, "=", float(cf))
print("p_none:", 1 - cf)
print("by hand: (1-4/10)(1-3/20)(1-2/10) =", (F(6,10) * F(17,20) * F(8,10)))
```

Real output:

```
closed form P(any): 74/125 = 0.592
p_none: 51/125
by hand: (1-4/10)(1-3/20)(1-2/10) = 51/125
```

The independence assumption is *right there* in that last line — `p_none` is the
**product**, which is only valid if the threats are independent. Nothing in the
data establishes that. Two of these three threats could plausibly fire together
because they share an entry point, and if they do, this number is wrong.

**On L20 we will build exactly that error, and it will pass every test you
write.** Today, just note the word *independent* in the docstring.

- ☐  What is `51/125` in plain words: ______
- ☐  Name one pair of your three threats that could plausibly be correlated,
      and say through what mechanism: ______

## PART 2 — THE ENGINE, AND THE CONVERGENCE (12 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random

THREATS = [
    {"id": "T-phish", "likelihood": F(4, 10), "impact": 3000},
    {"id": "T-ransom", "likelihood": F(3, 20), "impact": 45000},
    {"id": "T-doxs", "likelihood": F(2, 10), "impact": 12000},
]

def closed_form_p_any(threats):
    p_none = 1
    for t in threats:
        p_none *= (1 - t["likelihood"])
    return 1 - p_none

def simulate_year(rng, threats):
    """One year. Returns the total loss for that year."""
    total = 0
    for t in threats:
        if rng.random() < float(t["likelihood"]):
            total += t["impact"]
    return total

def monte_carlo(threats, years, seed=20270310):
    """Loss for each simulated year. The seed is a parameter, not a global."""
    rng = Random(seed)
    return [simulate_year(rng, threats) for _ in range(years)]

cf = closed_form_p_any(THREATS)
for years in (1000, 10000, 100000):
    losses = monte_carlo(THREATS, years)
    hits = sum(1 for L in losses if L > 0)
    emp = F(hits, years)
    print("years=%-7d empirical %-14s diff %s" % (years, emp, round(float(abs(emp - cf)), 5)))
```

Real output:

```
years=1000    empirical 581/1000       diff 0.011
years=10000   empirical 1179/2000      diff 0.0025
years=100000  empirical 2957/5000      diff 0.0006
```

Three sample sizes, three diffs: 0.011, 0.0025, 0.0006. Each is roughly a
factor of four smaller for each tenfold increase in `n` — the `1/√n` rate from
yesterday, visible in your own model.

- ☐  Is the engine hitting the closed form? ______ How do you know it is not just
      getting lucky: ______
- ☐  How many years would you need for the probability to be within 0.001?
      Use yesterday's formula: ______
- ☐  **The `float()` on line `if rng.random() < float(t["likelihood"])`:** why is
      that there, and what is the alternative? ______

The honest answer to the last one: `random()` returns a float in `[0, 1)`, so a
comparison against a `Fraction` requires the conversion. The alternative is an
integer comparison — draw `rng.randrange(0, den) < num` — which is exact and
costs nothing. Build it if you have the time, and note in the docstring which
approach you took and why.

## PART 3 — THE MEAN, AND THE THING THE MEAN HIDES (12 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random

THREATS = [
    {"id": "T-phish", "likelihood": F(4, 10), "impact": 3000},
    {"id": "T-ransom", "likelihood": F(3, 20), "impact": 45000},
    {"id": "T-doxs", "likelihood": F(2, 10), "impact": 12000},
]
def simulate_year(rng, threats):
    total = 0
    for t in threats:
        if rng.random() < float(t["likelihood"]):
            total += t["impact"]
    return total
def monte_carlo(threats, years, seed=20270310):
    rng = Random(seed)
    return [simulate_year(rng, threats) for _ in range(years)]

def ev(threats):
    return sum(t["likelihood"] * t["impact"] for t in threats)

print("closed form EV:", ev(THREATS))
losses = monte_carlo(THREATS, 200000)
emp_ev = F(sum(losses), len(losses))
print("empirical EV:", emp_ev, "=", float(round(emp_ev, 1)))
worst = max(losses)
print("worst observed:", worst, "in", sum(1 for L in losses if L == worst), "of", len(losses), "years")
print("theoretical worst (all three fire):", sum(t["impact"] for t in THREATS))
```

Real output:

```
closed form EV: 10350
empirical EV: 1040211/100 = 10402.1
worst observed: 60000 in 2401 of 200000 years
theoretical worst (all three fire): 60000
```

`empirical EV` is `1040211/100` — an exact fraction, because the sum of 200,000
integers divided by 200,000 is exactly that. Displaying it as a float is a
*presentation* decision, made deliberately at the print, which is where it
belongs.

Now the two lines that matter. **The worst year costs 60,000, and it happened
in 2,401 of 200,000 years — about 1.2% of all time.** Your expected loss is
10,350, which is one sixth of a single bad year.

- ☐  What is the ratio of a bad year to your expected annual loss? ______
- ☐  If your annual budget for risk were 12,000, **what fraction of years
      would it fail to cover?** ______
- ☐  The `2,401` figure is a frequency in a sample. What is the closed-form
      probability that all three threats fire in the same year? Compute it:
      ______  Does it match 2401/200000: ______
- ☐  Now the sentence: **A decision-maker reading "expected loss 10,350" and
      budget 12,000 concludes the year is covered. What is the one sentence
      that must accompany that number?** ______

That last checkbox is the difference between a model and a decision. A mean of
10,350 against a 12,000 budget does not mean the budget holds. It means the
budget holds *in expectation across many years*, and in 1.2% of years the loss
is 60,000 — five times the budget. Whether the organisation can survive those
years is a question about reserves, and it is the question your report exists to
raise.

## PART 4 — THE SHAPE (8 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random
from collections import Counter

THREATS = [
    {"id": "T-phish", "likelihood": F(4, 10), "impact": 3000},
    {"id": "T-ransom", "likelihood": F(3, 20), "impact": 45000},
    {"id": "T-doxs", "likelihood": F(2, 10), "impact": 12000},
]
def simulate_year(rng, threats):
    total = 0
    for t in threats:
        if rng.random() < float(t["likelihood"]):
            total += t["impact"]
    return total

rng = Random(20270310)
losses = [simulate_year(rng, THREATS) for _ in range(200000)]
c = Counter(losses)
for loss in sorted(c, reverse=True)[:6]:
    print("loss %-7d occurred %-7d times  p=%s" % (loss, c[loss], F(c[loss], len(losses))))
```

Real output:

```
loss 60000   occurred 2401    times  p=2401/200000
loss 57000   occurred 3578    times  p=1789/100000
loss 48000   occurred 9693    times  p=9693/200000
loss 45000   occurred 14524   times  p=3631/50000
loss 15000   occurred 13711   times  p=13711/200000
loss 12000   occurred 20451   times  p=20451/200000
```

Six rows, and the shape is immediately visible: a long thin tail at the top
where all three threats fire together, and a body of ordinary years below. **The
mean of this distribution is 10,350 and the distribution has seven distinct
values.** You cannot know that from the mean. A mean of 10,350 is compatible
with a smooth spread and with this exact six-spike comb, and the difference
between those two worlds is the difference between "budget for the mean" and
"reserve for the tail."

- ☐  How many distinct annual loss values are possible with three threats? ______
- ☐  The 57,000 row: which two threats fired? ______ (There is exactly one
      combination, and its probability is a product.)
- ☐  Rank the six rows by frequency. Is the most *damaging* row the most
      frequent, the least, or in between: ______

## PART 5 — BUILD IT (5 min)

- ☐  `closed_form_p_any(threats)`, `simulate_year(rng, threats)`,
      `monte_carlo(threats, years, seed)` in `riskkit.py`, exactly as above
- ☐  `distribution(losses)` returning a `Counter` keyed by loss value
- ☐  `engine_report(threats, years, seed)` returning a dict with
      `p_any_closed_form`, `p_any_empirical`, `ev_closed_form`, `ev_empirical`,
      `worst_case`, `p_worst_case`, `n_years`, `seed`, and a string
      `independence_assumed` — because the assumption is part of the result
- ☐  A test asserting `abs(p_any_empirical - p_any_closed_form) < 0.02` at
      100,000 years, with a comment saying it is a **sampling** tolerance and
      not a correctness proof
- ☐  A test that the worst observed loss equals the sum of all impacts

## TURN IN — The Monte Carlo Engine

1. `riskkit.py` with the five functions and both tests
2. The Part 1, Part 2, Part 3, and Part 4 outputs, run live
3. **Your one sentence from Part 3, fourth checkbox** — the sentence that has
   to accompany an expected loss in any report you write
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

The Part 3 finding is the shape of every serious breach cost estimate, and it is
the finding the ROC national CERT's post-incident material keeps returning to:
**organisations budget for the average year and are destroyed by the
coincident one.** Two incidents that are individually survivable become
un-survivable when they land in the same quarter, and the reason organisations
fail to prepare for that is precisely that a model reporting "expected annual
loss" describes the year that does not happen.

Taiwan's experience with ransomware against SMEs and hospitals makes the
tail concrete rather than theoretical. Backup that has never been restore-tested
is a `P(loss)` of 1 in the exposure population and a 45,000 impact that appears
in 1% of years — and 1% of years is four years in forty, which is inside the
planning horizon of any board that expects to exist. The national CERT's
repeated guidance on ransomware readiness, and the Ministry of Digital Affairs'
framework for smaller organisations, both reduce to the same instruction: decide
whether you can absorb the worst credible year, and write down the answer.

That is why `engine_report` includes `independence_assumed` as a **string in the
output**, not a comment in the source. Independence is what makes the closed form
legitimate; if two threats share an entry point, the product is wrong, and a
report that hides the assumption inside a docstring has buried the single
assumption a reviewer most needs to challenge. Your L26 defence is graded on
whether that assumption is visible on the page.
