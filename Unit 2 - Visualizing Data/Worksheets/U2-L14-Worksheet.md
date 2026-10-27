# U2 L14 — Paper Check: Unit 2 Review

Names: ___________________________  Date: ____

Closed notes. 25 minutes, then swap, grade with the key, and correct every miss in a second color. The corrections are the point — this is your study guide for the project and the unit wrap.

## 1: The check

### Section A — Chart types and when to use them

1. You have 72 days of phishing reports (a sequence in time). Which chart type, and why?

_________________________________________________________________________

2. You want to compare average phishing reports on weekdays vs weekends (two categories). Which chart type?

_________________________________________________________________________

3. You want to see the distribution of login success rates across all 72 days (one column, shape of the data). Which chart type?

_________________________________________________________________________

### Section B — Plot anatomy and the label rule

4. Write the three parts every complete chart must have (the label rule from U2 L03/L05):

_________________________________________________________________________

5. A chart shows a steep drop in phishing reports over three months, but the y-axis starts at 15 instead of 0. What does this hide from the reader?

_________________________________________________________________________

6. A news chart says "Phishing reports fell 50%!" but only shows a bar chart of two months with no denominator (no total students, no total emails). What is the misleading part?

_________________________________________________________________________

### Section C — Reading code: predict the output

7. `plt.savefig("chart.png")` runs AFTER `plt.show()`. What is wrong with the saved file, and what is the correct order?

_________________________________________________________________________

8. `plt.hist(data, bins=5)` vs `plt.hist(data, bins=100)` on the same column. What does each one risk hiding or inventing?

_________________________________________________________________________

9. `plt.clf()` is called between two plots in a script. What does it do, and what goes wrong with the second `savefig` if you skip it?

_________________________________________________________________________

### Section D — Cleaning rules (from U2 L08, U2 L11)

10. A CSV cell is blank (`""`). Name the two choices you have and one tradeoff of each.

_________________________________________________________________________

_________________________________________________________________________

11. Why does `to_float` return `None` instead of letting the `ValueError` crash the script?

_________________________________________________________________________

12. Your cleaning drops 50 of 1,000 rows. What does that quietly change about every chart you build afterward?

_________________________________________________________________________

### Section E — One fix-it (3 points)

13. This code has three bugs. Name all three:

```python
plt.bar(["Mon", "Tue", "Wed"], [15, 18, 22])
plt.title("Daily Phishing Reports")
plt.legend()
plt.savefig("phish.png")
plt.show()
```

Bug 1: ______________________________________________________________

Bug 2: ______________________________________________________________

Bug 3: ______________________________________________________________

---

## 2: Swap and grade

Graded by: ___________________________  Score: ________ / 16

---

## 3: Corrections

For each miss, correct it in a second color and write one line: what I had in my head vs what is true.

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

---

## 4: Look ahead — the project (U2 L15–L18)

The Unit 2 project launches next class (U2 L15): three visualizations built from the campus threat data, with cleaning you do yourself.

Write the one-sentence provenance statement you would make for the threat dataset, including how many days it covers and any cleaning you already know it needs:

_________________________________________________________________________

_________________________________________________________________________

Predict: which is more dangerous to a chart — a blank cell or an impossible value? Defend your choice.

_________________________________________________________________________

_________________________________________________________________________

---

## Hand-in

☐  Check sheet completed, graded by partner, corrections in a second color.

☐  Photo of the corrected check sheet submitted to the Classroom assignment by 11:59 PM tonight.

Keep the sheet — it is your study guide for the Unit 2 project and the unit wrap.