# Day 10 — Error Handling with try/except (Wed 2026-09-16)

**LO:** handle invalid input with `try/except` so programs don't crash.

Everything today happens in your VS Code workspace. No paper worksheet.

## PART 0 — Get today's lesson (first 5 minutes)

```bash
pwd
cd ~/computational-mathematics-2026-2027
git pull
```

Open: `Unit 1 - Working with Numbers` → this file.

## PART 1 — THE CRASH, AGAIN (5 min)

Run Monday's age calculator and feed it `banana`. Same crash as before.
Today you learn the tool that stops it: `try/except`.

## PART 2 — TRY/EXCEPT IN THE REPL (10 min)

```bash
python3
```

```python
>>> try:
...     x = int("banana")
... except ValueError:
...     print("That is not a number.")
...
>>> try:
...     x = int("banana")
... except ValueError:
...     print("That is not a number.")
... else:
...     print("Got", x)
...
>>> try:
...     1 / 0
... except ZeroDivisionError:
...     print("No dividing by zero!")
```

Watch exactly which error name each except catches. The name matters.

## PART 3 — CODE-ALONG: FIX THE AGE CALCULATOR (15 min)

Open Monday's `age-calculator.py` and rewrite it:

```python
# Age calculator v2 — with guardrails
while True:
    raw = input("What year were you born? (or q to quit) ")
    if raw == "q":
        break
    try:
        birth_year = int(raw)
    except ValueError:
        print("That is not a year. Try again.")
        continue
    print("You are about", 2026 - birth_year, "years old.")
```

Test it: a good year, then `banana`, then `q`. It should survive everything.

## PART 4 — CHALLENGE (10 min)

Write `number-doubler.py`: ask for a number, print double that number.
Rules:
- Bad input must NOT crash — ask again.
- It must keep asking until the user types `q`.

(Hint: this is the age calculator loop with a different calculation.)

## PART 5 — JOURNAL (last 5 min)

Give your journal a unique name — `journal-0916-<yourname>.md`
(same convention as Monday, e.g. `journal-0916-mei.md`). Answer in 2-3 sentences:
- What does `try/except` let your program do that it couldn't do before?
- Which is worse in a real program: a clean error message, or a crash? Why?

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. `git pull` output
2. PART 2 outputs (all three try/except blocks)
3. Age calculator v2 surviving `banana` then a good year
4. Your number doubler surviving at least one bad input

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
