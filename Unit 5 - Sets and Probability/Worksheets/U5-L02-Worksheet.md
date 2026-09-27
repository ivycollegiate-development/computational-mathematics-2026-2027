# U5 L02 — Venn Diagrams by Hand: Union, Intersection, Difference

Names: ___________________________  Date: Feb 18

Closed notes. 50 minutes. Pencil, ruler, notebook. No laptop. Today's hand counts are the specification tomorrow's code is tested against, so a wrong hand count produces a code that is wrong the same way and passes its test.

## 1: The two-circle diagram — Label every region

`A` = students in the CS club, 34. `B` = students in the chess club, 22. `U` = all 120 students in the school. Nine of the chess club members are also in the CS club, and 3 students are in neither club.

| region               | meaning              | count              |
| -------------------- | -------------------- | ------------------ |
| `A` only             | in CS, not chess     | ______________     |
| `B` only             | in chess, not CS     | ______________     |
| `A n B`              | in both              | ______________     |
| outside `A u B`      | in neither           | ______________     |
| **check: total**     | must equal 120       | ______________     |

**Section A — The reading order.**

☐  Why must the `A n B` region be read before `A` only and `B` only: ______________

☐  If you fill in 34 as the whole `A` circle and then subtract 9, what wrong answer do you produce, and which region is it: ______________

☐  Fill the table in the order the sentences actually give the information, and note where you had to go back: ______________

## 2: The four operations — Compute each from the regions above

| operation                 | definition in words     | your answer        |
| ------------------------- | ----------------------- | ------------------ |
| `A u B`                   | ______________          | ______________     |
| `A n B`                   | ______________          | ______________     |
| `A - B`                   | ______________          | ______________     |
| `B - A`                   | ______________          | ______________     |
| `A ^ B` (exactly one)     | ______________          | ______________     |
| neither                   | ______________          | ______________     |

☐  `A - B` and `B - A` use the same two circles. Name the region that separates them: ______________

☐  Write `A ^ B` using only `-` and `u`: ______________

☐  Check your `A ^ B` against `|A| + |B| - 2|A n B|`: ______________

☐  Check your union against `|A| + |B| - |A n B|`: ______________

☐  A student writes `A - B` and gets 25. What did they most likely do wrong: ______________

## 3: Phrase to operation — Name the set operation

| #          | sentence                                 | operation          |
| ---------- | ---------------------------------------- | ------------------ |
| 1          | takes Mandarin **and** French            | ______________     |
| 2          | takes Mandarin **or** French             | ______________     |
| 3          | takes Mandarin **but not** French        | ______________     |
| 4          | takes Mandarin **or** French, **but not both** | ______________     |
| 5          | takes **neither** Mandarin nor French    | ______________     |
| 6          | is in CS club **and** is on the **chess** team | ______________     |
| 7          | was late **or** absent                   | ______________     |
| 8          | is in **exactly one** of the two clubs   | ______________     |
| 9          | is not on the roster                     | ______________     |
| 10         | failed at least one exam                 | ______________     |

☐  Row 3, written fully: ______________

☐  Rows 4 and 8 are the same operation. Prove it in symbols: ______________

☐  Why can you not take a complement without a stated universe: ______________

☐  One sentence of your own life and the operation it hides: ______________

## 4: Three circles — All eight regions, and the total

Now `C` = the debate club: 15 students, 6 also in the CS club, 4 also in the chess club, 2 in all three, and exactly one member in chess, who is in all three.

| region                    | count              |
| ------------------------- | ------------------ |
| `A` only                  | ______________     |
| `B` only                  | ______________     |
| `C` only                  | ______________     |
| `A n B` only              | ______________     |
| `A n C` only              | ______________     |
| `B n C` only              | ______________     |
| `A n B n C`               | ______________     |
| outside all three         | ______________     |
| **total must be 120**     | ______________     |

☐  Did you have to go back and edit an earlier number? Which one, and why: ______________

☐  Which pair of regions, if one were wrong, would still let the total come to 120: ______________

☐  The outside region came out negative in a lot of first attempts. What did a negative region tell you: ______________

## 5: Predict tomorrow's code — Value and form, before you see it

With `A = {1,2,3,4,5}` and `B = {4,5,6,7}`.

| expression                | predicted output     | type (set / list / bool / int)     |                    |
| ------------------------- | -------------------- | ---------------------------------- | ------------------ |
| `A & B`                   | ______________       | ______________                     |                    |
| `A \                      | B`                   | ______________                     | ______________     |
| `A - B`                   | ______________       | ______________                     |                    |
| `A ^ B`                   | ______________       | ______________                     |                    |
| `len(A & B)`              | ______________       | ______________                     |                    |
| `A & B == {4, 5}`         | ______________       | ______________                     |                    |
| `A <= B`                  | ______________       | ______________                     |                    |
| `set(range(1,8)) - A`     | ______________       | ______________                     |                    |

☐  Which of the eight are you least sure about, and why: ______________

☐  Which one will not come out in the order you drew it: ______________

**TURN IN** — The two-circle table and the operations table photographed, the three-circle eight-region table with its total row, and this prediction table written before Friday. No credit for a total that does not equal 120.
