# U3 L06 — Lab: Choosing the Right Statistic for the Claim — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal. Change each ☐ to ☑ as you finish that step. Every number you record comes off your own screen — nothing on this sheet gives you the answer, and the sheet is checked against your output.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm where you are:  pwd   →  Path on screen:

_____________________________________________________________________

☐  Load data/u3_wage_comparison.csv as in PART 0 — drop every line starting with #, then build the rows with csv.DictReader. The fields are quoted, "Jordan, Haddad"-style, so never use split(","). The shape is a comment line, a header, then 120 employees in two families, Analyst and Coordinator, 60 each. Record what print(len(rows), "employees") says:

_____________________________________________________________________

☐  Record what print(rows[0]) shows, the first row as a dictionary:

_____________________________________________________________________

☐  Write the wages(family) helper exactly as PART 1 gives it, then build analyst and coord from it.

## 1: The claim under test

☐  Read the memo in PART 1. Its number is the mean. Run the loop over Analyst and Coordinator and fill the table from your own output. The loop prints mean, median, range and stdev — add min, max and the 25th percentile yourself, for example with statistics.quantiles(vals, n=4):

| Statistic | Analyst | Coordinator | The gap |
| --- | --- | --- | --- |
| mean | ________________ | ________________ | ________________ |
| median | ________________ | ________________ | ________________ |
| min | ________________ | ________________ | ________________ |
| max | ________________ | ________________ | ________________ |
| 25th percentile | ________________ | ________________ | ________________ |

☐  The memo's own word for that gap is decisive. Which gap, mean or median, better describes the typical difference between the two roles?

_____________________________________________________________________

☐  By how much does the mean gap overstate the median gap? Record the ratio:

_____________________________________________________________________

☐  Look at the largest salaries, then explain why the mean gap exceeds the median gap:

_____________________________________________________________________

## 2: Find the reason

☐  Run the print lines in PART 2. Record the Analyst top 6 on the first line, and the Coordinator top 6 on the second:

_____________________________________________________________________

_____________________________________________________________________

☐  Record the two over-200k counts:

Analyst over 200k ______________________

Coordinator over 200k ______________________

☐  Each top 6 has a cliff: a few values, then a drop. Record the value each family drops to:

Analyst drops to ______________________

Coordinator drops to ______________________

☐  Restate the claim honestly, twice: is "Analysts earn more" true, and is "the typical Analyst earns $28,000 more" true?

_____________________________________________________________________

_____________________________________________________________________

☐  Check the overlap: compare max(coord) with the Analyst median, and max(analyst) with the Coordinator median. What does that overlap say about what one specific person could earn?

_____________________________________________________________________

## 3: The range and standard deviation

☐  Name the statistic in your Part 1 table that is largest for Analyst, and explain why it tells you almost nothing about a typical Analyst:

_____________________________________________________________________

☐  Record the Analyst standard deviation from the loop output, with the Analyst mean beside it:

stdev ______________________

mean ______________________

☐  Write the honest form of the salary claim as a plus-or-minus sentence, using your own two numbers:

_____________________________________________________________________

☐  Would you put the range in the memo? Answer, then say in one sentence what range shows and what it hides:

_____________________________________________________________________

## 4: Build the honest memo

☐  Create memo_wages.md in the repo root. Memo A keeps the mean gap and the word average.

☐  Write Memo A's claim sentence:

_____________________________________________________________________

☐  Add one sentence naming what that average conceals, and one sentence a skeptical reader should demand before anyone acts on the memo:

_____________________________________________________________________

_____________________________________________________________________

☐  Write Memo B with the median and the spread reported together. Record its headline number:

_____________________________________________________________________

☐  Record the second number you report beside it and why you chose that one. Then name what Memo B can no longer claim that Memo A could:

_____________________________________________________________________

_____________________________________________________________________

## 5: The rules you will use

☐  Write the four rules from PART 5 in your notebook, then restate each one in your own words:


| Rule | In your own words |
| --- | --- |
| 1  Match the statistic to the claim | ______________________ |
| 2  Report the spread with the center | ______________________ |
| 3  Show the extremes when they drive the result | ______________________ |
| 4  Prefer the robust measure when extremes are untrustworthy | ______________________ |


☐  Apply rule 1 to a statistic you have seen in the news: write the sentence as it was published, then rewrite it so the verb and the number agree:

_____________________________________________________________________

_____________________________________________________________________

## 6: Look ahead: the U3 L07 paper check

☐  The next paper check is closed notes and by hand: centers and spread for both families. From memory, write mean, median, min and max for both families, then check them against your Part 1 table and record which one you had wrong:

_____________________________________________________________________

## 7: Save and push

☐  git add memo_wages.md

☐  git commit -m "U3 L06 statistic choice and honest memo for the wage claim"

☐  git push   →  Paste the push confirmation line GitHub printed:

_____________________________________________________________________

## Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment. Put these four numbers in the push message:

mean Analyst ______________________

median Analyst ______________________

mean gap minus median gap ______________________

employees over 200,000 in total ______________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
