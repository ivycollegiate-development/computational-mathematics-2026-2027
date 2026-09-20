# U1 L07 — Reflection: Safe vs Unsafe Arithmetic

**LO:** explain the difference between safe and unsafe programs, and state what "defensive programming" means.

Today is a paper and discussion day — your only terminal work is the journal at
the end. Friday's Calculator v2 lab builds directly on what you decide today.

## PART 1 — OPENING REVIEW: WHAT HAPPENED FRIDAY (10 min)

Last Friday (U1 L06) we learned `try/except`. Reconstruct it together before I
show anything:

- What does `try` do, and what does `except ValueError:` catch?
- Why did we put the `try/except` *inside* a loop instead of around the whole
  program?
- What is the difference between a crash and a quietly wrong answer? Which is
  easier to find, and why?

Write your answers in your notes first; then we go over them as a class.

## PART 2 — SAFE VS UNSAFE PROGRAMS (15 min)

In pairs, sort these behaviors into **safe** and **unsafe** — and be ready to
defend the borderline ones:

- a calculator that crashes when you type a word
- a calculator that asks again when you type a word
- a calculator that divides by zero and prints `inf`
- a calculator that refuses to divide by zero and explains why
- a program that accepts any number, even one bigger than all the money on Earth
- a program that checks the input is in range *before* doing math

Which of these is the program being honest with the user, and which is it just
hiding a problem?

## PART 3 — WHAT IS DEFENSIVE PROGRAMMING? (15 min)

In your notes, answer:

1. What does "defensive programming" mean, in your own words?
2. **Journal question (the big one):** which Python tool is most important for
   security — `try/except`, type conversion, or input validation? Pick ONE and
   defend your choice in 2-3 sentences. There is no single right answer; what
   matters is the reasoning.
3. In pairs, compare the error-handling strategies you used in yesterday's lab.
   Did your partner fix `get_number()` the same way you did? What was different?

## PART 4 — THE IMPOSSIBLE QUESTION (10 min)

Class discussion: *is it possible to make a program completely crash-proof?*

- Can you list every input a user might type? (Remember Part 2 of L5.)
- If you cannot list every input, what should the program do with the ones you
  did not expect?
- Where does the line sit between "the program is safe" and "the program is
  less unsafe"?

Write one sentence in your notes that you would be willing to say out loud.
Several of you will be asked to read yours.

## PART 5 — JOURNAL (last 15 min)

In your calculator lab repo (start with `pwd` — know where you are):

```bash
pwd
cd ~/compmath-lab
touch journal-0921-$(whoami).md
```

- `whoami` shows your userid, and `$(whoami)` inserts it into the filename
  automatically — so the file is clearly yours in the commit history.
- Open `journal-0921-$(whoami).md` and answer in 3-5 sentences:

  - Which Python tool (`try/except`, type conversion, input validation) is most
    important for security, and why? (Your Part 3 answer, tightened.)
  - Is a completely crash-proof program possible? What did the class discussion
    change about your first answer?

## PART 6 — PUSH (last 10 min — same loop as always)

Before you push, preview the check in your own terminal:

```bash
cd ~/compmath-lab
python3 self_check.py
```

This is the *same* check that GitHub runs on your push, run locally — you get
the exact score ("N of 6 checks passing") and the full report in your terminal
*before* anything is committed. If something is missing, the output tells you
what and how to fix it; fix, run it again, and only push when you are happy
with the score. Self-checking before you push is what professional developers
do: find your own errors before anyone else sees them.

Then push as usual:

```bash
cd ~/compmath-lab
git config pull.rebase false
git pull
git add journal-0921-$(whoami).md
git commit -m "Day 0921 journal — defensive programming"
git push
```

- The `git config pull.rebase false` line tells git how to combine work when
  the repo on GitHub has changes you do not have yet. Run it once; it is not
  an error if you already ran it.
- `git pull` downloads anything new from GitHub before you push. If your push
  is ever rejected with a message like "remote contains work you do not
  have", run `git pull` and then `git push` again.
- **If the `cd` step says "No such file or directory"** you never cloned (or
  the clone is gone — new workspace, fresh account). Rebuild it, then run the
  block above from the start:

```bash
git clone https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-$(whoami)_student.git compmath-lab
cd ~/compmath-lab
```

- And if git says "not a git repository", you are in the wrong folder — run
  `pwd`, and `cd ~/compmath-lab` before doing any git work.
- **Asked for a username/password?** GitHub username plus Personal Access Token
  (PAT) — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your journal file open with your Part 3 and Part 5 answers
2. the successful `git push` confirmation line

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
