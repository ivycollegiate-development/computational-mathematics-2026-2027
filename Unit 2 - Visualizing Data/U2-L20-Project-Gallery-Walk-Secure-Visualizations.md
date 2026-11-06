# U2 L20 — Project Gallery Walk: Secure Visualizations (TECH + DISCUSSION)

**Unit:** 2 — Visualizing Data
**Type:** Machine (gallery walk) + Discussion (peer review of submitted projects, 85 minutes)
**LO:** evaluate peer visualizations using the honesty audit; articulate what makes a visualization secure

---

## TODAY'S PURPOSE

Your projects are submitted (PRs open from L18). Today you don't look at your own — you look at **three others**. You apply the honesty audit you built in L18/L19 to someone else's work. This is the only way to know if the rubric actually works.

---

## PART 0 — GALLERY SETUP (10 min)

I assign you **three PRs to review** (not your own, not your L19 partner's).

For each PR:
1. Open the PR → Files Changed
2. Open the repo → view the three PNGs (`chart1_timeline.png`, `chart2_weekday_weekend.png`, `chart3_success_rate.png`)
3. Read `analysis.md`
4. Run their `project_charts.py` locally if you want (optional)

---

## PART 1 — THE HONESTY AUDIT ×3 (50 min)

For **each** of the three projects, fill this table in your notes:

| project | chart | y-axis starts at 0? | rows dropped? documented? | unplotted data? acknowledged? | one honest limitation stated? | overall: SECURE / NEEDS WORK / INSECURE |
|---|---|---|---|---|---|---|
| 1 | timeline | | | | | |
| 1 | weekday | | | | | |
| 1 | success rate | | | | | |
| 2 | timeline | | | | | |
| 2 | weekday | | | | | |
| 2 | success rate | | | | | |
| 3 | timeline | | | | | |
| 3 | weekday | | | | | |
| 3 | success rate | | | | | |

**Rules:**
- "SECURE" = all three charts pass the honesty audit
- "NEEDS WORK" = 1–2 charts have issues
- "INSECURE" = systematic issues (no audit, y-axis manipulation, silent drops)

**For any "NEEDS WORK" or "INSECURE":** Write one specific fix the author could make. Not "be more honest" — "add the dropped-row count to analysis.md paragraph 2."

---

## PART 2 — THE SECURITY QUESTIONS (25 min)

We discuss as a class. For each question, the *author of the project being discussed* does not answer first — others do.

1. **The campus network dataset has daily `failed_logins` counts.** A chart of that makes a bad week look worse than it was. What is the honest fix?
   > *Anchor:* Show the trend but also show the baseline. Contextualize the spike with "average failed logins = X, this week = Y× baseline."

2. **A chart of phishing reports by class period could let someone guess *which class* fell for them.** Same data, new risk. What changes?
   > *Anchor:* Aggregate to school-wide. If you must show by period, suppress periods with <5 reports (k-anonymity). Never publish identifiers.

3. **Your histogram showed days with unusually low login success rates.** Naming those **dates** in your write-up is more useful to your security team — and more dangerous to whoever caused them. Where is the line?
   > *Anchor:* Use "day 14" instead of "Oct 14" in analysis. Redact the exact date in public-facing versions; keep it in the internal security team version.

**There is no single right answer. There is a defensible one, and you have to be able to say why yours is defensible.**

---

## PART 3 — MY PRINCIPLE, REVISED (15 min)

In L19 you wrote a principle: "What is the one rule you will follow about making charts from data that is not yours?"

**Now, having reviewed three other projects, revise it.** One sentence. Hand in on paper.

---

## TURN IN (Google Classroom, due 23:59 tonight)

1. Your three completed honesty-audit tables (photo or typed)
2. Your revised principle (one sentence, on paper or in the submission box)
3. One sentence: which of the three projects you reviewed was most secure, and why?

---

## 📋 TOMORROW

**Next:** U2 L21 — Unit 2 Wrap & Transition to Unit 3. Reflection, journal, preview of Describing Data with Statistics.

---

## 🇹🇼 TAIWAN CONTEXT

The gallery walk is how the Taiwan CERT's own analysts review each other's threat reports before publication — not to find fault, but to find the *unintended implication*. A chart that says "phishing spiked in Period 3" sounds like operational intelligence until you realize it identifies a specific class of 28 students. The honest fix isn't censorship — it's aggregation with a footnote.