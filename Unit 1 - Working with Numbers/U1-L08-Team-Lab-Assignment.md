# U1 L08 — TEAM LAB: Calculator v1 — Safe Arithmetic (Two-Day Build)

**LO:** plan and build the first version of the unit project — a calculator that validates input and handles errors — as a team.

**This lab is a TEAM lab, and the build takes TWO days.** Teams of 3-4. I picked the teams; your team name and teammates are on the board. The plan day (no electronics) is done — your worksheet Parts A-E are agreed and checked. Now you build on **Day 1 (Wednesday)** and **Day 2 (Thursday)** in your team Codespace. Everything you decided on the plan day is what you build these two days, so follow the plan.

## PART 0 — THE PLAN YOU MADE (keep it open)

Your team's worksheet is your build script:

1. **Part A — Predictions:** check these against what you actually see on Day 1.
2. **Part B — Guards:** what each line protects against — you are about to prove it.
3. **Part C — Build plan:** your numbered, plain-English build order. Follow it in order across both days.
4. **Part D — Attack list:** your test list for Day 2.
5. **Part E — Reflection:** every member keeps their own copy for the checkout.

**Team roles** (every member has one; roles rotate at least once per day):

- **Driver** — the one whose Codespace is open; types the code.
- **Navigator** — reads the build plan aloud, tells the driver what comes next.
- **Tester** — runs `python3 test_calculator.py` after every change and reports the score.
- **Recorder** — keeps the plan and attack list handy and updates the build checklist.

A team of 3 drops the Recorder (Driver keeps the checklist); a team of 4 uses all four.

## DAY 1 — OPEN YOUR TEAM CODESPACE (first 10 min)

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

- If the pull prints `Already up to date.` you have everything. Either way, go to PART 1.

## DAY 1 — SEE IT FAIL (10 min)

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

You should see **1/4 passing** (test 4, quit, already works). Your two-day goal: **all 4 passing**.

## DAY 1 — FIX THE FIRST BUG (~40 min)

Open `calculator.py`. There are two `FIX ME` bugs. **Day 1 is bug 1 only:**

1. `get_number()` — wrap the conversion in `try/except ValueError`, print a friendly message, and ask again (loop).

This is the one behind **test 1** (bad input does not crash). Team rules:

- Follow the numbered build plan from worksheet Part C. Build in that order.
- The **Driver** types. Everyone else navigates: point at the line, read the plan, suggest. Do not grab the keyboard.
- **Rotate roles at least once** — when the bug is fixed, the Driver hands off to the next member. Nobody finishes this lab without having driven.
- The **Tester** runs `python3 test_calculator.py` after every change and calls the score out loud. Each PASS is a guardrail working.

**Milestone for Day 1: test 1 passing — 2/4.** Do NOT touch `divide()` yet; that is Day 2.

## DAY 1 — SAVE YOUR WORK (5 min — same loop as always)

```bash
git config pull.rebase false
git pull
git add calculator.py
git commit -m "add input validation guardrail"
git push
```

- Because teammates share one repo, **pull before you push, every time**. If two teammates changed the same lines, git will say so — raise your hand instead of guessing.
- **Asked for a username/password?** GitHub username plus Personal Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.

## DAY 2 — WARM-UP: PULL AND RE-CHECK (first 10 min)

1. Open your team Codespace (same one as Day 1 if you can).
2. Pull before you work — a teammate may have pushed after you left:

```bash
cd ~/compmath-u1-calculator-team
git config pull.rebase false
git pull
```

3. Re-run the self-check to confirm where you are:

```bash
python3 test_calculator.py
```

- You should still see **2/4 passing**. If you see anything else, raise your hand before changing anything.

## DAY 2 — FIX THE SECOND BUG (~40 min)

**Day 2 is bug 2:**

1. `divide()` — handle `b == 0` before dividing: print a friendly message and return `None`. In `main()`, skip printing when the result is `None`.

These are **tests 2 and 3** (divide by zero handled; the program still works after an error). Team rules are the same as Day 1 — Driver types, Navigator reads the plan, Tester calls the score, and **rotate roles at least once again** so everybody drives across the two days.

**Milestone for Day 2: all 4 self-check tests passing.** Then run your worksheet Part D attack list: try every input on it. If any of them crashes the calculator, that is a bug — fix it before you push.

## DAY 2 — SAVE YOUR WORK (5 min — same loop as always)

```bash
git config pull.rebase false
git pull
git add calculator.py
git commit -m "add divide-by-zero guardrail"
git push
```

- Pull before you push, every time.
- **Asked for a username/password?** GitHub username plus PAT — never your GitHub password. Raise your hand if yours is lost.

## TURN IN — PULL REQUEST LINK + TEAM STATEMENT (due Sunday Sep 27, 11:59 PM)

1. Push your final `calculator.py` (all 4 tests passing, attack list clean).
2. On github.com, open a Pull Request from your team repo back to the original repo (Contribute → Open pull request).
3. **Every team member submits** the same PR link, plus ONE sentence saying what you personally did across the two days (your role, what you built or caught). The team statement is how I see everyone worked — no sentence, no credit.

Submit the PR link to this assignment on Google Classroom.

Early finishers: add `%` and `**` to the menu, or reject absurdly large numbers (over 10**15) with an overflow warning.