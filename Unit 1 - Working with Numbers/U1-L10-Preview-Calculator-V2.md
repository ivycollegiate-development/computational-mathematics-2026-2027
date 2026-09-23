# U1 L10 — Preview: Calculator v2 — Conversions and Guardrails

**LO:** preview the Calculator v2 lab (U1 L11) by planning, on paper, the conversions and input guardrails the calculator will enforce.

No electronics today — paper, notes, and your partner. Lab day (U1 L11) you
extend the calculator your team built in the two-day build (U1 L08) with
everything from this unit. Today you decide *what* it will do and *how* it
will refuse bad input, so lab day is pure building, no deciding.

## PART 1 — OPENING REVIEW: UNIT CONVERSIONS (U1 L09) (10 min)

Last class (U1 L09) you wrote unit-conversion functions. Reconstruct them from
memory before I show anything — in your notes:

- What is the shape of a conversion function? (`def` a name, take one number,
  `return` one number.)
- Write the formula for Celsius to Fahrenheit, and for Kelvin from Celsius.
- Why does `c_to_k(-300)` deserve to be questioned before the math runs?
  (Hold that thought — it becomes a guardrail in the lab (U1 L11).)

Compare with your partner. Fix each other's formulas before we go over them.

## PART 2 — WHAT THE CALCULATOR V2 LAB ASKS FOR (10 min)

The Calculator v2 milestone has three requirements. Copy this list into
your notes — it is the checklist you build against:

1. **Conversions in the menu:** `c_to_f`, `f_to_c`, `c_to_k`,
   `km_to_miles`, `miles_to_km`, `kg_to_lbs`, `lbs_to_kg` — each a real menu
   choice, each fed through `get_number()` so bad input asks again.
2. **Overflow guard:** reject any number over 10**15 with a clear message
   ("absurdly large — refusing to compute") and ask again.
3. **Kelvin floor:** if a conversion would produce a temperature below 0 K,
   explain that nothing can be colder than 0 K and refuse the calculation.

## PART 3 — PREDICT THE CODE (15 min, in pairs)

Before writing any of it on lab day, predict it today. In your notes:

1. Sketch (plain English or pseudocode) a function named `is_too_big(n)` that
   returns `True` when `n` is over the limit. Where in the program should it
   run — before the math, after the math, or in the menu?
2. Sketch the Kelvin floor check: what must be true about the *input*
   temperature for the output to stay at or above 0 K? (Careful — it is not
   the same bound for C→K as for F→K.)
3. One small checker function used everywhere, or `if` statements scattered
   through the menu? Defend your choice. (Hint from U1 L06: what happens to a
   scattered `if` when you add a seventh menu option?)

## PART 4 — PLAN FOR LAB DAY (15 min, in pairs)

Fill in the plan worksheet with your partner:

- **Split of work:** who writes the conversion wiring, who writes the
  guardrails? (You still each write your own code — the plan is shared.)
- **Order of operations:** what gets built first so the tests can run at every
  step? Write the order as 4–5 plain-English steps.
- **Guard assignment:** assign one person to try to *break* each guardrail on
  Lab day (type `10**16`, type `-400 C`, type a word). Name the breakers now.
- **One question you want answered before you build.** Ask it now — lab day is
  for building, not for re-reading the requirements.

## PART 5 — THE IMPOSSIBLE QUESTION (10 min)

Class discussion to close: *can a guardrail ever be complete?*

- Your overflow guard rejects numbers over 10**15. What number just under
  10**15 could still produce a quietly wrong answer?
- What does your calculator do with input you never thought to guard? Where
  does the line sit between "the program is safe" and "the program is less
  unsafe"?

Write one sentence in your notes that you would be willing to say out loud.
Several of you will be asked to read yours — and your answer feeds the lab's
pair code review (U1 L11 Part 3).

## TURN IN — WORKSHEET (collected at the end of class)

One completed plan worksheet (Parts 2–4), both names on it, handed in before
you leave.

Submit a photo of the worksheet to this assignment on Google Classroom by
11:59 PM tonight.
Keep your notes — The lab builds directly on this plan.

Next: U1-L11-Calculator-v2-Lab.md