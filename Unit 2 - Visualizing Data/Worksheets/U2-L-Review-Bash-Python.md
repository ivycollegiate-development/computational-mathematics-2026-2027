# U2 Review — Bash Commands & Python Function Properties
**Closed notes. 15 minutes. Swap and grade with the key — corrections in a second color.**

---

## Part 1: Terminal & Git — The Daily Loop (U1 + U2)

1. **`pwd`** — What does it print, and why is "always run `pwd` first" the first rule of every lab?

_________________________________________________________________________

2. **`cd ~`** vs **`cd ~/compmath-u2-data-lab`** — You are in `/home/student`. What does each command do? Which one do you run at the start of *every* lesson?

_________________________________________________________________________

3. **`ls -la`** — What do the flags `-l` and `-a` show? Name one "hidden" file you will see in your lab repo that starts with `.`.

_________________________________________________________________________

4. **`git pull`** — When do you run it? What does "Already up to date." mean? What does a merge conflict message look like, and what is your first step?

_________________________________________________________________________

5. **The push loop** — Write the exact four commands (in order) to commit and push your changes. What does "Password prompt = Personal Access Token" mean?

_________________________________________________________________________

---

## Part 2: Python Function Properties — What You've Been Writing All Unit

6. **Function signature** — In `def load_and_clean(csv_path, sanity_dict):`, what are the **parameters**? What is the **return value** (type and meaning)?

_________________________________________________________________________

7. **`csv_path`** — What type of argument do you pass when calling this function? Give a concrete example from your project.

_________________________________________________________________________

8. **`sanity_dict`** — What is its structure? Write a minimal valid example.

```python
sanity_dict = ____________________________________________________________
```

9. **Inside the function — the cleaning pattern** — You have a `rows` list from `csv.DictReader`. Every value is a **string**. What three steps must happen to each value in a sanity column before it becomes a clean `float`?

Step 1: _________________________________________________________________
Step 2: _________________________________________________________________
Step 3: _________________________________________________________________

10. **`to_float` helper** — Why does it catch **both** `ValueError` and `TypeError`? Give one input for each.

_________________________________________________________________________

11. **The audit assertion** — `assert rows_in == rows_out + rows_dropped, "Count mismatch"` — What specific bug would this catch that `print(rows_in, rows_out, rows_dropped)` would not?

_________________________________________________________________________

---

## Part 3: Matplotlib — The Three Chart Functions You Must Know

12. Complete the table — **from memory**:

| Function | x-axis type | y-axis type | Use when... |
|----------|-------------|-------------|-------------|
| `plt.plot()` | | | |
| `plt.bar()` | | | |
| `plt.scatter()` | | | |
| `plt.hist()` | | | |

13. **Critical rule** — `plt.savefig("file.png")` must come **before** or **after** `plt.show()`? Why?

_________________________________________________________________________

14. **Honest axis** — One line of code to force the y-axis to start at 0:

```python
plt.__________________________________________________________________
```

---

## Part 4: Unit 2 Honesty Principle

15. **Scenario:** Your histogram of login success rates has a tail to 0.0. Your partner says "drop the outliers." You say "no." What is the **one-sentence principle** from Unit 2?

_________________________________________________________________________

---

## Swap and Grade

Graded by: ___________________________  Score: ________ / 15

## Corrections

For each miss, correct it in a second color and write one line: **what I had in my head vs what is true.**

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________