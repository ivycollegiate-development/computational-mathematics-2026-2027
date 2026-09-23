# U1 L09 — Unit Conversions and Real-World Math

**LO:** write your own functions for real-world unit conversions using `def` and `return`.

Today you get your own copy of a broken **unit converter** and fix it. It runs
in Codespaces, same as the two-day calculator build (U1 L08). Everything you
build today goes straight into the Calculator v2 lab (U1 L11).

## PART 0 — CODE-ALONG: `def` AND `return` (15 min)

A function is a named recipe. It takes ingredients (parameters), does the work,
and hands back a result:

```python
def c_to_f(c):
    return c * 9 / 5 + 32

print(c_to_f(100))    # 212.0
print(c_to_f(37))     # 98.6
print(c_to_f(-40))    # -40  (the famous crossover point)
```

In the REPL, first answer in your notes, then test:

- Why does `return c * 9 / 5 + 32` work without parentheses? (Order of operations.)
- What happens if you use `print` instead of `return` inside the function?
- What does a function with no `return` hand back?

## PART 1 — CODE-ALONG: TEMPERATURE (15 min)

Together we build the temperature section: Celsius↔Fahrenheit and Celsius↔Kelvin.

```python
def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_k(c):
    return c + 273.15
```

- Test each one with a value you already know (boiling water, freezing water,
  body temperature, -40).
- Kelvin has a hard floor: nothing can be colder than 0 K. What should
  `c_to_k` do if you hand it -300 °C? (Hold that thought — it comes back in
  (U1 L11's guardrails.)

## PART 2 — GET YOUR CONVERTER LAB REPO (first 10 minutes of the lab)

1. Check your school Gmail — you have an invitation to collaborate on your own
   private repo: `compmath-u1-converter-lab-<your-name>`. Accept it.
2. Your repo: github.com/ivycollegiate-development/compmath-u1-converter-lab-<your-name>.
3. Open it in Codespaces: green **Code** button → **Codespaces** tab →
   **Create codespace**. (Or clone it in your VS Code workspace terminal — both fine.)

## PART 3 — SEE IT FAIL, THEN SEE IT LIE (10 min)

```bash
pwd
python3 converter.py
```

- Pick a conversion, type `hello` for a number → 💥 crash.
- Pick **°F → °C** and enter 212 → it answers **117.78**. That is *wrong* —
  212 °F is 100 °C, not 117.78. **No crash, no error, just a quietly wrong
  answer.** These are the most dangerous bugs there are.

Then run the self-check:

```bash
python3 test_converter.py
```

You should see **3/5 passing**. Your goal today: **all 5 passing**.

## PART 4 — FIX IT (in pairs, ~35 min)

Open `converter.py`. There are two `FIX ME` bugs:

1. `f_to_c()` — the formula is missing a step. Compare it with the
   code-along version above. This is the quietly-wrong one.
2. `get_number()` — wrap the conversion in `try/except ValueError`, print a
   friendly message, and ask again (same pattern as your calculator lab).

Use the patterns from L6 and L8. Run `python3 test_converter.py` after each
fix — each PASS is one more way the converter can't hurt anyone.

## PART 5 — PAIR PROGRAMMING: DISTANCE AND WEIGHT (~20 min)

With your partner, write the remaining functions — you are on your own now:

- `km_to_miles(km)` and `miles_to_km(mi)`
- `kg_to_lbs(kg)` and `lbs_to_kg(lbs)`

Conversion facts: 1 mile = 1.609344 km exactly; 1 lb = 0.45359237 kg exactly.

- Verify each function against one real trip/weight you know.
- Add them to the menu so a user can actually pick them.

**Milestone for today:** all 5 self-checks passing, and all four new conversion
functions working from the menu.

## PART 6 — DISCUSSION: WHEN DO UNIT CONVERSIONS CAUSE REAL HARM? (10 min)

Case study: **Mars Climate Orbiter, 1999.** Lockheed Martin's navigation
software sent thrust data in *pound-force seconds*; NASA's software expected
*newton-seconds*. Nobody's program crashed. The $125M spacecraft entered the
Martian atmosphere too low and was destroyed. A conversion mismatch, passed
silently from one program to another.

In your notes: what would have caught it — a crash, or a guardrail?

## PART 7 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-converter-lab
git add converter.py
git commit -m "fix conversion formula and add input validation"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## TURN IN — PULL REQUEST LINK (due Sunday Sep 27, 11:59 PM)

1. Push your final `converter.py` (all 5 tests passing, all conversions working).
2. On github.com, open a Pull Request from your repo back to the original repo
   (Contribute → Open pull request).

Submit the PR link to this assignment on Google Classroom.

Early finishers: add a Kelvin floor check to `c_to_k` (warn if the result would
be below 0 K), or reject absurdly large numbers (over 10**15) with a warning.
