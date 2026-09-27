# U5 L07 — Bayes by Hand, No Code: The Hard One

Names: ___________________________  Date: Feb 25

Closed book. Bring a calculator and nothing else. 50 minutes. The point of today is understanding why the answer is so small, and that is not a coding skill.

## 1: The story — A disease affects 1 in 1,000 people

A test comes back positive 99% of the time if you have the disease (sensitivity), and 2% of the time if you do not (false-positive rate; the test is 98% accurate on healthy people). Your test is positive.

☐  The first thought most people have, and why it is wrong: ______________

☐  The number `99%` describes what exactly: ______________

☐  `1 in 1,000` is not about the test. It is about ______________

☐  With no math: is the answer closer to 99%, 50%, or 5%? ______________

☐  What makes the answer small, in one sentence: ______________

## 2: The tree, on paper — 1,000 people

Draw the tree yourself, then fill the table. Show each multiplication.

| branch                 | how many people     |
| ---------------------- | ------------------- |
| disease, test +        | ______________      |
| disease, test −        | ______________      |
| no disease, test +     | ______________      |
| no disease, test −     | ______________      |
| **total**              | ______________      |

☐  Of everyone who tested positive, how many in total: ______________

☐  Of those, how many actually have the disease: ______________

☐  The answer as a fraction ______________, as a decimal ______________, as a percent ______________

☐  Off from your Part 1 guess by a factor of roughly ______________

## 3: The 10,000-person version — Whole numbers

☐  How many have the disease: ______________

☐  Of those, how many test positive: ______________

☐  How many do not have it: ______________

☐  Of those, how many test positive anyway: ______________

☐  Total positive tests: ______________

☐  The answer, as a fraction of positives: ______________

Now write the sentence.

> Out of every 10,000 people tested, ______________ test positive. Of those, ______________ actually have the disease. So a positive result means you have roughly a ______________ % chance.

☐  The false positives outnumber the true positives by a factor of about ______________

☐  The base-rate trap, in one sentence and without numbers: ______________

☐  Why is a 98%-accurate test giving a 5% answer? Resolve the apparent contradiction: ______________

## 4: Make it worse, and better — Predict before computing

Same disease, same 1-in-1,000. Change one number at a time.

| change                                | effect on the answer (up/down)     | why                |
| ------------------------------------- | ---------------------------------- | ------------------ |
| false positive rate 2% → **1%**       | ______________                     | ______________     |
| false positive rate 2% → **0.1%**     | ______________                     | ______________     |
| sensitivity 99% → **100%**            | ______________                     | ______________     |
| sensitivity 99% → **90%**             | ______________                     | ______________     |
| base rate 1/1000 → **1/100**          | ______________                     | ______________     |
| base rate 1/1000 → **1/10,000**       | ______________                     | ______________     |

☐  Which of the six does the most to improve the answer: ______________

☐  Which does the least, and why is that the interesting one: ______________

☐  If the test is a medical decision, which error is worse, and does your answer change if the disease is fatal and the treatment carries a 5% survival rate: ______________

☐  Compute the 1% false-positive version on paper: 10,000 people, 10 sick, all 10 test positive, 9,990 well of whom 1% test positive. Answer: ______________

☐  A perfect test — 100% sensitivity, 0% false positives — gives 100%. Which single input did all the work, and what does that say about what "good enough" means for a test: ______________

## 5: Write the formula from memory — Twice

```
P(A|B) = ____________________
```

☐  Write it a second time with every symbol named in words beside it: ______________

☐  The two terms in the denominator, in plain English: ______________

☐  A colleague wrote the last term as "everyone who tests positive." Is that right, and what is the denominator actually counting: ______________

**TURN IN** — The tree and four-branch table with the arithmetic shown, the 10,000-person version with the filled sentence, the six-row effect table with the 1% false-positive computation done, Bayes' formula written twice from memory with symbols named, and the base-rate trap in one paragraph with no numbers. A copied formula is a zero on item 4.
