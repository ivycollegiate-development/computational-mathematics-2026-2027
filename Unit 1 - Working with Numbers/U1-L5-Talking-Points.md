# U1 L5 — Teacher Talking Points (Sep 17, Thu — PAPER DAY)

Teacher-facing memo only. Not a student handout. Keep it on your laptop or a printout.

---

## 1. OPEN — WHERE WE WERE YESTERDAY (L4, Wed Sep 16)

Recap to deliver in your own words, ~3 minutes. Ground rules: ask, don't lecture —
let them supply the answers.

**What they did yesterday:**

- Met `input()` for the first time and discovered the trap: **`input()` always hands
  you a string**, even when the user types a number. That is why `int(input(...))`
  exists.
- Ran the age calculator and deliberately fed it `banana`. It died with a **ValueError
  traceback** — and you told them to *leave it broken on purpose*. "You fix it on
  Friday" was the promise. Today you collect on the framing, not the fix.
- Saw three REPL surprises: `int("  42  ")` works (spaces around the number are
  stripped), `int("4 2")` crashes (space in the middle is fatal), and
  `float("1e3")` gives `1000.0` (a string can be a perfectly valid *float* without
  looking like an integer).
- **First-ever git push.** Every student created a PAT, pushed
  `journal-0916-*.md` and `repl-notes-0916-*.md` to their own repo, and submitted a
  screenshot of the whole loop: `git pull` → REPL outputs → two age-calculator runs
  (one good, one `banana` crash) → successful push.

**Worth asking out loud:**

- "Who got their push working on the first try? Who needed a hand?" — names the
  struggle as normal, and sets up that Monday's graded lab is the same loop done
  for real.
- "What was the error called when `banana` killed the calculator?" — they should
  say **ValueError** without prompting. If they can't, write it on the board; it is
  the exact exception Friday's code catches.
- "Whose fault was the crash — the user or the program?" — this IS Part 1 of today's
  lesson. Use the question as the bridge into the lesson proper, not as a detour.

**Watch for:** anyone whose push still failed last night (403 / repository not
found). Catch them in the first five minutes or during journal time — Friday and
Monday both end in pushes, and they cannot afford to carry a broken PAT forward.

---

## 2. TODAY — L5, THE WHY (what the lesson is actually for)

One sentence of framing before Part 1: *yesterday you saw the program die; today we
decide whose fault that is and what a program owes its user.*

- **The rule the whole unit turns on:** never trust user input. Validate before you
  compute. Everything after today is just implementations of that rule.
- Two outcomes of any check: **reject it** or **repair it**. Say both words; they
  reappear Friday.
- The Therac-25 story is the gravity of the lesson — real machines, real deaths,
  and the failure was *unvalidated operator input plus a software race*. Do not
  rush it. The flowchart they turn in (Part 5) is the concrete artifact; the case
  study is what makes "validate before you compute" feel like an obligation rather
  than a style tip.
- Journal prompt: `journal-0917-<yourname>.md` — same unique-name convention as
  yesterday. "Which input is most dangerous" should surface *quietly wrong answers*
  over loud crashes; steer the discussion there if it doesn't (a crash is
  information; a wrong number is silence).

---

## 3. AHEAD — WHAT FRIDAY AND MONDAY ARE (say this at the end of class)

Deliver as a two-beat promise, ~30 seconds:

1. **Friday (L6): the fix.** We go back to the same age calculator, feed it
   `banana` again, and make it *survive* — with `try/except`. The exact crash from
   yesterday becomes the exact demo. The `ValueError` on the board today is the
   thing Friday's `except ValueError:` catches. Reject-or-repair becomes code:
   `except` rejects and re-asks, `else` proceeds when the repair worked.
2. **Monday (L7): the graded lab.** Calculator v1 — Safe Arithmetic. Same loop as
   yesterday's push rehearsal (edit → add → commit → push) but for a grade. Today's
   flowchart is, literally, the control flow of Monday's program: ask → convert →
   worked? → use it / re-ask, repeat until `q`.

Close with: *"Friday we fix the banana. Monday you prove you can keep it fixed."*

---

## 4. LOGISTICS REMINDERS (your checklist, not theirs)

- Paper day: no student computers today — the journal is the only exception, run
  it in the last 5 minutes if workspace access is smooth, otherwise collect on
  paper and have them type it Friday.
- Both Classroom sections (P1, P2) have the L5 assignment staged as DRAFT, due
  tonight 23:59 — publish before class.
- The Therac-25 summary is delivered by you in pairs — no printed handout exists.
- Collect the flowcharts at the door (Part 5 is the turn-in); they are your
  diagnostic for Monday — a student whose flowchart has no loop-back arrow will
  not survive the calculator lab's re-ask loop without help.
