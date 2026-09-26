# U3 L17 — Project Lab 3: The Dashboard

**LO:** render four charts from the stats engine, gated by the privacy filter, with each chart labelling its statistic and its blind spot.

You have the engine (L14) and the gate (L15). Today you draw. This is the
day the whole unit becomes something a person can look at.

**Definition of done for today:** `dashboard.py` runs, calls the gate before
any plotting, renders four charts into one figure, and every chart carries a
title, axis labels with units, and a note naming what it hides.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
git checkout u3-dashboard
```

You should have `stats_engine.py` and `privacy_filter.py` in your repo. You
are adding `dashboard.py`. No new libraries — matplotlib and `csv`, same as
Unit 2.

## PART 1 — THE GATE COMES FIRST (15 min)

Write this line before you write a single plotting call. This is the
non-negotiable part of the lab.

```python
from stats_engine import load, summarise, group_summary, numeric
from privacy_filter import privacy_gate, describe_result, anonymize, k_value

DATA = "/tmp/u3_datasets/u3_project_dataset.csv"
PUBLISHED_FIELDS = ["Age"]          # the lesson from L15: NOT Age + City
GROUP_COLS = ["City", "Membership_Tier"]
MIN_K = 5

def load_publishable(path):
    """Load, anonymize, gate. Returns rows only if the gate passed."""
    rows = anonymize(load(path))
    ok, problems, warnings = privacy_gate(rows, PUBLISHED_FIELDS, GROUP_COLS, MIN_K)
    print(describe_result(ok, problems, warnings))
    if not ok:
        raise SystemExit("refusing to draw: privacy gate failed")
    return rows
```

- Read the control flow. Is there **any** path in this function that returns
  rows while `ok` is False?
- Why `SystemExit` rather than returning `None` or printing a warning and
  continuing?
- `PUBLISHED_FIELDS` is `["Age"]` and not `["Age", "City"]` because of the
  L15 finding. Write in your notes what changes if you add `"City"` back, and
  what the gate will say.

Print the gate output and paste it in your notes. **Do not start Part 2
until you have seen it pass.**

## PART 2 — CHART 1: THE SPREAD OF SPEND (25 min)

The most important chart in the dashboard, because it is the one the
misleading version gets wrong.

**Design rule from U3 L09: bar charts start at zero.** A histogram is not a
bar chart in that sense, but a bar chart of tier *averages* certainly is.

```python
import matplotlib.pyplot as plt
import statistics as st

def chart_spend_distribution(rows, ax):
    """Histogram of Spend_USD -- shows the skew the mean hides."""
    values = numeric(rows, "Spend_USD")
    ax.hist(values, bins=20, color="#3b5b8c", edgecolor="white")
    ax.set_xlabel("Spend (USD)")
    ax.set_ylabel("Number of members")
    ax.set_title("Spend per member is right-skewed")
    ax.text(0.98, 0.95,
            f"median ${st.median(values):,.2f}\n"
            f"mean   ${st.mean(values):,.2f}\n"
            "the mean is pulled by a few very large values",
            transform=ax.transAxes, ha="right", va="top", fontsize=8,
            bbox=dict(boxstyle="round", facecolor="#fff8e1", edgecolor="#d0a000"))
```

**Before you run it, fix one thing in the code above.** The first draft of
that text box computed the median as `sorted(values)[len(values)//2]`. That
is wrong, and it is wrong in a way worth understanding: with 120 values,
`len(values)//2` is 60, which is the **61st** value, not the middle. A true
median averages the 60th and 61st. The text box would have printed **96.42**
while the real median is **94.71**.

This is why `stats_engine.median()` exists. Always call it. Never reach for
`sorted(...)[n//2]` — you will get it wrong exactly when *n* is even, which
is half the time, and the error is invisible because the number looks
perfectly plausible.

Run it on the real data and record in your notes:

1. The median of `Spend_USD` and the mean. The mean is far higher.
2. How many members are in the tallest bar? (Most of them, or a handful?)
3. The `ax.text` box states what the chart hides. Is the statement *true* of
   your data? Check the two numbers in it against `summarise`.

**Now look at what you actually drew.** Render the chart and study it
honestly. With 20 bins spanning 0 to 18,500, roughly **115 of the 120 members
land in the very first bar**, and the rest are near-invisible slivers. You
have drawn a chart that is technically accurate and practically useless — it
says "almost everyone is cheap" in one lump and shows you nothing about the
116th person.

Three ways to fix it, in increasing order of honesty:

- **Widen the bin count.** More bins does *not* help here. The data genuinely
  has a 0-to-18,500 range and a cluster below 500. You cannot fix this by
  tuning.
- **Cap the axis** at, say, 500 and annotate what you cut off. Faster, and it
  is the U3 L09 truncated-axis move — legitimate *only* if the annotation says
  how many values are excluded and why.
- **Use a log x-axis.** The right answer for this data. It shows both the
  94.71 median and the 18,500.00 outlier in one picture, because a log scale
  is the one place where "one bar per equal *ratio*" is the honest encoding.

Do at least two of the three and put the resulting images in your notes. The
skill is recognising that **"the code ran and produced a chart" is not the same
as "the chart communicates something."**

**The statistic question:** why is a histogram the right chart here, and why
is a bar chart of tier *averages* actively wrong? (U3 L09: average spend by
tier makes the **Basic** tier look like the biggest spenders, at 648.03,
when dropping one 18,500.00 member drops that to 32.44.)

## PART 3 — CHART 2: VISITS BY TIER (20 min)

```python
def chart_visits_by_tier(rows, ax):
    """Median visits per tier, with the mean marked for contrast."""
    groups = group_summary(rows, "Monthly_Visits", "Membership_Tier")
    tiers = list(groups.keys())
    medians = [groups[t]["median"] for t in tiers]
    means = [groups[t]["mean"] for t in tiers]

    x = range(len(tiers))
    ax.bar(x, medians, width=0.6, color="#2e7d32", label="median")
    ax.plot(x, means, "o", color="#c62828", label="mean", markersize=8)
    ax.set_xticks(list(x))
    ax.set_xticklabels(tiers)
    ax.set_ylim(0, max(means) * 1.3)          # starts at zero: U3 L09
    ax.set_ylabel("Visits per month")
    ax.set_title("Median visits by tier (mean marked in red)")
    ax.legend()
```

Answer in your notes:

4. **Run this before you interpret it.** Every one of the four tiers has a
   median of exactly **2.00** visits. Four identical bars. Is that a bug in
   your code or a fact about the data? (It is a fact — `Monthly_Visits` is
   small, and half of every tier has 2 visits or fewer.) Given that, what is
   the *right* statistic for this chart, and why does the mean — not the
   median — turn out to be the more informative one here?
5. The red mean markers sit **above** the bars for every tier, and they sit
   above by different amounts: Basic 2.53, Standard 3.17, Enterprise 2.70,
   Premium 3.63. What does the Premium mean being highest tell you about
   Premium's distribution that its median hides? (A minority of Premium
   members visit a great deal; most do not.)
6. The y-axis starts at **0** even though the medians are small. Why is that
   non-negotiable for a bar chart? (Because bar **length** encodes the value.
   A bar from 0 to 2 and a bar from 0 to 4 look like 1:2; if you start at 1.5
   the same bars can be made to look like 1:20. A line or dot plot may
   truncate; a bar may not.)
7. Why plot the median as the bar and the mean as a point, rather than
   printing both as bars side by side?

## PART 4 — CHART 3: AGE DISTRIBUTION, BANDED (20 min)

This is the chart that proves your anonymization is real.

```python
def chart_age_bands(rows, ax):
    """Ages as bands, never as exact ages."""
    counts = {}
    for r in rows:
        lo = int(r["Age"].split("-")[0])
        label = r["Age"]
        counts[label] = counts.get(label, 0) + 1
    bands = sorted(counts)
    ax.bar(bands, [counts[b] for b in bands], width=0.6, color="#5d4037")
    ax.set_xlabel("Age band (years)")
    ax.set_ylabel("Number of members")
    ax.set_title("Members by age band")
    ax.tick_params(axis="x", rotation=45)
```

- Which L12 requirement does this chart satisfy that chart 1 and 2 do not?
  (It publishes `Age` in 15-year bands, so no exact age appears anywhere.)
- Write the exact ages that appear in your data — is any of them visible in
  this chart? It should be none of them.
- What is the smallest group size in your chart, and does it meet your own
  `MIN_K`? You should find four bands — 15-29 (29), 30-44 (40), 45-59 (36),
  60-74 (15) — with a smallest group of **15**, comfortably above `MIN_K`
  of 5. Check it rather than assuming; if your smallest group were 1, you
  would have found a real problem in your own dashboard and said so in the
  report rather than hoping nobody looked.

## PART 5 — CHART 4: SPEND BY CITY (20 min)

The chart most likely to hide something, which is why it is last.

```python
def chart_spend_by_city(rows, ax):
    """Median spend by city -- NOT the mean, and the title says so."""
    groups = group_summary(rows, "Spend_USD", "City")
    cities = list(groups.keys())
    medians = [groups[c]["median"] for c in cities]
    ax.bar(cities, medians, width=0.6, color="#00695c")
    ax.set_ylim(0, max(medians) * 1.3)
    ax.set_ylabel("Median spend (USD)")
    ax.set_title("Median spend by city")
    for i, c in enumerate(cities):
        s = groups[c]
        ax.text(i, s["median"], f"n={s['n']}", ha="center", va="bottom", fontsize=7)
```

8. Why is this the **median** and not the mean? Check both for every city:

   | City | n | median | mean | gap |
   |---|---|---|---|---|
   | Hsinchu | 20 | 55.36 | 103.53 | 48.17 |
   | Kaohsiung | 20 | 120.91 | 196.86 | 75.95 |
   | Taichung | 40 | 137.97 | 186.13 | 48.15 |
   | Tainan | 20 | 70.20 | **1,277.75** | **1,207.55** |
   | Taoyuan | 20 | 129.78 | 326.98 | 197.19 |

   **Tainan** is the one to understand. Its median is 70.20 — the fourth
   lowest — while its mean is 1,277.75, the highest of all five by an order
   of magnitude. A mean-by-city chart would make Tainan look like the
   heaviest-spending city in the country. The median chart shows the truth
   and the mean never appears.
9. The `n=` labels under each bar: is any city small enough to worry about?
   Compare against `MIN_K` and against the small-cell check from L15.
10. Your title says "Median spend by city." Could someone still be misled?
   Name one thing this chart does not show. (A median tells you nothing about
   the 18,500.00 member. Someone reading "median 26.09 for Basic" might
   conclude nobody spends much — the chart never says otherwise.)

## PART 6 — ASSEMBLE AND LABEL (20 min)

```python
def draw_all_charts(rows):
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    chart_spend_distribution(rows, axes[0][0])
    chart_visits_by_tier(rows, axes[0][1])
    chart_age_bands(rows, axes[1][0])
    chart_spend_by_city(rows, axes[1][1])
    fig.suptitle("Member statistics — anonymized, k>=5, no direct identifiers", fontsize=13)
    fig.tight_layout()
    fig.savefig("dashboard.png", dpi=110)
    print("wrote dashboard.png")

if __name__ == "__main__":
    publishable = load_publishable(DATA)
    draw_all_charts(publishable)
```

Then, for **each** of the four charts, add the same pair of lines somewhere
visible on the chart:

- **Statistic used:** which one, computed from which column.
- **What it hides:** one honest sentence.

A chart with no such note scores zero for that chart, even if the picture is
beautiful.

**Checklist before you commit — verify each, do not assume:**

- [ ] `load_publishable` is called, and `draw_all_charts` is *not* reachable
      without it
- [ ] Running `python3 dashboard.py` prints the gate result before any chart
- [ ] `dashboard.png` exists and all four panels are populated
- [ ] Every axis has a label and a unit
- [ ] No y-axis on a bar chart starts above zero
- [ ] No exact age, name, member ID, or zip appears anywhere in the image or
      in the printed output
- [ ] All four charts carry a statistic note and a blind-spot note

## PART 7 — THE FAILURE PROOF (10 min)

A dashboard that only works on good data is not tested. Temporarily set
`PUBLISHED_FIELDS = ["Age", "City"]` and run it again.

```bash
python3 dashboard.py
```

It must **refuse** and write no chart. Paste the failure message in your
notes. Then set it back.

**Answer in your notes:** what is the k of `Age + City` on your filtered data,
and how many members does that put at risk? (U3 L15: k = 1.)

## PART 8 — SAVE + PUSH (last 10 min)

```bash
git add dashboard.py dashboard.png
git commit -m "U3 L17 dashboard: four gated charts, each labelled with its statistic and blind spot"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `dashboard.py` and `dashboard.png`, pushed above, are the turn-in.
Submit the **push confirmation line** as a screenshot to this assignment on
Google Classroom.

Your push message must include:

1. the gate output line showing the pass
2. the **median** and **mean** of `Spend_USD`
3. the k of your published data, and the number of members still individually
   identifiable
4. one sentence: the blind spot of your weakest chart

If the gate output is not in the push message, I will assume you did not run
it.

Keep the terminal open — spot-checks.
