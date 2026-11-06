# U4 L20 — Unit 4 Wrap & Transition to Unit 5 (Paper)

**Unit:** 4 — Algebra and SymPy
**Type:** Paper (reflection + preview, 45 minutes)
**LO:** 4.1, 4.2, 4.3 — synthesize unit learning; carry error log forward; preview Sets & Probability

---

## TODAY'S PURPOSE

Unit 4 is done. You built a verified toolkit, demoed it live, and took the assessment. Today: reflect on what broke and why, carry your error log into Unit 5, and preview what's next (Sets & Probability — the math behind randomness, sampling, and statistical inference).

---

## PART 1 — ERROR LOG RETROSPECTIVE (15 min)

Open your error log (the running document you started in L01). Add a **Unit 4 Summary** entry:

```markdown
## Unit 4 — Algebra and SymPy Error Log Summary

### Top 3 errors I made:
1. **Error:** [e.g., forgot modular inverse requirement for affine `a`]
   **Lesson:** [e.g., gcd(a,26) must be 1; always validate keys before use]

2. **Error:** [e.g., chi-squared overfits on short texts]
   **Lesson:** [e.g., combine with bigrams; test on varying lengths]

3. **Error:** [e.g., manifest only verified on demand, not on startup]
   **Lesson:** [e.g., verify-before-execute is the only trustworthy pattern]

### Pattern I see across Unit 4:
[One sentence: e.g., "I trust statistical heuristics as proofs until they fail on edge cases."]

### One habit I'm taking to Unit 5:
[One sentence: e.g., "Write the verification test before the feature."]
```

- ☐ Error log updated with Unit 4 summary
- ☐ Top 3 errors are specific (not "I made mistakes")
- ☐ Pattern and habit are one sentence each

---

## PART 2 — UNIT 4 SYNTHESIS (15 min)

Answer on paper (hand in before leaving):

**Q1.** (3 sentences) The Cipher Toolkit's brute-force mode uses chi-squared + bigrams to rank candidates. Why is this a *heuristic* and not a *proof*? Give one concrete example where it would rank the wrong key highest.

**Q2.** (2 sentences) Your manifest uses SHA-256. If an attacker has write access to both your files AND your manifest, they can forge a valid manifest. What additional mechanism would prevent this? Name it and explain in one sentence how it works.

**Q3.** (2 sentences) In affine cipher, `a=4` has no inverse mod 26. What does this mean for decryption? What does it mean for an attacker who intercepts ciphertext encrypted with `a=4`?

**Q4.** (1 sentence) The most valuable thing I learned in Unit 4 that applies beyond cryptography is:

---

## PART 3 — UNIT 5 PREVIEW: SETS & PROBABILITY (15 min)

**Unit 5** (Sets & Probability) runs ~Feb 19 – Mar 10 (20 lessons). The central question: **How do we reason about uncertainty with code?**

| week | focus | key concepts |
|---|---|---|
| 1 | Sets & counting | set operations, cartesian product, permutations vs combinations, binomial coefficient |
| 2 | Probability foundations | sample spaces, events, axioms, conditional probability, Bayes' theorem |
| 3 | Random variables & simulation | PMF/CDF, expectation, variance, Monte Carlo estimation, law of large numbers |
| 4 | Distributions & inference | Binomial, Geometric, Poisson, Normal; sampling, confidence intervals, hypothesis testing |

**Python tools you'll use:**
- `itertools` — products, combinations, permutations
- `random` — sampling, choices, shuffle
- `statistics` — mean, stdev, quantiles
- `matplotlib` — histograms, PMF/CDF plots
- **SymPy** — symbolic sums, `binomial`, `factorial`, solving probability equations

**First lesson (L21):** `itertools` lab — generate all poker hands, count flushes, verify probability = 0.00198.

---

## TURN IN (before leaving class)

1. **Error log** with Unit 4 summary (can be digital, show on laptop)
2. **Paper answers** to Q1–Q4 (handwritten or printed, stapled)
3. **One question** you have about Unit 5 (write on the back)

---

## 📋 NEXT

**Unit 5 — Sets & Probability** starts next class (L21).

**Homework (optional, recommended):** Read the `itertools` docs (`product`, `combinations`, `permutations`). Try: `list(combinations("AKQJT", 5))` — how many 5-card hands from 10 cards?

---

## 🇹🇼 TAIWAN CONTEXT

The error log habit comes from Taiwan's semiconductor fabs: every defect is logged, classified, and traced to a process step. The pattern you notice ("I trust heuristics as proofs") is your *root cause*. The habit you carry forward ("write the verification first") is your *corrective action*. This is how fabs hit 99.999% yield — not by being perfect, by never making the same mistake twice.