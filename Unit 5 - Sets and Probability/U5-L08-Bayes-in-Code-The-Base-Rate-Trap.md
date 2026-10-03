# U5 L08 — Bayes in Code: The Base-Rate Trap, Demonstrated

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.6 — implement Bayes' theorem exactly; sweep the false-positive rate and
explain in writing why a highly accurate detector can be nearly useless

---

## TODAY'S PURPOSE

Yesterday you did the arithmetic on paper and got 4.72%. Today you will write
four lines of code that reproduce it exactly, and then do the thing that actually
matters: **sweep the false-positive rate and watch the answer move.**

The code is trivial. The sweep is the lesson.

## PART 1 — THE FUNCTION, AND A CHECK AGAINST YOUR PAPER (10 min)

```python
try:
    from sympy import Rational, simplify
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

def bayes(prior, like_pos, like_neg, total):
    """P(A | test+).

    prior:     P(A), as a Fraction
    like_pos:  P(test+ | A), the sensitivity
    like_neg:  P(test+ | not A), the false-positive rate
    total:     ignored, kept so the call site reads like yesterday's tree
    """
    tp = like_pos * prior
    fp = like_neg * (1 - prior)
    return tp / (tp + fp)

p_disease = Rational(1, 1000)
p_test_pos = Rational(99, 100)      # sensitivity
p_test_neg = Rational(1, 50)        # false positive rate 2%
print("posterior:", simplify(bayes(p_disease, p_test_pos, p_test_neg, 1000)))
print("as percent:", float(bayes(p_disease, p_test_pos, p_test_neg, 1000)) * 100)
```

Real output:

```
posterior: 11/233
as percent: 4.721030042918455
```

- ☐  What did **you** get on paper yesterday? ______
- ☐  They match? ______ If not, which is wrong and how do you know: ______
- ☐  The `total` parameter is never used. Why did I leave it in? ______

That last checkbox is a real design question and I want your answer, not a
guess. An unused parameter is either a mistake or a deliberate readability
choice, and you should be able to say which one and why.

## PART 2 — THE SWEEP (12 min)

One input at a time. This is the part that changes how you think about
detectors.

```python
try:
    from sympy import Rational, simplify
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

def bayes(prior, like_pos, like_neg):
    tp = like_pos * prior
    fp = like_neg * (1 - prior)
    return tp / (tp + fp)

p_disease = Rational(1, 1000)
p_test_pos = Rational(99, 100)

# the same disease, the same test, only the false-positive rate changes
p_test_neg2 = Rational(1, 100)
post2 = bayes(p_disease, p_test_pos, p_test_neg2)
print("posterior, 1% FP:", simplify(post2), "->", float(post2) * 100, "percent")

# the extremes
print("posterior with 100% sensitivity, 1% FP:", simplify(bayes(p_disease, 1, p_test_neg2)))
print("posterior with 100% sensitivity, 0% FP:", simplify(bayes(p_disease, 1, 0)))
```

Real output:

```
posterior, 1% FP: 11/122 -> 9.01639344262295 percent
posterior with 100% sensitivity, 1% FP: 100/1099
posterior with 100% sensitivity, 0% FP: 1
```

The second line is the one to sit with. **Halving the false-positive rate —
making the test twice as good — moved the answer from 4.7% to 9.0%.** A
doubling. And it is still 9%, which is a number most people would call
unacceptable for a medical decision.

The third line is stranger and more important: a *perfect* test at a 1% base rate
gives you `100/1099`, which is about 9.1%. **Even a test that never misses and
never false-alarms tells you almost nothing when the disease is rare.** The
information is not in the test. It is in how rare the thing is.

- ☐  From 4.72% to 9.02% is a factor of about ______
- ☐  In one sentence: why does a *perfect* test still give 9% here? ______
- ☐  What would the base rate have to be for a perfect test to be genuinely
      decisive — and what does that tell you about which problems testing is the
      right tool for? ______

## PART 3 — TEN THOUSAND PEOPLE, IN CODE (12 min)

Yesterday you counted people. Now let the code count them, and compare.

```python
try:
    from sympy import Rational, simplify
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

N = 10000
diseased = int(N * 0.001)
tp = int(N * 0.001 * 0.99)
fp = int(N * 0.999 * 0.02)
print("of", N, "->", diseased, "diseased,", tp, "true positive,", fp, "false positive")
print("posterior:", simplify(Rational(tp, tp + fp)))
print("the 1% that is NOT diseased but tested positive:", fp)
```

Real output:

```
of 10000 -> 10 diseased, 9 true positive, 199 false positive
posterior: 9/208
the 1% that is NOT diseased but tested positive: 199
```

**199 versus 9.** Twenty-two false positives for every true one. The code and
your paper tree agree — `9/208` is 4.33%, and the small discrepancy from 4.72%
is entirely because 0.99 × 10 = 9.9 and `int()` truncated it. That truncation is
not a bug in the model; it is what happens when you insist on whole people.

- ☐  `9/208` as a percent: ______  Where does the difference from 4.72% come
      from, exactly? ______
- ☐  If you had used 100,000 people, would the truncation error matter more or
      less? ______
- ☐  Now the security version, in one sentence: *a filter with a 2% false
      positive rate against a 1-in-1,000 event rate tells an analyst that a
      given alert is a true event roughly ______ % of the time.* ______

- ☐  **Write the flip side too.** A 2% false-positive rate against a **1-in-2**
      event rate — the same detector, a much more common threat. Same code, one
      changed number. What is the posterior, and what does the identical
      detector look like now? ______

The last checkbox is the whole lesson in one question. **The detector did not
change. The answer changed by an enormous amount, because the base rate did.**
A rule with a stated false-positive rate and no stated base rate is not a rule;
it is a number someone liked the look of.

## PART 4 — BUILD IT INTO `contingency.py` (8 min)

- ☐  Add `bayes(prior, sensitivity, false_positive_rate)` accepting and returning
      `Fraction`, raising `ValueError` if any argument is outside `[0, 1]` or if
      the prior is 0 while the sensitivity is 1 (a `0/0`)
- ☐  Add `posterior_from_table(table, row, col)` — the same number read out of a
      contingency table instead of three rates, so you can prove the two agree
- ☐  Docstrings. The `bayes` docstring must say **which direction the false
      positive rate goes**; the sign of that argument is the single most common
      bug in this formula and a bad docstring is a bug factory

- ☐  Write the test that would catch a sign flip: ______

## PART 5 — CLOSE (3 min)

- ☐  The sweep runs, and you can state the shape of the curve in one sentence
- ☐  Your posteriors are exact `Fraction`s, not floats
- ☐  **In writing: the security version of Part 3, both directions, with real
      numbers from your run.** This is graded and it is graded on whether the
      second direction is actually there. Most people do the alarming one and
      stop.

## TURN IN — Bayes in Code

1. `contingency.py` with `bayes` and `posterior_from_table`, plus the guard
2. The Part 1, Part 2, and Part 3 outputs, run live
3. The two-direction security writeup from Part 5
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

The sweep in Part 2 is the argument against buying security tooling on the
strength of its accuracy numbers, and it is an argument a procurement committee
can be shown. A vendor quoting "99.7% detection accuracy" against a threat
population of one in a million has told you nothing at all; the same rule
against a threat population of one in ten is close to decisive. The ROC national
CERT's incident-response guidance and the Ministry of Digital Affairs' advisories
both push this specific framing, because the vendors selling the tooling have no
incentive to state the base rate and every incentive to state the accuracy.

The two-direction requirement in Part 3 is the habit worth building. Every alert
threshold you ever set is a choice about which population the rule will run
against, and a rule tuned for a rare targeted intrusion is a rule that will fire
on almost everything in a month of ordinary scanning — the same rule, the same
false-positive rate, a base rate six orders of magnitude higher, and now your
analysts are the ones generating the noise. In your Risk Simulator, "likelihood"
is not a property of the threat. **It is a property of the threat *in the
environment you are modelling*, and it is yours to justify in writing.** That
justification is the defense you write on L26, and the base rate is the first
thing a reader will check.
