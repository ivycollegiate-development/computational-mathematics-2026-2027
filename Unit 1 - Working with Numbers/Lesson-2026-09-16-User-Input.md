# U1 L4 — User Input in Python

**LO:** take input with `input()`, convert strings to numbers with `int()` / `float()`.

Everything today happens in your VS Code workspace. No paper worksheet.

## PART 0 — Get today's lesson (first 5 minutes)

1. Sign in to your workspace: https://vscode.ivycollegiate.org/ (SCHOOL Google account).
2. In the terminal, refresh the course repo:

```bash
pwd
cd ~/computational-mathematics-2026-2027
git pull
```

(Always start with `pwd` — know where you are before you type anything else.)

3. Open: `Unit 1 - Working with Numbers` → this file.

## PART 0.5 — GITHUB ACCOUNT CHECK (5 min)

Monday's lab runs in your own GitHub repo, so you need a GitHub account today.
In your workspace browser, go to https://github.com and look at the top-right corner:

- **Already signed in?** Good. Copy your GitHub username into the top of your journal file.
- **No account, or not signed in?** Raise your hand — sort it out now, not on Monday.
  Create one with your SCHOOL email: https://github.com/signup
- **Have an account but forgot the username?** Raise your hand.

Mr. Jones is collecting usernames today. Without one, your Monday lab repo cannot be created.

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

**Key idea:** whatever the user types comes back from `input()` as a **string** — even
when it looks like a number. `"13" + 1` blows up because a string and an integer are
different kinds of things.

## PART 2 — CONVERSION (10 min)

```python
>>> int("13") + 1
>>> float("13") + 1
>>> int("13.5")     # 💥 why does this fail?
>>> float("13.5") + 1
>>> int(13.9)       # does int() round? or chop?
>>> int("hello")    # remember this error — it is Monday's whole lab
```

Write your prediction for each line BEFORE you press Enter. Keep your guesses — right
or wrong, you will paste them into your notes later.

## PART 3 — CODE-ALONG: AGE CALCULATOR (15 min)

Leave the REPL (`exit()`), then create `age-calculator.py` in your home directory
(VS Code: New File, or `nano age-calculator.py`) and type this in with me:

```python
# Age calculator
birth_year = input("What year were you born? ")
birth_year = int(birth_year)
age = 2026 - birth_year
print("You are about", age, "years old.")
```

Run it with a few different years. Then feed it `banana` and watch it die.
Leave it broken on purpose — you fix it on Friday.

## PART 4 — PITFALL DEMO (5 min)

Try these in the REPL, then talk them over with a partner:

```python
>>> int("  42  ")     # spaces are okay?
>>> int("4 2")        # what about a space in the middle?
>>> float("1e3")      # surprise! what is this?
```

## PART 5 — JOURNAL (last 5 min)

Name your journal uniquely — `journal-0916-<yourname>.md`
(use your own name, like `journal-0916-mei.md`). Answer in 2-3 sentences:
- Why does `input()` hand you a string instead of a number?
- What did `banana` do to the age calculator, and why?

Also create `repl-notes-0916-<yourname>.md` (same unique name) and paste in your PART 2
guesses (right or wrong — the guesses are the point) beside what really happened.

## PART 6 — FIRST PUSH (last 10 min — rehearsal for Monday's graded lab)

Push today's two files to GitHub. Type each command exactly:

```bash
cd ~
git init compmath-u1-push-test
cd compmath-u1-push-test
git remote add origin https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-<YOUR-STEM>_student.git
cp ~/journal-0916-*.md ~/repl-notes-0916-*.md .
git add journal-0916-*.md repl-notes-0916-*.md
git commit -m "Day 09 journal and REPL notes"
git push -u origin main
```

**⚠️ Your stem:** `<YOUR-STEM>` is the short code from your school email, like
`schen27` — so the repo is `compmath-u1-calculator-lab-schen27_student`.

- **Asked for a username/password?** Use your GitHub username plus a Personal Access
  Token (PAT) — never your GitHub password. Raise your hand and we will set your PAT
  up; every push from here on needs one.
- **`repository not found` or `403`?** Your account is not connected to your repo yet —
  raise your hand. This is exactly the thing we want to catch TODAY rather than Monday.
- **Success?** You should see `Branch 'main' set up to track...`. Open your repo on
  github.com and both files will be sitting there. That is the whole loop:
  edit → add → commit → push. You will repeat it every week.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot of your terminal showing, in order:
1. `git pull` output (today's lesson on top)
2. PART 2 outputs (all six lines, including the two 💥)
3. Your age calculator running twice (one good year, one `banana` crash)
4. Your `git push` succeeding (the `Branch 'main' set up to track...` line)

Submit the screenshot to this assignment on Google Classroom.
Mac: `Cmd+Shift+4` · Windows: `Win+Shift+S`. Leave the terminal open — spot-checks.
