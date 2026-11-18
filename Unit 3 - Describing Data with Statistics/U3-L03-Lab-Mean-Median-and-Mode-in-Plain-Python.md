# U3 L03 — Lab: Mean, Median, and Mode in Plain Python

**LO:** compute mean, median, and mode from a real dataset in Python, and state which one is robust and why.

**This lesson runs over two class days.**

- **Day 1** — set up your repo, create `centers.py`, load the data, and finish the mean.
- **Day 2** — the median, the mode, the finished file, what each measure throws away, and the push.

You predicted on the paper day and you did the arithmetic by hand on seven
numbers. Now you do it in code, on all 200 real donations, and you check whether
the seven-number story held up.

No `statistics` library and no pandas. You write all three yourself — the point
is to know what the code is doing when a real library does it for you.

## WHAT YOU ARE CREATING

One file, at the **top level of your repo** (not inside `data/`):

```text
compmath-u3-stats-lab/
├── data/            ← ships with the clone. Do not edit anything in here.
│   └── u3_donations.txt
└── centers.py       ← this is the only file you create in this lesson
```

`centers.py` must define these three functions. Each takes one list of numbers
and returns a single result:

| Function | Returns | Must handle |
|---|---|---|
| `mean_of(values)` | the sum divided by the count | any length |
| `median_of(values)` | the middle value **after sorting** | both an odd and an even count |
| `mode_of(values)` | `(value, count)` for the most common value, or `None` if no value repeats | a set where nothing repeats |

The file also has to run on its own. `python3 centers.py` must print the
comparison table in PART 4 — not just define the functions, but call them and
print the result.

**Done when, in your own repo:**

- ☐  `centers.py` sits at the repo root and `python3 centers.py` prints the table
- ☐  the table shows `716.07` mean / `242.76` median for all 200, and `267.40` / `242.38` with the outlier removed
- ☐  `git remote -v` shows your own username, not a classmate's
- ☐  the commit is pushed and you have the push confirmation line

# DAY 1 — SET UP, LOAD, AND THE MEAN (50 min)

You leave Day 1 with a working `centers.py` that loads the donations and prints
the mean, committed and pushed. Nothing on Day 1 is thrown away — Day 2 adds to
the same file.

## PART 0 — SET UP (5 min)

Clone **your own** Unit 3 repo. On this machine `whoami` prints your username
without the `_student` ending, so the command adds it back — that gives each
student a different repo, and nobody shares a copy. Every dataset for this unit
ships inside it, in `data/`. You never install anything.

```bash
cd ~ && git clone https://github.com/ivycollegiate-development/compmath-u3-stats-lab-$(whoami)_student.git compmath-u3-stats-lab
cd compmath-u3-stats-lab
ls data/
```

Already cloned it on U3 L01? Do not clone it twice. Get into the copy you have
and pull anything new:

```bash
cd ~/compmath-u3-stats-lab && git pull
```

Prove the copy is yours before you type a line of Python:

```bash
git remote -v
```

The URL must contain your username. If it contains a classmate's, you cloned the
wrong repo — go back to `cd ~`, remove that folder, and re-run the clone above
with your own URL.

## PART 0b — CREATE THE FILE AND LOAD THE DATA (12 min)

You do not work at the `>>>` prompt today. Every line you write goes into one
file — `centers.py` — and you run that file with `python3`. That file is what you
push at the end of the lesson.

**Step 1 — be in the repo root.** The data path is *relative*, so it only
resolves when your terminal is inside the repo. Check before you write anything:

```bash
cd ~/compmath-u3-stats-lab
pwd                          # the last part must read /compmath-u3-stats-lab
ls data/u3_donations.txt     # must print the path, not an error
```

If `pwd` shows anything else, or `ls` says "No such file or directory", you are
in the wrong folder. Go back to PART 0 — nothing below will work from there.

**Step 2 — create the file.** In the repo root, not inside `data/`:

```bash
touch centers.py
code centers.py
```

`code centers.py` opens it in the VS Code pane. No editor pane? Use
`nano centers.py`, type the code, then Ctrl+O, Enter, Ctrl+X to save and quit.

**Step 3 — type the load into it.** The file you are reading from is
`data/u3_donations.txt`: 201 lines, line 1 a comment, then 200 donation amounts.
Type this, exactly:

```python
with open("data/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

donations = [float(line) for line in raw if not line.startswith("#")]
print(len(donations), "values")
```

What each piece does:

- `open("data/u3_donations.txt")` — opens the file for reading. The `with` block
  closes it again when the block ends.
- `line.strip()` — removes the newline at the end of each line.
- `if line.strip()` — skips blank lines, so a trailing empty line does not
  become a value.
- `if not line.startswith("#")` — drops the comment line. This is the same shape
  as Unit 2: one comment line on top, then values.
- `float(line)` — turns each remaining piece of text into a number, so the list
  holds `338.66`, not `"338.66"`.
- `print(len(donations), "values")` — your proof that the load worked.

**Step 4 — save and run it.** Ctrl+S to save, then in the terminal:

```bash
python3 centers.py
```

Expected output — exactly one line:

```text
200 values
```

Three ways this goes wrong, and what each means:

- `FileNotFoundError: data/u3_donations.txt` — your terminal is not in the repo
  root. Back to Step 1.
- `SyntaxError` — indentation or a quote mark copied wrong. The message names the
  line; fix that line, save, run again.
- `IndentationError` — the two lines inside `with` must be indented by four
  spaces, and `donations = ...` must be back at the left margin.

**Step 5 — this file is the whole lesson.** Every PART from here adds lines to
`centers.py` and re-runs `python3 centers.py`. Leave the load block at the top of
the file — that is what makes the data available on every run. Never edit
anything inside `data/`.

## PART 1 — THE MEAN (12 min)

The mean is the sum divided by the count. The trap is dividing by the wrong
count. Add this below your load block, save, and run `python3 centers.py` again:

```python
n = len(donations)
total = sum(donations)
mean = total / n

print(f"n = {n}, total = {total:.2f}")
print(f"mean = {mean:.2f}")
```

In your notes:

- What did you get? Compare to the paper day: the mean of the seven numbers
  with the outlier was 1335.71. Why is this one so much smaller? (How many
  numbers are being averaged here?)

## PART 1b — WITH AND WITHOUT THE OUTLIER (12 min)

The donor file's comment said one entry is a mis-key. Try the mean without it,
without deleting anything permanently — add this below the mean lines, save,
run:

```python
clean = [d for d in donations if d < 5000]
print(f"mean with    outlier: {sum(donations)/len(donations):.2f}")
print(f"mean without outlier: {sum(clean)/len(clean):.2f}")
```

In your notes:

- The answer should be **267.40** without the outlier. How many times bigger
  is the mean *with* it? Why does **one** value out of 200 move the mean so
  much at all? (Think about what the mean is: a sum with a division at the
  end. The outlier is enormous inside that sum, and the division only
  divides by 200.)
- Write down what you still cannot tell about these 200 donations from the mean
  alone. Keep that list — Day 2 answers it.

## PART 1c — DAY 1 EXIT: COMMIT AND PUSH (9 min)

Day 1 ends with your work saved on GitHub, not just in the editor. Inside your
repo:

```bash
ls centers.py                 # must be here, at the top level
python3 centers.py            # must print 200 values, n, total, mean, and both outlier lines
git add centers.py
git commit -m "U3 L03 day 1: load donations and compute the mean"
git push
```

If `ls` says "No such file or directory", you are in the wrong folder or you
saved `centers.py` inside `data/`. Fix that before you commit — a file in the
wrong place is the one thing that fails this lab.

**Day 1 is done when:** `centers.py` is on your GitHub repo, `python3 centers.py`
prints `200 values` and the mean, and you can say out loud what the outlier did
to the mean.

# DAY 2 — MEDIAN, MODE, AND THE FINISHED FILE (50 min)

Everything today happens in the same `centers.py` you pushed on Day 1. Start by
getting back into it:

```bash
cd ~/compmath-u3-stats-lab && git pull
code centers.py
python3 centers.py            # the Day 1 output must still print
```

If that last command fails, your Day 1 work is not in the folder — re-type the
load block from PART 0b before going on.

## PART 2 — THE MEDIAN (12 min)

The median is the middle value **after sorting**. It is built from position,
so its size does not depend on how big the numbers are. Add this below your mean
lines, save, run:

```python
ordered = sorted(donations)
n = len(ordered)

if n % 2 == 1:
    median = ordered[n // 2]
    print("odd count, middle value:", median)
else:
    lower = ordered[n // 2 - 1]
    upper = ordered[n // 2]
    median = (lower + upper) / 2
    print(f"even count, mean of the two middle: ({lower:.2f} + {upper:.2f}) / 2 = {median:.2f}")
```

Our n is **200**, which is even. So there is no single middle value.

In your notes:

- The two middle values are **242.38** and **243.15**. The median is
  **242.76** — a number that **does not appear in the data at all**. Why is
  that not a problem? What does it mean that a median can be a value no
  donor gave?
- Now do the same to the clean list. Predict first, then check: what is the
  median without the outlier? (It should be **242.38** — barely different.)
- That is the entire lesson from the paper day in one line of output: **the mean
  went 267.40 -> 716.07, a 2.68x jump; the median went 242.38 -> 242.76, a
  change of 38 cents.** Write that contrast in your notes and say why, in
  your own words, the median is the robust one.
- The `n % 2` branch: try it on a 201-value list. Why must a median function
  handle both cases? What would happen if it did not?

## PART 3 — THE MODE (8 min)

The mode is the most common value. Here is a genuine surprise — add this below
your median lines, save, run:

```python
from collections import Counter

counts = Counter(donations)
top = counts.most_common(3)
print("three most common values:", top)

max_count = top[0][1]
print("highest frequency:", max_count)
print("how many distinct values:", len(counts))
```

In your notes:

- You should see that the most common value appears **twice** at most, and
  that nearly all 200 values are **distinct**. In real donation data, an
  exact repeating amount is rare — most people give round-ish but unique
  numbers.
- So: **does this dataset have a mode?** Be precise: `most_common` always
  returns something, but "the most common of 200 nearly-unique values" is
  not a mode in any useful sense.
- Why is that a problem for the mode as a measure of center? When would the
  mode be the *right* answer? (Think about what the mode is actually good
  at describing — a shape, not an average.)

## PART 4 — TURN THE SCRATCH INTO THE REAL FILE (12 min)

Your `centers.py` is currently three blocks of throwaway print statements. This
is where it becomes the file you turn in: the load stays on top, the three
calculations become **functions**, and the bottom of the file calls them and
prints one table.

Open the file you already have (`code centers.py`), select all of it (Ctrl+A),
and type or paste this in its place:

```python
from collections import Counter

with open("data/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]
donations = [float(line) for line in raw if not line.startswith("#")]

def mean_of(values):
    return sum(values) / len(values)

def median_of(values):
    s = sorted(values)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2

def mode_of(values):
    counts = Counter(values)
    best = counts.most_common(1)[0]
    return best if best[1] > 1 else None

clean = [d for d in donations if d < 5000]

print(f"{'set':<10}{'mean':>12}{'median':>12}")
for label, vals in (("all 200", donations), ("no outlier", clean)):
    print(f"{label:<10}{mean_of(vals):>12.2f}{median_of(vals):>12.2f}")

print("mode of all 200:", mode_of(donations))
```

Save (Ctrl+S) and run it:

```bash
python3 centers.py
```

Your output should look like — and nothing else:

```text
set               mean      median
all 200         716.07      242.76
no outlier      267.40      242.38
mode of all 200: (171.86, 2)
```

If you still see lines like `n = 200, total = ...` or
`three most common values:`, the old PART 1–3 code is still in the file. Go back
to Ctrl+A and replace the whole thing.

Spot-check with your notes, then:

- The mean fell 62.66% when one row was removed. The median moved by **38
  cents** on a value near 242. Which one describes "a donation from a
  typical donor" better?
- Your `median_of` handles both parities. Add a test at the bottom that
  calls it on a 5-value list and a 6-value list and prints both. (These are
  the two cases Unit 2's L13 taught you to spot.)

## PART 5 — WHAT EACH ONE THROWS AWAY (12 min)

No code in this part. You have the tools now; this is about what each one
*costs*. A statistic is not just a number — it is a number plus a decision about
what to ignore, and that decision can be honest or dishonest.

**Warm-up, out loud with a partner.** Three classes each raised money from
donors. Here is the **entire** record:

```text
Class A:  one gift of 900.00                -> mean 900.00, median 900.00
Class B:  ten gifts of 90.00                -> mean  90.00, median  90.00
Class C:  five gifts: 80 80 90 100 110      -> mean  92.00, median  90.00
```

- Which class raised the most? Which one is most *typical* for its donors?
- Class A has the highest mean. Is that a good thing, or a weird thing? Who
  does that one gift represent — every donor, or one?

**The dashboard problem.** A non-profit's website shows "average cost per
participant" for each program. Rooftop Garden: 12 participants, 4,800 total, and
one participant received an unusually large materials grant. Tutoring: 240
participants, 96,000 total, costs fairly even. Both programs display
"average cost per participant: 400.00".

- Two different programs, one identical headline number. What does a donor
  reading that page *believe* they are comparing? What are they actually
  comparing?

**Fill this in your notes**, with a real example in each row:

| Measure | What it answers | What it throws away |
|---|---|---|
| Mean | | |
| Median | | |
| Mode | | |

- The mean throws away the **shape** of the data — two totally different
  datasets can share a mean.
- The median throws away the **magnitudes** — it never sees how far from the
  middle anything is. (Something is very wrong in a dataset and the median
  does not move. Why is that dangerous? Come back to this in L05.)
- The mode throws away the **values** entirely — it only counts repeats.

Then: which one would you use to describe a class's test scores, and why not the
other two? One sentence you can defend, in your notes.

## PART 6 — SAVE + PUSH (6 min)

Stay inside your repo (`cd ~/compmath-u3-stats-lab`) and check the file before
you commit it:

```bash
ls centers.py        # must be here, at the top level — not inside data/
python3 centers.py   # run it once more; the table must still print
git add centers.py
git commit -m "U3 L03 day 2: mean, median, mode as functions over 200 donations"
git push
```

## TURN IN — PUSH CONFIRMATION (due 11:59 PM on Day 2)

`centers.py`, pushed, is the whole turn-in. There is nothing else to write up.

Submit the **push confirmation** — the block GitHub prints after a successful
push, ending in a line like `abc1234..def5678  main -> main` — as a screenshot
to this assignment on Google Classroom.

In the commit message or a comment, include these three numbers, which I will
spot-check against your output:

1. the mean of all 200 donations
2. the median of all 200 donations
3. the mean with the outlier removed

## LOOK AHEAD — THE U3 L05 LAB

Next we keep the center and ask a second question: not *where is the middle*,
but *how spread out is it*. You already have the reason you need to be careful —
the median does not move when something is very wrong, and sometimes very wrong
is the whole story.

Keep the terminal open — spot-checks.
