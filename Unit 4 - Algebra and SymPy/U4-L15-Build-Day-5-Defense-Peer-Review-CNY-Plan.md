# U4 L15 — Build Day 5: Defense Finalized, Peer Review, CNY Plan Locked (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (in-class build day, 45 minutes)
**LO:** 4.3 — finalize written defense, pass peer review, lock CNY break build plan with daily commit targets

---

## TODAY'S PURPOSE

Last in-class build day before CNY. By end of class: your README defense is **final**, a classmate has **verified** your toolkit works in a fresh clone, and your **CNY break plan** has specific 30-minute sessions with commit targets for Feb 3–14. The demo is Feb 16. You have 10 days of break — use them or lose them.

---

## PART 1 — README DEFENSE FINALIZATION (20 min)

Open your `README.md`. Revise each of the four answers using this rubric:

| question | weak answer | strong answer |
|---|---|---|
| 1. Proof vs exhaustive | "shift is proof, brute is search" | "Shift/affine encrypt/decrypt are proofs because modular inversion guarantees a unique inverse. Brute force is exhaustive search because it enumerates all 26 keys and ranks by heuristic — no mathematical guarantee the top candidate is correct." |
| 2. Error leakage | "my error message is fine" | "The stdlib `pow(a,-1,26)` raises `ValueError` for non-invertible `a`, leaking that `a` shares a factor with 26. My message says 'a=X has no inverse mod 26; choose from {1,3,5,7,9,11,15,17,19,21,23,25}' — it confirms the same fact without exposing the factorization. Acceptable." |
| 3. Candidate vs conclusion | "brute force might be wrong" | "A wrong key can produce readable English (e.g., ROT13 on 'hello' → 'uryyb'). My combined score (chi-squared + bigrams) is a statistical heuristic. On short texts (<30 chars) multiple keys score similarly. The output is a ranked candidate list; the human must decide." |
| 4. Frequency analysis | "I didn't do it because it's hard" | "I implemented chi-squared frequency analysis combined with bigram scoring. Chi-squared alone overfits on short texts; bigrams provide local structure evidence. The weighted combination puts the true key in top 3 for 8/10 test strings (20–200 chars). Weight=50 chosen by grid search." |

**Your revised answers must:**
- Use specific technical terms (modular inverse, chi-squared, bigram, heuristic, exhaustive search)
- Reference your actual implementation (weight=50, 8/10 test, the valid `a` set)
- Be honest about limitations (short texts, statistical not proof)

- ☐ All four answers revised to "strong" level
- ☐ `README.md` pushed
- ☐ `git commit -am "L15: README defense finalized" && git push`

---

## PART 2 — PEER VERIFICATION (15 min)

Swap laptops with a partner. **Do not talk them through it.** They must:

1. `git clone <your-repo-url>`
2. `cd compmath-u4-cipher-toolkit`
3. `python3 toolkit.py --cipher shift --key 7 --text "hello"`
4. `python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"`
5. `python3 toolkit.py --cipher brute --text "khear"`
6. `python3 test_toolkit.py`
7. `python3 demo_tamper.py`

**Partner fills this out:**

| check | PASS/FAIL | notes |
|---|---|---|
| clone works | | |
| shift round-trip | | |
| affine round-trip | | |
| brute ranks hello top 3 | | |
| test_toolkit.py all pass | | |
| demo_tamper.py completes | | |
| README defense readable | | |

**If any FAIL:** Fix it **now**. You have 10 minutes. This is the last in-class day.

- ☐ Partner verification all PASS
- ☐ Any failures fixed and re-verified
- ☐ `git commit -am "L15: peer verified" && git push`

---

## PART 3 — CNY BREAK BUILD PLAN (10 min)

You have **10 days** (Feb 3–14). CNY is Feb 4–14 (Feb 3 half day). Fill this table with **specific 30-minute sessions**. One session per row. Commit at the end of every session.

| date | session | target | commit message |
|---|---|---|---|
| Feb 3 (half) | 1 | | |
| Feb 4 | 1 | | |
| Feb 4 | 2 | | |
| Feb 5 | 1 | | |
| Feb 5 | 2 | | |
| Feb 6 | 1 | | |
| Feb 6 | 2 | | |
| Feb 7 | 1 | | |
| Feb 7 | 2 | | |
| Feb 8 | 1 | | |
| Feb 8 | 2 | | |
| Feb 9 | 1 | | |
| Feb 9 | 2 | | |
| Feb 10 | 1 | | |
| Feb 10 | 2 | | |
| Feb 11 | 1 | | |
| Feb 11 | 2 | | |
| Feb 12 | 1 | | |
| Feb 12 | 2 | | |
| Feb 13 | 1 | | |
| Feb 13 | 2 | | |
| Feb 14 | 1 | Final integration test | |
| Feb 14 | 2 | Final push | |

**Suggested targets (pick yours):**
- Polish README defense (clarify, shorten, add code snippets)
- Add docstrings to every function in all 4 modules
- Add `--decrypt` flag to shift/affine (currently decrypt = encrypt with negative key)
- Handle stdin input (`--text -` reads from stdin)
- Add `--verify-only` flag to `toolkit.py` (just checks manifest, exits)
- Test on Windows line endings (clone on Windows VM or WSL)
- Create a 30-second demo video (screen record)
- Write a one-page "how to verify" guide for the demo

**Rule:** No new features after Feb 10. Feb 11–14 are polish, test, document only.

- ☐ Table filled with 22 specific sessions
- ☐ No "new feature" sessions after Feb 10
- ☐ Plan pushed to repo as `CNY_BUILD_PLAN.md`
- ☐ `git commit -am "L15: CNY build plan locked" && git push`

---

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. **Link to final `README.md`** in your repo
2. **Partner's verification table** (photo or text)
3. **Your `CNY_BUILD_PLAN.md`** (pushed to repo)
4. **One sentence**: what is the single highest-risk item for Feb 15 demo, and your mitigation?

---

## 📋 TOMORROW

**No class Feb 3 (half day) through Feb 14 (CNY break).**

**Next class: Feb 15** — Final checks, final push. **Feb 16** — Demo day.

**Your job over break:** Execute the plan. One 30-min session, one commit, every day. If you miss a day, do two sessions the next. Do not let a week pass with zero commits — that is how the demo fails.

## 🇹🇼 TAIWAN CONTEXT

The "commit daily, demo weekly" rhythm is how the Taiwan open-source community (g0v, COSCUP, MOEA open data) ships reliable software with volunteer contributors. A project that goes dark for two weeks is a project that will not recover. Your CNY plan is your pulse — if it flatlines, the project dies.