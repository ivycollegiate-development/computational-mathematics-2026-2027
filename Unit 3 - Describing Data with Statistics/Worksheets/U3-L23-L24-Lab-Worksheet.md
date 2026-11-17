# U3 L23+L24 — Lab: A Statistics Library Others Can Trust + Winter Break Field Notes — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Two lessons, one sheet: Part A is the statslib lab, Part B is the break launch. Work top to bottom from your own terminal and change each ☐ to ☑ as you finish that step. Every number here comes off your own screen or your own paper — nothing on this sheet gives you the answer, and the sheet is checked against your output, not against a key.


## 0: Set up

☐  Open the terminal, go to your Unit 3 lab folder with  cd ~/compmath-u3-stats-lab  then confirm with pwd and record the path:

_____________________________________________________________________

☐  Build the module file, paste the one-line module docstring the lab gives you into it, and record its name:

module file name = ______________________

## 1: The contract, Part A

☐  Fill the contract table from memory, then check it against the lab:

| Function | Arguments | Returns |
| --- | --- | --- |
| mean | ____________ | ____________ |
| median | ____________ | ____________ |
| mode | ____________ | ____________ |
| stdev | ____________ | ____________ |
| percentile | ____________ | ____________ |
| five_number | ____________ | ____________ |
| iqr_fences | ____________ | ____________ |
| outliers | ____________ | ____________ |


☐  Rule 4 is a decision, not a fact. Record the choice you made and defend it in one sentence, in terms of what this dataset actually is:

standard deviation convention = ______________________

divides by = ______________________

_____________________________________________________________________


## 2: The core, with one input guard

☐  Write the shared check function as given, record what it hands back on good input, and record the line that is now first in every function:

returns = ______________________

first line of each function = ______________________

☐  Record the message it raises for each kind of bad input. Run each one; do not copy from the lab:

| Bad input | Message your code printed |
| --- | --- |
| values is None | ________________________ |
| a non-numeric element | ________________________ |
| an empty sequence | ________________________ |


## 3: The functions and the tests

☐  Paste the six functions from the earlier labs, add the guard line to each, and name the two pieces of this section that are new:

new function = ______________________

new check inside percentile = ______________________

☐  Record your counts from the first full run, then the first assertion that failed and which side you changed:

assertions written = ______________________

assertions passed = ______________________

☐  Run your stdev on a one-value list. Record the result, then use the rule line to say why the tests sit at the bottom of the module and what the guard prevents when another file imports it:

stdev of one value = ______________________

_____________________________________________________________________


## 4: Honest errors

☐  Write the error-showing helper and the six-bad-call block, run it, and fill the table from what your terminal printed:

| Bad call | What printed | Clear message? |
| --- | --- | --- |
| mean([]) | ________________ | ______ |
| mean([1, "abc"]) | ________________ | ______ |
| median(None) | ________________ | ______ |
| percentile([1, 2, 3], 1.5) | ________________ | ______ |
| percentile([1, 2, 3], -0.5) | ________________ | ______ |
| five_number([]) | ________________ | ______ |


☐  Which call produced a traceback instead of your exception? Record the call you fixed and rewrite one message so it names the problem:

call fixed = ______________________

_____________________________________________________________________

☐  One sentence on why returning None on bad input is worse for a caller than raising:

_____________________________________________________________________

## 5: The report

☐  Write the report function and run it on the donations data. Paste the first four lines of output:

_____________________________________________________________________

☐  Run it on the project spend column. Record one line of output and the outlier count:

spend column = ______________________

outlier count = ______________________

☐  The report shows a mean far above the median, and a standard deviation most readers will ignore. Write the line you would add so nobody quotes the mean as typical:

_____________________________________________________________________

☐  Your outlier list holds ordinary values as well as extreme ones. Decide what the report should do about that, and defend it in one sentence:

_____________________________________________________________________


## 6: Document it

☐  Answer the docstring questions for a stranger who has never seen your code:

what this module computes = ______________________

population or sample = ______________________

percentile scale = ______________________

behaviour on bad input = ______________________

mode on a tie = ______________________

☐  Ask Python for the docstring of your stdev, record the first line it prints, and say whether the code does what the line claims:

_____________________________________________________________________

## 7: Field notes plan, Part B

☐  This part is paper, not code: no laptop over the break, and the minimum is 21 values. Pick one number you actually live with, not a course average, and say how you will measure it so past-you cannot change the definition halfway:

the number I will track = ______________________

_____________________________________________________________________

☐  Be honest about collection. Record your rate and the total it gives you:

days per week I can collect = ______________________

values over the break = ______________________

☐  Design the paper table now. Three columns, and the third is the one you will thank yourself for:

| Column | What goes in it | Why it matters |
| --- | --- | --- |
| date | __________________ | __________________ |
| value | __________________ | __________________ |
| context | __________________ | __________________ |


☐  Write the four hand computations in the order you will do them, and the one you must show in full so a sorting mistake is visible:

_____________________________________________________________________

☐  Fill the work table with the formula you will use, and leave the value column for the pencil:

| Quantity | Formula you will use | Your value |
| --- | --- | --- |
| n | ____________ | __________ |
| mean | ____________ | __________ |
| median | ____________ | __________ |
| min and max | ____________ | __________ |
| range | ____________ | __________ |
| q1 (write k) | ____________ | __________ |
| q3 (write k) | ____________ | __________ |
| IQR | ____________ | __________ |
| lower fence | ____________ | __________ |
| upper fence | ____________ | __________ |
| outliers | ____________ | __________ |


☐  You will judge every outlier at the table, so write the two possible verdicts on the first line. On the second, draft the one-sentence claim you are aiming for, naming two numbers:

_____________________________________________________________________

_____________________________________________________________________

☐  Privacy check: could a classmate work out who the table describes, and what would you change to keep the story but lose the person?

_____________________________________________________________________


## 8: Save and push

☐  git add statslib.py   (add the three report outputs you pasted)

☐  git commit -m "U3 L23 statslib module with tests, honest errors, report"

☐  git push   →  Paste the push URL GitHub printed:

_____________________________________________________________________

☐  Leave any still-failing test in the file with a comment saying what you think is wrong. Record that comment here:

_____________________________________________________________________


## 9: Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment.

☐  Put your standard deviation decision, its reason, and your test count in the post:

decision = ______________________

assertions passed = ______________________

_____________________________________________________________________

☐  Paste the line you would add to stop the mean being read as typical, and state what your report does about ordinary values in the outlier list:

_____________________________________________________________________

_____________________________________________________________________

☐  Name one test that passed when you did not expect it, and say which of the two explanations it is:

_____________________________________________________________________

☐  Part B is one photo of the paper pages: table, five numbers, five-number summary, outliers, one-sentence claim, privacy fix. Record what the photo will contain:

_____________________________________________________________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
