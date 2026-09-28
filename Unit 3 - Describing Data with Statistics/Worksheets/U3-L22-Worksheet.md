# U3 L22 — Paper Check: Unit 3 Statistics and Privacy

Names: ___________________________  Date: ____

Closed notes. Paper only, no code, no terminal. 55 minutes, 25 points. Every question is answerable by hand. Show your work: for every numeric answer, write the setup line and then the answer. Circle any calculator you use.

## Part A — Descriptive statistics (8 points)

1. **A percentile, by hand.** Recorded response times (seconds) for 10 form submissions:

   ```text
   41, 55, 38, 62, 47, 51, 44, 58, 39, 35
   ```

   Using the U3 L08 method, k = (n − 1) × p:

   Sorted: ______________________________________________________

   k = ______________   bracketing values: ______________ and ______________

   p30 = ______________ seconds

2. **Five-number summary and IQR**, same 10 values:

   min = __________  q1 = __________  median = __________  q3 = __________  max = __________

   IQR = q3 − q1 = ______________

   Lower fence = ______________   Upper fence = ______________

3. **Outliers by the IQR rule.** List every value from question 2 that falls beyond either fence: ______________________

   If your answer is "none," that is correct. Explain in one line why the largest value in a set can still sit inside the fence: ______________________

4. **Mean or median?** A club collects monthly spending from 12 members:

   ```text
   120, 130, 125, 140, 135, 128, 132, 138, 122, 134, 126, 700
   ```

   mean = ______________   median = ______________

   The treasurer wants "what a member typically spends per month." Which do you report, and why in one sentence? ______________________

   The treasurer instead wants "our total monthly membership revenue." Which statistic, and why? ______________________

5. **Standard deviation, conceptually.** Your friend says: "this dataset's standard deviation is 15, so a value 15 away from the mean is completely normal." Is that right? Explain in one sentence. ______________________

## Part B — Misleading visuals (6 points)

6. **The truncated bar chart.** Three bars of height 2, 3, and 4, on a y-axis that starts at 1.5 instead of 0.

| axis range     | visual height of bar 2     | visual height of bar 3     | ratio (3÷2)     |
| -------------- | -------------------------- | -------------------------- | --------------- |
| 0 to 4         | __________                 | __________                 | __________      |
| 1.5 to 4       | __________                 | __________                 | __________      |

   How many times bigger does the 1.5-based chart make the difference between bars 3 and 2 look? ______________

7. **Mean, or the story you want?** The Basic-tier average monthly spend is **$648.02**. Exactly one of the 30 Basic members recorded **$18,500.00**; remove that one and the tier average is **$32.44**.

   a. The Basic tier looks like the most expensive tier. Is that supported? ______________________

   b. The single value responsible for the entire impression is ______________________

   c. Rewrite the tier comparison so it is honest, in one sentence: ______________________

8. **Reading a number you have never seen.** A chart title says **"Average satisfaction"**, the ratings run 1 to 5, and the distribution is strongly right-skewed — most people answer 4 or 5, a few answer 1.

   a. The word "average" is ambiguous between ______________________ and ______________________

   b. Which one does the title most likely mean? ______________________

   c. Is it the better choice here? ______________________

   d. Write a better title. ______________________

## Part C — PII and anonymization (8 points)

9. **Direct vs quasi-identifiers.** Mark each **D** (direct identifier), **Q** (quasi-identifier), or **N** (neither / safe alone).

| item                          | D / Q / N      |
| ----------------------------- | -------------- |
| a. Social Security number     | __________     |
| b. ZIP code                   | __________     |
| c. Age                        | __________     |
| d. First name                 | __________     |
| e. Height in centimetres      | __________     |
| f. Exact date of birth        | __________     |

   For one of the **Q** items, explain in one sentence why it can identify someone on its own: ______________________

10. **k-anonymity.** A dataset has 40 records. Count the equivalence classes over the published quasi-identifiers:

| age band + zip prefix     | count      |
| ------------------------- | ---------- |
| 25-34 + 90210             | 9          |
| 25-34 + 90211             | 4          |
| 35-44 + 90210             | 1          |
| 35-44 + 90211             | 6          |
| 45-54 + 90210             | 11         |
| 45-54 + 90211             | 9          |

   Check your counts sum to 40: sum = ______________

   k = ______________   With `MIN_K = 5`, records suppressed = ______________

   Are any people individually identifiable? ______________________  Which one? ______________________

   A rule says "we only have 1 person at risk, so publish anyway." Why is that rule wrong? Use the word k. ______________________

11. **Generalization, honestly.** You band ages at 25 years and the identifiable count drops from 1 to 0.

   Is k now at least 5? ______________________

   So did generalization **solve** the problem, or did it get lucky? ______________________

   In a different dataset, banding at 25 years still leaves one person alone. In one sentence, what has generalization done to that person? ______________________

12. **The Age + City result.** In the project dataset, `Age` and `City` cannot both be published at any age-band width — k = 1 at 5, 10, 15, 20, 25, and 30 years, because one member is always alone in their cell.

   a. "Banding to 30 years will fix it." Explain in one sentence why that is wrong. ______________________

   b. "Drop the City column, keep exact ages." Is that safe? Why or why not? ______________________

   c. Name the **one thing** you have to decide, and state which side you choose. ______________________

## Part D — The chain (3 points)

13. A researcher publishes "average weekly study hours by grade level" for 300 students. The data has grade level (9–12), exact age (all 14–18), ZIP code, and weekly hours. Hours are right-skewed: mean 6.2, median 4.5. Two students share a grade, age, and ZIP combination.

   1. Which statistic is plotted? ______________  reason: ______________________

   2. Which columns are published? ______________  reason: ______________________

   3. What is `MIN_K`? ______________  reason: ______________________

   4. What does the chart's subtitle say? ______________  reason: ______________________

   Item 4 is the graded one. The best answer names the statistic **and** discloses something the chart hides.

**TURN IN** — this completed paper, as a single photo or scan, at the end of the period.
