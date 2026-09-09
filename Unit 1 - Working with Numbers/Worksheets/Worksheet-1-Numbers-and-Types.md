# Unit 1: Working with Numbers — Worksheet 1

**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part A: Type Detectives

For each value below, write what type Python would assign it (`int`, `float`, `str`, or `complex`):

| Value | Type | Value | Type |
|-------|------|-------|------|
| `42` | | `"42"` | |
| `3.14` | | `"3.14"` | |
| `7 + 2j` | | `True` | |
| `1_000_000` | | `float("3.14")` | |
| `int("100")` | | `str(99)` | |
| `10 / 3` | | `10 // 3` | |
| `10 % 3` | | `10 ** 3` | |

## Part B: Order of Operations

Evaluate these expressions as Python would:

1. `5 + 3 * 2` → \_\_\_\_\_\_
2. `(5 + 3) * 2` → \_\_\_\_\_\_
3. `10 - 4 / 2` → \_\_\_\_\_\_
4. `2 ** 3 + 1` → \_\_\_\_\_\_
5. `9 % 4 * 2` → \_\_\_\_\_\_
6. `3 * 2 ** 2 + 1` → \_\_\_\_\_\_

## Part C: Write the Code

Write Python code for each task:

**7. Temperature converter:** Ask the user for a temperature in Celsius, convert to Fahrenheit, and print the result. Formula: `F = C * 9/5 + 32`

```
# Your code here:

```

**8. Even or Odd:** Ask the user for a number. Print whether it's even or odd. *(Hint: use `%`)*

```
# Your code here:

```

**9. Age in seconds:** Ask for the user's age in years. Calculate and print how many seconds old they are (ignore leap years).

```
# Your code here:

```

## Part D: Find the Bug

Each snippet has a bug. Circle the problem and write the fix:

**10.** 
```python
age = input("How old are you? ")
next_year = age + 1
print("Next year you'll be", next_year)
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**11.**
```python
result = 10 / 0
print("The result is", result)
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**12.**
```python
price = 19.99
tax = price * 0.05
total = price + tax
print("Total: $" + total)
```
Bug: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Fix: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Part E: Security Reflection

**13.** Imagine you're building a payment calculator for a website. A user enters `"free"` into the "amount" field. What happens if your code doesn't validate? Why is this a problem?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**14.** What does "never trust user input" mean to you? Give one example of how you'd protect your own program against bad input.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Checkout (before you leave)

Answer these to earn your exit check. **No notes — from memory.**

1. What type is `int("100")`? What type is `int(100.5)`?
2. What does `10 // 3` give you? Why is it different from `10 / 3`?
3. What happens if you run `age = input("Age: ")` then `age + 1`? Why?
4. In one sentence: why do you have to protect against bad user input?

---
**Teacher note:** Checkout is graded pass/fail (2 of 4 correct = pass). Record in the class tracker.
*Save this! We'll refer back for the Calculator project.*