# U1 L19 — Calculator Project: Submission & Peer Review (TECH)

**Unit:** 1 — Working with Numbers
**Type:** Machine (PR submission + structured peer review, 85 minutes)
**LO:** submit the Calculator project via Pull Request; review a partner's project using the same rubric you used on your own

---

## TODAY'S PURPOSE

You push your final commit, open a Pull Request, and then review someone else's calculator with the same rigor you applied to your own. The PR is the submission; the review is the proof you understand the rubric.

---

## PART 0 — OPEN THE PR (10 min)

```bash
cd ~/compmath-u1-calculator-lab
git push
```

Go to `github.com/ivycollegiate-development/computational-mathematics-2026-2027` → your fork → **Contribute → Open pull request**

- **Base:** `main` (upstream)
- **Compare:** your branch (or `main` if you worked on main)
- **Title:** `U1 Final: Calculator with Guardrails — [Your Name]`
- **Description:** Copy your `analysis.md` content here (or link to it)

Create the PR. **Do not merge.** The PR stays open for review.

---

## PART 1 — PEER REVIEW ASSIGNMENT (5 min)

I will assign you a partner. You review **their** PR. They review **yours**.

Open their PR. You have the Files Changed tab. You have the rubric from L18.

---

## PART 2 — STRUCTURED REVIEW (50 min)

**Review their code against every checkbox from L18 Part 0.** Write your review as a **PR Review** (not a comment — use the Review feature: Files Changed → Review Changes → Request Changes / Comment / Approve).

**Your review must contain:**

### For each of the 4 rubric sections (Core, Boundaries, Quietly Wrong, Tests, Analysis):

| section | verdict | evidence |
|---|---|---|
| Core functions | PASS / PARTIAL / FAIL | e.g., "`get_number` accepts empty string — FAIL" |
| Boundaries | PASS / PARTIAL / FAIL | e.g., "`-273.15` accepted but spec says 'below' — PARTIAL" |
| Quietly wrong | PASS / PARTIAL / FAIL | e.g., "`div` returns `float` for `4/2` — FAIL" |
| Tests | PASS / PARTIAL / FAIL | e.g., "`test_calculator.py` fails on line 23 — FAIL" |
| Analysis | PASS / PARTIAL / FAIL | e.g., "analysis.md missing limitation paragraph — PARTIAL" |

### One specific code suggestion (required):

Find **one** thing you would change in their `calculator.py`. Use the PR "Add suggestion" feature (hover line → `+` → type suggestion). It can be:
- A missing boundary check
- A type inconsistency
- A confusing variable name
- A missing docstring

### One question for the author (required):

Ask about a design choice. Example: "Why did you use `Fraction` in `mul` but `float` in `div`?" or "What happens if someone calls `c_to_k(-300)`?"

---

## PART 3 — RECEIVE YOUR REVIEW (15 min)

Your partner posts their review. You:
1. Read every comment.
2. **Do not defend.** Just understand.
3. If they found a real bug, fix it, commit, push — the PR updates automatically.
4. Reply to their review comment: "Fixed in `<commit-hash>`" or "Understood — I chose this because..."

---

## PART 4 — FINAL PUSH (5 min)

If you fixed anything based on review:
```bash
cd ~/compmath-u1-calculator-lab
git push
```

---

## TURN IN (Google Classroom, due 23:59 tonight)

1. **Link to your PR** (the one you opened)
2. **Link to the PR you reviewed** (your partner's)
3. Screenshot showing your review posted (with all 5 section verdicts, one code suggestion, one question)
4. Screenshot showing your partner's review on your PR

---

## 📋 TOMORROW

**Next:** U1 L20 — Unit 1 Wrap & Transition to Unit 2. Reflection, journal, preview of Visualizing Data.

---

## 🇹🇼 TAIWAN CONTEXT

The PR review is how every open-source project in Taiwan (g0v, COSCUP, MOEA sandbox) gates contributions. A maintainer does not merge code they haven't read. A contributor does not submit code they haven't tested. The "one code suggestion + one question" minimum ensures the review is substantive, not performative. This habit — review as rigorously as you write — is what separates a portfolio project from a production service.