# U3 L25 — Return From Winter Break: Does Your Pencil Match Your Code?

**LO:** check your hand-computed statistics against code, and be honest about
which Unit 3 ideas you actually own.

Sixteen days off. This first period is a **return day, not a launch** — we are
not learning anything new. Two jobs: find out whether your break work was right,
and find out where the gaps are before the midterm.

**The break assignment was due Sunday Jan 3.** It does not matter that it is
now past due — bring your pages. We work with them today so you can fix anything
wrong *before* it is graded.

## PART 1 — PULL THE REPO (10 min)

```bash
pwd
cd ~/compmath-u3-stats-lab
git pull
python3 statslib.py
ls data/
```

- If your clone lives somewhere else, `cd ~` first and check with `ls`.
- **If `statslib.py` runs and prints `all tests passed`**, good. If any test
  still fails from Dec 17, do not delete it — fix it today, and note what the
  bug was.

## PART 2 — DOES PYTHON AGREE WITH YOUR PENCIL? (20 min)

Put your hand-computed page next to the keyboard. Type your 21 values into
Python **exactly as you wrote them** — do not tidy them up first.

```python
values = [ ... ]          # your 21 numbers, in the order you collected them

values_sorted = sorted(values)
n = len(values)
mean = sum(values) / n
median = (values_sorted[n // 2] if n % 2
          else (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2)
print("n      =", n)
print("mean   = %.2f" % mean)
print("median = %.2f" % median)
print("min    =", min(values), " max =", max(values))
print("range  =", max(values) - min(values))
```

Now the five-number summary, using **your** convention from L08 — `k = (n - 1) x
p`, interpolated:

```python
def percentile(v, p):
    s = sorted(v)
    k = (len(s) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(s) - 1)
    return s[lo] + (k - lo) * (s[hi] - s[lo])

f = [min(values), percentile(values, 0.25), median,
     percentile(values, 0.75), max(values)]
iqr = f[3] - f[1]
lo_f, hi_f = f[1] - 1.5 * iqr, f[3] + 1.5 * iqr
out = [v for v in values if v < lo_f or v > hi_f]
print("five-number:", f)
print("fences: (%.2f, %.2f)  outliers: %s" % (lo_f, hi_f, out))
```

### Record every disagreement

| quantity | my paper | Python | agree? | if not, where did I go wrong |
|---|---|---|---|---|
| n | | | | |
| mean | | | | |
| median | | | | |
| min / max | | | | |
| range | | | | |
| q1 | | | | |
| q3 | | | | |
| IQR | | | | |
| outliers | | | | |

**Write down which column was wrong — yours or Python's.** That word is the
graded part of today. Almost always it is you, and almost always it is the sort
or the `k`. But "Python disagreed with me" is not an answer; "Python disagreed
with me because I interpolated q1 when k landed exactly on an index" is.

## PART 3 — THE UNIT 3 POST-MORTEM (20 min, in writing)

In your notebook, one line each. No discussion with your partner, no group
chat — this one is yours, because a group answer is a negotiated answer.

- The one Unit 3 concept I can explain to someone else without notes: ______
- The one I could do again *right now*, cold, without looking: ______
- The one I have been **faking**: ______
- The one I still cannot tell apart from its neighbour: ______
- If my `statslib.py` had to ship and I could not fix it, which one function
  would scare me least to leave broken, and which one would scare me most: ______

**The last line is the interesting one.** A person who knows which part of
their own code is fragile is further along than a person whose project got full
marks.

## PART 4 — OUTLIERS, ONE MORE TIME (15 min)

The break data gave you outliers. Now the uncomfortable question, from L21:

For **each** outlier you found, write one of these two labels and a half-sentence
of justification:

- **KEEP** — a real observation that happens to be extreme
- **DROP** — a measurement or transcription error

Then, separately:

- If you drop it, which of your five numbers move, and by how much: ______
- Which of your five numbers **do not move at all**: ______

**That second blank is the one to get right.** The median of a 21-value list
barely notices one removed value; the mean moves immediately. If you can see
that here, with your own data, you have understood more than the paper check on
Dec 16 asked for.

## PART 5 — PREVIEW: WHAT UNIT 4 IS (10 min)

Unit 4 is **Algebra and SymPy** — the same math you already know, handed to a
computer that does the bookkeeping.

- SymPy solves `2x + 5 = 17` symbolically and tells you *how* it got `x = 6`.
- It factors, expands, and simplifies expressions that you would not want to do
  by hand.
- It handles modular arithmetic, which is the arithmetic underneath hashes and
  ciphers.

No prep over the break is required, and there is no break assignment for Unit 4.
One curiosity, if you want it: think about what it means to ask a computer for
*every* solution to an equation, rather than one solution. Bring that thought
Jan 5.

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. A photo of your **Part 2 table**, filled in, with the words *mine* or
   *Python's* marked on every disagreement
2. One paragraph: what your break data taught you about your own week that the
   mean alone would have hidden
3. Your **Part 3 post-mortem**, in your own handwriting or your own words. It is
   not collected if you write something you think I want to read.

**Part 3 is ungraded for correctness and graded for honesty.** Writing "the one I
have been faking is percentiles" costs nothing and tells you exactly what to
review before the midterm. Writing "I understood everything" tells me nothing.

Keep your break pages — they are the study sheet for the Unit 3 midterm review.
