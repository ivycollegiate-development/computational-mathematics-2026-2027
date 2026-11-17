# U3 L09 — Lab: Misleading Statistics and the Truncated Axis — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom, in order. Change each ☐ to ☑ as you finish that step, and record only what your own terminal prints. Nothing on this sheet gives you an answer, and the sheet is checked against your screen, not against a key.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm where you are:  pwd   →  Path on screen:

_____________________________________________________________________

☐  Load data/u3_wage_comparison.csv the way PART 0 does: drop every line that starts with #, read the rest with csv.DictReader, then build analyst and coord through wages(family) on Job_Family and the Annual_USD column. Run it and fill the table from the loaded line.

| List | Count |
| --- | --- |
| analyst | ________________ |
| coord | ________________ |


## 1: The honest version first

☐  Run the PART 1 loop for both lists. Fill the table with your own output, and keep the min and max it prints for each group in view — later parts need them.

| Group | Mean | Median |
| --- | --- | --- |
| Analyst | ________________ | ________________ |
| Coordinator | ________________ | ________________ |


☐  Write the honest claim about the two families in one sentence, then name the two numbers in your table that agree on it:

_____________________________________________________________________

## 2A: Pick the flattering statistic

☐  Run the two-print gap block in PART 2A. Record both gaps:

mean gap ______________________     median gap ______________________

☐  Write the sentence a dishonest analyst would publish, built on whichever gap sounds strongest:

_____________________________________________________________________

☐  Write the honest sentence that quotes both gaps and says they answer different questions:

_____________________________________________________________________

## 2B: Truncate the axis

☐  Build truncated by keeping the Analysts at or above 80,000, run the three prints in PART 2B, then record them:

Analysts kept ______________________     total Analysts ______________________

range of the kept list ______________________     full range ______________________

☐  Sketch two bar charts of the same Analyst salaries, one with the y-axis starting at 0 and one starting at 80,000. Photograph both for the turn-in.

☐  Which one would you show to argue for a raise, which one is honest about spread, and what baseline rule is the second one obeying?

_____________________________________________________________________

## 2C: Cherry-pick the subgroup

☐  Run the PART 2C block, which builds exp and west, and record the four numbers it prints:

West, n __________________     West mean ______________________

All Analysts, n ___________     All Analysts mean ______________________

☐  Write the sentence that reports only the West figure, the way a cherry-picker would:

_____________________________________________________________________

☐  Is that sentence false? Name exactly what is misleading about it:

_____________________________________________________________________

## 2D: Let one value do the work

☐  Run the top-earner block in PART 2D and record the two means and their difference:

with the top earner ______________     without it ______________     difference ______________


☐  Filter to v <= 300000 exactly as PART 2D does, run that block, and fill the table from your own output:

| Set | Mean | Median |
| --- | --- | --- |
| all Analysts | ________________ | ________________ |
| everyone at or below 300,000 | ________________ | ________________ |


☐  One center barely moved and the other moved a long way. Which is which, and what does that mean for quoting a single number as a typical salary here?

_____________________________________________________________________

## 3: The five-number defense

☐  Type the percentile(values, p) function from PART 3 exactly as written, run the five-number loop for both groups, and fill the table:

| Group | Q1 | Median | Q3 |
| --- | --- | --- | --- |
| Analyst | ___________ | ___________ | ___________ |
| Coordinator | ___________ | ___________ | ___________ |


☐  Compare the Analyst median you got with the Coordinator max you got. Write the overlap sentence you would defend out loud:

_____________________________________________________________________

☐  Which Part 2 trick does the max in a five-number summary make hardest to pull off, and why?

_____________________________________________________________________

## 4: Rebuild the claim honestly

☐  Create honest_wages.md in the lab repo. Open it with the headline claim in one sentence, on the median gap and not the mean gap:

_____________________________________________________________________

☐  Add the five-number summary for both groups, one sentence on the overlap, and one sentence naming the sample size and where the data came from.

☐  Open a limitations section and give two things this data cannot tell you:


limitation 1 ______________________     limitation 2 ______________________


☐  Add a second section titled What I deliberately did not do and list the Part 2 tricks you declined, one line each:

_____________________________________________________________________

_____________________________________________________________________

## 5: The ethics, in one paragraph

☐  A statistic is technically accurate but is used to deceive. Is that lying? Give your reason:

_____________________________________________________________________

☐  Say who is responsible — the analyst, the person who publishes the chart, or the reader — and defend the choice with one specific example from this lab:

_____________________________________________________________________

## Save and push

☐  git add honest_wages.md

☐  git commit -m "U3 L09 honest wage memo, with limitations and rejected tricks"

☐  git push   →  Paste the push URL GitHub printed:

_____________________________________________________________________

## Turn in

☐  Screenshot the push confirmation line and submit it to this assignment on Google Classroom.

☐  Put these three numbers in the push message, taken from your own output:

mean gap between families ______________________

median gap between families ______________________

highest-paid Coordinator ______________________


☐  Keep the terminal open for a spot-check. Due 11:59 PM.
