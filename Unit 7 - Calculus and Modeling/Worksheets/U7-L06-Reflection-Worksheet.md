# U7 L06 — Reflection: The Trapezoid Rule, Done by Hand

Names: ___________________________  Date: ____

Closed notes. Pencil and graph paper. 45 minutes. In U7 L05 you ran the trapezoid rule; today you derive it and then predict its behaviour without running anything. Write the Part 4 predictions where you cannot revise them before the U7 L08 paper check.

## 1: Build it from a picture

Draw `f(x) = x²` on `[0, 1]` and lay **two** trapezoid panels under it, at `x = 0, 0.5, 1`.

**Section A — The picture.**

- ☐  On the drawing, label each panel's parallel sides and its width

**Section B — The formulas.**

1. Area of the first panel, in terms of `f(0)`, `f(0.5)`, and the width: _______

2. The second panel: _______

3. Add them. What is the general formula? _______

4. Where did the `2` in front of the middle values come from? _______

5. The rectangle rule is `(width) × f(left)`. Write it in the same language as the trapezoid formula: _______

## 2: Why it is second order

Taylor-expand `f` about the midpoint of a panel of width `h`.

**Section A — The algebra.**

6. Write `f(left) = f(m) − (h/2)f′ + (h²/8)f″ − …`: _______

7. Write `f(right) = f(m) + (h/2)f′ + (h²/8)f″ + …`: _______

8. Add them. Which term cancels? _______

9. Which is the first to survive, and what power of `h` is it? _______

10. The panel error is `O(h³)`, there are `1/h` panels, so the total error is `O(h²)`. Write that reasoning in one line: _______

**Section B — The consequence.**

11. If you had sampled at the left endpoint and the middle instead of both endpoints, what order would you get? _______

12. Is that the **midpoint rule**? Which one wins, and by how much? _______

## 3: Predict before you compute

No code today. Predict the value for each `n` on trapezoid over `x²` on `[0, 1]`.

**Section A — The three numbers.**

13. `n = 4`, predicted value: __________

14. `n = 16`, predicted value: __________

15. `n = 64`, predicted value: __________

16. Does the predicted value approach 1/3 from **above or below**? _______

17. By roughly what factor does the error drop each time `n` quadruples? _______

## 4: Error log

**Section A — Record it.**

- ☐  Every arithmetic slip in Parts 1 and 2
- ☐  Tag: **panel width**, **double counting**, **sign**, **order**, **careless**
- ☐  One tag that is new since the last paper check: _______
- ☐  Your Part 3 predictions are written down somewhere you cannot revise them. U7 L08 will tell you whether the **sign** of your error was right, which is a different and more useful check than the exact digits

___

**TURN IN** — This sheet, with the Part 3 predictions sealed and the derivation in Parts 1 and 2 written out in full.
