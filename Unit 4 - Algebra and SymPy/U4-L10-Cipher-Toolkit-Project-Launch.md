# U4 L10 — Cipher Toolkit Project Launch

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (project launch, 45 minutes)
**LO:** 4.1, 4.2, 4.3 — combine symbolic and modular reasoning into one working
deliverable; defend design choices in writing

---

## TODAY'S PURPOSE

You have been building pieces since Jan 6. `symkit.py` does symbolic algebra,
`modkit.py` does modular arithmetic, `integrity.py` does hashing. None of them
are a project. Today they become one program that someone else could run, and
you defend why it is built the way it is.

**Due: February 15, 11:59 PM.** The demo is Feb 16. You get the
**whole CNY break as build time** (Feb 3–14) — that is deliberate. Bring a
laptop, work in short sessions, and push. The in-class build days below are
*setup and structure*, not the only time you work on it.

## PART 1 — WHAT YOU ARE BUILDING (10 min)

A **Cipher Toolkit**: a command-line program that encrypts and decrypts, using
more than one cipher, and proves its own output is intact.

Required components, all of which you already have pieces of:

| # | Component | Comes from | Graded on |
|---|-----------|-----------|-----------|
| 1 | Shift cipher, encrypt + decrypt | `modkit.shift_cipher` (L05) | correctness |
| 2 | Affine cipher, encrypt + decrypt | `modkit.affine_cipher` (L05) | correctness, error handling |
| 3 | Brute-force solver for unknown `k` | new — you write it | does it distinguish a guess from a proof? |
| 4 | SHA-256 manifest of your source files | `integrity.py` (L07) | does tamper-detection actually run? |
| 5 | A written defense of your design | new — 1 page | reasoning quality |

**The unifying idea:** every cipher here is a bijection on a finite set, and the
only reason you can invert one is that you know the key. Your toolkit's job is
to be honest about which of its claims are proofs and which are guesses.

## PART 2 — DESIGN BEFORE CODE (12 min)

Paper first. No laptop yet. Answer these in writing; you will paste this
section into your README.

1. Your toolkit takes `--cipher {shift,affine,brute}`. Which of your three
   modes is a **proof** of correctness and which is an **exhaustive search**?
   What is the difference, in one sentence each?
2. Affine decryption calls `pow(a, -1, n)`, which raises `ValueError` when
   `gcd(a, n) != 1`. Write down what an attacker learns from that exception
   message. Is your error message too chatty?
3. Your brute-force solver tries all 26 shifts and reports which one produces
   readable English. A wrong key can also produce readable text — like the word
   `ORIGIN` under ROT13. What makes your solver's output a **candidate** rather
   than a **conclusion**?
4. Pick ONE of these and justify it in a sentence: *I will not implement
  frequency analysis, because …* or *I will implement frequency analysis, and
  it will be wrong on short inputs because …*

Write your 1-page defense now. Rough is fine. You will revise it at the end.

## PART 3 — SET UP THE PROJECT (15 min)

Create your repo today so the build is not all crammed into February.

```
compmath-u4-cipher-toolkit
├── README.md            # your Part 2 defense, revised
├── toolkit.py           # the main program
├── symkit.py            # from L02/L04
├── modkit.py            # from L05
├── integrity.py         # from L07
├── test_toolkit.py      # the test driver
└── manifest.sha256      # generated, committed
```

- ☐  Repo created, **public**, default branch `main`
- ☐  `symkit.py`, `modkit.py`, `integrity.py` copied in and importing cleanly
- ☐  `python3 toolkit.py --cipher shift --key 7 --text "hello"` round-trips
- ☐  `python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"` round-trips
- ☐  `python3 toolkit.py --cipher brute --text <25 letters>` finds something
      (try `khear` — 4 letters, a shift of 6)
- ☐  `python3 test_toolkit.py` prints `all tests passed`
- ☐  `manifest.sha256` generated and committed
- ☐  README has your Part 2 defense with the four questions answered

**No pip installs.** SymPy and the standard library only. If something is
missing, tell me — do not install it yourself.

## PART 4 — TEST THE THINGS THAT WILL BREAK (5 min)

Write down, with the actual output, what happens when:

- `a = 4, n = 26` (not invertible)
- `n = 1` (degenerate)
- empty input
- input with no letters at all
- a shift key of `0` and of `26`

- ☐  Each case either behaves sanely or raises a **clear** error
- ☐  No traceback leaks to the user
- ☐  Your error messages say what is wrong, not just that something broke

## PART 5 — WHAT "DONE" MEANS (3 min)

You are done when a classmate who has never seen your code can clone the repo,
run one command, and get correct output on all three ciphers. That is the whole
standard. Code that only works on your laptop is not done.

**Milestones — put these in your tracker today:**

| When | What |
|------|------|
| Jan 22 | Repo live, three ciphers round-trip, defense drafted |
| Jan 28 | Brute-force solver working, test driver green |
| Jan 29 | Edge cases handled, manifest generated, defense revised |
| **CNY Feb 3–14** | **Build days. Laptop. Short sessions, push often.** |
| Feb 15 | **Everything finished.** Final checks, final push |
| Feb 16 | Demo. Unit 4 complete |

**Build over the break — how.** Ten days is a lot, and it will evaporate if
you wait for a free afternoon that never comes. Work in 30-minute blocks. One
component per session. Commit at the end of every session so you can always
recover. If you finish early, the *best* use of the time is the edge-case
table and the defense — not new features.

**Next:** L11 — in-class build day and final checks. Then CNY,
then the Feb 16 demo. After the demo the unit is done and U5 starts Feb 17.

## TURN IN — Cipher Toolkit Launch Checklist

1. Public repo, default branch `main`, linked in Classroom
2. All three cipher modes round-trip correctly
3. `test_toolkit.py` prints `all tests passed` in a **fresh clone**
4. `manifest.sha256` committed, and you can demonstrate that editing one
   character of `toolkit.py` makes verification fail
5. The five edge cases from Part 4, each with its real output
6. README with your four-part defense, revised from Part 2
7. Tracker shows the five milestones with dates

## 🇹🇼 TAIWAN CONTEXT

The affine cipher's `gcd(a, 26) != 1` failure is not a curiosity — it is the
same structure as the weaknesses in hand-rolled ciphers used by small orgs
before TLS was affordable, and the same class of bug (bad key selection,
unguarded math) that produced the ROC cases the national CERT has written up.
A cipher that throws an exception on `a=4` is honest. One that silently
produces garbage is the dangerous one.
