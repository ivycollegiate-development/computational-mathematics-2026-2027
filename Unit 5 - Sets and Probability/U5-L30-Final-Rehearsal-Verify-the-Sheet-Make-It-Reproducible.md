# U5 L30 — Final Rehearsal: Verify the Sheet, Then Make It Reproducible

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (final rehearsal, 45 minutes)
**LO:** 5.1–5.10 — verify hand-worked results against executable code; produce a
reproducible repository as the unit's final artefact

---

## TODAY'S PURPOSE

Two jobs, and the second is the one that counts.

**Job 1: check your one-page sheet.** Every formula on it, run. If a hand result
disagrees with the code, one of them is wrong and you need to find out which
before the test, not during it.

**Job 2: make the repository clonable.** A stranger must be able to clone it,
read the README, run one command, and understand the result without you in the
room. Today is the working session for that.

## PART 1 — VERIFY THE SHEET (15 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def at_least_one(ls):
    if not ls:
        return F(0)
    p = ls[0]
    for q in ls[1:]:
        p = p + q - p * q
    return p

print("two sets:  5+4-2 =", 5 + 4 - 2)
print("three sets: 5+4+3-2-1-1+1 =", 5+4+3-2-1-1+1)
print("1/2 + 1/2 =", F(1,2) + F(1,2))
print("exactly one of two independent halves:", F(1,2) + F(1,2) - 2*(F(1,2)*F(1,2)))
print("bayes: 1/1000 * 99/100 =", F(1,1000) * F(99,100))
print("posterior:", F(1,1000)*F(99,100) / (F(1,1000)*F(99,100) + F(999,1000)*F(1,50)))
print("EV: (1/2)*3000 + (1/2)*(-1000) =", F(1,2)*3000 + F(1,2)*(-1000))
print("variance: (1/2)*2000^2 + (1/2)*2000^2 =", F(1,2)*2000**2 + F(1,2)*2000**2)
```

Real output:

```
two sets:  5+4-2 = 7
three sets: 5+4+3-2-1-1+1 = 9
1/2 + 1/2 = 1
exactly one of two independent halves: 1/2
bayes: 1/1000 * 99/100 = 99/100000
posterior: 11/233
EV: (1/2)*3000 + (1/2)*(-1000) = 1000
variance: (1/2)*2000^2 + (1/2)*2000^2 = 4000000
```

- ☐  `1/2 + 1/2 = 1` and `exactly one of two halves = 1/2`. Both correct. **Which
      one is the answer to "what is the probability that exactly one of two
      independent fair coins comes up heads", and why do the two look similar in
      the formula:** ______
- ☐  The `posterior: 11/233` from L08. Is that the answer you have written on
      your sheet, and is it in the form your test wants: ______
- ☐  **Now the important part:** run every one of your own sheet's answers. Did
      anything disagree with your hand work? List the disagreements: ______
- ☐  For each disagreement, was the hand work wrong or the code wrong, and how
      did you tell: ______

That last pair is the actual skill. When a hand result and a program disagree,
the instinct is to change whichever is easier to change, and that instinct has
cost more bugs than any other. **The method is to find the smallest input that
reproduces the disagreement** — reduce until the two results differ, and the
difference will be a case you can reason about directly rather than a mystery
you have to argue about abstractly.

## PART 2 — THE THREE NUMBERS THAT MATTER (10 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def at_least_one(ls):
    if not ls:
        return F(0)
    p = ls[0]
    for q in ls[1:]:
        p = p + q - p * q
    return p

print("P(1 or 2) - naive sum =", (F(3,20) + F(2,10)) - at_least_one([F(3,20), F(2,10)]))
print("times 12000 =", ((F(3,20) + F(2,10)) - at_least_one([F(3,20), F(2,10)])) * 12000)
print("P(file-server) =", at_least_one([F(3,20), F(2,10)]), " naive sum =", F(3,20)+F(2,10))
print()
print("naive ratio   (96/120)/(56/280) =", (F(96,120)) / (F(56,280)))
print("exposed ratio (68/80)/(28/200)  =", (F(68,80)) / (F(28,200)))
print("clean ratio   (28/40)/(28/80)   =", (F(28,40)) / (F(28,80)))
print("overstatement factor 4.00 / 2.00 =",
      (F(96,120))/(F(56,280)) / ((F(28,40))/(F(28,80))))
```

Real output:

```
P(1 or 2) - naive sum = 3/100
times 12000 = 360
P(file-server) = 8/25  naive sum = 7/20

naive ratio   (96/120)/(56/280) = 4
exposed ratio (68/80)/(28/200)  = 85/14
clean ratio   (28/40)/(28/80)   = 2
overstatement factor 4.00 / 2.00 = 2
```

Three results that each close a thread from earlier in the unit.

**`3/100`, and `3/100 × 12000 = 360`.** The exact shared-exposure credit from
L24. The entire L20 bug, quantified in one line, in a form you can write in an
exam.

**`8/25` against a naive `7/20`.** The correct probability versus the naive sum,
and the difference `3/100` is the same `3/100` as the line above — because it is
the same event counted twice. **The overcount is the same number whether you
express it as money or as probability**, which is the cleanest statement of
Idea 1 you will ever write.

**`4`, `85/14`, `2`.** L28's three ratios, exact. The naive figure is exactly 4,
the clean-stratum figure exactly 2, and the exposed stratum `85/14 ≈ 6.07` —
*larger* than the naive one. If you have time for one calculation in the test,
make it this one: it demonstrates stratification, it produces three different
answers from one dataset, and it is the one that shows you understand that a
confounder changes the *size* of an effect rather than its existence.

- ☐  Confirm `85/14` by hand: ______
- ☐  Why is the exposed-stratum ratio **larger** than the naive ratio? One
      sentence: ______

## PART 3 — MAKE IT REPRODUCIBLE (15 min)

The repository, final form.

- ☐  **`README.md`, first screen only.** A stranger reads the first ten lines
      before reading anything else. They must learn: what this is, what it
      models, who for, and how to run it. Write it and then **delete the first
      line of the file** and check it still works as a first screen
- ☐  **One command, from a clean checkout.** `python3 riskkit.py` must produce
      the manifest and nothing else surprising. **Test this by actually doing
      it** — clone or copy to a fresh directory and run it there, not in your
      working copy where you know what to expect
- ☐  **No absolute paths.** No `/Users/pauljonessr/...` anywhere in the
      repository. Search for it and confirm: ______
- ☐  **The seed is in the code, not in a comment.** A reader who changes it must
      not break anything
- ☐  **The tests run with one command too**, and their output is in the README
- ☐  Every output block in the README is **live output you pasted**, not
      reconstructed from memory. Check each one by re-running: ______

That last item is the whole project in one line, and it is worth being pedantic
about. Every false number this unit has produced came from someone writing what
the output *should* look like rather than what it *does* look like. The manifest
on L26 caught a spacing error that I had typed by hand; the `0.00149` I wrote
when the program printed `0.00148`; the L24 table that had the wrong column
widths. **Every one of those would have shipped, and every one would have been
caught by re-running.** If the repository contains a number that no run
produced, it is wrong, and no amount of care elsewhere in the project compensates
for it.

- ☐  Re-run every code block in your README, top to bottom, in a fresh
      directory. Any that fail or need editing: ______
- ☐  **The test that kills `v1`** is in the suite and passes against the current
      code. Run the suite and paste the real output
- ☐  `git status` is clean apart from your intended files, and **you have not
      committed** — I want to review before it goes in

## PART 4 — THE THIRD ARTEFACT (5 min)

You have the L27 critique and the L28 correction. Both are graded. Add the
third:

- ☐  **A single page: "What this model does not know."** Not a disclaimer — a
      list, with each item saying what evidence would resolve it. This is the
      document you would hand to the person who inherits the model, and it is
      the one nobody writes.

## TURN IN — Final Rehearsal

1. The Part 1 and Part 2 outputs, run live
2. Your one-page sheet, with the disagreements from Part 1 marked
3. **The repository**, verified from a clean directory
4. **`README.md`** with live output throughout
5. **"What this model does not know"**, one page
6. **Not committed.** Bring it to me.

## 📋 PREVIEW OF TOMORROW

**Next and last:** L31, Mar 31 — **paper, 50 minutes, and we close the
unit.** A final assessment, the two written artefacts returned with comments, and
the demonstration. Bring the repository and be ready to run it in front of
someone who has not seen it.

## 🇹🇼 TAIWAN CONTEXT

Part 3's clean-directory test is the reproducibility requirement, and it has a
direct institutional counterpart that this unit has been circling for a month.
The ROC national CERT's incident reporting and the Ministry of Digital
Affiliatives' framework for smaller organisations both depend on a figure being
**re-derivable by a third party from what was submitted** — which is the same
demand as a stranger cloning your repository and reproducing your manifest from
the seed in it.

This is not bureaucratic. The two failure modes it prevents are the two that
actually cause harm in this domain. **A result that cannot be re-derived is
indistinguishable from a result that was adjusted until it agreed with a
decision already taken**, and there is no way for a reader to tell the difference
except by re-deriving it. And a likelihood that cannot be traced to a named
calibration population cannot be compared against the sector figure that would
have been the better input — so the reader has no basis on which to challenge
it, which means the model's most fragile input is also the one no reviewer will
examine.

The `CALIBRATION` block you added on L26 is therefore not an extra field. It is
the part of the manifest that makes the other parts auditable, and the
clean-directory test in Part 3 is the part of the project that proves it. The
national CERT's practice in post-incident review is to require that every
quantitative claim in a report be re-computable from the supplied data by a
reviewer who was not present for the analysis — not because the analysts are
suspected of anything, but because the alternative is that the figure is
accepted on the authority of the person who produced it, and that is precisely
the standard the framework exists to move away from.
