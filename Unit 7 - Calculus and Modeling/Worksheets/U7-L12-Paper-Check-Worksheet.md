# U7 L12 — Paper Check: Committing to the Detector's Parameters

Names: ___________________________  Date: May 18

Closed notes. Pencil. 45 minutes. You commit to the detector's parameters on paper, with reasons, before Friday's deadline. The decisions are yours; the code only implements them.

## 1: Recall the numbers

**Section A — From Monday, from memory, then check.**

1. The two planted event times: __________ , and their signed magnitudes: __________

2. The detrended MAD spread: __________

3. The raw-series MAD spread: __________

4. The ratio between those two spreads: __________

5. At `k = 2`, which two points are false positives? __________

6. At `k = 3, 4, 5`, how many points are flagged? __________

7. The standard-deviation spread: __________

8. The spread with the two events deleted: __________

9. The `sd/mad` ratio with events, and without: __________ , __________

10. The first-8-points experiment: how many events caught? __________

11. The pure-sine `sd` from L09: __________

12. The recovered trend per day: __________ (built-in value: __________)

**Section B — Score it.**

- ☐  Score: ________ / 12
- ☐  Question 8 matters most. If you could not recall it, say so here: _______

## 2: Defend the detrending choice

**Section A — The argument.**

13. Name two methods for establishing a baseline: __________ , __________

14. Why does a 7-day moving average fail on this data? _______

15. What specifically is the `8.4438` from L09 measuring? _______

16. So the day-of-week method is better because _______

17. What does the day-of-week method **assume** that a moving average does not? _______

18. Give one real situation where the answer to 17 fails: _______

**Section B — The rule you will follow.**

19. A global statistic computed over a series with defective edges is partly measuring the defect. State that as a rule: _______

## 3: Commit to your parameters

**Section A — Fill the table.** Final answers, one line of reason each. You use these Friday.

| ---------------------------- | ------------- | --------------------- |
| ------------------------ | -------- | -------- |
| scale estimator          |          |          |
| `k`                      |          |          |
| one-sided or two-sided   |          |          |
| minimum points to report |          |          |

**Section B — The uncomfortable part.**

20. You know `k = 3`, `k = 4`, and `k = 5` all give identical flags on this data. What is your **actual** basis for choosing? _______

21. Fill in the defense sentence:

> "We set the threshold at __________ times the MAD-based spread, giving __________ , which flags __________ of our 2 labelled events with __________ false positives. The choice of __________ is not determined by this dataset — the data cannot distinguish it from alternatives — so we chose it because __________"

22. What would you need in order to choose `k` on evidence rather than on argument? _______

23. If you could not get that, what is the honest fallback? _______

24. From L09's Part 3, the detector was blind on 8 points. What must your output print so a reader can tell "quiet" from "not enough data"? _______

## 4: Error log

**Section A — Record it.**

- ☐  All errors from Parts 1 through 3
- ☐  Tags: **edge effects**, **contaminated statistic**, **coverage**, **judgement call**
- ☐  Newest tag, defined in your own words: _______
- ☐  Which of today's numbers would you want a **test** on rather than a comment about? _______

___

**TURN IN** — This sheet, with the Part 3 parameter table filled in and the Part 3B defense sentence written out in full.
