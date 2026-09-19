# U2 L04 — Reflection: Visualizing a News Story

**LO:** analyze a real-world visualization from the news: what story it tells, what it might hide, and who it is for.

Paper and reflection day — **no code, no terminals** for the discussion. You
need your eyes, your notes, and at the end your journal and a push. Today you
become a skeptical reader of charts, which matters more than making them.

## PART 1 — WARM-UP: THE CHART ON THE BOARD (5 min)

A chart is up front — a real one published by a news outlet. Before I say
anything about it, write down three things you notice and one thing you
wonder. Not judgments yet. Just observations.

## PART 2 — THE INTERROGATION: FIVE QUESTIONS FOR ANY CHART (15 min)

Copy these five questions into your notes. They apply to every chart you
will ever see, in class or in the wild:

1. **What is plotted?** What exactly is on each axis — quantity, unit, time
   span? Are the units honest and readable?
2. **What is omitted?** What is *not* shown? Where do the axes start — zero,
   or some convenient number? Are there years, groups, or cases missing?
3. **Who made it?** A journalist? A company selling something? A government
   agency? What do they *want* you to conclude?
4. **Who is the audience?** You? Voters? Investors? What does that audience
   already believe, and how might the chart feed it?
5. **What is the story vs. the truth?** Does the visual emphasis (big red
   arrow, truncated axis, cherry-picked window) match what the underlying
   numbers actually support?

Now apply all five to the chart on the board. Work through them with your
table — one question per person, then compare notes.

## PART 3 — CASE STUDY: THE TRUNCATED AXIS (15 min)

Handout time. The classic trick: two line charts of the *same* data, one
with the y-axis starting at zero, one starting just below the smallest value.
The second one makes a tiny change look like a cliff.

On the handout (also drawn on the board):

```text
Data:   Jan 100,  Feb 101,  Mar 103,  Apr 102,  May 104

Chart A: y-axis from 0 to 110     → gentle, honest slope
Chart B: y-axis from 99 to 105    → dramatic, terrifying mountain
```

Both charts are technically true. In your notes:

- What changed between A and B? (Not the data — only the *window*.)
- Which chart would a company fighting a "crisis" narrative publish?
- Write your own rule: *when is a non-zero baseline acceptable, and when is
  it manipulation?* (Hint: for temperature, zero isn't special. For
  money, it usually is.)

## PART 4 — GROUP TASK: RUN THE FIVE QUESTIONS ON A SECOND CHART (15 min)

Each table gets a different real news visualization (printed handouts).
As a group, fill in the five-question worksheet for your chart:

- Question-by-question, one written sentence per person.
- Then your group's verdict, in one sentence: **honest, misleading, or
  somewhere in between — and what one change would fix it?**

Groups present their verdict in one minute each. The class votes: agree or
push back.

## PART 5 — WHAT THIS MEANS FOR YOUR OWN PLOTS (10 min)

Back to your own work. Look at yesterday's scatter plot in your mind (or
your notes):

- Which of the five questions does YOUR chart fail? Be honest — likely
  candidates: no context on what a "study hour" is, no mention that 52
  students ≠ all students.
- Write one sentence: *the next chart I make will ___ that my last one
  didn't.*

## PART 6 — JOURNAL (last 5 min)

In your terminal (you'll need it for the push):

```bash
pwd
cd ~/compmath-lab
touch journal-u2l04.md
```

Answer in the file, 2-3 sentences each:

- Which of the five questions is hardest to answer, and why?
- From today's charts: what is the single most effective way a chart can
  mislead without telling a single lie?
- What will you now *check for* before trusting a chart in the wild?

## PART 7 — PUSH (last 10 min — same loop, now routine)

```bash
cd ~/compmath-lab
git add journal-u2l04.md
git commit -m "U2 L04 news chart reflection journal"
git push
```

- **Asked for a username/password?** GitHub username + Personal Access Token
  (PAT) — never your GitHub password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your five-question worksheet answers (or Part 3 notes) on paper
2. your journal file open with your Part 6 answers
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
