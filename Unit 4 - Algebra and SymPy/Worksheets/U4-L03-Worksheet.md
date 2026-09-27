# U4 L03 — Paper Check: Solve It, Then Predict

Names: ___________________________  Date: Jan 7

No laptop today. Pencil and notebook. Solve everything by hand, and for each one **also write what you predict SymPy will return**, including its *form* — a list, a set, a dict, or a bare expression. Forms are how you get tricked on a midterm. Hand this sheet in at the end of the period.

## 1: Linear, by hand

For each: solve it, then predict the exact shape of the output.

1. `3x + 7 = 22`   x = ______________   predicted SymPy returns: ______________________
2. `5x - 2 = 3x + 10`   x = ______________   predicted SymPy returns: ______________________
3. `2(x - 3) = 4x`   x = ______________   predicted SymPy returns: ______________________
4. `(x + 1)/3 = 4`   x = ______________   predicted SymPy returns: ______________________
5. `7 = 7x + 2`   x = ______________   predicted SymPy returns: ______________________

6. Question 2 is the one people get wrong. What is the trap in it? ______________________

7. How many steps did each take? Record the counts for 1–5: ______________

8. Did you get the same x by two different routes on any of them? Which, and how? ______________________

## 2: Quadratics, by hand

The quadratic formula. Show all five steps for the first two — the work is the graded part.

9. `x² - 5x + 6 = 0`   discriminant = __________   roots = ______________________   predicted SymPy returns: ______________________
10. `2x² + 7x + 3 = 0`   discriminant = __________   roots = ______________________   predicted SymPy returns: ______________________
11. `x² - 4x + 4 = 0`   discriminant = __________   roots = ______________________   predicted SymPy returns: ______________________
12. `x² + 2x + 5 = 0`   discriminant = __________   roots = ______________________   predicted SymPy returns: ______________________

13. Question 11 is a perfect square. Do you get one root or two? ______________________

14. Question 12 has a negative discriminant. Write what you expect SymPy to return for a **real-only** search versus an **unrestricted** one: ______________________

Now the factoring route, for the same four:

| #          | can it be factored over the integers?    | if yes, factor it          | if no, say why not         |
| ---------- | ---------------------------------------- | -------------------------- | -------------------------- |
| 9          | __________                               | ______________________     |                            |
| 10         | __________                               | ______________________     |                            |
| 11         | __________                               | ______________________     |                            |
| 12         | __________                               |                            | ______________________     |

15. For which numbers does `factor` on the left-hand side minus the right-hand side recover your roots, with no quadratic formula anywhere? ______________________

16. For which does it not, and what does SymPy hand back instead? ______________________

## 3: Two-symbol equations

17. Solve for `x`: `2x + 3y = 12`   x = ______________________ (in terms of y)

18. Solve for `y`: `5x - 2y = 4`   y = ______________________ (in terms of x)

19. `2x + 3y = 12` and `5x - 2y = 4` together. (x, y) = ______________________

    predicted SymPy returns: ______________________

20. Question 19 uses the same pair of equations as 17 and 18. What did combining them actually buy you? One sentence. ______________________

21. Write an equation that pairs with `2x + 3y = 12` to have **no** solution. ______________________

22. Write an equation that pairs with it to have **infinitely many** solutions. ______________________

## 4: Prediction audit

Count your predictions across Sections 1–3.

| section                | predictions made     | predicted value right     | predicted FORM right     | both wrong     |
| ---------------------- | -------------------- | ------------------------- | -------------------------- | -------------- |
| linear (1–5)           | __________           | __________                | __________                 | __________     |
| quadratic (9–12)       | __________           | __________                | __________                 | __________     |
| two-symbol (17–19)     | __________           | __________                | __________                 | __________     |

23. The single prediction you got most wrong was number ______ because ______________________

24. Were your **values** better than your **forms**? Evidence: ______________________

25. Is there a pattern to which forms you mispredicted? ______________________

## 5: Start the error log

Two columns: *what I wrote* and *what it should have been*.

☐  Every error from today goes in, including the ones you caught.

☐  Each entry is tagged with a cause: **sign**, **distribution**, **formula**, **careless**.

☐  Most common cause today: ______________________

**TURN IN** — one photo of Sections 1–3 with all work shown, one photo of the Section 4 audit table, and your error-log page, at the end of the period. Do not correct the predictions afterwards; the paper is the record of what you believed before you knew.
