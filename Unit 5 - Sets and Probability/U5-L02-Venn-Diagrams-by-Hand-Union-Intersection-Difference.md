# U5 L02 — Venn Diagrams by Hand: Union, Intersection, Difference

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (50 minutes)
**LO:** 5.2 — draw and read a two-set Venn diagram; compute union, intersection,
difference, and symmetric difference by counting regions

---

**No laptop today.** Pencil, ruler, notebook. Friday you will write code that
has to reproduce exactly what you count by hand today, so today's counts are
the specification your code gets tested against. If the hand count is wrong,
the code will be wrong in exactly the same way and the test will pass.

## PART 1 — DRAW THE DIAGRAM, LABEL EVERY REGION (10 min)

Let `A` = students in the CS club (34 students).
Let `B` = students in the chess club (22 students).
Let `U` = all 120 students in the school.

Draw the two circles and the box. Then fill in this table, one number per region:

| region | meaning | count |
|---|---|---|
| `A` only | in CS, not chess | ______ |
| `B` only | in chess, not CS | ______ |
| `A n B` | in both | ______ |
| outside `A u B` | in neither | ______ |
| **check: total** | must equal 120 | ______ |

Here is the information you actually have — read it twice, because the wording
is where these exercises live or die:

> 34 students are in the CS club. 22 are in the chess club. **9 of the chess
> club members are also in the CS club.** 3 students are in neither club.

- ☐  Why must the `A n B` region come *before* `A` only and `B` only in your
     reading order? ______
- ☐  What is the trap if you fill in "34" as the size of the whole `A` circle's
     left-plus-middle, then subtract 9? Write the wrong answer that produces:
     ______
- ☐  Fill the table in the order the sentences actually give it, and note where
     you had to go back: ______

## PART 2 — THE FOUR OPERATIONS, FROM THE SAME PICTURE (12 min)

Using only the regions you just filled in, compute each. Show the arithmetic.

| operation | definition in words | your answer |
|---|---|---|
| `A u B` | | |
| `A n B` | | |
| `A - B` | | |
| `B - A` | | |
| `A ^ B` (exactly one) | | |
| neither | | |

- ☐  `A - B` and `B - A` use the same two circles. Why are they different
     numbers? Point at the region that separates them. ______
- ☐  Write `A ^ B` using only `-` and `u`. ______
- ☐  Check your `A ^ B` against `|A| + |B| - 2|A n B|`: ______
- ☐  Check your union against `|A| + |B| - |A n B|`: ______
- ☐  A student writes `A - B` and gets 25. What did they most likely do
     wrong? ______

## PART 3 — THE PHRASE-TO-OPERATION TABLE (12 min)

This is the skill the test will actually ask for. For each sentence, write the
set operation. Be precise: "and" and "or" are not the same, and in this
discipline "or" almost always means the inclusive one.

| # | sentence | operation |
|---|---|---|
| 1 | takes Mandarin **and** French | |
| 2 | takes Mandarin **or** French | |
| 3 | takes Mandarin **but not** French | |
| 4 | takes Mandarin **or** French, **but not both** | |
| 5 | takes **neither** Mandarin nor French | |
| 6 | is in CS club **and** is on the **chess** team | |
| 7 | was late **or** absent | |
| 8 | is in **exactly one** of the two clubs | |
| 9 | is not on the roster | |
| 10 | failed at least one exam | |

- ☐  Number 3 is the one people get wrong. Write it fully: ______
- ☐  Number 4 and number 8 are the same thing. Prove it, in symbols. ______
- ☐  Number 9 needs `U` to exist. Why can't you take the complement without a
     stated universe? ______
- ☐  Write one sentence of your own life and the operation it hides. ______

## PART 4 — THREE CIRCLES, ONCE (10 min)

Now `C` = students in the debate club. 15 students, and **6 of them are also in
the CS club**, **4 are also in the chess club**, and **2 are in all three.** The
debate club has exactly one member who is in chess, and that person is in all
three.

Fill in all eight regions, including the outside:

| region | count |
|---|---|
| `A` only | |
| `B` only | |
| `C` only | |
| `A n B` only | |
| `A n C` only | |
| `B n C` only | |
| `A n B n C` | |
| outside all three | |
| **total must be 120** | |

- ☐  Did you have to go back and edit an earlier number? Which, and why: ______
- ☐  Which pair of regions, if you got one wrong, would make the total still come
     out to 120 anyway? ______
- ☐  The outside region came out negative in a lot of people's first attempt.
     What did that tell them? ______

The last question is the one to keep. **A negative region is not an arithmetic
mistake — it is your model telling you the story you told is impossible.** By
Friday you will see the same thing in code: a model that produces a probability
over 1 is not broken, it is confessing.

## PART 5 — PREDICT TOMORROW'S CODE (6 min)

Tomorrow you write a `setkit.py`. Predict, in writing, what each of these will
print — the **value and the form**:

| expression | predicted output | type (set / list / bool / int) |
|---|---|---|
| `A & B` for `A = {1,2,3,4,5}`, `B = {4,5,6,7}` | | |
| `A \| B` | | |
| `A - B` | | |
| `A ^ B` | | |
| `len(A & B)` | | |
| `A & B == {4, 5}` | | |
| `A <= B` | | |
| `set(range(1,8)) - A` | | |

- ☐  Which of these eight are you *least* sure about, and why: ______
- ☐  Which one do you expect will not be in the order you drew it: ______

## TURN IN — Venn by Hand

1. One photo of the two-circle table (Part 1) and the operations table (Part 2)
2. One photo of the three-circle eight-region table (Part 4), including the
   total row
3. Your Part 5 prediction table, written before Friday

**No credit for a total that does not equal 120.** If your regions are wrong
but your total is right, that is worse than being wrong and knowing it.

## 📋 PREVIEW OF TOMORROW

**Next:** L03, Fri Feb 19 — back to the machine. You build `setkit.py`, and then
you run it against today's hand counts. The interesting moment is when the two
disagree: one of you is wrong, and finding out which is the actual lesson.

**Bring tomorrow:** laptop, and today's photographed tables.

## 🇹🇼 TAIWAN CONTEXT

The symmetric difference is the operation that reconciliation teams at
Taiwanese hospitals and universities run weekly: "accounts present in the
legacy system but not the new one, and accounts present in the new one but not
the legacy one." The `^` from tonight is that query. A migration where you only
check one direction reports a clean cutover while silently orphaning records,
and the discovery usually comes from a patient who cannot be found — not from
the system that lost them.
