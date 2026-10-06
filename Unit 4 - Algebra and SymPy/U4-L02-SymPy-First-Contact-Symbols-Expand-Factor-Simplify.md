# U4 L02 — SymPy First Contact: Symbols, Expand, Factor, Simplify

**LO:** declare symbols, run the four algebraic verbs, and use round-tripping as a self-check.

Yesterday's idea, today in the machine. We do not do anything you could not do
by hand — we do it faster, and we make the machine **show its work** so you can
audit it.

## PART 1 — DOES THE SERVER HAVE SYMPY? (5 min, do this first)

Open your VS Code workspace terminal:

```bash
pwd
cd ~/compmath-u4-sympy-lab
git pull
ls
```

Then run the guard you typed yesterday:

```bash
python3 sympy_check.py
```

- ☐  It printed a clear confirmation that SymPy imported
- ☐  **If it printed the "not installed" message, stop and tell me.** Do not
     `pip install` anything yourself. I need to know which servers are missing it
     before the unit depends on it.

Also confirm the interpreter you are using:

```bash
python3 -c "import sympy, sys; print(sys.executable); print(sympy.__version__)"
```

Write the two lines of output here. The first one is the answer to "which Python
is this." ______

## PART 2 — THE FOUR VERBS, ONE AT A TIME (20 min, code-along)

Create `l02_lab.py`. Type each block, run it, and **read the output before moving
on.** Guessing what it will print and then checking is the fastest way to learn
this library.

```python
try:
    from sympy import Symbol, expand, factor, simplify, together, cancel
    HAVE_SYMPY = True
except ImportError:
    HAVE_SYMPY = False

if not HAVE_SYMPY:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")

x = Symbol('x')                 # declare the symbol before using it
y = Symbol('y')

print(expand((x + 2) * (x + 5)))
print(factor(x**2 + 7*x + 10))
print(simplify(2 * x / 2))
print(simplify((x**2 - 4) / (x - 2)))
print(cancel((x**2 - 4) / (x - 2)))
print(together(x/3 + y/4))
```

Predictions, written **before** you run it:

| expression | I predict the output will be | actually printed | surprise? why? |
|---|---|---|---|
| `expand((x + 2) * (x + 5))` | | | |
| `factor(x**2 + 7*x + 10)` | | | |
| `simplify(2 * x / 2)` | | | |
| `simplify((x**2 - 4) / (x - 2))` | | | |
| `cancel((x**2 - 4) / (x - 2))` | | | |
| `together(x/3 + y/4)` | | | |

**The row that matters is `simplify((x**2 - 4) / (x - 2))`.** It *does* print
`x + 2` — and on this version that is the correct result **for the expression as
written**, because `x` is a general symbol, not the number 2. Nobody told it
`x = 2`, so the cancelled form is right.

But the identity is only true for `x ≠ 2`. At `x = 2` the original is `0/0`.
Check it yourself, and the difference between the two tools becomes visible:

```python
print(simplify((x**2 - 4) / (x - 2)).subs(x, 2))   # 4  <- the simplified form
print((x**2 - 4).subs(x, 2) / (x - 2).subs(x, 2))  # nan <- the original
```

- ☐  What is `cancel` for, then, if `simplify` already cancelled that? ______
- ☐  Which of those two numbers is "the right answer to the original question,"
     and how would you know which one to trust without reading the docs? ______

**The lesson generalizes.** Any time you cancel, divide, or take a square root,
you have possibly changed the answer at one specific input. On a midterm that
costs a point. In a program it costs a crash, or worse, a wrong answer nobody
notices. The symbol is not the number, and simplification is a claim about the
general case.

## PART 3 — ROUND-TRIPPING AS A SELF-CHECK (20 min)

The habit from L01, written as code. If `factor(expand(f))` does not return `f`,
something is wrong — either a typo in `f` or a genuine identity you found.

```python
def roundtrip(expr_str):
    """Expand then factor an expression written as a string; report agreement."""
    from sympy import sympify
    original = sympify(expr_str)
    there_and_back = factor(expand(original))
    ok = simplify(there_and_back - original) == 0
    return original, there_and_back, ok

trials = [
    "(x + 2) * (x + 5)",
    "(x - 1)**3",
    "x**4 - 1",
    "(x**2 + 1) * (x**2 - 1)",
    "x**2 - 2",
]
for t in trials:
    orig, back, ok = roundtrip(t)
    print("%-28s -> %-24s %s" % (t, back, "OK" if ok else "MISMATCH"))
```

- ☐  All five round-trip? ______
- ☐  If any failed, **do not delete the failing case.** Paste it here and
     explain the failure in a comment in the file. ______

## PART 4 — BUILD YOUR OWN TOOLKIT MODULE (20 min)

Start `symkit.py`. This is the module you will import for the rest of the unit,
so get the docstring right.

```python
"""symkit.py — Unit 4 algebraic helpers.

Q1: What is the one thing SymPy will not do for me automatically?
Q2: Why does cancel() exist separately from simplify()?
Q3: What does factor(expand(f)) == f actually *prove*? Be careful.
Q4: What breaks if a user passes a string instead of an expression?
Q5: Which of these functions would be worst to ship broken, and why?
"""

try:
    from sympy import Symbol, expand, factor, simplify, sympify
    x = Symbol('x')
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")


def expand_str(expr_str):
    """Expand an expression given as a string. Raise ValueError if it is not one."""
    try:
        return expand(sympify(expr_str))
    except Exception as exc:
        raise ValueError("cannot expand %r: %s" % (expr_str, exc))


def factor_str(expr_str):
    """Factor an expression given as a string. Raise ValueError if it is not one."""
    try:
        return factor(sympify(expr_str))
    except Exception as exc:
        raise ValueError("cannot factor %r: %s" % (expr_str, exc))


def roundtrips(expr_str):
    """Return True if factoring the expansion of expr_str returns it unchanged."""
    e = sympify(expr_str)
    return simplify(factor(expand(e)) - e) == 0
```

Then a driver, `test_symkit.py`, that prints `all tests passed`:

```python
import symkit

CASES = ["(x + 2) * (x + 5)", "(x - 1)**3", "x**4 - 1"]

for case in CASES:
    if not symkit.roundtrips(case):
        print("FAIL roundtrip", case)
    else:
        print("ok  roundtrip", case, "->", symkit.factor_str(case))

# the bad input must raise ValueError, not a traceback
for bad in ["x +", "2 **", "((x"]:
    try:
        symkit.expand_str(bad)
    except ValueError:
        print("ok  rejected", bad)
    except Exception as exc:
        print("FAIL wrong exception for", bad, type(exc).__name__)
    else:
        print("FAIL accepted", bad)

print("all tests passed")
```

- ☐  `python3 test_symkit.py` prints `all tests passed`
- ☐  No failing test was deleted to get there
- ☐  The module docstring answers all five questions in your own words

## PART 5 — CLOSE-OUT (5 min)

- ☐  Commit and push. `git status` clean.
- ☐  Write one line in your notebook: the single SymPy behaviour that surprised
     you most today, and one line on whether it surprised you **correctly** or
     **incorrectly**. ______

That second half is the point. A tool can surprise you rightly — the 0/0
behaviour from Part 2 is a correct surprise — or wrongly, because you expected
something that was never guaranteed. You are learning to tell them apart.

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. `symkit.py` and `test_symkit.py`, pushed
2. A photo of your **Part 2 prediction table**, filled in — the *before* column
   is graded, not the after column
3. The two outputs from **Part 1**: the interpreter path and the SymPy version
4. One paragraph: which Part 2 row surprised you, and did the library surprise
   you correctly or incorrectly?

**Your predictions are the graded part.** Getting `simplify((x**2 - 4) / (x - 2))`
wrong on purpose — writing what you *expected* it to return — is worth more than
a screenshot of it returning the truth. I need to know what you assumed.

## 📋 PREVIEW OF TOMORROW

**Next:** L03 — paper. You hand-solve, then predict what the machine
will say, then check. Same four verbs, no laptop, and the place where the two
versions of algebra start to disagree in ways worth noticing.

**Bring tomorrow:** pencil and notebook. Not the laptop. Genuinely not.

## 🇹🇼 TAIWAN CONTEXT

One habit worth starting now: keep Unit 4 algebra errors in one place. Start a
page in your notebook titled **Algebra Error Log** with two columns — *what I
wrote* and *what it should have been*. L08 is built entirely out of that page,
and pages you start today are worth more than ones you start in L03.
