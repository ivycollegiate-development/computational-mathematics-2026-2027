# U3 L10 — Lab: PII — What Makes Data Identifying — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal and in privacy_audit.md. Change every box to ☑ as you finish that step. Everything you record here comes off your own screen — nothing on this sheet gives you the answer, and the sheet is checked against your output, not against an answer key.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm where you are:  pwd   →  Path on screen:

_____________________________________________________________________

☐  Load data/u3_clinic_visits.csv with csv.DictReader, dropping every line that starts with #, exactly as in PART 0 of the lab. Record the row count it prints:


______________________ visits

☐  Record the column list it prints, in order:

_____________________________________________________________________

☐  Record the first row dictionary exactly as printed:

_____________________________________________________________________

☐  Run the naive split on the first data row, lines[1] and not the header. Record both counts:

naive field count ______________________

correct field count ______________________

☐  Record what each method calls Age — copy the repr output, quotes included:

naive[2] ______________________    rows[0]["Age"] ______________________

☐  No exception was raised, yet the analysis is wrong. Name the column that gets shifted and what it lands on:

_____________________________________________________________________

## 1: The three tiers of identifying information

☐  Classify every column. One tier per row: direct identifier, quasi-identifier, sensitive, or non-identifying.

| Column | Tier | The one fact that decided it |
| --- | --- | --- |
| Patient_ID | ______________ | ______________ |
| Name | ______________ | ______________ |
| Age | ______________ | ______________ |
| Visit_Date | ______________ | ______________ |
| Condition | ______________ | ______________ |
| Zip_Code | ______________ | ______________ |
| Visit_Count | ______________ | ______________ |
| Insurance_Plan | ______________ | ______________ |

☐  State the key idea of the lesson about a single column versus a combination of columns:

_____________________________________________________________________

## 2: The direct audit

☐  Run the per-column loop over rows[0].keys() and copy the three printed values for every column into the table. Do not skip a row.

| Column | distinct | sample (as printed) |
| --- | --- | --- |
| Patient_ID | ______________ | ______________ |
| Name | ______________ | ______________ |
| Age | ______________ | ______________ |
| Visit_Date | ______________ | ______________ |
| Condition | ______________ | ______________ |
| Zip_Code | ______________ | ______________ |
| Visit_Count | ______________ | ______________ |
| Insurance_Plan | ______________ | ______________ |

☐  Which column has as many distinct values as the file has rows, and what does that make it, even though it is just a code?

_____________________________________________________________________

☐  Record the distinct count for Name, then say why it is smaller than the row count:

distinct names ______________________

_____________________________________________________________________

☐  Name plus a date usually pins one visit exactly. Which count above proves that, and how?

_____________________________________________________________________

## 3: The reconciliation problem

☐  Build key from Name, Visit_Date and Condition, then print how many combinations are distinct. Fill in your own numbers:

distinct combinations ______________________  of  ______________________  rows

☐  If that count equals the row count, what has the combination done with no names in it at all?

_____________________________________________________________________

☐  Play the weaker attacker: build qkey from Age and Zip_Code. Record both printed numbers:

distinct Age+Zip pairs ______________________

pairs appearing exactly once ______________________

☐  Write the sentence the lesson asks for — is removing the name column enough to make this file anonymous?

_____________________________________________________________________

☐  Where does an attacker's Age+Zip lookup come from, given a hospital already holds both columns for its own patients?

_____________________________________________________________________

## 4: The cell-size problem

☐  Count Condition with Counter, sort ascending, run the loop that flags small cells. List every flagged condition and the count next to it:

| Condition (flagged) | count | flag text printed |
| --- | --- | --- |
| ______________________ | ______________ | ______________ |
| ______________________ | ______________ | ______________ |
| ______________________ | ______________ | ______________ |
| ______________________ | ______________ | ______________ |

☐  Record the smallest cell in the file and the condition it belongs to:

smallest cell ______________________

condition ______________________

☐  Publishing a cell that size tells the world something specific. Write what it tells them, and why a small clinic makes it worse:

_____________________________________________________________________

☐  Write the suppression threshold you would pick, then defend the number:

threshold ______________________

_____________________________________________________________________

## 5: The privacy filter spec

☐  Copy the privacy_gate skeleton into privacy_audit.md — read it, do not run it yet. Record the value of MIN_CELL:

MIN_CELL ______________________

☐  List the four things the filter must do, in the order the lesson gives them:

_____________________________________________________________________

☐  What does privacy_gate return, and what is each piece of it?

_____________________________________________________________________

☐  Why return a tuple rather than a plain boolean? Name the thing a boolean cannot carry:

_____________________________________________________________________

☐  Why must the gate come before the chart instead of a review at the end? Say what a chart library does when you hand it bad data:

_____________________________________________________________________

☐  Add your own requirement for a quasi-identifier — suppress it, generalize it (age 66 becomes 65+), or drop it. Pick one and defend it:

_____________________________________________________________________

☐  Check privacy_audit.md holds the filled tier table plus your answers from sections 2, 3 and 4 and these requirements. Missing part:

_____________________________________________________________________

## Save and push

☐  git add privacy_audit.md

☐  git commit -m "U3 L10 PII audit of clinic visits, three tiers, and privacy gate spec"

☐  git push   →  Paste the push confirmation line GitHub printed:

_____________________________________________________________________

## Turn in

☐  Post a screenshot of the push confirmation line to the U3 L10 assignment on Google Classroom.

☐  Put these three numbers in the push message, taken from your own run:

distinct Name+Date+Condition combinations ______________________

conditions with fewer than 5 patients ______________________

columns in the file ______________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
