# U1 L10 — Security Lens: Integer Overflow and Arithmetic Boundaries

**LO:** explain integer overflow conceptually, and describe when Python protects you and when it does not.

Today is mostly a discussion day with one interactive demo. Your journal answer
feeds directly into Monday's Calculator v2 — you will be deciding the bounds
your calculator enforces.

## PART 1 — DEMO: HOW BIG CAN A PYTHON NUMBER GET? (10 min)

Open the REPL (start with `pwd`, then `python3`) and try:

```python
2 ** 10
2 ** 100
2 ** 1000
2 ** 1000000      # Python doesn't even flinch
10 ** 400 / 3     # floats, though, have limits
1.8e308 * 2       # what is this?
```

- Python integers have **arbitrary precision** — they grow as big as memory
  allows. Type `2 ** 1000` and count the digits.
- But `float` wraps at about 1.8 × 10**308. Go past it and you get `inf` — a
  **quietly wrong answer**, not a crash. (Monday's guardrails exist for this.)

In your notes: which of these would break our calculator if a user typed it,
and how would it break?

## PART 2 — WHAT OVERFLOW LOOKS LIKE IN OTHER LANGUAGES (10 min)

Python's big integers are a luxury. Most languages (C, C++, Java) use fixed
width integers — for example, 32 bits, which tops out at 2,147,483,647. One
more, and the number **wraps around** to negative — silently.

Simulate it (no crash, no warning — like a real overflow):

```python
INT_MAX = 2_147_483_647
x = INT_MAX + 1          # in C, this wraps to -2147483648
print(x)                 # Python is fine here — but imagine it wrapped
```

In pairs: if a bank's balance variable wrapped from +2 billion to −2 billion,
which is worse — the crash, or the wrap? Why?

## PART 3 — CASE STUDY: THE PATRIOT MISSILE ROUNDING ERROR (15 min)

Read the case summary I project, then answer in your notes:

**Patriot missile battery, Dhahran, 1991.** The Patriot system tracked time by
counting tenths of a second — but stored it in a fixed-point number that cannot
represent 0.1 exactly. The tiny rounding error (about 0.000000095 seconds per
hour) grew as the battery ran. After 100 hours of continuous operation, the
clock was off by over a third of a second — far enough that the tracking
software looked in the wrong part of the sky. An incoming Scud was missed.
**28 soldiers died.**

Answer in your notes:

1. Was this a crash or a quietly wrong answer?
2. Why did it get worse the longer the system ran?
3. What *guardrail* would have caught it? (Think: reset the clock, check the
   runtime, test with realistic durations.)
4. One lesson you will apply to your own calculator.

## PART 4 — JOURNAL (15 min)

In your calculator lab repo (start with `pwd`):

```bash
pwd
cd ~/compmath-lab
touch journal-0925-$(whoami).md
```

- `whoami` shows your userid, and `$(whoami)` inserts it into the filename
  automatically — so the file is clearly yours in the commit history.
- Open `journal-0925-$(whoami).md` and answer:

  1. Summarize the Patriot missile failure in 3-4 sentences: what went wrong,
     why it grew, what it cost.
  2. What is the *lesson learned*, in one sentence?
  3. **Feed Monday's lab:** what bounds should our calculator enforce? Propose
     at least two — for example, "reject numbers over 10**15" or "warn if a
     Kelvin conversion would go below 0 K." Say what the calculator should do
     when a bound is hit: refuse? warn but proceed? Explain your choice.

## PART 5 — PUSH (last 10 min — routine by now)

```bash
cd ~/compmath-lab
git add journal-0925-$(whoami).md
git commit -m "Day 0925 journal — overflow and boundaries"
git push
```

- **Asked for a username/password?** GitHub username plus Personal Access Token
  (PAT) — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 1 REPL outputs (the big-number demo)
2. your journal file open with your Part 4 answers
3. the successful `git push` confirmation line

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
