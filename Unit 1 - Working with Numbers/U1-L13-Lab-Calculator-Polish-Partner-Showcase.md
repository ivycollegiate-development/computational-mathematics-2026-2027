# Lesson 13 — Calculator Polish and Partner Showcase

**LO:** exercise your calculator with unusual inputs, find one thing that still
breaks, fix it, then show a partner what your program does well.
then show a partner what your program does well.

**Folder:** `compmath-u1-calculator-lab` (in your VS Code workspace)

You already did the hard part. Your calculator handles add, subtract, multiply
and divide, and it has a menu that a user can actually drive. L11 and L12 were
about making it *work*. This lesson is about two last things: finding the inputs
that make it **improve**, and showing somebody else what you built.

Most of what you find here will be small. That is the honest truth about code at
this stage — a working calculator with two known weak spots, not a disaster.
Treat this as a careful look around your own work, not an exam.

---

## Part 0 — Setup (2 min)

You already have the folder from L08. Go get it and pull today's changes:

```bash
cd ~/compmath-lab
git config pull.rebase false
git pull
```

**Never cloned?** Use your own repo instead:

```bash
git clone https://github.com/ivycollegiate-development/compmath-u1-calculator-lab-$(whoami)_student.git ~/compmath-lab
cd ~/compmath-lab
```

☐ My terminal is in `~/compmath-lab` and `git pull` finished with no red text.

---

## Part 1 — Generate your edge cases (5 min)

You get your own randomized set of unusual inputs, seeded from your seat number.
Nobody knows your cases in advance, and yours will not match anyone else's.

```bash
python3 gen_probes.py <your seat number>
```

Replace `<your seat number>` with the number you were given — for example:

```bash
python3 gen_probes.py 7
```

This writes a file called `edge_case_probes.py` with four groups:

| Group | What it is checking |
|---|---|
| `WRONG_TYPE` | input that is not a number at all |
| `HUGE` | numbers too big or too small for normal math |
| `BOUNDARY` | values right at the edge of a range |
| `DIV_ZERO` | dividing by zero, or by something that rounds to zero |

Two things worth knowing:

- `edge_case_probes.py` is **already in your `.gitignore`**. Do not commit it and
  do not share it. That is intentional — the cases are yours to work through.
- If you lose it, run `gen_probes.py` again with the same seat number and you
  get the exact same set back.

☐ `edge_case_probes.py` exists in my editor, and I understand I will not commit it.

---

## Part 2 — Work the cases (15 min)

Pick any three cases — spread them across the four groups rather than doing all
three from one. Run your calculator and type the case in.

For each one write down all three of these, on paper or in a scratch file:

```
the input  |  what actually happened  |  bug, or correct behavior?
```

That third column is the important one, and it has two valid answers:

- **bug** — it crashed, gave a wrong answer, or behaved confusingly.
- **correct behavior** — it handled the input properly.

Write down "correct behavior" when you find it. That is a real finding, not a
dud. Two examples from the starter code:

- `divide(1, 0)` → `ZeroDivisionError`, the program stops. **That is a bug.**
- `get_number()` on `4` → returns `4.0` and moves on. **That is correct
  behavior**, and it is worth noting that it works.

You are looking for **one genuine bug**, and one is a complete result. Work three
cases, name the one bug you will fix, and stop hunting — finding four is not
better than finding one, and digging for damage that is not there wastes the time
you need to prove your fix works.

☐ I worked three cases. ☐ I have one genuine bug written down.
☐ I noted at least one case that behaved correctly.

---

## Part 3 — Fix what you found (15 min)

Now make your calculator better. Fix the one bug you named in Part 2, properly.

One fix, done well and proven, is the whole assignment. You have to show it
working in Part 4, and that matters more than a longer list of problems you did
not have time to address.

Open `calculator.py`. You will see two functions with `FIX ME` comments:
`get_number()` and `divide()`. Whichever bug you are fixing, put your code where
the `FIX ME` says, and add a comment saying what you changed and why.

If you fixed an input bug, this shape works:

```python
def get_number(prompt):
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("That is not a number. Try again.")
```

If you fixed the divide-by-zero bug:

```python
def divide(a, b):
    if b == 0:
        return None
    return a / b
```

…and then handle the `None` where you print the result, so the user sees a
message instead of `TypeError`.

Whichever route you took, verify the fix:

```bash
python3 test_calculator.py
```

The starter ships with `1 of 4 passing` — one test already passes, and the other
three are the bugs you may find. **Your goal is 4 of 4.** You are fixing one
today, so expect 2 of 4, and that is a real result — say in your showcase what is
still outstanding.

☐ The test run improved from 1 of 4. ☐ I re-ran the failing case from Part 2 and it now behaves correctly.

**If you are not done with everything:** stop here anyway. A working calculator
with one fixed bug is a complete lesson. Push what you have and move to Part 4.

---

## Part 4 — Partner showcase (15 min)

This is the graded performance item, and it is a conversation, not a test.

**1. Push your work.**

```bash
git add .
git commit -m "fix one edge case from my probe set"
git push
```

Note `git add .` will **not** pick up `edge_case_probes.py` — that is what the
`.gitignore` is for. If it somehow gets staged, `git reset edge_case_probes.py`
and commit again.

☐ My push went through, and my probes file is not in the repo.

**2. Pair up with one partner.**

One person runs the calculator as the driver; the other calls out inputs. Swap
after four minutes so you each drive once.

**Driver:** run your calculator. **Caller:** feed it the cases you remember from
Part 2 — including the one you fixed. The driver narrates what is happening on
screen. The caller writes down anything surprising.

Then swap, and do it again with your partner's program.

**3. Each person answers these three questions out loud:**

- What did your calculator do well?
- What was the one bug you fixed, and what does it do now that it did not before?
- What is still not perfect about it?

**4. Take a screenshot before you leave.** This is your turn-in evidence. Capture
your terminal showing either your passing test run or your fixed bug in action.

- Chromebook: hold **Ctrl + Shift** and press the **Show windows** key
- Windows: **Windows key + Shift + S**
- Mac: **Cmd + Shift + 4**
- iPad: side button + volume-up

☐ My partner and I each drove once. ☐ I have a screenshot saved.

---

## TURN IN — screenshot

Upload your screenshot to the Classroom assignment:

1. Go to Google Classroom, click **Classwork**, click today's assignment, then
   **View assignment**.
2. Under **Your work**, click **Add or create**, click **File**, upload your
   screenshot, then click **Turn in** twice.

☐ My screenshot is attached and the assignment shows **Turned in**.

---

## Rubric — 10 points

| Points | What earns them |
|---|---|
| 2 | Working calculator — add, subtract, multiply and divide all run |
| 2 | One genuine bug found **and written down** in Part 2 |
| 1 | At least one case noted as correct behavior |
| 2 | One bug fixed properly, with a comment explaining the change |
| 2 | Partner showcase — drove the calculator and answered all three questions |
| 1 | Screenshot turned in as evidence |

**A note on the 2 points for the bug:** one honest bug with a clear write-up
earns full marks. This is not a hunt for the most damage, and finding four is not
better than finding one.

---

---

## BEFORE NEXT TIME

**Journal entry (5 min, U1 L12 handed you the prompt):**

- Which single bug will you fix next time, after the assessment? One. Not three.
- Which case surprised you the most?
- What did your calculator do that you were actually proud of?

**Bring next time:** your calculator, working and pushed. Next lesson is the
Unit 1 assessment — no code, no terminal.

---

*Turn in: your screenshot + your partner's name on the assignment line.*
