# U3 L20 — Project Final Push: Polish and Submit — Submission Checklist


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal and your editor, and change each ☐ to ☑ only when the evidence is on your own screen — a file that lists, a test line that prints PASSED, a chart you opened, a hash git printed. Nothing on this sheet gives you the answer; every blank is filled from your own run, and the sheet is checked against your repository, not against an answer key.

## 0: Set up

☐  Go to the project repo:  cd ~/compmath-u3-stats-lab

☐  Switch to the branch you have been building on:  git checkout u3-dashboard-fix

☐  Record the branch you are on and the newest commit line git log shows:

| Branch | Newest commit line |
| --- | --- |
| ____________________ | ________________________________ |


☐  Run the dashboard once before you change anything:  python3 dashboard.py

☐  Record where the image landed and how the run ended:

| dashboard.png path | Run ended clean (yes / no) |
| --- | --- |
| ________________________ | ________ |

## 1: Files

☐  List all four deliverables and the dataset in one command:  ls README.md dashboard.py stats_engine.py dashboard.png data/u3_project_dataset.csv

☐  Fill the table from what ls prints. A file you cannot see is a file that is not submitted:

| File | Size shown by ls | Modified |
| --- | --- | --- |
| README.md | ____________ | ____________ |
| dashboard.py | ____________ | ____________ |
| stats_engine.py | ____________ | ____________ |
| dashboard.png | ____________ | ____________ |
| data/u3_project_dataset.csv | ____________ | ____________ |

☐  Record the members and columns your own loader reports for the dataset:

| Members | Columns |
| --- | --- |
| ____________ | ____________ |

## 2: Tests and the fresh clone

☐  Run the engine's own tests:  python3 stats_engine.py

☐  Paste the summary line the test run printed:

_____________________________________________________________________


☐  Prove it runs off your machine. Clone your own repo into a scratch folder, then run it there:

cd /tmp && rm -rf clone-test && git clone -b u3-dashboard-fix <your-repo-url> clone-test

cd clone-test && ls data/ && python3 dashboard.py

☐  Record what that clone run produced:

| Clone ran (yes / no) | PNG appeared (yes / no) | What was missing |
| --- | --- | --- |
| ________ | ________ | ____________________ |

## 3: The dashboard and its polish

☐  Pick one title-case convention for every title, axis label and legend entry, put a unit on every numeric axis, and make every label legible at 100% zoom by changing the figure size rather than shrinking the font.

☐  Add one subtitle stating the anonymization honestly. It has to match the gate result your own run printed.

☐  Open dashboard.png and read it as someone who has never seen your data.

☐  Copy the four chart titles exactly as they appear in the image:

| Chart | Title shown on the image |
| --- | --- |
| 1 | ________________________________ |
| 2 | ________________________________ |
| 3 | ________________________________ |
| 4 | ________________________________ |

☐  Confirm every bar chart's y-axis starts at zero, a log axis says log in its label, and each of the four charts carries a statistic note and a blind-spot note.

## 4: The privacy gate

☐  Run python3 dashboard.py again and paste the gate line it prints before any chart appears:

_____________________________________________________________________


☐  Record the two numbers that line reports:

| Achieved k | MIN_K |
| --- | --- |
| ____________ | ____________ |

☐  Search the image, the titles, the legends and the printed output for First_Name, Last_Name, Member_ID, Zip_Code and Signup_Date. Say where you looked and what you found:

_____________________________________________________________________


☐  Fill the gate table from your own run:

| Check | Passed (yes / no) | Where you saw it |
| --- | --- | --- |
| Gate prints before any chart | ________ | ____________ |
| Gate result says PASSED | ________ | ____________ |
| Achieved k is at least MIN_K | ________ | ____________ |
| No direct identifier in image or output | ________ | ____________ |
| Ages appear only as bands | ________ | ____________ |
| Age + City still blocked | ________ | ____________ |

## 5: The README

☐  Confirm README.md carries all six headings, that How to run gives the real command and the real output file (python3 dashboard.py  →  dashboard.png), and that Data names the file and the counts you recorded.

☐  Confirm The privacy filter lists MIN_K, PUBLISHED_FIELDS, the dropped columns and GROUP_COLS.

☐  Confirm Known limits of this anonymization names what is still exposed, in specifics:

_____________________________________________________________________


☐  Confirm Known problems is non-empty. Paste your first entry:

_____________________________________________________________________


## 6: Git history

☐  Record the two most recent commit subject lines, and confirm this session's work is committed as readable, separate commits rather than one dump:

| Commit | Subject line |
| --- | --- |
| newest | ________________________________ |
| previous | ________________________________ |

## 7: Reflection

☐  In one sentence, with no hedging: what is this dashboard for?

_____________________________________________________________________


☐  Name the one finding you chose not to fix, and say why you left it:

_____________________________________________________________________


## 8: Submission checklist

☐  Tick a line only when the evidence is in front of you. An unticked line is a real missing piece, not a formality.

| Requirement | Evidence you can point at | Met (initials) |
| --- | --- | --- |
| Repository link posted | ____________ | ________ |
| dashboard.png attached, not linked | ____________ | ________ |
| Defense written as six to ten sentences of prose | ____________ | ________ |
| Achieved k and MIN_K stated in the defense | ____________ | ________ |
| Median and mean of Spend_USD stated | ____________ | ________ |
| Count of members still identifiable stated | ____________ | ________ |
| One risk the filter does not cover stated | ____________ | ________ |
| Branch pushed, git status clean | ____________ | ________ |
| README Known problems non-empty | ____________ | ________ |

## 9: Save and push

☐  git add -A

☐  git commit -m "U3 L20: README with k, anonymization limits, and known problems; visual polish; final audit"

☐  git push

☐  Record the push evidence exactly as git and GitHub printed it:

| Push URL | Commit hash | Subject |
| --- | --- | --- |
| ____________________ | ________________ | ________________ |

☐  Confirm the push landed and the tree is clean:  git log --oneline -1   then   git status

## 10: Turn in

☐  Paste your repository link:

_____________________________________________________________________


☐  Attach dashboard.png directly to the Classroom assignment so the image shows in the stream.

☐  Post the written defense as plain prose, not a list, answering the five questions from Part 4.

☐  Re-read the defense and confirm the required figures are actually in it: your k, your MIN_K, the median and mean of Spend_USD, and the count of members still individually identifiable.

☐  Keep the terminal open for a spot-check. Due 11:59 PM.
