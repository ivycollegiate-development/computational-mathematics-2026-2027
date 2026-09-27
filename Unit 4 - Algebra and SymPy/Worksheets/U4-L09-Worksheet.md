# U4 L09 — Paper Check Under Exam Conditions

Names: ___________________________  Date: Jan 15   Start time: __________  Finish time: __________

Last class before midterms. Closed book, no laptop, no notebook, no error log, no phone. Time limit: 50 minutes, and the clock starts when it starts. Show work — a bare answer earns no credit. If you do not know a question, write `SKIP` and move on. Put a `?` next to every answer you are not sure of. Do not erase; cross out and continue. Method is marked over result.

## Section A — Working with Numbers (Unit 1), 8 marks

1. [2] Evaluate without a laptop. `17 // 5` = __________   `17 % 5` = __________   `17 / 5` = __________

   Show each: ______________________________________________________

2. [2] A program must read a student's score from the keyboard and reject anything outside 0–100. Write the two lines, including the conversion and the check.

   _____________________________________________________________________

3. [2] What is printed, and why?

   ```python
   x = 10
   def change(x):
       x = x + 1
       return x
   print(change(x), x)
   ```

   Output: ______________   Why: ______________________________

4. [2] A counter needs to go up to 3,000,000,000. Which Python type, and exactly what goes wrong if you choose wrong?

   _____________________________________________________________________

## Section B — Visualizing Data (Unit 2), 6 marks

5. [2] A chart shows failed logins spiking hugely on a Monday. Give **two** reasons the chart might be misleading that have nothing to do with the data.

   _____________________________________________________________________

6. [2] A y-axis runs from 94 to 100 on a chart of success rate. Is this misleading? Explain, and say what you would do about it.

   _____________________________________________________________________

7. [2] Name the three checks every chart must pass before you show it, and say which one people skip most often.

   _____________________________________________________________________

## Section C — Describing Data with Statistics (Unit 3), 12 marks

8. [2] For n = 12 sorted values, compute *k* for `q1` and for `q3` under k = (n − 1) × p, and name the two indices each *k* falls between.

   q1: k = __________  between indices __________ and __________

   q3: k = __________  between indices __________ and __________

9. [2] A dataset has mean 58, median 71, min 12, max 130. Is the mean pulled up or pulled down, and by what specifically?

   _____________________________________________________________________

10. [2] Write the IQR fence formulas, and state the exact rule for calling a point an outlier.

   _____________________________________________________________________

11. [2] A 4,000-row table of student ID, name, and grade is to be shared with a vendor. Name **two** specific problems, and give **two** specific fixes — one for each.

   _____________________________________________________________________

12. [2] A dataset has n = 20. How many values can you drop without changing the median at all? Why is that different from the mean?

   _____________________________________________________________________

13. [2] One sentence: what does the mean tell you that the median does not, and what does the median tell you that the mean does not?

   _____________________________________________________________________

## Section D — Algebra and SymPy (Unit 4), 20 marks

14. [2] Why is `3*x` in Python not the same as the algebra `3x`, and what is a `Symbol` for?

   _____________________________________________________________________

15. [2] Expand `(x + 4)(x − 4)` and factor the result. Name the identity.

   Expanded: ______________   Factored: ______________   Identity: ______________________

16. [3] Solve `4x − 11 = 3x + 2`. Show the line where a sign is at risk, and say in words what you did to protect it.

   _____________________________________________________________________

17. [3] `3x² − 5x − 2 = 0`. Find the discriminant, give both roots, and give them as fractions in lowest terms. Show the formula you used.

   discriminant = __________   roots = ______________________

   _____________________________________________________________________

18. [2] What does `solve` return for each of these, and what does each answer *mean*?

   ```python
   solve([2*x + y - 5, x - y], [x, y])
   solve([x + y - 5, x + y - 2], [x, y])
   ```

   First: ______________________  Second: ______________________

   _____________________________________________________________________

19. [2] Give one reason `solve` might return a dict whose value still contains `y`, and say why that case needs special handling in code.

   _____________________________________________________________________

20. [2] Compute, and give the rule you used:

   ```python
   (-8) % 5
   2 ** 10 % 7
   ```

   ______________ and ______________   Rule: ______________________________

21. [2] Why must a cipher's modulus have no small prime factors? Give the specific failure that a factor of `2` or `13` causes in Z_26.

   _____________________________________________________________________

___

## Section E — Self-mark

Do this alone, in writing, before you open your notebook. Mark each section `✓` (right, and you could have shown the method), `?` (right, but you guessed or rushed), or `✗`.

| section          | ✓              | ?              | ✗              |
| ---------------- | -------------- | -------------- | -------------- |
| A (8 marks)      | __________     | __________     | __________     |
| B (6 marks)      | __________     | __________     | __________     |
| C (12 marks)     | __________     | __________     | __________     |
| D (20 marks)     | __________     | __________     | __________     |

1. The section I lost the most marks in is ______________________ , and the specific question types are ______________________

2. The single concept I will not be able to do in 45 minutes on Monday: ______________________

3. The pattern in my `✗` and `?` marks — one habit, or several? ______________________

4. Compare to Tuesday's L06 diagnostic. Did I close the gap I identified, or did I find a new one?

   _____________________________________________________________________

## Section F — The last three days

| day                      | the one thing I will fix     | how I will prove it to myself     |
| ------------------------ | ---------------------------- | --------------------------------- |
| Fri Jan 15 (tonight)     | ______________________       | ______________________            |
| Sat Jan 16               | ______________________       | ______________________            |
| Sun Jan 17               | ______________________       | ______________________            |

5. Sunday night: I will be studying until __________ and then stopping.

6. Monday morning, before the exam: I will ______________________

**TURN IN** — one photo of the complete paper with your start and finish times, one photo of Sections E and F, and a paragraph answering Section E question 4, at the end of the period.
