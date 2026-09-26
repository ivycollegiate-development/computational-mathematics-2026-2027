# U3 L23 — Lab: A Statistics Library Others Can Trust

**LO:** build a tested, documented module with honest error handling — the
smallest thing a stranger can rely on.

Last lab of the unit. You have written statistics code five times now: once
each in L03, L05, L08, L14, and L21. Today you do the part nobody assigns:
you make it into a **thing other people can use without breaking**.

The bar is not "it works on my data." The bar is: someone else can call it,
get a correct answer or a **clear error**, and never be misled about which one
they got.

## PART 0 — THE CONTRACT (10 min)

Write these rules down before you write code. You will test against them.

```text
R1. mean(v)          -> float. Error on an empty list.
R2. median(v)        -> float. Works for odd and even n.
R3. mode(v)          -> value, or None if every value is unique.
R4. stdev(v)         -> float (population, divide by n).
R5. percentile(v, p) -> float. p in [0, 1], matching U3 L08/L14/L21.
R6. five_number(v)   -> (min, q1, median, q3, max)
R7. iqr_fences(v)    -> (lo, hi)
R8. outliers(v)      -> list, may be empty
R9. describe(v)      -> readable multi-line report
R10. Every error is a ValueError with a message that names the problem.
R11. Keep the conventions you already use: percentile takes 0-1, and stdev is
     population. A library that contradicts the rest of your own work is a
     new source of bugs, not a clean slate.
```

**R4 is a decision, not a fact.** Population or sample? Population divides by
`n`; sample divides by `n - 1` and needs at least 2 values. Pick **population**
for this module, because you are describing a dataset that *is* the
population of interest — the 120 members are not a sample from a larger world.
Document the choice in the docstring, because a reader who does not know your
choice will misread every number you produce.

## PART 1 — THE CORE, WITH TESTS FIRST (25 min)

Write `statslib.py`:

```python
"""Descriptive statistics. Population standard deviation (divides by n)."""

def _check(values):
    """Return values as a list of floats, or raise ValueError."""
    if values is None:
        raise ValueError("values is None; expected a sequence of numbers")
    out = []
    for v in values:
        try:
            out.append(float(v))
        except (TypeError, ValueError):
            raise ValueError("non-numeric value: %r" % (v,))
    if not out:
        raise ValueError("empty sequence: need at least one value")
    return out
```

Now every function **starts** with `_check`, including `stdev`, which must
additionally reject a single value.

### The test suite

Write `test_statslib.py` **in the same file, below the functions**, guarded:

```python
if __name__ == "__main__":
    test_mean()
    test_median()
    ...
    print("all tests passed")
```

**Put the tests in the same file, not a separate one.** That is deliberate. A
separate test file is a file someone can forget to run; tests at the bottom of
the module are impossible to delete without deleting the code. This matters
because your dashboard in L17 imports `stats_engine` — and it worked, in part
because `test_engine()` never ran at import time. Same fix, same reason.

### The tests you must write

```python
def test_mean():
    assert mean([2, 4, 4, 4, 5, 5, 7, 9]) == 5.0
    assert mean([10, 20]) == 15.0
    assert mean([7]) == 7.0

def test_median():
    assert median([1, 3, 2]) == 2            # odd n
    assert median([4, 1, 3, 2]) == 2.5      # even n, interpolated

def test_mode():
    assert mode([1, 2, 2, 3]) == 2
    assert mode([1, 1, 2, 2]) is None       # genuine tie -> no single mode
    assert mode([5, 5, 5, 9, 9]) == 5      # NOT a tie: 5 occurs 3x, 9 only 2x
    assert mode([1, 2, 3]) is None          # all unique -> no mode

def test_stdev():
    # population stdev of [2,4,4,4,5,5,7,9] is exactly 2.0
    assert abs(stdev([2, 4, 4, 4, 5, 5, 7, 9]) - 2.0) < 1e-9
    assert stdev([5, 5, 5]) == 0.0
    assert stdev([5]) == 0.0          # population: one value has no spread
    expect_error(lambda: stdev([]), "empty")

def test_percentile():
    assert percentile([1, 2, 3, 4], 0) == 1
    assert percentile([1, 2, 3, 4], 1) == 4
    assert percentile([1, 2, 3, 4], 0.5) == 2.5
    expect_error(lambda: percentile([1, 2], 1.5), "between 0 and 1")
    expect_error(lambda: percentile([1, 2], -0.1), "between 0 and 1")

def test_five_number():
    # n=5 -> p25 lands exactly on index 1, p75 on index 3. No interpolation.
    # n=5 -> p25 lands exactly on index 1, p75 on index 3. No interpolation.
    assert five_number([1, 2, 3, 4, 5]) == (1, 2.0, 3.0, 4.0, 5)

def test_iqr_and_outliers():
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
    lo, hi = iqr_fences(v)
    assert outliers(v) == [100]
    assert outliers([1, 2, 3]) == []          # empty is a valid answer
```

And the helper, so your error tests are one line each:

```python
def expect_error(fn, must_mention):
    try:
        fn()
    except ValueError as e:
        assert must_mention in str(e), \
            "message %r does not mention %r" % (str(e), must_mention)
        return
    raise AssertionError("expected a ValueError, none was raised")
```

**Note `stdev([5]) == 0.0`.** Population standard deviation of a single value
is 0.0 — arithmetically fine, statistically meaningless. Sample stdev would
be undefined, because you cannot divide by `n - 1 = 0`. **Your R4 choice
decides which of these you get**, and because you chose population, the test
above asserts 0.0.

Write that assertion, get it passing, and be able to say in one sentence why
population was the right call for this data. That you can defend a convention
you *chose* — rather than inherited it — is the difference between using a
library and trusting one.

Run it:

```bash
python3 statslib.py
```

Every assertion must pass. **A test that fails is doing its job** — do not
delete it to get a clean run. Fix the function or fix the test, and know which
one you changed and why.

**Expect at least one assertion to fail on your first run.** Two of the tests
above are there precisely because they are easy to get wrong:

- `mode([5,5,5,9,9])` looks like a tie and is not — 5 appears **three** times
  and 9 only twice, so the mode is 5. A tie means the *top count is shared*,
  which is what `[1,1,2,2]` is and `[5,5,5,9,9]` is not.
- `five_number([1,2,3,4,5])` looks like it should give 1.5 and 4.5 for the
  quartiles. It does not. With n = 5, `k = (5-1) x 0.25 = 1.0` lands exactly on
  an index, so there is nothing to interpolate between and you get **2.0 and
  4.0**.

**When a test fails, decide whether the test or the function is wrong, and
write down which.** Both of the traps above are cases where *your first
instinct* was the wrong one. The failure is the lesson.

## PART 2 — HONEST ERRORS (20 min)

A library that returns `None` for an error is a library whose callers cannot
tell a real answer from a failure. Raise instead.

```python
def show_error(fn):
    """Call fn and print its error, or say it succeeded. For the report."""
    try:
        result = fn()
        print("  returned %r  (no error raised)" % (result,))
    except ValueError as e:
        print("  ValueError: %s" % e)
```

Write a demonstration block (below the tests, in its own `if
__name__ == "__main__":` section — or a second guard, your choice) that tries
**six bad calls** and prints what happened:

```python
if __name__ == "__main__":
    for bad in [lambda: mean([]),
                lambda: mean([1, "abc"]),
                lambda: median(None),
                lambda: percentile([1, 2, 3], 1.5),
                lambda: percentile([1, 2, 3], -0.5),
                lambda: five_number([])]:
        show_error(bad)
```

For each, your notes must record whether you got a clear `ValueError` or a
traceback or a wrong answer:

| bad call | got | message clear? |
|---|---|---|
| `mean([])` | | |
| `mean([1, "abc"])` | | |
| `median(None)` | | |
| `percentile([1,2,3], 1.5)` | | |
| `percentile([1,2,3], -0.5)` | | |
| `five_number([])` | | |

**R10 is the whole point of this part.** "list index out of range" is not an
error message; it is a leak. "empty sequence: need at least one value" is.

## PART 3 — THE REPORT (20 min)

```python
def describe(values):
    """Return a readable report as a single string."""
    v = _check(values)
    f = five_number(v)
    iqr = f[3] - f[1]
    out = outliers(v)
    lines = [
        "n = %d" % len(v),
        "mean   = %.2f" % mean(v),
        "median = %.2f" % median(v),
        "mode   = %s" % (mode(v),),
        "stdev  = %.2f  (population, divides by n)" % stdev(v),
        "min    = %.2f" % f[0],
        "q1     = %.2f" % f[1],
        "q3     = %.2f" % f[3],
        "max    = %.2f" % f[4],
        "IQR    = %.2f" % iqr,
        "fences = (%.2f, %.2f)" % iqr_fences(v),
        "outliers (%d): %s" % (len(out), out if out else "none"),
    ]
    return "\n".join(lines)
```

Now run it on three datasets and paste the output:

```bash
python3 statslib.py
```

1. the donations file (200 values) ______
2. `Spend_USD` from the project dataset ______
3. `[2,4,4,4,5,5,7,9]` ______

**Then answer, in your notes:**

4. For the donations data, `describe` reports a mean of **716.07** and a
   median of **242.76**. A reader glances at the report and sees both. What
   single line would you add to that report so nobody quotes 716.07 as
   "typical"? ______
5. The report says `stdev 6346.21 (population, divides by n)`. Is that number
   useful to a reader? Why or why not? ______
6. Your `outliers` line for `Spend_USD` will list **14** values, several of
   which (510.87, 544.98) are ordinary. Should `describe` print them all, print
   a count, or do something else? Defend your choice in one sentence. ______

**Question 6 is the one I care about.** A report that lists outliers without
saying what to do about them pushes a decision onto a reader who does not have
the context to make it.

## PART 4 — DOCUMENT IT (15 min)

Add a module docstring that answers, for a stranger:

- What does this module compute? ______
- **Population or sample standard deviation?** ______
- Does `percentile` take 0–1 or 0–100? (It is 0–1. Say why that matches
  U3 L08, L14, and L21 rather than contradicting them.) ______
- What happens on bad input? ______
- What is `mode` for a tie? ______

Then verify the docstring is **true**:

```python
help(stdev)
```

If the docstring says one thing and the code does another, the code is wrong.
The tests cannot catch this one; only reading can.

## TURN IN — THE LIBRARY (due 11:59 PM tonight)

Push `statslib.py` and the three report outputs. In the Classroom post, state:

1. **Your R4 decision** (population or sample) and the one-sentence reason
2. **Your test count** and the number that passed
3. **Your answer to question 4** — the line that stops 716.07 being read as
   typical
4. **Your answer to question 6** — what `describe` does about ordinary values
   in the outlier list
5. One test you wrote that you are **surprised** passed, and why

**Item 5 is the graded one.** Everyone writes tests that confirm what they
expected. A test that passes when you did not expect it to is either a lucky
boundary case or evidence that a function does something you did not
intend — and knowing the difference is what separates code that works from
code you understand.

Keep the terminal open — spot-checks.
