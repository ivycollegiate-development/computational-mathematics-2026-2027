# U3 L07 — Paper Check: Centers and Spread

**LO:** compute and interpret means, medians, ranges, and standard deviations by hand, and justify which statistic a claim requires.

**Closed notes. Paper only. No terminals and no code for Parts 1–4.** You may
use a calculator, not Python. This checks whether the ideas are yours, not
whether you can call a function.

Your name and date at the top. Show your arithmetic — a bare answer with no
working is a zero.

## PART 1 — CENTERS ON A SMALL DATASET (10 min)

Compute all four by hand. Show the work.

```text
A:  12  15  15  18  20  22  25  40
```

1. Mean = ______
2. Median = ______
3. Mode = ______ (or state that there is none)
4. Range = ______

Now the same data with the 40 removed:

```text
B:  12  15  15  18  20  22  25
```

5. Mean of B = ______
6. Median of B = ______

7. Which value changed more between A and B — the mean or the median? By how
   much did each change, and why did one hold steady while the other moved?

## PART 2 — EVEN COUNTS AND QUARTILES (10 min)

```text
C:  4  7  9  12  15  19  22  26
```

Eight values, so there is **no single middle value**.

1. Median of C = ______ (show how you got it from the two middle values)
2. What are the two middle values themselves, and what is interesting about
   the fact that your median is probably **not** one of the eight numbers?
3. Q1 (25th percentile) of C = ______
4. Q3 (75th percentile) of C = ______
5. IQR = ______
6. The outlier fence is Q3 + 1.5 × IQR = ______. Is any value in C beyond
   that fence? (Careful — the answer is **no**.) How far is the largest value
   from the fence, and what does that tell you about dataset C? Compare with
   dataset A, where the 40 was an obvious outlier by this same rule.

## PART 3 — SPREAD BY HAND (15 min)

This is the one that matters. Use dataset C: `4 7 9 12 15 19 22 26`.

7. Mean of C = ______
8. Subtract the mean from each value. Write all eight deviations:

   `______  ______  ______  ______  ______  ______  ______  ______`

9. Square each deviation and write all eight results:

   `______  ______  ______  ______  ______  ______  ______  ______`

10. Add the eight squares = ______
11. Divide by 8 = ______ (**variance**)
12. Take the square root of that = ______ (**standard deviation**)
13. Now a sanity question, and it is worth more than the arithmetic: your
    answer in step 12 is in the **same units** as the data (dollars, or
    seconds, or points). Is your answer in step 11 in those units? Why did we
    have to take a square root at all? (Hint: which of the two would you be
    able to *picture*?)
14. In one sentence: why is the standard deviation the number you would show
    a non-mathematician, and the variance the one you would keep for your own
    algebra?

## PART 4 — WHICH STATISTIC? JUSTIFY YOUR CHOICE (10 min)

For **each** claim below, name the single best statistic and **defend the
choice in one sentence**. A wrong choice with a good defense earns more than
a right choice with no defense.

1. "The average wait at the clinic is 11 minutes."
2. "A wait of 2 minutes is unusually fast and deserves investigation."
3. "Salaries at this firm vary enormously."
4. "Most students scored 70 or above."
5. "Our graduates' first salaries cluster tightly around 62,000."

Then one of your own: write a claim about a real dataset, name its best
statistic, and defend it.

## PART 5 — THE INTERPRETATION SET (last 10 min)

A clinic reports these two lines. The second one is the whole question.

```text
Mean wait:      11.36 minutes
Median wait:    11.00 minutes
Standard dev:    5.28 minutes
Shortest:        2 minutes
Longest:        26 minutes
```

6. Would the median alone convince you that waits are consistent? Why or why
   not?
7. The standard deviation is 5.28 on a mean of 11.36. Roughly what fraction
   of waits falls between 11.36 − 5.28 and 11.36 + 5.28? (If you have used a
   calculator: it is **151 of 240**, about **63%**.) The common rule of thumb
   says 68%. This data gives 63% instead. Does that surprise you, and what
   does the gap tell you about the shape of the data? (Recall that many
   patients wait the same short time, so the distribution is lopsided rather
   than symmetric.)
8. Someone wants to say, *"wait times are stable."* Using only the five
   numbers above, give the strongest **honest** version of that claim — and
   the strongest **dishonest** version, so you can recognize both.

## PART 6 — TURN IN — PAPER (due 11:59 PM tonight)

Photograph or scan your **complete worksheet** — all six parts, your name, and
your arithmetic — and submit it to this assignment on Google Classroom.

Before you submit, check:

- [ ] Name and date at the top
- [ ] Working shown for every numeric answer, not just the answers
- [ ] Parts 1–4 are handwritten; no terminal output pasted in
- [ ] Part 4 has a defense sentence for each of the five claims

Keep your terminal closed until the upload is confirmed.

Early finishers: compute the mean of dataset A **including** the 40, then
explain in your own words why adding one value changed the mean by so much
more than it changed the median.
