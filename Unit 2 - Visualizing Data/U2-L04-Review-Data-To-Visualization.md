# U2 L04 — Review: From Data to Visualization

**LO:** consolidate U2 L02–L03 concepts — messy data, CSV reading, first matplotlib plots — before advancing to chart customization in L05.

No new content today. You have seen real datasets, read CSV files with the stdlib, and produced your first labeled scatter plot. This lesson checks that the foundation is solid before L05 adds customization (colors, legends, savefig, bar/line/scatter choice).

---

## PART 1 — CONCEPT CHECK (15 min, closed notes)

Answer in your notes. One sentence each unless marked.

### A. Data vs. Numbers (from L02)
1. What is the difference between "a number" and "data"?
2. The study-habits file had 53 lines but only 52 students. Why?
3. The mental-health file crashed when you tried `messy[0][1] + 1`. What was on line 1, and why did it break your code?

### B. CSV Reading Mechanics (from L02)
4. What does `csv.reader` return for each row — a list, a dict, or a string?
5. If a CSV has a comment line (`# ...`) then a header, which slice skips both correctly: `[1:]`, `[2:]`, or `[3:]`?

### C. First Visualization (from L03)
6. You have `days = [1,2,3]` and `temps = [12,18,9]`. Which call makes a line chart: `plt.plot(days, temps)` or `plt.scatter(days, temps)`?
7. A chart without labels is a rumor. What **three things** must every plot have? (L03 rule)
8. You plotted Test_Score vs. Study_Hours with `plt.scatter`. Why `scatter` and not `plot`?
9. What does `plt.savefig("chart.png", dpi=150)` do that `plt.show()` does not?

### D. Quick Apply
10. (2 points) This code has two bugs. Name both:
```python
import matplotlib.pyplot as plt
plt.bar(["A", "B", "C"], [10, 20, 15])
plt.title("Scores by Group")
plt.savefig("groups.png")
plt.legend()
```
(Hint: what does `legend()` show when nothing has a `label=`, and which axis has no name?)

---

## PART 2 — LIVE REBUILD (20 min)

Open your lab repo and rebuild the L03 scatter plot **from memory** — no copy-paste from old screenshots.

```bash
cd ~/compmath-u2-data-lab
git pull
python3
```

In the REPL, reconstruct the complete L03 Part 4 script:
- Load `data/u2_dataset1_study_habits.csv` with `csv.reader`
- Skip the header
- Extract `Study_Hours` (column 1) and `Test_Score` (column 2) as floats
- Build a scatter plot with: title, x-label with units, y-label with units, grid
- `savefig("review_scatter.png", dpi=150)`

If you get stuck, check your L03 notes — but the goal is to do it cold.

---

## PART 3 — EXTENSION: ADD A SECOND SERIES (10 min)

Using the **same dataset**, add `Sleep_Hours` (column 3) as a second scatter series in a different color with `label=` and `plt.legend()`. Save as `review_two_series.png`.

In your notes: what relationship (if any) do you see between Sleep_Hours and Test_Score?

---

## PART 4 — PAPER CHECK PREVIEW (5 min)

Tuesday (U2 L06) is a paper check on L03–L05 concepts. In your notes, write one question you would put on that check for each of these topics:
- CSV reading (header vs. comment line)
- Chart anatomy (title, x-label, y-label, units)
- Chart type choice (line vs. bar vs. scatter)

---

## PART 5 — JOURNAL + PUSH (last 10 min)

```bash
cd ~/compmath-u2-data-lab
touch journal-u2l04.md
```

Answer in 2–3 sentences each:
- Which L02/L03 concept felt shakiest today, and what did you do to firm it up?
- What is one thing about matplotlib that still surprises you?
- Paste the output of `ls -lh review_scatter.png review_two_series.png` showing both files exist.

```bash
git add journal-u2l04.md review_scatter.png review_two_series.png
git commit -m "U2 L04 review: data to visualization"
git push
```

---

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. Your Part 1 answers (1–10)
2. Your Part 2 REPL session showing the rebuilt scatter plot working
3. Your Part 3 two-series plot on screen
4. `ls -lh` proving both PNGs exist
5. Successful `git push`

Submit the screenshot to this assignment on Google Classroom.

---

**Next:** U2 L05 — Matplotlib: Customizing Plots (https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%202%20-%20Visualizing%20Data/U2-L05-Matplotlib-Customizing-Plots.md)