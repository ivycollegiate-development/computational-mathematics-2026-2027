# Day 09 — User Input in Python (Mon 2026-09-14)

**LO:** take input with `input()`, convert strings to numbers with `int()` / `float()`.

Everything today happens in your VS Code workspace. No paper worksheet.

## PART 0 — Get today's lesson (first 5 minutes)

1. Log into your workspace: https://vscode.ivycollegiate.org/ (SCHOOL Google account).
2. In the terminal, update the course repo:

```bash
cd ~/computational-mathematics-2026-2027
git pull
```

3. Open: `Unit 1 - Working with Numbers` → this file.

## PART 0.5 — GITHUB ACCOUNT CHECK (5 min)

Your Friday lab needs your own GitHub account. In your workspace browser, go to
https://github.com and check the top-right corner:

- **Signed in?** You're set. Write your GitHub username at the top of `journal-0914.md`.
- **Not signed in / no account?** Raise your hand now — do not wait for Friday.
  Sign up with your SCHOOL email: https://github.com/signup
- Already have an account but can't remember the username? Raise your hand.

Mr. Jones will collect usernames from anyone who signs up today — your Friday
lab repo cannot be created without it.

## PART 1 — INPUT() (10 min)

Start Python:

```bash
python3
```

```python
>>> name = input("What is your name? ")
>>> print("Hello, " + name)
>>> age = input("How old are you? ")
>>> age + 1        # 💥 what happened? WHY?
```

**Key idea:** `input()` ALWAYS gives you a **string**, even when the user types digits.
`"13" + 1` fails because you cannot add a string and a number.

## PART 2 — CONVERSION (10 min)

```python
>>> int("13") + 1
>>> float("13") + 1
>>> int("13.5")     # 💥 why does this fail?
>>> float("13.5") + 1
>>> int(13.9)       # does int() round? or chop?
>>> int("hello")    # 💥 remember this error — it is Friday's whole lab
```

Predict each line BEFORE running it. Write down your guesses.

## PART 3 — CODE-ALONG: AGE CALCULATOR (15 min)

Exit the REPL (`exit()`), create `age-calculator.py` in your home directory
(VS Code: New File, or `nano age-calculator.py`), and type this in with me:

```python
# Age calculator
birth_year = input("What year were you born? ")
birth_year = int(birth_year)
age = 2026 - birth_year
print("You are about", age, "years old.")
```

Run it a few times with different years. Then try typing `banana` as your birth
year and watch the crash. Don't fix it yet — that's Wednesday.

## PART 4 — PITFALL DEMO (5 min)

Type this in the REPL and discuss with a partner:

```python
>>> int("  42  ")     # spaces are okay?
>>> int("4 2")        # what about a space in the middle?
>>> float("1e3")      # surprise! what is this?
```

## PART 5 — JOURNAL (last 5 min)

Create `journal-0914.md` in your home directory. Answer in 2-3 sentences:
- Why does `input()` give you a string instead of a number?
- What did typing `banana` do to the age calculator, and why?

Also create `repl-notes-0914.md` and paste in your PART 2 guesses (right or wrong —
guesses are the point) next to what actually happened.

## PART 6 — FIRST PUSH (last 10 min — practice before Friday's graded lab)

Push today's two files to GitHub. Type each command exactly:

```bash
cd ~
git init compmath-u1-push-test
cd compmath-u1-push-test
git remote add origin https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-<YOUR-STEM>_student.git
cp ~/journal-0914.md ~/repl-notes-0914.md .
git add journal-0914.md repl-notes-0914.md
git commit -m "Day 09 journal and REPL notes"
git push -u origin main
```

**⚠️ Your stem:** `<YOUR-STEM>` is the short code from your school email, like
`schen27` — the repo is named `compmath-u1-calculator-lab-schen27_student`.

- **Asked for a username/password?** Use your GitHub username + a Personal Access
  Token (PAT), not your GitHub password. Raise your hand and we'll set up your PAT
  — every push from now on needs one.
- **`repository not found` or `403`?** Your account isn't connected to your repo
  yet — raise your hand. This is exactly the problem we want to find TODAY,
  not Friday.
- **Success?** You should see `Branch 'main' set up to track...` — check your repo
  on github.com and you'll see your two files. That's the whole skill: edit →
  add → commit → push. You'll do this every week from now on.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot of your terminal showing, in order:
1. `git pull` output (today's lesson on top)
2. PART 2 outputs (all six lines, including the two 💥)
3. Your age calculator running twice (one good year, one `banana` crash)
4. Your `git push` succeeding (the `Branch 'main' set up to track...` line)

Submit the screenshot to this assignment on Google Classroom.
Mac: `Cmd+Shift+4` · Windows: `Win+Shift+S`. Keep the terminal open — spot-checks.
