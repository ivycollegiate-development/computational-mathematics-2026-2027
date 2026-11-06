# U4 L18 — Demo Day: 5-Minute Talk (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (live demo, 5 minutes per student)
**LO:** 4.3 — demonstrate working toolkit, explain design choices, answer one question

---

## TODAY'S PURPOSE

**5 minutes. No slides. Live code only.** You show the toolkit works, you show the manifest detects tampering, you answer one question. That is the whole grade for the Cipher Toolkit project.

---

## DEMO SCRIPT (5 minutes exactly)

### 0:00–0:30 — Clone and Shift Cipher
```bash
git clone <your-repo-url>
cd compmath-u4-cipher-toolkit
python3 toolkit.py --cipher shift --key 7 --text "hello"
# output: olssv
python3 toolkit.py --cipher shift --key 7 --text "olssv"
# output: hello
```
**Say:** "Shift cipher encrypts and decrypts. Round-trip verified."

### 0:30–1:00 — Affine Cipher
```bash
python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"
# output: <ciphertext>
python3 toolkit.py --cipher affine --key 5 --b 8 --text "<ciphertext>"
# output: hello
```
**Say:** "Affine cipher with modular inverse. Key 5 is invertible mod 26."

### 1:00–2:00 — Brute Force with Scoring
```bash
python3 toolkit.py --cipher brute --text "khear"
```
**Say:** "Brute force tries all 26 shifts and ranks by combined chi-squared + bigram score. Top candidate is k=6 → 'hello'. This is a candidate list, not a proof — short texts can have multiple plausible decryptions."

### 2:00–3:30 — Tamper Demo
```bash
python3 demo_tamper.py
```
**Say:** "Every run verifies the manifest on startup. I tamper with one character in toolkit.py, run again, and the integrity check fails naming the exact file. Restore from git, and it passes again."

### 3:30–4:00 — Test Driver
```bash
python3 test_toolkit.py
# output: all tests passed
```
**Say:** "Test driver covers round-trips, brute ranking, edge cases, manifest generation. Runs in a fresh clone."

### 4:00–5:00 — One Question (from audience/instructor)
**Prepare for these likely questions:**
- "What happens if the ciphertext is only 3 letters?" → "Bigram score has no pairs; chi-squared dominates; multiple keys tie. Output is correctly ambiguous."
- "Why not frequency analysis alone?" → "Chi-squared overfits on short texts. Bigrams add local structure. Combined score (weight=50) puts true key top 3 for 8/10 test strings."
- "What does the affine error message leak?" → "It confirms `a` has no inverse mod 26, which leaks that `a` shares a factor with 26. My message lists valid `a` values — same information, no factorization exposed."
- "How does the manifest chain work?" → "Each record hashes the previous digest + new record. Changing record 2 changes the final digest even if record 3 is untouched. But an attacker who recomputes the whole chain can still forge — that's what a signature is for."

---

## GRADING RUBRIC (100 pts)

| component | pts | criteria |
|---|---|---|
| Shift round-trip | 15 | Correct output, no traceback |
| Affine round-trip | 15 | Correct output, valid key used |
| Brute force ranking | 20 | True key in top 3, scores shown |
| Tamper demo | 25 | Fresh run → tamper → fail naming file → restore → pass |
| Test driver | 10 | "all tests passed" in fresh clone |
| Question answer | 15 | Technically accurate, honest about limitations |

**Deductions:**
- Any traceback shown: -10
- Demo exceeds 5 minutes: -5 per 30 seconds
- Cannot answer question: -10
- Repo not public / wrong branch: -20

---

## TURN IN (immediately after demo)

**Nothing to submit.** Grade is recorded live. Repo must already be pushed (L17 deadline).

---

## 📋 TOMORROW

**Next:** L19 — Unit 4 Assessment (Paper). Closed-book, 35 minutes. Covers: SymPy verbs, modular arithmetic, affine cipher invertibility, hash properties, manifest vs signature.

## 🇹🇼 TAIWAN CONTEXT

The 5-minute live demo is how g0v hackathons judge projects: no slides, no video, just `git clone` and run. If it works in a fresh environment, you ship. If it doesn't, you don't. The audience question is the code review — can you defend your choices under pressure?