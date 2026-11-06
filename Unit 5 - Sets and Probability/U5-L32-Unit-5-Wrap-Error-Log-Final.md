# U5 L32 — Unit 5 Wrap: Error Log Final & Reflection Principle (PAPER)

**Unit:** 5 — Sets and Probability
**Type:** Paper (reflection + error log final, 45 minutes)
**LO:** synthesize Unit 5 into one defensible principle; finalize error log for the year

---

## TODAY'S PURPOSE

The assessment and demo are done (L31). Today you close Unit 5 the same way you closed Units 1–4: error log retrospective, one honest principle, and the habit you're taking forward — which this year means **the habit you're taking out of this class entirely**.

---

## PART 1 — ERROR LOG RETROSPECTIVE (15 min)

Open your error log (the running document from Unit 1). Add a **Unit 5 Summary** entry:

```markdown
## Unit 5 — Sets and Probability Error Log Summary

### Top 3 errors I made:
1. **Error:** [e.g., added probabilities of overlapping events instead of using inclusion-exclusion]
   **Lesson:** [e.g., P(A ∪ B) = P(A) + P(B) − P(A ∩ B) — always check intersection]

2. **Error:** [e.g., reported expected value without variance for the risk simulator]
   **Lesson:** [e.g., a single number is not a risk description; variance/quantiles are required]

3. **Error:** [e.g., confused sensitivity with positive predictive value in Bayes problem]
   **Lesson:** [e.g., P(A|B) ≠ P(B|A); the denominator changes the whole number]

### Pattern I see across Unit 5:
[One sentence: e.g., "I compute the point estimate and forget the distribution that carries it."]

### One habit I'm taking out of this class:
[One sentence: e.g., "Every number I report needs a confidence interval or a sensitivity analysis."]
```

- ☐ Error log updated with Unit 5 summary
- ☐ Top 3 errors are specific
- ☐ Pattern and habit are one sentence each

---

## PART 2 — UNIT 5 SYNTHESIS (15 min)

Answer on paper (hand in before leaving):

**Q1.** (2 sentences) Your risk simulator reported `expected annual loss = 5,047` and `p_any_loss = 0.591`. A manager asks: "Should I fund the $5,000 backup?" Which of these two statistics actually decides the question, and why is the other one a distraction?

**Q2.** (2 sentences) An external report claims `P(at least one threat) = 0.20 + 0.15 + 0.20 = 0.55`. What is the mathematical error? What is the correct formula? Is the report's number too high, too low, or could it be either?

**Q3.** (2 sentences) In your Monte Carlo engine, you used `random.random()` and ran 10,000 trials. A peer used `numpy.random` and 100,000 trials. Both got similar means. What is the one thing you must check *before* comparing their variances?

**Q4.** (1 sentence) The most valuable thing I learned in Unit 5 that applies beyond probability is:

---

## PART 3 — THE YEAR'S PRINCIPLE (15 min)

You have written a principle at the end of every unit (U1–U4). Read them all now. Then write **one final principle** for the entire year — the single rule that, if you followed it every time you wrote code or computed a statistic, would have prevented your worst mistakes.

**Rules you may NOT use:**
- "Be careful" / "Don't rush" / "Test your code" — table stakes
- "Use the right formula" — technique, not principle

**I want the rule that only you would write, because it came from your specific pattern of errors across five units.**

> Example from a past student: "Every number I put in a report has a shadow — the assumption it depends on, the row I dropped, the distribution I ignored. I write the shadow first, then the number."

Write yours (3–4 sentences). Then write: **What is the one situation where you know you will break this rule, and what will you do when you catch yourself?**

---

## TURN IN (Google Classroom, due 23:59 tonight)

1. Your Part 1 error log summary (show on laptop or photo)
2. Your Part 2 answers Q1–Q4 (paper)
3. Your Part 3 year principle + "where I'll break it" answer (paper)

---

## 📋 TOMORROW

**Next:** U5 L33 — Course Close: What You Built This Year. Final reflection, portfolio review, goodbye.

---

## 🇹🇼 TAIWAN CONTEXT

The year-end principle is how the Taiwan CERT's senior analysts hand off to the next cohort: not "here are the procedures" but "here is the rule I learned the hard way that kept us honest." The error log you've kept all year is your personal CVE database — every entry is a vulnerability you patched in your own thinking. Take it with you.