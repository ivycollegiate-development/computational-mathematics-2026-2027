# U1 L5 — Reflection: Trust Nothing the User Types

**LO:** explain why unchecked user input is dangerous, and lay out the validation rules a program needs.

Today starts on paper and ends in the terminal — you will need your workspace for
Parts 3 and 4.

## PART 1 — OPENING REVIEW: WHAT HAPPENED YESTERDAY (10 min)

Before anything new, let's reconstruct Wednesday's lesson (U1 L4 — User Input).

Answer these together before I show any code:

- What does `input()` always hand your program, no matter what the user types?
- Why did `age = int(input("Age: "))` need the `int()` around it?
- What exactly happened when we typed `banana` into the age calculator? What was
  the error called?
- We typed `int("  42  ")` and it worked, but `int("4 2")` crashed. What was the
  difference?

Write your answers in your notes first; then we go over them as a class. By the end
of this part you should be able to say in one sentence: **why does `banana` break
every program we have written so far?**

## PART 2 — "WHAT ELSE COULD GO WRONG?" (15 min)

In small groups, list every bad input you can think of for a program that asks for
a number. Push past the obvious first three:

- empty input (just pressing Enter)
- spaces, letters, symbols, punctuation
- a number that is absurdly large
- a number that is negative, or absurdly small
- units that don't match what the program expects
- two numbers where the program wants one

Each group posts its top three on the board, and we sort them into "crashes" versus
"quietly wrong answers."

## PART 3 — REVIEW: THE FUNCTIONS WE KNOW (15 min)

Open your workspace. First command, always:

```bash
pwd
```

(Verify where you are before you type anything else.)

Then start the Python REPL:

```bash
python3
```

For each function below, first answer in your notes: *what does it do, and what
does it give back?* Then test it in the REPL and check your answer:

- `print()`
- `input()`
- `int()`
- `float()`
- `str()`
- `//` and `/` and `%` — which is which, and what does each return?
- `Fraction()` — from where do we import it, and why is it exact?

Try to surprise yourself: what does `int(input())` do if you type `3.7`? What about
`float(input())` with `3.7`? Every answer you get here belongs in your notes — the
surprises are tomorrow's subject.

## PART 4 — REVIEW: THE TERMINAL (10 min)

Exit the REPL (`exit()` or Ctrl-D). In your notes, answer: *what does each of these
commands do, and where are you when you type it?* Then run each one and check.

- `pwd`
- `cd ~`
- `cd ~/computational-mathematics-2026-2027`
- `ls`
- `git pull`

Each student explains one command to the class — what it stands for, what it does,
what happens if you skip it. When we get to `git pull`, run it for real so
tomorrow's lesson is already on your machine.

## PART 5 — JOURNAL (last 5 min)

Create the file first, in the right place — the same folder you will push from.
In the terminal (start with `pwd` — know where you are):

```bash
pwd
cd ~
cd compmath-u1-push-test
whoami
mkdir -p $(whoami)
touch $(whoami)/journal-0917.md
```

- `whoami` shows your userid, and `$(whoami)` inserts the same thing automatically
  into a command — every student gets their **own folder**, so nobody's journal
  collides with anyone else's.
- `mkdir -p` creates the folder (`-p` = no error if it already exists).
- `touch` creates an empty file inside it. Open it in VS Code's file list on the
  left, and answer in 2-3 sentences:

- Which input from PART 2 is the most dangerous, and why?
- What is the one rule you will apply to every program you write from here on?

## PART 6 — PUSH (last 10 min — same loop as Wednesday, now routine)

Your journal is already in `compmath-u1-push-test`, so push it. Type each command exactly:

```bash
cd ~/compmath-u1-push-test
git remote add origin https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-$(whoami)_student.git
cp ~/compmath-u1-push-test/$(whoami)/journal-0917.md .
cp ~/repl-notes-0917*.md . 2>/dev/null
git add .
git commit -m "Day 0917 journal"
git branch -M main
git pull
git push -u origin main
```

- **Asked for a username/password?** Use your GitHub username plus your Personal
  Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see the `Branch 'main' up to date` or push confirmation
  line. Same loop as Wednesday: edit → add → commit → push.
- **Behind?** If `git push` complains, run `git pull` first, then push again —
  that order (pull, then push) prevents almost every push error you will ever see.

**TURN IN — SCREENSHOT (due 11:59 PM tonight):** one screenshot of your terminal
showing your Part 3/4 REPL-and-terminal outputs and the successful `git push`.
Submit it to this assignment on Google Classroom. Mac: `Cmd+Shift+4` ·
Windows: `Win+Shift+S`.
