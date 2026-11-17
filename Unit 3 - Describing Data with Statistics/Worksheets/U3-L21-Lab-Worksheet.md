# U3 L21 — Lab: Outliers — Keep, Report, or Remove — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal, one step at a time. Change each ☐ to ☑ when that step is finished and its blanks are filled. Everything you record comes off your own screen — nothing on this sheet gives you the answer, and the sheet is checked against your output, not an answer key.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm you are in the repo and see the data files:  pwd   then   ls data/   →  Paste both outputs:


_____________________________________________________________________

☐  Start a Python session inside the repo:  python3

## 1: Get the data

☐  Type the two imports and load(path) from PART 0 exactly as written, then run:  rows = load("data/u3_project_dataset.csv")

☐  Type numeric(rows, col) exactly as written, run it on Age, and record what came back:


values returned for Age = ______________________

## 2: Build the fence

☐  Type five_number(values) and iqr_fences(values) from PART 1. Reuse your percentile from U3 L08 and U3 L14 — copy it, do not rewrite it.

☐  Run five_number on Monthly_Visits. Record all five numbers and both fences:


| field | your value |
| --- | --- |
| min | ________________ |
| Q1 | ________________ |
| median | ________________ |
| Q3 | ________________ |
| max | ________________ |
| lower fence | ________________ |
| upper fence | ________________ |

☐  Type outliers(values), then run the PART 1 loop over ["Age", "Monthly_Visits", "Spend_USD"]. Copy n, median and IQR for each column:


| column | n | median | IQR |
| --- | --- | --- | --- |
| Age | ________ | ________ | ________ |
| Monthly_Visits | ________ | ________ | ________ |
| Spend_USD | ________ | ________ | ________ |

☐  Copy the fences and the flagged counts from those same three printed lines. Nothing in these tables comes from expectation — it comes from your run:


| column | lower fence | upper fence | # outliers |
| --- | --- | --- | --- |
| Age | ________ | ________ | ________ |
| Monthly_Visits | ________ | ________ | ________ |
| Spend_USD | ________ | ________ | ________ |

## 3: The uncomfortable part

☐  Look at your Monthly_Visits row. Record how many values the fence flagged:


flagged values = ______________________

☐  Print those flagged values, sorted. Record the single value they all share:


flagged value = ______________________

☐  Describe that column's shape — where the bulk sits, where the gap is, and why the fence lands in the gap instead of somewhere in the middle of the data:


_____________________________________________________________________

☐  Type stdev_population(values) and high_outliers_2sd(values) from PART 2, then run the comparison loop on ["Monthly_Visits", "Spend_USD"]. Fill in your own counts:


| column | IQR flags | 2-sd-above-mean flags |
| --- | --- | --- |
| Monthly_Visits | ________ | ________ |
| Spend_USD | ________ | ________ |

☐  Explain the disagreement in two sentences, one per rule. Use q3, mean and standard deviation, and say what one enormous value does to each cut-off. Then say when you would trust each rule:


_____________________________________________________________________

## 4: The removal problem

☐  Type mean_of(values) from PART 3, build spend, flagged and kept exactly as the lab does, then run the four print lines. Copy each line's numbers here:


| line printed | your output |
| --- | --- |
| original | ________________ |
| flagged | ________________ |
| kept | ________________ |
| mean moved | ________ % |
| median moved | ________ % |

☐  One flag rule plus one delete has quietly removed a fraction of the rows. Work it out from your n values, and say which statistic moved further:


fraction of rows removed = ______________________    moved further = ______________________

☐  Where did the largest Spend_USD value come from? Using only the numbers in front of you, is it an error? Name the evidence you would need before saying yes:


_____________________________________________________________________

☐  Choose one option by letter:  (a) median as the headline, outlier kept, flags footnoted;  (b) both figures side by side, labelled;  (c) trimmed mean with the trimmed fraction stated.


choice = ______________________

☐  Write the sentence that justifies your choice:


_____________________________________________________________________

☐  Could a reader misread your result as a claim about the typical member? Write the one sentence in your report that stops that reading:


_____________________________________________________________________

## 5: Your own outlier

☐  Run:  grep -n "18500" data/u3_project_dataset.csv   →  Paste the line it printed:


_____________________________________________________________________

☐  Was that value introduced as a plausible member or as a deliberate anomaly? Say which, and quote the part of the line that tells you:


_____________________________________________________________________

☐  The value is real data, not a typo. You can now delete anything that ruins your result — give one concrete situation where an honest analyst would still be wrong to delete:


_____________________________________________________________________

## 6: Save and push

☐  Save the functions you typed into outliers_lab.py in the repo root, then:  git add outliers_lab.py

☐  git commit -m "U3 L21 outlier fences, 2-sd comparison, removal measurement"

☐  git push   →  Paste the push URL GitHub printed:


_____________________________________________________________________

## 7: Turn in

☐  Write the outlier report: five to eight sentences of plain prose, no bullets. Put these figures from your own run in it:


| figure | your value |
| --- | --- |
| Spend_USD upper fence | ________________ |
| flags | ________________ |
| mean before | ________________ |
| mean after | ________________ |
| median before | ________________ |
| median after | ________________ |

☐  Copy your choice letter and your written sentences from the removal and outlier sections into the report. The sentence on when deletion is the wrong call is the graded one.

☐  Post the report to the Classroom assignment with a screenshot of the push confirmation line.

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
