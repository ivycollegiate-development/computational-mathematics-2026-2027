# Unit 2 Assessments

## The paper

[`Unit-2-Assessment.md`](Unit-2-Assessment.md) — 50 points, 35 minutes,
closed computer, pen and paper only.

**Print double-sided before class.**

| Section | Points | Covers |
|---|---|---|
| A — Short Response | 20 | 10 questions: chart-type taxonomy, matplotlib syntax (`plot`/`bar`/`scatter`/`hist` args), `csv.DictReader` behavior, comment-line bug, sanity bounds vs outliers, `figure`/`savefig`/`show` order |
| B — Code Reading | 10 | Problem 11 (cleaning loop: blanks, unparseable, sanity bounds, `break`/`continue`, audit assert); Problem 12 (timeline chart: blank-PNG bug, honest axis, tick overlap, audience-aware title) |
| C — Data Integrity & Honesty | 10 | Provenance statement, blank-GPA bias, outlier vs signal, k-anonymity / aggregation fix |
| D — Write Code | 10 | `load_and_clean(csv_path, sanity_dict)` — strip comments, convert, apply bounds, print drops, audit assert |

Do not deviate from the printed paper. The coversheet carries the student's name,
their confident item, and the "one thing I hope is NOT on the test" note that
tells us where to spend Unit 3 review time.

## The key

[`Unit-2-Assessment-Answer-Key.md`](Unit-2-Assessment-Answer-Key.md) — **teacher
copy, do not distribute to students.** Per-item point splits, model answers,
the Section D rubric (`eval()` is an automatic zero for the question), and
grading bands that route each score range to reteach or proceed.

**Source markdown:** `~/Projects/compmath-answer-keys/Unit-2-Assessment-Answer-Key.md`  
**Deliverable GDoc:** School Drive → Unit 2 folder (built via `build_gdoc_from_md_with_real_tables.py` → `postbuild_finisher.py`)

## Where this sits in the sequence

Lesson files carry no dates, so this is the ordering reference for the end
of Unit 2:

| Lesson | Role |
|---|---|
| `U2-L17-Reflection-Peer-Review-Of-Visualizations.md` | Diagnose — traffic-light every topic, your Reds become the study list |
| `U2-L18-Project-Final-Push-Polish-And-Submit.md` | Consolidate — project submission, final integrity audit |
| `U2-L19-Reflection-Unit-2-Wrap-What-Makes-A-Secure-Visualization.md` | Repair — synthesize three pillars, write personal principle |
| **This assessment** | **The paper** — administered on the U2-L19 lesson day (Nov 3, half day) |
| `U3-L01-Introduction.md` | Unit 3 begins |

The assessment is administered during the U2-L19 lesson period (Unit 2 Wrap,
half day). It assesses Unit 2 content (L02–L19 + project).

## A note on keys

This repo is **public**. Every `*-Answer-Key*.md` file is gitignored on purpose
— a student can clone this and read the key. Keys live in the school Google
Drive, not here. If you add a key to this folder it will not be committed, which
is correct; copy it to Drive instead.