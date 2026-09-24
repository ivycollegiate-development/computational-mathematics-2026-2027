# U1 L08 — TEAM LAB BUILD: Calculator v1 — Safe Arithmetic

Team name: ____________________   Members: ___________________________________   Date: Sep 23-24

Build days for the calculator your team planned on the plan day. Day 1 is Wednesday, Day 2 is Thursday. Keep this sheet open both days — it is your build script, and it works together with the Parts A-E plan sheet you already agreed on.

## 1: Roles before anything else (Day 1, first 5 min)

Fill in who starts in each role. Rotate at least once each day — nobody finishes this lab without having driven.

| Role | Day 1 starter | Day 2 starter |
|---|---|---|
| Driver (types the code) |  |  |
| Navigator (reads the plan aloud) |  |  |
| Tester (runs the self-check, calls the score) |  |  |
| Recorder (keeps plan + attack list) |  |  |

Team of 3? Drop the Recorder — the Driver keeps the checklist.

Rotation log — write who took over and when:

| Day | Handoff 1 | Handoff 2 |
|---|---|---|
| Day 1 |  |  |
| Day 2 |  |  |

## 2: Open the team Codespace (Day 1, first 10 min)

☐  Every member has accepted the GitHub invitation to the team repo compmath-u1-calculator-team- plus your team number (exact name is on the board).

☐  Codespace is open from the team repo (green Code button, then Codespaces).

☐  Lab files arrived — run: ls ~/compmath-u1-calculator-team — you should see calculator.py and test_calculator.py.

☐  Pull before you start. Teammates share this repo, so this matters more than ever:

git config pull.rebase false

git pull

☐  The pull said Already up to date. or brought down changes — either way you have everything. Something missing? Raise your hand — do not start guessing.

## 3: See it fail, then check your predictions (Day 1, 10 min)

Run the calculator and feed it the two bad inputs. Watch what happens, then fill the table — this is Part A against reality.

python3 calculator.py

| Test we ran | What Part A predicted | What actually happened | Crash type |
|---|---|---|---|
| divide, then hello for a number |  |  |  |
| divide, then 5 and 0 |  |  |  |

☐  Both crashes print errors, not silence — we know where the two bugs live.

Now the self-check:

python3 test_calculator.py

☐  We see 1/4 passing (test 4, quit, already works). Our two-day goal: all 4 passing.

## 4: Fix bug 1 — get_number() (Day 1, about 40 min)

Day 1 is bug 1 ONLY — the one behind test 1 (bad input does not crash). Follow your Part C build order; check each step off as the Driver completes it:

☐  Wrap the conversion in try/except ValueError.

☐  Print a friendly message — say what went wrong and what to do instead.

☐  Ask again in a loop until the input is a real number.

☐  Tester runs python3 test_calculator.py after every change and calls the score out loud. Each PASS is a guardrail working.

Guard labeling — one line each:

| Piece we added | What it guards against | Why a guard beats a crash here |
|---|---|---|
| try/except ValueError |  |  |
| the ask-again loop |  |  |

Milestone Day 1: test 1 passing — 2/4. Do NOT touch divide() today; that is Day 2.

## 5: Save your work (Day 1, 5 min)

Pull before you push — every time. Two teammates changed the same lines? Git will say so; raise your hand instead of guessing.

☐  git config pull.rebase false

☐  git pull

☐  git add calculator.py

☐  git commit -m "add input validation guardrail"

☐  git push

Asked for a username and password? GitHub username plus Personal Access Token — never your GitHub password. Push rejected? git pull, then git push again.

## 6: Warm-up — pull and re-check (Day 2, first 10 min)

☐  Open the same team Codespace as Day 1.

☐  cd ~/compmath-u1-calculator-team

☐  git config pull.rebase false

☐  git pull — a teammate may have pushed after you left.

☐  python3 test_calculator.py — you should still see 2/4. Anything else? Stop and raise your hand before changing anything.

## 7: Fix bug 2 — divide() (Day 2, about 40 min)

Tests 2 and 3 are waiting: divide by zero handled, and the program still works after an error.

☐  Check b == 0 BEFORE dividing.

☐  Print a friendly message and return None instead of dividing.

☐  In main(), skip printing when the result is None.

☐  Rotate roles again — everybody drives across the two days.

Guard labeling — same drill as Day 1:

| Piece we added | What it guards against | Why the skip in main() matters |
|---|---|---|
| the b == 0 check |  |  |
| returning None |  |  |
| the is None skip in main() |  |  |

Milestone Day 2: all 4 self-check tests passing.

## 8: Run the attack list (Part D, Day 2)

Your Part D list is the test plan — run every input on it, one attacker each. If any attack crashes the calculator, that is a bug: fix it before you push.

| Attack input | Attacker | Predicted | Actual | Calculator survived? |
|---|---|---|---|---|
| hello (a word) |  |  |  |  |
| 5 and 0 (divide) |  |  |  |  |
| just pressing Enter |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Blank rows are your own Part D attacks — copy them in.

## 9: Save your work (Day 2, 5 min)

Same loop as always. Pull before you push, every time.

☐  git config pull.rebase false

☐  git pull

☐  git add calculator.py

☐  git commit -m "add divide-by-zero guardrail"

☐  git push

## 10: Team checkout — before you leave (Day 2)

Every member writes their own answers — this is Part E, and it is what you bring to the checkout.

1. Which attack did your calculator survive that it would not have survived on Day 1, and which guard caught it?

_________________________________________________________________________

2. Which test was the hardest to make pass, and what fixed it?

_________________________________________________________________________

3. One thing Calculator v2 should keep from the way your team worked these two days:

_________________________________________________________________________

## TURN IN — PULL REQUEST LINK + TEAM STATEMENT (due Sunday Sep 27, 11:59 PM)

☐  All 4 self-check tests passing.

☐  Attack list clean — no crash left standing.

☐  Pull Request opened on github.com from your team repo back to the original repo (Contribute, then Open pull request).

☐  Every member submits the same PR link to this assignment on Google Classroom, plus ONE sentence saying what you personally did across the two days (your role, what you built or caught). No sentence, no credit.

Keep the terminal open — spot-checks.

Early finishers: add remainder (%) and power to the menu, or reject absurdly large numbers (over 10^15) with an overflow warning.

Next: U1 L09 — Unit Conversions (Friday). The conversion functions you build next reuse these same guards.
