# U4 L19 — Unit 4 Assessment (Paper)

**Unit:** 4 — Algebra and SymPy
**Type:** Paper (closed-book, closed-laptop, 35 minutes)
**LO:** 4.1, 4.2, 4.3 — assess symbolic algebra, modular arithmetic, ciphers, hashing, integrity

---

## ASSESSMENT STRUCTURE (50 points, 35 minutes)

| section | topic | pts | time |
|---|---|---|---|
| A | SymPy Verbs | 10 | 7 min |
| B | Modular Arithmetic & Ciphers | 20 | 12 min |
| C | Hashing & Integrity | 15 | 10 min |
| D | Design Reasoning | 5 | 6 min |

---

## SECTION A — SYMPY VERBS (10 pts)

**A1.** (3 pts) Write the SymPy code to:
- Declare a symbol `x`
- Expand `(x + 3)(x - 2)`
- Factor the result back
- Simplify `2*x/2`

**A2.** (3 pts) What does `solve(x**2 - 4, x)` return? What does `solve(x**2 + 4, x)` return? Explain the difference in one sentence.

**A3.** (4 pts) A student writes:
```python
from sympy import expand
print(expand((x + 2)(x + 3)))
```
and gets `SyntaxError`. Why? Write the corrected line.

---

## SECTION B — MODULAR ARITHMETIC & CIPHERS (20 pts)

**B1.** (4 pts) List all values of `a` in `{1,2,...,25}` that have a modular inverse modulo 26. (Hint: `gcd(a,26)=1`)

**B2.** (4 pts) Affine cipher: `encrypt(p) = (a*p + b) mod 26`. If `a=5, b=8`, what is the encryption of `h` (p=7)? Show the arithmetic.

**B3.** (4 pts) For the same cipher (`a=5, b=8`), what is the decryption formula? Compute `a_inv` and write the full decrypt function.

**B4.** (4 pts) Why does `a=4` fail for affine cipher modulo 26? What does the ciphertext look like when you encrypt `hello` with `a=4, b=0`? (Conceptual answer — no code needed.)

**B5.** (4 pts) Brute-force shift cipher on ciphertext `khoor` (5 letters). The top candidate is `hello` at shift 3. Name **two reasons** why this might be the wrong key even though `hello` is a valid English word.

---

## SECTION C — HASHING & INTEGRITY (15 pts)

**C1.** (3 pts) You change one character in a 10 MB file. How many of the 64 hex characters in its SHA-256 digest change? Why does this matter?

**C2.** (4 pts) A manifest contains:
```
a1b2c3  data/log_1.csv
d4e5f6  data/log_2.csv
```
You tamper with `log_2.csv`. The manifest check reports `CHANGED  data/log_2.csv`. **What two things does this tell you, and what one thing does it NOT tell you?**

**C3.** (4 pts) Hash chain vs. flat manifest. An attacker can edit files AND the manifest. Explain in two sentences:
- How a flat manifest fails against this attacker
- How a hash chain improves the situation
- What a hash chain still cannot prevent

**C4.** (4 pts) Difference between integrity and authenticity. Complete:
- A hash proves the data has not changed **since ______**.
- A signature proves **______** wrote the data.
- Why can't a hash alone establish authenticity?

---

## SECTION D — DESIGN REASONING (5 pts)

**D1.** (5 pts) Your Cipher Toolkit's brute-force mode outputs a ranked list of candidates. A user asks: "Which one is the right key?" Write a **two-sentence** answer that is honest, technically accurate, and useful.

---

## ADMINISTRATION

- **Format:** Paper only. No laptop, no phone, no notes.
- **Allowed:** Pen/pencil, calculator (for modular arithmetic only).
- **Turn in:** Staple pages in order. Name on every page.
- **Answer key:** Held separately (not in student repo). Graded by instructor.

---

## 📋 TOMORROW

**Next:** L20 — Unit 4 Wrap and Transition to Unit 5. Reflection, error log carry-forward, Sets & Probability preview.

---

## 🇹🇼 TAIWAN CONTEXT

This assessment mirrors the kinds of questions on Taiwan's information security certification (TWISC) and the national CERT's incident response drills: given a hash mismatch, what do you know? Given a cipher with a bad key, what leaks? The math is the same; the stakes are higher.