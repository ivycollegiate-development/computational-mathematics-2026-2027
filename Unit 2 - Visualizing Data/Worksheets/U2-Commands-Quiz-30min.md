# U2 Commands & Concepts — 30-Minute Quiz

**Name:** _________________________  **Seat:** ____  **Date:** ___________

*Closed notes. 25 minutes. Swap & grade. Corrections in second color.*

---

## Part 1: Terminal & Git (5 questions)

1. What does `pwd` print, and why is the "always know where you are" rule the first thing we enforce?

2. `mkdir -p data/cleaned` — what does the `-p` flag do, and what error does it prevent?

3. `git add` → `git commit -m "msg"` → `git push` — what does each command actually do? (One phrase each.)

4. You cloned a repo yesterday. Today you want updates. Which command: `git clone` or `git pull`? What error happens if you re-clone into the same folder?

5. GitHub asks for a "password" on `git push`. What do you actually type?

---

## Part 2: Python & Pandas (3 questions)

6. `python3` vs `python` on the VPS — which one do we use and why?

7. `df = pd.read_csv("data.csv")` — what type is `df`, and what type is every value inside it before cleaning?

8. `to_float("N/A")` returns `None` instead of crashing. Why is `None` better than letting `ValueError` bubble up?

---

## Part 3: Matplotlib (4 questions)

9. Match the chart to the scenario:

   | Scenario | Chart type |
   |----------|------------|
   | Phishing reports over 72 days | |
   | Weekday vs weekend average reports | |
   | Distribution of login success rates | |

10. `plt.scatter(x, y, s=12, alpha=0.4)` — what do `s` and `alpha` control? Why use `alpha=0.4` with 1,000 points?

11. `plt.hist(data, bins=20, edgecolor="white")` — what does `bins=20` do? Why `edgecolor="white"`? Is 20 the "correct" number?

12. `plt.savefig("chart.png")` then `plt.show()` — why must `savefig` come **before** `show()`?

---

## Part 4: Cleaning & Reading Charts (2 questions)

13. Sanity bounds (e.g., GPA 0.0–4.0) vs IQR outlier detection — give **one reason** we prefer sanity bounds for cleaning.

14. A histogram shows a long right tail with a peak near 0. The mean is 4.2, median is 1.8. What does this tell you about the real-world data?

---

## Part 5: One Fix-It (1 question)

15. This code has **three bugs**. Circle each and write the fix.

```python
plt.bar(categories, values)
plt.title("Phishing Reports by Month")
plt.legend()
plt.savefig("monthly.png")
plt.show()
plt.xlabel("Month")
plt.ylabel("Reports")
```

---

## Swap & Grade

**Score:** _____ / 15

**Partner:** _________________________

---

## Corrections (second color)

| Q | What I wrote | What is true |
|---|--------------|--------------|
|   |              |              |
|   |              |              |
|   |              |              |

---

## Look Ahead — U2 Project (L15 Launch)

One chart you'll build for the Campus Threat project and the **exact** chart type:

_____________________________________________________________________________

One cleaning step you'll document in your provenance statement:

_____________________________________________________________________________