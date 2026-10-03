# U5 L10 — Expected Value, and the Start of `riskkit.py`

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.7 — compute expected value from an outcome distribution; write
`riskkit.py`'s `expected_value` with input validation; state what EV does not
tell you

---

## TODAY'S PURPOSE

Everything so far has been set arithmetic. Today the sets become **money**:
expected value is the weighted average of outcomes by probability, and it is
the number your entire Risk Simulator project exists to compute.

It is also the number most likely to be quoted without the sentence that makes
it honest. `EV = -200` does not mean you will lose 200 dollars. It means
something narrower, and today's last part is about saying the narrow thing
precisely.

## PART 1 — THE DEFINITION, THEN THE TWO EASY CASES (10 min)

**Expected value** is the probability-weighted average of the possible
outcomes. For a distribution over outcomes, `EV = Σ pᵢvᵢ`. If the `pᵢ` do not
sum to 1, you do not have a distribution and the number you compute means
nothing.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def expected_value(outcomes):
    """outcomes: list of (probability, payoff). Returns the mean payoff."""
    if not outcomes:
        raise ValueError("expected_value needs at least one outcome")
    p_total = sum(p for p, _ in outcomes)
    if p_total != 1:
        raise ValueError("probabilities must sum to 1, got %r" % (p_total,))
    return sum(p * v for p, v in outcomes)

coin = [(F(1,2), 100), (F(1,2), -100)]
print("coin flip EV:", expected_value(coin))
print("a sure 50:", expected_value([(F(1,2), 50), (F(1,2), 50)]))
roll = [(F(1,6), v) for v in (1,2,3,4,5,6)]
print("one die EV:", expected_value(roll))
two_dice = [(F(1,36), a+b) for a in range(1,7) for b in range(1,7)]
print("two dice EV:", expected_value(two_dice))
print("coin EV equals 50, but the outcomes are:", [v for _, v in coin])
```

Real output:

```
coin flip EV: 0
a sure 50: 50
one die EV: 7/2
two dice EV: 7
coin EV equals 50, but the outcomes are: [100, -100]
```

Two checks worth your attention.

**`7/2`, not `3.5`.** Exact rational arithmetic, because the answer to a
probability question is a rational number and rounding it is a decision you
should make on purpose, at the display layer, not by accident inside the
computation.

**The last line is the whole lesson in one comparison.** A coin flip has EV 0
and a guaranteed 50 has EV 50 — but a *coin flip for 100 against −100* has the
same EV as a *guaranteed 0*, which is a different thing from the guaranteed 50
you just computed. **EV is not a score of how good the deal is. It is a
weighted average, and two distributions with the same average can be nothing
alike.** Wednesday is about that in full.

- ☐  Why is `7/2` a better answer than `3.5` in a program that only prints it?
      ______
- ☐  Name a pair of decisions with the same EV where you would obviously choose
      one. ______

## PART 2 — A REAL DECISION (12 min)

Your laptop holds one term of work you have not backed up. The drive is two years
old.

- With a backup, the probability of losing the work is 1 in 10 a year.
- Without one, it is 1 in 2 a year.
- Either way, if you lose it, it costs you 2,000 dollars in your own time to
  rebuild.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def expected_value(outcomes):
    if not outcomes:
        raise ValueError("expected_value needs at least one outcome")
    p_total = sum(p for p, _ in outcomes)
    if p_total != 1:
        raise ValueError("probabilities must sum to 1, got %r" % (p_total,))
    return sum(p * v for p, v in outcomes)

backup = [(F(9,10), 0), (F(1,10), -2000)]
no_backup = [(F(1,2), 0), (F(1,2), -2000)]
print("with backup, EV:", expected_value(backup))
print("without backup, EV:", expected_value(no_backup))
print("expected dollars backup saves:", expected_value(no_backup) - expected_value(backup))
```

Real output:

```
with backup, EV: -200
without backup, EV: -1000
expected dollars backup saves: -800
```

The sign is awkward on that last line and it is worth a moment. `−1000 − (−200)`
is `−800`, which reads backwards: *skipping* the backup makes the expected loss
800 dollars worse. The subtraction order is the whole confusion. Write the
sentence, not the sign:

> Skipping the backup adds **800 dollars a year** to the expected loss.

- ☐  What does `−200` mean, in a sentence a non-mathematician would accept? It
      does **not** mean: ______ It does mean: ______
- ☐  Both options can lose everything you care about. Why is the EV comparison
      still the right first move? ______
- ☐  What single piece of information would you want before making this
      decision, that EV does not contain? ______

That last one is the L12 preview. Note it now: the answer is something about
*how bad* the bad outcome is when it happens, and how *spread out* the outcomes
are.

## PART 3 — THE GUARD, AND WHY IT IS NOT FUSSY (10 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def expected_value(outcomes):
    if not outcomes:
        raise ValueError("expected_value needs at least one outcome")
    p_total = sum(p for p, _ in outcomes)
    if p_total != 1:
        raise ValueError("probabilities must sum to 1, got %r" % (p_total,))
    return sum(p * v for p, v in outcomes)

try:
    print(expected_value([(F(1, 2), 10)]))
except ValueError as exc:
    print("ValueError:", exc)
try:
    print(expected_value([]))
except ValueError as exc:
    print("ValueError:", exc)
```

Real output:

```
ValueError: probabilities must sum to 1, got Fraction(1, 2)
ValueError: expected_value needs at least one outcome
```

Without the first guard, that half-probability distribution returns `5` — a
small, plausible, entirely fictional number. **This is the single most likely
way your Risk Simulator produces a wrong answer while appearing to work**, and
on L20 we build exactly that bug on purpose. The guard costs three lines.

- ☐  Without the guard, what would `expected_value([(F(1,2), 10)])` return, and
      why is a wrong-but-plausible number worse than a crash? ______
- ☐  The empty-list guard: is that a real case or a fantasy? In your threat
      model, what would produce it? ______
- ☐  Should `expected_value` also reject a negative probability? Write the
      check. ______

## PART 4 — START `riskkit.py` (8 min)

Create the file. Today it gets **three** functions and nothing else.

```
compmath-u5-risk-simulator
├── setkit.py           (from L03, L04)
├── contingency.py      (from L06, L08)
└── riskkit.py          ← today
```

- ☐  `expected_value(outcomes)` — as above, with both guards
- ☐  `outcome_distribution(likelihood, loss)` — the common two-outcome case,
      returning a list of `(Fraction, value)` pairs
- ☐  `ev_report(outcomes)` — a function that returns a **dict** with at least
      `ev`, `worst_case`, `best_case`, and `n_outcomes`, so a caller gets
      context and not just a number

- ☐  Every docstring says what the function returns **and what it assumes**
- ☐  One test each, including the failing-probability-sum case
- ☐  A test that would catch a float sneaking in through an int division

- ☐  **Why a dict and not a bare number from `ev_report`?** One sentence:
      ______

## PART 5 — CLOSE (5 min)

- ☐  `riskkit.py` imports cleanly
- ☐  You can state, without looking, the sentence "EV = Σ pᵢvᵢ means ______"
- ☐  **In writing: the expected loss of one threat in a threat model you invent
      right now, with your probability and your impact number both stated
      explicitly as choices you made.** Three lines minimum. This is the first
      draft of the sentence your whole defense is built on.

## TURN IN — Expected Value

1. `riskkit.py` with the three functions, both guards, docstrings, and tests
2. The Part 1, Part 2, and Part 3 outputs, run live
3. Your three-line threat statement from Part 5, explicitly labelled *these are
   assumptions I chose*
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

Expected value without its assumptions is how public institutions get into
trouble, and the pattern is familiar enough to be worth naming. A risk
assessment that computes an expected loss and reports the number — without the
probability model behind it, without the population it applies to, and without
saying who chose the parameters — has produced a figure that reads as a
measurement and functions as a guess. The ROC national CERT's published risk
methodology is explicit that a likelihood figure is an **analyst judgement
calibrated against observed incidents**, and that a model which cannot say where
its parameters came from is not a model, it is a number with a decimal point.

The guard in Part 3 is the same discipline in code form. A program that accepts
a probability distribution summing to 1/2 and returns a confident EV of 5 is
doing exactly what an uncalibrated assessment does: producing a specific,
authoritative-looking figure from inputs that do not support it. Crashing is
the honest response. Your simulator's defense has to say the same thing in
prose — *the numbers here are assumptions the analyst chose* — and the grading
for this project is on that sentence, not on the arithmetic.
