# Unit 1: Working with Numbers — Worksheet 2

**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part A: Input Validation

For each scenario, write what the program would do (crash? wrong answer?) and how to fix it:

| Scenario | What happens? | Fix |
|----------|--------------|-----|
| `age = int(input("Age: "))` — user types `"ten"` | | |
| `price = float(input("Price: "))` — user types `""` (empty) | | |
| `x = int(input("X: "))` — user types `"3.7"` | | |
| `y = int("1,000")` | | |

## Part B: try/except Practice

**5.** Write a program that asks for two numbers and divides them. Use `try/except` to handle:
- Invalid input (not a number)
- Division by zero

```
# Your code here:

```

**6.** Write a "safe input" function that keeps asking until the user enters a valid integer:

```python
def get_int(prompt):
    # Your code here — keep asking until valid

# Test it:
age = get_int("Enter your age: ")
print(f"You are {age} years old.")
```

## Part C: Fraction Basics

**7.** Use Python's `Fraction` module to solve these. Write the result:

```python
from fractions import Fraction

a = Fraction(1, 3)
b = Fraction(1, 6)
```

a) `a + b` = \_\_\_\_\_\_\_\_\_\_
b) `a * 3` = \_\_\_\_\_\_\_\_\_\_
c) `a - b` = \_\_\_\_\_\_\_\_\_\_
d) `Fraction(4, 8)` simplified = \_\_\_\_\_\_\_\_\_\_

**8.** Why does `Fraction("1/3") * 3` give you exactly `1`, but `float` arithmetic gives `0.999...`? Explain:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part D: Security Case Study — The Patriot Missile Problem

**Context:** During the Gulf War (1991), a Patriot missile battery failed to intercept an incoming Scud missile. The error: a floating-point imprecision of **0.000000095 seconds** per tick. Over 100 hours of operation, the timing drift grew to **0.34 seconds** — enough for the radar to look in the wrong place.

**9.** If the Patriot ran for just 10 hours (36,000 ticks per hour), how much total drift would accumulate?

```
Show your work:

```

**10.** How could a programmer protect against this kind of timing drift? (What Python tools have you learned that might help?)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part E: Calculator Design Brief

**11.** You're building a calculator that handles +, -, *, and /. Write pseudocode for the input validation step. What specific checks should your program make before doing any math?

```
PSEUDOCODE:

```

**12.** List at least 4 test cases you would try to break your calculator:

| Test Case | Expected Behavior |
|-----------|------------------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

## Checkout (before you leave)

Answer these to earn your exit check. **No notes — from memory.**

1. Write one line that turns a user's `str` into an `int` *safely* (won't crash on bad input).
2. What happens if you try `int("3.7")`? What does it tell you about strings vs floats?
3. True/False: a `try/except` block lets a program keep running after an error instead of crashing.
4. Give one real example where error-prone user input caused a serious problem.

---
**Teacher note:** Checkout is graded pass/fail (2 of 4 correct = pass). Record in the class tracker.
*Keep this for the Calculator project reference.*