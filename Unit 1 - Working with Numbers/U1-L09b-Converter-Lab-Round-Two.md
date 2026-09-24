# U1 L09b — Converter Lab, Round Two: Speed, Volume, and Guardrails

**LO:** extend your converter with new unit families and your first real
guardrails — checks that stop bad values before they become bad answers.

Last Friday you fixed a quietly-wrong formula and added input validation. Your
converter has temperature, distance, and weight, and all 5 self-checks pass.
Today I hand you two more unit families — **speed** and **volume** — and you add
them the same way a working programmer would: a little at a time, with a test
after each step. Everything you add today lands in Calculator v2 (U1 L11).

## PART 0 — WARM-UP: PULL AND VERIFY (5 min)

Open your `compmath-u1-converter-lab-<your-name>` repo in Codespaces, then:

```bash
cd ~/compmath-converter-lab
git pull
python3 test_converter.py
```

You should still see **5/5 passing**. If you see anything else, fix that first —
today builds on top of last Friday's work, and you cannot extend a broken base.

## PART 1 — CODE-ALONG: SPEED (10 min)

One new family, same recipe. Add to `converter.py`:

```python
def kph_to_mph(kph):
    return kph / 1.609344

def mph_to_kph(mph):
    return mph * 1.609344
```

In the REPL, first answer in your notes, then test:

- Why does one function divide and the other multiply? (Inverse operations.)
- A Taiwan freeway limit is 110 km/h. What is that in mph? Does the answer
  match what a US road sign would say?
- Why does speed use the *same* 1.609344 factor as distance? (Speed is
  distance per time — the units inherit the conversion.)

Add both to the menu so a user can pick them.

## PART 2 — CODE-ALONG: VOLUME (10 min)

```python
def l_to_gal(liters):
    return liters / 3.785411784

def gal_to_l(gallons):
    return gallons * 3.785411784
```

- A US gallon of milk is about 3.785 L. Verify `gal_to_l(1)`.
- Gasoline in Taiwan is priced per liter; in the US per gallon. If gas is
  NT$31/L, what is that per gallon? (NT$117 or so — check with your function.)

## PART 3 — PAIR WORK: TESTS FOR EVERYTHING (~15 min)

A converter without tests is a converter that can quietly lie again. With your
partner, extend `test_converter.py` so every new family is covered:

- `kph_to_mph(110)` ≈ 68.35
- `mph_to_kph(60)` ≈ 96.56
- `l_to_gal(3.785411784)` == 1.0
- `gal_to_l(2)` ≈ 7.57

Copy the existing test pattern — assert with a tolerance, print PASS/FAIL,
count at the end. **Milestone:** your self-check now says **9/9** (or however
many you wrote — the point is every function has one).

## PART 4 — GUARDRAILS: THE KELVIN FLOOR (10 min)

Last Friday's stretch idea becomes today's main event. Kelvin has a hard floor:
0 K is absolute zero — nothing in this universe is colder.

```python
def c_to_k(c):
    k = c + 273.15
    if k < 0:
        print(f"WARNING: {c} °C is below absolute zero — no such temperature.")
        return None
    return k
```

In your notes:

- Why return `None` instead of the nonsense number? (A wrong-but-plausible
  answer is worse than no answer — Mars Climate Orbiter, again.)
- Who is the guardrail for — the user, or the next programmer?

## PART 5 — SAVE YOUR WORK (5 min)

```bash
git add converter.py test_converter.py
git commit -m "add speed and volume conversions, kelvin floor guardrail"
git push
```

## TURN IN — UPDATE YOUR PULL REQUEST (due at end of class, 11:59 PM tonight)

1. Push your final work (all tests passing, guardrail in place).
2. Your Pull Request from last Friday is still open — your new commits attach
   to it automatically. Open it on github.com and confirm your latest commits
   appear.
3. In your PR, leave one comment: which of today's additions would you keep if
   you could only keep one, and why?

Submit nothing new on Classroom — this is the same PR, updated.
