# U3 L04 — Reflection: What Each Statistic Throws Away

**LO:** explain, in your own words, what information a given measure of center or spread destroys, and argue for which measure fits a situation.

Paper and reflection day — **no code, no terminals** for the discussion. You
have the tools now. Today you learn what each one *costs*, because a
statistic is not just a number, it is a number plus a decision about what to
ignore. That decision can be honest or dishonest, and telling the difference
is the skill.

## PART 1 — WARM-UP: THREE DONORS, ONE NUMBER (5 min)

Three fundraising classes, one donor each. Each class raised money; here is
the **entire** record:

```text
Class A:  one gift of 900.00        -> mean 900.00, median 900.00
Class B:  ten gifts of 90.00       -> mean  90.00, median  90.00
Class C:  five gifts, 80 80 90 100 110 -> mean  92.00, median  90.00
```

- Which class raised the most? Which one is most *typical* for its donors?
- Class A has the highest mean. Is that a good thing, or a weird thing? Who
  does that one gift represent — every donor in the class, or just one?
- Say out loud what the mean of Class A is *describing*: a gift, or a class?

## PART 2 — THE DASHBOARD PROBLEM (10 min)

Here is a real scenario. A non-profit's website shows, for each program,
"average cost per participant." The programs are:

- **Rooftop Garden** — 12 participants, 4,800 total, and one participant
  received an unusually large materials grant
- **Tutoring** — 240 participants, 96,000 total, costs fairly even

Both programs show "average cost per participant: 400.00."

Answer in your notes:

- Two numbers are identical: 4,800 / 12 = 400.00 and 96,000 / 240 = 400.00.
  Do the two programs **cost the same** per participant? What did the
  dashboard throw away?
- For which program is the 400.00 actively *misleading*, and why that one?
- What extra number would you add next to the 400.00, and where would you
  get it?

## PART 3 — WHAT EACH MEASURE CANNOT SEE (15 min)

Fill in the "blind spot" column from memory and from your Unit 3 labs. This
table is worth copying into your notebook properly — it is the Unit 3 spine.

| Statistic | The question it answers | Its blind spot (what it cannot see) |
|---|---|---|
| **Mean** | | |
| **Median** | | |
| **Mode** | | |
| **Range** | | |
| **Standard deviation** | | |

The one to get right is the **median's** blind spot, because it is the most
surprising. Our donations data makes it concrete:

```text
                    clean (199)     with 90000.00 (200)
mean                    267.40                716.07    <- 2.68x
median                  242.38                242.76    <- 38 cents
```

The median **cannot see** that something enormous is wrong. Imagine a charity
that reported only the median: 242.38 every single year while the data got
more and more broken. The median would never warn them. That is its cost.

Write one sentence: *the median is robust to extremes, and the price of that
robustness is that it also cannot tell you extremes exist.*

## PART 4 — THE MODE'S HONEST LIMIT (10 min)

Our donation data: 200 values, **199 distinct**, and the most common value
appears **twice**.

- So: does this data have a mode? Defend your answer precisely. (Be careful
  — `most_common` returns something no matter what. That is not the same as
  a mode existing.)
- Explain why a mode is the right statistic for "how many hours do students
  study each night" but useless for "how much money do alumni donate."
  What is the mode actually measuring — the values, or the shape?

## PART 5 — DESIGN YOUR OWN DASHBOARD (10 min)

The project later this unit is a **Privacy-Aware Stats Dashboard**. Sketch on
paper, for a dataset you choose (the clinic visits, the wages, the donations,
or one you invent):

- The one or two numbers you would put at the top, and **why those** and not
  others.
- What you would *never* show, and what harm it could do.
- One sentence a reader could learn from your dashboard that they could not
  learn from your single headline number.

Keep this sketch. You will build it in the project labs.

## PART 6 — JOURNAL + PUSH (last 10 min)

```bash
cd ~/compmath-lab
touch journal-u3l04.md
```

Answer in the file, 2-3 sentences each:

- Which of the five statistics has the most dangerous blind spot, and what
  real decision could go wrong because of it?
- Explain the median's blind spot to someone who has never taken a stats
  class, using the 242.38 / 242.76 numbers.
- Your Part 5 dashboard sketch: name the number you chose and the harm you
  avoided by not choosing the other one.

```bash
git add journal-u3l04.md
git commit -m "U3 L04 reflection journal: blind spots of each statistic"
git push
```

- **Asked for a username/password?** GitHub username + Personal Access Token
  (PAT) — never your GitHub password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 3 blind-spot table, filled in
2. your Part 5 dashboard sketch
3. your Part 6 journal file open
4. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

Early finishers: find a real statistic published somewhere in the news this
week. Write down the number, the source, and — using the Part 3 table — what
it is blind to.
