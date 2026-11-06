# U3 L28 — Assessment Walkthrough & Reflection (PAPER)

**Unit:** 3 — Describing Data with Statistics
**Type:** Paper (grade release + reflection, 45 minutes)
**LO:** honestly diagnose assessment gaps; synthesize Unit 3 into one defensible principle

---

## TODAY'S PURPOSE

Assessments back. We go over the key together, you mark **got it** / **not yet**, and then you write the reflection that carries Unit 3 forward.

---

## PART 1 — GRADE RELEASE WALKTHROUGH (15 min)

We go problem by problem. As we do:

- Mark each problem **got it** or **not yet** — no points yet, just honesty.
- For every **not yet**, write one sentence: *what specifically confused me?*
  - "I didn't study" → not an answer
  - "I mixed up the interpolation formula for q1" → answer
  - "I forgot the lower fence is q1 - 1.5*IQR, not q1 - IQR" → answer

These sentences are raw material for Part 3.

---

## PART 2 — THE THREE THINGS UNIT 3 WAS ACTUALLY ABOUT (15 min)

In your notes, name each one with **a concrete example from your own project**:

1. **Centers & spread** — the mean lies when outliers exist; the median doesn't.
   - Which of your project's statistics was most affected by an outlier?
   - What did the median show that the mean hid?

2. **Percentiles & outliers** — the five-number summary is a contract: min, q1, median, q3, max.
   - Your project's data had outliers. Which fence caught them?
   - When you dropped them, which of the five numbers moved? Which didn't?

3. **Privacy & honesty** — the audience is real. Your data came from campus systems; someone was behind every row.
   - What did you have to be careful **not** to show in your dashboard?
   - What generalization (suppression, binning) did you apply, and what k did you achieve?

**The point of naming all three:** A statistic is only as good as the honesty of the pipeline that produced it. Perfect computation on de-identified data that wasn't actually de-identified is still a privacy violation.

---

## PART 3 — THE PRINCIPLE (15 min)

Write, in your own words and in 3–4 sentences, your answer to this:

**What is the one rule you will follow for the rest of this class — and probably the rest of your life — about computing statistics from data that is not yours?**

**Rules you may NOT use as your answer:**
- "Be accurate" — table stakes, not a principle
- "Don't lie" — too vague
- "Check for outliers" — a technique, not a principle

**I want the rule that only you would write, because it came from something that actually went wrong in your own work.**

**Example principles from past years:**
- "If removing one row changes the headline statistic, the row stays — and I footnote why."
- "I never publish a statistic I cannot explain to the person whose data it is."
- "Every statistic I report has an 'honesty appendix' — one paragraph listing what I dropped, what I imputed, and what the number cannot answer."

**Then: what is the HARDEST part of keeping that rule when you are in a hurry and someone is waiting for a number?**

> Write the honest answer. "I forget" is not an answer. "The pressure to ship fast makes me skip the anonymization audit" is.

---

## TURN IN (Google Classroom, due 23:59 tonight)

1. Your Part 1 "not yet" sentences (photo or typed)
2. Your Part 2 three themes with your own examples
3. Your Part 3 principle (3–4 sentences) + the "hardest part" answer

---

## 📋 TOMORROW

**Next:** U3 L29 — Unit 3 Wrap & Transition to Unit 4. Error log carry-forward, Algebra & SymPy preview.

---

## 🇹🇼 TAIWAN CONTEXT

The principle exercise is how the Ministry of Digital Affairs' data governance framework trains analysts: not "follow the checklist" but "name the rule you broke last time and commit to the one you'll keep next time." The Taiwan CERT's own incident reports follow this pattern — every report ends with a "lessons learned" section that is a principle, not a procedure.