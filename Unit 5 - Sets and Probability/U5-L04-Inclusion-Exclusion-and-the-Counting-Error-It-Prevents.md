# U5 L04 — Inclusion–Exclusion, and the Counting Error It Prevents

**Date:** Monday, February 22, 2027
**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.4 — apply inclusion–exclusion to two and three sets; explain precisely
which counting error the formula exists to prevent

---

## TODAY'S PURPOSE

On L02 you filled in a Venn diagram and the union worked. Today is the part
where you stop drawing and start *adding*, and where the first genuinely
dangerous habit of this course shows up: **adding counts of overlapping groups
as if they were disjoint.**

This is not a cute error. It is the single most common way a real analysis gets
a number that is too big, and you are about to build a program whose entire
output is a number.

## PART 1 — THE ERROR, NAMED AND SIZED (10 min)

A school of 120 students: 54 are in the band, 41 are in the club. Both numbers
are true. Add them and you have 95.

```python
try:
    from fractions import Fraction
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

in_band, in_club, both, total_students = 54, 41, 18, 120
print("naive union:", in_band + in_club)
print("true union:", in_band + in_club - both)
print("anyone in neither:", total_students - (in_band + in_club - both))
```

Real output:

```
naive union: 95
true union: 77
anyone in neither: 43
```

You just told the school that 43 students are in neither club. In fact **43
students are in neither club** — the number is right. But you got it by
accident, through a subtraction of 18 that you had no reason to make.

- ☐  The naive answer overstates the union by exactly ______
- ☐  Why does that error *always* run one way and never the other? ______
- ☐  A classmate says "but 95 is less than 120, so it's probably fine." Reply in
      one sentence: ______

That reply matters. **The overcount is invisible whenever the group is small
relative to the whole, and that is exactly when the error is hardest to
notice.**

## PART 2 — THE TWO-SET FORM, IN CODE (10 min)

```python
try:
    from fractions import Fraction
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def union_size(a, b, both):
    """Inclusion-exclusion for two sets, given |A|, |B|, and |A n B|."""
    return a + b - both

data = {"wifi": 78, "wired": 46, "both": 33, "universe": 100}
u = union_size(data["wifi"], data["wired"], data["both"])
print("wifi or wired:", u)
print("exactly one:", data["wifi"] + data["wired"] - 2 * data["both"])
print("neither:", data["universe"] - u)
```

Real output:

```
wifi or wired: 91
exactly one: 58
neither: 9
```

Note the *exactly one* line: `a + b - 2*both`, not `- both`. The intersection
was counted twice in the naive sum, and it has to leave the picture entirely —
so it is subtracted twice. Getting that `- 2` wrong is the second most common
error in this topic and it silently produces a number that looks reasonable.

- ☐  Explain in words why "exactly one" needs `- 2 * both` and not `- both`:
      ______
- ☐  If someone tells you 78 use wifi, 46 use wired, and 33 use **both**, how
      many use **only** wifi? Show the subtraction: ______

## PART 3 — THREE SETS, WHERE IT GETS SERIOUS (12 min)

Two sets, one correction. Three sets, and the correction itself contains
overlaps that have to be corrected back.

```python
try:
    from fractions import Fraction
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

# 100 students: 58 in CS, 36 in band, 22 in chess
# pairwise: 14 in CS and band, 8 in CS and chess, 6 in band and chess
# 2 in all three
three = {"a": 58, "b": 36, "c": 22, "ab": 14, "ac": 8, "bc": 6, "abc": 2}
naive3 = three["a"] + three["b"] + three["c"]
print("naive three:", naive3)
print("true three:", naive3 - (three["ab"] + three["ac"] + three["bc"]) + three["abc"])
print("overcount:", (three["ab"] + three["ac"] + three["bc"]) - three["abc"])

abc = three["abc"]
regions = [three["a"] - three["ab"] - three["ac"] + abc,
           three["b"] - three["ab"] - three["bc"] + abc,
           three["c"] - three["ac"] - three["bc"] + abc,
           three["ab"] - abc, three["ac"] - abc, three["bc"] - abc, abc]
print("regions a,b,c,ab,ac,bc,abc:", regions)
print("in at least one:", sum(regions), " outside:", 100 - sum(regions))
```

Real output:

```
naive three: 116
true three: 90
overcount: 26
regions a,b,c,ab,ac,bc,abc: [38, 18, 10, 12, 6, 4, 2]
in at least one: 90  outside: 10
```

Follow the `+ abc` on those region lines. The `A n C` figure of 8 **includes**
the 2 students in all three, so when you want the "A and C but not B" region you
must add the 2 back. This is the same correction as the union formula, applied
one level down, and it is the step people skip.

- ☐  The naive sum overstates by 26, not 14. Where does the extra 12 come from,
      in one sentence? ______
- ☐  Fill in the eight-region table from L02 Part 4 and check it against the
      `regions` list above. All eight match? ______
- ☐  Sum your eight L02 regions. If you got 120 total, was the eighth region 10,
      26, or something else? ______

## PART 4 — BUILD IT INTO `setkit.py` (8 min)

Add to the file you started Friday:

- ☐  `union_size(a, b, both)` — the size-level version from Part 2
- ☐  `exactly_one_size(a, b, both)` — the `- 2*both` version
- ☐  `union_size_three(a, b, c, ab, ac, bc, abc)` — the full formula, with a
      `ValueError` if `abc > min(ab, ac, bc)`, because **that inequality is a
      fact, not a preference**
- ☐  Each one gets a docstring and one test

- ☐  Write the test that would catch someone dropping the `+ abc` term: ______
- ☐  What should `union_size_three` do if `abc` is 5 but `ac` is 3? What does that
      model say about reality? ______

## PART 5 — CLOSE (5 min)

- ☐  `setkit.py` imports cleanly, five-plus functions, all documented
- ☐  You can state the two-set and three-set formulas from memory, on paper,
      without looking
- ☐  **Write down one number you have ever added that was really a union of
      overlapping groups.** This is the honest version of the lesson: ______

## TURN IN — Inclusion–Exclusion

1. `setkit.py` with `union_size`, `exactly_one_size`, `union_size_three`, and
   the `ValueError` guard
2. The Part 3 output, run live
3. **Part 5's last checkbox, in writing.** This is graded. A real example beats a
   hypothetical one, and "I can't think of one" is an acceptable answer only if
   you can defend it.

**No pip installs.** Standard library and SymPy only. Tell me if something is
missing.

## 🇹🇼 TAIWAN CONTEXT

Double-counting is the mechanism behind a large share of the misreported
breach-notification numbers that reach the ROC national CERT and the Ministry
of Digital Affairs. An incident touches a host, an account, a subnet, and a
user; a status page that counts "affected entities" as the sum of those four
reports a figure several times the size of the real one, and the difference
between the reported number and the real number is almost always the
overlapping set. It looks like over-reporting rather than under-reporting, which
is why it survives review.

The practical rule that falls out of today: **when two groups can overlap, their
counts do not add, and you have to know the size of the overlap to get anything
right.** In your Risk Simulator that overlap is a specific object — two threats
that hit the same asset — and on L20 it is the bug that survives every test you
write. You will not see it coming from this lesson. You will see it on L20.
