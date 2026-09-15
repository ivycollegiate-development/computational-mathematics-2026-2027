# U1 L6 — LAB: Calculator v1 — Safe Arithmetic

**LO:** build the first version of the unit project — a calculator that validates input and handles errors.

Today you get YOUR OWN copy of a broken calculator and fix it. This one runs in **Codespaces**.

## PART 0 — Get your lab repo (first 10 minutes)

1. Check your school Gmail — you have an invitation to collaborate on your own private repo: `compmath-u1-calculator-lab-<your-name>`. Accept it.
2. Your repo: github.com/ivycollegiate-development/compmath-u1-calculator-lab-<your-name>.
4. Open it in Codespaces: green **Code** button → **Codespaces** tab → **Create codespace**.
   (Or clone it in your VS Code workspace terminal — both are fine.)

## PART 1 — SEE IT FAIL (10 min)

In the Codespace terminal, first check where you are:

```bash
pwd
python3 calculator.py
```

- Pick divide, type `hello` for a number → 💥 crash.
- Run again, pick divide, type `5` and `0` → 💥 crash (different error — read it).

Then run the self-check:

```bash
python3 test_calculator.py
```

You should see **1/4 passing**. Your goal today: **all 4 passing**.

## PART 2 — FIX IT (in pairs, ~40 min)

Open `calculator.py`. There are two `FIX ME` bugs:

1. `get_number()` — wrap the conversion in `try/except ValueError`, print a
   friendly message, and ask again (loop).
2. `divide()` — handle `b == 0` before dividing: print a friendly message
   and return `None`. In `main()`, skip printing when the result is `None`.

Use the patterns from the U1 L5 lesson. Run `python3 test_calculator.py`
after each fix — each PASS is a guardrail working.

**Milestone for today:** basic operations working, all 4 self-check tests passing.

## PART 3 — SAVE YOUR WORK (5 min)

```bash
git add calculator.py
git commit -m "add input validation and divide-by-zero guardrails"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## PART 4 — TURN IN (due Sunday Sep 27, 11:59 PM)

1. Push your final `calculator.py` (all 4 tests passing).
2. On github.com, open a Pull Request from your repo back to the original repo
   (Contribute → Open pull request).
3. Turn in the PR link on Google Classroom.

Early finishers: add `%` and `**` to the menu, or reject absurdly large
numbers (over 10**15) with an overflow warning.