# U2 L21 — Unit 2 Wrap & Transition to Unit 3 (PAPER)

**Unit:** 2 — Visualizing Data
**Type:** Paper (reflection + preview, 45 minutes)
**LO:** synthesize Unit 2 learning; carry error log forward; preview Describing Data with Statistics

---

## TODAY'S PURPOSE

Unit 2 is done. You built three honest charts from messy campus network data, audited your own cleaning, and reviewed peers' work with the same rigor. Today: reflect on what broke and why, carry your error log into Unit 3, and preview what's next (Describing Data with Statistics — the math behind the picture).

---

## PART 1 — ERROR LOG RETROSPECTIVE (15 min)

Open your error log. Add a **Unit 2 Summary** entry:

```markdown
## Unit 2 — Visualizing Data Error Log Summary

### Top 3 errors I made:
1. **Error:** [e.g., forgot `plt.savefig()` before `plt.show()` — got empty PNG]
   **Lesson:** [e.g., `show()` clears the figure; save first, then show]

2. **Error:** [e.g., dropped rows with `failed_logins > 1000` as "outliers" without checking if they were real attacks]
   **Lesson:** [e.g., an outlier in security data is often the signal, not the noise]

3. **Error:** [e.g., y-axis didn't start at zero, made a 5% change look like a doubling]
   **Lesson:** [e.g., the three-label rule includes the y-axis baseline; if not zero, footnote why]

### Pattern I see across Unit 2:
[One sentence: e.g., "I optimize for the chart looking good before I verify the data is honest."]

### One habit I'm taking to Unit 3:
[One sentence: e.g., "Clean with an audit trail, not just a filter."]
```

- ☐ Error log updated with Unit 2 summary
- ☐ Top 3 errors are specific
- ☐ Pattern and habit are one sentence each

---

## PART 2 — UNIT 2 SYNTHESIS (15 min)

Answer on paper (hand in before leaving):

**Q1.** (2 sentences) Your L18 honesty audit asked: "Does my y-axis start at zero? If not, do I say why?" You answered "yes" for your timeline chart. But the PNG shows y-axis starting at 120. What one line in `analysis.md` would make this honest?

**Q2.** (2 sentences) In L20 gallery walk, you saw a peer's weekday/weekend chart that aggregated by period. One period had 3 phishing reports. They plotted it as a bar. What is the k-anonymity violation, and what is the fix?

**Q3.** (2 sentences) Your cleaning script (`clean_threats.py`) dropped 47 rows with unparseable timestamps. Your `analysis.md` says "dropped malformed rows." The rubric required: "state exactly how many rows I dropped and why (blank, impossible, unparseable — by column)." What is missing from your statement?

**Q4.** (1 sentence) The most valuable thing I learned in Unit 2 that applies beyond visualization is:

---

## PART 3 — UNIT 3 PREVIEW: DESCRIBING DATA WITH STATISTICS (15 min)

**Unit 3** (Describing Data with Statistics) runs ~Nov 17 – Dec 17 (29 lessons). The central question: **The chart shows a pattern — but what does the number say?**

| week | focus | key concepts |
|---|---|---|
| 1 | Centers & spread | mean, median, mode; range, variance, stddev; which survives an outlier |
| 2 | Choosing the right statistic | distribution shape, skewed vs symmetric, when mean lies |
| 3 | Percentiles & five-number summary | quartiles, IQR, fences, outliers — the box plot's math |
| 4 | Misleading statistics | truncated axes, selective windows, correlation ≠ causation |
| 5 | PII & anonymization | what makes data identifying, suppression, generalization, k-anonymity |
| 6 | Project: Privacy-Aware Stats Dashboard | campus data → stats engine + privacy filter + dashboard |
| 7 | Assessment & wrap | paper test + reflection principle |

**Python tools you'll use:**
- `statistics` — `mean`, `median`, `mode`, `stdev`, `variance`, `quantiles`
- Your own `statslib.py` — you build it lesson by lesson
- `csv` — reading data (review from Unit 2)

**First lesson (U3 L01):** Launch — From Charts to Numbers: Why a Picture Is Not Enough. No coding.

---

## TURN IN (before leaving class)

1. **Error log** with Unit 2 summary (show on laptop)
2. **Paper answers** to Q1–Q4 (handwritten or printed, stapled)
3. **One question** you have about Unit 3 (write on the back)

---

## 📋 NEXT CLASS

**U3 L01:** Launch — From Charts to Numbers: Why a Picture Is Not Enough. Bring your error log.

---

## 🇹🇼 TAIWAN CONTEXT

The transition from visualization to statistics mirrors Taiwan's national security reporting pipeline: the CERT's weekly threat bulletin starts with charts (timelines, heatmaps) but the actionable intelligence is in the statistics (percentile shifts, anomaly scores, confidence intervals). The chart gets the decision-maker's attention; the statistic justifies the decision. Unit 3 teaches you to produce the statistic that survives scrutiny.