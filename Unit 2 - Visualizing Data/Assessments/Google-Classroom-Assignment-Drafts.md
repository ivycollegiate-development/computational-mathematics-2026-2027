# Unit 2 Google Classroom Assignment Drafts (DRAFT — Do Not Post Yet)

**Course:** Computational Mathematics Period E  
**Unit:** 2 — Visualizing Data  
**Status:** All assignments in DRAFT state. Review, then click "Assign" when ready.

---

## ASSIGNMENT 1: U2 L15 — Project Launch: Visualizing Threats

**Title:** U2 L15 — Project Launch: Visualizing Threats  
**Topic:** Unit 2: Visualizing Data  
**Points:** 20  
**Due:** Oct 28, 2026 at 23:59  
**Status:** DRAFT

### Instructions

Today is the **project launch day**. You chose a dataset on the break assignment (U2 L14 Part 3). Today you turn those sketches into a working repo and a clean dataset.

**Your audience is your choice** — security team, principal, or parents — but you must *say who it is* in your analysis, because that choice decides your titles, your wording, and what you highlight.

**Three required visualizations**, all built from **cleaned** data, each saved as a PNG, each with a 1-paragraph written analysis:
1. **Daily timeline** — line chart of `phishing_reports` and `failed_logins` over the dates. Does trouble spike on certain days? Do the two lines move together?
2. **Weekday vs weekend** — bar chart comparing average values on weekdays against weekends. Is the attack activity a school-week pattern?
3. **Login success rate** — histogram of `login_success_rate`. Where do most days sit, and are there suspicious outliers on the low end?

### Turn In — Screenshot (due 23:59)

1. Screenshot showing `clean_threats.py` terminal output (rows in/out/dropped counts).
2. Screenshot of `chart1_timeline.png` open in VS Code.
3. Your written claim and audience choice (photo of paper or text in a file).

Submit to this assignment.

**Keep the terminal open** — spot-checks happen.

### Rubric (20 pts)

| Criterion | 5 | 3 | 1 |
|-----------|---|---|---|
| Cleaning script runs, prints in/out/dropped | ✅ | ⚠️ partial | ❌ |
| Chart 1 exists, has title + both axis labels | ✅ | ⚠️ | ❌ |
| Claim written, audience named | ✅ | ⚠️ | ❌ |
| Repo pushed with clean script + chart1 | ✅ | ⚠️ | ❌ |

---

## ASSIGNMENT 2: U2 L16 — Project Lab: Build Your Visualizations

**Title:** U2 L16 — Project Lab: Build Your Visualizations  
**Topic:** Unit 2: Visualizing Data  
**Points:** 20  
**Due:** Oct 29, 2026 at 23:59  
**Status:** DRAFT

### Instructions

Full lab period to build **Charts 2 and 3** from your project plan. Continue from yesterday's `project_charts.py`.

**Chart 2 — Weekday vs Weekend Bar Chart:**
- Compute average `phishing_reports` (and/or `failed_logins`) for weekdays vs weekends
- Bar chart with two bars, different colors, legend if needed
- Title, x-label, y-label
- `plt.ylim(bottom=0)` — honest axis
- Save as `chart2_weekday_weekend.png`

**Chart 3 — Login Success Rate Histogram:**
- Histogram of `login_success_rate` with `bins=15`
- Title, x-label, y-label
- `edgecolor="white"` on bars
- Save as `chart3_success_rate.png`

**Analysis Draft:**
Write one paragraph per chart (three total). Each paragraph must:
- Name the audience and the one thing they should notice
- Contain **one honest limitation** (what the chart leaves out, or a caveat)

### Turn In — Screenshot (due 23:59)

1. Terminal showing `python3 project_charts.py` ran with no errors.
2. All three PNGs visible in VS Code (`chart1`, `chart2`, `chart3`).
3. Draft `analysis.md` with three paragraphs.

### Rubric (20 pts)

| Criterion | 5 | 3 | 1 |
|-----------|---|---|---|
| Chart 2: correct, labeled, honest axis | ✅ | ⚠️ | ❌ |
| Chart 3: correct bins, labeled | ✅ | ⚠️ | ❌ |
| Analysis: 3 paragraphs, audience + limitation each | ✅ | ⚠️ | ❌ |
| Code clean, comments, `plt.clf()` between charts | ✅ | ⚠️ | ❌ |

---

## ASSIGNMENT 3: U2 L17 — Peer Review of Visualizations

**Title:** U2 L17 — Peer Review of Visualizations  
**Topic:** Unit 2: Visualizing Data  
**Points:** 15  
**Due:** Oct 30, 2026 at 23:59  
**Status:** DRAFT

### Instructions

**Structured peer review.** You read a partner's repo, score all three charts on three dimensions, then revise one chart from their feedback.

**Three scoring dimensions (1–5 each):**
- **Clarity** — I understood the chart with no explanation. Title, labels, legend all do their job.
- **Honesty** — The chart says exactly what the data says. No dropped context, no inflated axes, no hidden gaps. Y-axis starts at 0 (or states why not). Missing data acknowledged.
- **Impact** — The one thing the audience should notice jumps out immediately. The chart has a *point*, not just data.

### Process

1. Get partner's repo link (GitHub URL from PR). Clone or read on github.com.
2. For **each chart**, fill out the feedback form in your notes (scores + specific actionable suggestion).
3. Swap roles.
4. **Revise one chart** from your partner's suggestion (or defend why you disagree in your journal).
5. Commit and push the revision.

### Turn In — Screenshot (due 23:59)

1. Your completed feedback forms (all three charts, scores + suggestion).
2. Your revised chart's new PNG.
3. The successful `git push`.

### Rubric (15 pts)

| Criterion | 5 | 3 | 1 |
|-----------|---|---|---|
| All 3 charts scored on all 3 dims with "because" | ✅ | ⚠️ | ❌ |
| One specific, actionable suggestion per chart | ✅ | ⚠️ | ❌ |
| Revision made + pushed (or defended in journal) | ✅ | ⚠️ | ❌ |

---

## ASSIGNMENT 4: U2 L17b — Unit 2 Stress Test & Exam Strategy

**Title:** U2 L17b — Unit 2 Stress Test & Exam Strategy  
**Topic:** Unit 2: Visualizing Data  
**Points:** 10 (completion)  
**Due:** Nov 2, 2026 at 23:59  
**Status:** DRAFT

### Instructions

**Diagnostic day.** No new material — you find your gaps before the assessment.

**Part 0 — Traffic Light Diagnosis (15 min)**
Mark every Unit 2 topic 🟢 (can teach), 🟡 (with notes), 🔴 (would miss on test).

**Part 1 — Verb Drill (10 min)**
Practice reading the verb: "What" → value, "Why" → sentence, "What happens" → actual error.

**Part 2 — Stress Test (25 min)**
Timed: **Unit 2 Practice Test Version B** (50 pts, 35 min, closed notes). Swap and grade with key.

**Part 3 — Red Repair (20 min)**
For each 🔴 from Part 0: write explanation, type code in REPL, or re-write missed item.

**Part 4 — Exam Strategy Card (10 min)**
Write your personal 3-5 reminders on an index card.

**Part 5 — Journal (5 min)**
Three Reds now 🟢, one still 🔴 + plan, what "answer the verb" means to you.

### Turn In — Screenshot (due 23:59)

One screenshot showing, in order:
1. Part 0 traffic light table (all topics marked)
2. Part 1 verb drill (completed)
3. Part 4 exam strategy card (photo or text)
3. Part 5 journal entries

Submit to this assignment.

### Grading

Completion only (10 pts). The value is the diagnosis — your Reds tell you what to study.

---

## ASSIGNMENT 5: U2 L18 — Project Final Push: Polish and Submit

**Title:** U2 L18 — Project Final Push: Polish and Submit  
**Topic:** Unit 2: Visualizing Data  
**Points:** 40 (project total)  
**Due:** Nov 14, 2026 at 23:59 (Common Good Day)  
**Status:** DRAFT

### Instructions

**Last working day on the project.** No new building — you make what you have **correct, complete, and honest**.

### Part 0 — Self-Audit (20 min)

Run your code. Grade yourself honestly against the rubric. **Tick only if true, not nearly true.**

**Data Integrity:**
- ☐ `project_charts.py` runs start to finish with **no error output**
- ☐ Prints row count before/after cleaning
- ☐ I can state exactly how many rows dropped and why (blank, impossible, unparseable — by column)
- ☐ Dates parse in chronological order

**Three Required Charts:**
- ☐ `chart1_timeline.png` exists, has title + both axis labels
- ☐ `chart2_weekday_weekend.png` exists, has title + both axis labels
- ☐ `chart3_success_rate.png` exists, has title + both axis labels
- ☐ I chose histogram bins **on purpose** and can say why
- ☐ Every chart's code has a one-line comment

**Analysis (`analysis.md`):**
- ☐ One paragraph per chart (three total)
- ☐ Each names audience + one thing they should notice
- ☐ Each contains **one honest limitation**
- ☐ I did not claim anything the chart does not show

**Honesty Audit (do last, seriously):**
1. Does my y-axis start at zero? If not, do I **say why** in `analysis.md`?
2. Did I drop rows that would make my story less dramatic? Why was dropping correct — did I say so?
3. Is there anything I chose not to plot? A careful reader would notice. Say so yourself.

### Part 1 — Fix What Is Wrong (50 min)

Order: 1) Does it run? 2) Are numbers true? 3) Do labels tell truth? 4) Polish.

If a chart is missing → document the gap in `analysis.md`. A **documented gap is honest. A silent gap is a lie.**

### Part 2 — Final Submission (15 min)

```bash
git add project_charts.py analysis.md
git add chart1_timeline.png chart2_weekday_weekend.png chart3_success_rate.png
git commit -m "final: three visualizations with analysis"
git push
```

Update your Pull Request (don't open a second one). Verify on github.com:
- ☐ `project_charts.py` is latest version
- ☐ All three PNGs visible and render
- ☐ `analysis.md` shows three paragraphs
- ☐ PR page shows latest commit

### Turn In — Pull Request Link (due 23:59)

One submission showing:
1. Completed self-audit checklist + honesty audit answers
2. Final `git push` confirmation
3. Updated PR page on github.com with latest commit visible

### Rubric (40 pts)

| Criterion | Points |
|-----------|--------|
| Data integrity: clean script, audit print, known drops | 8 |
| Chart 1: timeline, correct, labeled, honest axis | 6 |
| Chart 2: weekday/weekend bar, correct, labeled, honest axis | 6 |
| Chart 3: histogram, bins chosen intentionally, labeled | 6 |
| Analysis: 3 paragraphs, audience + limitation each | 8 |
| Honesty audit: all 3 questions answered in writing | 6 |
| **Total** | **40** |

---

## ASSIGNMENT 6: U2 L19 — Unit 2 Assessment + Reflection

**Title:** U2 L19 — Unit 2 Assessment + Reflection  
**Topic:** Unit 2: Visualizing Data  
**Points:** 50 (assessment) + 10 (reflection) = 60  
**Due:** Nov 16, 2026 (in class, second day back from Fall Break)  
**Status:** DRAFT

### Instructions

**Half day — Assessment administered on the second day back from Fall Break, then reflection.**

**Part 0 — Paper Assessment (35 min, 50 pts)**
- Closed computer. No terminals, no notes, no neighbors.
- Covers: chart taxonomy, matplotlib, CSV pipeline, sanity bounds, data integrity, honesty audit.
- Format mirrors Unit 1: 4 sections (Short Response 20, Code Reading 10, Data Integrity 10, Write Code 10).
- Coversheet: name + confident topic + "hope not on test."

**Part 1 — Reflection: What Makes a Secure Visualization? (35 min, 10 pts)**
After the paper, open your journal and answer:

1. **What is the one principle from Unit 2 you will use every time you visualize data?** (3–4 sentences, specific)
2. **Give an example from your project where you caught a dishonest choice before it shipped.** What was it, and what did you change? (3–4 sentences)
3. **What would you tell a new student on Day 1 of Unit 2?** One paragraph.

### Turn In

- **Paper:** Hand in at end of assessment period.
- **Reflection:** Submit to this assignment by end of class (or 23:59 if you need more time).

### Grading

Assessment scored via bands:
| Score | Band | Next Step |
|-------|------|-----------|
| 45–50 | Mastery | Proceed to Unit 3 |
| 35–44 | Approaching | One conversation: review weak sections |
| 25–34 | Developing | Reteach session + alternate retake |
| <25 | Beginning | Full unit review + 1-on-1 |

Reflection (10 pts): specificity + evidence from your project.

---

## ASSIGNMENT 7: U2 Review Packet (Optional / Extra Practice)

**Title:** U2 Review Packet — Practice Tests + Keys (Optional)  
**Topic:** Unit 2: Visualizing Data  
**Points:** 0 (ungraded)  
**Due:** Nov 15, 2026 at 23:59  
**Status:** DRAFT

### Instructions

**Optional practice materials** — use them or don't, but the students who do the stress test honestly score higher on the real assessment.

**Contains:**
1. **150% Practice Test** (75 pts, 50 min) — diagnostic, find your Reds
2. **Practice Test Version B** (50 pts, 35 min) — dress rehearsal, same shape as real test
3. **Answer Keys** for both (teacher copy — use after you finish each test)
4. **Quick Reference** — chart decision table, matplotlib cheatsheet, CSV pipeline, verb drill

### How to Use

1. **This week:** Do the 150% test untimed. Mark every problem "got it" / "not yet." Your "not yet" = study list.
2. **L17b (Stress Test day):** Do Version B timed (35 min). Swap and grade. Compare to 150% results.
3. **Weekend before assessment:** Re-do your "not yet" items from both keys. Bring questions to FLEX Day (Nov 13).

### Files

All materials in `Unit 2 - Visualizing Data/Assessments/` folder on Drive:
- `Unit-2-Practice-Test-150.md` (student version)
- `Unit-2-Practice-Test-Version-B.md` (student version)
- `Unit-2-Practice-Test-150-Answer-Key.md` (teacher only)
- `Unit-2-Practice-Test-Version-B-Answer-Key.md` (teacher only)
- `Unit-2-Review-Packet.docx` (this packet, printable)

---

## POSTING ORDER (Recommended)

| Date | Assignment | Notes |
|------|------------|-------|
| Oct 26 (Mon) | U2 L15 Project Launch | Post morning of |
| Oct 27 (Tue) | U2 L16 Project Lab | Post morning of |
| Oct 28 (Wed) | U2 L17 Peer Review | Post morning of |
| Oct 29 (Thu) | U2 L17b Stress Test | Post morning of |
| Oct 30 (Fri) | U2 L18 Final Push | Post morning of; due Nov 14 |
| Nov 13 (Fri) | U2 Review Packet | Post FLEX Day for weekend study |
| Nov 16 (Mon) | U2 L19 Assessment | Post day of (in-class) |

---

## REVIEW CHECKLIST BEFORE POSTING

- [ ] All due dates match corrected lesson plan sheet
- [ ] Points match rubrics in lesson plans
- [ ] "Typhoon Day" (Oct 23) noted — no assignment that day
- [ ] Fall Break (Nov 4–12) — no assignments due
- [ ] Assessment on Nov 16 (second day back) — not Nov 3
- [ ] Project final due Nov 14 (Common Good Day) — PR link
- [ ] All links to Drive files work (student vs teacher folders)
- [ ] Rubrics use language from lesson plans (honest axis, sanity bounds, provenance)