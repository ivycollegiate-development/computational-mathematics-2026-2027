# U4 L16 — CNY Break Build Days: Daily Commits, No Silent Weeks (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (self-directed build days, Feb 3–14)
**LO:** 4.3 — execute the CNY build plan; maintain daily commit cadence; arrive Feb 15 with zero surprises

---

## TODAY'S PURPOSE

**No class meeting.** This lesson is your accountability structure for the 10-day CNY break (Feb 3 half day – Feb 14). You made a plan in L15. Today through Feb 14, you execute it. One 30-minute session = one commit. No exceptions.

---

## THE RULES

1. **One session = one commit.** The commit message must match your `CNY_BUILD_PLAN.md` target.
2. **No silent days.** If you miss a day, do two sessions the next day. Two missed days in a row = plan failed.
3. **No new features after Feb 10.** Feb 11–14 are polish, test, document only.
4. **Push every commit.** A local commit that isn't pushed does not count.
5. **Feb 14 Session 2 = Final integration test.** Run the full verification sequence in a fresh clone.

---

## DAILY VERIFICATION SEQUENCE (run every session)

```bash
# In a FRESH directory every time
git clone <your-repo-url>
cd compmath-u4-cipher-toolkit
python3 toolkit.py --cipher shift --key 7 --text "hello"
python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"
python3 toolkit.py --cipher brute --text "khear"
python3 test_toolkit.py
python3 demo_tamper.py
```

**Every session must end with this sequence passing.** If it fails, fix it before you commit.

---

## COMMIT LOG TEMPLATE

Append to `CNY_BUILD_LOG.md` after each session:

```markdown
## Feb 3 Session 1
**Target:** Polish README defense — clarify chi-squared weighting explanation
**Commit:** `git commit -am "Feb 3 S1: README chi-squared clarification"`
**Verification:** Fresh clone → all 6 checks PASS
**Time:** 32 min
**Notes:** Reduced chi-squared weight from 50 to 45 after testing on 20-char strings
```

---

## FEB 14 SESSION 2 — FINAL INTEGRATION TEST (mandatory)

This is not optional. On Feb 14, your second session **must** be a complete fresh-clone verification:

```bash
# In a completely fresh directory
git clone <your-repo-url>
cd compmath-u4-cipher-toolkit

# 1. All three ciphers round-trip
python3 toolkit.py --cipher shift --key 7 --text "hello"
python3 toolkit.py --cipher shift --key 7 --text "olssv"
python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"
python3 toolkit.py --cipher affine --key 5 --b 8 --text "<ciphertext>"
python3 toolkit.py --cipher brute --text "khear"

# 2. Test driver
python3 test_toolkit.py

# 3. Tamper demo
python3 demo_tamper.py

# 4. Verify manifest still works after demo restores files
python3 test_toolkit.py

# 5. README exists and has all four defense answers
cat README.md
```

**Every step must pass.** If any step fails, you have until 11:59 PM Feb 15 to fix and push.

---

## FEB 15 — FINAL CHECKS, FINAL PUSH (class day)

**In class Feb 15:** You bring a laptop with your repo. We run the verification sequence together. You hand in:

1. Repo URL (public, default branch `main`)
2. `CNY_BUILD_LOG.md` with 22 entries (or explanation for any gaps)
3. Fresh-clone verification output (run in class)
4. Demo readiness: you can run the tamper demo in 30 seconds

**Feb 16 — DEMO DAY:** 5-minute talk. Show the toolkit, show the tamper demo, answer one question.

---

## TURN IN (Google Classroom, due Feb 15, 11:59 PM)

1. **Repo URL**
2. **`CNY_BUILD_LOG.md`** (full log with 22 entries)
3. **Fresh-clone verification output** (run in class Feb 15)
4. **One paragraph**: what you learned from maintaining daily commits over a break, and what you would do differently next time

---

## 📋 TOMORROW (Feb 15)

**Next:** L17 — Final Checks and Final Push. In-class verification, last fixes, push by 11:59 PM.

## 🇹🇼 TAIWAN CONTEXT

The "no silent weeks" rule is how g0v projects survive: every project has a "heartbeat" — a weekly commit, a weekly meeting, a weekly sync. If the heartbeat stops for two weeks, the project is archived. Your CNY log is your heartbeat. If it has gaps, the project is not dead — but it is on life support, and the demo is the resuscitation attempt.