# U1 L13 — Worksheet: Calculator Polish and Partner Showcase

Names: ___________________________  Partner: ___________________________  Date: ____

You already did the hard part. Your calculator handles add, subtract, multiply and divide, and it has a menu a user can actually drive. This sheet is the written half of U1 L13: your edge cases, your one fix, and your showcase.

Most of what you find will be small. That is the honest truth about code at this stage — a working calculator with a couple of known weak spots, not a disaster. This is a careful look around your own work, not an exam.

## Part 0 — SETUP

Go get your folder and pull today's changes.

```bash
cd ~/compmath-lab
git config pull.rebase false
git pull
```

Never cloned? Use your own repo instead.

```bash
git clone https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-$(whoami)_student.git ~/compmath-lab
cd ~/compmath-lab
```

☐  My terminal is in `~/compmath-lab` and `git pull` finished with no red text.

## Part 1 — GENERATE YOUR EDGE CASES

You get your own randomized set of unusual inputs, seeded from your seat number. Nobody knows your cases in advance, and yours will not match anyone else's.

```bash
python3 gen_probes.py <your seat number>
```

Replace `<your seat number>` with the number you were given — for example:

```bash
python3 gen_probes.py 7
```

This writes `edge_case_probes.py` with four groups:

| Group | What it is checking |
|---|---|
| `WRONG_TYPE` | input that is not a number at all |
| `HUGE` | numbers too big or too small for normal math |
| `BOUNDARY` | values right at the edge of a range |
| `DIV_ZERO` | dividing by zero, or by something that rounds to zero |

- `edge_case_probes.py` is already in your `.gitignore`. Do not commit it and do not share it. That is intentional — the cases are yours to work through.
- If you lose it, run `gen_probes.py` again with the same seat number and you get the exact same set back.

☐  `edge_case_probes.py` exists in my editor, and I understand I will not commit it.

## Part 2 — WORK THE CASES

Pick any three cases — spread them across the four groups rather than doing all three from one. Run your calculator and type the case in.

For each one write down all three of these: **the input | what actually happened | bug, or correct behavior?**

That third column has two valid answers:

- **bug** — it crashed, gave a wrong answer, or behaved confusingly.
- **correct behavior** — it handled the input properly. Write it down. That is a real finding, not a dud.

Two examples from the starter code:

- `divide(1, 0)` → `ZeroDivisionError`, the program stops. **That is a bug.**
- `get_number()` on `4` → returns `4.0` and moves on. **That is correct behavior**, and it is worth noting that it works.

You are looking for **one genuine bug**, and one is a complete result. Work three cases, name the one bug you will fix, and stop hunting — finding four is not better than finding one.

| # | Group | The input I tried | What actually happened | Bug, or correct behavior? |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

☐  I worked three cases, spread across the four groups.
☐  I have one genuine bug written down.
☐  I noted at least one case that behaved correctly.

## Part 3 — FIX WHAT YOU FOUND

Fix the one bug you named in Part 2, properly. One fix, done well and proven, is the whole assignment — you have to show it working in Part 4, and that matters more than a longer list of problems you did not have time to address.

Open `calculator.py`. You will see two functions with `FIX ME` comments: `get_number()` and `divide()`. Put your code where the `FIX ME` says, and add a comment saying what you changed and why.

| Question | My answer |
|---|---|
| The one bug I chose to fix |  |
| Why this one over the others |  |
| Which function — `get_number()` or `divide()` |  |
| The test run before my fix |  |
| The test run after my fix |  |
| The case from Part 2 I re-ran, and what it does now |  |

Verify the fix:

```bash
python3 test_calculator.py
```

The starter ships with `1 of 4 passing` — one test already passes, and the other three are the bugs you may find. **Your goal is 4 of 4.** You are fixing one today, so expect 2 of 4, and that is a real result — say in your showcase what is still outstanding.

If you are not done with everything: stop here anyway. A working calculator with one fixed bug is a complete lesson. Push what you have and move to Part 4.

## Part 4 — PARTNER SHOWCASE

This is the graded performance item, and it is a conversation, not a test.

**1. Push your work.**

```bash
git add .
git commit -m "fix one edge case from my probe set"
git push
```

`git add .` will **not** pick up `edge_case_probes.py` — that is what the `.gitignore` is for. If it somehow gets staged, run `git reset edge_case_probes.py` and commit again.

☐  My push went through, and my probes file is not in the repo.

**2. Pair up.** One person runs the calculator as the driver; the other calls out inputs. Swap after four minutes so you each drive once. The caller feeds the cases from Part 2 — including the one you fixed. The driver narrates what is happening on screen. The caller writes down anything surprising.

☐  My partner and I each drove once.

**3. Each person answers these three questions out loud:**

| Question | My partner's calculator | My calculator |
|---|---|---|
| What did your calculator do well? |  |  |
| What was the one bug you fixed, and what does it do now that it did not before? |  |  |
| What is still not perfect about it? |  |  |

The one input that surprised me most was my partner's:

   _________________________________________________________________________

   _________________________________________________________________________

**4. Take a screenshot before you leave.** Capture your terminal showing either your passing test run or your fixed bug in action.

☐  I have a screenshot saved.

## TURN IN — SCREENSHOT (due 11:59 PM)

Go to Google Classroom, click **Classwork**, click today's assignment, then **View assignment**. Under **Your work**, click **Add or create**, click **File**, upload your screenshot, then click **Turn in** twice.

☐  My screenshot is attached and the assignment shows **Turned in**.
☐  My partner's name is on the assignment line.

## RUBRIC — 10 POINTS

| Points | What earns them |
|---|---|
| 2 | Working calculator — add, subtract, multiply and divide all run |
| 2 | One genuine bug found **and written down** in Part 2 |
| 1 | At least one case noted as correct behavior |
| 2 | One bug fixed properly, with a comment explaining the change |
| 2 | Partner showcase — drove the calculator and answered all three questions |
| 1 | Screenshot turned in as evidence |

A note on the 2 points for the bug: one honest bug with a clear write-up earns full marks. This is not a hunt for the most damage, and finding four is not better than finding one.

## JOURNAL — BEFORE NEXT TIME

- Which single bug will you fix next time, after the assessment? One. Not three.
- Which case surprised you the most?
- What did your calculator do that you were actually proud of?

   _________________________________________________________________________

   _________________________________________________________________________

Bring next time: your calculator, working and pushed. U1 L14 is the Unit 1 review and catch-up; the assessment after that needs no code and no terminal.
