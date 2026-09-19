# U2 L06 — Security Lens: Misleading Visualizations

**LO:** recognize common chart-manipulation tactics: truncated y-axes, cherry-picked ranges, and misleading scales.

No code today — paper, markers, and suspicion. Friday you learned to *make*
charts; today you learn what a chart can be made to say that the data does not.
This is a security lesson: a misleading chart is a lie dressed as evidence, and
lies like that move money, budgets, and policy.

## PART 1 — WARM-UP: TRUST THIS CHART? (10 min)

Imagine this chart, shown at a school board meeting, demanding more security
budget:

> A bar chart titled **"Cyber incidents are exploding!"** — two bars, one for
> last month (45 phishing reports) and one for this month (47 reports). The
> y-axis starts at **44**, so the second bar looks roughly **three times** as
> tall as the first.

Nothing is fake: 45 and 47 are real numbers, the bars are drawn accurately
*from that axis*. And yet the honest story is: reports went up by 4%. One
truncated number at the bottom of the axis — the y-axis floor — turned "basically
flat" into "exploding."

In your notes: what single change to this chart would make it honest?

## PART 2 — THE THREE TACTICS (15 min, notes as we go)

**Tactic 1 — Truncated y-axis.** Start the y-axis at a number other than zero.
For bar charts this is nearly always misleading, because your eye compares bar
*areas* — a bar that is 2x taller looks like "2x more." (Line charts are
different: a zoomed y-axis is honest there when the interesting action is a
few-degree change.)

**Tactic 2 — Cherry-picked ranges.** Choose the window of time (or the slice of
data) that supports the story and quietly drop the rest.

> A line chart titled **"Scores collapsing!"** shows test scores from March to
> June falling from 84 to 78. What the chart leaves out: in February scores
> were 77, so the *honest* picture is 77 → 84 → 78 — a wobble, not a collapse.

Ask of every range chart: *what is not shown?* Which months got cut off, and
why those?

**Tactic 3 — Misleading scales.** Units or scales chosen to exaggerate:

- a y-axis measured in *percent change* when the reader expects raw numbers
- axes chosen after seeing the data so one point becomes a dramatic spike
- a bar chart where bar *length* encodes one thing but bar *shading or size*
  suggests another (3D bars are notorious — the front bar always looks bigger)
- two lines on one chart with two hidden y-axes scaled so they look perfectly
  correlated

## PART 3 — WORKED EXAMPLE: ONE DATASET, TWO CHARTS (15 min)

Same data, plotted two ways. Here are the phishing reports from a campus
security dataset (the one you will meet in Tuesday's lab), five weeks:

| Week | Reports |
|------|---------|
| 1 | 12 |
| 2 | 14 |
| 3 | 13 |
| 4 | 15 |
| 5 | 20 |

**Dishonest version** (a bar chart): y-axis runs from 10 to 20; title says
*"Phishing surges 67%!"* Week 1's bar is invisible, Week 5's tower looks like
the sky is falling. Every number is technically correct.

**Honest version** (same bar chart): y-axis starts at **0**; title says
*"Phishing reports rose in week 5."* Now the bars tell the truth — a quiet
month, a bump at the end. Same data, opposite message.

In small groups, compare the two:

- What exactly did the dishonest version change? (Three things: axis floor,
  title framing, and what the reader's eye does.)
- Who benefits when a reader believes "67% surge"?
- Write your group's one-sentence rule: *when is a y-axis allowed to not start
  at zero?*

## PART 4 — YOUR TASK: SKETCH THE HONEST VERSION (20 min)

On paper, redraw one of these dishonest charts honestly. You get the
description of the lie and the real data — your job is a truthful chart:

1. *"Downloads collapsing!"* — bar chart, y-axis from 900 to 1000, weekly
   downloads: 930, 955, 970, 962, 988. (Sketch the honest bars and an honest
   title.)
2. *"Study time pays off — until it doesn't!"* — line chart showing only hours
   0–6 of a study-vs-score trend where the data runs 0–12 and keeps rising
   through hour 12. (Sketch the honest full range and title it truthfully.)
3. *"Campus WiFi perfectly safe!"* — a login-success-rate line chart with the
   y-axis running 0–100%, so a drop from 98% to 90% is invisible. (Here a
   *zoomed* y-axis is the honest choice — sketch it and write why this one is
   different from #1.)

Swap sketches with a partner. Your partner's test: from the sketch alone, could
a stranger state the true story in one sentence? If not, it isn't done.

## PART 5 — JOURNAL (last 10 min)

Open the lab repo you already have on your machine (`cd ~/compmath-lab`), then:

```bash
touch journal-1012.md
```

Answer in 3–4 sentences in `journal-1012.md`:

- Which of the three tactics would be hardest for *you* to spot in the wild,
  and why?
- Where have you already seen a chart you now suspect? (Ad, news, game stats,
  school data — anywhere.)

## PART 6 — PUSH (last 5 min)

```bash
cd ~/compmath-lab
git add journal-1012.md
git commit -m "Day 1012 journal misleading charts"
git push
```

- **Asked for a username/password?** Personal Access Token, not your GitHub
  password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your honest sketch from Part 4 (paper or a photo of it, whichever your
   teacher allows)
2. your journal answers
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep your sketch — Tuesday's lab grades honesty, not art.
