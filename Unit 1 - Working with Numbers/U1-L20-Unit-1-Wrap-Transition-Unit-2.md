# U1 L20 — Unit 1 Wrap & Transition to Unit 2 (PAPER)

**Unit:** 1 — Working with Numbers
**Type:** Paper (reflection + preview, 45 minutes)
**LO:** synthesize Unit 1 learning; carry error log forward; preview Visualizing Data

---

## TODAY'S PURPOSE

Unit 1 is done. You built a calculator that guards its boundaries, validates its input, and refuses to lie. Today: reflect on what broke and why, carry your error log into Unit 2, and preview what's next (Visualizing Data — the math behind honest charts).

---

## PART 1 — ERROR LOG RETROSPECTIVE (15 min)

Open your error log (the running document you started in L01). Add a **Unit 1 Summary** entry:

```markdown
## Unit 1 — Working with Numbers Error Log Summary

### Top 3 errors I made:
1. **Error:** [e.g., used `/` when I needed `//` for integer division]
   **Lesson:** [e.g., `/` always returns float in Python 3; `//` is floor division]

2. **Error:** [e.g., forgot to convert `input()` string to `int` before arithmetic]
   **Lesson:** [e.g., `input()` returns `str` every time; convert before math]

3. **Error:** [e.g., let `-273.15` pass the absolute-zero check when spec said "below"]
   **Lesson:** [e.g., boundary conditions are exact — test the edge, not just the neighborhood]

### Pattern I see across Unit 1:
[One sentence: e.g., "I assume the happy path and forget the guardrails until a test fails."]

### One habit I'm taking to Unit 2:
[One sentence: e.g., "Write the validation before the calculation."]
```

- ☐ Error log updated with Unit 1 summary
- ☐ Top 3 errors are specific (not "I made mistakes")
- ☐ Pattern and habit are one sentence each

---

## PART 2 — UNIT 1 SYNTHESIS (15 min)

Answer on paper (hand in before leaving):

**Q1.** (2 sentences) Your calculator refuses `-273.16` for Celsius-to-Kelvin but accepts `-273.15`. The spec says "below absolute zero — refusing." Is your behavior correct? If not, what one character fixes it?

**Q2.** (2 sentences) A user enters `1000000000000000` (10^15) and `1` for addition. Your calculator refuses with "Result exceeds safe integer range." But Python integers have arbitrary precision — `10**15 + 1` works fine in Python. Why does the project spec impose this limit?

**Q3.** (2 sentences) `float(4/2)` returns `2.0`. `int(4/2)` returns `2`. Your rubric required returning `int` when mathematically exact. Why does this matter for a security tool?

**Q4.** (1 sentence) The most valuable thing I learned in Unit 1 that applies beyond calculators is:

---

## PART 3 — UNIT 2 PREVIEW: VISUALIZING DATA (15 min)

**Unit 2** (Visualizing Data) runs ~Oct 8 – Nov 3 (21 lessons). The central question: **How do you make a chart that tells one true thing?**

| week | focus | key concepts |
|---|---|---|
| 1 | Chart taxonomy & Matplotlib basics | chart type ↔ data type, three-label rule, `figure`/`savefig`/`show` order |
| 2 | Reading data & cleaning | `csv.DictReader`, comment lines, sanity bounds, audit trail |
| 3 | Categorical & time-series | bar charts, timelines, weekday/weekend split |
| 4 | Relationships & distributions | scatter plots, correlation ≠ causation, histograms, bin choice |
| 5 | Integrity & privacy | provenance, k-anonymity, honesty audit (y-axis, dropped rows) |
| 6 | Project: Visualizing Threats | campus network data → three charts + analysis |
| 7 | Assessment & wrap | paper test + reflection principle |

**Python tools you'll use:**
- `csv` — `DictReader`, handling comment lines
- `matplotlib.pyplot` — `plot`, `bar`, `scatter`, `hist`, `savefig`
- `statistics` — mean, median, stdev (review from Unit 1)

**First lesson (U2 L01):** Unit 1 Assessment (paper) + Reflection journal. **No coding.**

---

## TURN IN (before leaving class)

1. **Error log** with Unit 1 summary (show on laptop)
2. **Paper answers** to Q1–Q4 (handwritten or printed, stapled)
3. **One question** you have about Unit 2 (write on the back)

---

## 📋 NEXT CLASS

**U2 L01:** Unit 1 Assessment (paper, 35 min) + Reflection journal. Bring pen, no computer for first 45 minutes.

---

## 🇹🇼 TAIWAN CONTEXT

The error log habit comes from Taiwan's semiconductor fabs: every defect is logged, classified, and traced to a process step. The pattern you notice ("I assume the happy path") is your *root cause*. The habit you carry forward ("write the validation first") is your *corrective action*. This is how fabs hit 99.999% yield — not by being perfect, by never making the same mistake twice.