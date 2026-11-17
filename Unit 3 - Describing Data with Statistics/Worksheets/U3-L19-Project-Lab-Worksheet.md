# U3 L19 — Project Lab 4: Fix the Review Findings — Project Checkpoint Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal with dashboard.py open beside this sheet. Change each ☐ to ☑ as you finish that step. Every number you record comes off your own screen — nothing here gives you the answer, and the sheet is checked against your running dashboard.


## 0: Set up

☐  Go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Make the fix branch, or keep your L17 branch if you still have one:  git checkout -b u3-dashboard-fix   →  branch you are on:

_____________________________________________________________________

☐  Confirm the recent history:  git log --oneline | head -3

_____________________________________________________________________

☐  Prove the file runs before you touch it:  python3 dashboard.py   →  what happened:

_____________________________________________________________________

☐  Tag the untouched state and confirm it:  git branch before-fixes   then   git branch --list before-fixes

## 1: Triage the findings

☐  Re-open your review issue and take only the rows you marked Fix now. Target count = ______________

☐  Finding 1, as the specific thing that is wrong:

_____________________________________________________________________

finding 1 now = ______________________

finding 1 after = ______________________

finding 1 evidence that will change = ______________________

☐  Finding 2. A finding with no measurable after line is not a fix:

finding 2 now = ______________________

finding 2 after = ______________________

finding 2 evidence that will change = ______________________

## 2: Fix each one, in its own commit

☐  Make the smallest edit that fixes the actual problem. Nothing else in the same pass.

☐  Commit that finding, not that file. Message you used:

_____________________________________________________________________

☐  Repeat for the next finding. Two records: commits so far = ______________  and, for your first fix, before = ______________  after = ______________

☐  Park anything unrelated on a Minor list instead of fixing it now. What you parked:

_____________________________________________________________________

## 3: The three fixes that usually apply

☐  Fix A, the histogram. Run the current 20-bin Spend_USD chart and say where the bars pile up:

_____________________________________________________________________

☐  Apply math.log10 in place of numpy, keep only values above zero, rerun. X-axis label you set:

_____________________________________________________________________

☐  Two counts: values your v > 0 filter dropped = ______________  and members your caption shows, of how many = ______________

☐  Print the bin counts again. Busiest bin = ______________________

☐  Fix B, the titles. A title that does not name its statistic, exactly as it appears now:

_____________________________________________________________________

☐  Fix C, the gate. The early return in check_k that passes on an empty published_fields:

_____________________________________________________________________

☐  Two counts: columns your four charts group by = ______________  and columns in the gate's group_cols = ______________

## 4: Re-test the gate

☐  Point the gate at two identifying columns:  sed -i.bak 's/PUBLISHED_FIELDS = ["Age"]/PUBLISHED_FIELDS = ["Age", "City"]/' dashboard.py

☐  Run it:  python3 dashboard.py   →  gate output:

_____________________________________________________________________

☐  Put it back and run it again:  sed -i.bak 's/PUBLISHED_FIELDS = ["Age", "City"]/PUBLISHED_FIELDS = ["Age"]/' dashboard.py   then   python3 dashboard.py   →  gate output:

_____________________________________________________________________

☐  Verdict: did the gate still block on Age + City? The number that proves it:

_____________________________________________________________________

☐  If it passed when it should have blocked, undo the last commit. Hash you undid = ______________

## 5: Your before-and-after table

☐  One row per fix you committed. Re-test result is what you saw the second time you ran it.

| Finding | Fix applied | Re-test result |
| --- | --- | --- |
| ______________ | ______________ | ______________ |
| ______________ | ______________ | ______________ |
| ______________ | ______________ | ______________ |
| ______________ | ______________ | ______________ |


## 6: Project checkpoint

☐  dashboard.py finishes with no traceback. Last line it prints:

_____________________________________________________________________

☐  Two counts: chart titles that name their statistic = ______________  and commits above before-fixes = ______________

☐  The histogram sits on a log x-axis, the axis says so, and the caption states how many members are shown and why any are missing:

_____________________________________________________________________

☐  The gate still blocks Age + City. Final k = ______________   MIN_K = ______________

☐  Rows in the section 5 table with a re-test result = ______________________

☐  None of those items leaves this room unproven. Show me the terminal if one does.

## 7: Save and push

☐  git add -A

☐  git commit -m "U3 L19: addressed N review findings with before/after evidence"   →  your N = ____________

☐  git push   →  paste the push URL GitHub printed:

_____________________________________________________________________

## 8: Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment.

☐  Number of findings you fixed:

_____________________________________________________________________

☐  Before gate output, pasted:

_____________________________________________________________________

☐  After gate output, pasted:

_____________________________________________________________________

☐  Final k = ______________________   MIN_K = ______________________

☐  One finding you pushed back on, with the number that justifies the push-back:

_____________________________________________________________________

☐  One finding you traded off on purpose, and what the dashboard gave up:

_____________________________________________________________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
