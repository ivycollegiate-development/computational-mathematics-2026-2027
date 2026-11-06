# U3 L26 — Midterm Review: Units 1–3 Consolidation (PAPER)

**Unit:** 3 — Describing Data with Statistics
**Type:** Paper (cold review, 45 minutes)
**LO:** retrieve Unit 1–3 skills without notes; identify personal gaps before the midterm

---

## TODAY'S PURPOSE

Midterms are next week (Jan 18–21). Today is a **cold review** — no notes, no neighbor, no computer. You face problems from Units 1, 2, and 3 to find out what you actually remember vs. what you only recognized when you saw it.

---

## PART 1 — UNIT 1: NUMBERS & GUARDRAILS (15 min)

**No computer. Pen and paper only.**

1. **Types & division:** `type(7/2)`, `type(7//2)`, `type(7%2)`. What does each return?
2. **Input validation:** Write the 4-line loop that gets a positive integer from the user, re-asks on `ValueError`, refuses `<= 0`.
3. **Boundaries:** Your `c_to_k(c)` refuses `c < -273.15`. You test with `-273.15`, `-273.16`, `-273`. Which are refused? Which are accepted? Is this correct per the spec "below absolute zero — refusing"?
4. **Quietly wrong:** `add(10**15, 1)` in Python returns `1000000000000001`. Your calculator refuses it. Why does the spec impose `10**15` as a ceiling when Python handles it?
5. **Security lens:** One sentence — why is a function that returns `0.0` instead of `0` dangerous in a security tool?

---

## PART 2 — UNIT 2: VISUALIZATION & INTEGRITY (15 min)

1. **Chart taxonomy:** You have daily `failed_logins` counts for 30 days. Which chart type: line, bar, scatter, or histogram? Why?
2. **Three-label rule:** What are the three labels every chart must have?
3. **Cleaning audit:** Your `clean_threats.py` drops rows. The rubric requires: "print the row count before and after cleaning." Why is *printing* required, not just computing?
4. **Honesty audit:** A peer's timeline chart has y-axis starting at 1,200 (not zero). They say "it makes the trend clearer." Is this acceptable? What must they add to `analysis.md`?
5. **Privacy:** A histogram of login success rates by class period. One period has 2 reports. They plot it. What is the k-anonymity violation? The fix?

---

## PART 3 — UNIT 3: STATISTICS & ANONYMIZATION (15 min)

1. **Centers:** Dataset: `[2, 2, 3, 3, 3, 4, 4, 100]`. Mean = ?, Median = ?, Mode = ?. Which survives the outlier?
2. **Spread:** Same dataset. Range = ?, Variance ≈ ?, StdDev ≈ ?. What does the stddev tell you that the range doesn't?
3. **Percentiles:** 21 values sorted. Your `percentile(v, 0.25)` uses `k = (n-1)*p`, interpolated. For `p=0.25`, `n=21`, what is `k`? What are `lo` and `hi` indices?
3. **IQR fences:** `q1=3, q3=7`. `iqr=4`. Lower fence = ?, Upper fence = ?. Is `100` an outlier?
4. **Anonymization:** A table has `age`, `zipcode`, `gender`. You suppress `age < 18` and generalize `zipcode` to first 3 digits. Is this k-anonymity for k=5? Why or why not?
5. **Misleading stats:** "Average login success rate = 99.2%." True, but misleading. What one number would make it honest?

---

## PART 4 — GAP MAP (10 min)

For each question above, mark in your notes:
- ✓ **Cold** — did it without any prompt
- ~ **Prompted** — needed the question to remember
- ✗ **Missing** — couldn't do it even with the question

**The ✗ items are your midterm study list.** Not "review everything" — review exactly these.

---

## TURN IN (Google Classroom, due 23:59 tonight)

Photo of your paper with all answers and your ✓/~✗ marks.

---

## 📋 TOMORROW

**Next:** U3 L27 — Unit 3 Assessment (Paper). 50 points, 35 minutes, closed book.

---

## 🇹🇼 TAIWAN CONTEXT

The "cold review" is how the ROC military's cyber units run readiness exercises — no runbooks, no hints, just the scenario and the clock. If you can't do it cold, you don't own it. The gap map is your personal after-action report.