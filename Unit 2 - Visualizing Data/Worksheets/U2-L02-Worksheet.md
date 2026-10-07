# U2 L02 — Worksheet: Bridge from Numbers to Data

Names: ___________________________  Date: ____

Exploration day. This sheet is a fill-in companion to the lesson in the repo — you read the directions there and write your answers here. No plotting yet; today is pure REPL exploration.

## Part 1 — What is data?

| Question | My answer |
|------------|------------|
| The weather this morning: is that a number or data? What is the difference? |                                                                      |
| Your grade in this class: is it a number or data? What makes it *mean* something? |                                                                      |
| Handed 52 test scores as a list, what can you tell at a glance? What can you NOT? |                                                                      |

Key idea, in your own words: **data is numbers plus context.** A number tells you *how much*; data tells you _how much of what, from whom, measured when_.

   _________________________________________________________________________

## Part 2 — Meet the dataset

For each column of the study-habits survey, write what it measures and what unit or range it lives in.

| Column | What it measures | Unit or range |
|------------|--------------------|----------------|
| Student_ID  |  |  |
| Study_Hours |  |  |
| Test_Score  |  |  |
| Attendance  |  |  |
| Sleep_Hours |  |  |

Which column do you predict has the strongest connection to `Test_Score`?

   _________________________________________________________________________

What is one thing this 5-row excerpt CANNOT tell us that the full 52 rows could?

   _________________________________________________________________________

## Part 3 — Reading a CSV with only the stdlib

Why did we use `with open(...)` instead of just `open(...)`?

   _________________________________________________________________________

What type is each thing inside `rows`? What type is each element of a row?

   _________________________________________________________________________

`rows[0]` is NOT a data row. What is it, and why must we skip it?

   _________________________________________________________________________

## Part 4 — The messy first line

What is on line 1 of the mental-health file, and why does `messy[0][1] + 1` crash?

   _________________________________________________________________________

Why index `2:` and not `1:`? What would `1:` have given you?

   _________________________________________________________________________

## Part 5 — Numbers become information

Run the Part 5 code and record your numbers.

| Value | Result |
|------------|------------|
| n = |  |
| mean score = |  |
| mean study hours = |  |
| max score  |  |
| min score  |  |
| range (max − min) |  |
| mean of `high` (hours ≥ 4) |  |
| mean of `low` (hours < 4) |  |
| high − low gap |  |

One sentence: does the high-vs-low difference support your Part 2 prediction?

   _________________________________________________________________________

## Part 6 — Who is this data about?

If a school used this data to decide study-hall policy, what should it be careful about? (Correlation vs. cause — say it in your own words.)

   _________________________________________________________________________

What could a missing row or a lying survey answer do to the mean?

   _________________________________________________________________________

## Part 7 — Journal + push

- ☐  `journal-u2l02.md` created in `~/compmath-u2-data-lab`, the three prompts answered, `git push` confirmed.

## TURN IN

- ☐  Parts 1–6 complete, including your Part 5 numbers and the high-vs-low comparison.
- ☐  Screenshot to the Classroom assignment by 11:59 PM tonight showing: your Part 3 output (`len(rows)` = 53, `rows[0]` = column names), your Part 4 crash and `len(data_rows)` = 60, your Part 5 means and comparison, and the successful `git push`.

Keep the terminal open — spot-checks.