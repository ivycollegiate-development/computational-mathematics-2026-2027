# U2 L17b — Unit 2 Stress Test & Exam Strategy

**LO:** diagnose every Unit 2 topic, practice reading the verb, and complete a timed stress test.
**Estimated time:** 85 minutes (was ~65). We move slower so the diagnosis is real, not performative.
**Prerequisite:** U2 L16 (Project Lab) submitted. U2 L17 (Peer Review) done.

---

## PART 0 — TRAFFIC LIGHT DIAGNOSIS (15 min)

Open your journal. For each topic below, mark **🟢 Green** (I can teach it), **🟡 Yellow** (I can do it with notes), or **🔴 Red** (I would miss this on a test).

| Topic | 🟢/🟡/🔴 | Evidence (one specific thing you did) |
|-------|--------|----------------------------------------|
| Chart type ↔ data type matching (line/bar/scatter/hist) | | |
| Three-label rule (title, x, y) — every chart | | |
| `plt.plot` / `plt.bar` / `plt.scatter` / `plt.hist` key args | | |
| `plt.figure()`, `plt.legend()`, `plt.grid()`, `plt.clf()` | | |
| `savefig` BEFORE `show()` — why it matters | | |
| Honest axis: `plt.ylim(bottom=0)` for bars | | |
| `csv.DictReader` returns strings; every value is `str` | | |
| Comment-line bug: `#` first line → corrupted header | | |
| `newline=""` in `open()` — Windows blank-line bug | | |
| `writer` vs `DictWriter` — when to use each | | |
| `to_float` / `to_int` with `try/except (ValueError, TypeError)` | | |
| Sanity bounds dict: domain knowledge > statistical outliers | | |
| Cleaning loop: blank → unparseable → impossible → convert | | |
| `break` in each `if`; `continue` skips append | | |
| Audit assert: `rows_in == rows_out + rows_dropped` | | |
| Provenance statement: raw → clean → dropped + reasons | | |
| Blank-GPA bias: dropping missingness = dropping strugglers | | |
| Outlier vs signal: thin tail = real incidents, not noise | | |
| k-anonymity: suppress <5, aggregate, redact dates | | |
| Correlation ≠ causation: third variable, direction unknown | | |
| Audience-aware titles: jargon for security, plain for parents | | |
| `alpha` for density (1000 pts) vs visibility (6 pts) | | |
| Histogram vocab: center, spread, skew, outlier | | |
| Right-skew: mean > median, tail right | | |

**Your Reds are your study list.** Every Red becomes a practice problem in Part 2.

---

## PART 1 — VERB DRILL (10 min)

The #1 point loss on assessments: **answering a different question than asked.**

For each prompt, write **what the verb demands** (not the answer — just the *form* of the answer):

| Prompt | Verb demands... |
|--------|-----------------|
| "What happens when `float('banana')`?" | |
| "Why is `savefig` before `show()` critical?" | |
| "What does `alpha=0.3` change in `plt.grid()`?" | |
| "Name the exception raised by `int('3.5')`." | |
| "Why does dropping blank GPA bias the average upward?" | |
| "Rewrite the title for a parent audience." | |
| "What does the `break` do in the cleaning loop?" | |
| "Give one input that triggers `TypeError` in `to_float`." | |

**Rule:** "What" → value/word. "Why" → sentence. "What happens" → actual error/behavior (not the fix).

---

## PART 2 — STRESS TEST (25 min)

**Closed notes. 20 minutes. Swap and grade with the key — corrections in a second color.**

Do the **Unit 2 Practice Test (Version B)** — 50 points, 35 minutes.
[`Unit 2 - Visualizing Data/Assessments/Unit-2-Practice-Test-Version-B.md`](Unit-2-Practice-Test-Version-B.md)

**Print it double-sided.** Treat it exactly like the real test:
- No notes, no computer, no neighbors
- Write name + confident item + "hope not on test" on coversheet
- 35 minutes, then stop

After 35 minutes:
1. Swap papers with a partner
2. Grade with the answer key (teacher provides)
3. For every **miss**, correct it in a second color and write one line:
   > *What I had in my head vs what is true.*

Example: "I thought `savefig` after `show` was fine → actually `show()` closes the figure, PNG comes out blank."

---

## PART 3 — RED REPAIR (20 min)

For each **Red** from Part 0, do one of:

| If Red is... | Do this... |
|--------------|------------|
| Conceptual (e.g., "why sanity bounds?") | Write a 3-sentence explanation in your journal. Say it out loud to a partner. |
| Code syntax (e.g., "`plt.hist` args") | Type the minimal working example in the REPL. Run it. Break it. Fix it. |
| Verb confusion (e.g., "what vs why") | Re-write the missed stress-test item with the *correct* verb answer. |
| Chart choice (e.g., "when scatter vs line") | Draw the decision table from memory. Check against L05/L13 notes. |

**Goal:** Every Red → 🟢 by end of period. If not, that's your homework.

---

## PART 4 — EXAM STRATEGY CARD (10 min)

On an index card (or half-sheet), write your **personal exam strategy** — the 3-5 things *you* need to remember:

```
MY UNIT 2 EXAM CARD
1. Read the VERB first. What? → value. Why? → sentence.
2. savefig BEFORE show. Every time.
3. Honest axis: ylim(bottom=0) on ALL bar charts.
4. Sanity bounds = domain knowledge (impossible), not IQR (surprising).
5. Provenance: raw → clean → dropped + reasons + bias check.
6. k-anonymity: <5 suppress, aggregate, redact dates.
7. Correlation ≠ causation. Third variable. Direction unknown.
8. Blank PNG? savefig after show. Fix: move it up.
9. Overlapping xticks? rotation + tight_layout + [::step].
10. Proud of: ___________   Scared of: ___________
```

Keep this card. Review it the night before the test.

---

## PART 5 — JOURNAL (5 min)

In your journal file, answer:

1. Which **three Reds** from Part 0 are now 🟢? What did you do to fix each?
2. Which **one topic** is still 🔴? What will you do tonight?
3. One sentence: what does "answer the verb" mean to you now?

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:
1. Your Part 0 traffic light table (all topics marked)
2. Your Part 1 verb drill (completed)
3. Your Part 4 exam strategy card (photo or text)
4. Your Part 5 journal entries

Submit to the U2 L17b assignment on Google Classroom.

**Keep the terminal open** — spot-checks.

---

## WHY THIS MATTERS

**The test is not a surprise.** Every question type above appears on the real assessment. The stress test (Part 2) is the *same size and shape* as the real paper. The only difference: the real test has different numbers, different variable names, different CSV columns — but the *thinking* is identical.

**Students who do this lesson honestly** walk into the assessment knowing exactly what they know and what they don't. Students who performatively mark 🟢 on everything get the score their preparation earned.

**Your Reds are a gift.** They tell you where to spend your limited study time. Use them.

---

**Next:** U2 L18 — Project Final Push: Polish and Submit  
**Then:** U2 L19 — Unit 2 Assessment (half day) + Reflection