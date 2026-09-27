# U6 L12 — Paper Check: Measuring and Thresholding a Fractal

Names: ___________________________  Date: Apr 27

Closed notes. Pencil. 45 minutes. Complete the recall from memory first, then check against your own `results.txt`. The threshold paragraph you write in Part 3 goes into your project README.

## 1: Recall the measurement

**Section A — Koch.** From Thursday, complete from memory.

1. Perimeter at `n = 3`: __________ segments, each of length __________, perimeter __________

2. The multiplier from one step to the next: __________

3. So the perimeter, in the limit, is: __________

4. Koch area, in the limit: __________

**Section B — Sierpinski.**

5. Filled cells at depth 5: __________

6. `filled/side²` at depth 5: __________

7. True dimension `log2(3)`: __________

8. Your measured dimension at depth 5: __________

9. Absolute error: __________

**Section C — Score it.**

- ☐  All nine right: ________ / 9
- ☐  Questions 3 and 4 are the contrast the whole project rests on. In one sentence, why can a shape have one of those and not the other: _______

## 2: The fight — which row was correct

Yesterday's table, at threshold 1.2:

| ---------------------- | ------------ | ------------------ | ---------------------------------------- |
| ------------------ | -------- | ----------- | -------- |
| Koch depth 3       | 1.3067   | FRACTAL     |          |
| Koch depth 4       | 1.3278   | FRACTAL     |          |
| solid circle       | 1.7891   | FRACTAL     |          |
| thick diagonal     | 1.0000   | not fractal |          |
| random noise 30%   | 1.6531   | FRACTAL     |          |
| random noise 55%   | 1.8127   | FRACTAL     |          |
| sparse dots 2%     | 0.4590   | not fractal |          |

**Section A — Mark every row.** Then justify the two you expect to be argued about.

1. The circle's 1.79 — the real answer is: _______

2. The 30% noise's 1.65 — the real answer is: _______

3. Which misclassification is worse for a security detector, and why? _______

4. The sparse-dots row scored 0.459. Is that "not fractal" for the right reason, or for a reason that would embarrass you in a defense? _______

The last one is a fair trap. The threshold caught it only because 0.459 is far from 1.2. Denser dots would have been called fractal.

## 3: Defend your threshold

**Section A — The paragraph.** Three sentences minimum. This goes in the README nearly verbatim.

> I set the threshold at __________. At that value, my detector correctly classifies __________ of my 8 cases, and misclassifies __________ . I chose it over the alternative of __________ because __________ . A reader should not use my detector to conclude that __________ , because __________ .

5. Write the paragraph: _______

**Section B — The harder sentence.**

> The **one** case where my detector is most likely to be wrong on real input is __________ , because __________ .

6. Write that sentence: _______

## 4: Error log

**Section A — Record it.**

- ☐  Every error from Parts 1 and 2 into the **Geometry Error Log**
- ☐  Tag each: **measurement**, **threshold**, **reasoning**, **recall**, **careless**
- ☐  Newest tag, and what it means: _______
- ☐  How many errors were **recall** — things you could not reproduce without notes? ________

___

**TURN IN** — This sheet, with the Part 3 paragraph and the Part 3B sentence written out in full.
