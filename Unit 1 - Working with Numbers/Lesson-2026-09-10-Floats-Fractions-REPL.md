# Sep 10 — Fractions & Floating-Point Precision in the REPL

**Unit 1 · Week 1 · Thursday (Reflection + REPL day)**

Everything today happens in your VS Code workspace. No paper worksheet.

## Part 1: Housekeeping — out with the old repo (first 15 minutes)

Yesterday, all of you cloned the course repo. Today, I want you all to learn how to delete and recreate it — with `rm`, the most dangerous command in the terminal.

Everything below is also on GitHub, with clickable links and commands: https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%201%20-%20Working%20with%20Numbers/Lesson-2026-09-10-Floats-Fractions-REPL.md
Open that page in a browser so you can click the repo link instead of typing it. (You can also start from the README at https://github.com/ivycollegiate-development/computational-mathematics-2026-2027 — today's lesson is linked there.)

**⚠️ Safety first: `rm -rf` is permanent.** There is no trash can, no undo, no recycle bin. A typo in the path can delete the wrong thing — forever. The survival habit: **always run `pwd` immediately before any `rm -rf`** so you know exactly which directory you're standing in.

### Step-by-step (type each command exactly as shown)

1. **Log in** at https://vscode.ivycollegiate.org/ — use your school Google account.
2. **Open a terminal.** In VS Code, click `Terminal` in the top menu bar, then `New Terminal` (or press `` Ctrl+` ``). A terminal panel opens at the bottom of the window.
3. **Orient yourself — find out where you are.** Type this, then press Enter:
   **pwd**
   This prints your current directory ("print working directory"). You want it to end in something like `/home/yourname` — that's your home directory. If it does NOT, type:
   **cd ~**
   (That means "change directory to my home." The `~` tilde is shorthand for home.)
4. **Look at what's here.** Type:
   **ls**
   ("list" — shows the files and folders in the current directory.) You should see the old course folder, `computational-mathematics-2026-2027`, among other things.
5. **Verify the folder before deleting it.** First peek inside:
   **ls computational-mathematics-2026-2027**
   You should see course files and folders (README.md, Syllabus.md, Unit folders, lesson files). Then check which remote it was cloned from:
   **cd computational-mathematics-2026-2027**
   **git remote -v**
   This prints the URL the repo was cloned from. Verify you can see a GitHub URL ending in `computational-mathematics-2026-2027.git`. Now go back home:
   **cd ~**
   Run `pwd` again if you want to confirm you're back in `/home/yourname`.
6. **Delete the old copy.** First, run `pwd` one more time — confirm it says your home directory. This is the habit that will save you someday. Then type:
   **rm -rf computational-mathematics-2026-2027**
   (`rm` = remove, `-r` = recursive / everything inside, `-f` = force / no confirmation prompts. It completes silently — silence is success.)
7. **Verify it's gone.** Type:
   **ls**
   The `computational-mathematics-2026-2027` folder should no longer appear.
8. **Clone the fresh copy from the school org.** Type this whole line on one line, then Enter:
   **git clone https://github.com/ivycollegiate-development/computational-mathematics-2026-2027.git**
   You'll see progress text ending with `done.` — that means the download finished. If instead you see `fatal:` or `Could not resolve host`, retype the command slowly and exactly.
9. **Verify what you got — four checks:**
   - **ls** — the folder `computational-mathematics-2026-2027` is back
   - **cd computational-mathematics-2026-2027**
   - **git remote -v** — the URL should now say `ivycollegiate-development/computational-mathematics-2026-2027.git`
   - **git log --oneline -3** — shows the last 3 commits, one line each; the top line is today's lesson commit
   - **ls "Unit 1 - Working with Numbers"** — you should see `Lesson-2026-09-10-Floats-Fractions-REPL.md` — that's today's lesson, and you're looking at it
10. **Start the REPL.** Type:
    **python3**
    You'll see a `>>>` prompt — that's Python waiting for you.

## Part 2: The floating-point surprise (~10 minutes)

Yesterday every calculation came out exact. Today, watch this one.

In the REPL (where you see the `>>>` prompt), type each line below, press Enter, and **look at the output before moving on**. Before you press Enter on each line, say or write down what you think it will print:

```
>>> 0.1 + 0.2
>>> 0.1 + 0.2 == 0.3
>>> 1 / 3
>>> (1 / 3) * 3
>>> (1 / 3) * 3 == 1.0
```

Line-by-line guidance:
- Line 1: a plain addition. You expect `0.3`. Run it and look very carefully at what actually appears.
- Line 2: `==` asks "are these two things equal?" and prints `True` or `False`. Which do you expect? Which do you get?
- Line 3: `1 / 3` in Python 3 does true division. It prints many digits — and those digits stop at 16. Why there?
- Line 4: multiply the previous result back by 3. Mathematically `(1/3)*3 = 1` exactly. Does the computer agree?
- Line 5: ask the computer directly. The answer may surprise you.

**Write down what you expected vs what you got for lines 2 and 5.** You'll need it for the journal.

### Why does this happen?

Computers store decimal numbers in **binary** (base 2). Some decimals that are short and tidy in base 10 — like 0.1 — are *infinite, repeating* fractions in base 2. Python's floats store only ~16 significant digits, so a tiny error creeps in and stays.

It's not a Python bug. Every language that uses IEEE 754 floats does this.

## Part 3: Discussion — when does this matter? (~10 minutes)

Talk through these with the class:

- **Banking:** if a bank stores $0.10 as a float and loses a rounding error on millions of transactions a day, where does the money go? (Real answer: banks use integers of cents or exact decimal types.)
- **Missile guidance:** the Patriot missile failure in 1991 — a tiny time-keeping rounding error accumulated over 100 hours of operation. The intercept missed by ~0.34 seconds ≈ 687 meters.
- **Therac-25:** a radiation therapy machine where software bugs — including numeric and race-condition errors — contributed to patients receiving massive overdoses.

The pattern: **small errors + accumulation = real consequences.** A mathematician says "close enough." An engineer has to ask "how close, and what breaks when it isn't?"

## Part 4: The fix — Python's Fraction class (~10 minutes)

`fractions.Fraction` stores numbers as exact ratios of integers. No rounding, ever.

Still in the REPL, type these one at a time:

```
>>> from fractions import Fraction
>>> Fraction(1, 3)
>>> Fraction(1, 3) * 3
>>> Fraction(0.1) + Fraction(0.2)
>>> float(Fraction(0.1) + Fraction(0.2))
>>> Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10)
```

What each line means and what to notice:
- Line 1: import the Fraction class from Python's standard `fractions` library. After this, `Fraction(...)` is available.
- Line 2: `Fraction(1, 3)` means the exact value one-third. Python prints it back as `Fraction(1, 3)`.
- Line 3: one-third times 3 gives exactly `1` — no error, no `0.999...`.
- Line 4: this still shows a long number! That's the subtle trap: `Fraction(0.1)` converts the *already-corrupted float* 0.1, so the error comes along for the ride.
- Line 5: `float(...)` converts the Fraction back to a float for display.
- Line 6: building from integer ratios (`1, 10` and `2, 10`) gives an exact `3/10`, and the comparison is `True`.

**The rule: build Fractions from integer ratios, not from floats.**

## Part 5: Practical exercise — predict, then run (~10 minutes)

Before each line, write down what you think it prints. Then run it in the REPL.

1. **0.1 * 3 == 0.3** — float version. True or false?
2. **Fraction(1,10) * 3 == Fraction(3,10)** — exact version. True or false?
3. **1 / 49 * 49** — does multiplying back give exactly 1? (If not, where did the digits go wrong?)
4. **Fraction(1,49) * 49** — and the exact version?
5. **sum([0.1] * 10)** then **sum([Fraction(1,10)] * 10)** — add ten tenths both ways. Which one gives exactly 1?

Hint for line 5: `[0.1] * 10` makes a list of ten 0.1s; `sum(...)` adds them up. Try both lines and compare the outputs.

## Part 6: Journal (last 5 minutes)

Leave the REPL: type **exit()** and press Enter. Then create a journal file using VS Code: in the file explorer (left sidebar), make sure you're in your home directory, click the **New File** icon, name it:
**journal-0910.md**
Or from the terminal: **nano journal-0910.md** (type your entry, `Ctrl+O` Enter to save, `Ctrl+X` to exit).

Write 2–3 sentences answering:
- In your own words: why can't a computer store 0.1 exactly using floats?
- Name one situation from today's discussion where float rounding could cause real harm.

## Turn in — SCREENSHOT

ONE screenshot of your terminal showing, in order:
1. `pwd` — taken right before your `rm -rf` (proving you were in `~` when you deleted)
2. the repo `ls` before deletion
3. the `ls` after deletion (folder gone)
4. the `git remote -v` output from your fresh clone (showing `ivycollegiate-development/...`)
5. your Part 2 float-surprise outputs (all 5 lines with results)
6. your Part 4 Fraction outputs (all 6 lines with results)
7. your Part 5 predict answers (True/False for each)

To take the screenshot on the VPS desktop: press `PrtSc` or use the screenshot tool in the taskbar. Then submit it to the Classroom assignment before **11:59 PM**. Keep your terminal open — I'll spot-check live screens.
