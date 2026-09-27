# U3 L04 — Reflection: What Each Statistic Throws Away

Names: ___________________________  Date: Nov 12

Paper and reflection day. Pencil and notebook only; no code, no terminals. A statistic is a number plus a decision about what to ignore — write the decision down. Hand this sheet in at the end of the period.

## 1: Three classes, one number each

```text
Class A:  one gift of 900.00            -> mean 900.00, median 900.00
Class B:  ten gifts of 90.00           -> mean  90.00, median  90.00
Class C:  five gifts, 80 80 90 100 110 -> mean  92.00, median  90.00
```

1. Which class raised the most? ______________  Which is most *typical* for its donors? ______________

2. Class A has the highest mean. Is that a good thing or a weird thing? Who does that one gift represent — every donor in the class, or one?

   _____________________________________________________________________

3. Say out loud what the mean of Class A is *describing*: a gift, or a class?

   _____________________________________________________________________

## 2: The dashboard problem

A non-profit's website shows "average cost per participant" for each program.

- **Rooftop Garden** — 12 participants, 4,800 total, and one participant received an unusually large materials grant
- **Tutoring** — 240 participants, 96,000 total, costs fairly even

Both programs display **400.00**.

4. Verify the two divisions: 4,800 ÷ 12 = ______________  and  96,000 ÷ 240 = ______________

5. Do the two programs cost the same per participant? What did the dashboard throw away?

   _____________________________________________________________________

6. For which program is the 400.00 actively *misleading*, and why that one?

   _____________________________________________________________________

7. What extra number would you put next to the 400.00, and where would you get it?

   _____________________________________________________________________

## 3: Blind spots

Copy this table into your notebook properly. It is the spine of the unit.

| Statistic              | The question it answers     | Its blind spot (what it cannot see)     |
| ---------------------- | --------------------------- | --------------------------------------- |
| Mean                   | ______________________      | ______________________                  |
| Median                 | ______________________      | ______________________                  |
| Mode                   | ______________________      | ______________________                  |
| Range                  | ______________________      | ______________________                  |
| Standard deviation     | ______________________      | ______________________                  |

The one to get right is the **median's** blind spot. Our donations data makes it concrete:

```text
                    clean (199)     with 90000.00 (200)
mean                    267.40                716.07    <- 2.68x
median                  242.38                242.76    <- 38 cents
```

8. The mean moved by 2.68x; the median moved by 38 cents. What exactly does the median fail to notice?

   _____________________________________________________________________

9. A charity reports only the median: 242.38 every year while the data gets more and more broken. Write the one-sentence cost of that robustness: *the median is robust to extremes, and the price of that robustness is that ____________.*

   _____________________________________________________________________

10. Which of the five blind spots would cause the most real damage, and what decision could go wrong because of it?

   _____________________________________________________________________

___

## 4: The mode's honest limit

Our donation data: 200 values, **199 distinct**, and the most common value appears **twice**.

11. Does this data have a mode? Defend the answer precisely. A function that returns *something* no matter what is not the same as a mode existing.

   _____________________________________________________________________

12. A mode is the right statistic for "how many hours do students study each night" and useless for "how much money do alumni donate." What is the mode actually measuring — the values, or the shape?

   _____________________________________________________________________

## 5: Design your own dashboard

For a dataset you choose (clinic visits, wages, donations, or one you invent), specify:

13. The one or two numbers you would put at the top, and **why those** and not others.

   _____________________________________________________________________

14. What you would *never* show, and what harm it could do.

   _____________________________________________________________________

15. One sentence a reader could learn from your dashboard that they could not learn from your single headline number.

   _____________________________________________________________________

Keep this sketch. You will be graded against it during the project labs.

**TURN IN** — this sheet, with the Section 3 blind-spot table filled in and your Section 5 sketch drawn, at the end of the period.
