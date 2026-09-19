# U2 L17 — Reflection: Peer Review Of Visualizations

**LO:** give and receive feedback on visualizations — clarity, honesty, impact.

Today is a review day. You read a partner's repo through their GitHub link, score
it, and then revise one of your own charts from the feedback you receive.

## PART 1 — WHAT MAKES A CHART GOOD? (10 min)

Before you score anyone, agree on the standard. In your notes, answer:

- What is the difference between a chart that is **unclear** and one that is
  **dishonest**? (One is a mistake; the other is a lie.)
- Name one way a chart can be technically correct but still mislead its audience —
  think about the three-audience exercise from Monday.

We will use three scoring dimensions all day, each 1-5:

| Dimension | 5 means... |
|-----------|-----------|
| **Clarity** | I understood the chart with no explanation: title, labels, legend all do their job |
| **Honesty** | The chart says exactly what the data says — no dropped context, no inflated axes, no hidden gaps |
| **Impact** | The one thing the audience should notice jumps out immediately |

## PART 2 — STRUCTURED SWAP (25 min)

Get your partner's repo link (their GitHub URL from yesterday's PR). Clone or read
it on github.com, then review **all three** required charts. For each chart, fill
out the feedback form in your notes:

**Feedback form — one per chart:**

- Chart: timeline / weekday / histogram (circle one)
- Clarity: 1 2 3 4 5 — because: \_\_\_
- Honesty: 1 2 3 4 5 — because: \_\_\_
- Impact: 1 2 3 4 5 — because: \_\_\_
- **One suggestion** — specific and actionable ("move the legend outside the plot",
  "your y-axis starts at 30, which shrinks the visible drop — start at 0 or say why")

Rules of review:

- ☐  Score before you talk — form first, conversation second
- ☐  Every score gets a "because"
- ☐  Every review ends with one suggestion, not zero and not ten
- ☐  "Looks good" is not a review

Then swap roles. You will each give and receive a full review.

## PART 3 — REVISE ONE CHART FROM FEEDBACK (20 min)

Open your own repo and pick the **one** chart your reviewer's suggestion would
help most:

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
```

- ☐  Make the exact change your partner suggested (or, if you disagree, write one
     sentence in your journal defending why)
- ☐  Re-run `python3 project.py` and regenerate the PNG
- ☐  Update that chart's paragraph in `analysis.md` if the change altered the story

Commit the revision:

```bash
cd ~/compmath-u2-data-lab
git add project.py analysis.md
git commit -m "revise chart from peer feedback"
git push
```

(Password prompt = Personal Access Token, not your GitHub password.)

## PART 4 — JOURNAL (last 10 min)

Open your journal file in your repo and answer in 3-4 sentences:

- What did your partner catch that you could not see yourself? Why do you think
  you missed it?
- Which of the three dimensions — clarity, honesty, impact — is hardest to get
  right, and why?
- What is the one habit you will carry into every chart you ever make?

## PART 5 — PUSH (last 5 min — same loop, now routine)

```bash
cd ~/compmath-u2-data-lab
git add analysis.md
git commit -m "L17 peer review journal"
git push
```

- **Asked for a username/password?** Use your GitHub username plus your Personal
  Access Token (PAT) — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your completed feedback forms (all three charts, scores + suggestion)
2. your revised chart's new PNG (the change your partner suggested)
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
