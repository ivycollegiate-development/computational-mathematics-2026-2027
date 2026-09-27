# U3 L24 — Winter Break Launch: Field Notes (Full Day)

**Date:** Dec 17 (Thu) — last day before Winter Break
**LO:** close Unit 3 on paper, and set up a break task that works on a plane.

Today you finish the `statslib` lab from L23. Then we do the last thing in the
unit, and it is **paper** — the same deal as the fall break launch, except this
break is sixteen days long and the most of it is holiday.

**The rule for the next sixteen days: no laptop.** The assignment below is done
with a pencil. Students who fly home, stay in Taiwan, or go nowhere at all can
all finish it. That is on purpose, not a limitation.

## PART 1 — CLOSE THE LIBRARY (first 30 min, whatever you have)

Whatever state `statslib.py` is in right now is the state you walk away with.
Before anything else:

- ☐  `python3 statslib.py` runs and prints `all tests passed`
- ☐  the six bad calls print clear `ValueError` messages, not tracebacks
- ☐  `describe()` runs on your three datasets and you pasted the output
- ☐  the module docstring answers the five questions from L23 Part 4

**If a test still fails today, you do not delete it.** Leave the failing test in
the file with a comment saying what you think is wrong. That is worth more on
Jan 4 than a green run you got by removing the evidence.

## PART 2 — ❄️ WINTER BREAK ASSIGNMENT (launched today, due Jan 7)

**No code over the break. No repo work. This is paper.**

Sixteen days is long enough to forget a semester. So the work is small and the
deadline is real. Before you come back on Jan 4, do exactly this, on paper:

1. **Pick one number you live with.** Not a course average — a number that
   appears in your actual week. Minutes of sleep. Steps. Money spent on food.
   Minutes spent on a commute. Songs played. Screens. Pick **one**, and write
   down roughly how many days a week you could honestly collect it for.
   - If you can collect **21 or more** values, use that number.
   - If not, pick a different number. Do not invent data you did not live.

2. **Collect 21 values, on paper.** A small table: date, value, one word of
   context. "Tue, 6.5 h, exam week." "Wed, 4, presentation." The third column is
   what turns 21 numbers into data later — you will not remember why a value was
   weird without it.

3. **Compute five numbers by hand.** Sorted, on paper, no calculator on the
   first pass:
   - **n**
   - **mean**
   - **median**
   - **min and max**
   - **the range** (max − min)

   Show the sorted list. I want to see the sort, because a wrong median is
   almost always a sorting mistake, and a visible sort is how I find that in ten
   seconds instead of five minutes.

4. **Compute the five-number summary.** q1, median, q3 using the **same**
   `percentile` convention you used in L08, L14, and L21: `k = (n - 1) x p`,
   interpolate between the two values that straddle it. Write the `k` you
   computed for q1 and for q3.

5. **Find the IQR fences and name your outliers.** `lo = q1 - 1.5 x IQR`,
   `hi = q3 + 1.5 x IQR`. List every value outside the fences. Then, in one
   sentence: **is each one a mistake, or a real day?** A 14-hour sleep in a week
   you were sick is not an error in your data. Say which it is.

6. **Write the claim your numbers support — in one sentence, and only one.**
   - Too vague: *"my sleep data is interesting."*
   - Good: *"My median sleep is 6.2 hours but my mean is 6.9, so the two late
     nights a week are pulling the average above what a typical night actually
     looked like."*
   - Also fine: *"My range is 4.1 hours and my IQR is only 1.2, so almost
     everything about my week is predictable and one or two days are not."*

7. **Privacy check.** Your table has real dates and a real number about a real
   person: you. Before you turn it in, answer two questions in the margin:
   - If a classmate read your table, could they work out **who** it is?
   - What would you have to change to publish the same table with the story
     intact but the person unidentifiable?
   That is the L12 lesson — suppression and generalization — applied to your own
   life, not to a dataset.

**Turn in:** one photo of the pages — the table, the five numbers, the
five-number summary, the outliers, and the one-sentence claim. Upload to Google
Classroom. **Due 11:59 PM Thursday Jan 7.**

## PART 3 — ON JAN 4, THIS IS WHAT YOU WILL ALREADY HAVE DONE

- ☐  21 real values, sorted
- ☐  a mean **and** a median computed by hand
- ☐  a five-number summary with your `k` values written down
- ☐  outliers named and judged
- ☐  one sentence you can defend
- ☐  a privacy fix for your own data

None of that needs a computer. All of it makes Jan 4 fast.

## PART 4 — WHAT HAPPENS ON JAN 4

Briefly, so you can rest instead of worrying:

- We run your numbers **through code** and see whether Python agrees with your
  pencil. That is the whole point of the return day.
- We do a **Unit 3 post-mortem**: which concept from the unit you own, and which
  one you are still faking. I want the honest answer.
- Unit 4 opens the following week. No project planning over the break.

## 🇹🇼 BREAK CONTEXT

**Winter Break: dismiss 12:30 Friday Dec 18, out through Sunday Jan 3. Classes
resume Monday Jan 4.** Sixteen days.

Comp Math is an **early-period** course. The first period after a break is not
the time to learn something new, which is why Jan 4 is a return day and not a
launch. Sleep more than you study.

## 📋 PAPER RULES (for the break, not today)

- ☐  handwriting is fine, it does not need to be beautiful — it needs to be **legible to you in two weeks**
- ☐  show your sorted list, every time
- ☐  if you are not sure about a value, write the number anyway and put a `?`
  next to it. A marked uncertainty is honest; a filled-in guess is not.
- ☐  no screenshotting someone else's break assignment. Your week is not the
  assignment.

## NO TURN-IN TONIGHT

Nothing is due tonight. The break assignment above is due **Jan 7** — photograph
the instructions or write the four steps down before you leave so you remember
them on Jan 4.
