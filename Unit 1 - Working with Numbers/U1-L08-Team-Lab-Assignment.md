# U1 L08 — TEAM LAB: Calculator v1 — Safe Arithmetic (Sep 22-23)

**LO:** plan and build the first version of the unit project — a calculator that validates input and handles errors — as a team.

**This lab is now a TEAM lab.** Teams of 3-4. I pick the teams; find your team name and teammates on the board. Today (Tuesday, Sep 22) is a **no-electronics planning day**: no laptops, no phones — the work is talking, deciding, and writing. Tomorrow (Wednesday, Sep 23) your team builds the calculator **in Codespaces**. Everything you decide today is what you will build tomorrow, so make the plan good.

## PART 0 — TODAY: PLAN AS A TEAM (no electronics)

Your team does the **U1 L08 worksheet together**. Every team member fills in their own copy, but the answers must be agreed as a team — argue until you agree, then write it down.

1. **Part A — Predict:** agree on one prediction per line. If you disagree, say why and settle it.
2. **Part B — Label the guards:** agree on what each line protects against.
3. **Part C — Plan tomorrow's build:** this is the most important part. Your team writes the numbered build plan in plain English. This plan is your tomorrow.
4. **Part D — Attack ideas:** brainstorm at least 4 inputs that could break the calculator. This list becomes tomorrow's test list.
5. **Part E — Reflection + Checkout:** every member writes their own answers; checkout is from memory, no notes.

**Pick your team roles now** (every member needs one; roles rotate at least once tomorrow):

- **Driver** — the one whose Codespace is open; types the code.
- **Navigator** — reads the build plan aloud, tells the driver what comes next.
- **Tester** — runs `python3 test_calculator.py` after every change and reports the score.
- **Recorder** — keeps the team's plan and attack list handy and updates the build checklist.

A team of 3 drops the Recorder (Driver keeps the checklist); a team of 4 uses all four.

## PART 1 — TOMORROW: OPEN YOUR TEAM CODESPACE (first 10 min)

1. Check your school Gmail — you have an invitation to collaborate on your **team repo**: `compmath-u1-calculator-team-<your team number>` (the exact name is on the board). If you have not accepted it yet, accept it now.
2. Go to github.com, sign in with your school GitHub account, open the team repo, and click the green **Code** button → **Codespaces** → open the Codespace.
3. In the Codespace terminal, check the lab files arrived:

```bash
ls ~/compmath-u1-calculator-team
```

- You should see `calculator.py` and `test_calculator.py`. If you do not, raise your hand — do not start guessing.

4. **Always pull before you start** — teammates share this repo, so this matters more than ever:

```bash
git config pull.rebase false
git pull
```

- If the pull prints `Already up to date.` you have everything. Either way, go to PART 2.

## PART 2 — SEE IT FAIL (10 min)

In the Codespace terminal:

```bash
python3 calculator.py
```

- Pick divide, type `hello` for a number → crash.
- Run again, pick divide, type `5` and `0` → crash (a different error — read it).

Then run the self-check:

```bash
python3 test_calculator.py
```

You should see **1/4 passing**. Your team's goal today: **all 4 passing**.

## PART 3 — BUILD IT AS A TEAM (~40 min)

Open `calculator.py`. There are two `FIX ME` bugs:

1. `get_number()` — wrap the conversion in `try/except ValueError`, print a friendly message, and ask again (loop).
2. `divide()` — handle `b == 0` before dividing: print a friendly message and return `None`. In `main()`, skip printing when the result is `None`.

Team rules:

- Follow the numbered build plan you agreed on today (worksheet Part C). Build in that order.
- The **Driver** types. Everyone else navigates: point at the line, read the plan, suggest. Do not grab the keyboard.
- **Rotate roles at least once** — when the first bug is fixed, the Driver hands off to the next member. Nobody finishes this lab without having driven.
- The **Tester** runs `python3 test_calculator.py` after every change and calls the score out loud. Each PASS is a guardrail working.
- Use your Part D attack list: after the fixes pass the self-check, try every input on your attack list. If any of them crashes the calculator, that is a bug — fix it before you push.

**Milestone for today: all 4 self-check tests passing AND your attack list produces no crashes.**

## PART 4 — SAVE YOUR WORK (5 min — same loop as always)

```bash
git config pull.rebase false
git pull
git add calculator.py
git commit -m "add input validation and divide-by-zero guardrails"
git push
```

- Because teammates share one repo, **pull before you push, every time**. If two teammates changed the same lines, git will say so — raise your hand instead of guessing.
- **Asked for a username/password?** GitHub username plus Personal Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.

## TURN IN — PULL REQUEST LINK + TEAM STATEMENT (due Sunday Sep 27, 11:59 PM)

1. Push your final `calculator.py` (all 4 tests passing, attack list clean).
2. On github.com, open a Pull Request from your team repo back to the original repo (Contribute → Open pull request).
3. **Every team member submits** the same PR link, plus ONE sentence saying what you personally did on the team (your role, what you built or caught). The team statement is how I see everyone worked — no sentence, no credit.

Submit to this assignment on Google Classroom.

Early finishers: add `%` and `**` to the menu, or reject absurdly large numbers (over 10**15) with an overflow warning.
