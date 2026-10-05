# Unit 1 Assessment — Computational Mathematics

**Schedule:** Unit 1 Assessment
**Time:** 35 minutes
**Conditions:** Closed computer. Pen and paper only. No notes, no phone, no neighbors.

Print double-sided. Do not write your name inside the body — write it on the
coversheet only.

Total: 50 points.

---

## COVERSHEET

Before you start, on the cover of your paper write:

- Your name
- One thing from Unit 1 you feel confident about
- One thing you hope is **NOT** on this test

The coversheet is not graded. The third answer is the useful one — it tells me
where to spend review time in Unit 2.

---

## RULES

- Answer in complete sentences where the question asks *why*.
- A value or a word is fine where the question asks *what*.
- **Answer the verb.** "What happens when…" wants the actual error, not the fix.
  "Why" wants a sentence, not a value. Most lost points on this test come from
  answering a different question than the one asked.
- Show your work on every code question. Partial credit is real.
- If you finish early, review. There is no extra credit for finishing fast.

---

## SECTION A — SHORT RESPONSE (10 questions, 2 points each = 20 points)

**1.** What type does Python give you for `7 / 2`? What type for `7 // 2`?
Give both values and both types.

**2.** What type does `input()` always return? Why does it need a wrapper like
`int()` or `float()` around it before we can do arithmetic with it?

**3.** A user types `banana` into `age = int(input("Age: "))`. Name the exact
exception Python raises, then write the one line of `try/except` that catches
it.

```python
try:
    age = int(input("Age: "))
except ________:
    print("That is not a number. Try again.")
```

**4.** A program returns `0.0` when the user meant `0`. Is that a **crash** or a
**quietly wrong answer**? Which is more dangerous, and why?

**5.** Assuming `x = 0`, write True or False for each:

- `x == 0`
- `x >= 0`
- `x > 0 or x < 0`

**6.** `Fraction(1, 3)` is exact. `1 / 3` is not. Why? Name the type `/`
produces.

**7.** `17 % 5` — what does it return? Name one real use for modulo from class.

**8.** Order these from smallest step size to largest (least precise to most
precise): `int`, `float`, `Fraction`. One sentence on why that order.

**9.** In your calculator lab, what did `get_number()` protect against, and
what did it do when validation failed?

**10.** The security lens: give one example from Unit 1 of "trusting the user"
going wrong, and state the one rule you now apply to every input.

---

## SECTION B — CODE READING (2 problems, 5 points each = 10 points)

*You do not run this code. You read it the way a debugger would.*

### Problem 11

```python
total = 0
for price in ["3.50", "4", "1.25", "oops"]:
    total = total + float(price)
print("Total:", total)
```

**a.** What happens on the **third** loop iteration? Be precise about which
value is being converted.

**b.** What happens on the **fourth** iteration? Name the exception.

**c.** Rewrite **only the loop body** so a bad price prints a warning and the
program keeps going instead of crashing. Two or three lines is enough.

### Problem 12

```python
def f_to_c(f):
    return f * 5 / 9 - 32

temp = input("Enter °F: ")
print(f_to_c(float(temp)))
```

**a.** There is one bug that makes this *quietly wrong*. Find it and write the
correct line. (Hint: test it mentally with 212 °F.)

**b.** The program still crashes on `banana`. Rewrite the last two lines with a
full `try/except`.

**c.** One sentence: why is bug (a) worse than bug (b)?

---

## SECTION C — BOUNDARIES (1 problem, 10 points)

Your unit had exactly two boundary numbers. Use them.

**13.** Absolute zero is −273.15 °C, and 0 K is −273.15 °C.

```python
def c_to_k(c):
    return c + 273.15
```

**a.** Write the complete, correct version of `c_to_k`. It must refuse a
temperature below absolute zero and return the string `"Below absolute zero —
refusing."` in that case. Include the guard and the normal return. (3 points)

**b.** What is `c_to_k(-273.15)`? Give the exact value and its type. (2 points)

**c.** We also needed an explicit `10 ** 15` ceiling in the calculator, even
though Python integers are unlimited. In one sentence: why is unlimited integer
precision actually a problem for this class of work? (3 points)

**d.** Your calculator must reject values at or above `10 ** 15`. Write the
single `if` line you would put at the top of `get_number()`. (2 points)

---

## SECTION D — WRITE CODE (1 problem, 10 points)

**14.** Write a function called `get_int(prompt)` that:

- asks the user for a number using the given prompt
- keeps asking if the input is not a valid integer (do not crash, do not exit)
- refuses a value at or above `10 ** 15`
- returns the valid integer once you have one

Write the whole function. You may not use `eval()`. Do not add features that
were not asked for.

---

## FINISHING

Turn your paper face down and wait quietly.
