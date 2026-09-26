# U3 L22 — Paper Check: Unit 3 Statistics and Privacy

**LO:** demonstrate, on paper, the full Unit 3 chain — from a raw number to a
defensible claim that respects both statistics and privacy.

**Closed notes. Paper only. No code, no terminal. If you have a computer open,
close it.** Every question here is answerable by hand. That is the point: this
is the exam of whether you understand the ideas rather than whether you can
type them.

**SHOW YOUR WORK.** A bare answer to a percentile question earns half credit.
For every numeric answer, write the setup line and then the answer.

You have 55 minutes. There are 25 points.

---

## PART A — DESCRIPTIVE STATISTICS (8 points)

### A1. (2 pts) A percentile, by hand.

The recorded response times (seconds) for 10 form submissions:

```
41, 55, 38, 62, 47, 51, 44, 58, 39, 35
```

Sort them, then find the 30th percentile using the same method as U3 L08:
`k = (n - 1) x p`, and interpolate between the two values that bracket k.

- Sorted: ____________________________________
- k = ______
- The bracketing values are ______ and ______
- **p30 = ______ seconds**

### A2. (2 pts) The five-number summary and the IQR.

Using the same 10 values:

- min = ______  q1 = ______  median = ______  q3 = ______  max = ______
- IQR = q3 - q1 = ______
- Lower fence = q1 - 1.5 x IQR = ______
- Upper fence = q3 + 1.5 x IQR = ______

### A3. (1 pt) Outliers by the IQR rule.

List every value from A2 that falls beyond either fence: ____________________

**If your answer is "none," that is a correct and interesting answer.** Do not
change it to force a finding. Explain in one line why a value can be the
largest in the set and still sit inside the fence: ____________________

### A4. (2 pts) Mean or median?

A club collects monthly spending from 12 members. The amounts are:

```
120, 130, 125, 140, 135, 128, 132, 138, 122, 134, 126, 700
```

- mean = ______
- median = ______

The club's treasurer wants to report "what a member typically spends per
month." Which statistic do you report, and why in one sentence? ______

- Now the treasurer instead wants to report "our total monthly membership
  revenue." Which statistic, and why? ______

The same two numbers, two legitimate questions, two different correct
answers. That is the whole lesson.

### A5. (1 pt) Standard deviation, conceptually.

Your friend says: "this dataset's standard deviation is 15, so a value of 15
away from the mean is completely normal."

Is that right? Explain in one sentence. ______

(Hint: what fraction of values should fall within **one** standard deviation,
if the data is roughly symmetric?)

---

## PART B — MISLEADING VISUALS (6 points)

### B1. (2 pts) The truncated bar chart.

A bar chart shows three bars of height 2, 3, and 4. The y-axis starts at 1.5
instead of 0.

- The **visual** height of the third bar, as a fraction of the tallest bar,
  is ______
- The **true** ratio of the third bar to the second is ______

Fill in the table for both a zero-based and a 1.5-based axis:

| axis range | visual height of bar 2 | visual height of bar 3 | ratio (3÷2) |
|---|---|---|---|
| 0 to 4 | | | |
| 1.5 to 4 | | | |

How many times bigger does the 1.5-based chart make the difference between
bars 3 and 2 look? ______

### B2. (2 pts) Mean, or the story you want?

The Basic-tier average monthly spend is **$648.02**. Exactly one of the 30
Basic members recorded **$18,500.00** in one month; remove that one member and
the tier average is **$32.44**.

- The Basic tier looks like the **most** expensive tier. Is that supported? ______
- The single value responsible for the entire impression is ______
- Rewrite the tier comparison so that it is honest. One sentence: ______

### B3. (2 pts) Reading a number you have never seen.

A chart's title says **"Average satisfaction"**. The underlying values are
ratings from 1 to 5, and the distribution is strongly right-skewed — most
people answer 4 or 5, a few answer 1.

- The title's word "average" is ambiguous between ______ and ______
- Which one does the title most likely mean? ______
- Is it the better choice here? ______
- Write a better title. ______

---

## PART C — PII AND ANONYMIZATION (8 points)

### C1. (2 pts) Direct vs quasi-identifiers.

For each item, mark **D** (direct identifier), **Q** (quasi-identifier), or
**N** (neither / safe alone).

| item | D / Q / N |
|---|---|
| a. Social Security number | |
| b. ZIP code | |
| c. Age | |
| d. First name | |
| e. Height in centimetres | |
| f. Exact date of birth | |

For one of the **Q** items, explain in one sentence why it can identify
someone on its own: ____________________

### C2. (2 pts) k-anonymity.

A dataset has 40 records. Count the equivalence classes over the published
quasi-identifiers (age band, ZIP prefix, city):

| age band + zip prefix | count |
|---|---|
| 25-34 + 90210 | 9 |
| 25-34 + 90211 | 4 |
| 35-44 + 90210 | 1 |
| 35-44 + 90211 | 6 |
| 45-54 + 90210 | 11 |
| 45-54 + 90211 | 9 |

- k = ______ (the smallest class size)
- With `MIN_K = 5`, how many records are **suppressed**? ______
- Are any people individually identifiable? ______ Which one? ______
- A rule says "we only have 1 person at risk, so publish anyway." Why is that
  rule wrong? Use the word k. ______

### C3. (2 pts) Generalization, honestly.

You band ages at 25 years and the identifiable count drops from 1 to 0.

- Is k now at least 5? ______
- So did generalization **solve** the problem, or did it just get lucky? ______
- Now consider a different dataset where banding at 25 years leaves one person
  alone. In one sentence: what has generalization done to that person? ______

### C4. (2 pts) The Age + City result.

In the project dataset, `Age` and `City` **cannot both be published** at any
age-band width, because k = 1 no matter how coarsely you band — 5, 10, 15, 20,
25, or 30 years. One member is always alone in their cell.

- The student says: "banding to 30 years will fix it." Explain in one sentence
  why that is wrong. ______
- The student says: "drop the City column, keep exact ages." Is that safe?
  Why or why not? ______
- Name the **one thing** the student has to decide, and state which side you
  would choose. ______

---

## PART D — THE CHAIN (3 points)

### D1. (3 pts) One dataset, four decisions.

A researcher publishes a chart of "average weekly study hours by grade level,
a sample of 300 students."

The data has: grade level (9–12), age (exact, all 14–18), ZIP code, and
weekly hours. The hours distribution is right-skewed with a mean of 6.2 and a
median of 4.5. Two students share a grade, age, and ZIP combination.

For each of the four decisions below, state the choice you would make and give
**one** reason:

1. **Which statistic is plotted?** ______ reason: ______
2. **Which columns are published?** ______ reason: ______
3. **What is `MIN_K`?** ______ reason: ______
4. **What does the chart's subtitle say?** ______ reason: ______

**Item 4 is the graded one.** The best answer names the statistic *and*
discloses something the chart hides — for example, that the two duplicate
records were excluded, or that the mean was chosen despite the skew, or that
the top 1% of hours were trimmed.

---

## SCORING GUIDE (for your own checking)

**Part A — 8 pts.**

- A1: 2 — 1 for sorting, 1 for **p30 = 40.40** (k = 2.7, bracketed by 39
  and 41: 39 + 0.7 x (41 - 39)).
- A2: 2 — min 35, q1 39.5, median 45.5, q3 54, max 62, **IQR 14.5**,
  fences **(17.75, 75.75)**.
- A3: 1 — the correct answer is **none**.
- A4: 2 — mean **177.50**, median **131.00**; one point for each
  statistic-plus-reason pair.
- A5: 1.

**Part B — 6 pts.**

- B1: 2 — zero-based: bar 2 at **0.500**, bar 3 at **0.750**, ratio
  **1.5**. At 1.5: bar 2 at **0.200**, bar 3 at **0.600**, ratio **3.0**. The
  difference is exaggerated by a factor of **2**.
- B2: 2 — the **$18,500.00** value; the honest rewrite must not use the tier
  mean at all.
- B3: 2.

**Part C — 8 pts.**

- C1: 2 — a D, b Q, c Q, d D, e N, f D or Q (accept either, but demand a
  reason if Q).
- C2: 2 — k = **1**; **1** record suppressed; the identifiable person is the
  **35-44 + 90210** member. Note: after suppressing that record the smallest
  *surviving* class is 6 — but k was already 1 when the data was published,
  which is what the rule is about.
- C3: 2.
- C4: 2.

**Part D — 3 pts.** One point per decision, only if a reason is given.

## A NOTE ON THE "NONE" ANSWERS

Three of these questions have a correct answer of "none" or "no":

- A3: no value falls beyond the fence.
- C2's "are any people identifiable?" — the person **is** identifiable *at the
  moment of publication*, which is the only moment that matters. Suppressing
  them afterwards does not undo the disclosure that k = 1 allowed.
- C3: banding may not raise k at all.

If your instinct was to hunt for a non-empty answer, that instinct is exactly
what a statistics course is trying to train out of you. A finding you cannot
support is worse than no finding.

## TURN IN (due 11:59 PM tonight)

Your completed paper, as a single photo or scan, to this assignment on Google
Classroom. Photograph it flat, in focus, with all four corners visible.

**Write your name and the date at the top of the first page before you hand
it in.** And if you used a calculator for any arithmetic, circle it — not
because it is forbidden, but so I know which parts of this you could do in
your head. I am more interested in the second number than the first.
