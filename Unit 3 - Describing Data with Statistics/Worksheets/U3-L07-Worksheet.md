# U3 L07 — Paper Check: Centers and Spread

Names: ___________________________  Date: Nov 17

Closed notes. Paper only, no terminals and no code. A calculator is allowed; Python is not. Show your arithmetic on every numeric answer — a bare answer with no working is a zero. Hand this sheet in at the end of the period.

## 1: Centers on a small dataset

```text
A:  12  15  15  18  20  22  25  40
```

1. Mean = ______________
2. Median = ______________
3. Mode = ______________ (or state that there is none)
4. Range = ______________

Now the same data with the 40 removed:

```text
B:  12  15  15  18  20  22  25
```

5. Mean of B = ______________
6. Median of B = ______________
7. Which changed more between A and B, the mean or the median? By how much did each change, and why did one hold steady while the other moved?

   _____________________________________________________________________

   _____________________________________________________________________

## 2: Even counts and quartiles

```text
C:  4  7  9  12  15  19  22  26
```

Eight values, so there is no single middle value. Use the linear-interpolation method: the percentile at fraction *p* sits at index *k* = (n − 1) × *p*, and you interpolate between the two values that bracket it.

8. For p25, k = 7 × 0.25 = ______________   The bracketing values are ______________ and ______________   Q1 = ______________
9. For p75, k = 7 × 0.75 = ______________   The bracketing values are ______________ and ______________   Q3 = ______________
10. Median of C, from the two middle values ______________ and ______________ = ______________
11. Why is your median probably **not** one of the eight numbers? ______________________
12. IQR = Q3 − Q1 = ______________
13. Upper fence = Q3 + 1.5 × IQR = ______________
14. Is any value in C beyond that fence? ______________________  How far is the largest value from the fence? ______________
15. What does that tell you about dataset C? Then compute the same fence for dataset A and state whether the 40 is beyond it.

   C fence: ______________   A Q1 = ______________  A Q3 = ______________  A IQR = ______________  A fence = ______________

## 3: Spread by hand

Use dataset C: `4 7 9 12 15 19 22 26`.

16. Mean of C = ______________
17. Subtract the mean from each value. Write all eight deviations:

   ________  ________  ________  ________  ________  ________  ________  ________

18. Square each deviation and write all eight results:

   ________  ________  ________  ________  ________  ________  ________  ________

19. Sum of the eight squares = ______________
20. Divide by 8 = ______________ (**variance**)
21. Square root of that = ______________ (**standard deviation**)
22. Your step 20 answer is in squared units; step 21 is in the units of the data. Which of the two can you *picture*, and why did we have to take the square root at all?

   _____________________________________________________________________

23. In one sentence: why is the standard deviation the number you show a non-mathematician, and the variance the one you keep for your own algebra?

   _____________________________________________________________________

___

## 4: Which statistic? Justify your choice

Name the single best statistic for each claim and defend it in one sentence. A wrong choice with a good defense earns more than a right choice with no defense.

| #          | Claim                                    | Statistic      | Defense                    |
| ---------- | ---------------------------------------- | -------------- | -------------------------- |
| 1          | "The average wait at the clinic is 11 minutes." | __________     | ______________________     |
| 2          | "A wait of 2 minutes is unusually fast and deserves investigation." | __________     | ______________________     |
| 3          | "Salaries at this firm vary enormously." | __________     | ______________________     |
| 4          | "Most students scored 70 or above."      | __________     | ______________________     |
| 5          | "Our graduates' first salaries cluster tightly around 62,000." | __________     | ______________________     |

6. Write a claim of your own about a real dataset, name its best statistic, and defend it.

   Claim: _______________________________________________________________

   Statistic: ______________   Defense: ______________________________

## 5: The interpretation set

```text
Mean wait:      11.36 minutes
Median wait:    11.00 minutes
Standard dev:    5.28 minutes
Shortest:        2 minutes
Longest:        26 minutes
```

7. Would the median alone convince you that waits are consistent? Why or why not?

   _____________________________________________________________________

8. The window 11.36 − 5.28 to 11.36 + 5.28 is 6.08 to 16.64. How much of the wait distribution does one standard deviation cover here, and what does the gap between that and the 68% rule of thumb tell you about the shape of the data?

   _____________________________________________________________________

9. Someone wants to say *"wait times are stable."* Using only the five numbers above, write the strongest **honest** version of that claim, then the strongest **dishonest** version, so you can recognize both.

   _____________________________________________________________________

   _____________________________________________________________________

**TURN IN** — this completed sheet, all five sections, with your working, at the end of the period.
