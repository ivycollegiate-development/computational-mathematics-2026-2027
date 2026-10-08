# U2 L03 — Worksheet: What Makes a Good Visualization

Names: ___________________________  Date: ____

Exploration day. This sheet is a fill-in companion to the lesson in the repo — you read the directions there and write your answers here. Today your numbers become a picture for the first time.

## Part 1 — Why pictures beat tables

| Question | My answer |
|------------|------------|
| Which took longer to absorb — reading the table or imagining the line? |                                                                      |
| From the table alone, how fast can you find the biggest two-day jump? From a line chart? |                                                                      |
| What does a chart expose that a table only stores? |                                                                      |

Key idea, in your own words: a table stores values; a chart exposes **shape, trend, and outliers**. A chart is also an *argument* — someone chose what to plot.

   _________________________________________________________________________

## Part 2 — Your first plot

Run `import matplotlib.pyplot as plt`, then `plt.plot(days, temps)` and `plt.show()`.

| Question | My answer |
|------------|------------|
| What does `pyplot` do, and why does everyone shorten it to `plt`? |                                                                      |
| Swap the lists: `plt.plot(temps, days)`. What broke, and which list is x and which is y? |                                                                      |
| Add `plt.plot(days, [t + 5 for t in temps])` before `plt.show()`. What happened? |                                                                      |

   _________________________________________________________________________

## Part 3 — Anatomy of a plot

A complete chart has three things. Fill in what each one answers:

| Part of a chart | What question does it answer? |
|------------|------------|
| Title |  |
| X-axis label |  |
| Y-axis label |  |

What did `marker="o"` change? When would you want it, when not?

   _________________________________________________________________________

Why does every axis label carry a unit? What is the chart saying that a bare line could not?

   _________________________________________________________________________

Try `linestyle="--"`. Describe the change in one sentence.

   _________________________________________________________________________

## Part 4 — Plot the real data: study hours

Run the Part 4 code against `u2_dataset1_study_habits.csv` and answer.

| Question | My answer |
|------------|------------|
| Why `scatter` here instead of `plot`? |                                                                      |
| Does the cloud of points lean which way? What does the lean suggest? |                                                                      |
| Where would a point at (1.0, 95) sit? Does it fit the pattern? What is that point called? |                                                                      |

## Part 5 — savefig: make it a turn-in

What does `dpi=150` change, and why does a crisp image matter when someone else grades your chart?

   _________________________________________________________________________

Why must `savefig()` run before (or instead of) `show()` in a script?

   _________________________________________________________________________

## Part 6 — What makes a chart good?

With your table, rank these sins from worst (1) to least-worst (5), one sentence each in your notes:

| Rank | Sin |
|------------|------------|
|  | no title |
|  | no axis labels |
|  | no units |
|  | y-axis starting at a weird number to exaggerate a trend |
|  | rainbow colors on a black background |

Which sin did you rank worst, and why?

   _________________________________________________________________________

## Part 7 — Journal + push

- ☐  `first_plot.py` and `score_vs_hours.png` committed in `~/compmath-u2-data-lab`, `git push` confirmed.

## TURN IN

- ☐  Parts 1–6 complete, including your Part 3 labeled chart and Part 4 scatter.
- ☐  Screenshot to the Classroom assignment by 11:59 PM tonight showing: your Part 3 labeled temperature chart, your Part 4 scatter plot, `ls -lh score_vs_hours.png`, and the successful `git push`.

Keep the terminal open — spot-checks.

Bonus: add Sleep_Hours vs. Test_Score as a second series in a different color with `label=` and `plt.legend()`, save a second PNG.
