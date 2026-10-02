# U1 L17 — Reteach: Fixing What the Assessment Exposed (Oct 9, Fri — TECH DAY)

**LO:** turn yesterday's graded assessment into working code, so the gap you
were graded on stops being a gap.

Your Unit 1 assessment came back graded. Today is not a guilt session and it is
not new material — it is the **repair** session. You looked at the paper, you
found the two or three items that cost you, and today you make them work.

Bring your assessment and your calculator lab repo.

## PART 0 — NAME THE GAP (10 min)

Turn your assessment over. Find the items you got wrong or guessed. Do not
look at the total first — look at the *items*.

Write on paper, one line each:

1. The concept I lost points on: ______________________
2. The question I got right **by luck**: ______________________
3. The bug in my calculator that matches gap #1: ______________________

Most papers have one or two real gaps, not ten. You are about to fix one or
two. Finding them precisely is the whole job.

## PART 1 — REPRODUCE THE MISS (25 min)

A concept you missed on paper is a concept you cannot yet do on a keyboard.
Prove that, then fix it.

For your gap from Part 0, in this order:

1. **Write the smallest program that shows the mistake.** Run it.
2. **Say what you expected** and what actually happened. Write both down.
3. **Fix the real thing in your calculator**, not the snippet.

```bash
cd ~/compmath-lab
git pull
python3 test_calculator.py
```

## PART 2 — THE THREE THAT RECUR (25 min)

Whichever gap you have, these are the ones that cost the most points across
the class. Check your own code against each.

**Quietly wrong beats crashed.** A crash tells you something is broken. A
program that returns `0.0` when the user meant `0` tells you nothing, and that
answer can flow straight into a decision. Look for the quiet ones:

```python
# This does not crash. That is the problem.
def f_to_c(f):
    return f * 5 / 9 - 32      # wrong: conversion applied in the wrong order
```

The correct line converts the offset, not the result:

```python
def f_to_c(f):
    return (f - 32) * 5 / 9
```

**Boundaries are not edge cases to ignore.** −273.15 °C and `10**15` are the
two numbers this unit was about. Test them on purpose:

```python
def c_to_k(c):
    if c < -273.15:
        return "Below absolute zero — refusing."
    return c + 273.15
```

**Trust nothing the user types.** `input()` returns a string every single time.
The conversion goes *before* the arithmetic:

```python
while True:
    try:
        age = int(input("Age: "))
        if age <= 0:
            print("Age must be positive.")
            continue
        break
    except ValueError:
        print("That is not a number. Try again.")
```

## PART 3 — PROVE IT (10 min)

Push the fix. Then, in one sentence in your commit message, name the concept
you were missing on Wednesday and what you did about it.

That sentence is the deliverable. The code is the proof.

## TURN IN — PUSH (due 11:59 PM tonight)

One screenshot showing, in order:

1. Your terminal with `python3 test_calculator.py` passing.
2. The `git push` confirmation line with your commit message visible.

Submit the screenshot to this assignment on Google Classroom.

Keep the terminal open — spot-checks.

**Next Monday we start Unit 2** — visualizing data. The habits you just
repaired (validate input, guard the boundary, distrust a quiet answer) are the
same habits that make a chart honest.
