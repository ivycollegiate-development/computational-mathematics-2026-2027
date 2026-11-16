# Unit 2 Functional Test — Campus Network Threat Data

**Computational Mathematics**    **Total: 50 points**    **Time: 50 minutes**    **One period**

Name: ______________________________    Period: ______    Score: ______ / 50

---

## 0. What this test is

This is a **functional test**: it checks whether you can run, read and defend a working pipeline, start to finish, without being walked through it. You get a messy CSV, two worked-solution scripts, and one period. At the end of the period your repo must contain three scripts/files that run and two images that exist.

It is **not** a memory test. Everything you have done in Unit 2 is fair game to look up.

| Feature | This test |
|---|---|
| Where the work happens | The VPS only — `vscode.ivycollegiate.org` |
| Internet | **Open.** Notes, docs, browsers, AI chat, your past repos, every earlier assignment |
| What is graded | The committed artifacts: scripts that run, CSVs/PNGs that exist, analysis that is honest — and **your ability to explain any line you submitted** |
| What is *not* graded | Typing speed, memorized syntax, how fancy your chart looks |

**The one rule that outranks the open internet:** you must be able to explain, line by line, anything you submit. During the period I will walk around and ask you to point at one dropped row in your output and tell me why your script dropped it. "I don't know, the AI wrote it" is a zero for that task, no matter what the code does.

---

## 1. Clock plan — follow it

Both scripts ship complete, so running them takes minutes. That time goes into reading them — you will be asked to explain any line — and into `analysis.md`, which you write from scratch.

| Clock | Minutes | Task | You are done when |
|---|---|---|---|
| 0:00 – 0:05 | 5 | Setup and verify (Section 3) | `pwd` shows `~/functional-test`, `ls` shows `threats_raw.csv` |
| 0:05 – 0:25 | 20 | **Task 1** — read, run and be ready to defend `clean_threats.py` | `python3 clean_threats.py` prints the summary and `All checks passed`, and `threats_clean.csv` exists |
| 0:25 – 0:33 | 8 | **Task 2** — Chart 1 | `chart1_timeline.png` exists and opens |
| 0:33 – 0:40 | 7 | **Task 3** — Chart 2 | `chart2_weekday_weekend.png` exists and opens |
| 0:40 – 0:46 | 6 | **Task 4** — `analysis.md` | Three paragraphs, each with audience + number + limitation |
| 0:46 – 0:50 | 4 | Commit, push, checklist | Commit hash pasted into the Classroom assignment |

**If you fall behind, protect the order.** Run both scripts first, then write `analysis.md`. If a script fails on your machine at 0:46, write one sentence in `analysis.md` saying what failed and what you tried — a documented gap earns partial credit; a silent gap is a deduction.

---

## 2. The scenario

You are a student analyst on the campus IT security team. The automated collection system exported two months of network threat telemetry to `threats_raw.csv`. Nobody cleaned it. Your job is the honest version of the job:

1. load it,
2. clean it **with a written audit trail** — every row you remove, you can name the reason you removed it,
3. chart it twice,
4. write what the charts actually say, including what they cannot say.

The data is synthetic but plausible: weekday phishing traffic is higher than weekend traffic, and a couple of days are broken on purpose.

### The file

`threats_raw.csv` — 4 columns, in this order:

```
date,phishing_reports,failed_logins,login_success_rate
```

| Column | Type | Meaning | Unit |
|---|---|---|---|
| `date` | text | calendar day, format `YYYY-MM-DD` | — |
| `phishing_reports` | integer | phishing emails reported by users that day | reports/day |
| `failed_logins` | integer | failed login attempts across all systems that day | attempts/day |
| `login_success_rate` | decimal | successful_logins / (successful_logins + failed_logins) | 0.0 – 1.0 |

Two things will bite you if you do not look at the file before you code:

- **The first lines are not the header.** The file opens with `#` comment lines (source, column meanings, date range). `csv.DictReader` reads the *first line it sees* as the header — hand it a file that starts with a comment and every column name is wrong, with no error. This is the "quietly wrong" bug from U2 L11, and it is worth 2 points here.
- **Two rows are deliberately broken.** One has a blank cell. One has a physically impossible value. Your script must drop them, print why, and prove the arithmetic balances. Do not hand-fix the CSV — `threats_raw.csv` is read-only evidence. If you edit it, you have nothing left to prove your cleaner works.

**Do not modify `threats_raw.csv`.** Everything your script produces is a new file.

---

## 3. Setup (5 minutes) — do this in order

### 3.1 Open the VPS

Go to `https://vscode.ivycollegiate.org/`, open a terminal, and start from your home directory. Do not start inside whatever folder the editor restored from last time.

```bash
cd ~
pwd
```

`pwd` must print `/home/<your-username>` — for example `/home/slee27`. If it prints anything else, `cd ~` again before continuing. **Every path in this test is relative to `~`, so being in the wrong directory silently creates a second copy of your work that you will then fail to commit.**

### 3.2 Clone your repo — it already exists

Your test repo was created for you and already contains the data file. **Do not run `git init`. Do not fork. Do not create a new repo.**

```bash
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u2-functional-test-$(whoami)_student.git functional-test
cd functional-test
ls
```

`$(whoami)` expands to your username, so the clone URL is yours and nobody else's.

`ls` must show exactly these four entries:

```
README.md        clean_threats.py        project_charts.py        threats_raw.csv
```

If `git clone` says `destination path 'functional-test' already exists`, you cloned earlier in the year. Move into it and pull instead of cloning again:

```bash
cd ~/functional-test
git pull
```

If `ls` does **not** show `threats_raw.csv`, stop and read Section 8 (Troubleshooting) before writing any code — you are almost certainly in the wrong directory, and code written in the wrong directory cannot be submitted.

### 3.3 Verify your tools before the clock is really running

```bash
python3 -c "import csv, io; print('csv ok')"
python3 -c "import matplotlib; print('matplotlib', matplotlib.__version__)"
```

Both must print a line. If `matplotlib` is missing, run `python3 -m pip install --user matplotlib` once and re-check. Finding this out at minute 25 is the most common way students lose a chart.

### 3.4 Look at the file before you write a single line

```bash
head -12 threats_raw.csv
wc -l threats_raw.csv
```

Answer these four questions **in your head** from that output, because your script is going to answer them in code:

1. How many lines are comments, and how can you tell a comment from data?
2. Which line is the real header?
3. What is the exact column order you must preserve in the clean output?
4. What does a blank cell look like in this file — empty, `N/A`, `??`, or a lone space?

Both scripts you need already exist in your repo, and both ship **complete**: `clean_threats.py` is the worked solution for Task 1 (§4.5), `project_charts.py` is the worked solution for Tasks 2 and 3 (§5.3 and §6.3 — same file, two charts). Both define a `main()`, and `project_charts.py` builds its two charts in sequence. Run them in order, because the charts read the cleaner's output. `analysis.md` is the one file you write from scratch (Task 4), and you still create it with `touch`:

```bash
code clean_threats.py
code project_charts.py
touch analysis.md
code analysis.md
```

Run each script in a **separate** terminal command, in this order:

```bash
python3 clean_threats.py
```

Run each script in its own command block and read the output before moving on — if you open a file and run it in the same breath you will not know which one printed what.

---

## 4. Task 1 — Load and clean with an audit trail (20 points)

**File:** `clean_threats.py` — **ships complete in your repo.** It is the worked solution: read it, run it, and use its shape as the model for Tasks 2 and 3.
**Produces:** `threats_clean.csv` + a printed audit.

The whole point of this task is not "remove bad rows." It is **prove you removed exactly the rows you say you removed, and nothing else.** A cleaner that quietly drops good data is worse than no cleaner, because the chart built on it looks fine.

### 4.1 Required behaviour, in this order

The shipped script does these nine things. Read it in that order — several of them break if you reorder.

1. **Open `threats_raw.csv`** with `open("threats_raw.csv", newline="")` — the `newline=""` argument is the documented way to hand a file to the `csv` module.
2. **Strip the comment lines before the CSV parser sees them.** Read the file as text, split into lines, keep only lines that are not blank and do not start with `#` (strip whitespace before testing, so an indented `  #` is still a comment).
3. **Parse the surviving lines with `csv.DictReader`.** `DictReader` accepts any iterable of lines, so a list works directly — no temporary file needed. If you prefer to re-join the lines into one string, wrap it in `io.StringIO(...)` and import `io`.
4. **Confirm the header is the four expected columns**, in the expected order. If a column is missing you will get a `KeyError` four lines later instead of at the top where the cause is obvious.
5. **Define the sanity bounds in one dict** at the top of the file, not scattered as `if` statements:

   | Column | Low | High |
   |---|---|---|
   | `phishing_reports` | 0 | 1000 |
   | `failed_logins` | 0 | 10000 |
   | `login_success_rate` | 0.0 | 1.0 |

   A bound is a claim about what is *physically possible* in the world, not about what is typical. `0` and `1000` reports are both possible, so both stay. `-3` reports, or a success rate above `1.0` when the rate is stored as a fraction, cannot be true, so those go. Keep that distinction straight in your head — Task 4 asks you about it.
6. **Clean each row in a fixed order: blank → unparseable → impossible.** For each numeric column, in the column order above:

   - blank → drop the row, reason `"blank <column>"`
   - not convertible to a number → drop the row, reason `"unparseable <column>"`
   - outside the bound → drop the row, reason `"impossible <column>=<value-as-written>"`

   On a pass, **replace the string in the row dict with the numeric value** (`int` for the two count columns, `float` for the rate). `csv.DictReader` hands you strings, always. A chart built later on `r["failed_logins"]` without converting it plots categories, not numbers, and matplotlib will not warn you. In this file the count columns are whole numbers, so `int()` is safe; if you are ever unsure, convert with `float()` first and cast afterwards.

   The shipped reason strings are exactly `blank`, `unparseable`, `impossible`, with the column name, and with the offending value appended for `impossible`. Be ready to name the branch that prints each one and the order the three tests run in.

7. **Print every drop** as it happens, one line each, in the form:

   ```
   Dropped row: blank phishing_reports
   ```

   Blank means the cell contains nothing or whitespace. Unparseable means the cell contains something that is not a number at all. Impossible means it is a number and the number cannot be true. Getting the *category* right is worth more than getting the row count right: a row you reject for the wrong reason is a bug in your code, not bad data.

8. **Count and reconcile.** Track `rows_in` (data rows read, after the header), `rows_out` (rows written), `rows_dropped` (total), and a per-reason breakdown. Then assert the arithmetic:

   ```python
   assert rows_in == rows_out + sum(drops.values()), "Count mismatch"
   ```

   This is a genuine assertion, not a comment: if the counts disagree, the script must die with `AssertionError`, because the only thing worse than a wrong cleanup is a wrong cleanup that reports success.

9. **Write `threats_clean.csv`** with `csv.writer` and the **original header order** (write the header list yourself — do not rely on the dict key order, and do not write `DictWriter` with `restval`). Then print this summary:

   ```
   Rows in: <n>
   Rows out: <n>
   Rows dropped: <n>  {'blank': <n>, 'unparseable': <n>, 'impossible': <n>}
   All checks passed
   ```

   Exact labels and the exact final line. The numbers are whatever your run produces — never type expected numbers from a classmate or from an earlier version of the file.

### 4.2 What good output looks like

```
Dropped row: blank <column>
Dropped row: impossible <column>=<value>
Rows in: <n>
Rows out: <n>
Rows dropped: <n>  {'blank': <n>, 'unparseable': <n>, 'impossible': <n>}
All checks passed
```

The `<…>` markers stand for numbers **your** run produces. The answers are published in §4.5 — the two defects, the counts, the exact summary — but run the file and read your own output anyway: Task 4 asks you to justify each number, and "the README said so" is not a justification.

### 4.3 Definition of done — verify, don't hope

```bash
python3 clean_threats.py          # no traceback, ends with "All checks passed"
wc -l threats_clean.csv           # one more line than "Rows out" (header + data)
grep -c '^#' threats_clean.csv     # must print 0 — no comment lines copied through
head -3 threats_clean.csv          # header on line 1, numeric values, correct order
```

Then open `threats_clean.csv` and read the first three rows. The header must be exactly `date,phishing_reports,failed_logins,login_success_rate`, and no cell may be empty. An empty cell in the clean file would mean a column reached the writer without passing through `clean_row`'s checks at all.

### 4.4 Bugs the shipped script avoids — be ready to point at the line that prevents each

| Symptom | Cause | Fix |
|---|---|---|
| `KeyError: 'phishing_reports'` | The comment lines were read as the header | Strip `#` lines **before** `DictReader` |
| `ValueError: could not convert string to float: ''` | Blank check missing or after conversion | Test for blank first, drop, and `continue` |
| `ValueError: invalid literal for int() with base 10: '0.92'` | Used `int()` on the rate column | `float()` for `login_success_rate` |
| `AssertionError: Count mismatch` | Counted a row twice, or dropped without counting | One counter increment per dropped row, one per kept row |
| Clean CSV written with the wrong column order | Rebuilt the header from a dict | Write the header list explicitly |
| Script "works" but drops far more than the two real defects | Bound is a *typical* range instead of a *possible* range | Widen the bound to what is physically possible |

### 4.5 Answers — the worked solution, spelled out

`clean_threats.py` in your repo is the finished script. Here is what it finds and why, so you can check your own work against it instead of guessing.

**The file, counted.** `threats_raw.csv` is 8 comment lines, 1 header line, and 61 data rows. The comments are real comments (`# Campus Network Threat Log — …`) — no data row starts with `#`, so stripping comment lines cannot eat a measurement.

**The two defects.** Every other row passes the bounds. These are the two drops:

Two rows are worth a second look and are **not** defects: `2026-10-24` and `2026-11-25` each report `0` failed logins with a `0.0` success rate. The bounds pass them, so they stay — but 0/0 is not 0%, it is undefined, and a stricter cleaner would flag it. Naming that in `analysis.md` is a limitation nobody planted.

| Date | Row | Defect | Reason printed |
|---|---|---|---|
| 2026-10-08 | `2026-10-08,,901,0.91` | `phishing_reports` is empty | `Dropped row: blank phishing_reports` |
| 2026-10-09 | `2026-10-09,11,834,1.4` | success rate of 1.4 cannot exist | `Dropped row: impossible login_success_rate=1.4` |

**The exact run.** Output of the finished script on the shipped data:

```
Dropped row: blank phishing_reports
Dropped row: impossible login_success_rate=1.4
Rows in: 61
Rows out: 59
Rows dropped: 2  {'blank': 1, 'unparseable': 0, 'impossible': 1}
All checks passed
```

`threats_clean.csv` therefore has 60 lines — the header plus 59 data rows — with dates 2026-10-01 through 2026-11-30 minus the 8th and 9th of October.

**The six decisions the task is actually marking.**

1. **Strip comments before parsing.** `DictReader` treats its first line as the header. Feed it the raw file and the only field name is `# Campus Network Threat Log — October–November 2026`, with the rest of each row landing under the key `None`, and `DictReader` raises nothing: a plain script dies later with `KeyError`, while this one's header check raises `ValueError` immediately. Strip first, then parse.
2. **`newline=""` on both ends.** On the way in it is what the `csv` docs require; on the way out it stops `csv.writer`'s `\r\n` from being doubled to `\r\r\n` when the file is written on a platform that translates newlines.
3. **Check the header, don't assume it.** `if reader.fieldnames != HEADER: raise ValueError(...)`. A missing or reordered column then fails at the top with the actual header in the message rather than as a bare `KeyError` in the middle of the loop.
4. **Blank → unparseable → impossible, in that order, every column.** Blank first because `int("")` raises `ValueError` — a crash, not a drop. Conversion before bounds because comparing a string to a number raises `TypeError`. The category matters more than the count: a row rejected for the wrong reason is a bug in your code.
5. **`int()` for counts, `float()` for the rate.** `DictReader` hands you strings always, so `int("0.92")` on the rate column is the classic crash. The whole-number columns are safe to `int()` here; if ever unsure, `float()` then cast.
6. **Assert the arithmetic.** `rows_in == rows_out + sum(drops.values())`. Assert, not a comment: a cleanup that drops good rows but prints `All checks passed` is worse than one that falls over, because the chart built on it looks fine.

Two smaller decisions the code makes deliberately: the header is written from the `HEADER` list, never from a row dict's keys (dict order is an accident of insertion, and a wrong column order still opens fine); and `clean_row` receives `dict(row)` so a rejected row cannot half-mutate the row list.

---

## 5. Task 2 — Chart 1: daily timeline (10 points)

**File:** `project_charts.py` — **ships complete in your repo.** Both charts are in it; §5.3 gives the answers for this one.
**Produces:** `chart1_timeline.png`

```bash
code project_charts.py
```

Then run it — after `clean_threats.py`, because it reads that script's output:

```bash
python3 project_charts.py
```

### 5.1 Required behaviour

1. **Load `threats_clean.csv`** — the Task 1 output, not the raw file. `with open("threats_clean.csv", newline="") as f: rows = list(csv.DictReader(f))`.
2. **Convert at load, not at plot time.** Build three parallel lists — `dates`, `phishing`, `failed` — and convert inside the list comprehension:

   ```python
   dates    = [r["date"] for r in rows]
   phishing = [int(r["phishing_reports"]) for r in rows]
   failed   = [int(r["failed_logins"]) for r in rows]
   ```

   Strings in, numbers out, at the moment you build the list. This is the single most common silent bug in this unit: `plt.plot` will happily accept a list of numeric *strings* and draw a meaningless categorical axis without raising anything.
3. **One figure, two series**, both on the same axes:

   | Requirement | Value |
   |---|---|
   | Figure size | `plt.figure(figsize=(10, 5))` |
   | Phishing series | `marker="o"` |
   | Failed-login series | `marker="s"` |
   | Legend | present, with readable labels |
   | X label | `"Date"` |
   | X tick rotation | `rotation=45, ha="right"` so the rotated label hangs off its tick instead of overlapping the next one |
   | X tick density | about 15 labels, not one per day (see below) |
   | Y label | `"Count"` (both series are counts — say so) |
   | Y axis | `plt.ylim(bottom=0)` |
   | Layout | `plt.tight_layout()` |

   **Thin the x ticks or your axis is unreadable.** You have ~60 dates and about 9 inches of width. One label per day overlaps so badly that the axis becomes a grey smear — nobody can read a date, so the chart has no x-axis in practice. Plot every point (the line must be continuous), label only every fourth one:

   ```python
   plt.xticks(range(0, len(dates), 4), dates[::4], rotation=45, ha="right")
   ```

   Put that line **before** `plt.tight_layout()` — `tight_layout` measures the margins from the tick labels that are on the axis when it runs, so the rotated labels must already be there. Changing `4` to `3` or `5` to taste is fine; leaving all 60 labels in is not. The shipped version also forces the peak day into the tick set, so the date the title names can be found on the axis.

4. **The title states a finding, not a subject.** The shipped title is built from the data — the peak date is computed, and an assert checks that both series really do peak on it. The words "Move Together" and "Both Peak" are a claim; the assert is what keeps the claim true of this file.

   | Weak — a subject | Strong — a finding |
   |---|---|
   | "Daily Phishing Reports" | "Phishing Peaks Mid-Week While Failed Logins Stay Flat" |
   | "Failed Logins Over Time" | "Failed Logins Track Phishing on Every Spike" |
   | "Network Threat Data" | "Both Series Fall Sharply After the Break" |

   Open the chart and check the shipped title is still true of the picture under it. A column name with the underscores taken out is not a finding. The examples above show the *shape* of a finding; they are not facts about this file, and some are false here.

5. **`savefig` before anything else that clears or shows the figure.** Use exactly:

   ```python
   plt.savefig("chart1_timeline.png", dpi=150, bbox_inches="tight")
   plt.clf()
   ```

   On an interactive backend `plt.show()` blocks, and closing its window destroys the figure — a later `savefig` then writes a blank PNG, invisible unless you open the file. This script sets the `Agg` backend instead, where `show()` is a no-op: **the PNG is the deliverable, not a window.**

6. **`plt.clf()` after**, because Chart 2 is drawn in the same script. What actually prevents overdraw here is that each chart opens its own `plt.figure(...)`; drop that call *and* `clf()` and Chart 2 draws on top of Chart 1. (`plt.close()` is the more accurate call if you are not reusing the figure; `clf()` is enough here.)

### 5.2 Definition of done

```bash
python3 project_charts.py
ls -l chart1_timeline.png
```

- The script runs with no traceback.
- The PNG exists and is **not zero bytes** (anything under ~10 KB is suspicious for a 150-dpi chart — open it).
- Open the image. Do you see a date axis whose labels do **not** overlap? Two distinguishable series with a legend? A y-axis starting at zero? A title that makes a claim?

A chart you have not opened is a chart you have not checked.

### 5.3 Answers — Chart 1, spelled out

`project_charts.py` loads `threats_clean.csv` (the 59 surviving rows) and converts in the list comprehension; Chart 2 filters those same lists rather than re-reading the file, so neither chart can describe a different dataset. Here is what the finished chart contains and why each choice is the answer.

**The title, as a finding.** The script builds it from the data instead of hard-coding it:

```python
peak_count = max(phishing)
peak_date = dates[phishing.index(peak_count)]
plt.title("Phishing and Failed Logins Move Together; Both Peak on {}".format(peak_date))
```

Printed on this dataset: **"Phishing and Failed Logins Move Together; Both Peak on 2026-10-12"**. That date is the maximum of both series — 25 phishing reports and 1,678 failed logins — and the script asserts the shared peak before it titles anything, so the sentence is true of the picture under it. The date is computed; "Move Together" is still a claim the code does not measure.

**The numbers in the picture.**

| Quantity | Value |
|---|---|
| Rows plotted | 59 (the two drops from Task 1 are gone) |
| Date span | 2026-10-01 to 2026-11-30 |
| Phishing range | 0 to 25, peak 2026-10-12 |
| Failed-login range | 0 to 1,678, peak 2026-10-12 |
| Date labels drawn | 16 (every fourth point, plus the peak day) |

**The four decisions being marked.**

1. **Convert at load, not at plot time.** `[int(r["phishing_reports"]) for r in rows]`. `plt.plot` accepts numeric strings silently and draws a categorical axis; nothing raises, the chart is just wrong.
2. **Thin the ticks, keep every point.** `ticks = sorted(set(range(0, len(dates), 4)) | {peak_index})` then `plt.xticks(ticks, [dates[i] for i in ticks], rotation=45, ha="right")` — 16 readable labels instead of 59 overlapping ones, including the peak. It sits **before** `plt.tight_layout()`, so the margins are measured for the rotated labels.
3. **`savefig` first, `clf` second.** `plt.savefig(..., dpi=150, bbox_inches="tight")` then `plt.clf()`. On an interactive backend, closing a `show()` window before the save leaves a blank file; under `Agg` the save is the only way the figure reaches disk.
4. **Zero-based y-axis.** `plt.ylim(bottom=0)` with the label `Count`, because both series are counts.

**The limitation you should name in Task 4.** The two series are on very different scales: failed logins run near 700 while phishing reports run near 10. On one zero-based axis the phishing line is squashed against the bottom, so its day-to-day shape is hard to read even though the two series move together. That is a real, honest limitation of this chart — and naming it is worth more than pretending the chart shows everything. The alternative (a second y-axis) hides the scale difference instead, which is why this packet asks for one axis and a stated limitation.

**The second limitation, if you want a second one.** The dates are plotted as category labels, not as real dates: `plt.plot` spaces the 59 points evenly, so a missing day in the log would not appear as a gap — the line would run straight through it. A real date axis needs `matplotlib.dates`. Worth naming; not required.

Verified by opening the file: ~105 KB at 150 dpi, 16 non-overlapping rotated date labels with the peak day among them, two marker styles with a legend, no clipping.

---

## 6. Task 3 — Chart 2: weekday vs weekend (10 points)

**Same file**, `project_charts.py`, after Chart 1. Chart 2 filters the lists already loaded and never re-reads the CSV — reuse is the point.

### 6.1 Required behaviour

1. **Split rows by day of week** using a real date parse, not string guessing:

   ```python
   from datetime import datetime

   def is_weekend(date_text):
       return datetime.strptime(date_text, "%Y-%m-%d").weekday() >= 5
   ```

   `weekday()` returns `0` for Monday through `6` for Sunday, so `>= 5` is Saturday/Sunday. Do not compare against `"Sat"`/`"Sun"` strings — this file stores full dates.

2. **Compute the average `phishing_reports` for each group** — `sum(group) / len(group)`, once per group. Do not divide by 7, and do not divide by a hardcoded number of days: divide by the number of rows that group actually contains. A weekend average computed as `sum(weekend) / 14` is wrong even though nothing crashes.
3. **Print both averages with their sample sizes** so you can read them off the terminal — you need those numbers for the title and for `analysis.md`:

   ```
   weekday <avg> (<n> days) | weekend <avg> (<n> days)
   ```

   Read your own printed numbers. The script puts them in the bar labels and the title; you put them in `analysis.md` — one set of numbers, three places, no retyping from memory.

4. **Bar chart**, two bars, one per group:

   | Requirement | Value |
   |---|---|
   | Figure size | `plt.figure(figsize=(6, 4))` |
   | Bars | `plt.bar(["Weekday", "Weekend"], [avg_wd, avg_we])` |
   | Labels on bars | `plt.text()` at the top of each bar, formatted to 2 decimals |
   | Text placement | `ha="center", va="bottom"` so the label sits **above** the bar, not through it |
   | Title | states the finding, with **your** numbers in it |
   | Y label | `"Average phishing reports"` |
   | Y axis | zero-based, with headroom: `plt.ylim(0, max(avg_wd, avg_we) * 1.18)` |
   | Layout | `plt.tight_layout()` |
   | Save | `plt.savefig("chart2_weekday_weekend.png", dpi=150, bbox_inches="tight")` |
   | Cleanup | `plt.clf()` |

5. **Title with the comparison in it**, built by the script as `"Weekdays Average {:.2f} Phishing Reports vs Weekends {:.2f}"`. If the number in the title disagrees with the number printed on the bar, one of them came from somewhere other than the code.

6. **Headroom is not the same as a truncated axis.** `plt.ylim(0, max(avg_wd, avg_we) * 1.18)` still starts at **zero** — the rule is about the bottom of the axis, not the top. Without the top headroom the tallest bar's label is drawn right at the plot boundary and gets visually cut in half; the axis maximum is auto-scaled to the tallest bar. 18% is enough room for a two-decimal label.

7. **Guard the empty group.** If either group ends up with zero rows, `sum(...) / len(...)` raises `ZeroDivisionError`; Chart 1 is already saved by then. `chart2_weekday_weekend` checks both groups and returns with a message — belt and braces, not a graded requirement.

### 6.2 Definition of done

```bash
python3 project_charts.py
ls -l chart1_timeline.png chart2_weekday_weekend.png
```

Both files exist, both open, both have finding titles and zero-based axes. The two averages printed on the bars are the two averages in the title, and both are the ones your terminal printed.

### 6.3 Answers — Chart 2, spelled out

**The split, from the 59 clean rows.** 41 weekdays and 18 weekend days. Averages of `phishing_reports`: **weekday 11.71**, **weekend 4.78** — a weekend day carries roughly 40% of a weekday's reports.

The mandated print line, exactly as the shipped script prints it:

```
weekday 11.71 (41 days) | weekend 4.78 (18 days)
```

**The title**, built from those two variables rather than retyped:

```
Weekdays Average 11.71 Phishing Reports vs Weekends 4.78
```

**The decisions being marked.**

1. **Parse the date, don't pattern-match it.** `datetime.strptime(date_text, "%Y-%m-%d").weekday() >= 5`. `weekday()` is 0 for Monday through 6 for Sunday, so `>= 5` is Saturday/Sunday. Searching for `"Sat"` in a file of ISO dates finds nothing and silently produces an empty weekend group.
2. **Divide by the rows the group actually has.** `sum(group) / len(group)` — 41 and 18, not 7, not 59. A weekend average written as `sum(weekend) / 14` is wrong and does not crash, which is exactly why it is worth marks.
3. **Label above the bar, with headroom.** `plt.text(..., ha="center", va="bottom")` for placement, `plt.ylim(0, max(avg_wd, avg_we) * 1.18)` for air. The bottom stays at zero — headroom is a top-of-axis decision, not permission to truncate the scale.
4. **Reuse the rows.** Chart 2 filters the `rows` list Chart 1 already loaded. Re-reading the CSV in the same script means two chances for the two charts to describe different data.
5. **Two decimals, three places, one source.** The printed line, the bar label and the title all come from `avg_wd` and `avg_we`. If the number on the bar disagrees with the number in the title, one of them was typed.

**The limitation this chart is begging for.** 18 weekend days against 41 weekdays: the weekend average is the less stable of the two, and one unusual weekend moves it several tenths. And the split compares *day types*, not causes — a lower weekend average is a fact about traffic, not evidence that anyone rests. Both of those sentences belong in Task 4's second paragraph.

Verified by opening the file: 32 KB at 150 dpi, two bars, `11.71` and `4.78` readable above their bars with nothing clipped.

---

## 7. Task 4 — Analysis (10 points)

**File:** `analysis.md`

```bash
touch analysis.md
code analysis.md
```

Three paragraphs. Not three bullet lists, not one long paragraph with numbers in it — three paragraphs of prose, roughly 80–120 words each.

### 7.1 Paragraph 1 — Chart 1 (the timeline)

Must contain, clearly and explicitly:

- **A named audience.** Pick one and say it: the school board, the IT director, or students. "Everyone" is not an audience; a chart that is for everyone is read by no one.
- **The one number they should notice.** One. Quote it, with its date or its average, from what your chart actually shows.
- **One honest limitation.** Something the chart genuinely cannot tell that reader — e.g. the number of days in the window, the days dropped by your cleaner, the fact that correlation across a month is not a trend, or that the y-axis compresses one series to make the other readable.

### 7.2 Paragraph 2 — Chart 2 (weekday vs weekend)

Same three elements, plus the limitation this chart is begging for: it compares a small number of weekend days against a larger number of weekdays, so the weekend average is the less stable of the two. Name both sample sizes.

Also worth saying, if it is true of your data: the split compares *day types*, not causes. A drop on weekends is a fact about traffic, not evidence that the attacker rests.

### 7.3 Paragraph 3 — synthesis: the honest version

This paragraph is the one that earns the last 4 points, and it is not a summary. Answer:

1. **What would the dishonest version of these two charts look like?** Be concrete: an axis that starts at a number other than zero so a small difference looks huge; a title that names a subject instead of a finding; a dropped row that was silently dropped because it spoiled the story.
2. **What in the shipped code avoids each of those?** Point at the exact line: the zero-bottom `ylim`, the computed finding title, the printed drop reasons, the assertion that reconciled the counts.

Name at least **two** of the Unit 2 honesty principles:

| # | Principle | What it looks like in code |
|---|---|---|
| 1 | The y-axis starts at zero unless you say why not | a zero bottom on both charts: `plt.ylim(bottom=0)` / `plt.ylim(0, …)` |
| 2 | Every dropped row is documented | one printed `Dropped row: <reason>` per drop |
| 3 | An outlier is signal until proven noise | the near-zero days stay in the dataset |
| 4 | The title states the finding, not the subject | "Weekdays Average 11.71 Phishing Reports vs Weekends 4.78", not "Phishing reports" |
| 5 | The chart is designed for a named audience | the audience sentence in each paragraph |
| 6 | Provenance is stated | what you cleaned, how many rows, and why |

### 7.4 The rule that decides these 10 points

**Every number in `analysis.md` must be a number your own run printed or your own chart shows.** The answer sections (§4.5, §5.3, §6.3) carry the same numbers, so quote one only after you have seen it in your own terminal or in your own image — not from a classmate, and not from an AI answer that used a different file. A single number you cannot trace to your own terminal output turns an honest analysis into a fabricated one, and fabrication scores zero on this task regardless of how well it reads.

### 7.5 Definition of done

```bash
wc -w analysis.md     # ~250–360 words total
cat analysis.md
```

Read it as if you were the IT director. Can you find the audience, the number, and the limitation in each of the first two paragraphs without hunting? Does the third paragraph point at your own code?

---

## 8. Troubleshooting

| What you see | What it means | What to do |
|---|---|---|
| `KeyError: 'date'` / column names look like a sentence | `DictReader` used a comment line as the header | Strip `#` lines before parsing; print `reader.fieldnames` to confirm |
| `ValueError: could not convert string to float: ''` | A blank cell reached `float()` | Blank check first, drop, `continue` |
| `AssertionError: Count mismatch` | Your counters do not reconcile | Count once per row, on exactly one branch |
| PNG is blank / white / 0 bytes | `plt.show()` ran before `savefig` | Save first, `show()` last or never |
| `chart2` looks like `chart1` | Chart 2 drew on Chart 1's figure | Keep `plt.figure(...)` at the top of each chart and `plt.clf()` after each `savefig` |
| The date axis is an unreadable smear | ~60 labels on ~9 inches of axis | Thin the ticks: `plt.xticks(range(0, len(dates), 4), dates[::4], rotation=45, ha="right")`, before `tight_layout()` |
| The bar's number is sliced in half at the top | Axis top auto-scaled to the bar height | `plt.ylim(0, max(avg_wd, avg_we) * 1.18)` |
| Y axis starts near 600, not 0 | `ylim(bottom=0)` missing | Add it — this is graded on both charts |
| X axis shows numbers like 0, 5, 10 instead of dates | You plotted categories, not dates, or the list is unsorted | Convert at load; keep the file's chronological order |
| `ValueError: x and y must have same first dimension` | One list skipped a row that another kept | Build all three lists in one pass over the same `rows` |
| `ModuleNotFoundError: matplotlib` | Wrong interpreter or a fresh shell | `python3 -m pip install --user matplotlib`, re-run |
| `fatal: not a git repository` | You are outside `~/functional-test` | `cd ~/functional-test`; never `git init` |
| `fatal: could not read Username` / auth rejected | GitHub wants a token, not a password | Username + **Personal Access Token** |
| Push rejected, `fetch first` | Remote has a commit you do not | `git pull --rebase`, resolve, push again |
| Everything looks right but `git status` shows nothing to commit | You wrote `analysis.md` in `~`, not in the repo | Move it in: `mv ~/analysis.md ~/functional-test/` |

---

## 9. Acceptance checklist — tick only what is true

Run each check; do not tick from memory.

- ☐  I am in `~/functional-test` (`pwd`), and `threats_raw.csv` is unmodified
- ☐  `python3 clean_threats.py` runs with **no traceback** and ends with `All checks passed`
- ☐  The summary prints `Rows in`, `Rows out`, `Rows dropped` with the `{'blank': …, 'unparseable': …, 'impossible': …}` breakdown
- ☐  The counts reconcile: rows in = rows out + rows dropped, and the assertion is in the code
- ☐  `threats_clean.csv` exists, has the 4-column header in the original order, contains **no** `#` lines, and **no** empty cells
- ☐  `python3 project_charts.py` runs with **no traceback**
- ☐  `chart1_timeline.png` exists, opens, has a finding title, `Date` / `Count` labels, a legend, and a zero-based y-axis
- ☐  `chart2_weekday_weekend.png` exists, opens, has a finding title, bar labels, and a zero-based y-axis
- ☐  The two averages printed on the bars match the two averages in the title and in `analysis.md`
- ☐  `analysis.md` has exactly three paragraphs; paragraphs 1 and 2 each name audience + number + limitation
- ☐  Paragraph 3 names at least two honesty principles and describes the dishonest alternative
- ☐  `git log --oneline -1` shows my commit, and I have pasted that line into the Classroom assignment

---

## 10. Scoring (50 points)

| Task | Points | Criteria |
|---|---|---|
| 1. Load & Clean | 20 | Comment strip before `DictReader`; bounds dict for all three columns; per-row drop reasons in the right category; audit assertion; clean CSV with original header order; summary with correct counts |
| 2. Chart 1 | 10 | Correct data as numbers; finding title; zero-based honest y-axis; both axis labels; legend; rotated ticks; `savefig` before `show`; `clf` |
| 3. Chart 2 | 10 | Correct weekday/weekend split by parsed date; correct averages; averages printed on the bars; finding title; zero-based axis; `savefig` before `show`; `clf` |
| 4. Analysis | 10 | Three paragraphs; audience + key number + limitation in each of the first two; synthesis names at least two honesty principles; every number traceable to your own output |

### Deductions

| Deduction | Condition |
|---|---|
| −5 | `plt.show()` before `savefig` (blank PNG) |
| −5 | Missing audit assertion, or counts that do not reconcile |
| −5 | Y-axis not starting at zero, with no justification in `analysis.md` |
| −5 | A missing chart or file that `analysis.md` does not mention |
| −3 each | Missing `plt.clf()` between charts (overlapping/duplicate output) |
| 0 on Task 4 | A number in `analysis.md` that your own script never printed |
| 0 on a task | You cannot explain a line you submitted for that task |

**Partial credit is real.** A Task 1 that cleans correctly and prints drops but never writes the CSV still earns most of its 20. A chart saved with a subject title instead of a finding title loses 3, not 10. Submit what works; document what does not.

---

## 11. Not graded — do not spend test time on it

These are good habits from the unit. They are worth zero points here, and doing them while a chart is missing is a bad trade.

- The optional `--drill` mode (injecting fake broken rows to prove the cleaner catches them).
- Colour choices, `edgecolor`, font sizes, and any styling beyond what is listed above.
- Refactoring the shipped scripts further, renaming their variables, or splitting them into more files.
- A README, comments in every line, or docstrings.
- Chart 3 (the login-success-rate histogram). This test asks for two charts.

---

## 12. Submit

Your repo already exists and already contains `threats_raw.csv`. **Do not run `git init`.**

```bash
cd ~/functional-test
git add .
git status                 # read this: is every file you made listed?
git commit -m "Unit 2 functional test submission"
git push origin main
git log --oneline -1
```

Then paste the whole `git log --oneline -1` line — short hash **and** message — into the Classroom assignment **U2 Functional Test — Live Coding**. No pull request is needed; you push straight to your own repo.

**Commit both the scripts and the outputs.** `git add .` covers `clean_threats.py`, `project_charts.py`, `analysis.md`, `threats_clean.csv`, and both PNGs. If you add files one at a time, `git status` must show a clean tree before you push — a commit that contains only the PNGs loses your code, and the code is most of the grade.

**Password prompt = Personal Access Token, not your GitHub password.** If the token is rejected, re-enter your username and paste the token again; it is not a typo in your password.

**If the push fails, keep working locally and tell me at the end.** I can collect the work from the VPS directly — but only if the files are in `~/functional-test`. Work left in `~` is not collectable.

---

## 13. Rehearsal — the honest way to prepare

The answers are published, so rehearsing the *answers* is not preparation — reading them is not a skill. What is still graded, and still unrehearsed, is whether you can do this yourself when the file is not in front of you. Tonight, on your own time, in `compmath-u2-data-lab` (the project repo — not the test repo):

1. Open `clean_threats.py` from your test repo, read it once, then close it and retype its four functions into a new file, `clean_*.py`, in the project repo. Run it on one of the project's messier files, not the one in your test repo. If you cannot rebuild the comment-strip, the three bounds, the per-row drop reasons and the count assertion without looking, that is the task that will cost you points.
2. Retype the chart calls the same way — two series, finding title, zero-based axis, `savefig` before `show`, `clf` between charts — and check with your own eyes that both PNGs open.
3. Write three paragraphs of analysis for a named audience, each with one number and one limitation — from memory of the structure, not by copying the exemplar.
4. Push it.

If you can rebuild that pipeline from a blank file in 45 minutes tonight, you can rebuild it in 50 tomorrow with the shipped file sitting in your cloned repo as your reference. If you cannot, you now know exactly which of the four tasks is going to cost you points, and you have time to fix it.

---

**Time starts when I say it starts. 50 minutes. Work in order, verify by running, and submit something that runs.**
