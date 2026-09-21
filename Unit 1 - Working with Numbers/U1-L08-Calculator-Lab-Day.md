# U1 L08 — LAB: Calculator v1 — Safe Arithmetic

**LO:** build the first version of the unit project — a calculator that validates input and handles errors.

Today you get YOUR OWN copy of a broken calculator and fix it. This one runs on the class **VS Code server**, in the same lab repo you have been using since U1 L04 (`~/compmath-lab`).

## PART 0 — Open your lab repo (first 10 minutes)

1. Check your school Gmail — you have an invitation to collaborate on your own private repo: `compmath-u1-calculator-lab-$(whoami)`. (`whoami` shows your userid — `$(whoami)` is it spelled out.) If you have not accepted it yet, accept it now.
2. Open a terminal and check whether your clone is already there:

```bash
ls ~/compmath-lab
```

- **If you see `calculator.py` and `test_calculator.py`** — you are set; the lab files arrived with the invitation. Go to step 3.
- **If it says "No such file or directory"** you never cloned (or the clone is gone — new workspace, fresh account). Rebuild it, then `cd` in:

```bash
git clone https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-$(whoami)_student.git compmath-lab
cd ~/compmath-lab
```

- `whoami` shows your userid and `$(whoami)` inserts it into the URL automatically — same as U1 L07.
- And if git says "not a git repository", you are in the wrong folder — run `pwd`, then `cd ~/compmath-lab` before doing any git work.
3. **Always pull before you start working** — it gets any changes I pushed to your repo since last class:

```bash
git config pull.rebase false
git pull
```

- `git config pull.rebase false` tells git how to combine work; run it once, it is not an error if you already ran it.
- If the pull prints `Already up to date.` you have everything. Either way, go to PART 1.

## PART 1 — SEE IT FAIL (10 min)

In your repo folder (VS Code server terminal), first check where you are:

```bash
cd ~/compmath-lab
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

Use the patterns from the U1 L06 lesson. Run `python3 test_calculator.py`
after each fix — each PASS is a guardrail working.

**Milestone for today:** basic operations working, all 4 self-check tests passing.

## PART 3 — SAVE YOUR WORK (5 min — same loop as always)

```bash
cd ~/compmath-lab
git config pull.rebase false
git pull
git add calculator.py
git commit -m "add input validation and divide-by-zero guardrails"
git push
```

- The `git config pull.rebase false` line tells git how to combine work when the repo on GitHub has changes you do not have yet. Run it once; it is not an error if you already ran it.
- If your push is ever rejected with a message like "remote contains work you do not have", run `git pull` and then `git push` again.
- **Asked for a username/password?** GitHub username plus Personal Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.

## TURN IN — PULL REQUEST LINK (due Sunday Sep 27, 11:59 PM)

1. Push your final `calculator.py` (all 4 tests passing).
2. On github.com, open a Pull Request from your repo back to the original repo
   (Contribute → Open pull request).

Submit the PR link to this assignment on Google Classroom.

Early finishers: add `%` and `**` to the menu, or reject absurdly large
numbers (over 10**15) with an overflow warning.