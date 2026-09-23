# U1 L10 — Calculator v2 Preview Worksheet

Names: ___________________________  Date: Sep 25

Planning sheet for Monday's Calculator v2 lab. One sheet per pair. You still write your own code Monday — today you agree on the plan.

## 1: Thursday's conversions, from memory

Fill in each formula before checking with your partner.

Celsius to Fahrenheit: F = ______________________________

Fahrenheit to Celsius: C = ______________________________

Kelvin from Celsius: K = ______________________________

Why does c_to_k(-300) deserve to be questioned before the math runs?

_________________________________________________________________________

_________________________________________________________________________

## 2: Monday's checklist

Copy check — these are the three things Monday's build is graded on. Check each box as you and your partner read it:

☐  Conversions in the menu: c_to_f, f_to_c, c_to_k, km_to_miles, miles_to_km, kg_to_lbs, lbs_to_kg — each a real menu choice, each fed through get_number()

☐  Overflow guard: reject any number over 10^15 with a clear message and ask again

☐  Kelvin floor: if a conversion would produce a temperature below 0 K, explain why and refuse the calculation

## 3: Predict the code

Box A — sketch is_too_big(n) in plain English or pseudocode:

_________________________________________________________________________

_________________________________________________________________________

Where in the program should it run? Circle one:   before the math   /   after the math   /   in the menu

Box B — the Kelvin floor. What must be true about the INPUT temperature for the output to stay at or above 0 K? Careful: the bound is not the same for C to K as for F to K.

C to K input bound: ______________________________

F to K input bound: ______________________________

Box C — one small checker function used everywhere, or if statements scattered through the menu? Circle one and defend it in one line:

_________________________________________________________________________

_________________________________________________________________________

## 4: Plan for Monday

Split of work — who writes what Monday:

Conversion wiring: ___________________________  Guardrails: ___________________________

Order of operations — write 4-5 plain-English steps, in the order you will build them:

1. _______________________________________________________________________

2. _______________________________________________________________________

3. _______________________________________________________________________

4. _______________________________________________________________________

5. _______________________________________________________________________

Guard breakers — who tries to break each guardrail Monday (type 10^16, type -400 C, type a word):

Overflow guard: ___________________________  Kelvin floor: ___________________________  Word input: ___________________________

One question you want answered before you build:

_________________________________________________________________________

## 5: The impossible question

Your overflow guard rejects numbers over 10^15. What number just UNDER 10^15 could still produce a quietly wrong answer?

_________________________________________________________________________

Write one sentence you would be willing to say out loud about whether a guardrail can ever be complete:

_________________________________________________________________________

## Hand-in

☐  Both names on the sheet, all five parts filled in.

☐  Photo of this sheet submitted to the Classroom assignment by 11:59 PM tonight.

Keep your notes — Monday's lab builds directly on this plan.
