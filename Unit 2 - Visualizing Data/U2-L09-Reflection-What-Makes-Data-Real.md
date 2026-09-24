# U2 L09 — Reflection: What Makes Data Real?

**LO:** reflect on data provenance — where does data come from, and can you trust it?

Today starts on paper and ends in the terminal — you will need your workspace for
Parts 3 and 4. No coding until late. Your job today: figure out where data
actually comes from, and whether you should believe it.

## PART 1 — OPENING REVIEW: WHAT HAPPENED LAST WEEK (10 min)

Before anything new, let's reconstruct Wednesday's lesson (U2 L08 — your first
plotted charts).

Answer these together before I show any code:

- What are the three things every honest chart needs? (Title, axis labels, units.)
- Why did `plt.show()` not do anything useful in the terminal, and what did we
  use instead?
- What does `savefig()` do, and where did your file end up?

Write your answers in your notes first; then we go over them as a class. By the
end of this part you should be able to say in one sentence: **a chart is only as
honest as the data underneath it.**

## PART 2 — PROVENANCE CHAIN: WHO, WHY, HOW, WHEN (15 min)

Every dataset has a backstory. In small groups, pick any dataset you can think
of — the weather report, a video game leaderboard, a class survey — and build its
provenance chain. Four questions, in order:

1. **Who** collected it? (A person? A sensor? A program?)
2. **Why** did they collect it? (Were they paid? Curious? Selling something?)
3. **How** did they collect it? (Interview? Automatic logging? A guess?)
4. **When** did they collect it? (Last week? Ten years ago? Continuous?)

Each group posts its chain on the board. Then we sort the datasets into "I'd
trust this" versus "I'd double-check this" — and the interesting answer is
almost always: **it depends on what I'm using it for.**

## PART 3 — IS OUR DATA REAL? (15 min)

Open your **compmath-u2-data-lab** repo — start in the terminal, always:

```bash
pwd
cd ~/compmath-u2-data-lab
ls data
```

You have been using `data/u2_student_performance_data.csv` all week: 1,000 rows
of students with study hours, sleep, GPA, absence rates. Now the uncomfortable
question: **is any of this real?**

First answer in your notes, then discuss as a class:

- Do 1,000 real students' records with this many personal columns seem likely
  to be sitting in a public CSV?
- If I told you a program generated these rows from random ranges, what clues
  would you look for in the file itself?
- Open the file in VS Code and scroll. Write down at least two clues that
  support "synthetic" and two that support "real" — then defend your call.

The honest answer for our file: it is **synthetic** — generated to be realistic
enough to practice on. That is not a weakness. Synthetic data lets us practice
on numbers that behave like the real thing without shipping anyone's private
information. But it changes what we are allowed to *claim* from our charts.

## PART 4 — HOW CAN YOU TELL? (10 min)

A provenance checklist, one line per item. In your notes, write what each
question catches:

- **Is there a source named?** A file with no origin story is a red flag.
- **Do the rows contradict themselves?** A 3-year-old with a GPA is data that
  was never checked against reality.
- **Are the numbers *too* clean?** Real measurements are messy and uneven.
- **Is it surprisingly complete?** Real data almost always has holes.
- **Does the date fit the story?** Data collected before the thing existed is
  fabricated.

I will hand out two tiny files on the board — one real-looking, one synthetic —
and you vote. We keep score on how often the class is right.

## PART 5 — JOURNAL (last 5 min)

In your data-lab repo (you are already inside it — verify with `pwd`):

```bash
touch journal-1019.md
```

Open `journal-1019.md` in VS Code and answer in 3–4 sentences:

- Where did our performance data come from, and why does that matter for the
  charts I made last week?
- Name one real-world dataset you use (or that is used on you). What is its
  provenance chain, and what would you have to believe to trust it?
- One rule I will apply to every dataset from here on:

## PART 6 — PUSH (last 10 min — same loop as Wednesday, now routine)

Your journal is already inside your repo, so push it. Type each command exactly:

```bash
cd ~/compmath-u2-data-lab
git add journal-1019.md
git commit -m "Day 1019 journal: data provenance"
git push
```

- **Asked for a username/password?** Use your GitHub username plus your Personal
  Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line. Edit → add → commit → push.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your `ls data` output with the dataset files visible
2. your journal answers open in VS Code
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
