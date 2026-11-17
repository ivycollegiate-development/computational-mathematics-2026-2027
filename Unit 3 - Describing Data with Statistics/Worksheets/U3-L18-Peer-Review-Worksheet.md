# U3 L18 — Peer Review: Statistics Dashboards — Review Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom with their repository open beside this sheet. Change each ☐ to ☑ once that step is done and you have written down what it actually printed. Every blank comes off your own screen — nothing on this sheet gives you an answer, and no expected verdict is written here.

## 0: Set up

☐  Go to the lab repo and clone theirs:  cd ~/compmath-u3-stats-lab   then   git clone <their-repo-url> peer-dashboard

☐  Go in and list:  cd peer-dashboard   then   ls

☐  Record who you are reviewing, then check the repo for the four files a reviewable dashboard carries:

team or repo owner ______________________   repository name ______________________

| File | Present? (Y/N) | If missing, what is there instead |
| --- | --- | --- |
| dashboard.py | ______ | ______________________ |
| stats_engine.py | ______ | ______________________ |
| privacy_filter.py | ______ | ______________________ |
| dashboard.png | ______ | ______________________ |


☐  Do not edit anything inside peer-dashboard; every file you write today belongs in your own repo.

## 1: Run it

☐  Run theirs:  python3 dashboard.py

☐  Record the run in one line — clean exit, or the last traceback line with its number:

_____________________________________________________________________


☐  If data/u3_project_dataset.csv is missing, stop and ask rather than substituting another file. What you found: ______________________

☐  Record the three run facts off your own screen:

ran without a traceback ______________________   wrote dashboard.png ______________________

printed a gate result before drawing ______________________   gate state, in their words ______________________

## 2: The privacy review

☐  Read their PUBLISHED_FIELDS out of privacy_filter.py, not off their README, and copy it exactly:

_____________________________________________________________________

☐  One row per published field, spelled as it appears in the source:

| Field | Direct identifier? (Y/N) | Quasi-identifier? (Y/N) |
| --- | --- | --- |
| ______________________ | ______ | ______ |
| ______________________ | ______ | ______ |
| ______________________ | ______ | ______ |

☐  Run the lesson's k check yourself — import k_value, anonymize and load, put their actual list on the THEIR_FIELDS line — and record what it printed:

k you computed ______________________   their stated MIN_K ______________________

☐  Does their gate pass while their k sits under their own MIN_K? Start from the verdict, then one sentence saying why.   verdict = ______________________

_____________________________________________________________________

☐  Every direct identifier still visible — on a chart, in a title, in a legend, in the printed output:

_____________________________________________________________________

☐  Age handling:  exact ages or bands ______________________   band width ______________________   smallest band ______________________

☐  The zip check — any Zip_Code in the printed output or inside the PNG?  found ______________________   where ______________________

## 3: The statistics review

☐  One row per chart they drew; read their code, not the picture, for the statistic column:

| Chart | Statistic used | Title names it? (Y/N) | Y-axis starts at zero? (Y/N) |
| --- | --- | --- | --- |
| ______________ | ______________ | ______ | ______ |
| ______________ | ______________ | ______ | ______ |
| ______________ | ______________ | ______ | ______ |
| ______________ | ______________ | ______ | ______ |

☐  Run the lesson's summarise check on Spend_USD and record what it printed:

_____________________________________________________________________

☐  Any chart showing a mean over right-skewed data? Name it, then say whether the mean or the median is defensible here, and why:

_____________________________________________________________________

☐  Any bar chart that does not start at zero? Name it and work out the real exaggeration factor from its bars:

chart ______________________   factor ______________________ x

☐  Their line chart, if any: is a truncated y-axis acceptable there? Use the word slope; write none if they drew no line chart:

_____________________________________________________________________

☐  Any chart whose statistic contradicts its own title?  chart ______________________   title ______________________


## 4: The clarity and truth review

☐  Every axis needs a label and a unit. One row per axis you can see:

| Chart | Axis | Label present? (Y/N) | Unit present? (Y/N) |
| --- | --- | --- | --- |
| ______________ | ______ | ______ | ______ |
| ______________ | ______ | ______ | ______ |
| ______________ | ______ | ______ | ______ |

☐  Bins and range: any chart that makes the data look more uniform than it is?  chart ______________________   bins ______________________

☐  Does the dashboard say what it hides?  charts carrying a blind-spot note ______________________ of ______________________

☐  Name the single most misleading element, then write the sentence you would use to explain it to someone outside the class:

element = ______________________


_____________________________________________________________________

☐  Their strongest element, specific enough that they could keep it on purpose:

_____________________________________________________________________

## 5: Triage the review you received

☐  Sort every point your partner made into exactly one column, and count the points in each:

| Column | Meaning | Your count |
| --- | --- | --- |
| Fix now | They are right, it is a real defect | ______ |
| Push back | They are wrong, and a number shows it | ______ |
| Trade-off | They are right, but the fix costs more | ______ |
| Won't fix | I disagree and will not argue it | ______ |


☐  For each Push back, the number or line that disproves it; for each Won't fix, what you gain:

_____________________________________________________________________

## 6: What goes back to the team

☐  Rank their top three fixes, most serious first. Each must name a number, a line or a pixel; a general complaint does not count:

| Rank | Fix | The number or line that proves it |
| --- | --- | --- |
| 1 | ____________________________ | ______________________ |
| 2 | ____________________________ | ______________________ |
| 3 | ____________________________ | ______________________ |

☐  Of the three, which one blocks a reader outside the class?  blocking rank ______________________

## 7: Save and push

☐  Write the review in your own repo as peer-review.md, in the lesson's headings: run result, gate, published fields, k achieved, blocking issues, should fix, minor, what works, my k and gate result.

☐  Write nothing into peer-dashboard and open no pull request against their code — next period they fix their own dashboard.

☐  git add peer-review.md

☐  git commit -m "U3 L18 peer review of the partner dashboard"

☐  git push   →  paste the push URL GitHub printed:

_____________________________________________________________________

## 8: Turn in

☐  Open the review as an issue on their repository, using the same headings as your file. Paste the issue link:

_____________________________________________________________________

☐  Post that issue link to this assignment on Google Classroom.

☐  Put your triage table in a comment on the same issue, not in a second issue. Record your own numbers:

your k = ______________________   your gate = ______________________

☐  If your partner found a real blocking issue in your work, say so in the first line of that comment.

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
