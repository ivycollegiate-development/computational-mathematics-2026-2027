# U2 L01 — Unit 1 Assessment and Reflection

**LO:** demonstrate mastery of Unit 1: types, arithmetic, input validation, error handling, and the security lens.

Today is a **paper assessment day**. The written part is closed-computer — no
terminals, no notes, no neighbors. Everything on this paper is something we
built or debugged together in Unit 1. After the assessment, you reflect in
your journal and push it.

## PART 1 — BEFORE YOU START (5 min)

Put everything away except a pen or pencil. On the cover of your paper, write:

- your name
- one thing from Unit 1 you feel confident about
- one thing you hope is NOT on the test (be honest — it won't change the test,
  but it tells me where to spend review time next unit)

Then close your notes. Deep breath. You have seen every problem type below.

## PART 2 — WRITTEN ASSESSMENT (35 min, no computers)

The exam is a standalone paper:
[`Unit 1 - Working with Numbers/Assessments/Unit-1-Assessment.md`](https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%201%20-%20Working%20with%20Numbers/Assessments/Unit-1-Assessment.md)

**Print it double-sided before class.** 50 points, 35 minutes, pen and paper.
Structure:

| Section | Points | Covers |
|---|---|---|
| A — Short Response | 20 | 10 questions: `/` vs `//`, `input()` conversion, `ValueError`, quiet vs crash, truth table, `Fraction` vs `float`, modulo, precision order, `get_number()`, security lens |
| B — Code Reading | 10 | Problem 11 (the price loop), Problem 12 (the broken `f_to_c`) |
| C — Boundaries | 10 | −273.15 °C / 0 K guard, the `10**15` ceiling and why it exists |
| D — Write Code | 10 | `get_int(prompt)` — validate, re-ask, refuse out of range |

Do not deviate from the printed paper. The coversheet on the front carries your
name, your confident item, and the "one thing I hope is NOT on the test" note
from Part 1.

## PART 3 — HAND BACK THE COMPUTERS: GRADE RELEASE WALKTHROUGH (10 min)

We go over the answer key together, problem by problem. As we do:

- Mark each problem **got it** or **not yet** — no points yet, just honesty.
- For every **not yet**, write one sentence: *what specifically confused me?*
  "I didn't study" is not an answer. "I mixed up `//` and `/`" is.

These sentences are raw material for your journal in Part 4.

## PART 4 — JOURNAL (last 10 min)

Open your lab repo and create today's journal:

```bash
pwd
cd ~/compmath-lab
touch journal-u2l01.md
```

Answer in the file, 3-5 sentences each:

- Which assessment problem was hardest, and what does that tell you about
  what to review before the next unit builds on it?
- Unit 2 is about **visualizing data**. Where in Unit 1 did we already touch
  data (even a little)?
- One prediction: what could go *visually* wrong with data that goes wrong
  numerically?

## PART 5 — PUSH (last 5 min — same loop, now routine)

```bash
cd ~/compmath-lab
git add journal-u2l01.md
git commit -m "U2 L01 assessment reflection journal"
git push
```

- **Asked for a username/password?** GitHub username + Personal Access Token
  (PAT) — never your GitHub password.
- **Success?** You should see a push confirmation line. Edit → add → commit →
  push. That loop is muscle memory now.

## TURN IN — PHOTO + SCREENSHOT (due 11:59 PM tonight)

1. **Photo of your paper assessment** (all sections, legible, right side up) —
   take it with your phone right after Part 2.
2. **One screenshot** showing, in order:
   - your journal file open with your Part 4 answers
   - the successful `git push`

Submit both to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

**Next:** U2 L02 — Bridge: From Numbers to Data (https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%202%20-%20Visualizing%20Data/U2-L02-Bridge-From-Numbers-To-Data.md)
