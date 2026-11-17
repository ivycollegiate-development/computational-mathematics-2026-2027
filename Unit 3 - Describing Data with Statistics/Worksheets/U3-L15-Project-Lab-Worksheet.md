# U3 L15 — Project Lab 2: The Privacy Filter — Project Checkpoint Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom at your own terminal, building the files as you go. Change each ☐ to ☑ when that step is finished on screen. Everything you write here comes off your own run — nothing on this sheet gives you the answer, and every claim you make will be run in front of you.

## 0: Set up

☐  cd ~/compmath-u3-stats-lab   then   git checkout u3-dashboard   and confirm with git branch --show-current

☐  Create privacy_filter.py with yesterday's import at the top:  from stats_engine import load, summarise, numeric

☐  Load the project data and print the row count:  rows = load("data/u3_project_dataset.csv")

rows loaded = ______________________

☐  Split the files before writing any check: every def and constant in privacy_filter.py; every block that loads data and prints in demo_gate.py, inside if __name__ == "__main__":

## 1: The rules

☐  Write DIRECT_IDENTIFIERS, QUASI_IDENTIFIERS, SENSITIVE and MIN_K. Column names only, no values.

☐  Make sure the direct identifiers catch codes as well as names, then record how many column names are in each set and one name from each:

| Set | How many names | One name in it |
| --- | --- | --- |
| DIRECT_IDENTIFIERS | ________ | ____________ |
| QUASI_IDENTIFIERS | ________ | ____________ |
| SENSITIVE | ________ | ____________ |


## 2: Check one — identifiers

☐  Write check_identifiers(rows) so it returns the problem list plus the quasi-identifier columns, with the columns sorted.

☐  Run it on the loaded rows and write out every problem line, exactly as printed:

| # | Line your function printed |
| --- | --- |
| 1 | ____________________________ |
| 2 | ____________________________ |
| 3 | ____________________________ |

quasi-identifiers the same call returned = ______________________

☐  Those problems each name a column, so the list alone is already useful. Say what the caller needs the quasi list for, and what a caller holding only problems would get wrong:

_____________________________________________________________________


## 3: Check two — k-anonymity

☐  Write k_value(rows, fields) and check_k(rows, published_fields, min_k=MIN_K) using Counter over the tuple of field values.

☐  Run the five field combinations from the lab and fill the table from your own output:

| Published fields | k | PASS or BLOCK |
| --- | --- | --- |
| ["Age"] | ________ | ____________ |
| ["Age", "Zip_Code"] | ________ | ____________ |
| ["City"] | ________ | ____________ |
| ["Membership_Tier"] | ________ | ____________ |
| ["Age", "City", "Membership_Tier"] | ________ | ____________ |

☐  Two of those rows disagree even though both fields are just a number or a place. Explain the difference by group size, then say what one row with a count of one does to the whole dataset:

_____________________________________________________________________


## 4: Check three — small cells

☐  Write check_small_cells(rows, group_col, min_k=MIN_K) so it reports every group below the threshold, sorted by group name.

☐  Run it on the three groupings from the lab and record how many problems each returned:

| Group column | Problems returned |
| --- | --- |
| Zip_Code | ________________ |
| City | ________________ |
| Membership_Tier | ________________ |

☐  Your charts group by City and Membership_Tier. Read the two counts you just wrote: if either grouping came back clean here, does that make it safe on its own? Name what this check cannot see that the k check can:

_____________________________________________________________________


## 5: The gate

☐  Write privacy_gate(rows, published_fields, group_cols, min_k=MIN_K) so it calls all three checks and returns (ok, problems, warnings), with describe_result beside it.

☐  Run privacy_gate on an empty row list and record what it returns, then run it on the loaded rows:

ok = ______________________

☐  Your gate reports warnings without setting ok to False. Explain why, then say what happens to a correctly anonymized dataset if you change that and make warnings block:

_____________________________________________________________________


## 6: The fail-closed demo

☐  Write anonymize(rows, age_width=15) in privacy_filter.py: it drops the identifier and date columns and replaces Age with a band string. Run it on the loaded rows:

| anonymize result | Columns |
| --- | --- |
| removed | ____________________________ |
| surviving | ____________________________ |

☐  On the filtered rows, record both k values the demo prints:

k over ["Age"] = ______________________

k over ["Age", "City"] = ______________________

☐  Rerun at each band width and fill the table:

| age_width | k (Age alone) | k (Age + City) | rows still unique |
| --- | --- | --- | --- |
| 5 | ________ | ________ | ________ |
| 10 | ________ | ________ | ________ |
| 15 | ________ | ________ | ________ |
| 25 | ________ | ________ | ________ |
| 30 | ________ | ________ | ________ |

☐  State the decision your filter makes — which fields you publish, which you drop, and whether you suppressed rows — and defend it against the band-width table you just filled:

_____________________________________________________________________


☐  Run the gate on the raw rows with ["Age", "Zip_Code"] published and ["Zip_Code"] as the group column, then record what came back:

ok = ______________________

problems listed = ______________________

☐  Now run it on the filtered rows with ["Age", "City"] as published fields and read the result before you defend it. Write what the gate decided and why, naming the combination:

_____________________________________________________________________


## 7: The wiring

☐  Write publish(rows, draw) so the gate runs first and draw is called only when ok is True, then run it on the filtered rows and on the raw rows and record the return each time:

filtered rows = ______________________

raw rows = ______________________

## 8: Checkpoint — what must exist on screen before you leave

☐  privacy_filter.py holds check_identifiers, k_value, check_k, check_small_cells, privacy_gate, describe_result, anonymize and publish.

☐  python3 -c "import privacy_filter" prints nothing at all — no demo output, no traceback.

☐  python3 demo_gate.py runs top to bottom with no error, and you can point at every printed line.

☐  You can show the pair on demand: the same gate, run once on the filtered rows and once on the raw rows, with both outcomes on screen.

☐  Fill the summary table from a fresh run of each case, before you commit:

| Rows | Published fields | ok | Problems |
| --- | --- | --- | --- |
| filtered | ["Age"] | ________ | ________ |
| raw | ["Age", "Zip_Code"] | ________ | ________ |
| filtered | ["Age", "City"] | ________ | ________ |


## 9: Save and push

☐  git add privacy_filter.py demo_gate.py

☐  git commit -m "U3 L15 privacy filter: identifier, k-anonymity, and small-cell gates, fail-closed"

☐  git push   →  paste the push line GitHub printed:

_____________________________________________________________________


## 10: Turn in

☐  Screenshot the push confirmation line and post it to the Classroom assignment.

☐  Put all five items in the push message. Record them here first:

| Item | Your value |
| --- | --- |
| problems on the raw dataset | ________________ |
| k over ["Age"] after filtering | ________________ |
| result line, safe dataset | ________________ |
| result line, raw dataset | ________________ |
| combination that still blocks | ________________ |

☐  Keep the terminal open and be ready to run any of the three cases. Due 11:59 PM.
