# U3 L02 — Preview: Mean, Median, Mode — Which One Survives an Outlier?

**LO:** predict which measure of center is robust to a single extreme value, and defend the prediction before you compute.

Paper and prediction day — **no code, no terminals** for the discussion. You
need a pencil, your notebook, and your ability to argue. Today you commit to
an answer *before* seeing the arithmetic, which is the only honest way to
learn which intuition is wrong.

## PART 1 — WARM-UP: THE CHARITY BOARD (5 min)

A charity's board must report one number for last year's giving. One donor
made a typo: their gift was entered as **$9,000** instead of $90.00.

- The board's intern calculates the **mean**. What does the intern report?
- A different intern calculates the **median**. What does she report?
- Which report would *you* sign your name to, and what would you say to the
  board about the other one?

Do not compute yet. Just commit to a position.

## PART 2 — THE SEVEN NUMBERS (10 min)

This is the whole unit in one line. Seven donations came in:

```text
    25.00    40.00    50.00    60.00    75.00    100.00    9000.00
```

Call the 9000.00 the **outlier** — one value, far from everything else.

Write down your prediction for **each** measure, and mark each one
VULNERABLE or STABLE to the outlier:

| Measure | Your predicted value | Vulnerable or stable? | Why? |
|---|---|---|---|
| **Mean** (the average) | | | |
| **Median** (the middle) | | | |
| **Mode** (the most common) | | | |
| **Range** (largest − smallest) | | | |

Rules of the day: predict before computing, and give a *reason* in the last
column. A wrong prediction with a good reason is worth more than a right one
with no reason.

## PART 3 — WORK IT BY HAND (15 min)

No computers. Arithmetic only. Do each one on paper.

**Mean.** Add all seven, divide by 7. Now do it again with the 9000.00
**removed** (six numbers, divide by 6).

**Median.** Sort them, find the middle. Seven numbers — what position is the
middle? Now remove the 9000.00: six numbers, so there is no single middle
value. What do you do, and what do you get?

**Mode.** Which value appears most often? Does the outlier change that?

**Range.** Largest minus smallest, with and without the outlier.

Now fill in the reveal table and correct your predictions:

| Measure | With 9000.00 | Without 9000.00 | Changed? |
|---|---|---|---|
| Mean | | | |
| Median | | | |
| Mode | | | |
| Range | | | |

## PART 4 — THE REVEAL (10 min)

Here are the real answers. Compute nothing — just compare to your paper.

```text
              WITH 9000.00     WITHOUT        verdict
Mean             1335.71        58.33         23x larger
Median              60.00        55.00        barely moved
Mode              no mode       no mode        unchanged
Range             8975.00       75.00         120x larger
```

Now the actual lesson, in your own words:

- **The mean and the range are hostage to one value.** The mean went from
  58.33 to 1335.71 — a 23x jump — because 9000 is 1 of 7 numbers here and
  dominates the sum. In a real dataset of 200 donations, one bad value still
  moved our mean from 267.40 to 716.07. That is a 2.68x jump.
- **The median barely noticed** (60.00 → 55.00). It is built from *position*,
  not *magnitude*, so one extreme value cannot reach it. This is why the
  median is the **robust** measure of center.
- **The mode never changed** — but not because it is robust. It is
  unchanged because these seven numbers are all **different**. There is no
  mode at all. Be careful here: the mode's stability is an accident of this
  data, not a guarantee. When values are all distinct, the mode is useless.
- **The range is the worst of the four.** It is 120x larger with the outlier
  — the most extreme distortion of anything we computed.

## PART 5 — SO WHICH NUMBER DO YOU TRUST? (10 min)

This is the part that matters in the real world. Careful: the answer is not
"always use the median."

- Name a situation where the **mean** is the better answer, and the median
  would mislead. (Hint: think about totals and budgets, not about a "typical
  person.")
- Name a situation where the **median** is the better answer.
- Our charity board: which one do you report, and what is the *other* one
  for? (There is no wrong answer here, but "I'll just report one number" is
  a bad answer.)

Write your own rule in one sentence, in the form: *"Use the mean when ___;
use the median when ___."*

## PART 6 — JOURNAL + PUSH (last 10 min)

```bash
cd ~/compmath-lab
touch journal-u3l02.md
```

Answer in the file, 2-3 sentences each:

- What did you predict for the mean before computing, and what was it
  actually? If you were wrong, what did you get wrong about how the mean
  works?
- The median moved from 55.00 to 60.00. Explain in your own words why the
  outlier barely touched it.
- Write your own rule from Part 5. You will use it on the paper check.

```bash
git add journal-u3l02.md
git commit -m "U3 L02 preview journal: mean vs median vs mode vs range"
git push
```

- **Asked for a username/password?** GitHub username + Personal Access Token
  (PAT) — never your GitHub password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 2 prediction table, filled in **before** you computed
2. your Part 3 hand-work on paper
3. your Part 6 journal file open
4. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

Early finishers: invent a fourth measure — the **mid-range**, or the
difference between the mean and the median — and say out loud whether it
would be robust or vulnerable to the 9000.00. There is no wrong answer, but
there is a defensible one.
