# U3 L01 — Launch: From Charts to Numbers, Why a Picture Is Not Enough

**LO:** explain what a chart can and cannot tell you, and write the one sentence a number would answer where a chart cannot.

Unit 2 you turned numbers into pictures. Today we go the other way and find
out what pictures *lose*. Every chart you made last unit has something it
cannot tell you. Today we name that gap, and we start building the tool that
fills it.

Your datasets for this unit are already on your workspace at
`/tmp/u3_datasets/`. You never install anything.

```bash
cd ~/compmath-lab
ls /tmp/u3_datasets/
```

## PART 1 — WHAT YOUR CHARTS CANNOT SAY (10 min)

In your notes, take these three questions and answer each **for a specific
chart you made in Unit 2** — not in general, but naming the chart:

1. Your `study_habits` scatter (Test Score vs. Study Hours): what was the
   *average* test score? Could you read that off the chart? (No — you could
   estimate the *range*, not the middle.)
2. Your Unit 2 categorical bar chart: what was the **median** value in the
   tallest bar's category?
3. Your project dashboard: if I asked "is this difference real, or did I get
   lucky with a few extreme values?" — what would you need that the chart
   does not show?

Key idea, write it down:

- A chart answers **shape** questions: what is the trend, where are the
  clusters, what looks unusual.
- A chart cannot answer **quantity** questions: what is the middle, how
  spread out, how many.

Today we build the quantity half. Everything in Unit 3 is a number that
answers "how much" and "how spread out" — and every one of those numbers is
a decision someone made, and can be misused.

## PART 2 — THE DONATION DATA (10 min)

Our dataset for the first three lessons is an alumni donation log: 200
entries, one number per line.

```bash
head -5 /tmp/u3_datasets/u3_donations.txt
```

Read the top of the file. There is a `#` comment line, then values. This is
the same layout you handled in Unit 2 — comment first, data after.

Load it exactly the way L11 taught you, and print the first five:

```python
with open("/tmp/u3_datasets/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

data = [line for line in raw if not line.startswith("#")]
donations = [float(line) for line in data]

print(len(donations), "values")
print(donations[:5])
```

You should see `200 values`. In your notes:

- Why filter `startswith("#")` *before* converting to `float`, and not
  after? (Try `float("# Alumni...")` and read the error. What does the
  error tell you about the order of operations?)
- The file's comment says one entry is a **mis-key**. Hold that thought.

## PART 3 — THE SENTENCE A NUMBER WOULD ANSWER (10 min)

Here is our dataset as a chart. Before you compute anything, write down what
you think the "typical" donation is:

```text
Your best guess for a typical donation:  $ _______
```

Now the honest question. If I said to a donor, *"our average donor gave
$242"*, how would you react? And if I said *"our median donor gave $242"*?

Those are different sentences about different people, and today you will
find out which one the data actually supports.

## PART 4 — SORT IT AND LOOK (10 min)

No formulas yet — just look at the data:

```python
ordered = sorted(donations)
print("smallest five:", ordered[:5])
print("largest five: ", ordered[-5:])
print("count:", len(ordered))
```

Look at the largest five. Then answer in your notes:

- Are the five largest numbers all about the same size, or is one of them
  dramatically bigger than the rest?
- The largest value in the file is `90000.00`. The second largest is
  `813.89`. Roughly **how many times bigger** is the biggest than the
  second biggest? (This is the "easily seen" clue — the file's comment
  called it a mis-key, and now you can see why.)
- Would you describe a donor who gave 90,000 as "typical"? Why or why not?

## PART 5 — WHY THIS MATTERS (10 min)

Here is the situation this unit is about. A charity's board looks at one
number to decide whether the fundraising campaign worked. Suppose the
number is the **mean** and suppose one gift was a typo.

- What could go wrong for the board's decision?
- What would you want to know *besides* the mean before you trusted it?

Today: nothing. In Unit 3 you will have three or four numbers instead of
one, and you will be able to say exactly what each one throws away. That
is the difference between a number and a statistic.

## PART 6 — JOURNAL + PUSH (last 10 min)

```bash
cd ~/compmath-lab
touch journal-u3l01.md
```

Answer in the file, 2-3 sentences each:

- Name one specific question your Unit 2 charts could not answer.
- A donor gave 90,000 while the next largest was 813.89. What is the *word*
  for a value like that, and why does one value change what a whole dataset
  means?
- What would you want a second number for, if you only had one number to
  describe 200 donations?

```bash
git add journal-u3l01.md
git commit -m "U3 L01 launch journal: what a chart cannot say"
git push
```

- **Asked for a username/password?** GitHub username + Personal Access Token
  (PAT) — never your GitHub password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 1 answers naming a specific Unit 2 chart
2. your Part 2 terminal output showing `200 values` and the first five
3. your Part 4 output showing smallest five and largest five
4. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

Early finishers: sort the data and print the 190th through 200th values, and
write down what you notice about that neighborhood of the list.
