# U1 L14 — Unit 1 Review & Catch-Up — Worksheet

Names: ___________________________  Date: ____

Not a cram session — a **gap-finding** one. Bring your lab repo.

## Part 0 — DIAGNOSE

```
cd ~/compmath-lab
git pull
python3 test_calculator.py
```

Last two lines the test printed:

   _________________________________________________________________________

   _________________________________________________________________________

Mark honestly — an honest Red beats a generous Green. This list is for you, not me.

| Topic | Green | Yellow | Red |
|---|---|---|---|
| int vs float, // vs /, %, exponent |  |  |  |
| input() + int() / float() conversion |  |  |  |
| try/except ValueError |  |  |  |
| Division by zero — why it crashes |  |  |  |
| Boundary tests: 10**15 and the Kelvin floor |  |  |  |
| Unit conversions (temp, distance, weight) |  |  |  |
| Finding factors and multiples |  |  |  |
| Writing your own tests |  |  |  |

My top two Reds:

1. ____________________________________________________________________

2. ____________________________________________________________________

## Part 1 — RED-TOPIC CLINIC

1. Reproduce the failure first. Don't guess at the fix.
2. Read the error. ZeroDivisionError names the problem; most beginners skip it and start editing at random.

Topic I worked, what the terminal printed, and the actual cause (not "I fixed the bug"):

   _________________________________________________________________________

   _________________________________________________________________________

The fix I made:

   _________________________________________________________________________

Does your try/except wrap **each input** (asks again) or the whole program?

   _________________________________________________________________________

## Part 2 — THE TRAPS

| Trap I have actually hit | Hit? |
|---|---|
| 7 / 2 is 3.5, 7 // 2 is 3, 7 % 2 is 1 | ☐ |
| input() returns a string — input() + 1 is a TypeError | ☐ |
| try/except around the whole program hides the error | ☐ |
| 10**15 and -273.15 Celsius are boundary tests | ☐ |

## Part 3 — PRACTICE THE FORMATS

No computer. Notes only.

**1.** The type() of each expression.

| Expression | Value | type() |
|---|---|---|
| 7 / 2 |  |  |
| 7 // 2 |  |  |
| 7 % 2 |  |  |
| int("42") |  |  |
| "42" + "0" |  |  |

**2.** A try/except that catches bad input and asks again.

   _________________________________________________________________________

   _________________________________________________________________________

**3.** A guardrail rejecting input over 10**15. Finish this — the second half is the point:

   It should not just raise. It should _____________________________________

   _________________________________________________________________________

**4.** −40 °C to Kelvin and back. Round-trip?

   Celsius to Kelvin: ____________     Kelvin back to Celsius: ____________

   ☐ Yes  ☐ No

**5.** In one sentence: why does a silently wrong answer matter more than a crash?

   _________________________________________________________________________

## DEBRIEF

Use this before you leave. An honest sheet tells you what to review; a generous
one tells you nothing.

**The one I got wrong** — and the *actual* reason. "Forgot the `except`" is a
real reason. "Misread it" is not a diagnosis.

   _________________________________________________________________________

**The one I got right by luck.** Guessing a type you half-remember is luck.
Mark it — it might not land next time.

   _________________________________________________________________________

## TURN IN — PUSH

☐  I pushed what I fixed in Part 1.

☐  It names the two topics I worked on.

☐  It says what was **actually wrong**, not just what I changed.

☐  If everything was green, my PR says so — a real answer, not a cop-out.

## JOURNAL

One thing you now understand about your calculator that you didn't in Week 1:

   _________________________________________________________________________

   _________________________________________________________________________
