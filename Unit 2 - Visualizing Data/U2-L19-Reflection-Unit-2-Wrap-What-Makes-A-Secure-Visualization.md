# U2 L19 — Unit 2 Assessment + Reflection: What Makes A Secure Visualization?

**LO:** demonstrate mastery of Unit 2 (visualization, data integrity, privacy), then synthesize into one defensible principle.
**Estimated time:** 70 minutes (35 min paper + 35 min reflection).
**Schedule:** Half day — Unit 2 Assessment administered on the second day back from Fall Break, then reflection.

---

**No electronics during the assessment.** The written part is closed-computer — no
terminals, no notes, no neighbors. Everything on the paper is something we
built or debugged together in Unit 2. After the assessment, we reflect.

## PART 0 — BEFORE THE ASSESSMENT (5 min)

Put everything away except a pen or pencil. On the cover of your paper, write:

- your name
- one thing from Unit 2 you feel confident about
- one thing you hope is NOT on the test (be honest — it won't change the test,
  but it tells me where to spend review time in Unit 3)

Then close your notes. Deep breath. You have seen every problem type below.

## PART 0B — WRITTEN ASSESSMENT (35 min, no computers)

The exam is a standalone paper:
[`Unit 2 - Visualizing Data/Assessments/Unit-2-Assessment.md`](https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%202%20-%20Visualizing%20Data/Assessments/Unit-2-Assessment.md)

**Print it double-sided before class.** 50 points, 35 minutes, pen and paper.
Structure:

| Section | Points | Covers |
|---|---|---|
| A — Short Response | 20 | 10 questions: chart-type taxonomy, matplotlib syntax, `csv.DictReader` behavior, comment-line bug, sanity bounds vs outliers, `figure`/`savefig`/`show` order |
| B — Code Reading | 10 | Problem 11 (cleaning loop), Problem 12 (timeline chart bugs) |
| C — Data Integrity & Honesty | 10 | Provenance, blank-GPA bias, outlier vs signal, k-anonymity |
| D — Write Code | 10 | `load_and_clean(csv_path, sanity_dict)` — strip comments, convert, apply bounds, print drops, audit assert |

Do not deviate from the printed paper. The coversheet on the front carries your
name, your confident item, and the "one thing I hope is NOT on the test" note
from Part 0.

## PART 0C — GRADE RELEASE WALKTHROUGH (10 min)

We go over the answer key together, problem by problem. As we do:

- Mark each problem **got it** or **not yet** — no points yet, just honesty.
- For every **not yet**, write one sentence: *what specifically confused me?*
  "I didn't study" is not an answer. "I mixed up `plt.plot` and `plt.scatter`" is.

These sentences are raw material for your journal in Part 4.

---

## PART 1 — THE THREE THINGS THIS UNIT WAS ACTUALLY ABOUT (15 min)

Unit 2 was three lessons wearing one costume. Name each one, in your notes, with **a concrete example from your own project**:

1. **Visualization** — getting a picture to say one true thing clearly.
   - Which of your three charts did this best?
   - What made it **clear** rather than merely **informative**?

2. **Data integrity** — cleaning, auditing, and knowing what you do not have.
   - Name one thing your data could **not** answer, no matter how good your chart was.

3. **Privacy and honesty** — the audience is real. Your data came from a campus network; someone was behind every row.
   - What did you have to be careful **not** to show?

**The point of naming all three:** A visualization is only as good as the honesty of the pipeline that produced it. Perfect rendering of a lie is still a lie.

---

## PART 2 — GALLERY: WHAT MAKES A SECURE VISUALIZATION? (25 min)

We will walk the room's projects as a class gallery — screens up, no presenting required. For each project you see, you are looking for **one security question**:

> **If I built this chart, who could be hurt by it, and what would I have to change?**

Work through these together, out loud:

1. **The campus network dataset has daily `failed_logins` counts.** A chart of that makes a bad week look worse than it was. What is the honest fix?
   > *Discussion anchor:* Show the trend but also show the baseline. Contextualize the spike with "average failed logins = X, this week = Y× baseline."

2. **A chart of phishing reports by class period could let someone guess *which class* fell for them.** Same data, new risk. What changes?
   > *Discussion anchor:* Aggregate to school-wide. If you must show by period, suppress periods with <5 reports (k-anonymity). Never publish identifiers.

3. **Your histogram showed days with unusually low login success rates.** Naming those **dates** in your write-up is more useful to your security team — and more dangerous to whoever caused them. Where is the line?
   > *Discussion anchor:* Use "day 14" instead of "Oct 14" in analysis. Redact the exact date in public-facing versions; keep it in the internal security team version.

**There is no single right answer here. There is a defensible one, and you have to be able to say why yours is defensible.**

---

## PART 3 — THE PRINCIPLE (20 min)

Write, in your own words and in 3–4 sentences, your answer to this:

**What is the one rule you will follow for the rest of this class — and probably the rest of your life — about making charts from data that is not yours?**

**Rules you may NOT use as your answer:**
- "Be accurate" — table stakes, not a principle
- "Label everything" — table stakes, not a principle
- "Don't lie" — too vague

**I want the rule that only you would write, because it came from something that actually went wrong in your own work.**

**Example principles from past years:**
- "If removing a row changes the headline, the row stays — and I footnote why."
- "I never publish a chart I cannot explain to the person whose data it is."
- "Every chart I make has an 'honesty appendix' — one paragraph listing what I dropped, what I imputed, and what the chart cannot answer."

**Then: what is the HARDEST part of keeping that rule when you are in a hurry and someone is waiting for a chart?**

> Write the honest answer. "I forget" is not an answer. "The pressure to ship fast makes me skip the cleaning audit" is.

---

## PART 4 — CLOSING THE UNIT (journal, 10 min)

In your journal file, answer in a few sentences each:

1. Which skill from Unit 2 will you still be using in Unit 3?
2. What did the data you could **not** answer teach you about asking better questions?
3. One sentence to the student who sits next to you: what should they do differently in Unit 3?

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:
1. Your Part 1 notes, with all three themes named and your own example for each
2. Your Part 3 principle, written in your own words
3. Your Part 4 journal entries

Submit the screenshot to the U2 L19 assignment on Google Classroom.

**Keep the terminal open** — spot-checks.

---

## WHY THIS MATTERS (the bigger picture)

**Unit 2 was never about matplotlib.** Matplotlib is a tool. The unit was about the **discipline that sits on top of the tool**:

| Skill | Where you practiced it | Where it lives next |
|---|---|---|
| Chart type ↔ data type matching | U2 L05, L07, L10, L13 | Every chart you ever make |
| Three-label rule (title, x, y) | Every chart lesson | Every chart you ever make |
| Cleaning with audit trail | U2 L11, L15 | Every dataset you ever touch |
| Correlation ≠ causation | U2 L10 | Every relationship claim you ever make |
| Audience-aware design | U2 L14, project | Every presentation you ever give |
| Honesty audit (y-axis, dropped rows, unplotted data) | U2 L18, L19 | Every chart you ever publish |

**Unit 3 (Describing Data with Statistics) assumes you can:** load data, clean it with a documented script, choose the right chart type, label it, and write one honest paragraph about it. The statistics are new; the discipline is the same.

**Your Unit 2 project and journal carry forward.** The new repo is announced on the first day of Unit 3.

---

**This concludes Unit 2: Visualizing Data.**