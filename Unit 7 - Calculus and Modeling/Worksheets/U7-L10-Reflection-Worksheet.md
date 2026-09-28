# U7 L10 — Preview: What Makes an Anomaly an Anomaly

Names: ___________________________  Date: ____

Closed notes. Pencil. 45 minutes. U7 L11 builds the detector. Today you decide what it will look for, on paper, before any of it is written. The threshold words you write in Part 2 are the deliverable.

## 1: Four definitions, four different detectors

For each definition, say what it flags and what it would miss.

**D1. "Far from the mean."** Something whose value differs from the mean by a lot.

- ☐  Flags: _______
- ☐  **Misses:** _______
- ☐  If the series has a strong trend, does this work at all? _______

**D2. "Far from the recent past."** A big change from a short window.

- ☐  Flags: _______
- ☐  **Misses:** _______
- ☐  The window is a parameter. What happens if it is too short versus too long? _______

**D3. "Unusual for this day of the week, at this level of trend."** The residual after removing both.

- ☐  Flags: _______
- ☐  **Misses:** _______
- ☐  Why does this one need the most work to implement, and is the extra work worth it? _______

**D4. "Unusual in a way that was not predicted."** A residual from a full model of the expected series.

- ☐  Flags: _______
- ☐  **Misses:** _______
- ☐  Is D4 meaningfully better than D3, or just more code? _______

**Section B — The D1 verdict.**

1. Is D1 ever the right choice? Give a case where it is: _______

2. What is the cost of choosing it? _______

## 2: What makes a threshold defensible

**Section A — The words you will use in U7 L11.**

3. A threshold is defensible when it is set relative to __________ and reviewed against __________

4. Why is a hardcoded absolute number — say "alert above 80 requests" — a weak threshold? Give **two** reasons: _______

5. Why is a percentage-of-the-mean threshold also weak? _______

6. What are the two numbers that must appear in the **same sentence** to defend a threshold? _______

7. Name the quantity that tells you how often the detector fires on uneventful data. _______

8. Name the quantity that tells you how often it fails on real events. _______

9. Can you choose the first without knowing the second? _______

**Section B — The labelled-sample statement.**

> "Our threshold was tuned against a **labelled** sample of two known events. On unlabelled production data we would not have this, and the threshold would have to be chosen on a stated assumption instead. That assumption is: __________"

10. Complete that sentence: _______

11. Is the labelled sample a weakness or a strength of the writeup? _______

## 3: The two-sided problem

Our two planted events are `+25.5` and `−25.0`.

**Section A — Argue it.**

12. Should a detector fire on both? A traffic spike and a traffic collapse are both worth knowing about — argue it: _______

13. If a business only cares about capacity, and a collapse means "server down, we already know", what does one-sided detection cost you, and what is its risk? _______

14. Name the two ways to handle this in code, and pick one: _______

15. You choose `k = 3` and the detector fires on nothing. What did you just learn about the data, and what did you possibly break? _______

16. The same detector at `k = 2` fires on 4 points, of which 2 are false. Name the trade you are making in one word. _______

**Section B — Which error is worse.**

17. In a monitoring system you must trust — a missed event or a false alarm — which is worse? Defend it in one sentence: _______

18. Does your answer change if the alert has been firing 40 times a day for a month? _______

## 4: Error log

**Section A — Record it.**

- ☐  Record slips
- ☐  Tags: **definition**, **threshold**, **sensitivity**, **one-sided**
- ☐  Newest tag: _______

___

**TURN IN** — This sheet, with the Part 2 threshold statement and the Part 3 one-word trade written out in full.
