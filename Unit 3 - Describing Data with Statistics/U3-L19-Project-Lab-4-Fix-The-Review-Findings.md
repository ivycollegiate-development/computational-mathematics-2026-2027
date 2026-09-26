# U3 L19 — Project Lab 4: Fix the Review Findings

**LO:** turn a critique into correct code, and prove the fix with before-and-after evidence.

You received a review. Some of it was right. Today you fix it, and the
standard is not "I changed it" — it is **"here is the number that was wrong,
and here it is now."**

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
git checkout u3-dashboard-fix
```

If you are on a branch name from L17, use that. Either way, confirm:

```bash
git log --oneline | head -3
python3 dashboard.py   # does it still run?
```

Record the current state before you change anything:

```bash
git branch before-fixes
```

You now have a named point to compare against. Skipping this is how you end
up unable to prove your own fixes worked.

## PART 1 — TRIAGE, THEN COMMIT TO A NUMBER (15 min)

Open your review issue again and re-read your triage. Take only the rows you
marked **Fix now**. Ignore the push-backs — defending those is not today's
job.

For each fix-now finding, write down **the specific assertion that will change
when it is fixed.** Not "improve the chart." A number or a string:

```text
Finding:  y-axis on "Visits by tier" starts at 1.5
Now:      axis min = 1.5
After:    axis min = 0
Evidence: the 2.0 bar is drawn at 20% of axis height instead of 50%

Finding:  gate passes but k = 1 over ["Age","City"]
Now:      privacy_gate(...) returns (True, [], [...])
After:    returns (False, ["k=1 over ['Age','City'] ..."], [])
```

**A finding with no measurable "after" is a wish, not a finding.** If you
cannot write the "After" line, the finding was not specific enough, and you
should go back to the review and say so rather than inventing a change.

Count how many you are fixing. That number is your target for today.

## PART 2 — FIX THEM, ONE AT A TIME (40 min)

For each finding, in this order:

1. **Make the change.** Smallest edit that fixes the actual problem.
2. **Commit it separately** with a message naming the finding, not the file:
   ```bash
   git add -A
   git commit -m "fix: y-axis on visits-by-tier now starts at 0 (review finding 3)"
   ```
   One commit per finding. Six commits are better than one giant commit,
   because then your partner can verify each fix independently and you can
   revert one without losing the rest.
3. **Record the evidence.** Paste the before and after in your notes.

Do **not** do a stylistic rewrite while you are in there. If you spot
something unrelated, add it to a `### Minor` list and move on. Mixing a
refactor into a correctness fix means nobody can tell which change solved the
problem.

## PART 3 — THE THREE FIXES YOU WILL PROBABLY NEED (25 min)

These are the findings that come up most often in this project. Check each
against your own dashboard; if it does not apply, say why in your notes.

### Fix A — the histogram that shows nothing

The 20-bin histogram of `Spend_USD` puts ~115 of 120 members in the first
bar. The fix that actually works is a log x-axis:

```python
import math

# No numpy in this course. Here is the same transformation, written out:
values = [v for v in numeric(rows, "Spend_USD") if v > 0]
log_values = [math.log10(v) for v in values]
ax.hist(log_values, bins=20, color="#3b5b8c", edgecolor="white")
ax.set_xlabel("Spend (USD, log10 scale — each bar is a 10x range)")
```

- The x-axis label **must** say it is a log scale. An unlabelled log axis is
  worse than a bad linear one, because a reader who does not notice will
  misread the distances.
- A log axis cannot show **0**, which is why the `v > 0` filter exists. Count
  how many values you dropped. On this data it is exactly **1** — a single
  `Spend_USD` of 0.00 — so your caption must say "119 of 120 members; one
  zero-spend member cannot be shown on a log scale." Dropping a value
  silently is the L09 truncated-axis mistake wearing a better hat.
- **Check the fix worked** rather than assuming. The linear version put ~115
  of 120 in one bin. After the log transform, the busiest bin holds **17**.
  Print your bin counts and compare:

  ```python
  log_values = [math.log10(v) for v in values if v > 0]
  lo, hi = min(log_values), max(log_values)
  counts = [0] * 20
  for x in log_values:
      i = min(19, int((x - lo) / (hi - lo) * 20))
      counts[i] += 1
  print(counts)
  ```

  You should get roughly `[4, 6, 12, 11, 13, 12, 10, 17, 6, 10, 8, 4, 3, 1, 0, 0, 1, 0, 0, 1]`
  — spread across the range instead of piled in one place. If your counts
  still show a single dominant bin, something is wrong with the transform,
  not the data.

- Can a reader now see both the 94.71 median and the 18,500.00 outlier as
  distinct features? On a log axis they sit at log10 = **1.98** and
  log10 = **4.27**, more than two decades apart, so yes. If your version
  cannot, the log scale is not doing its job.

### Fix B — the title that hides the method

If your chart plots medians and the title says "Spend by City", rename it.

```python
ax.set_title("Median spend by city (mean not shown)")
```

Adding the parenthetical is not decoration. It tells the reader two things at
once: which statistic to trust, and that another one exists and was omitted
**on purpose**. A reader who knows a choice was made cannot mistake it for an
oversight.

Check all four of your titles. Each must name its statistic.

### Fix C — the gate that passes something it should not

If your partner found that your gate returns PASSED while k is below your own
`MIN_K`, the bug is in `check_k`, not in the data. Read it again:

```python
def check_k(rows, published_fields, min_k=MIN_K):
    if not published_fields:
        return []          # <-- suspect this line
    k = k_value(rows, published_fields)
    if k >= min_k:
        return []
    ...
```

That early return means "if you publish nothing identifying, we pass." For a
dashboard that shows *nothing* per person that is arguably correct — but for
one that groups by a small column, `published_fields` may be empty while the
**chart** still splits people into tiny cells. The small-cell check has to
catch that case, and it only does so if you passed the right `group_cols`.

Check: does your gate's `group_cols` list every column your four charts
actually group by? Count them. A chart that groups by something the gate
never heard of is an unsupervised split.

## PART 4 — RE-RUN THE FAILURE PROOF (10 min)

Your gate must still block. A fix to the charts must never have quietly
weakened the filter.

```bash
sed -i '' 's/PUBLISHED_FIELDS = \["Age"\]/PUBLISHED_FIELDS = ["Age", "City"]/' dashboard.py
python3 dashboard.py
```

It must refuse, exit non-zero, and write **no** PNG. Then:

```bash
sed -i '' 's/PUBLISHED_FIELDS = \["Age", "City"\]/PUBLISHED_FIELDS = ["Age"]/' dashboard.py
python3 dashboard.py
```

It must pass and write the PNG. Record both outputs.

**If your fixes made the gate pass on `Age + City`, stop and undo the last
commit.** You have traded a broken chart for a privacy hole, and that is a
strictly worse outcome than an ugly picture.

## PART 5 — YOUR BEFORE-AND-AFTER TABLE (10 min)

This is the deliverable that proves the work. One row per fix:

| # | Finding | Before | After | Evidence |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

If you fixed nothing because your partner found nothing blocking, say so and
show the evidence that made that the right conclusion — the gate output, the
k, and the four chart titles. "Nothing to fix" is a legitimate result when
you can defend it.

## PART 6 — SAVE + PUSH (last 10 min)

```bash
git add -A
git commit -m "U3 L19: addressed N review findings with before/after evidence"
git push
```

## TURN IN — PUSH CONFIRMATION (due 11:59 PM tonight)

Push confirmation screenshot, to this assignment on Google Classroom.

Your push message must contain:

1. the number of findings you fixed
2. the **before** and **after** gate output (both must be in your message)
3. your final k and your `MIN_K`
4. one finding you **pushed back** on, with the number that justifies it
5. one finding you chose to **trade off**, and what you gave up

Item 5 is the one I am most interested in. A dashboard that fixes everything
criticised is often a dashboard that has given away its most interesting
finding. If you traded something away on purpose, say what and why — that is a
judgement, and I want to see you make one.

Keep the terminal open — spot-checks.
