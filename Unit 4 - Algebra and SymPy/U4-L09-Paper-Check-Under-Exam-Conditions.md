# U4 L09 — Paper Check Under Exam Conditions: Last Class Before Midterms (Full Period)

**LO:** perform, under timed closed-book conditions, the full Units 1–4 content you will be examined on.

This is not a practice quiz with a study guide. It is a **paper check under
exam conditions** — timed, closed-book, no laptop, no notes, no phone. The
midterm block opens **Monday Jan 18** and runs through **Thursday Jan 21**.

I am going to treat today the way the exam will treat you, because the gap
between "I understand this" and "I can produce this in 45 minutes with no
material" is exactly what the next three days are for.

**Bring:** two sharpened pencils, an eraser, a calculator if you want one, and
yourself. **Do not bring** your notebook, your error log, your laptop, or your
phone. Leave them in your bag. I will not ask for them and I will not hold them
for you later.

## PART 1 — CONDITIONS (5 min, read before you start)

- ☐  Write your name and the time you start. ______
- ☐  **Time limit: 50 minutes.** The clock starts when I say start, not when you
     start writing.
- ☐  Closed book. Nothing on your desk except this paper, a pencil, and a
     calculator if you brought one.
- ☐  Show work. A bare answer earns no credit, because I cannot distinguish a
     correct method from a lucky guess.
- ☐  If you do not know a question, write `SKIP` and move on. Do not sit on it.
- ☐  Put a `?` next to every answer you are not sure of. A `?` costs nothing
     and tells me something true about your preparation.
- ☐  Do not erase. Cross out a wrong answer and continue — crossed-out work is
     evidence you were thinking.

**On the grading of this paper, plainly:** I will mark method over result. A
well-set-up quadratic that goes wrong in the last step scores higher than a
correct answer with no work, and I will tell you so in writing on the returned
paper.

## PART 2 — THE PAPER (50 minutes)

### SECTION A — Working with Numbers (Unit 1) — 8 marks, ~10 min

**A1** [2] Evaluate without a laptop. `17 // 5`, `17 % 5`, and `17 / 5`. Show
each.

**A2** [2] A program must read a student's score from the keyboard and reject
anything outside 0–100. Write the two lines that do it, including the
conversion and the check.

**A3** [2] What is printed, and why?

```python
x = 10
def change(x):
    x = x + 1
    return x
print(change(x), x)
```

**A4** [2] A counter needs to go up to 3,000,000,000. Which Python type, and
exactly what goes wrong if you choose wrong?

### SECTION B — Visualizing Data (Unit 2) — 6 marks, ~7 min

**B1** [2] A chart shows failed logins spiking hugely on a Monday. Give **two**
reasons the chart might be misleading that have nothing to do with the data.

**B2** [2] A y-axis runs from 94 to 100 on a chart of success rate. Is this
misleading? Explain, and say what you would do about it.

**B3** [2] Name the three checks every chart must pass before you show it, and
say which one people skip most often.

### SECTION C — Describing Data with Statistics (Unit 3) — 12 marks, ~13 min

**C1** [2] For `n = 12` sorted values, compute `k` for `q1` and for `q3` under
`k = (n − 1) × p`, and name the two indices each `k` falls between.

**C2** [2] A dataset has mean 58, median 71, min 12, max 130. Is the mean
pulled up or down, and by what specifically?

**C3** [2] Write the IQR fence formulas, and state the exact rule for calling a
point an outlier.

**C4** [2] A 4,000-row table of student ID, name, and grade is to be shared
with a vendor. Name **two** specific problems, and give **two** specific
fixes — one for each.

**C5** [2] A dataset has `n = 20`. How many values can you drop without
changing the median at all? And why is that different from the mean?

**C6** [2] One sentence: what does the mean tell you that the median does not,
and what does the median tell you that the mean does not?

### SECTION D — Algebra and SymPy (Unit 4) — 20 marks, ~20 min

**D1** [2] Explain in one or two sentences why `3*x` in Python is not the same
as the algebra `3x`, and what a `Symbol` is for.

**D2** [2] Expand `(x + 4)(x − 4)` and factor the result. Name the identity.

**D3** [3] Solve `4x − 11 = 3x + 2`. Show the line where a sign is at risk, and
say in words what you did to protect it.

**D4** [3] `3x² − 5x − 2 = 0`. Find the discriminant, give both roots, and give
them as fractions in lowest terms. Show the formula you used.

**D5** [2] What does `solve` return for each of these, and what does each answer
*mean*?

```python
solve([2*x + y - 5, x - y], [x, y])
solve([x + y - 5, x + y - 2], [x, y])
```

**D6** [2] Give one reason `solve` might return a dict whose value still
contains `y`, and say why that case needs special handling in code.

**D7** [2] Compute, and give the rule you used:

```python
(-8) % 5
2 ** 10 % 7
```

**D8** [2] Why must a cipher's modulus have no small prime factors? Give the
specific failure that a factor of `2` or `13` causes in `Z_26`.

## PART 3 — AFTER THE TIMER STOPS (10 min, still paper)

Do not leave. Do not open your notebook yet. Do not talk to your partner about
the answers — that is the one thing that turns this from a measurement into a
guess. Do these three parts first, alone, in writing.

### Part 3A — The self-mark

Mark each question with `✓` (right, and I could have shown the method), `?`
(right, but I guessed or rushed the method), or `✗`.

| section | ✓ | ? | ✗ |
|---|---|---|---|
| A (8 marks) | | | |
| B (6 marks) | | | |
| C (12 marks) | | | |
| D (20 marks) | | | |

The middle column is the one I care about. A `?` is a correct answer you cannot
reproduce on demand, and reproducing it on demand is what an exam tests.

### Part 3B — The diagnosis

1. The section I lost the most marks in is ______ , and the specific question
   types are ______
2. The single concept I will not be able to do in 45 minutes on Monday:
   ______
3. The pattern in my `✗` and `?` marks — is it one habit, or several?
   ______
4. Compare to the U4 L06 diagnostic. Did I close the gap I identified, or
   did I find a new one? ______

That last question is the real one. A diagnostic you do not act on is just a
test you took twice.

### Part 3C — The last three days

| day | the one thing I will fix | how I will prove it to myself |
|---|---|---|
| Fri Jan 15 (tonight) | | |
| Sat Jan 16 | | |
| Sun Jan 17 | | |

Three days. One thing each. If a row says "review Unit 3," rewrite it — that is
not a thing you can do, and it is the most common way students waste the last
weekend before an exam.

- ☐  Sunday night: I will be studying until ______ and then stopping.
- ☐  Monday morning, before the exam: I will ______

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. One photo of the **complete paper**, all four sections, with your start and
   finish times written
2. One photo of **Part 3A and 3C**, filled in
3. One paragraph: your answer to Part 3B #4 — did the plan work, and what does
   that tell you about how you should spend the last three days

**This paper is not graded for a high score. It is graded for whether the
diagnosis in Part 3 is specific.** A paper with 40% and a precise diagnosis is
worth more to you than 85% with "I need to study more."

## 📋 AFTER MIDTERMS

- **Jan 18–21** — midterm block. Nothing from me except the exam.
- **Jan 22 (Fri)** — back to Unit 4. You start the **Cipher Toolkit** project:
  `modkit.py` and `integrity.py` from L05 and L07 become the engine, and you
  build the deliverable. Bring this paper back — I want to compare your Jan 22
  self-assessment against today's.
- **CNY break: Feb 4–14.** Eleven days. Project work over the break is paper
  only; the build days are Feb 15 onward.

**Next:** L10, Fri Jan 22 — Cipher Toolkit project launch. Bring the errors
from today's paper. Especially the `?`s.

## 🇹🇼 TAIWAN CONTEXT

One last reminder about the exam itself. If SymPy is available on the exam
machine, use it to *check* your arithmetic, never to produce it — as you saw
last week, a float can pass an exactness check or fail it depending on
rounding, and you need to know which side of that line your answer is on. Bring
a pencil. The exam is paper, and the paper is the point.
