# U7 L01 — Unit Launch: From Measuring Shapes to Predicting Them

**Date:** Monday, May 3, 2027
**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.1 — distinguish a measured quantity from a modelled one, and explain
why a model needs a stated failure condition

---

**No laptop today.** Pencil. Last Friday you finished a unit about measuring
shapes that exist. This unit is about **inventing curves for data that exists
and then trusting them with predictions.** It is a different kind of danger.

## PART 1 — WHAT CHANGED (10 min)

Unit 6: you measured. Given a shape, you computed a dimension. The answer was a
property of the thing, and when the method was wrong the answer was wrong in a
way you could trace.

Unit 7: you **fit**. You choose a family of curves, you pick the member of that
family that comes closest to the data, and then you use it to say what happens
*next*. Three things now live where one thing lived:

1. The **data** — the only part that came from the world
2. The **model** — a function you chose, and it is a decision
3. The **prediction** — what you claim about data you have not seen

- ☐  Which of the three can be wrong without any human error? ______
- ☐  Which one is a *choice*? ______
- ☐  In Unit 6, when `measure()` returned the wrong dimension, who was at
     fault? Write the answer in the form "the ______ was wrong": ______

The intended answer to the last one is "the method". Unit 7's answer will be
"the model, and we chose it". That is a genuinely different failure and you
should notice the difference before it happens to you.

## PART 2 — THREE NUMBERS, THREE CLAIMS (15 min)

Here are three ways of stating a number about the same data. Fill in what each
one is *claiming*.

| statement | the claim it makes | what it hides |
|---|---|---|
| "regression slope = 0.6" | | |
| "the relationship is linear" | | |
| "next week will be 63" | | |

- ☐  Write a fourth statement about the same data, one level further along:
     ______
- ☐  Which of the four would you put in a report? ______
- ☐  Which of the four would you put in a *forecast email to a manager*?
     ______
- ☐  What is the difference between those two answers? ______

The gap between the second and the third row is the gap this unit is about. "The
relationship is linear" is a statement about the data. "Next week will be 63" is
a statement about the future, and it is only licensed if the second is true
*and stays true*. Nothing guarantees that.

## PART 3 — THE FAILURE CONDITION (12 min)

Every model should ship with the condition under which it is not to be trusted.
Read these four model statements and write the missing failure condition.

1. "A line fits these 40 points."
   → Not valid when: ______________________________________
2. "A quadratic fits these 40 points."
   → Not valid when: ______________________________________
3. "This line will continue to predict next month's value."
   → Not valid when: ______________________________________
4. "The detector flags a value beyond 3 standard deviations."
   → Not valid when: ______________________________________

Number 4 is the one you have already met twice — the solid circle scoring 1.79,
and the anomaly detector firing on ordinary days. The general rule:

> A threshold or a model is only as trustworthy as the **assumptions** you
> measured it under.

- ☐  In your own words, why does a 3-sigma threshold need a failure condition?
     ______
- ☐  Give one failure condition for a linear fit on network throughput over
     time. ______

## PART 4 — THE UNIT'S PROMISE (8 min)

Five topics, and each one is a different way of being wrong:

| # | topic | how it fails |
|---|---|---|
| 1 | numerical differentiation | the step size trades truncation against round-off |
| 2 | numerical integration | a smooth average can hide a spike |
| 3 | least-squares fitting | a line can fit and still be the wrong shape |
| 4 | residuals | they tell you the fit is wrong in a *structured* way |
| 5 | modelling and prediction | it fails on the same day you declare victory |

- ☐  Which of those five do you expect to be the hardest? ______
- ☐  Which do you expect to be most useful outside class? ______
- ☐  **Write down the answer to the first question. Check it in five weeks.**
     ______

## 🇹🇼 TAIWAN CONTEXT

Unit 6 ended with a warning: a model calibrated on a pattern that does not occur
in the wild produces confident nonsense. That is not a lesson, it is a weekly
event in operational forecasting, and Taiwan is no exception.

The concrete shape of it: diurnal and weekly traffic rhythms are strong and
completely normal. A trend model fitted to a window that happens to contain one
weekday peak will report a steep rise and predict it continuing. A linear fit
across a month of traffic data that ignores the weekly cycle is not slightly
wrong — it is confidently, systematically wrong, and the direction of the error
depends on where in the week the window starts. The one-day-ahead forecast for
Monday morning will be badly off in a way that looks like a model failure and
is actually a **specification** failure: the model had no room for a weekly
term.

That is the error class this entire unit is built to prevent, and the reason
residuals — which you meet on Thursday — are the most important thing in the
course. Residuals are how you notice you left a term out.

**Next:** L02, Tue May 4 — paper check and the arithmetic of a difference
quotient, by hand, until the shape of the thing is obvious. Then Wednesday we
make the computer do it.
