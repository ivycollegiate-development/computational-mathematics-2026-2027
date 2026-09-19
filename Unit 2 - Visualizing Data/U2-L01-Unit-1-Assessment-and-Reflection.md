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

### Section A — Short Response (10 questions, 2 points each)

Answer in complete sentences where it asks *why*; a word or value is fine where
it asks *what*.

1. What type does Python give you when you write `7 / 2`, and what type for
   `7 // 2`? Give both answers and both types.
2. Why does `input()` need a wrapper like `int()` or `float()` around it when
   we want a number? What type does `input()` always return?
3. A user types `banana` into `age = int(input("Age: "))`. Name the exact
   exception Python raises, and write the one line of `try/except` that would
   catch it.
4. What is the difference between a program that **crashes** and a program
   that is **quietly wrong**? Which one is more dangerous, and why?
5. Write the truth table (just True/False) for each of these, assuming
   `x = 0`:
   - `x == 0`
   - `x = 0`
   - `x > 0 or x < 0`
6. Why is `Fraction(1, 3)` exact but `1 / 3` is not? What kind of number does
   Python use for `/`?
7. In your calculator lab, what did the `get_number()` function protect
   against, and what did it do when validation failed?
8. Order these from smallest to largest step size (precision):
   `int`, `float`, `Fraction`. One sentence on why.
9. What does `%` (modulo) return for `17 % 5`, and name one real use for
   modulo we discussed in class.
10. The security lens: give one example from Unit 1 of "trusting the user"
    going wrong, and the one rule you now apply to every input.

### Section B — Code Reading (2 problems, 5 points each)

*You do not run this code. You read it like a debugger would.*

**Problem 11.** Read this program:

```python
total = 0
for price in ["3.50", "4", "1.25", "oops"]:
    total = total + float(price)
print("Total:", total)
```

a) What happens on the third loop iteration? Be precise about which value
   is being converted.
b) What happens on the fourth iteration? Name the exception.
c) Rewrite ONLY the loop body so a bad price prints a warning and the
   program keeps going instead of crashing. (Two or three lines is enough.)

**Problem 12.** Read this converter:

```python
def f_to_c(f):
    return f * 5 / 9 - 32

temp = input("Enter °F: ")
print(f_to_c(float(temp)))
```

a) There is one bug that makes this *quietly wrong* — find it and state what
   the correct line is. (Hint: test it mentally with 212 °F.)
b) The program still crashes on `banana`. Write the full `try/except` version
   of the last two lines.
c) One sentence: why is bug (a) worse than bug (b)?

When you finish the written section, turn your paper face down and wait
quietly. If you finish early, review your answers — there is no extra credit
for finishing fast.

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
