# U3 L20 — Project Final Push: Polish and Submit

**LO:** finish, document, and defend a dashboard that a stranger can trust.

Last project day. Everything after this is the wrap-up unit (L21–L23), so
what you leave behind is what gets graded. Today is about the unglamorous
work that separates a working program from something you would be willing to
put your name on.

## PART 0 — THE HONEST STARTING CHECK (10 min)

```bash
cd ~/compmath-lab
git checkout u3-dashboard-fix
git log --oneline | head -5
python3 dashboard.py
```

Before you polish anything, answer these three in your notes:

1. Does it run clean from a fresh clone? (If not, everything else today is
   wasted effort on top of a broken base.)
2. Does `git status` show anything uncommitted? ______
3. If a classmate cloned your repo right now and ran `python3 dashboard.py`
   with nothing but the datasets, would they get the same PNG you get? ______

Question 3 is the real one. Test it honestly:

```bash
cd /tmp && rm -rf clone-test && git clone <your-repo-url> clone-test
cd clone-test
mkdir -p /tmp/u3_datasets
cp <path to>/u3_project_dataset.csv /tmp/u3_datasets/
python3 dashboard.py
```

If that fails, **stop and fix it before anything else.** A project that only
runs on your laptop is not finished, it is merely finished on your laptop.

## PART 1 — THE README (25 min)

You have code and a picture. What you do not have is anything that lets
someone else use it safely. Write `README.md`:

```markdown
# Privacy-Aware Member Statistics Dashboard

## What this shows
<four sentences: the four charts, and the one question the dashboard exists
to answer>

## Data
`/tmp/lab-data/u3_project_dataset.csv` — 120 members, 10 columns.
<where it comes from, and whether it is real or synthetic>

## How to run
```bash
mkdir -p /tmp/u3_datasets
cp /tmp/lab-data/u3_project_dataset.csv /tmp/u3_datasets/
python3 dashboard.py
```
Outputs `dashboard.png`. Requires Python 3.10+ and matplotlib.

## The privacy filter
| Setting | Value | Why |
|---|---|---|
| `MIN_K` | 5 | <reason> |
| `PUBLISHED_FIELDS` | ["Age"] | Age and City cannot be published together: k = 1 at every band width from 5 to 30 years. |
| Dropped columns | First_Name, Last_Name, Member_ID, Zip_Code, Signup_Date | direct identifiers / near-identifiers |
| `GROUP_COLS` | City, Membership_Tier | the columns the charts split by |

**Achieved k: ____ .** The gate prints this on every run.

**Known limits of this anonymization:**
<be specific. "Age banded to 15 years, city retained for grouping only.
Location within a city is not protected. The dataset is synthetic.">

## What the charts hide
- **Spend distribution:** <...>
- **Visits by tier:** <...>
- **Age bands:** <...>
- **Median spend by city:** <...>

## Known problems
<the findings you did NOT fix, and why. An empty section here reads as
"nothing to declare", which is never true.>
```

**The "Known problems" section is the part that matters.** A dashboard with
an honest list of its weaknesses is more trustworthy than one claiming
perfection, and a section you left empty is a claim of perfection.

## PART 2 — THE VISUAL POLISH (20 min)

Ten minutes, and only these four things. Do not start redesigning.

1. **Title case consistency.** Every axis, title, and label follows the same
   convention. Pick one.
2. **Units on every numeric axis.** "Spend (USD)", "Visits per month",
   "Age band (years)". A number without a unit is a number nobody can use.
3. **Readable fonts.** Your labels should be legible at 100% zoom. If
   anything is tiny, change the figure size — do not shrink the font.
4. **One honest subtitle** on the figure:
   ```python
   fig.suptitle("Member statistics — anonymized, k≥5, no direct identifiers",
                fontsize=13)
   ```
   If your actual k is not ≥5, this text is a lie. Fix the text or fix the
   filter.

Then regenerate and **look at it**. Open `dashboard.png` and read it as
someone who has never seen your data. Does anything look like a mistake?

## PART 3 — THE FINAL SELF-AUDIT (25 min)

Run every check and record the actual result. No boxes ticked by assumption.

**Privacy**

- [ ] `python3 dashboard.py` prints a gate result **before** any chart
- [ ] The gate result says PASSED
- [ ] Achieved k is ≥ `MIN_K`
- [ ] No `First_Name`, `Last_Name`, `Member_ID`, or `Zip_Code` appears in the
      PNG, in a title, in a legend, or in the printed output
- [ ] Ages appear only as bands
- [ ] The `Age + City` failure still blocks (L19 Part 4 evidence)

**Statistics**

- [ ] Every chart's title names the statistic it plots
- [ ] Every numeric axis has a label and a unit
- [ ] Every bar chart's y-axis starts at zero
- [ ] No mean is plotted for a right-skewed column without a note
- [ ] The log-axis chart, if you have one, says "log" on its axis label

**Honesty**

- [ ] Each of the four charts carries a statistic note and a blind-spot note
- [ ] The README's "Known problems" is non-empty and specific
- [ ] The README's "Known limits of this anonymization" names what is still
      exposed

**Reproducibility**

- [ ] A fresh clone runs and produces the same PNG
- [ ] `git status` is clean
- [ ] `python3 stats_engine.py` passes its own tests

For each box you cannot tick, write the reason. A completed audit with six
honest failures is worth more than a ticked list with a broken program.

## PART 4 — THE DEFENSE (20 min)

You will present this dashboard to someone who does not care about your
project. Prepare these five answers. You will be asked.

1. **"What is the one thing this dashboard is for?"** One sentence, no
   hedging.
2. **"Your mean spend is 379.56 and your median is 94.71. Which is the real
   number?"** (Neither. The median describes the typical member; the mean
   describes the total divided by 120. Ask which question you are answering
   before you pick one.)
3. **"Why can't you show the city and the age together?"** (k = 1 at every
   band width from 5 to 30 years. One member is alone in their age-and-city
   cell no matter how coarsely you band, and k-anonymity forbids k = 1.)
4. **"What is the worst thing someone could do with this data?"** Have a
   real answer. Consider: combining with an external list, differencing
   against a previous version, or noting that membership in a 15-person band
   in one city is itself identifying for a small group.
5. **"What would you do differently with two more days?"** A real answer
   beats a humble one. "Ship the four charts as an HTML report so the
   numbers are selectable" is a real answer. "I would try harder" is not.

## PART 5 — FINAL PUSH (10 min)

```bash
git add -A
git commit -m "U3 L20: README with k, anonymization limits, and known problems; visual polish; final audit"
git push
```

Verify the push landed:

```bash
git log --oneline -1
git status          # must be clean
```

## TURN IN — FINAL SUBMISSION (due 11:59 PM tonight)

**Three things to this assignment on Google Classroom:**

1. **Your repository link.**
2. **`dashboard.png`** — attached directly, not just linked. I want to see the
   image in the assignment stream, not go hunting for it.
3. **A written defense, six to ten sentences**, answering the five questions
   from Part 4. Plain prose, not a list. This is the piece I read most
   closely, because it is the only part that shows whether you understood
   what you built or just assembled it.

**Required in the defense, by name:**

- your achieved **k** and your **`MIN_K`**
- the **median** and **mean** of `Spend_USD` (94.71 and 379.56)
- the number of members still individually identifiable under your published
  fields (should be **0** at k ≥ 5)
- one thing your anonymization does **not** protect against

Submissions without those four numbers are returned ungraded. Not harsh —
just not gradable, because the numbers are the work.

## AND THEN

L21–L23 close the unit: outliers, a paper check, and a statistics library
other people can trust. Your dashboard becomes the reference implementation
for that last lab, so the thing you polish today is the thing you will be
relying on in four days.
