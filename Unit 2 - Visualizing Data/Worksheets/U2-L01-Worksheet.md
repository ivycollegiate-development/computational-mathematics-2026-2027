# U2 L01 — Unit 1 Assessment (Paper Day)

Names: ___________________________  Date: ____

**Paper assessment. No computers, no notes, no neighbors.** Everything below is something we built or debugged together in Unit 1. 35 minutes, in silence.

## Part 1 — Before you start (5 min)

Put everything away except a pen. On the cover of your paper write:

- your name
- one thing from Unit 1 you feel confident about: ______________________________________
- one thing you hope is NOT on the test: __________________________________________

Be honest. It will not change the test — it tells me where to spend review time next unit.

## Part 2 — Written assessment (35 min)

### Section A — Short response (10 questions, 2 points each)

Complete sentences where it asks *why*. A word or value is fine where it asks *what*.

**1.** What type does Python give you for `7 / 2`, and what type for `7 // 2`? Give both values and both types.

   _________________________________________________________________________

**2.** Why does `input()` need a wrapper like `int()` or `float()` when we want a number? What type does `input()` always return?

   _________________________________________________________________________

**3.** A user types `banana` into `age = int(input("Age: "))`. Name the exact exception Python raises, and write the one line that would catch it.

   _________________________________________________________________________

**4.** What is the difference between a program that **crashes** and one that is **quietly wrong**? Which is more dangerous, and why?

   _________________________________________________________________________

   _________________________________________________________________________

**5.** Write the value (just True/False) for each of these, assuming `x = 0`:


| Code | What Python does |
|------------|------------------|
| `x == 0`                |               |
| `x >= 0`                |               |
| `x > 0 or x < 0`        |               |

**6.** Why is `Fraction(1, 3)` exact but `1 / 3` is not? What kind of number does Python use for `/`?

   _________________________________________________________________________

**7.** In your calculator lab, what did `get_number()` protect against, and what did it do when validation failed?

   _________________________________________________________________________

**8.** Order these from smallest to largest step size (precision): `int`, `float`, `Fraction`. One sentence on why.

   _________________________________________________________________________

**9.** What does `%` return for `17 % 5`, and name one real use for modulo we discussed.

   _________________________________________________________________________

**10.** The security lens: give one example from Unit 1 of "trusting the user" going wrong, and the one rule you now apply to every input.

   _________________________________________________________________________

   _________________________________________________________________________

### Section B — Code reading (2 problems, 5 points each)

*You do not run this code. You read it like a debugger would.*

**Problem 11.** Read this program:

```python
total = 0
for price in ["3.50", "4", "1.25", "oops"]:
    total = total + float(price)
print("Total:", total)
```

a) What happens on the third loop iteration? Be precise about which value is being converted.

   _________________________________________________________________________

b) What happens on the fourth iteration? Name the exception.

   _________________________________________________________________________

c) Rewrite ONLY the loop body so a bad price prints a warning and the program keeps going instead of crashing.

   _________________________________________________________________________

   _________________________________________________________________________

**Problem 12.** Read this converter:

```python
def f_to_c(f):
    return f * 5 / 9 - 32

temp = input("Enter °F: ")
print(f_to_c(float(temp)))
```

a) There is one bug that makes this *quietly wrong* — find it and state the correct line.

   _________________________________________________________________________

b) The program still crashes on `banana`. Write the full `try/except` version of the last two lines.

   _________________________________________________________________________

c) One sentence: why is bug (a) worse than bug (b)?

   _________________________________________________________________________

## Part 3 — Hand back the computers

Not yet — turn your paper face down and wait quietly. If you finish early, review your answers. There is no extra credit for finishing fast.

## Part 4 — Journal (last 10 min)

1. Which assessment problem was hardest, and what does that tell you about what to review before the next unit builds on it?

   _________________________________________________________________________

2. Unit 2 is about **visualizing data**. Where in Unit 1 did we already touch data, even a little?

   _________________________________________________________________________

3. One prediction: what could go *visually* wrong with data that goes wrong numerically?

   _________________________________________________________________________

## Part 5 — Push

- ☐  `journal-u2l01.md` created in `~/compmath-lab`, Part 4 answered, `git push` confirmed.

## TURN IN

- ☐  Photo of your paper assessment — all sections, legible, right side up.
- ☐  Screenshot to the Classroom assignment by 11:59 PM tonight showing: your journal file with the Part 4 answers, and the successful `git push`.

Keep the journal — Unit 2 builds directly on what you found in the gaps.
