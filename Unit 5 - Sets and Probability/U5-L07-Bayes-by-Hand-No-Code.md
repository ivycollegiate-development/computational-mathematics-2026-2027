# U5 L07 — Bayes by Hand, No Code: The Hard One

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (50 minutes)
**LO:** 5.6 — derive Bayes' theorem from a tree or a table; compute a posterior
by hand and explain the base-rate trap in your own words

---

**No laptop today, and that is deliberate.** In U5 L08 you will code Bayes, and
coding it is easy. Understanding why the answer is so small — and why almost
everyone's first answer is large — is not a coding skill, and if you let Python
do it today you will not notice the mistake when it happens.

Bring a calculator. Nothing else. Everything today is arithmetic and a Venn
diagram.

## PART 1 — THE STORY (8 min)

Read it three times. It is a real shape of problem, not a contrived one.

> A disease affects **1 in 1,000** people. A test exists.
>
> - If you **have** the disease, the test comes back positive **99%** of the
>   time. *(sensitivity)*
> - If you **do not** have the disease, the test comes back positive **2%** of
>   the time. *(false positive rate — the test is 98% accurate on healthy
>   people)*
>
> Your test comes back **positive**. What is the probability you have the
>   disease?

Before you compute anything, answer in one sentence each:

- ☐  The first thought most people have, and why it is wrong: ______
- ☐  The number `99%` describes what exactly? ______
- ☐  `1 in 1,000` is not about the test. It is about ______
- ☐  Without doing any math: is the answer closer to 99%, 50%, or 5%? ______
- ☐  Why? What makes the answer small, in one sentence? ______

That last question is the entire lesson. **A very accurate test tells you almost
nothing when the thing you are testing for is rare**, because the false positives
come from a much larger pool.

## PART 2 — THE TREE, ON PAPER (14 min)

Draw the tree yourself. Left branch: 1,000 people. From there it splits again.
Fill in every number.

```
1000 people
├── have the disease ......... 1
│   ├── test + ............... 0.99 of the 1
│   └── test - ............... 0.01 of the 1
└── do not have the disease .. 999
    ├── test + ............... 0.02 of the 999
    └── test - ............... 0.98 of the 999
```

| branch | how many people |
|---|---|
| disease, test + | |
| disease, test − | |
| no disease, test + | |
| no disease, test − | |
| **total** | must be 1000 |

- ☐  Fill the table. Show each multiplication, e.g. `0.99 × 1 = ______`
- ☐  Of everyone who tested **positive**, how many are there in total? ______
- ☐  Of those, how many actually have the disease? ______
- ☐  The answer: ______ as a fraction, ______ as a decimal, ______ as a percent
- ☐  Compare that to your guess in Part 1. Off by a factor of roughly ______

## PART 3 — THE 10,000-PERSON VERSION (12 min)

The tree is the right mental model, but the fractions are small. Redo it with
**10,000 people** so the numbers are whole.

- ☐  How many have the disease? ______
- ☐  Of those, how many test positive? ______
- ☐  How many do **not** have it? ______
- ☐  Of those, how many test positive anyway? ______
- ☐  Total positive tests: ______
- ☐  **The answer, as a fraction of positives:** ______

Now write the sentence:

> Out of every 10,000 people tested, ______ test positive. Of those, ______
> actually have the disease. So a positive result means you have roughly a
> ______ % chance.

- ☐  Fill that in with your numbers.
- ☐  The false positives outnumber the true positives by a factor of about
      ______
- ☐  **This is the base-rate trap.** In one sentence, without numbers: ______
- ☐  Why is a 98%-accurate test giving a 5% answer? It sounds like a
      contradiction. Resolve it: ______

That last checkbox is worth real marks. There is no contradiction. The test is
98% accurate *per person tested*, and the two populations it is applied to are
not the same size — 10 sick against 9,990 well. **The small pool produces
almost no true positives; the large pool produces a lot of false ones.**

## PART 4 — MAKE IT WORSE, AND BETTER (10 min)

Same disease, same 1-in-1,000. Change **one number at a time** and say whether
the answer goes **up** or **down**, with a reason, *before* computing.

| change | effect on the answer | why |
|---|---|---|
| false positive rate 2% → **1%** | | |
| false positive rate 2% → **0.1%** | | |
| sensitivity 99% → **100%** | | |
| sensitivity 99% → **90%** | | |
| base rate 1/1000 → **1/100** | | |
| base rate 1/1000 → **1/10,000** | | |

- ☐  Which of those six does the most to improve the answer? ______
- ☐  Which does the least? ______ Why is that the interesting one: ______
- ☐  If the test is a medical decision, which error is worse — a false positive
      or a false negative? Does your answer change if the disease is fatal and
      the treatment is a 5% survival of complications? ______

- ☐  **Now compute the 1% false-positive version on paper.** 10,000 people, 10
      sick, all 10 test positive, 9,990 well of whom 1% test positive.
      Answer: ______

There is a version of this where the test is **perfect**: 100% sensitivity, 0%
false positives. The answer is then 100%. Which single input did all the work
there, and what does that tell you about what "good enough" means for a test?
______

## PART 5 — WRITE THE FORMULA FROM MEMORY (6 min)

Closed notes. Write, from memory, in your own hand:

```
P(A|B) = ____________________
```

- ☐  Now write it a second time with every symbol named in words beside it.
- ☐  What are the two terms in the denominator, in plain English? ______
- ☐  A colleague of mine wrote last term "everyone who tests positive." Is that
      right? What is the denominator actually counting? ______

That last one is the single most common misreading of the theorem. The
denominator is **not** everyone who tested positive. It is everyone for whom
*this* test could have come back positive — the true positives and the false
positives, not true positives and true negatives. That is why it is a smaller
number than the whole tested population, and it is why the fraction comes out
larger than the numerator alone.

## TURN IN — Bayes on Paper

1. The tree and the four-branch table (Part 2), arithmetic shown
2. The 10,000-person version (Part 3) with your filled-in sentence
3. The six-row effect table (Part 4), with the 1%-false-positive computation done
4. Bayes' formula written twice from memory, with symbols named
5. **The base-rate trap in your own words, one paragraph, no numbers.** This is
   the highest-value item on the page.

**Closed book. No notes, no laptop.** A copied formula is a zero on item 4; a
formula you derived and can explain is the whole point of the lesson.

## 📋 PREVIEW OF TOMORROW

**Next:** L06's file, L08, Feb 26 — back to the machine. You will code
`bayes()` in four lines, watch it reproduce today's 4.72% exactly, and then run
it across a sweep of false-positive rates to see the shape of the curve. The
code is easy. The thing worth your attention is how little it changes your
intuition.

**Bring tomorrow:** laptop, today's tree redrawn if you want to compare.

## 🇹🇼 TAIWAN CONTEXT

The base-rate trap is not a medical curiosity, it is the single most exploited
weakness in security alerting. A detection rule with a 1% false-positive rate
against a 1-in-1,000 event rate produces mostly noise, and an analyst who reads
"99% accurate" in the vendor's documentation and stops there has been told
exactly what they need to hear by someone who benefits from the belief. The ROC
national CERT's advisories on intrusion detection repeatedly land on the same
instruction: measure the *positive predictive value* — the rate of true events
among alerts — not the detection rate, because the detection rate is the number
that looks good and the predictive value is the number that tells you whether
your alert volume is worth an analyst's hour.

The phishing example is the one to sit with. A "99.9% accurate" spam filter
means almost nothing about your incoming mail, because almost none of it is
phishing. The math today is the reason a well-meaning administrator can install
a technically excellent filter, watch the alert count fall, and conclude the
network is safer — while the actual click-through rate on the alerts that remain
has gone *up*, because the filter is now selecting for the attacks that look
unlike the ones it was trained to catch. The number that tells you this is a
conditional, and the conditional is what you computed on paper today.
