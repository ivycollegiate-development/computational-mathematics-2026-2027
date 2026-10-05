# U1 L16 — Unit 1 Crash Course: Last Call Before the Assessment (TECH DAY)

**LO:** convert yesterday's paper stress test into working code, so nothing on
the assessment tomorrow is a surprise you could have fixed today.

> **Sequence note.** The Unit 1 assessment paper and its answer key are in
> `Assessments/` — see [`Assessments/README.md`](Assessments/README.md) for the
> full order of L14 → L15 → L16 → assessment → L17. This lesson is the last
> prep session before the paper.

Tomorrow is the Unit 1 assessment. You already did a closed-notes run
yesterday and you have an honest red list from earlier this week. Today is not a review
lecture — it is the last chance to **make the broken thing work** before you
are asked to explain it on paper.

Bring your calculator lab repo open.

## PART 0 — REDUCE YESTERDAY TO A NUMBER (5 min)

Take the paper you self-marked in Part 3 yesterday. Count only the items you
lost points on. Write the count here: ______

That number is your scope. You are not fixing Unit 1 today. You are fixing
**that** many things.

## PART 1 — REPRODUCE, THEN FIX (30 min)

Work your own list, in your own repo. For each Red item, in this order:

1. **Make it fail.** Write the smallest snippet that reproduces the mistake.
   Run it. Read the actual output.
2. **Say what you expected** vs what happened. The gap between those two
   sentences *is* the concept.
3. **Fix the real thing in your calculator** — not the snippet. If the bug is
   in `get_number()`, fix `get_number()`.

Do these three in order. Students who skip to step 3 patch symptoms and still
miss the question tomorrow.

```bash
cd ~/compmath-lab
git pull
python3 test_calculator.py
```

A snippet to reproduce the `input()` trap, if you need to see it fail:

```python
age = input("Age: ")
print(age + 1)          # TypeError: can only concatenate str
```

And the fix, which is a conversion *before* the arithmetic — not a `try`
wrapped around the whole program:

```python
while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("That is not a number. Try again.")
```

**The four that cost the most points last time:**

| Symptom | What is actually wrong |
|---|---|
| `7 / 2` and `7 // 2` swapped | `/` is true division and always gives `float`; `//` floors and can give `int` |
| `input() + 1` throws `TypeError` | `input()` always returns a `str` — you must convert before arithmetic |
| A `try` with no `except` | That is not a `try/except`; it changes nothing and still crashes |
| Huge input returns a wrong number | You need an explicit `10**15` ceiling, not Python's unlimited integers |

## PART 2 — THE PAPER IS TOMORROW: REHEARSE THE VERB (20 min)

Tomorrow is pen and paper. In your notes, no computer, answer these the way
you would write them on the exam:

1. What type does `7 / 2` return? What type does `7 // 2` return?
2. Why must `input()` be wrapped in `int()` or `float()`? One sentence.
3. A user types `banana` into `int(input("Age: "))`. Name the exception, then
   write the one line that catches it.
4. A program returns `0.0` when the user meant `0`. Is that a crash or a
   quietly wrong answer? Which is more dangerous, and why?
5. `Fraction(1, 3)` is exact; `1 / 3` is not. Why? Name the type `/` gives.

**Rule for tomorrow: answer the verb.** "What happens when…" wants the actual
error, not your fix. "Why" wants a sentence, not a value. Students lose points
by answering a different question than the one asked.

## TURN IN — PUSH (due 11:59 PM tonight)

One screenshot showing, in order:

1. Your terminal with `python3 test_calculator.py` passing.
2. The `git push` confirmation line.

Submit the screenshot to this assignment on Google Classroom.

Keep the terminal open — spot-checks.
