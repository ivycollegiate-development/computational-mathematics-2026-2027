# U3 L17 — Project Lab 3: The Dashboard — Project Checkpoint Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom as you build the dashboard, filling this sheet from your own screen. Change each ☐ to ☑ when that step is finished. Everything you record is your own output — nothing on this sheet hands you the number, and the sheet is checked against your running dashboard, not against an answer key.


## 0: Set up

☐  In the terminal:  cd ~/compmath-u3-stats-lab   then   git checkout u3-dashboard   then   ls stats_engine.py privacy_filter.py   then   git branch --show-current — record the branch it prints below.

☐  Create dashboard.py in that repo. No new libraries — matplotlib and csv, as in Unit 2.

branch = ______________________

## 1: The gate comes first

☐  Write load_publishable(path) before a single plotting call: anonymize(load(path)), then privacy_gate(rows, PUBLISHED_FIELDS, GROUP_COLS, MIN_K), print describe_result(...), and hand back rows only if the gate passed. Run that step alone and do not start the charts until you have watched it pass.

☐  Copy DATA, PUBLISHED_FIELDS, GROUP_COLS and MIN_K from the lab exactly as written, then read the control flow back to yourself.

☐  Is there any path through that function that returns rows while ok is False? Name the line that makes it impossible, and say why SystemExit beats returning None or printing a warning and carrying on:


_____________________________________________________________________

☐  Paste the gate line that printed on the run which passed:


_____________________________________________________________________

## 2: Chart 1 — the spread of spend

☐  Write chart_spend_distribution(rows, ax): numeric(rows, "Spend_USD"), ax.hist with bins=20, both axes labelled in words a stranger understands, a title stating what the picture shows, and an ax.text box built with stats_engine.median() — never sorted(values)[len(values)//2], which is wrong whenever the count is even and wrong quietly. Run it, then fill the table below from your own screen.

| Chart 1 reading | your own output |
| --- | --- |
| data source | ______________________ |
| median printed | ______________________ |
| mean printed | ______________________ |
| members in the tallest bar | ______________________ |

☐  Try at least two of the three fixes for the squashed histogram — more bins, a capped axis with an annotation, a log x-axis — and keep an image of each attempt:

| Fix tried | What you changed | Image kept |
| --- | --- | --- |
| more bins | ______________________ | ______________________ |
| capped axis | ______________________ | ______________________ |
| log x-axis | ______________________ | ______________________ |

☐  Why is a histogram right for this column when a bar chart of tier averages would be actively wrong? Then say which fix you kept and, in one sentence, what chart 1 hides:


_____________________________________________________________________

## 3: Chart 2 — visits by tier

☐  Write chart_visits_by_tier(rows, ax) from one group_summary(rows, "Monthly_Visits", "Membership_Tier") call. Bars carry the median, the mean is a point, and set_ylim(0, ...) keeps the axis on zero.

chart 2 data source = ______________________

☐  Run it, then fill every tier in from your own output:

| Membership_Tier | median | mean |
| --- | --- | --- |
| Basic | ________________ | ________________ |
| Standard | ________________ | ________________ |
| Premium | ________________ | ________________ |
| Enterprise | ________________ | ________________ |

☐  Look at the bars before you interpret them. Same height four times, or four heights? A bug in your code, or a fact about the column? Which statistic carries the information here, and what does chart 2 hide?


_____________________________________________________________________

## 4: Chart 3 — age bands

☐  Write chart_age_bands(rows, ax): count rows by their Age band string, sort the labels, bar the counts, rotate the x tick labels.

chart 3 data source = ______________________

☐  Run it and record every band your data contains, with its count:

| Age band | count |
| --- | --- |
| ________________ | ________________ |
| ________________ | ________________ |
| ________________ | ________________ |
| ________________ | ________________ |

☐  Compare your smallest group against MIN_K and scan the chart for an exact age. Does the smallest group pass, does any exact age appear, and what would you do if a group fell under k?


_____________________________________________________________________

## 5: Chart 4 — spend by city

☐  Write chart_spend_by_city(rows, ax) from group_summary(rows, "Spend_USD", "City"): bars on the median, the y-axis from zero, an n= label above every bar.

chart 4 data source = ______________________

☐  Run it and record the median and the mean for every city in your data:

| City | n | median | mean |
| --- | --- | --- | --- |
| ________________ | ________ | ____________ | ____________ |
| ________________ | ________ | ____________ | ____________ |
| ________________ | ________ | ____________ | ____________ |
| ________________ | ________ | ____________ | ____________ |
| ________________ | ________ | ____________ | ____________ |

☐  Name the city with the widest gap between its median and its mean, then say what that gap warns you about, why this chart is plotted on the median, and what it still hides:


_____________________________________________________________________

## 6: Assemble and label

☐  Write draw_all_charts(rows) with fig, axes = plt.subplots(2, 2, figsize=(14, 9)), the four charts in the order you built them, a suptitle stating the anonymized gated claim, then fig.tight_layout() and fig.savefig("dashboard.png", dpi=110). Then add both notes to every chart — the statistic used with the column it came from, and one honest sentence on what the chart hides. Look at dashboard.png and tick what is really there, not what you meant to write:

| Chart | statistic note | blind-spot note |
| --- | --- | --- |
| 1 spend distribution | ________________ | ________________ |
| 2 visits by tier | ________________ | ________________ |
| 3 age bands | ________________ | ________________ |
| 4 spend by city | ________________ | ________________ |

☐  Run python3 dashboard.py end to end, confirm the gate line prints before any chart, and record the line that followed it:


_____________________________________________________________________

## 7: The failure proof

☐  Temporarily put both Age and City in PUBLISHED_FIELDS, save, and run python3 dashboard.py again. Record the refusal as it was printed, and whether dashboard.png was written anyway:


_____________________________________________________________________

☐  Set PUBLISHED_FIELDS back to the single field and run once more. What is on screen:


panels rendered = ______________________

## 8: Checkpoint — what must be on screen before you leave

☐  load_publishable is called, and draw_all_charts is not reachable without it.

☐  python3 dashboard.py prints the gate result before any chart appears.

☐  dashboard.png exists and all four panels are populated, every axis labelled with its unit and no bar-chart y-axis above zero.

☐  No exact age, name, member ID or zip appears in the image or in the printed output.

☐  All four charts carry a statistic note and a blind-spot note.

☐  Every table above is filled in from your own run.

instructor initials = ______________________

## 9: Save and push

☐  git add dashboard.py dashboard.png

☐  git commit -m "U3 L17 dashboard: four gated charts, each labelled with its statistic and blind spot"

☐  git push   →  Paste the confirmation line GitHub printed:


_____________________________________________________________________

## 10: Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment.

| Put in the push message, from your own run | your value |
| --- | --- |
| gate output line | ______________________ |
| Spend_USD median | ______________________ |
| Spend_USD mean | ______________________ |
| k of published data | ______________________ |
| members still identifiable | ______________________ |

☐  One sentence naming the blind spot of your weakest chart:


_____________________________________________________________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
