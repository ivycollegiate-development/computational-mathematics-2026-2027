# U4 L01 — Unit 4 Launch: Number Answers vs. Symbol Answers

**Date:** Jan 5 (Tue)
**LO:** understand what a computer gains from keeping a variable symbolic, and preview the four things SymPy will do for you.

Unit 4 is **Algebra and SymPy**. Everything in it is math you already know. The
only new thing is *who does the bookkeeping*.

For sixteen weeks you have been writing code where the answer came out as a
number: a mean, a count, a pixel. Today we hand the same mathematics to a
library that refuses to collapse `2x + 3` into a single value, because it does
not know `x` yet. You keep `x` alive. You can inspect it, factor it, substitute
it, and solve it — and *then*, if you want, collapse it to a number.

This is a **paper day.** Pencil, no laptop. It is a reflection and a preview, and
it is how Unit 4 opens: not with a new tool on a cold screen, but with the idea
the tool exists to serve.

## PART 1 — WHAT "SYMBOLIC" ACTUALLY MEANS (12 min)

Here are four lines. They are the same arithmetic, and they are not the same
kind of answer.

```
2 * 3 + 1                 ->  7            (numeric: a value, right now)
2 * x + 1                 ->  ???          (symbolic: no value, x is unknown)
2 * x + 1  with x = 3     ->  7            (substituted: a value, again)
2 * x + 1  for which x    ->  x = 3        (solved: a value AND the input)
```

The third line — substitute a number you already know — is the whole reason
symbolic math exists. A spreadsheet does line 4 for you constantly. A cipher
does line 3 over a letter instead of a number.

- ☐  In your own words: what is the difference between the second line and the
     fourth line? One or two sentences. ______
- ☐  Name one thing you have already done in this course that is really line 3
     in disguise. ______

## PART 2 — FOUR THINGS SYMPY WILL DO (15 min, discussion + notes)

SymPy is a Python library for symbolic mathematics. Four verbs, and you will use
all four for the rest of the unit.

| verb | what it does | by-hand example |
|---|---|---|
| **expand** | multiplies a product out | `(x + 2)(x + 3)` → `x² + 5x + 6` |
| **factor** | reverses that | `x² + 5x + 6` → `(x + 2)(x + 3)` |
| **simplify** | rewrites without changing the value | `2x/2` → `x`, `x + x` → `2x` |
| **solve** | returns the inputs that make an equation true | `2x + 1 = 7` → `x = 3` |

Two properties of that table matter more than the table itself.

**1. Round-tripping is a check.** `factor(expand(f))` should give you back `f`
almost every time. When it does not, you have found either a genuine identity or
your own typo. This is the cheapest self-check available in mathematics, and you
will use it as a habit for the rest of the week.

- ☐  By hand: expand `(x + 2)(x + 5)`, then factor the result back. Write both. ______
- ☐  `(x + 2)(x + 5)` and `(x + 5)(x + 2)` are the same expression. Which piece
     of Python's bookkeeping makes that true without you thinking about it? ______

**2. Solve returns *every* solution, not one.** This is the thought I asked you
to bring today. A CAS — a computer algebra system — does not sample. If an
equation has four solutions, it gives you four. If it has infinitely many, it
tells you that, which is a different kind of answer from `x = 3`.

- ☐  Write down one equation you can think of that has **no** solution. ______
- ☐  Write down one that has **infinitely many**. ______
- ☐  Which of those two is harder to represent in ordinary code, and why? ______

That last blank is the honest one. "No solution" and "infinitely many" are
conditions on a *set*, and ordinary code returns one value at a time. You will
see how SymPy names them in L02.

## PART 3 — THE FOUR-UNIT SPINE (12 min, fill this in, keep it)

Unit 4 has a shape. Fill this table in now, in pencil, and correct it whenever
the week tells you to.

| day | date | what you can do after it | paper or machine |
|---|---|---|---|
| L01 | Jan 5 (Tue) | name what symbolic means | paper |
| L02 | Jan 6 (Wed) | use `Symbol`, `expand`, `factor`, `simplify` on paper *and* in code | machine |
| L03 | Jan 7 (Thu) | hand-solve, then predict what the machine will say | paper |
| L04 | Jan 8 (Fri) | solve systems and read a full symbolic solution | machine |
| L05 | Jan 11 (Mon) | do arithmetic in `Z_n` and explain why ciphers need it | machine |
| L06 | Jan 12 (Tue) | midterm consolidation: Units 1–4 on paper, cold | paper |
| L07 | Jan 13 (Wed) | use a hash to detect that data changed | machine |
| L08 | Jan 14 (Thu) | find and fix your own algebra errors from an error log | paper |
| L09 | Jan 15 (Fri) | full paper check under exam conditions | paper |

- ☐  Which of these nine is the one you are most worried about? ______
- ☐  Which do you expect to be easiest? ______

Be specific. "Systems" is a useful answer. "Everything" is not.

## PART 4 — HOW TO USE THE LIBRARY WITHOUT A HEADACHE (10 min)

Two rules, and they save an enormous amount of time all week.

**Rule 1 — the library is a guest, not a resident.** If the server you are on
does not have SymPy, nothing in this unit runs. So *every* script you write in
this unit starts with this guard, before anything else:

```python
try:
    from sympy import Symbol, expand, factor, simplify
    HAVE_SYMPY = True
except ImportError:
    HAVE_SYMPY = False

if not HAVE_SYMPY:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")
```

Read what that guard does: it fails **loudly and early** with a sentence a human
can act on, instead of dying later with a `NameError` on line 30 and no clue
which import broke. You get a useful error or a clear one, never a mystery.

**Rule 2 — make the symbol before you use it.** SymPy will not guess.

```python
from sympy import Symbol, expand, factor, simplify

x = Symbol('x')          # you must declare this yourself
print(expand((x + 2) * (x + 5)))   # x**2 + 7*x + 10
print(factor(x**2 + 7*x + 10))      # (x + 5)*(x + 2)
print(simplify(2 * x / 2))          # x
```

- ☐  Why do you think `x = Symbol('x')` is not allowed to happen automatically
     the way `x = 5` just works? One sentence. ______

That is not a mystery either. It comes back in L02, and it is worth being able
to answer now.

## PART 5 — CLOSING REFLECTION (10 min, yours alone)

In your notebook, one paragraph, no partner, no group chat. A negotiated answer
is not an answer.

- What is one piece of algebra you have *done* in this course that you now
  realise was the machine's version of a symbolic step? ______
- Is there any algebra you have done that you think a computer does *better*
  than a person? Say which, and why. ______
- Is there any algebra you think a person does *better* than a computer? Say
  which, and why. ______

The third question is not a trick. There is a real answer, and finding it is
worth more than anything on the midterm.

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. Your **Part 3 spine table**, filled in, with the two named days from the
   bottom of Part 3
2. Your **Part 2 three blanks** — the no-solution equation, the infinitely-many
   equation, and which is harder to code
3. Your **Part 5 paragraph**, in your own words

**Part 5 is graded for honesty, not for being right.** "I cannot tell whether a
computer or a person is better at picking a factoring strategy, but I know the
computer is better at expanding and I am better at spotting which factor to try"
is a better answer than anything I could write. "Computers are good at math" is
not.

## 📋 TOMORROW

Bring: pencil, notebook, a laptop, and the `PART 1` guard code from today typed
into a file called `sympy_check.py`. We will run it first thing and find out
whether the server has the library — before anything depends on it.

**Next:** L02, Wed Jan 6 — first contact with the machine. `Symbol`, `expand`,
`factor`, `simplify`, and the round-trip check from Part 1 written as code.

## 🇹🇼 TAIWAN CONTEXT

Unit 4 is a **TTh-heavy** unit in terms of the paper/machine split — three of
the nine days are paper consolidation before midterms. If you want an early edge:
Mersenne primes and Fermat's little theorem are worth ten minutes of reading
before Monday, because L05 assumes you have seen `a^p ≡ a (mod p)` at least
once. `2^p - 1` being prime for prime `p` is the idea behind a whole family of
public-key ciphers. You do not need to know that today.
