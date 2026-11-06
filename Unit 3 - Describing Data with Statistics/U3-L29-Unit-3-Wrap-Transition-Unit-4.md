# U3 L29 — Unit 3 Wrap & Transition to Unit 4 (PAPER)

**Unit:** 3 — Describing Data with Statistics
**Type:** Paper (reflection + preview, 45 minutes)
**LO:** synthesize Unit 3 learning; carry error log forward; preview Algebra & SymPy

---

## TODAY'S PURPOSE

Unit 3 is done. You built a privacy-aware stats dashboard, audited your own anonymization, and took the assessment. Today: reflect on what broke and why, carry your error log into Unit 4, and preview what's next (Algebra & SymPy — the math underneath ciphers and hashes).

---

## PART 1 — ERROR LOG RETROSPECTIVE (15 min)

Open your error log. Add a **Unit 3 Summary** entry:

```markdown
## Unit 3 — Describing Data with Statistics Error Log Summary

### Top 3 errors I made:
1. **Error:** [e.g., used mean instead of median for skewed data in the dashboard]
   **Lesson:** [e.g., mean is not robust; median survives outliers]

2. **Error:** [e.g., forgot to interpolate percentiles — used nearest-rank instead of (n-1)*p]
   **Lesson:** [e.g., the interpolation convention matters; document which you use]

3. **Error:** [e.g., generalized zipcode to 3 digits but k-anonymity was only k=2]
   **Lesson:** [e.g., k-anonymity requires checking the actual equivalence classes, not just the technique]

### Pattern I see across Unit 3:
[One sentence: e.g., "I compute the number first and ask if it's honest later."]

### One habit I'm taking to Unit 4:
[One sentence: e.g., "Verify the anonymization before I compute the statistic."]
```

- ☐ Error log updated with Unit 3 summary
- ☐ Top 3 errors are specific
- ☐ Pattern and habit are one sentence each

---

## PART 2 — UNIT 3 SYNTHESIS (15 min)

Answer on paper (hand in before leaving):

**Q1.** (2 sentences) Your dashboard reported "average login success rate = 99.2%." The median was 99.8%. The mean was pulled down by one day at 87%. Which statistic should the security team see in the alert, and why?

**Q2.** (2 sentences) You generalized `zipcode` to first 3 digits for k-anonymity. A reviewer points out that in your dataset, the 3-digit prefix `100` appears for only 1 student. What is the k-anonymity violation, and what is the fix?

**Q3.** (2 sentences) Your percentile function used `k = (n-1)*p` with linear interpolation. A colleague's function uses `k = n*p` with nearest-rank. For n=21, p=0.25, what does each return? Which convention does the Unit 3 rubric require?

**Q4.** (1 sentence) The most valuable thing I learned in Unit 3 that applies beyond statistics is:

---

## PART 3 — UNIT 4 PREVIEW: ALGEBRA & SYMPY (15 min)

**Unit 4** (Algebra & SymPy) runs ~Jan 5 – Feb 16 (20 lessons). The central question: **The same math you already know, handed to a computer that does the bookkeeping.**

| week | focus | key concepts |
|---|---|---|
| 1 | SymPy first contact | symbols, expand, factor, simplify, solve |
| 2 | Solving systems & modular arithmetic | linear systems, modular inverse, `a*b ≡ 1 (mod n)` |
| 3 | Ciphers & hashing | shift/affine ciphers, SHA-256, integrity manifests |
| 4 | Project: Cipher Toolkit | shift, affine, brute-force with integrity verification |
| 5 | CNY break build days | daily commits, peer review, final demo |
| 6 | Assessment & demo | paper test + 5-minute live demo |

**Python tools you'll use:**
- `sympy` — `symbols`, `expand`, `factor`, `simplify`, `solve`, `linsolve`, `mod_inverse`
- `hashlib` — `sha256`, hex digests, manifest chains
- Your own modules: `symkit.py`, `modkit.py`, `integrity.py`, `toolkit.py`

**First lesson (U4 L01):** Launch — Number Answers vs Symbol Answers. SymPy solves `2x + 5 = 17` and tells you *how* it got `x = 6`.

---

## TURN IN (before leaving class)

1. **Error log** with Unit 3 summary (show on laptop)
2. **Paper answers** to Q1–Q4 (handwritten or printed, stapled)
3. **One question** you have about Unit 4 (write on the back)

---

## 📋 NEXT CLASS

**U4 L01:** Launch — Number Answers vs Symbol Answers. Bring your Codespace ready.

---

## 🇹🇼 TAIWAN CONTEXT

The transition from statistics to algebra mirrors Taiwan's cryptographic pipeline: the national CERT's analysts use statistical anomaly detection (Unit 3) to flag suspicious traffic, then algebraic verification (Unit 4 — modular arithmetic, hash chains, cipher analysis) to prove what happened. The statistic raises the alert; the algebra confirms it. Unit 4 teaches you the verification layer.