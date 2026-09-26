# U3 L13 — Preview: Build the Privacy-Aware Stats Dashboard

**LO:** specify what your dashboard will show, what it will refuse to show, and what "finished" means.

You have done the mathematics and you have done the security work. The next
four lessons are one project, and this is the day you decide what it *is*.

Paper day. No laptop. This is a specification, not a sketch — a sketch is a
picture of a dashboard, a specification says exactly what it will do and what
it must never do.

## WHAT YOU ARE BUILDING

A **privacy-aware statistics dashboard** for a 120-member organisation, built
from `u3_project_dataset.csv`. It summarises members — age, city, visits,
spend, tier — **without publishing anyone's identity**.

The defining feature of this project is not the charts. It is that **the
privacy filter runs first, and the dashboard refuses to render if it fails.**
You built the requirements in L10, you measured the cost in L12, and tomorrow
you build the engine that enforces them.

## PART 1 — DECIDE YOUR AUDIENCE (10 min)

A dashboard has an audience, and the audience determines what is safe to
show. Choose one and write it at the top of your spec:

- (A) The **membership committee** — needs spend by tier to set pricing.
- (B) A **prospective member** — needs to know what membership is like.
- (C) A **journalist or auditor** — needs to verify the numbers are honest.
- (D) The **board** — needs a one-page summary of member health.

Answer in writing: *for your audience, which of age, city, visits, spend, and
tier must appear?* If your audience is the journalist, note that a journalist
is *trying* to identify people — how does that change your threshold?

## PART 2 — CHOOSE YOUR CHARTS (15 min)

You have four charts to draw. For each, name the **exact statistic** you will
plot and the **exact column** you will group by. You may not write "a bar
chart of spend" — that is not a specification.

| # | Question the chart answers | Group by | Statistic plotted | Why this statistic |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

**Rule from L09: bars start at zero.** If any of your charts is a bar chart,
its y-axis begins at 0. No exceptions, and I will check.

**Rule from L03/L09: say which statistic and why.** For every chart, the
"why this statistic" cell must survive the question *"what does this hide?"*
A mean with a comment, or a median because one member is enormous.

**Watch for this trap.** Average spend by tier makes the **Basic** tier look
like the biggest spenders. That is arithmetically true and completely
misleading, and it will be a grading criterion. If your chart 1 is spend by
tier, state in your spec which statistic protects the reader from this.

## PART 3 — SPECIFY THE REFUSALS (20 min)

This is the graded heart of the project. Your dashboard must be able to say
**no**. Write each rule as a sentence beginning "The dashboard must refuse
to…".

1. The dashboard must refuse to…
2. The dashboard must refuse to…
3. The dashboard must refuse to…
4. The dashboard must refuse to…

Use these facts about the data, which you have already established:

- `Age + Zip_Code` is unique across **all 120** members.
- Grouping by `Zip_Code` and requiring k ≥ 5 keeps **zero** rows.
- Four tiers of 30 members each pass a k ≥ 5 rule; five cities of 20–40 also
  pass.
- One member has `Spend_USD` of **18,500.00** in the **Basic** tier, and
  dropping them moves the Basic mean from **648.03** to **32.44**.
- `Zip3` (3-digit prefix) maps to exactly one `City`, so it adds no privacy.
- No age-band width makes `Age + City` safe: a 15-year band gives k = 15 on
  its own, but k = 1 as soon as `City` joins it, at **every** width from 5 to
  30 years. If your dashboard publishes both, it fails the gate.

Now, decide and justify:

5. Will you publish `Age`? If yes, at what precision — exact, 5-year band,
   10-year band, 15-year band? What *k* does your choice produce?
6. Will you publish `Zip_Code` at all? If you keep a prefix, explain why it is
   not merely a disguised `City`.
7. Will you publish `Member_ID`? Argue both sides, then decide.
8. What is your `MIN_K`, and what is the *specific* chart that `MIN_K` blocks?

## PART 4 — DEFINE FINISHED (10 min)

A project without a definition of done produces infinite fiddling. Write
your definition. It must include:

1. The dashboard renders **four** charts.
2. The privacy filter runs **before** any chart is drawn, and I can prove it
   by running your code on a deliberately unsafe dataset and watching it stop.
3. If the filter fails, the program prints **why** in plain English and exits
   without drawing anything.
4. Every chart shows **which statistic** it plots and **what it hides**.
5. The report states the *k* of the published data and admits if it is below
   your own threshold.

Which of those five is the one you are most tempted to skip, and why?

## PART 5 — PLAN THE FOUR LABS (10 min)

| Lab | Date | What you build |
|---|---|---|
| L14 | Thu Dec 4 | `stats_engine.py` — load, compute, summarise |
| L15 | Mon Dec 7 | `privacy_filter.py` — the gate, and the refusals |
| L17 | Wed Dec 9 | `dashboard.py` — the four charts |
| L19 | Fri Dec 11 | Fix the findings from peer review |

Write one sentence per lab saying what *done* looks like. Keep this spec — in
four days you will be graded against it, including by your classmates, who
will read it during peer review on Dec 10.

## TURN IN

Hand in this specification sheet at the end of the period.

Be specific enough that a classmate could build your dashboard without asking
you a single question. Vague specs are the single most common reason the
dashboard labs run long.
