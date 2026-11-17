# U3 L14 — Project Lab 1: Build the Stats Engine — Project Checkpoint Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom, terminal and editor side by side. Change each ☐ to ☑ once that step runs and you have recorded what it did. Every blank here is filled from your own screen — nothing on this sheet gives you an answer.

## 0: Set up

☐  Go to the repo and branch:  cd ~/compmath-u3-stats-lab   then   git checkout -b u3-dashboard

☐  Confirm where you are:  pwd   →  paste the path your shell printed:

_____________________________________________________________________

☐  Create stats_engine.py in the repo root — everything today goes into that one file.

## 1: The loader

☐  Put the import and the comment marker at the top of stats_engine.py:  import csv   and   COMMENT = "#"

☐  Write load(path). It drops blank and comment lines, reads the rest with csv.DictReader, returns a list of dicts, and raises when the file has no data row. Record the error type the guard raises on a file cut down to a comment plus a header:

error raised ______________________

☐  Point load at data/u3_project_dataset.csv and call it. Record what came back:

rows returned ______________________

☐  What does csv.DictReader handle that open().read().split(",") does not? Name the field shape that breaks the naive split:

_____________________________________________________________________

## 2: The statistics

☐  Write mean(values), median(values), percentile(values, p) and stdev(values): a list in, a number out, no prints, no file reads.

☐  Build percentile on position (n - 1) x p, the inclusive method from the L08 lab. Record which standard library quantile method would give different numbers on the same data:

_____________________________________________________________________

☐  Call your median on a list with an odd count, then on one with an even count. What did the even case return that the odd case never can?

_____________________________________________________________________

☐  Write five_number(values) and fill in what it returns for a small list of your own:


| Position | Value |
| --- | --- |
| min | ________________ |
| Q1 | ________________ |
| median | ________________ |
| Q3 | ________________ |
| max | ________________ |

## 3: The outlier fence

☐  Write iqr_fences(values) returning (lower, upper) at 1.5 x IQR below Q1 and above Q3, and outside_fence(values) on top of it.

☐  Call iqr_fences on the twelve-value list in PART 4 of the lab. Record both fences:

lower fence ______________________

upper fence ______________________

☐  The fence flags more values on the real data than you expected. Why does a rule built on the middle 50% sit so far below a long upper tail?

_____________________________________________________________________

## 4: The summary

☐  Write numeric(rows, col) — floats pulled out, junk dropped, no exception escaping — then summarise(rows, col), returning column, n, mean, median, min, max, stdev, iqr, fences, outliers, skew.

☐  Write group_summary(rows, col, by) with a stable sorted order.

☐  Run the PART 3 print loop over Age, Monthly_Visits and Spend_USD. Record the row count from its header line:

members ______________________

☐  Copy your own centre and skew numbers in for each column:


| Column | mean | median | skew |
| --- | --- | --- | --- |
| Age | ________ | ________ | ________ |
| Monthly_Visits | ________ | ________ | ________ |
| Spend_USD | ________ | ________ | ________ |

☐  Same run — spread and the flag count:


| Column | stdev | IQR | outliers |
| --- | --- | --- | --- |
| Age | ________ | ________ | ________ |
| Monthly_Visits | ________ | ________ | ________ |
| Spend_USD | ________ | ________ | ________ |

☐  Which column's outlier list would you trust in a report, and why? Name the column and give one reason:

_____________________________________________________________________

☐  Before you hunt for a bug in the fence, write what you checked to convince yourself the flag count is right:

_____________________________________________________________________

## 5: Assert your engine

☐  Write test_engine() and carry over the known-answer assertions from PART 4 — the tiny inputs, the five-number tuple, the fence bounds, the error-path loop, and the mixed-column check.

☐  Add three assertions of your own against the project data: one for Spend_USD, one for Age, one that proves an outlier is detected. Use the values your own run printed.

☐  Run the file. Record the line test_engine() printed at the end:

______________________

☐  Break one assertion on purpose by changing a constant so the claim is false, rerun, and record what the interpreter raised. Then put the constant back and confirm the pass line returns:

error raised ______________________

☐  Why is the if __name__ == "__main__": guard load-bearing once the dashboard imports this file?

_____________________________________________________________________

☐  median([1, 2, 3, 4]) returns a value that is not in the list. Say when reporting that number is correct and when it would be wrong:

_____________________________________________________________________

## 6: Look ahead

☐  Write one thing this engine is missing that privacy_filter.py will need — something that would force a rewrite of summarise if you noticed it too late:

_____________________________________________________________________

## 7: Checkpoint — what must be on screen before you leave

☐  stats_engine.py open in your editor with every function visible. List them in the order they appear in the file:

_____________________________________________________________________

☐  Terminal scrollback showing the PART 3 summary block for all three columns — header, centre, spread, fences, outlier list and skew for each.

☐  Terminal showing a clean test_engine() run and its pass line, and the failed run you caused and then reverted.

☐  From your own run, ready to state without reading it off this sheet: the mean and median of Spend_USD, the count the fence flagged in it, and whether you stand behind that count.

## 8: Save and push

☐  git add stats_engine.py

☐  git commit -m "U3 L14 stats engine: load, summarise, group, fence, with assertions"

☐  git push -u origin u3-dashboard

☐  Paste the push confirmation line GitHub printed:

_____________________________________________________________________

## 9: Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment.

☐  Your push message must carry all three of these. Fill them in from your run:

mean of Spend_USD ______________________

median of Spend_USD ______________________

values the fence flagged in Spend_USD ______________________

a sentence on whether that count is meaningful ______________________

_____________________________________________________________________

the line test_engine() printed ______________________

☐  Leave the terminal open for a spot-check. Due 11:59 PM.
