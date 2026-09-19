# U2 L02 — Bridge: From Numbers to Data

**LO:** transition from Unit 1 (numbers) to Unit 2 (data visualization) by exploring what data looks like and why it matters.

Yesterday you proved you can handle numbers. Today those numbers start meaning
something: we meet our first **dataset** — and discover that real data is
messier than anything we typed ourselves. No plotting yet; today is pure
exploration in the REPL.

## PART 1 — OPENING DISCUSSION: WHAT IS DATA? (10 min)

Before any code, answer in your notes:

- You checked the weather this morning. Was that a number or data? What is
  the difference?
- Your grade in this class: is it a number or data? What makes it *mean*
  something?
- If I hand you 52 test scores as a list of numbers, what can you tell me
  at a glance? What can you NOT tell me at a glance?

Key idea to write down: **data is numbers plus context.** A number tells you
*how much*; data tells you *how much of what, from whom, measured when*.

## PART 2 — MEET THE DATASET (10 min)

Our first dataset this unit is a study-habits survey: 52 students, four
measurements each. Here is a 5-row excerpt:

```text
Student_ID,Study_Hours,Test_Score,Attendance,Sleep_Hours
S01,4.5,82,0.93,7.0
S02,1.0,55,0.71,5.5
S03,7.0,95,0.98,8.0
S04,3.0,74,0.88,6.5
S05,0.5,48,0.65,5.0
```

In your notes, for each column write: *what it measures, and what unit or
range it lives in?* (Attendance is a fraction — 0.93 means 93% of classes.)

Questions to discuss with your table:

- Which column do you predict has the strongest connection to `Test_Score`?
- What is one thing this 5-row excerpt can NOT tell us that the full 52 rows
  could?

## PART 3 — CODE-ALONG: READING A CSV WITH ONLY THE STDLIB (15 min)

Open your workspace. First command, always:

```bash
pwd
```

Then start the Python REPL:

```bash
python3
```

A CSV (comma-separated values) file is just text where each line is a row and
commas split the columns. Python's standard library ships a module for it —
no installs, ever:

```python
import csv

with open("/tmp/u2_datasets/u2_dataset1_study_habits.csv") as f:
    rows = list(csv.reader(f))

print(len(rows))       # how many lines?
print(rows[0])         # what's on the first line?
print(rows[1])         # and the second?
```

Now answer in your notes, then test:

- Why did we use `with open(...)` instead of just `open(...)`?
- What type is each thing inside `rows`? What type is each element of a row?
- `rows[0]` is NOT a data row. What is it, and why must we skip it?

## PART 4 — THE MESSY FIRST LINE (10 min)

Try this:

```python
print(rows[0][1] + 1)
```

It crashes. Why? Because the real file's first line is:

```text
# U2 dataset 1 — study habits survey, collected via Google Form
```

That `#` line is a **comment** someone left in the data file. Real datasets
are full of these surprises: comment lines, blank rows, missing values,
weird units. Our first job as data people is to notice them *before* doing
math.

```python
data_rows = rows[2:]     # skip the comment line AND the header
print(len(data_rows))    # should be 52
print(data_rows[0])
```

In your notes: why index `2:` and not `1:`?

## PART 5 — COMPUTE: NUMBERS BECOME INFORMATION (15 min)

Everything from Unit 1 applies now. Convert, then average:

```python
def mean(nums):
    return sum(nums) / len(nums)

scores = [float(r[2]) for r in data_rows]
hours  = [float(r[1]) for r in data_rows]

print("n =", len(scores))
print("mean score:", mean(scores))
print("mean study hours:", mean(hours))
```

In your notes, then verify in the REPL:

- What is `max(scores)`? `min(scores)`? The range between them?
- Split the class: build `high = [s for s, h in zip(scores, hours) if h >= 4]`
  and `low = [...] if h < 4]`. Print `mean(high)` and `mean(low)`.
- One sentence: does the difference support your Part 2 prediction?

That's the whole game of data work: **a pile of numbers becomes one
comparable statement.** Next lesson, we make that statement a *picture*.

## PART 6 — DISCUSSION: WHO IS THIS DATA ABOUT? (5 min)

This dataset describes *people* — including, in spirit, you. In your notes:

- If a school used this data to decide study-hall policy, what should it
  be careful about? (Correlation vs. cause — say it in your own words.)
- What could a missing row or a lying survey answer do to the mean?

## PART 7 — JOURNAL + PUSH (last 10 min)

In your lab repo:

```bash
cd ~/compmath-lab
touch journal-u2l02.md
```

Answer in 2-3 sentences each:

- What surprised you about the real file compared to the excerpt above?
- What is one messy-data surprise you expect in future datasets?
- Write down your Part 5 numbers: n, both means, and the high-vs-low gap.

```bash
cd ~/compmath-lab
git add journal-u2l02.md
git commit -m "U2 L02 data exploration journal"
git push
```

- **Asked for a username/password?** GitHub username + PAT, never your
  password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 3–4 REPL output (`len(rows)`, `rows[0]`, the comment-line crash)
2. your Part 5 means and the high-vs-low comparison
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
