# U3 L18 — Peer Review: Statistics Dashboards

**LO:** critique a real dashboard for statistical honesty, privacy, and clarity — and act on what the critique finds.

You built a dashboard. Someone else built one too. Today you break theirs,
carefully and with evidence, and you will take the same treatment next period.

**The rule: every criticism must name a specific number, a specific line, or
a specific pixel.** "This chart is confusing" is not a review. "The y-axis
starts at 1.5 on a bar chart, so the gap between 2 and 4 visits looks like
twenty bars" is a review.

## PART 0 — SET UP (5 min)

You need the review partner's repository link from Classroom. Clone it:

```bash
cd ~/compmath-lab
git clone <their-repo-url> peer-dashboard
cd peer-dashboard
ls
```

You should see their `dashboard.py`, their `stats_engine.py` and
`privacy_filter.py`, and a `dashboard.png`. **Do not edit anything yet.**

## PART 1 — RUN IT (10 min)

```bash
mkdir -p /tmp/u3_datasets
cp /tmp/lab-data/u3_project_dataset.csv /tmp/u3_datasets/
python3 dashboard.py
```

If the copy fails, your partner's repo should already contain the dataset at
`/tmp/lab-data/`; if it is not there, ask before continuing rather than
substituting a different file. Reviewing a dashboard against data it was not
built on produces findings that are wrong in both directions.

Now the honest part. Record:

1. Did it run without a traceback? ______
2. Did it write `dashboard.png`? ______
3. Did it print a **gate result** before drawing? ______
4. Does the gate say PASSED, FAILED, or is there no gate at all? ______

**If there is no privacy gate, that is your first and most serious finding.**
Write it up now and stop reading their statistics — a dashboard that
publishes `First_Name`, `Last_Name` and `Member_ID` is disqualified no matter
how good the charts look. Note it in the review and move on to the remaining
questions anyway, because you still need something to hand back.

## PART 2 — THE PRIVACY REVIEW (20 min)

Answer with the **actual** column names and values you find, not with the
names you wish they had used.

5. What is their `PUBLISHED_FIELDS` (or equivalent)? ______
6. What k does their gate actually achieve over those fields? Run it yourself
   rather than trusting their printout. Copy their `PUBLISHED_FIELDS` list
   out of their `privacy_filter.py` first — do not assume it matches their
   documentation:
   ```python
   from privacy_filter import k_value, anonymize
   from stats_engine import load

   rows = anonymize(load("/tmp/u3_datasets/u3_project_dataset.csv"))

   THEIR_FIELDS = ["Age"]          # <-- replace with THEIR actual list
   print("their published fields:", THEIR_FIELDS)
   print("k =", k_value(rows, THEIR_FIELDS))
   ```
   Replace the value on the `THEIR_FIELDS` line. If their fields include a
   column your `anonymize()` does not produce, you cannot run this check —
   note that as a finding in its own right and move to the next question.
7. Does their k meet their own stated `MIN_K`? If their gate **passes** but
   k is below their threshold, that is a bug in their gate, not a styling
   choice. Describe it in one sentence. ______
8. List every direct identifier still visible anywhere: on a chart, in a
   title, in a legend, in the printed output. ______
9. Look at their age handling. Do exact ages appear, or bands? If bands, what
   width, and does the smallest band have at least `MIN_K` members? ______
10. **The check almost nobody does:** does the printed output or the PNG
    contain any `Zip_Code`? Zip is a quasi-identifier even after you drop the
    name, and it is the fastest route back to a person. ______

## PART 3 — THE STATISTICS REVIEW (25 min)

This is the heart of it. For **each** of their four charts, answer:

11. Which statistic does the chart use? (mean, median, five-number summary,
    something else) ______
12. Does the chart's **title** name that statistic? A chart titled
    "Spend by City" that plots medians has hidden its own method. ______
13. Is there a case where the mean is being shown for right-skewed data? Check
    the data yourself:
    ```python
    from stats_engine import summarise, numeric, group_summary
    rows = load("/tmp/u3_datasets/u3_project_dataset.csv")
    print(summarise(numeric(rows, "Spend_USD")))
    ```
    Then say whether the mean or median is the defensible choice, and why. ______
14. **Bar charts:** does every y-axis start at zero? List any that does not,
    and compute how much the truncation exaggerates. (If a bar chart starts at
    1.0 and the bars are 2, 3, and 4, the visual ratios are 1, 2, 3 — but the
    true ratios are 2, 3, 4. Find the real exaggeration factor for theirs.)
    ______
15. **A line chart, if present:** is a truncated y-axis *acceptable* there?
    Explain the difference in one sentence. (For a line, the *slope* carries
    the meaning, not the intercept, so truncation costs less — but it still
    needs an explicit note. U3 L09.)
16. Is any chart's statistic inconsistent with its own chart title? ______

## PART 4 — THE CLARITY AND TRUTH REVIEW (20 min)

17. Does every axis have a label **and a unit**? List any that do not. ______
18. Is there a chart where the bins or the axis range make the data look more
    uniform than it is? (A histogram of `Spend_USD` with 20 bins across
    0–18,500 puts about 115 of 120 members in the first bar. Technically
    correct, practically unreadable.) ______
19. Does the dashboard state what it **hides**? For each chart, is there a
    note naming its blind spot? ______
20. Pick the single most misleading element in the whole dashboard and write
    the sentence you would use to explain it to someone outside the class. ______
21. What is the dashboard's strongest element? Name something specific. A
    review that only criticises is not a review. ______

## PART 5 — WRITE THE REVIEW (20 min)

Write your review as a GitHub issue on their repository. Use this structure.

```markdown
## Peer review — U3 L18

**Run result:** runs clean / traceback at line __
**Gate:** present, PASSES / present, FAILS / absent
**Published fields:** ___
**k achieved:** ___ (threshold ___)

### Blocking issues
1. <specific, with a number or a line reference>
2. <...>

### Should fix
3. <...>

### Minor
4. <...>

### What works
- <specific praise>

### My k and gate result
```
<the output of your own k_value run>
```
```

**Then stop.** Do not open a pull request against their code. The next period
they fix their own dashboard; you are not their maintainer.

## PART 6 — REVIEW THE REVIEW (15 min)

Now read the review you received on *your* dashboard from your partner, and
do the hardest part: **triage it honestly.**

Sort every point they made into exactly one column:

| Column | Meaning | Your count |
|---|---|---|
| **Fix now** | They are right, it is a real defect, I will change it | ___ |
| **Push back** | They are wrong, and here is the number that shows it | ___ |
| **Trade-off** | They are right, but fixing it costs something I value more | ___ |
| **Won't fix** | I disagree and I do not care to argue | ___ |

Rules for this part, which is the actual assignment:

- If you put something in **Push back**, you must supply the number or the
  line that disproves the point. "I disagree" is not a push-back.
- If you put something in **Won't fix**, you must say what you gain. Silence
  here reads as not having read it.
- If a point lands in **Fix now** and you push back anyway, that is a
  disagreement worth having — but write the push-back down, do not just skip
  it.

Two or three sentences per point. Not paragraphs.

## TURN IN — THE REVIEW ISSUE (due 11:59 PM tonight)

1. The review issue you opened on your partner's repo, **as a link**, posted
   to this assignment on Google Classroom.
2. Your triage table, as a comment on the **same issue** — it is your own
   dashboard's review, so put it in a reply rather than opening a second issue.

**In the triage comment, state your dashboard's k and whether your gate
passes.** If your partner found a real blocking issue in your work, say so
plainly in the first line. A student who writes "partner was right, k was
broken, fixed" has done harder work than one who writes "I disagree with
everything."

Keep the terminal open — spot-checks.
