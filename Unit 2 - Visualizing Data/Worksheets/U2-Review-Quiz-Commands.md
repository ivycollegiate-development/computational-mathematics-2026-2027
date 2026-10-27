# U2 Review Quiz — Commands & Concepts (U1 + U2 L01–L13)

**Closed notes. 25 minutes. Swap and grade with the key — corrections in a second color.**

---

## Part 1: Terminal & Git (U1 + U2)

1. **`pwd`** — What does it print, and why is "always run `pwd` first" a rule in this class?

_________________________________________________________________________

2. **`cd ~`** vs **`cd`** — What is the difference, and which guarantees you start from home?

_________________________________________________________________________

3. **`mkdir -p folder/subfolder`** — What does the `-p` flag do? What happens without it if `folder` already exists?

_________________________________________________________________________

4. **`git clone URL folder_name`** — When do you clone vs when do you `git pull`? What error does re-cloning into an existing folder produce?

_________________________________________________________________________

5. **`git add file.py; git commit -m "message"; git push`** — What does each command do? What does "Password prompt = Personal Access Token" mean?

_________________________________________________________________________

---

## Part 2: Python REPL & Core Syntax (U1 + U2)

6. **`python3`** vs **`python`** — Which do we use on the VPS, and why?

_________________________________________________________________________

7. **List comprehension:** `[float(r["GPA"]) for r in rows if r["GPA"]]` — What three things does this single line do?

_________________________________________________________________________

8. **Dictionary access:** `row["Overall GPA"]` returns a **string** (e.g., `"3.7"`). What must happen before you can compare it to `4.0`?

_________________________________________________________________________

9. **`try/except` pattern for safe conversion:**

```python
def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
```

Why catch **both** `ValueError` and `TypeError`? Give one input that triggers each.

_________________________________________________________________________

10. **`int(6.5)`** — What does it return? Why is this a *choice* (not a requirement) when binning study hours?

_________________________________________________________________________

---

## Part 3: CSV & Data Loading (U2 L03, L08, L11)

11. **`csv.DictReader(f)`** — What does it return? What is the type of each row? What is the type of every value inside that row?

_________________________________________________________________________

12. **Comment lines in CSV:** A file starts with `# Mental health survey, GPA on 4.0 scale`. What happens if you pass this file directly to `csv.DictReader`? Why is this "worse than a crash"?

_________________________________________________________________________

13. **The fix — strip comments before parsing:**

```python
lines = [ln for ln in f if not ln.startswith("#")]
rows = list(csv.DictReader(lines))
```

What does `ln.startswith("#")` check? What does the list comprehension keep vs discard?

_________________________________________________________________________

14. **`csv.writer(f)`** vs **`csv.DictWriter(f, fieldnames)`** — When do we use `writer` (as in `clean_data.py`), and why does `[r[col] for col in header]` matter?

_________________________________________________________________________

15. **`newline=""` in `open()`** — What bug does it prevent on Windows? Is it harmless on Linux/macOS?

_________________________________________________________________________

---

## Part 4: Matplotlib — The Three Chart Types (U2 L03, L05, L10, L13)

16. Complete the table from memory:

| Chart type | Use when... | x-axis | y-axis | Key function |
|------------|-------------|--------|--------|--------------|
| Line plot | | | | `plt.plot()` |
| Bar chart | | | | `plt.bar()` |
| Scatter plot | | | | `plt.scatter()` |
| Histogram | | | | `plt.hist()` |

17. **`plt.plot(x, y, marker="o", linestyle="--", color="steelblue")`** — What does each argument change?

_________________________________________________________________________

18. **`plt.bar(categories, values, color=["#c0392b", "#e67e22", "#27ae60"])`** — Why pass a *list* of colors instead of one string?

_________________________________________________________________________

19. **`plt.scatter(x, y, s=10, alpha=0.4)`** — What does `s=` control? What does `alpha=` control? Why use `s=10, alpha=0.4` for 1,000 points but `s=40` for 6 points?

_________________________________________________________________________

20. **`plt.hist(data, bins=20, edgecolor="white")`** — What does `bins=20` do? What does `edgecolor="white"` do? Why is there no "correct" bin count?

_________________________________________________________________________

21. **`plt.figure()`** — When do you call it? What happens if you skip it when drawing a second chart in the same script?

_________________________________________________________________________

22. **`plt.legend()`** — What must each plotted element have for the legend to show it? What happens if you omit `label=` on one series?

_________________________________________________________________________

23. **`plt.savefig("file.png", dpi=150, bbox_inches="tight")`** — What does `dpi=150` do? What does `bbox_inches="tight"` do? **Critical rule:** `savefig` must come **before** or **after** `plt.show()`?

_________________________________________________________________________

24. **`plt.grid(True, alpha=0.3)`** — What does `alpha=0.3` change? Why not `alpha=1.0`?

_________________________________________________________________________

25. **`plt.clf()`** — What does it do? In the histogram lesson, why is it called inside the loop over bin counts?

_________________________________________________________________________

---

## Part 5: Data Cleaning Pipeline (U2 L08, L11)

26. **Sanity bounds dictionary:**

```python
SANITY = {
    "Overall GPA": (0.0, 4.0),
    "Age": (10, 22),
    "Absence Rate": (0.0, 1.0),
}
```

Why use **sanity bounds** (domain knowledge) instead of **statistical outliers** (e.g., 1.5×IQR)? Give two reasons.

_________________________________________________________________________

_________________________________________________________________________

27. **The cleaning loop pattern (from `clean_data.py`):**

```python
for r in rows:
    drop_reason = None
    for col in SANITY:
        if is_blank(r[col]):
            drop_reason = f"blank {col}"
            break
        val = to_float(r[col])
        if val is None:
            drop_reason = f"unparseable {col}"
            break
        if is_impossible(col, val):
            drop_reason = f"impossible {col}={val}"
            break
        r[col] = val
    if drop_reason:
        print(f"Dropped row: {drop_reason}")
        continue
    clean_rows.append(r)
```

What does the `break` do in each `if` block? What does `continue` at the end do? Why is `r[col] = val` important?

_________________________________________________________________________

28. **The audit assertion:** `assert rows_in == rows_out + rows_dropped, "Count mismatch"` — What bug would this catch that a simple `print` would miss?

_________________________________________________________________________

29. **Provenance statement** — You cleaned 1,000 rows down to 947. Write the one-sentence provenance statement you would put in your project `analysis.md`:

_________________________________________________________________________

---

## Part 6: Reading Charts — Vocabulary & Skepticism (U2 L03, L04, L05, L10, L12, L13)

30. **Three relationship types** a scatter plot can show:

______________________   ______________________   ______________________

31. In a scatter with `alpha=0.4`, what does a **darker region of dots** mean?

_________________________________________________________________________

32. **Histogram vocabulary** — match each term to its definition:

| Term | Definition |
|------|------------|
| Center | |
| Spread | |
| Skew | |
| Outlier | |

A. Where the bulk of the bars sit (the "typical" value)
B. How wide the bars range from lowest to highest
C. A long tail on one side (right-skewed = tail right)
D. An isolated bar far from the rest

33. **Right-skewed absence rates** — most students near 0.05, thin tail to 0.4. What does this mean in real-world words? What happens to mean vs median?

_________________________________________________________________________

34. **The "quietly wrong" pattern** — name two bugs from this unit that produce no error message but silently corrupt your charts.

_________________________________________________________________________

_________________________________________________________________________

35. **Simplifying vs misleading** — one sentence each:
   - Simplifying is...
   - Misleading is...

_________________________________________________________________________

_________________________________________________________________________

---

## Part 7: Project Readiness (U2 L14, L15)

36. The Unit 2 project requires **three visualizations** from the threat dataset. Name all three and the chart type for each:

1. ________________________________________ — chart type: _______________
2. ________________________________________ — chart type: _______________
3. ________________________________________ — chart type: _______________

37. For the **weekday vs weekend** comparison (Chart 2), what is the single most common mistake students make, and why is it wrong?

_________________________________________________________________________

_________________________________________________________________________

38. Your `analysis.md` must include a **provenance statement**. What three things must it include?

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

---

## Bonus (not graded — for discussion)

39. You built a histogram of login success rates and see three days below 0.75. Your partner says "those are outliers, drop them." You say "no, they're the story." Who is right, and why?

_________________________________________________________________________

_________________________________________________________________________

40. One habit from this unit you will use in every data project, ever:

_________________________________________________________________________

---

## Swap and grade

Graded by: ___________________________  Score: ________ / 40

## Corrections

For each miss, correct it in a second color and write one line: what I had in my head vs what is true.

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________