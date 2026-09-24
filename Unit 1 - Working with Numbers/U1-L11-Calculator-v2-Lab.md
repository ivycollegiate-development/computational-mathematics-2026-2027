# U1 L11 — LAB: Calculator v2 — Unit Conversions + Guardrails

**LO:** add unit conversion features and input guardrails to the calculator project, and review a partner's guardrail.

Today you extend the calculator your team built in the two-day build (U1 L08)
with everything from this unit: your conversions (U1 L09) and your plan (U1 L10). You work in
**your own calculator lab repo** — no new invitations today.

## PART 0 — OPEN YOUR CALCULATOR REPO (first 10 minutes)

In your VS Code workspace terminal — start with `pwd`:

```bash
pwd
cd ~/compmath-lab
git pull
python3 test_calculator.py
```

- If your clone lives somewhere else, `cd ~` first and check with `ls` — the
  repo is `compmath-lab` inside `~`.
- `git pull` first, always — grab anything you pushed from another machine.
- Confirm your **4/4 tests still pass** before you touch anything. If they do
  not, fix that first — today's work builds on it.

## PART 1 — ADD THE CONVERSIONS (~30 min)

Bring your converter functions (U1 L09) into `calculator.py`:

- `c_to_f`, `f_to_c`, `c_to_k` (temperature)
- `km_to_miles`, `miles_to_km` (distance)
- `kg_to_lbs`, `lbs_to_kg` (weight)

You may copy your tested functions from your converter lab repo — that is what
they are for. Extend the menu so each conversion is a real menu choice, and
wire it through `get_number()` so bad input asks again (your U1 L08 guardrail
already does the work).

## PART 2 — ADD THE GUARDRAILS (~30 min)

From your plan worksheet (U1 L10), add at least these two bounds:

1. **Overflow guard:** reject numbers over 10**15 with a clear message
   ("absurdly large — refusing to compute") and ask again.
2. **Kelvin floor:** if a conversion would produce a temperature below 0 K,
   print a warning explaining that nothing can be colder than 0 K, and refuse
   the calculation.

Implementation hint: one small function that checks a bound before the math
runs — `def is_too_big(n): ...` — beats scattering `if` statements everywhere.
That is the defensive-programming habit: **validate before you compute.**

## PART 3 — PAIR CODE REVIEW (~15 min)

Swap screens (or repos — read each other's pushed code on github.com) and find
each other's guardrail implementations:

- Which bound did your partner enforce, and how?
- What input would still sneak past their guardrail? Try to break it.
- Give one specific compliment and one specific suggestion. "Looks good" is
  not a review.

## PART 4 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-lab
git add calculator.py
git commit -m "add unit conversions and overflow/Kelvin guardrails"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

**Milestone for today:** Calculator v2 — all original tests passing, conversions
working from the menu, both guardrails live.

## TURN IN — PULL REQUEST LINK (due Sunday Oct 4, 11:59 PM)

1. Push your final `calculator.py` (conversions + guardrails working).
2. On github.com, open or update a Pull Request from your repo back to the
   original repo (Contribute → Open pull request).

Submit the PR link to this assignment on Google Classroom.
(One PR covers v1 and v2 — update the same PR if you already opened one.)

Early finishers: add the "safe mode" toggle — when on, the calculator refuses
every operation whose inputs violate your bounds; when off, it only warns. Or
write `test_calculator.py` cases that try to sneak past your own guardrails.
