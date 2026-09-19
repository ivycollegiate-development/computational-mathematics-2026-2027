# U2 L14 — Reflection: Visualizing For An Audience

**LO:** design a visualization for a specific audience and purpose.

Today starts on paper and ends in the terminal — you will need your workspace for
Parts 3 and 4.

## PART 1 — OPENING REVIEW: WHAT HAPPENED LAST WEEK (10 min)

Before anything new, let's reconstruct where Unit 2 stands. Answer these together
before I show any charts:

- What are the four pieces of "plot anatomy" every chart we have made must have?
  (Hint: two are labels, one is a title, one is a legend.)
- What does `csv.DictReader` give back when you loop over it — and what does each
  row look like?
- When we cleaned the threat data, what kinds of "dirty" rows did we have to throw
  out or fix?
- What is the difference between a line chart and a bar chart, and when would you
  pick each one?

Write your answers in your notes first; then we go over them as a class. By the end
of this part you should be able to say in one sentence: **what does a chart owe the
person who reads it?**

## PART 2 — SAME DATA, THREE AUDIENCES (20 min)

I will put one chart on the screen — the daily phishing reports from our campus
threat dataset. Now imagine it has to be shown to three different audiences:

- the **security team** — they need to spot which days had attack spikes so they
  can respond
- the **principal** — she needs to know whether the problem is getting better or
  worse overall, in one glance
- the **parents** at an open house — they need to know their kids are safe, without
  jargon

In small groups, for each audience, decide on paper:

- which chart **type** you would use (line? bar? histogram?), and why
- what **title** you would put on it — write the exact words
- which numbers you would **highlight** and which you would leave out

Then we discuss the hard question: are these three charts "the same data" or
"different stories"? Where is the line between **simplifying for an audience** and
**misleading** them?

Each group posts one chart sketch on the board. We vote: clearest, and most honest.

## PART 3 — PLAN YOUR PROJECT CHARTS (15 min)

Open your workspace. First command, always:

```bash
pwd
```

Then open your data-lab repo and pull anything new:

```bash
cd ~/compmath-u2-data-lab
git pull
```

Tomorrow we launch the Unit 2 project (U2 L15): three required visualizations from
`u2_campus_threat_daily.csv`. Today, on paper, plan them. For each of the three:

- the daily timeline of phishing reports and failed logins
- the weekday-vs-weekend comparison
- the histogram of login success rate

write in your planning notes:

- ☐  chart type I will use, and one sentence on why it fits the question
- ☐  what goes on each axis (and the units)
- ☐  the exact title I will give it — and **who my audience is**
- ☐  one thing that could go wrong (unclean data? a gap in the dates?)

## PART 4 — JOURNAL (last 5 min)

Open your journal file in your data-lab repo and answer in 2-3 sentences:

- Which of the three audiences was hardest to design for, and why?
- What is the one rule you will follow so your charts are clear **and** honest?

## PART 5 — PUSH (last 10 min — same loop as last week, now routine)

Your journal is already inside your repo, so push it. Type each command exactly:

```bash
cd ~/compmath-u2-data-lab
git add analysis.md
git commit -m "L14 audience planning journal"
git push
```

- **Asked for a username/password?** Use your GitHub username plus your Personal
  Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your Part 2 planning notes (the three audience chart sketches)
2. your Part 3 project planning checklist (all three charts planned)
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
