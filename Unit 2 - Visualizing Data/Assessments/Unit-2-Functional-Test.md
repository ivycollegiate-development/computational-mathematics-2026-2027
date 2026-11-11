# Unit 2 Functional Test — Live Coding on VPS
**50 minutes. Closed notes. VPS only — no browser, no local files, no AI. One terminal, one editor.**

---

## Rules

- **No notes, no browser, no chat.** You may use `man`, `--help`, and the Python REPL (`python3`).
- **Start in a fresh terminal.** `cd ~` first. Run `pwd` and confirm you are in `/home/<your-username>`.
- **All work in `~/functional-test/`.** Create it, work there, submit from there.
- **Submit:** `git` push to a new repo `compmath-u2-functional-test-<your-username>_student` (the invitation email has the link). Push your work, then submit the **PR link** to Classroom.
- **Keep the terminal open** — spot-checks happen.

---

## The Scenario

You are given a raw CSV file `threats_raw.csv` with campus network threat data. It has **comment lines**, **messy values**, and **missing data**. Your job: load it, clean it with an audit trail, and produce **two visualizations** with honest analysis.

The file has these columns:
```
date, phishing_reports, failed_logins, login_success_rate
```

---

## Task 1 — Load & Clean with Audit (20 pts)

**Create `clean_threats.py`** that:

1. **Reads `threats_raw.csv`** (in the same directory)
2. **Strips comment lines** (lines starting with `#`) **before** `csv.DictReader`
3. **Defines sanity bounds** for all three numeric columns:
   - `phishing_reports`: (0, 1000)
   - `failed_logins`: (0, 10000)
   - `login_success_rate`: (0.0, 1.0)
4. **Cleans every row** using the pattern from class:
   - Blank check → drop reason `"blank <col>"`
   - Convert to float/int → drop reason `"unparseable <col>"`
   - Bounds check → drop reason `"impossible <col>=<val>"`
   - On pass: replace string with numeric value in the row dict
5. **Prints each dropped row's reason** (e.g., `Dropped row: blank phishing_reports`)
6. **Tracks counts:** `rows_in`, `rows_out`, `rows_dropped` (with per-reason breakdown)
7. **Audit assertion:** `assert rows_in == rows_out + rows_dropped, "Count mismatch"`
8. **Writes cleaned rows** to `threats_clean.csv` with the **original header order** (use `csv.writer` + header list)
9. **Prints summary:**
   ```
   Rows in: <n>
   Rows out: <n>
   Rows dropped: <n>  {'blank': <n>, 'unparseable': <n>, 'impossible': <n>}
   All checks passed
   ```

**Run it and verify:** `python3 clean_threats.py` → six `[PASS]` lines, clean CSV written.

---

## Task 2 — Chart 1: Daily Timeline (15 pts)

**Create `project_charts.py`** that:

1. **Loads `threats_clean.csv`** (your output from Task 1) with `csv.DictReader`
2. **Builds three parallel lists:** `dates`, `phishing`, `failed` (all numeric where appropriate)
3. **Creates a line chart** with:
   - `plt.figure(figsize=(10, 5))`
   - Both series: `phishing_reports` (marker="o") and `failed_logins` (marker="s")
   - **Title states the finding**, not the subject (e.g., "Phishing Spikes Mid-Week; Failed Logins Steady")
   - **X-axis:** "Date" with `rotation=45`
   - **Y-axis:** "Count" with `plt.ylim(bottom=0)`
   - `plt.legend()`, `plt.tight_layout()`
   - **`plt.savefig("chart1_timeline.png", dpi=150, bbox_inches="tight")`** — **BEFORE any `show()`**
   - `plt.clf()`

---

## Task 3 — Chart 2: Weekday vs Weekend (15 pts)

**In the same `project_charts.py`** (after Chart 1, same `rows` list):

1. **Split rows** into weekday vs weekend using `datetime.strptime(date, "%Y-%m-%d").weekday() >= 5`
2. **Compute average phishing reports** for each group
3. **Create a bar chart** with:
   - `plt.figure(figsize=(6, 4))`
   - `plt.bar(["Weekday", "Weekend"], [avg_wd, avg_we])`
   - **Print both averages on the bars** with `plt.text()`
   - **Title states the finding** (e.g., "Weekdays Average 8.0 Phishing Reports vs Weekends 2.9")
   - **Y-axis:** "Average phishing reports" with `plt.ylim(bottom=0)`
   - `plt.tight_layout()`
   - **`plt.savefig("chart2_weekday_weekend.png", dpi=150, bbox_inches="tight")`**
   - `plt.clf()`

---

## Task 4 — Analysis (15 pts)

**Create `analysis.md`** with **three paragraphs** (one per chart + one synthesis):

**Paragraph 1 (Chart 1):** What the timeline shows for your named audience (school board / IT director / students), the **one number they should notice**, and **one honest limitation**.

**Paragraph 2 (Chart 2):** What the weekday/weekend comparison shows for your audience, the **one number**, and **one honest limitation** (hint: unequal sample sizes).

**Paragraph 3 (Synthesis):** Connect both charts to the **Unit 2 honesty principles** — what would a dishonest version of these charts look like, and what did you do to avoid it?

---

## Acceptance Checklist (verify before submit)

- [ ] `clean_threats.py` runs with **no error output**, prints summary with counts
- [ ] `threats_clean.csv` exists and has **no comment lines**, numeric columns
- [ ] `project_charts.py` runs with **no error output**, produces **both PNGs**
- [ ] `chart1_timeline.png` and `chart2_weekday_weekend.png` **render** (open them)
- [ ] `analysis.md` has **three paragraphs**, each with audience, key number, limitation
- [ ] `analysis.md` synthesis paragraph names **honesty principles** from Unit 2
- [ ] **Git repo** has all files committed and pushed
- [ ] **PR opened** on GitHub with latest commit visible

---

## Scoring (50 pts total)

| Task | Points | Criteria |
|------|--------|----------|
| 1. Load & Clean | 20 | Comment strip, sanity bounds, per-row drop reasons, audit assertion, clean CSV, summary prints |
| 2. Chart 1 | 15 | Correct data, finding title, honest y-axis, labels, legend, savefig before show, clf |
| 3. Chart 2 | 15 | Correct split, averages printed on bars, finding title, honest y-axis, savefig before show, clf |
| 4. Analysis | 15 | Three paragraphs, audience + key number + limitation each, synthesis names honesty principles |
| **Deductions** | | |
|  | -5 | Any `plt.show()` before `savefig` (blank PNG) |
|  | -5 | Missing audit assertion or count mismatch |
|  | -5 | Y-axis not starting at 0 without justification in analysis |
|  | -5 | Silent gap (missing chart/file) without documentation in analysis |
|  | -3 per | Missing `plt.clf()` between charts (overlap) |

---

## Submit

1. `cd ~/functional-test`
2. `git init`
3. `git add .`
4. `git commit -m "Unit 2 functional test submission"`
5. `git remote add origin https://github.com/ivycollegiate-development/compmath-u2-functional-test-$(whoami)_student.git`
6. `git push -u origin main`
7. Open PR on GitHub → submit **PR link** to Classroom assignment "U2 Functional Test"

**Password prompt = Personal Access Token, not your GitHub password.**

---

**Time starts now. 50 minutes. Good luck.**