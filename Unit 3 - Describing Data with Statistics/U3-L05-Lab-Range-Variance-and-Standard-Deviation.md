# U3 L05 — Lab: Range, Variance, and Standard Deviation

**LO:** compute measures of spread in Python and explain why spread sometimes matters more than the center.

You have the center. Today you get the second half of a description: not
*where is the middle* but *how far from the middle do the values sit*. A mean
of 242 with a standard deviation of 5 is a very different world from a mean
of 242 with a standard deviation of 500. Same center, different data.

As with L03, no `statistics` library — you write the formulas.

## PART 0 — SET UP (5 min)

```bash
cd ~/compmath-lab
pwd
```

```python
with open("/tmp/u3_datasets/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

donations = [float(line) for line in raw if not line.startswith("#")]
clean = [d for d in donations if d < 5000]
print(len(donations), len(clean))
```

## PART 1 — RANGE: THE CHEAPEST SPREAD MEASURE (5 min)

```python
r_all = max(donations) - min(donations)
r_clean = max(clean) - min(clean)
print(f"range with outlier: {r_all:.2f}")
print(f"range clean:        {r_clean:.2f}")
print(f"ratio: {r_all / r_clean:.1f}x")
```

In your notes:

- The range went up **121x** — the most extreme distortion of anything we
  have computed. Compare: mean 2.68x, median 1.00x, range 121x.
- Why is the range the *worst* possible spread measure? (Hint: it only looks
  at two values and ignores the other 198.)
- Two datasets can have the same range and be wildly different. Describe
  such a pair.

## PART 2 — VARIANCE: SQUARED DEVIATIONS (15 min)

Variance asks: on average, how far is a value from the mean? The steps
matter, so do them by hand first on the six clean paper-day numbers
`25 40 50 60 75 100`:

- mean = **58.33**
- subtract it from each, getting **−33.33, −18.33, −8.33, 1.67, 16.67, 41.67**
- square each one: **1111.11, 336.11, 69.44, 2.78, 277.78, 1736.11**
- add them: **3533.33**
- divide by 6: **588.89** — that is the **population variance**

Notice every deviation is now positive — squaring is what lets average
"distance" mean anything. Now the code:

```python
def variance_of(values):
    m = sum(values) / len(values)
    total = sum((v - m) ** 2 for v in values)
    return total / len(values)

print(f"variance clean: {variance_of(clean):.2f}")
print(f"variance all:   {variance_of(donations):.2f}")
```

- Does the clean number match your 588.89? It will not — 588.89 was for
  those six *paper* numbers, while this is all 199 real ones. Do not panic;
  check the method on the paper set to be sure your function is right:

```python
print(f"paper set variance: {variance_of([25, 40, 50, 60, 75, 100]):.2f}")   # 588.89
```

- The full data's variance is **2,734x** the clean variance. Explain that
  ratio in your own words. Why does variance distort *more* than the standard
  deviation will? (Hint: squaring a huge number.)

## PART 3 — STANDARD DEVIATION: UN-SQUARING (10 min)

Variance is in **dollars squared**, which nobody can picture. The standard
deviation is the square root, which puts it back in dollars:

```python
def stdev_of(values):
    return variance_of(values) ** 0.5

sd_clean = stdev_of(clean)
sd_all = stdev_of(donations)
print(f"stdev clean: {sd_clean:.2f}")
print(f"stdev all:   {sd_all:.2f}")
print(f"ratio: {sd_all / sd_clean:.2f}x")
```

In your notes:

- The standard deviation grew **52x**, while the variance grew **2,734x**.
  Explain the gap between those two ratios. (Same underlying fact — the
  outlier — but squaring exaggerates. This is why we report the standard
  deviation to people and keep the variance for algebra.)
- **Use the standard deviation as a ruler.** Clean data: mean 267.40, sd
  121.05. So a typical donation sits within about 121 of 267, i.e. roughly
  146 to 388. Check that with the data: how many of the 199 clean values fall
  outside 267.40 ± 121.05? Write the count down. (The **empirical rule**
  predicts roughly 68% for a normal, symmetric distribution. Our donations
  are right-skewed, so the real answer is about **73%** — more clustered
  than a normal curve. The rule is a guide, not a guarantee, and this is the
  first case where you can see it fail.)

```python
low, high = 267.40 - 121.05, 267.40 + 121.05
inside = sum(1 for d in clean if low <= d <= high)
print(f"{inside}/{len(clean)} = {100*inside/len(clean):.0f}% within one sd")
# You should see 146/199 = 73%. Compare with the empirical rule's 68%.
```

- With the outlier included, the "typical donation" is 716.07 ± 6330.32.
  Read that aloud to yourself. What has happened to the meaning of the
  number?

## PART 4 — SIDE-BY-SIDE: THE FULL DESCRIPTION (10 min)

Write `spread.py` and run it:

```python
def mean_of(v):
    return sum(v) / len(v)

def median_of(v):
    s = sorted(v)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

def variance_of(v):
    m = mean_of(v)
    return sum((x - m) ** 2 for x in v) / len(v)

def stdev_of(v):
    return variance_of(v) ** 0.5

clean = [d for d in donations if d < 5000]

print(f"{'set':<12}{'mean':>10}{'median':>10}{'range':>12}{'stdev':>12}")
for label, vals in (("all 200", donations), ("clean 199", clean)):
    print(f"{label:<12}{mean_of(vals):>10.2f}{median_of(vals):>10.2f}"
          f"{max(vals)-min(vals):>12.2f}{stdev_of(vals):>12.2f}")
```

Expected output:

```text
set             mean    median       range      stdev
all 200        716.07     242.76    89928.67    6330.32
clean 199      267.40     242.38      742.56     121.05
```

Answer in your notes:

- Two of these four columns are *robust* and two are not. Which two, and
  what makes a column robust?
- If you could only show a donor **one** extra number beside the mean, which
  column, and why is it *not* the range?

## PART 5 — WHY SPREAD BEATS THE CENTER SOMETIMES (10 min)

- A class has mean score 80 with sd 3. Another has mean 80 with sd 15. Two
  students are absent; can you predict who scores what in the second class?
  Why is the second class's *mean* a worse description of a typical student?
- Machine learning models are often reported as "mean absolute error." What
  does a huge outlier do to that average, and what alternative would you
  report alongside it?
- Return to the median's blind spot from the paper day: if the median cannot
  see an extreme value, which of today's four measures *can* see it? (Hint:
  the median's blind spot is the standard deviation's specialty.)

## PART 6 — LOOK AHEAD: THE U3 L06 LAB

Next lesson you use all of this to make a real decision: given a claim like
"wage group A earns more than wage group B," you will choose which
statistics support it and which would let you mislead an audience on purpose.
You now have every tool that decision needs.

## PART 7 — SAVE + PUSH (last 10 min)

```bash
git add spread.py
git commit -m "U3 L05 range, variance, and standard deviation over donations"
git push
```

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

Your `spread.py`, pushed above, is the turn-in. Submit the **push
confirmation line** as a screenshot to this assignment on Google Classroom.

Include these four numbers in the push message so I can spot-check:

1. mean of all 200 donations
2. standard deviation of all 200 donations
3. standard deviation with the outlier removed
4. the percentage of clean values within one standard deviation of the mean

Keep the terminal open — spot-checks.
