# U4 L04 — Solving Systems and Reading the Whole Answer

**LO:** solve systems with SymPy, and read the three possible answer shapes — point, nothing, or family.

Yesterday you hand-solved and predicted. Today you find out how often you were
right, and then you learn the part that actually matters for the rest of the
unit: **`solve` has three possible shapes of answer, not one.**

## PART 1 — CHECK YOUR PREDICTIONS (10 min)

Open your L03 paper next to the keyboard. Then:

```bash
cd ~/compmath-u4-sympy-lab
git pull
python3 l03_check.py
```

where `l03_check.py` is the block from the bottom of yesterday's lesson. Fill in
the *real* column and compute the Part 4 audit for real:

| section | value right | form right | form I actually got | verdict |
|---|---|---|---|---|
| linear (1–5) | /5 | /5 | | |
| quadratic (6–9) | /4 | /4 | | |
| two-symbol (10–12) | /3 | /3 | | |

**Do not rewrite your predictions.** If you got a form wrong, the wrong
prediction is the evidence.

- ☐  Your worst section was ______ and the mistake was ______

## PART 2 — THREE SHAPES, NOT ONE (20 min, this is the lesson)

Run each of these and **write down the exact type** of what comes back. The
`type(...)` is printed for you; your job is to say what it *means*.

```python
from sympy import Symbol, solve, symbols
x, y = symbols('x y')

# 1. exactly one solution
r1 = solve([2*x + 3*y - 12, 5*x - 2*y - 4], [x, y])
print("unique   :", r1, type(r1))

# 2. no solution — the equations contradict
r2 = solve([x + y - 1, x + y - 2], [x, y])
print("none     :", r2, type(r2))

# 3. infinitely many — the second equation is a multiple of the first
r3 = solve([x - y - 1, 2*x - 2*y - 2], [x, y])
print("infinite :", r3, type(r3))

# 4. infinitely many — only one real equation, two unknowns
r4 = solve([x - y - 1], [x, y])
print("underdet :", r4, type(r4))
```

Record:

| case | output | what the free symbol `y` means | how would a person miss this? |
|---|---|---|---|
| unique | | | |
| none | | | |
| infinite (2 eqs) | | | |
| underdetermined | | | |

**The critical distinction in rows 3 and 4.** Both return a dict whose value
still mentions a symbol. In row 4 that is because there genuinely is not
enough information. In row 3 there *is* enough information — but it is
redundant, and SymPy had no way to know you meant one of the two equations to
be a copy. **The output is the same shape and the mathematics is different.**

- ☐  How could a program tell rows 2 and 3 apart if it were not told which case
     to expect? One sentence. ______
- ☐  Which of these four cases is the most dangerous in a program that stores
     results, and why? ______

Row 2 is the dangerous one. `[]` is falsy in Python, so code written as
`if solve(...):` silently treats "no answer" as "false" and a valid solution
list also has to be checked for emptiness deliberately.

```python
sol = solve([x + y - 1, x + y - 2], [x, y])
print("bool(sol) =", bool(sol))          # False
print("len(sol)  =", len(sol))           # 0  <- the honest test
```

## PART 3 — BUILD `solve_system` FOR REAL (25 min)

Add this to `symkit.py`. It must return a **labelled** result, because the
three shapes are not interchangeable and a bare `[]` loses the difference.

```python
def solve_system(eq_strs, sym_names):
    """Solve a linear system given as strings.

    Returns a dict with exactly one key:
      'unique'     -> the {symbol: value} mapping
      'none'       -> None, the system contradicts itself
      'family'     -> a {symbol: expression} mapping that still contains a
                      free symbol; the caller must decide if that is allowed
    Raises ValueError on anything it cannot parse.
    """
    from sympy import sympify, solve, symbols, simplify
    syms = symbols(' '.join(sym_names))
    if not isinstance(syms, tuple):
        syms = (syms,)
    try:
        eqs = [sympify(s) for s in eq_strs]
    except Exception as exc:
        raise ValueError("cannot parse equations %r: %s" % (eq_strs, exc))

    ans = solve(eqs, list(syms))
    if not ans:
        return {"unique": None, "none": True, "family": None}
    if any(v.free_symbols for v in ans.values()):
        return {"unique": None, "none": False, "family": ans}
    return {"unique": ans, "none": False, "family": None}
```

Test it, and do not remove a case that fails:

```python
import symkit

checks = [
    (["2*x + 3*y - 12", "5*x - 2*y - 4"], ['x', 'y'], "unique"),
    (["x + y - 1", "x + y - 2"],          ['x', 'y'], "none"),
    (["x - y - 1", "2*x - 2*y - 2"],      ['x', 'y'], "family"),
]
for eqs, names, expected in checks:
    got = symkit.solve_system(eqs, names)
    verdict = "ok" if expected in got and got[expected] is not None or got["none"] else "CHECK"
    print("%-8s expected=%-7s -> %s" % (verdict, expected, got))
```

- ☐  `python3 test_symkit.py` still prints `all tests passed`
- ☐  Add the three new cases to that test file, properly
- ☐  A caller that asks for `unique` on the `family` case gets a clear error
      telling it the system is underdetermined — implement that, with
      `ValueError` and a sentence naming what happened

## PART 4 — VERIFY YOUR OWN SOLUTION (10 min)

The habit from L02, applied to systems. Never trust a solver; check its answer.

```python
from sympy import symbols, simplify
x, y = symbols('x y')

def verify(eq_strs, solution):
    """True only if every equation is satisfied by the solution."""
    from sympy import sympify
    ok = all(simplify(sympify(e).subs(solution)) == 0 for e in eq_strs)
    return ok

good = {x: 36/19, y: 52/19}
bad  = {x: 1, y: 1}
print(verify(["2*x + 3*y - 12", "5*x - 2*y - 4"], good))   # True
print(verify(["2*x + 3*y - 12", "5*x - 2*y - 4"], bad))    # False
```

Now the part that will actually surprise you. **You do not have to guess —
run it.** On this version of SymPy:

```python
good = {x: 36/19, y: 52/19}
print(repr(good[x]))                 # 1.894736842105263   <- a float
print(verify(["2*x + 3*y - 12", "5*x - 2*y - 4"], good))   # False
```

`False`. The solution is **correct** and `verify` rejects it, because in plain
Python `36/19` is float division and it evaluates to `1.894736842105263`, not
to the exact rational. SymPy then tries to prove that
`1.894736842105263` is *exactly* zero and cannot, so it says the equation is not
satisfied.

The fix is one character of discipline — make SymPy do the division, not Python:

```python
from sympy import Rational
good = {x: Rational(36, 19), y: Rational(52, 19)}
print(repr(good[x]))                 # 36/19
print(verify(["2*x + 3*y - 12", "5*x - 2*y - 4"], good))   # True
```

- ☐  What did you actually get for `36/19`, float or exact? ______
- ☐  If float: what is the general risk of a float where an exact rational was
     meant, in a program that checks passwords or verifies a signature? ______

**This is the single most important habit in the unit.** An approximate answer
silently fails an exactness check, and it will do so *sometimes* — which is
worse than always. `0.1 + 0.2 == 0.3` is `False` in Python. A checker built on
exact comparison rejects some right answers and no wrong ones until the day a
wrong answer happens to be exact. **Reach for `Rational(a, b)` or `sympify(a)/b`,
never for `a/b` on two literals, whenever the answer feeds a comparison.**

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. `symkit.py` and `test_symkit.py` pushed, with the three new system cases in
2. Your **Part 2 table**, filled in, with the two "how would a person miss
   this" cells written
3. Your **Part 1 audit** — prediction versus reality, unchanged from before you
   checked
4. A screenshot of the `False` above **and** the `True` after switching to
   `Rational`, plus one paragraph: why an approximate answer that fails a
   correctness check is more dangerous than one that fails loudly

**The graded part is the float/Rational analysis.** Everyone can call `solve`.
Knowing that `36/19` is not `36/19` until you say so is the actual content.

## 📋 PREVIEW OF MONDAY

**Next:** L05, Mon Jan 11 — modular arithmetic. `7 mod 5`, why `(-3) mod 5` is
not `-3` in Python, arithmetic in `Z_n`, and the one theorem — Fermat's little
theorem — that makes public-key ciphers possible. This is the day the algebra
finally does something you would use it for.

**Bring Monday:** laptop, `symkit.py`, and the Part 2 table above. You will need
the row about free symbols.

## 🇹🇼 TAIWAN CONTEXT

Watch one thing before Monday: SymPy printed `I` for the imaginary unit in the
L03 check — capital `i`, and Python's own `1j` is a different object. A letter
substitution cipher maps letters to numbers, and the moment a cipher has to
handle negatives or non-integers, the modular arithmetic from Monday stops being
a curiosity and starts being a requirement. That is why it is L05 and not L07.
