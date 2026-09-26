# U3 L03 — Lab: Mean, Median, and Mode in Plain Python

**LO:** compute mean, median, and mode from a real dataset in Python, and state which one is robust and why.

You predicted on the paper day and you did the arithmetic by hand on seven
numbers. Today you do it in code, on all 200 real donations, and you check
whether the seven-number story held up.

No `statistics` library and no pandas. You write all three yourself — the
point is to know what the code is doing when a real library does it for you.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

Load the donations. This is the same shape as Unit 2: comment line, then
values.

```python
with open("/tmp/u3_datasets/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

donations = [float(line) for line in raw if not line.startswith("#")]
print(len(donations), "values")
```

Keep `donations` loaded. Everything today builds on it.

## PART 1 — THE MEAN (10 min)

The mean is the sum divided by the count. The trap is dividing by the wrong
count. Build it:

```python
n = len(donations)
total = sum(donations)
mean = total / n

print(f"n = {n}, total = {total:.2f}")
print(f"mean = {mean:.2f}")
```

In your notes:

- What did you get? Compare to yesterday's paper: the mean of the seven
  numbers with the outlier was 1335.71. Why is this one so much smaller?
  (How many numbers are being averaged here?)
- The donor file's comment said one entry is a mis-key. Try the mean without
  it, without deleting anything permanently:

```python
clean = [d for d in donations if d < 5000]
print(f"mean with    outlier: {sum(donations)/len(donations):.2f}")
print(f"mean without outlier: {sum(clean)/len(clean):.2f}")
```

- The answer should be **267.40** without the outlier. How many times bigger
  is the mean *with* it? Why does **one** value out of 200 move the mean so
  much at all? (Think about what the mean is: a sum with a division at the
  end. The outlier is enormous inside that sum, and the division only
  divides by 200.)

## PART 2 — THE MEDIAN (15 min)

The median is the middle value **after sorting**. It is built from position,
so its size does not depend on how big the numbers are.

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
- That is the entire lesson from yesterday in one line of output: **the mean
  went 267.40 -> 716.07, a 2.68x jump; the median went 242.38 -> 242.76, a
  change of 38 cents.** Write that contrast in your notes and say why, in
  your own words, the median is the robust one.
- The `n % 2` branch: try it on a 201-value list. Why must a median function
  handle both cases? What would happen if it did not?

## PART 3 — THE MODE (10 min)

The mode is the most common value. Here is a genuine surprise:

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

## PART 4 — ALL THREE, ONE TABLE (10 min)

Put it together. Write this into a file called `centers.py` and run it:

```python
from collections import Counter

with open("/tmp/u3_datasets/u3_donations.txt") as f:
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

Your output should look like:

```text
set             mean      median
all 200        716.07      242.76
no outlier     267.40      242.38
```

Spot-check with your table, then answer in your notes:

- The mean fell 62.66% when one row was removed. The median moved by **38
  cents** on a value near 242. Which one describes "a donation from a
  typical donor" better?
- Your `median_of` handles both parities. Add a test at the bottom that
  calls it on a 5-value list and a 6-value list and prints both. (These are
  the two cases Unit 2's L13 taught you to spot.)

## PART 5 — WHERE EACH ONE LIES (10 min)

Every one of these three is a *choice* someone made, and each choice throws
something away. Fill this in your notes with a real example each:

| Measure | What it answers | What it throws away |
|---|---|---|
| Mean | | |
| Median | | |
| Mode | | |

- The mean throws away the **shape** of the data — two totally different
  datasets can share a mean.
- The median throws away the **magnitudes** — it never sees how far from the
  middle anything is. (Something is very wrong in a dataset and the median
  does not move. What is that dangerous? Come back to this in L05.)
- The mode throws away the **values** entirely — it only counts repeats.

Which one would you use to describe a class's test scores, and why not the
other two?

## PART 6 — LOOK AHEAD: THE U2 L05 LAB

Tomorrow we keep the center and ask a second question: not *where is the
middle*, but *how spread out is it*. You already have the reason you need
careful — the median does not move when something is very wrong, and
sometimes very wrong is the whole story.

## PART 7 — SAVE + PUSH (last 10 min)

```bash
git add centers.py
git commit -m "U3 L03 mean, median, mode functions over 200 donations"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `centers.py`, pushed above, is the turn-in. Submit the **push
confirmation line** — the URL GitHub prints after a successful push — as a
screenshot to this assignment on Google Classroom.

In the push message or a comment, include these three numbers, which I will
spot-check against your output:

1. the mean of all 200 donations
2. the median of all 200 donations
3. the mean with the outlier removed

Keep the terminal open — spot-checks.
