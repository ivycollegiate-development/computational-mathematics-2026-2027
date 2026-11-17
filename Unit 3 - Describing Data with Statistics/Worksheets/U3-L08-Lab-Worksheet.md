# U3 L08 — Lab: Percentiles, the Five-Number Summary, and the IQR Fence — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal. Change each ☐ to ☑ as you finish that step. Everything you record here comes off your own screen — nothing on this sheet gives you the answer.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm where you are:  pwd   →  Path on screen:

_____________________________________________________________________

☐  Load the survey file the way PART 0 does: open data/u3_survey_times.csv, drop every line that starts with #, read the rest with csv.DictReader, then build waits as the sorted ints of the Wait_Minutes column.

☐  Run it and record the three numbers it prints:

| What it printed | Your value |
| --- | --- |
| responses | ______________ |
| min wait | ______________ |
| max wait | ______________ |

☐  Create percentiles.py in the lab repo. Every function and print statement in this lab goes into that one file, and you re-run it after each part.

## 1: What a percentile means

☐  In one sentence: what is the 90th percentile of wait times? Say it as a value in the data, not as a percentage of the maximum.

_____________________________________________________________________

☐  Which is bigger? Write the one that is larger:

bigger percentile ______________________

☐  Why must that one be bigger? Answer in terms of position in the sorted list:

_____________________________________________________________________

☐  A percentile is a position, so with 240 sorted values the 90th percentile does not land on a value. Compute its index from k = (n - 1) * p and record k:

k = ______________________

☐  Is k a whole number? What does its fractional part force the function to do?

_____________________________________________________________________

## 2: Compute it yourself

☐  Type the percentile(values, p) function from PART 2 into percentiles.py exactly as written. p is a fraction here — 0.25 for the 25th percentile, 0.90 for the 90th.

☐  Loop over p = 0.10, 0.25, 0.50, 0.75, 0.90 and print each line. Fill in your own output:

| Percentile | Value |
| --- | --- |
| p10 | ______________ |
| p25 | ______________ |
| p50 | ______________ |
| p75 | ______________ |
| p90 | ______________ |

☐  Compare each line against the hand check you did on paper. If p50 disagrees with the median you can read off the sorted list, stop and find your bug before going on.

☐  Why does p50 come out to the median? Look at the formula at p = 0.5 with an even count:

_____________________________________________________________________

☐  Q1, Q2 and Q3 are just p25, p50 and p75. Write Q1 and Q3 from this function:

Q1 = ______________________

Q3 = ______________________

☐  Compare Q1 and Q3 with the paper quartile method from the previous lab. Where do the two methods disagree?

_____________________________________________________________________

☐  Why is there no single right answer for quartiles on a small dataset?

_____________________________________________________________________

## 3: The five-number summary

☐  Build five and labels and print the five lines. Fill in your own output:

| Statistic | Value |
| --- | --- |
| min | ______________ |
| Q1 | ______________ |
| median | ______________ |
| Q3 | ______________ |
| max | ______________ |

☐  Compute iqr = five[3] - five[1] and print it:

IQR = ______________________

☐  Record both fences from the 1.5 * IQR rule:

upper fence = ______________________

lower fence = ______________________

☐  Decide whether the maximum wait is an outlier by the IQR rule. Record the answer and the margin:

outlier by the IQR rule? ______________________

how far past, or how far inside, the fence ______________________ minutes

☐  In one sentence, say why the IQR is the robust measure of spread and the range the fragile one. Count how many values each one depends on.

_____________________________________________________________________

## 4: Reading shape from five numbers

☐  Compute lower_half, upper_half and tails, print both lines, then record the four gaps:

| Gap | Size |
| --- | --- |
| median - Q1 | ______________ |
| Q3 - median | ______________ |
| Q3 to max | ______________ |
| min to Q1 | ______________ |

☐  Take the two symmetry checks off the gaps you just filled in — yes or no for each, and write the pair of gaps that decided it:

| Check | Answer | Gaps that decided it |
| --- | --- | --- |
| middle half symmetric? | __________ | __________ vs __________ |
| tails symmetric? | __________ | __________ vs __________ |

☐  Name the shape of the wait times:

shape (left or right) ______________________

☐  Defend that shape with the two tail gaps you just measured:

_____________________________________________________________________

☐  Do the same four gaps for the donations from the L05 lab. Which way do they point?

donations (left or right) ______________________

☐  Most real-world data points the same way. One sentence on why:

_____________________________________________________________________

## 5: How the summary compares datasets

☐  Loop over the distinct values of the Day_Of_Week column. For each group build a fresh five and print one line: min, Q1, med, Q3, max. Keep the group label with your numbers in this table:

| Group | Median | IQR |
| --- | --- | --- |
| group 1 | __________ | __________ |
| group 2 | __________ | __________ |
| group 3 | __________ | __________ |
| group 4 | __________ | __________ |
| group 5 | __________ | __________ |

☐  Do any two groups look meaningfully different? Name them and say how:

_____________________________________________________________________

☐  Compare the spread inside one group with the spread across all the groups together:

_____________________________________________________________________

☐  A single overall five-number summary hides the per-group variation. Say what a dashboard loses if it shows only the whole:

_____________________________________________________________________

## 6: Save and push

☐  git add percentiles.py

☐  git commit -m "U3 L08 percentiles, five-number summary, and distribution shape"

☐  git push   →  Paste the push URL GitHub printed:

_____________________________________________________________________

## 7: Turn in

☐  Put these four numbers in the push message so they can be spot-checked:

25th percentile of wait times ______________________

median wait (p50) ______________________

IQR ______________________

upper outlier fence ______________________

☐  Post a screenshot of the push confirmation line to this Classroom assignment.

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
