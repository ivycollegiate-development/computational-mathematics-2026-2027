# U4 L13 — Build Day 3: Frequency Analysis and Defense Draft (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (in-class build day, 45 minutes)
**LO:** 4.2, 4.3 — add frequency analysis as a second scoring signal; produce a coherent written defense of your design choices

---

## TODAY'S PURPOSE

Two deliverables today: a **smarter brute force** that combines bigrams + frequency analysis, and a **draft README** that answers the four design questions from L10 Part 2. The demo is 11 days away (counting CNY break). Code that works is baseline; code you can *explain* is the grade.

---

## PART 1 — CHI-SQUARED FREQUENCY ANALYSIS (20 min)

English letter frequencies (percentages, from Norvig/Google Books):

```python
ENGLISH_FREQ = {
    'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75,
    's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'u': 2.76,
    'c': 2.78, 'm': 2.41, 'f': 2.23, 'y': 1.97, 'w': 2.36, 'g': 2.02,
    'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
    'q': 0.10, 'z': 0.07
}
```

Chi-squared statistic: for each letter, `(observed - expected)² / expected`. Lower = closer to English.

Add to `modkit.py`:

```python
def chi_squared(text):
    """Chi-squared statistic vs English frequencies. Lower = more English-like."""
    text = "".join(c.lower() for c in text if c.isalpha())
    if not text:
        return float("inf")
    n = len(text)
    observed = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
    for c in text:
        observed[c] += 1
    chi2 = 0.0
    for c, exp_pct in ENGLISH_FREQ.items():
        exp = n * exp_pct / 100.0
        obs = observed[c]
        chi2 += (obs - exp) ** 2 / exp
    return chi2


def combined_score(text):
    """Lower is better. Bigram score inverted + chi-squared."""
    # Invert bigram so higher bigram score -> lower combined
    bg = bigram_score(text)
    # Scale: bigram max ~len(text), chi2 typical 0-1000. Weight them.
    return chi_squared(text) - bg * 50  # tune weight as needed
```

Update `brute_force_shift` to return combined score and sort by it:

```python
def brute_force_shift(text):
    results = []
    for k in range(26):
        plain = shift_cipher(text, k, decrypt=True)
        results.append((k, plain, combined_score(plain)))
    results.sort(key=lambda x: x[2])  # ASCENDING: lower combined = better
    return results
```

- ☐ `chi_squared` and `combined_score` in `modkit.py`
- ☐ `brute_force_shift` sorts by combined score (ascending)
- ☐ Test: `python3 toolkit.py --cipher brute --text "khear"` — top is still `k=6 -> hello`
- ☐ Test on longer text: encrypt a 100-char paragraph with shift 13, brute should rank k=13 top
- ☐ `git commit -am "L13: chi-squared frequency analysis" && git push`

---

## PART 2 — COMBINED SCORE TUNING (10 min)

The weight `50` in `combined_score` is a guess. Tune it:

```python
# Quick tuning script (run once, not in modkit.py)
for weight in [10, 25, 50, 75, 100, 150]:
    # test on 10 known ciphertexts, count how many rank true key in top 3
    pass
```

Pick the weight that puts the true key in **top 3 for at least 8/10 test strings** of varying length (20-200 chars). Document your choice in a comment.

- ☐ Weight chosen and documented
- ☐ 8/10 test strings rank true key top 3
- ☐ `git commit -am "L13: tuned combined score weight" && git push`

---

## PART 3 — README DEFENSE DRAFT (15 min)

Open `README.md`. Write your answers to the **four questions from L10 Part 2** in your own words. This is the draft — you will revise it on L15.

1. **Proof vs exhaustive search**: Which mode is a proof, which is exhaustive search? One sentence each.
2. **Affine error leakage**: What does `ValueError` from `pow(a, -1, 26)` tell an attacker? Is your message too chatty?
3. **Brute-force candidate vs conclusion**: A wrong key can produce readable text. What makes your output a *candidate*?
4. **Frequency analysis decision**: "I will [not] implement frequency analysis, because..." — one sentence justification.

**Format:**

```markdown
# Cipher Toolkit

## Design Defense

### 1. Proof vs Exhaustive Search
**Shift/Affine encrypt/decrypt** is a **proof** — given the key, the output is mathematically guaranteed correct because modular arithmetic is deterministic and invertible.

**Brute-force solver** is an **exhaustive search** — it tries all 26 keys and ranks candidates by statistical likelihood. It cannot prove which key is correct; it only proposes the most plausible.

### 2. Affine Error Leakage
The `ValueError` from `pow(a, -1, 26)` reveals that `gcd(a, 26) != 1`, which tells an attacker that `a` shares a factor with 26 (i.e., `a` is even or 13). My error message says "a=X has no inverse mod 26" — it confirms the same fact but does not leak the factorization. This is acceptable chatter.

### 3. Candidate vs Conclusion
My brute-force output is a **candidate list** because: (a) short texts have multiple plausible decryptions (e.g., ROT13 on "hello" -> "uryyb" is also a word), (b) the combined score is a heuristic, not a proof. The top candidate is the *most likely*, not the *proven* key.

### 4. Frequency Analysis Decision
I **did** implement frequency analysis (chi-squared) combined with bigram scoring, because: on texts >50 chars it reliably identifies the correct shift; on shorter texts the bigram score prevents chi-squared from overfitting to noise. The combination is more robust than either alone.
```

- ☐ `README.md` exists with all four answers drafted
- ☐ Answers are in your own words, not copied
- ☐ `git commit -am "L13: README defense draft" && git push`

---

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. **Output of brute force on a 100-char ciphertext** (encrypt a paragraph, show top 5 ranked)
2. **Your chosen weight** for combined score and the 8/10 test result
3. **Link to `README.md`** in your repo (public, so I can read it)
4. **One sentence**: which of the four defense questions is hardest to answer honestly?

---

## 📋 TOMORROW

**Next:** L14 — Build Day 4. Manifest integrity on *every run* (not just on demand), tamper demonstration script, and final edge-case sweep. The written defense gets peer-reviewed.

**Milestone check:** By end of L14, a classmate should be able to clone, run `toolkit.py` once, see the manifest update, tamper with a file, run again, and see the failure — all without asking you how.

## 🇹🇼 TAIWAN CONTEXT

Chi-squared frequency analysis is the same statistical test used in Taiwan's national ID validation (the checksum digit) and in detecting forged documents — if the distribution of digits in a batch of receipts doesn't match Benford's law or expected frequencies, it's a flag. The same math that breaks a shift cipher catches tax fraud.