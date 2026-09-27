# U5 L03 — `set` in Python: Build `setkit.py`, Then Check the Paper

**Date:** Friday, February 19, 2027
**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.3 — use Python's `set` type for the five operations; build `setkit.py`
and verify it against the hand counts from L02

---

## TODAY'S PURPOSE

Yesterday you counted regions in a Venn diagram with a pencil. Today you write
functions that compute the same five things, and then — this is the part that
matters — **you check the code against yesterday's paper.**

Not "does it run." Does it produce *your* numbers. If the two disagree, one of
you is wrong, and finding out which is the lesson.

## PART 1 — THE TYPE, AND ITS ONE SURPRISE (10 min)

```python
try:
    from fractions import Fraction
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

teams = {"ana", "bo", "cy", "di", "eli", "fen", "gus"}
hardware = {"bo", "di", "fen"}

print(sorted(teams & hardware))
print(sorted(teams | hardware))
print(sorted(teams - hardware))
print(sorted(teams ^ hardware))
print(len(teams), len(hardware))
```

Real output:

```
['bo', 'di', 'fen']
['ana', 'bo', 'cy', 'di', 'eli', 'fen', 'gus']
['ana', 'cy', 'eli', 'gus']
['ana', 'cy', 'eli', 'gus']
7 3
```

Two things to notice before you write anything.

**One: I wrapped everything in `sorted()`.** A Python set is *unordered* — it
guarantees the members are there, not that they arrive in any particular
sequence. Printing a set directly can give you a different order on a different
run. This matters enormously in three weeks when you generate a `manifest.sha256`
and commit it. Sorted output is deterministic; raw set output is not.

**Two: `teams - hardware` and `teams ^ hardware` printed the same thing.** That is
not a bug and not a coincidence — in this data the only overlap is the
hardware people, and they are in both, so "not in hardware" and "in exactly one"
coincide. It will not coincide in general. Yesterday's `A ^ B` was 1, 2, 3, 6, 7
and `A - B` was 1, 2, 3.

- ☐  Give me a two-set example where `A - B` and `A ^ B` differ, in one line:
      ______
- ☐  Why would you ever *want* to print a set unsorted? (Think: order matters
      to a human reading a list, not to a program.) ______

## PART 2 — MUTATION AND THE INVISIBLE COPY (8 min)

```python
try:
    from fractions import Fraction
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

teams = {"ana", "bo", "cy", "di", "eli", "fen", "gus"}
teams.add("hana")
teams.discard("ana")
teams.discard("nobody")
print(sorted(teams))

frozen = frozenset({"x", "y"})
print(isinstance(frozen, frozenset), sorted(frozen | {"z"}))
print("bo" in teams, "zed" in teams)
hardware = {"bo", "di", "fen"}
print(sorted(teams & hardware) == sorted(set.intersection(teams, hardware)))
print(sorted(teams & hardware) == {"bo", "di", "fen"})

fresh = {"ana", "bo"}
try:
    fresh.remove("nobody")
except KeyError as exc:
    print("KeyError:", exc)
```

Real output:

```
['bo', 'cy', 'di', 'eli', 'fen', 'gus', 'hana']
True ['x', 'y', 'z']
True False
True
False
KeyError: 'nobody'
```

The middle line is a trap worth ten seconds of your time. `sorted(teams & hardware)`
is a **list**; `set.intersection(...)` is a **set**. `['bo', 'di', 'fen'] == {'bo',
'di', 'fen'}` is `False`, and the reason is not the values — it is the *type*.
Python will not quietly coerce a list into a set to make your assertion pass,
and that refusal has saved this class a real amount of debugging time. If you
want to compare, make the types match, or compare sets to sets.

Also note `discard` did not raise on `"nobody"` while `remove` did. That is the
whole difference: `remove` is a statement that the element should be there;
`discard` is a request. In a threat model where a target id might have been
renamed, `discard` is the honest call and `remove` is the loud one.

- ☐  What does `{"a", "b"} == ["a", "b"]` evaluate to, and why is that the
      *correct* answer rather than a Python wart? ______
- ☐  Why would a `frozenset` be the right type for a set of *asset ids* you never
      intend to edit? ______

## PART 3 — BUILD `setkit.py` (15 min)

Create the file now. Four functions, no more, no less:

```
compmath-u5-risk-simulator
└── setkit.py
```

- ☐  `union(a, b)` — returns `a | b`
- ☐  `intersection(a, b)` — returns `a & b`
- ☐  `difference(a, b)` — returns `a - b`
- ☐  `symmetric_difference(a, b)` — returns `a ^ b`

Each one needs a **docstring that says what it returns in English**, because
L14 is the day a stranger has to read your code, and L26 is the day they will
try.

```python
try:
    from fractions import Fraction
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def union(a, b):
    """Return every element that is in a, in b, or in both."""
    return a | b

def intersection(a, b):
    """Return every element that is in both a and b."""
    return a & b

def difference(a, b):
    """Return the elements of a that are not in b."""
    return a - b

def symmetric_difference(a, b):
    """Return the elements in exactly one of a and b, never both."""
    return a ^ b

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
for name, fn in (("union", union), ("intersection", intersection),
                 ("difference", difference), ("symmetric_difference", symmetric_difference)):
    print("%-22s %s" % (name, sorted(fn(A, B))))
```

Real output:

```
union                  [1, 2, 3, 4, 5, 6, 7]
intersection           [4, 5]
difference             [1, 2, 3]
symmetric_difference    [1, 2, 3, 6, 7]
```

- ☐  Add a fifth function `complement(a, universe)` that raises `ValueError` if
      `a` is not a subset of `universe`. **Why is that a real error and not a
      fussy one?** Answer: ______
- ☐  Write the test for it: ______

## PART 4 — THE CHECK AGAINST YESTERDAY'S PAPER (8 min)

Now the actual assignment. Yesterday's club problem, in code.

`A` = CS club, 34 members. `B` = chess club, 22 members. 9 in both. 3 in neither,
120 total.

- ☐  Build the sets from the *sentence* you were given, not from the region
      table. Write the code that constructs `A_only`, `both`, `B_only`,
      `neither` from the four facts, and print the four region counts.
- ☐  Print your total and confirm it is 120.
- ☐  Now print `len(union(A, B))` and `len(intersection(A, B))` from the raw sets
      and confirm they match the region arithmetic.
- ☐  **Compare every number to your photographed L02 tables.** Mark each one
      `match` or `mismatch` in the table below.

| quantity | my L02 count | `setkit.py` | match? |
|---|---|---|---|
| `A` only | | | |
| `B` only | | | |
| both | | | |
| union | | | |
| symmetric difference | | | |
| neither | | | |
| total | | | |

- ☐  If anything mismatched: which side was wrong, and how do you know? ______
- ☐  If nothing mismatched: what would you have to change to make it fail, so
      you know the check is real? ______

That last checkbox is the important one. **A test that has never failed is not
evidence of anything.** I would rather see you deliberately break `difference`
and watch the paper disagree than see seven green ticks.

## PART 5 — CLOSE (4 min)

- ☐  `setkit.py` is committed and imports cleanly from a fresh terminal
- ☐  Every function has a docstring
- ☐  The L02 comparison table is filled in, mismatches or not
- ☐  You have written down one question you cannot answer yet. Write it here:
      ______

## TURN IN — `setkit.py`

1. `setkit.py` in the repo — four functions, plus `complement` with its
   `ValueError`, each with a docstring
2. The four-fact reconstruction from Part 4, with its output
3. The L02-vs-code comparison table, photographed, with your verdict on which
   side was wrong if anything disagreed
4. **No pip installs.** Standard library and SymPy only. If something is missing,
   tell me — do not install it.

## 🇹🇼 TAIWAN CONTEXT

`discard` versus `remove` is the difference between a log line and an outage.
The Monday internet-exposed routers in Unit 4, and the many small businesses
that still run them, produce their worst incidents from code paths that assume
input is well-formed: an asset id that no longer exists, a record deleted by a
different team an hour ago, an entry the migration script did not write. A
tool that raises on a missing key is a tool that tells you the truth. A tool
that quietly continues is the one you read about afterward.

The sorted-output rule is not style. When the ROC national CERT publishes an
indicator-of-compromise list, those indicators are generated by enumerating
hashes and IPs, and a set iterated in arbitrary order produces a different file
every time — which makes the "did anything change?" question unanswerable. You
will generate a manifest in three weeks. Deterministic order is what makes it a
manifest and not a coin flip.
