# U5 L12 — Variance and Spread: Why a Mean Alone Is Dangerous

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.8 — compute variance and standard deviation; explain why two
distributions with equal expected value can demand opposite decisions

---

## TODAY'S PURPOSE

You wrote the sentence on L10: *EV = Σ pᵢvᵢ means…* and you stopped before the
second half. Here is the second half.

**Four gambles. All of them have expected value 1,000. Two of them you would
take and two of them you would refuse, and the mean cannot tell them apart.**
That is not a limitation of arithmetic. It is a fact about what a mean is: a
weighted average, which is blind to everything except the total.

## PART 1 — FOUR BOOKS, ONE MEAN (12 min)

Read all four before computing anything. Then compute.

| book | outcomes | your gut reaction |
|---|---|---|
| **safe** | 1,000 for certain | |
| **risky** | 3,000 or −1,000, equally likely | |
| **equal** | −1,000, 1,000, 1,000, 3,000, each 1/4 | |
| **skew** | −500 with p = 9/10, or 14,500 with p = 1/10 | |

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

def variance(outcomes):
    """Population variance: the mean of the squared deviations from the mean."""
    mu = expected_value(outcomes)
    return sum(p * (v - mu) ** 2 for p, v in outcomes)

def stdev(outcomes):
    return round(float(variance(outcomes)) ** 0.5, 4)

safe  = [(F(1), 1000)]
risky = [(F(1,2), 3000), (F(1,2), -1000)]
equal = [(F(1,4), v) for v in (-1000, 1000, 1000, 3000)]
skew  = [(F(9,10), -500), (F(1,10), 14500)]
for name, book in (("safe", safe), ("risky", risky), ("equal", equal), ("skew", skew)):
    print("%-5s EV %-4s var %-9s sd %s" % (name, expected_value(book), variance(book), stdev(book)))
print("all four EVs equal?", len({expected_value(b) for b in (safe, risky, equal, skew)}) == 1)
```

Real output:

```
safe  EV 1000 var 0         sd 0.0
risky EV 1000 var 4000000   sd 2000.0
equal EV 1000 var 2000000   sd 1414.2136
skew  EV 1000 var 20250000  sd 4500.0
all four EVs equal? True
```

All four expected values are 1,000. The standard deviations are 0, 1,414,
2,000, and 4,500.

- ☐  Rank them by standard deviation: ______
- ☐  The `skew` book has the **largest** sd but a small typical loss. Why does a
      mean-based sd miss that? ______
- ☐  The `risky` book loses 1,000 half the time. The `skew` book loses 500 nine
      times out of ten. **Which is the better bet for someone who cannot afford
      a 1,000 loss, and how would you know that from these four numbers?**
      ______

That last question is the assignment. The answer is that **you cannot** — not
from the mean, and not from the standard deviation either, because both treat
every outcome as equally weighted around the centre. If the answer depends on
*which* losses hurt, you need a different statistic. Part 3.

## PART 2 — WHAT VARIANCE IS ACTUALLY MEASURING (10 min)

Variance is the expected value of the **squared** deviation from the mean:
`Var = Σ pᵢ(vᵢ − μ)²`. The squaring is not decoration — it is what makes the
quantity non-negative and what lets deviations above and below cancel in a
controlled way. Standard deviation is the square root, which puts it back in
the units of the original outcomes, which is why it is the one people quote.

- ☐  Why does the formula need `pᵢ` as a multiplier rather than just averaging
      the squared deviations? ______
- ☐  For `safe`, the variance is 0. Is that a *good* score? What does it tell
      you about the risk? ______
- ☐  Compute the variance of `skew` by hand, one term at a time, and check it
      against the code. Write your two terms: ______
- ☐  The `skew` sd of 4,500 is **larger than its own expected value of 1,000.**
      Is that possible? What does it tell you about using sd as a risk measure:
      ______

That last checkbox is not a curiosity, it is a warning. A standard deviation
bigger than the mean means the distribution is extremely skewed, and a
risk-averse decision-maker who reasons in sd-units is reading a number that no
longer corresponds to their intuition about money.

## PART 3 — ASYMMETRY: THE STATISTIC YOU ACTUALLY NEED (12 min)

The `skew` book loses a small amount, often. The `risky` book loses a lot,
sometimes. A person with limited resources cares about a completely different
thing from a person who can absorb one bad year. So: condition on the outcomes
that are bad.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def expected_value(outcomes):
    p_total = sum(p for p, _ in outcomes)
    return sum(p * v for p, v in outcomes)

def expected_shortfall(outcomes, threshold=0):
    """Mean payoff of the outcomes strictly below threshold, and how likely they are."""
    tail = [(p, v) for p, v in outcomes if v < threshold]
    p_below = sum(p for p, _ in tail)
    if p_below == 0:
        return F(0), p_below
    return F(sum(p * v for p, v in tail)) / F(p_below), p_below

safe  = [(F(1), 1000)]
risky = [(F(1,2), 3000), (F(1,2), -1000)]
equal = [(F(1,4), v) for v in (-1000, 1000, 1000, 3000)]
skew  = [(F(9,10), -500), (F(1,10), 14500)]
for name, book in (("safe", safe), ("risky", risky), ("equal", equal), ("skew", skew)):
    es, p_below = expected_shortfall(book, 0)
    print("%-5s P(loss) %-4s  mean outcome when it loses %s" % (name, p_below, es))
```

Real output:

```
safe  P(loss) 0     mean outcome when it loses 0
risky P(loss) 1/2   mean outcome when it loses -1000
equal P(loss) 1/4   mean outcome when it loses -1000
skew  P(loss) 9/10  mean outcome when it loses -500
```

Read the last two lines against the sd table from Part 1. `risky` has the
*smaller* standard deviation, 2,000 against 4,500 — and it is the one that
ruins you. The standard deviation ranked them backwards.

- ☐  Which of `risky` and `skew` has the higher chance of a loss? ______
- ☐  Which has the larger loss when it happens? ______
- ☐  Which has the higher standard deviation? ______
- ☐  So what does `expected_shortfall` see that `stdev` does not? ______
- ☐  Try `expected_shortfall(skew, -1000)`. What is the probability, and what
      does that tell you about the *size* of the tail? ______

That last one is the honest limitation of today's statistic, and you should find
it yourself: `skew`'s big outcome is on the *good* side, so a threshold-based
downside measure sees only the small losses. **`skew` has a huge standard
deviation and no dangerous tail.** Variance and shortfall are looking at
opposite ends of the distribution, and neither is the whole story. The version
that sees both is the histogram — and on Friday you build one by sampling,
which is the Monte Carlo engine your project needs.

- ☐  Write the sentence: *for a risk that can bankrupt the organization, the
      statistic I would report first is ______ and I would report ______
      alongside it because* ______

## PART 4 — BUILD IT INTO `riskkit.py` (8 min)

- ☐  `variance(outcomes)` and `stdev(outcomes)` — exact, no floats until the
      caller asks
- ☐  `expected_shortfall(outcomes, threshold)` returning a **tuple** of
      `(mean_loss_given_loss, probability_of_loss)`
- ☐  `shape_report(outcomes)` returning a dict: `ev`, `variance`, `stdev`,
      `p_loss`, `mean_loss_given_loss`, `best`, `worst`, `n_outcomes`
- ☐  Docstring on `shape_report` saying explicitly: **a caller who reads only
      `ev` is making a decision on one number and should not**
- ☐  Tests, including the four books from Part 1 as a fixed regression set — if
      a change to your code alters any of those four EV/var/sd values, something
      is wrong

- ☐  Run your `shape_report` on the four books and print a table. Paste it:
      ______

## TURN IN — Variance and Spread

1. `riskkit.py` with `variance`, `stdev`, `expected_shortfall`, `shape_report`,
   and the four-book regression test
2. The Part 1, Part 2, and Part 3 outputs, run live
3. Your sentence from the end of Part 3
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

This lesson is the mathematics of a decision that gets made badly in real
organisations every quarter. A security programme evaluated on **expected loss**
will always prefer the option with the smallest average and the largest
possible single loss, because averaging hides exactly the outcome that ends the
programme. A ransomware event that occurs once in five years at a cost that
exceeds the entire mitigation budget has a small expected value and a
catastrophic tail. The institution that bought its way to a low expected loss
has not reduced its risk; it has converted an uncertain risk into a certain one.

This is not hypothetical in Taiwan. The ransomware pressure on schools,
hospitals, and SMEs has been a recurring theme in national CERT advisories and
in the Ministry of Digital Affairs' guidance, and the recurring recommendation
is the one today's statistics support: model the **worst credible case** and
decide whether you can survive it, rather than model the average and decide
whether it is small. Taiwan's smaller organisations are the exposed case —
limited reserves, limited staff, and a single un-tested backup is a tail risk
with a `P(loss) = 9/10` attached to it and an `expected value` that looks
entirely reasonable on a slide.

For your Risk Simulator this is not an abstraction. `shape_report` returning a
dict instead of a bare EV is the structural version of the argument: the report
should make it *hard* to quote the mean alone. If a reader can get at `ev`
without seeing `p_loss` and `mean_loss_given_loss`, you have built a tool that
supports the exact mistake this lesson is about.
