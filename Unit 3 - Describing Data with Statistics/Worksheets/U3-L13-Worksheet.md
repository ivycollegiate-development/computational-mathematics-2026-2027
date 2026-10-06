# U3 L13 — Preview: Specification for the Privacy-Aware Stats Dashboard

Names: ___________________________  Date: ____

Paper day, no laptop. This is a specification, not a sketch: it must be exact enough that a classmate could build your dashboard without asking you one question. Keep it — you are graded against it during the project labs and again during peer review.

## 1: Decide your audience

You are building a privacy-aware statistics dashboard for a 120-member organisation from `u3_project_dataset.csv`, summarising age, city, visits, spend, and tier without publishing anyone's identity. The privacy filter runs **first**, and the dashboard refuses to render if it fails.

1. Your audience, one of: (A) membership committee, (B) prospective member, (C) journalist or auditor, (D) the board. Circle it and write it at the top of your spec: ______________

2. For that audience, which of age, city, visits, spend, and tier must appear, and which must not?

   Must appear: ______________________________________________________

   Must not: _________________________________________________________

3. If you chose the journalist, they are *trying* to identify people. Write how that changes your threshold:

   _____________________________________________________________________

## 2: Choose your four charts

Name the **exact statistic** and the **exact column** you group by. "A bar chart of spend" is not a specification.

| #          | Question the chart answers     | Group by       | Statistic plotted     | Why this statistic         |
| ---------- | ------------------------------ | -------------- | --------------------- | -------------------------- |
| 1          | ______________________         | __________     | __________            | ______________________     |
| 2          | ______________________         | __________     | __________            | ______________________     |
| 3          | ______________________         | __________     | __________            | ______________________     |
| 4          | ______________________         | __________     | __________            | ______________________     |

4. Bars start at zero. State, for any bar chart in your table, where its y-axis begins: ______________

5. Every "why this statistic" cell must survive the question *what does this hide?* Write the one thing your riskiest chart hides: ______________________

6. Average spend by tier makes the **Basic** tier look like the biggest spenders. If one of your charts is spend by tier, state which statistic protects the reader from this: ______________

## 3: Specify the refusals

The graded heart of the project. Your dashboard must be able to say no. Each rule is one sentence beginning "The dashboard must refuse to…".

7. The dashboard must refuse to…

   _____________________________________________________________________

8. The dashboard must refuse to…

   _____________________________________________________________________

9. The dashboard must refuse to…

   _____________________________________________________________________

10. The dashboard must refuse to…

   _____________________________________________________________________

Facts about the data you have already established:

- `Age + Zip_Code` is unique across all 120 members.
- Grouping by `Zip_Code` and requiring k ≥ 5 keeps zero rows.
- Four tiers of 30 members each pass a k ≥ 5 rule; five cities of 20–40 also pass.
- One member has `Spend_USD` of **18,500.00** in the **Basic** tier; dropping them moves the Basic mean from **648.03** to **32.44**.
- `Zip3` (3-digit prefix) maps to exactly one `City`, so it adds no privacy.
- No age-band width makes `Age + City` safe: a 15-year band gives k = 15 alone, but k = 1 as soon as `City` joins it, at every width from 5 to 30 years.

11. Will you publish `Age`? Exact, 5-year, 10-year, or 15-year band? What *k* does your choice produce? ______________

12. Will you publish `Zip_Code` at all? If you keep a prefix, explain why it is not merely a disguised `City`:

   _____________________________________________________________________

13. Will you publish `Member_ID`? Argue both sides, then decide: ______________________

   _____________________________________________________________________

14. What is your `MIN_K`, and what is the *specific* chart that `MIN_K` blocks?

   _____________________________________________________________________

## 4: Define finished

Your definition of done must include all five of these:

☐  The dashboard renders **four** charts.
☐  The privacy filter runs **before** any chart is drawn, provable by running your code on a deliberately unsafe dataset and watching it stop.
☐  If the filter fails, the program prints **why** in plain English and exits without drawing anything.
☐  Every chart shows **which statistic** it plots and **what it hides**.
☐  The report states the *k* of the published data and admits if it is below your own threshold.

15. Which of those five are you most tempted to skip, and why? ______________________

## 5: Plan the four labs

| Lab        | Date           | What you build                           | What done looks like       |
| ---------- | -------------- | ---------------------------------------- | -------------------------- |
| L14        | Dec 4          | `stats_engine.py` — load, compute, summarise | ______________________     |
| L15        | Dec 7          | `privacy_filter.py` — the gate, and the refusals | ______________________     |
| L17        | Dec 9          | `dashboard.py` — the four charts         | ______________________     |
| L19        | Dec 11         | Fix the findings from peer review        | ______________________     |

**TURN IN** — this specification sheet at the end of the period.
