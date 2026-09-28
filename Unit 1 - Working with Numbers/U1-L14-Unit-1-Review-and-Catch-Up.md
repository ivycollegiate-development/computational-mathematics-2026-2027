# U1 L14 — Unit 1 Review & Catch-Up (Oct 5, Mon — TECH DAY)

**LO:** close the gaps in Unit 1 before the U1 L16 assessment, and rehearse the problem types it will ask.

Thursday is the Unit 1 assessment. Today is the working session that decides
how ready you are for it — not a cram session, but a **gap-finding** one. Bring
your calculator lab repo open.

## PART 0 — DIAGNOSE (10 min)

Before fixing anything, find out what is actually broken. Run:

```bash
cd ~/compmath-lab
git pull
python3 test_calculator.py
```

Then, on paper, list every topic from Unit 1 and mark yourself honestly:

| Topic | Green | Yellow | Red |
|---|---|---|---|
| `int` vs `float`, `//` vs `/`, `%`, `**` | | | |
| `input()` + `int()`/`float()` conversion | | | |
| `try/except ValueError` | | | |
| Division by zero — why it crashes | | | |
| `10**15` bound | | | |
| Kelvin floor (below 0 K) | | | |
| Unit conversions (temp, distance, weight) | | | |
| Finding factors and multiples | | | |
| Writing your own tests | | | |

**Everything Red is your study list for Wednesday.** Green means move on. Be
honest — this list is for you, not for me.

## PART 1 — RED-TOPIC CLINIC (25 min)

Pick your top two Reds and work them with the group around you. Two rules:

1. **Reproduce the failure first.** Do not guess at the fix. Make the wrong
   thing happen, look at the actual output, and read the error message.
2. **Read the error.** `ZeroDivisionError: division by zero` names the problem.
   Most Python beginners scroll past it and start editing code at random. The
   error message is the most informative thing on your screen.

Common Unit 1 traps worth checking against your own code:

- `7 / 2` is `3.5` but `7 // 2` is `3` — and `7 % 2` is `1`. If you got these
  backwards, every conversion you built is subtly wrong.
- `input()` **always** returns a string. `input() + 1` is a `TypeError`; it
  never silently works.
- A `try/except` that wraps the whole program hides the error. Wrapping each
  input lets you ask again.
- `10**15` overflow and `-273.15` Celsius are both boundary tests, not edge
  cases to ignore.

## PART 2 — PRACTICE THE FORMATS (20 min)

The assessment is paper. In your notes, do these without a computer:

1. `type()` of: `7 / 2`, `7 // 2`, `7 % 2`, `2 ** 10`, `int("42")`, `"42" + "0"`.
2. Write the `try/except` block that catches bad input and asks again.
3. Write a guardrail that rejects input over `10**15`, and say what it should
   *do* rather than just `raise`.
4. Convert −40 °C to Kelvin, then back. Does it round-trip?
5. In one sentence: why does a silently wrong answer matter more than a crash?

## TURN IN — PUSH (due 11:59 PM tonight)

Push whatever you fixed in Part 1. Write in your PR description: which two
topics you worked on, what was actually wrong, and what fixed it. If you
worked on nothing because everything is green, say that — that is a real
answer, not a cop-out.
