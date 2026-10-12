# U2 L14 — Reflection: Visualizing For An Audience

**LO:** design a visualization for a specific audience and purpose; articulate the line between simplifying and misleading.

**Estimated time:** 70 minutes (was ~50). We move slower so the audience-design habit becomes deliberate.

---

Today starts on paper and ends in the terminal — you will need your workspace for Parts 3 and 4.

---

## PART 1 — OPENING REVIEW: WHAT HAPPENED IN UNIT 2 SO FAR (15 min)

Before anything new, let's reconstruct where Unit 2 stands. Answer these in your notes first; then we go over them as a class.

1. What are the **four pieces of plot anatomy** every chart we have made must have? (Hint: two are labels, one is a title, one is a legend — but legend is only when multiple series exist.)

   > **Expected:** Title (states the question), x-label (with units), y-label (with units), and legend (when >1 series is plotted).

2. What does `csv.DictReader` give back when you loop over it — and what does each row look like?

   > **Expected:** An iterator of `dict` objects, one per data row. Keys are the header column names. All values are **strings** — numeric columns must be converted with `float()` or `int()`.

3. When we cleaned the performance data in U2 L11, what kinds of "dirty" rows did we have to throw out or fix?

   > **Expected:** Blank cells (missing values), impossible values (GPA > 4.0, Age < 10), type traps ("N/A" in numeric columns).

4. What is the difference between a line chart and a bar chart, and when would you pick each one?

   > **Expected:** Line chart = x-axis is continuous/ordered (time, numeric sequence); shows trend. Bar chart = x-axis is categorical (groups, bands, categories); compares amounts.

5. What does a histogram show that a scatter plot does not?

   > **Expected:** Histogram = distribution of **one** variable (center, spread, skew). Scatter = relationship between **two** variables (direction, strength, form).

**By the end of this part you should be able to say in one sentence:** **A chart owes its reader honesty first, clarity second, and beauty never at the expense of the first two.**

---

## PART 2 — SAME DATA, THREE AUDIENCES (25 min)

I will put one chart on the screen — the daily phishing reports from our campus threat dataset (`u2_campus_threat_daily.csv`). Now imagine it has to be shown to three different audiences:

| Audience | What they need to do with the chart | What they already know |
|---|---|---|
| **Security team** | Spot which days had attack spikes so they can respond (investigate, block, alert) | Know the systems, jargon, normal baselines |
| **Principal** | Know whether the problem is getting better or worse overall, in one glance | Knows the school, not the technical details |
| **Parents** at an open house | Know their kids are safe, without jargon | Knows nothing technical; trusts the school |

In small groups, for each audience, decide on paper:

1. **Which chart type** you would use (line? bar? histogram?), and **why**.
2. **What exact title** you would put on it — write the exact words.
3. **Which numbers you would highlight** and which you would leave out.

**Then we discuss the hard question:** Are these three charts "the same data" or "different stories"? Where is the line between **simplifying for an audience** and **misleading** them?

**Each group posts one chart sketch on the board.** We vote: clearest, and most honest.

**In your notes after the discussion:** Write your personal answer to the "simplifying vs misleading" line — one sentence you will use as a filter for every chart you build this project.

> **Example filter:** "If removing a detail would change the reader's conclusion, it stays — even if it makes the chart busier."

---

## PART 3 — PLAN YOUR PROJECT CHARTS (20 min)

Open your workspace. First command, always:

```bash
pwd
```

Then open your data-lab repo and pull anything new:

```bash
cd ~/compmath-u2-data-lab
git pull
```

**Tomorrow (U2 L15) we launch the Unit 2 project:** three required visualizations from `u2_campus_threat_daily.csv`. Today, on paper, plan them. For each of the three, write in your planning notes:

### Chart 1 — Daily timeline of phishing reports and failed logins
- ☐ Chart type I will use, and one sentence on why it fits the question
- ☐ What goes on each axis (and the units)
- ☐ The exact title I will give it — and **who my audience is**
- ☐ One thing that could go wrong (unclean data? a gap in the dates?)

### Chart 2 — Weekday-vs-weekend comparison
- ☐ Chart type I will use, and one sentence on why it fits the question
- ☐ What goes on each axis (and the units)
- ☐ The exact title I will give it — and **who my audience is**
- ☐ One thing that could go wrong

### Chart 3 — Histogram of login success rate
- ☐ Chart type I will use, and one sentence on why it fits the question
- ☐ What goes on each axis (and the units)
- ☐ The exact title I will give it — and **who my audience is**
- ☐ One thing that could go wrong

**Why plan on paper first:** The project is 4 lessons (U2 L15–L18). Students who code without a plan spend U2 L15–L16 redoing charts. Students who plan spend U2 L15–L16 building exactly what they envisioned and U2 L17–L18 polishing.

---

## PART 4 — JOURNAL (10 min)

Open your journal file in your data-lab repo (or create it if missing):

```bash
touch journal-$(whoami).md
```

Open `journal-$(whoami).md` in VS Code and answer in 3–4 sentences:

1. Which of the three audiences was hardest to design for, and why?
2. What is the one rule you will follow so your charts are clear **and** honest?
3. Look back at your U2 L10 scatter plots and U2 L13 histograms. If you had to present *one* of those to parents, what would you change?

**Why a journal file in the repo:** It creates a permanent, versioned record of your design thinking. Future you (and I) can see how your audience-awareness evolved across the unit.

---

## PART 5 — PUSH (10 min — same loop as last week, now routine)

Your journal is already inside your repo, so push it. Type each command exactly:

```bash
cd ~/compmath-u2-data-lab
git add journal-$(whoami).md
git commit -m "L14 audience planning journal"
git push
```

**Reminders:**
- **Asked for a username/password?** Use your GitHub username plus your **Personal Access Token (PAT)** — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line. The loop is now: Edit → add → commit → push.

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:
1. Your Part 2 planning notes (the three audience chart sketches)
2. Your Part 3 project planning checklist (all three charts planned)
3. The successful `git push`

Submit the screenshot to the U2 L14 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS (the bigger picture)

**Audience design is not a lesson — it's a constraint on every chart you will ever make.** The Unit 2 project (U2 L15–L18) requires you to state your audience for each of the three visualizations. The grader (me) will evaluate whether the chart *actually serves* that audience — not just whether it runs without crashing.

**The simplifying vs misleading line:**
- **Simplifying:** Removing noise the audience cannot act on (e.g., dropping gridlines for parents).
- **Misleading:** Removing context the audience needs to reach the right conclusion (e.g., truncating the y-axis to exaggerate a small trend for the principal).

**The audit trail:** Your journal, your planning notes, and your git history together form the evidence that you designed deliberately. "I just picked a line chart" is not a design rationale. "I picked a line chart because the principal needs to see the trend over time, and the x-axis is continuous dates" is.

**Next:** U2 L15 — Project Launch: Visualizing Threats  
[U2-L15-Project-Launch-Visualizing-Threats.md](U2-L15-Project-Launch-Visualizing-Threats.md)