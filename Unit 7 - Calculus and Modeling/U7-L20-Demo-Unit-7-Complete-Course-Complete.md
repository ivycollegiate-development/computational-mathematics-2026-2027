# U7 L20 — Demo. Unit 7 Complete. Course Complete

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.5 — demonstrate a completed project and close the course

---

**Demo day.** Laptop, projector, five minutes, and the program runs live.

## THE FORMAT

| segment | minutes | what |
|---|---|---|
| Setup | 3 | start, load, confirm the environment works |
| **Talk** | **5** | the defense, from L17/L18 |
| **Live run** | **5** | the program, on screen, with output read aloud |
| Guard demo | 2 | the coverage refusal, deliberately |
| Questions | 10 | from L17 Part 3, and whatever else |
| Reset | 2 | restore the room for the next presenter |

Total 27 minutes of material in a 45-minute block, with the remainder as
slack. **The slack is deliberate** — the most common demo-day failure is
running over because the talk was eight minutes, not five.

## DEMO ORDER — NON-NEGOTIABLE

**Talk first, then the live run. Never the reverse.**

If you run first, the audience is watching a program and is not listening, and
the talk becomes a recap of what they just saw. If you talk first, every line of
output is confirmation rather than information. The talk frames the run; the run
is the evidence for the talk.

- ☐  Did you decide your order before today? Which, and why? ______

## THE TWO RUNS

### Run 1 — the happy path

The development data, the labelled events, the detector finds them.

- ☐  The exact command: ______
- ☐  The one line of output you want the room to see: ______
- ☐  Read it aloud. Which words do you emphasise? ______

### Run 2 — the refusal

A short series, below `MIN_POINTS`. The program declines to answer.

```text
INSUFFICIENT DATA: 8 points, need 20. No conclusion drawn.
```

- ☐  Why is this the more valuable demo? ______
- ☐  What does it say about the tool that the happy path does not? ______

That second answer is the one to have ready, because the refusal is what
separates a detector from a script. A tool that only produces answers on
suitable input is a script. A tool that tells you when its input is unsuitable
is a tool, and the suitability check is the part that took the most thought to
get right across seven units.

## THE CLOSING — COURSE COMPLETE

Eight units, four projects, one through-line. Say this part in your own words,
in under a minute, and make it specific rather than sentimental.

- ☐  **1.** What was the first thing you could do in Unit 0 that you could not
       do now? ______
- ☐  **2.** Name one thing you believed in September that was wrong: ______
- ☐  **3.** The one habit from L19 you are taking with you: ______
- ☐  **4.** The one thing you still cannot do: ______
- ☐  **5.** What you will do about 4 in your first two weeks of what comes next:
       ______

**5 is the only one being graded**, and it is graded on specificity. "I will
practise more" is not an answer. "I will work through the calculus problems I got
wrong on the unit test, in order, before the end of the month" is.

## WHAT HAPPENS AFTER TODAY

- **Mon May 31 – Thu Jun 3: finals**, four days, cumulative across Units 0–7.
- Your project files and this error log are the artifact you keep. **The error
  log is the most useful thing in your folder** — it is a record of how your
  reasoning actually changed, and it is worth more to a reader than any single
  finished assignment.
- ☐  6. Before you leave: make sure the log is committed, named clearly, and
       that the first and last entries are both present. ______
- ☐  7. Name the one tag from L19 Part 1 that you would keep if you could only
       keep one: ______

## THE LAST QUESTION

Ask yourself this in writing, and it is the honest closer to the whole course:

**1. Name a claim you made during this course that you believed was true, and
that turned out to be false only because you went and checked.**

______

Every student has one. The size of yours is a measure of how much verification
actually happened rather than how much confident writing did. Write it down,
keep it with the log, and — this is the part that matters — **be willing to
notice the next one.** The habit is not "being right." It is "finding out when
you are not," and that is a different thing, it is rarer, and it is what this
course was for.

## 🇹🇼 TAIWAN CONTEXT

The course closes on a habit that is worth naming in local terms, carefully, so
that it is neither overclaimed nor dismissed. Across four projects you built
things whose output was **checkable by design** — detectors that refuse when
their data is insufficient, threshold reports that state the cost in a unit an
operator can use, residuals printed individually so a wrong specification is
visible rather than hidden inside an RMSE. The transferable skill is not any one
technique. It is the disposition that says: *a number presented to me should
come with enough information that I can check it*, and the willingness to hold
your own outputs to the same standard.

That disposition matters most exactly where summary dashboards and inherited
thresholds are most trusted, which is everywhere. The version of it worth
keeping is small enough to do on a bad day with no time: **reproduce one figure
by hand before you believe it.** If it matches, you have learned something about
the system. If it does not, you have found the thing worth reporting — and over
this course, that second outcome is where essentially all the real learning
came from.

**Demo order: talk, then run, then the refusal. Good luck.**
