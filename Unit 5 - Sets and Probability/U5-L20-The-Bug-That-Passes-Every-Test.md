# U5 L20 — The Bug That Passes Every Test

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.4, 5.9 — diagnose an over-counting error in a risk aggregator that
survives a complete test suite; write the test that would have caught it

---

## TODAY'S PURPOSE

I told you on L04 that the error we were building toward would arrive on L20
and that you would not see it coming. Here it is.

**`v1` is wrong. It is wrong by 40.5 dollars — about 4%. Every test it ships
with passes.** Nothing is broken. The code does exactly what it says, faithfully
and correctly, and it is still giving you a number that is too big, for a
reason that has nothing to do with the code.

## PART 1 — `v1`, THE SHIPPED VERSION (10 min)

Read it as a reviewer, not a user. What is it *claiming* to compute?

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

A = 5400

def v1(threats):
    """Expected loss for a set of (likelihood, impact) threats. Adds them up.

    Assumes each threat's expected loss is independent of the others.
    """
    total = F(0)
    for p, impact in threats:
        total += p * impact
    return total

def suite_v1():
    assert v1([(F(1, 2), 100)]) == 50
    assert v1([(F(1, 2), 100), (F(1, 2), 100)]) == 100
    assert v1([(F(1, 2), 100), (F(1, 3), 100)]) == F(50) + F(100, 3)
    assert v1([(F(1, 2), 100), (F(1, 3), 100), (F(1, 4), 100)]) == 50 + F(100, 3) + 25
    return "4 assertions passed"

print(suite_v1())
print("every assertion is a single-threat or a simple-sum case.")
print("none of them has two threats hitting the SAME asset.")
```

Real output:

```
4 assertions passed
every assertion is a single-threat or a simple-sum case.
none of them has two threats hitting the SAME asset.
```

Four assertions, all green. Now read that last line carefully, because it is the
whole lesson in advance: **every test describes a case where the threats hit
different things.** The bug lives in the case the tests do not describe.

- ☐  What does `v1`'s docstring claim? ______
- ☐  What does the code actually do? ______
- ☐  Are those the same thing? ______

They are not. The docstring says "expected loss for a set of threats." The code
computes the **sum of each threat's expected loss counted separately**, which is
only the expected loss of the whole set when the assets are distinct. The gap
between the claim and the code is where the bug lives.

## PART 2 — THE CASE NOBODY TESTED (12 min)

Two threats. Both of them compromise **the same asset**, worth 5,400.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

A = 5400
p1, p2 = F(3, 20), F(1, 20)
print("p1 =", p1, " p2 =", p2, " p1*p2 =", p1 * p2)
print("P(T1 alone) =", p1, "  P(T2 alone) =", p2, "  P(both) =", p1 * p2)
print("P(at least one) = p1 + p2 - p1*p2 =", p1 + p2 - p1 * p2)
```

Real output:

```
p1 = 3/20  p2 = 1/20  p1*p2 = 3/400
P(T1 alone) = 3/20  P(T2 alone) = 1/20  P(both) = 3/400
P(at least one) = p1 + p2 - p1*p2 = 77/400
```

`p1 + p2 - p1*p2` is inclusion–exclusion. It is the L04 formula. It is the only
correct way to combine two probabilities, and it was in your hands three weeks
ago.

Now the two implementations:

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

A = 5400

def v1(threats):
    total = F(0)
    for p, impact in threats:
        total += p * impact
    return total

def v2(threats):
    """P(at least one) by inclusion-exclusion, times the shared asset value."""
    if not threats:
        return F(0)
    first, *rest = threats
    p = first[0]
    for q, _ in rest:
        p = p + q - p * q
    return p * A

p1, p2 = F(3, 20), F(1, 20)
threats = [(p1, A), (p2, A)]
print("v1 expected loss:", v1(threats))
print("v2 expected loss:", v2(threats))
print("v1 overstates by:", v1(threats) - v2(threats))
print("the shared-exposure credit v1 omits:", p1 * p2 * A)
```

Real output:

```
v1 expected loss: 1080
v2 expected loss: 2079/2
v1 overstates by: 81/2
the shared-exposure credit v1 omits: 81/2
```

`v1` says 1,080. `v2` says 1,039.50. The difference is 40.50, and **the
difference is exactly `p1*p2*A` — the asset consumed twice.**

Read that as a story. In `3/400` of years, both threats fire. In those years
`v1` charges you 5,400 for the ransomware and 5,400 for the data exposure —
two separate losses on **one asset that is gone once**. The real loss in those
years is 5,400. `v1` does not have a rounding error or a type error. It has
double-counted a destroyed asset, which is the L04 error, sixteen days later,
wearing a different hat.

- ☐  Express the overstatement as a formula in words: ______
- ☐  With three threats where only the first two share: `v1` says 1,620 and
      `v2` says `29511/20`. The gap is `2889/20` = ______. Is that
      `p1*p2*A` alone, or something larger, and why: ______
- ☐  **The critical question:** why did none of the four tests in `suite_v1`
      catch this? Answer precisely, not "they weren't thorough": ______

The precise answer: the tests use `100` as the impact, and each test's threats
implicitly point at different things. `v1` is **not** a function of the
likelihoods alone — it is a function of the likelihoods *given an assumption
about the assets that the function signature does not encode and therefore
cannot test*. The bug is not in the arithmetic. **It is in the interface.** A
function that takes only `(p, impact)` pairs has no way to know that two entries
refer to the same asset, so it cannot be tested for the case that matters
without being told what that case is.

## PART 3 — THE FIX, AND THE INTERFACE CHANGE THAT PREVENTS IT (12 min)

There are two fixes and only one of them is a real fix.

**Fix 1: subtract the overlap inside `v1`.** Works, and leaves you in the same
place next month, because the next shared asset will not be the same pair of
threats and nothing will remind you the correction is needed.

**Fix 2: make the shared asset part of the data.** Group threats by the asset
they damage, combine within a group with inclusion–exclusion, then sum the
groups. Now the code *cannot* be wrong about a shared asset, because the shared
asset is the unit it operates on.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

A = 5400

def at_least_one(likelihoods):
    """P(at least one of these fires), by repeated inclusion-exclusion."""
    if not likelihoods:
        return F(0)
    p = likelihoods[0]
    for q in likelihoods[1:]:
        p = p + q - p * q
    return p

def v3(groups):
    """groups: {asset_value: [likelihood, ...]}. The asset is the unit."""
    total = F(0)
    for value, likelihoods in groups.items():
        total += at_least_one(likelihoods) * value
    return total

p1, p2 = F(3, 20), F(1, 20)
shared = {A: [p1, p2]}
distinct = {5400: [p1], 1200: [p2]}
print("one shared asset, v2 approach:", at_least_one([p1, p2]) * A)
print("one shared asset, v3:        ", v3(shared))
print("two distinct assets, v1:     ", p1 * 5400 + p2 * 1200)
print("two distinct assets, v3:     ", v3(distinct))
print("v3 agrees with v1 when the assets are distinct:",
      v3(distinct) == p1 * 5400 + p2 * 1200)
print()
print("and v3 is now impossible to misuse:")
print("v3(shared) =", v3(shared), " v1 on the same threats =", p1 * A + p2 * A)
```

Real output:

```
one shared asset, v2 approach: 2079/2
one shared asset, v3:         2079/2
two distinct assets, v1:       870
two distinct assets, v3:       870
v3 agrees with v1 when the assets are distinct: True

v3(shared) = 2079/2 v1 on the same threats = 1080
```

**`v3` reproduces `v1` exactly when the assets are distinct, and corrects it
exactly when they are shared.** That is the signature of a fix rather than a
patch: the old behaviour is preserved in every case where it was right, and
changed only where it was wrong.

The second-to-last line is the payoff. With `v3`, there is no code path in which
two threats hit one asset and get charged twice, because the dict key says
"this asset" and the function is written in terms of assets. You cannot call it
incorrectly without restructuring the data first.

- ☐  Why is "subtract the overlap in `v1`" a weaker fix than grouping by asset?
      One sentence: ______
- ☐  `v3`'s signature takes a **dict**. What is the interface change, stated as a
      rule for future code: ______
- ☐  Write the test that kills `v1` and passes `v3`. It must use the *same*
      inputs `v1` handles today plus one addition. What must it assert: ______

That last checkbox is the deliverable of the lesson. A test that distinguishes
`v1` from `v3` is a test that encodes a *world fact* — "two threats on one asset
cost that asset once" — rather than a *regression* on old output. It is the
only kind of test that can catch a bug whose arithmetic was never wrong.

## PART 4 — BUILD IT (8 min)

- ☐  `at_least_one(likelihoods)` in `riskkit.py`
- ☐  `expected_loss(groups)` — the `v3` interface, with a `ValueError` if any
      asset value is not positive or any likelihood is outside `[0, 1]`
- ☐  **Migrate your `THREATS` list**: add an `asset` field to every threat, and
      group by it. This is the change to your model, and it is the one that
      matters.
- ☐  A test asserting that grouping by a *distinct* asset per threat reproduces
      the old `v1` number exactly — so you can prove the migration did not
      silently change anything else
- ☐  A test asserting `at_least_one([p]) == p` for a single threat, which is the
      property `v1` silently assumed and never checked
- ☐  A test with the signature comment: `# kills v1, passes v3`

- ☐  After migrating, does your total EV go up, down, or stay the same? ______
      By how much, and is the direction right: ______

## PART 5 — CLOSE (3 min)

- ☐  `expected_loss(groups)` in the file, with the guard
- ☐  The test that distinguishes `v1` from `v3` exists and passes
- ☐  **In writing, two sentences: what the bug in `v1` actually was, and the
      general rule about interfaces that you are taking out of this lesson.**
      The second sentence should be about *what a function's inputs must encode*
      for the function to be testable.

## TURN IN — The Bug That Passes Every Test

1. `riskkit.py` with `at_least_one`, `expected_loss`, the migration, and all
   three tests
2. The Part 1, Part 2, and Part 3 outputs, run live
3. **Your sealed prediction from Friday**, brought out again, with a note on
   whether you predicted *this* bug
4. Your two sentences from Part 5
5. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

This is a real and repeated pattern in institutional risk reporting, and the
Taiwan case makes it concrete because the incidents are the ones the
government documents. When a ransomware event and a data-exposure notification
concern the same institution, the same servers, and the same calendar quarter,
the natural institutional response is to produce a cost figure per incident and
sum them. The two figures are not independent losses; they are two descriptions
of one loss, and adding them overstates the impact by exactly the cost of the
overlapping exposure — the rebuild that only happens once.

The national CERT's post-incident guidance and the Ministry of Digital Affairs'
framework both require that incident impact assessment identify **affected
assets explicitly** rather than accumulate per-incident costs, and the reason is
precisely this arithmetic. The guidance's phrasing is that cost figures must be
traced to assets so that overlapping effects are visible; without an asset
register there is no way to detect the double count, because the two incidents
arrive through different reporting channels and nobody is looking for the
overlap between them.

The second lesson — that the fix is an **interface**, not an arithmetic patch —
is the transferable one and it is the reason the ROC's review practice asks for
asset-level tracking rather than incident-level summaries. An incident-level
summary can be summed, and summing it is exactly the error. An asset-level view
cannot be summed, because the asset appears once in the register. The data
structure enforces the truth that the arithmetic could not.

Your `v3` is that register. It is why the shape of the data matters more than
the cleverness of the function, and it is the same principle as the
`likelihood_source` field on L14: **what the model cannot represent, the model
cannot get wrong — and what it cannot represent, it will get wrong quietly, in
a direction that looks conservative.**
