# U3 L12 — Lab: Anonymization — Suppression and Generalization — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal with the lab open beside this sheet. Change each ☐ to ☑ as you finish that step. Everything you record comes off your own screen — nothing on this sheet gives you the answer, and the sheet is checked against your output, not against an answer key.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm where you are, then copy the path it prints:

pwd ______________________

☐  Load data/u3_project_dataset.csv with the PART 0 loader that skips the comment line. Record the member count and the column list:

members ______________________

columns ______________________

## 1: The target — k-anonymity

☐  Type k_value(rows, fields) from PART 1 exactly as given, then run the combos loop. Fill the table from your own output:

| Fields published | groups | k | unique people |
| --- | --- | --- | --- |
| Zip_Code | __________ | __________ | __________ |
| Age | __________ | __________ | __________ |
| Age + Zip_Code | __________ | __________ | __________ |
| City + Age + Zip_Code | __________ | __________ | __________ |
| Age + City + Membership_Tier | __________ | __________ | __________ |


☐  Name the two columns whose combination gives the smallest k in your table, and write that k:

smallest-k pair ______________________

k for that pair ______________________

☐  Neither of those columns is a name. Explain in one sentence what that says about deleting a name column and calling the file anonymous:

_____________________________________________________________________

## 2: Technique 1 — suppression

☐  Set MIN_K = 5 and type suppress(rows, field, min_k=MIN_K) from PART 2, then run the four-field loop. Fill the table:

| Grouped by | keep | drop | k_now |
| --- | --- | --- | --- |
| City | __________ | __________ | __________ |
| Membership_Tier | __________ | __________ | __________ |
| Zip_Code | __________ | __________ | __________ |
| Age | __________ | __________ | __________ |


☐  The Zip_Code line printed a k that is not a count of people. Record it, then explain in one line why suppression produced it:

_____________________________________________________________________

☐  Run the threshold loop over 3, 5 and 10 on Zip_Code. Fill the table:

| Rule | keep | drop |
| --- | --- | --- |
| k >= 3 | __________ | __________ |
| k >= 5 | __________ | __________ |
| k >= 10 | __________ | __________ |

☐  Which rule leaves you with too little to analyze? And what does a near-total drop on one column tell you about that column — where should it have been fixed instead of filtered row by row?

_____________________________________________________________________

## 3: Technique 2 — generalization

☐  Type age_band(age_str, width=10) and zip_prefix(zip_str, digits=3) exactly as given, then call age_band("34"):

age_band("34") = ______________________

☐  Build the banded list, run both print statements, then the four-combination loop. Fill the table:

| Published fields | groups | k | unique |
| --- | --- | --- | --- |
| Age_Band | __________ | __________ | __________ |
| Zip3 | __________ | __________ | __________ |
| Age_Band + City | __________ | __________ | __________ |
| Age_Band + City + Membership_Tier | __________ | __________ | __________ |


☐  Adding a column moved k the wrong way here. Which combinations reached k >= 5, and what does that say about publishing more columns?

_____________________________________________________________________

☐  Rerun with width=15, then width=25, then width=5. Fill the table:

| Band width | k, band alone | k, band + Membership_Tier |
| --- | --- | --- |
| 5 | __________ | __________ |
| 10 | __________ | __________ |
| 15 | __________ | __________ |
| 25 | __________ | __________ |


☐  Did the 5-year band raise k or lower it against the 10-year band, and why is a narrower band less private? Use the words accuracy and privacy:

k direction ______________________

_____________________________________________________________________

☐  Print the crosstab of Zip3 against City, count the distinct Zip3 values and the cities each one maps to, then say in one sentence what keeping both columns means:

distinct Zip3 values ______________________

cities per Zip3 ______________________

_____________________________________________________________________

## 4: Your anonymization pass

☐  Write anonymize.py in your repo with DIRECT_IDENTIFIERS, QUASI_IDENTIFIERS, MIN_K and the functions load, drop_direct, generalize, k_value from PART 4. Record the direct identifiers you listed:

DIRECT_IDENTIFIERS ______________________

☐  Run it end to end on ["Age", "Zip_Code", "City"]. Record before and after:

k before ______________________

k after ______________________

unique people still exposed after ______________________

☐  Prove no direct identifier survives by printing the columns left in the output:

_____________________________________________________________________

☐  Write anonymization_report.md with the four required items. Draft the one-sentence accuracy cost of each technique, suppression first and generalization second:

_____________________________________________________________________

☐  Record your age_width and zip_digits, the k you measured at those settings, and justify that pair from the measured k values rather than from taste:

age_width ______________________

zip_digits ______________________

k at those settings ______________________

_____________________________________________________________________

## 5: The limitation you must state

☐  After banding ages into 10-year groups, name two things you can still say about one member:

first ______________________

second ______________________

☐  Describe how someone could combine the published fields with outside knowledge of a small company in five known cities to re-identify a member:

_____________________________________________________________________

☐  Write one honest sentence on what your anonymized dashboard does and does not protect against, and say why "we removed the names" will not do:

_____________________________________________________________________

## 6: Save and push

☐  git add anonymize.py anonymization_report.md

☐  git commit -m "U3 L12 anonymization pass: suppression, generalization, measured k"

☐  git push   →  Paste the push confirmation line GitHub printed:

_____________________________________________________________________

## 7: Turn in

☐  Screenshot the push confirmation line and submit it to this assignment on Google Classroom.

☐  Put these three numbers in the push message so they can be spot-checked:

k for Age + Zip_Code before anonymization ______________________

k for your best generalized combination ______________________

members still individually identifiable after your pass ______________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
