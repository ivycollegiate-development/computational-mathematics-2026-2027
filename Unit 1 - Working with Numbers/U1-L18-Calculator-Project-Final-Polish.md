# U1 L18 — Calculator Project: Final Polish (TECH)

**Unit:** 1 — Working with Numbers
**Type:** Machine (project final push, 85 minutes)
**LO:** finish the Calculator with Guardrails project to a submittable standard — all functions work, boundaries guarded, tests pass, analysis honest

---

## TODAY'S PURPOSE

Last working day on the Calculator project. You are not building new features. You are taking what you have and making it **correct, complete, and honest** — then submitting it.

---

## PART 0 — OPEN YOUR REPO AND AUDIT YOURSELF (20 min)

```bash
pwd
cd ~/compmath-u1-calculator-lab
git pull
python3 test_calculator.py
```

Now grade yourself honestly against the rubric. **Tick a box only if it is true, not if it is nearly true.**

### Core functions

- ☐ `get_number(prompt)` — validates, re-asks on bad input, refuses out-of-range
- ☐ `get_operation()` — accepts only `+ - * / // % **`, re-asks otherwise
- ☐ `c_to_f`, `f_to_c`, `c_to_k`, `k_to_c` — all four conversions correct
- ☐ `add, sub, mul, div, floor_div, mod, pow` — all seven operations correct
- ☐ Division by zero → clear message, not a crash

### Boundaries (the two numbers this unit was about)

- ☐ `c_to_k` refuses input `< -273.15` with message "Below absolute zero — refusing."
- ☐ `f_to_c` refuses input that would produce `< -273.15 °C`
- ☐ `add/sub/mul` refuse inputs where `|result| > 10**15` with "Result exceeds safe integer range."
- ☐ `div/floor_div/mod` refuse divisor `== 0` with "Division by zero — refusing."

### Quietly wrong vs crashed

- ☐ No function returns `0.0` when the user meant `0` (type consistency)
- ☐ No function returns `float` when `int` is mathematically exact (use `Fraction` or return `int`)
- ☐ `10**15 + 1` does not silently become `1000000000000000.0` — it is refused

### Tests

- ☐ `python3 test_calculator.py` prints `all tests passed`
- ☐ You can explain what each test is checking (not just that it passes)

### Analysis (`analysis.md`)

- ☐ One paragraph per function group (conversions, arithmetic, input) — three paragraphs total
- ☐ Each paragraph names the audience and the one thing they should notice
- ☐ Each paragraph contains **one honest limitation**
- ☐ You did not claim anything the code does not actually do

---

## PART 1 — FIX WHAT IS ACTUALLY WRONG (50 min)

Work in this order. **Do not skip to polish while something is still broken.**

1. **Does it run?** `test_calculator.py` passes. Fix this before anything else.
2. **Are the boundaries real?** Re-read every guard. If you wrote `if c < -273.15:` but the test passes `-273.15`, does it refuse or accept? The spec says "below absolute zero" — `-273.15` is exactly absolute zero. Decide and be consistent.
3. **Are the types honest?** `type(5/2)` is `float`. `type(4/2)` is `float`. Do you want that? The rubric says "return `int` when mathematically exact." Fix it.
4. **Now** polish: docstrings on every function, readable variable names, consistent error message format.

**If a function is missing**, say so in `analysis.md` and explain what you tried. A **documented gap is honest work. A silent gap is a lie.**

---

## PART 2 — FINAL COMMIT (15 min)

```bash
cd ~/compmath-u1-calculator-lab
git add calculator.py test_calculator.py analysis.md
git commit -m "final: calculator with guardrails — all boundaries guarded, tests pass"
git push
```

Verify on github.com that all files are visible and the commit is there.

---

## TURN IN (Google Classroom, due 23:59 tonight)

1. Your completed self-audit checklist (all boxes ticked or explained)
2. Your final `git push` confirmation
3. Screenshot of the GitHub repo showing the latest commit

Submit to the U1 L18 assignment.

**Keep the terminal open** — spot-checks.

---

## 📋 TOMORROW

**Next:** U1 L19 — Calculator Project: Submission & Peer Review. You submit the PR, then review a partner's project using the same rubric.

---

## 🇹🇼 TAIWAN CONTEXT

The "quietly wrong" category is the Unit 1 version of what the Taiwan CERT calls "silent data corruption" — a computation that finishes successfully and returns a plausible-looking number that is, in fact, wrong. The boundary guards (`-273.15`, `10**15`, division by zero) are your checksums. If you don't have them, you're not computing — you're guessing.