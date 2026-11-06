# U4 L17 — Final Checks and Final Push (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (in-class final verification, 45 minutes)
**LO:** 4.3 — pass the complete fresh-clone verification; push final version by 11:59 PM

---

## TODAY'S PURPOSE

**Deadline: 11:59 PM tonight.** In class we run the full verification sequence together. You fix anything that fails. You push the final version. The demo is tomorrow.

---

## PART 1 — FULL VERIFICATION SEQUENCE (30 min)

Run in a **completely fresh directory** (not your working copy):

```bash
# Fresh directory
mkdir /tmp/verify-u4 && cd /tmp/verify-u4
git clone <your-repo-url>
cd compmath-u4-cipher-toolkit

# 1. Shift cipher round-trip
python3 toolkit.py --cipher shift --key 7 --text "hello"
python3 toolkit.py --cipher shift --key 7 --text "olssv"

# 2. Affine cipher round-trip (all valid a)
python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"
python3 toolkit.py --cipher affine --key 5 --b 8 --text "<ciphertext-from-above>"

# 3. Brute force ranks correctly
python3 toolkit.py --cipher brute --text "khear"

# 4. Test driver
python3 test_toolkit.py

# 5. Tamper demo
python3 demo_tamper.py

# 6. Verify manifest still works after demo restores
python3 test_toolkit.py

# 7. Edge cases (no tracebacks)
python3 toolkit.py --cipher shift --key 0 --text "hello"
python3 toolkit.py --cipher shift --key 26 --text "hello"
python3 toolkit.py --cipher shift --key -1 --text "hello"
python3 toolkit.py --cipher shift --key 5 --text ""
python3 toolkit.py --cipher shift --key 5 --text "123!@#"
python3 toolkit.py --cipher affine --key 4 --b 7 --text "hello"
python3 toolkit.py --cipher affine --key 13 --b 0 --text "hello"
```

**Every step must pass.** If any step fails, you fix it, commit, push, and re-run from step 1.

---

## PART 2 — DELIVERABLES CHECKLIST (10 min)

| item | verified? |
|---|---|
| Repo public, default branch `main` | ☐ |
| All 6 manifest files tracked | ☐ |
| `toolkit.py` has verify-on-startup | ☐ |
| `modkit.py` has bigram + chi-squared scoring | ☐ |
| `integrity.py` has build/check/chain | ☐ |
| `symkit.py` has expand/factor/simplify/solve | ☐ |
| `test_toolkit.py` prints "all tests passed" | ☐ |
| `demo_tamper.py` completes successfully | ☐ |
| `README.md` has all 4 defense answers (strong level) | ☐ |
| `CNY_BUILD_LOG.md` has 22 entries (or documented gaps) | ☐ |
| No tracebacks reach user for any input | ☐ |

---

## PART 3 — FINAL PUSH (5 min)

```bash
git add .
git commit -m "L17: final push - all verification green"
git push
```

**Confirm:** `git log --oneline -1` shows your final commit on `main` at GitHub.

---

## TURN IN (Google Classroom, due 11:59 PM TONIGHT)

1. **Repo URL** (public, default branch `main`)
2. **Fresh-clone verification output** (full terminal output from Part 1)
3. **`CNY_BUILD_LOG.md`** (from repo)
4. **One sentence**: what is the one thing you would still improve if you had one more week?

---

## 📋 TOMORROW

**Next:** L18 — Demo Day. 5-minute talk. Show the toolkit, run the tamper demo, answer one question.

**Demo order (30 seconds each):**
1. `git clone` → `python3 toolkit.py --cipher shift --key 7 --text "hello"`
2. `python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"`
3. `python3 toolkit.py --cipher brute --text "khear"` (show top 3)
4. `python3 demo_tamper.py` (tamper → fail → restore → pass)
5. One audience question

---

## 🇹🇼 TAIWAN CONTEXT

The "fresh clone verification" is how every CI/CD pipeline works: GitHub Actions, GitLab CI, Azure Pipelines — they all spin up a clean runner, clone your repo, and run your tests. If it passes there, it ships. If it only passes on your laptop, it doesn't. Your demo tomorrow is your pipeline.