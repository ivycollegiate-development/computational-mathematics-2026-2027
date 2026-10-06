# U4 L03 — Paper Check: Solve It, Then Predict (No Laptop)

**LO:** hand-solve linear and quadratic equations, and predict the machine's answer before checking it.

**No laptop today.** Pencil, notebook, and the `symkit.py` you built yesterday
still on your screen at home — you will want it tonight, not today.

The reason for this day is narrow and worth stating: you have now run the four
algebraic verbs in code, and you may have quietly started believing the library
instead of the mathematics. Today we find out which of the two is actually
carrying you.

So: solve everything by hand, and for each one **also write what you predict
SymPy will return**, including its *form* — not just the value, but whether it
comes back as a list, a set, a dict, or a bare expression. Forms are how you get
tricked on a midterm.

## PART 1 — LINEAR, BY HAND (15 min)

For each: solve it, then predict the exact shape of the output.

1. `3x + 7 = 22`

   x = ______  predicted SymPy returns: ______

2. `5x - 2 = 3x + 10`

   x = ______  predicted SymPy returns: ______

3. `2(x - 3) = 4x`

   x = ______  predicted SymPy returns: ______

4. `(x + 1)/3 = 4`

   x = ______  predicted SymPy returns: ______

5. `7 = 7x + 2`

   x = ______  predicted SymPy returns: ______

- ☐  Number 2 is the one people get wrong. What is the trap in it? ______
- ☐  How many steps did each take? Record the count: ______
- ☐  Did you get the same x by two different routes on any of them? Which, and
     how? ______

## PART 2 — QUADRATICS, BY HAND (20 min)

The quadratic formula. Show all five steps for the first two — the work is the
graded part, the answer is nearly free once the work is there.

6. `x² - 5x + 6 = 0`

   discriminant = ______  roots = ______  predicted SymPy returns: ______

7. `2x² + 7x + 3 = 0`

   discriminant = ______  roots = ______  predicted SymPy returns: ______

8. `x² - 4x + 4 = 0`

   discriminant = ______  roots = ______  predicted SymPy returns: ______

9. `x² + 2x + 5 = 0`

   discriminant = ______  roots = ______  predicted SymPy returns: ______

Number 8 is a perfect square — note whether you get one root or two.
Number 9 has a negative discriminant — **write what you expect SymPy to
return for a real-only search versus an unrestricted one.** ______

Then the factoring route, for the same four:

| # | can it be factored over the integers? | if yes, factor it | if no, say why not |
|---|---|---|---|
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |

- ☐  For which numbers does `factor` on the *left-hand side minus the
     right-hand side* recover your roots, without the quadratic formula
     anywhere? ______
- ☐  For which does it not, and what does SymPy hand back instead? ______

## PART 3 — TWO-SYMBOL EQUATIONS (15 min)

10. Solve for `x`: `2x + 3y = 12`

    x = ______  (in terms of y)

11. Solve for `y`: `5x - 2y = 4`

    y = ______  (in terms of x)

12. `2x + 3y = 12` and `5x - 2y = 4` together. Solve for the point.

    (x, y) = ______  predicted SymPy returns: ______

- ☐  Number 12 is the same pair of equations as 10 and 11. What did combining
     them actually buy you? One sentence. ______
- ☐  Write an equation that pairs with `2x + 3y = 12` to have **no** solution.
     ______
- ☐  Write an equation that pairs with it to have **infinitely many** solutions.
     ______

Those last two are the Part 2 of L01 coming back, and on the midterm they are
worth marks because most people cannot produce them.

## PART 4 — PREDICTION AUDIT (10 min)

Count your predictions across Parts 1–3.

| section | predictions made | predicted value right | predicted *form* right | both wrong |
|---|---|---|---|---|
| linear (1–5) | | | | |
| quadratic (6–9) | | | | |
| two-symbol (10–12) | | | | |

Now answer, in writing:

- ☐  The single prediction I got most wrong was number ______ because ______
- ☐  Were your **values** better or your **forms**? Evidence: ______
- ☐  Is there a pattern to which forms you mispredicted? ______

That last question matters more than it looks. If you keep predicting a bare
expression where SymPy returns a list of solutions, you now know that, and you
will not lose the point again.

## PART 5 — START THE ERROR LOG (5 min)

Open the page you started in L02 — **Algebra Error Log**, two columns: *what I
wrote* and *what it should have been*.

- ☐  Every error from today goes in, including the ones you caught.
- ☐  Tag each with a cause: **sign**, **distribution**, **formula**, **careless**.
- ☐  Most common cause today: ______

The U4 L07 error log is the raw material for U4 L08. A log with six entries beats
an empty one with six good intentions.

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. One photo of **Parts 1–3**, all work shown
2. One photo of the **Part 4 prediction audit** table
3. Your **error log** page, however many entries it has

**Grade this on prediction honesty.** If you wrote a prediction, got it wrong,
and can say *why* you expected the wrong thing, that is a full-credit answer. If
every prediction is miraculously right, I will assume you filled the table in
afterwards, and that is a zero on Part 4.

## 📋 TONIGHT, OPTIONAL, 15 MINUTES

Now that you have guessed, check. Open `sympy_check.py`'s neighbours and run
this — it is short enough to type from memory:

```python
from sympy import Symbol, solve, factor, sympify
x, y = Symbol('x'), Symbol('y')

print(solve(sympify('3*x + 7') - 22, x))
print(solve(x**2 - 5*x + 6, x))
print(solve(x**2 + 2*x + 5, x))
print(solve([2*x + 3*y - 12, 5*x - 2*y - 4], [x, y]))
print(factor(x**2 - 4*x + 4))
```

Compare to your predictions. **Do not change your paper.** The paper is the
record of what you believed before you knew, and that is the only honest
version of the exercise.

## 📋 PREVIEW OF TOMORROW

**Next:** L04 — back to the machine, and now `solve` gets serious:
systems with two unknowns, the `dict` form for multiple symbols, the conditions
under which `solve` returns an empty list, and turning that into a function you
can call with anything.

**Bring tomorrow:** laptop, and your paper from today.

## 🇹🇼 TAIWAN CONTEXT

If you want fifteen minutes tonight after the check: read about **modular
arithmetic** — just `7 mod 5` and `(-3) mod 5` and why Python's answer to the
second one is not negative. The U4 L04 lesson is built on that, and having already
thought about it is worth a full question.
