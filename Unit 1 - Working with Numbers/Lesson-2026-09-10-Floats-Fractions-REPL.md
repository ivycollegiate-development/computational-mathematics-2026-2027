# Sep 10 — Fractions & Floating-Point Precision in the REPL

**Unit 1 · Week 1 · Thursday (Reflection + REPL day)**

Everything today happens in your VS Code workspace. No paper worksheet.

## Part 1: Housekeeping — out with the old repo (first 15 minutes)

Yesterday some of you cloned the course repo from my personal GitHub account. That copy is being retired — the real home for course materials is now the school organization account. Today you'll clean up using the terminal, then clone fresh from the right place.

**⚠️ Safety first: `rm -rf` is permanent.** There is no trash can, no undo, no recycle bin. A typo in the path can delete the wrong thing — forever. The survival habit: **always run `pwd` immediately before any `rm -rf`** so you know exactly which directory you're standing in.

1. Log in at https://vscode.ivycollegiate.org/ — school Google account
2. Open a terminal, then orient yourself:
   - `pwd` — where am I? You want your home directory. If not: `cd ~`
   - `ls` — look at what's here. You should see the old course folder, `computational-mathematics-2026-2027`
3. Check what you're about to delete — look before you leap:
   - `ls computational-mathematics-2026-2027` — confirm it's the course repo
   - `cd computational-mathematics-2026-2027 && git remote -v` — this shows which URL you cloned from. If it says `nascar-paul/...`, it's the old copy. Then `cd ~` to go back home.
4. Delete it — run `pwd` one more time to confirm you're in `~`, then:
   **rm -rf computational-mathematics-2026-2027**
5. Verify it's gone: `ls` — the folder should no longer appear
6. Clone the fresh copy from the school org:
   **git clone https://github.com/ivycollegiate-development/computational-mathematics-2026-2027.git**
7. Verify what you got:
   - `ls` — the folder is back
   - `cd computational-mathematics-2026-2027 && git remote -v` — the URL should now say `ivycollegiate-development/...`
   - `git log --oneline -3` — you should see today's lesson commit at the top
   - `ls "Unit 1 - Working with Numbers"` — you should see `Lesson-2026-09-10-Floats-Fractions-REPL.md` — that's today's lesson, and you're looking at it
8. Start the REPL: type `python3`

## Part 2: The floating-point surprise (~10 minutes)

Yesterday every calculation came out exact. Today, watch this one:

```
>>> 0.1 + 0.2
>>> 0.1 + 0.2 == 0.3
>>> 1 / 3
>>> (1 / 3) * 3
>>> (1 / 3) * 3 == 1.0
```

**Predict each line first, then run it.** Write down what you expected vs what you got.

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

```
>>> from fractions import Fraction
>>> Fraction(1, 3)
>>> Fraction(1, 3) * 3
>>> Fraction(0.1) + Fraction(0.2)
>>> float(Fraction(0.1) + Fraction(0.2))
>>> Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10)
```

Notice:
- `Fraction(1,3) * 3` gives exactly `1` — no error
- `Fraction(0.1) + Fraction(0.2)` still shows a long number — because `Fraction(0.1)` converts the *already-corrupted float*. But `Fraction(1,10) + Fraction(2,10)` is exactly `3/10`
- The rule: build Fractions from **integer ratios**, not from floats

## Part 5: Practical exercise — predict, then run (~10 minutes)

Before each line, write down what you think it prints. Then run it.

1. `0.1 * 3 == 0.3` — float version. True or false?
2. `Fraction(1,10) * 3 == Fraction(3,10)` — exact version. True or false?
3. `1 / 49 * 49` — does multiplying back give exactly 1?
4. `Fraction(1,49) * 49` — and the exact version?
5. `sum([0.1] * 10)` vs `sum([Fraction(1,10)] * 10)` — add ten tenths both ways. Which one gives 1?

## Part 6: Journal (last 5 minutes)

Create `journal-0910.md` in your home directory. Write 2–3 sentences:
- In your own words: why can't a computer store 0.1 exactly using floats?
- Name one situation from today's discussion where float rounding could cause real harm.

## Turn in — SCREENSHOT

ONE screenshot of your terminal showing, in order:
`pwd` (taken right before your `rm -rf`), the repo `ls` before and after deletion, the `git remote -v` output from your fresh clone (showing `ivycollegiate-development/...`), your Part 2 float-surprise outputs, your Part 4 Fraction outputs, and your Part 5 predict answers.
Submit it to the Classroom assignment before 11:59 PM. Keep your terminal open — I'll spot-check live screens.
