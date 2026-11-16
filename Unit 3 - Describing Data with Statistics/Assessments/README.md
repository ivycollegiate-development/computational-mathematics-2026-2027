# Unit 3 Assessments

## The paper

[`Unit-3-Assessment.md`](Unit-3-Assessment.md) — 50 points, 45 minutes, closed book, no computer, pen and paper only.

**Print double-sided, one per student, before class.** Coversheet is on page 1.

| Section | Points | Covers |
|---|---|---|
| A — Centres & Spread | 10 | mean/median/mode and which is honest under an outlier; range, variance, sample stddev; spec conformance from mean and sd alone |
| B — Percentiles & Outliers | 10 | `(n−1)·p` interpolation at integer k; five-number summary; IQR fences; what moves when the outlier is dropped |
| C — Misleading Statistics & Privacy | 20 | misleading mean vs median; direct vs quasi-identifiers; counting equivalence classes and choosing a generalisation to reach k = 5; the publish/refuse decision and the reply to a stakeholder |
| D — Write Code | 10 | `five_number(v)` — no caller mutation, clamped index, survives n = 1 |

### Why the weighting is 34 / 46 / 20 and not the old 60 / 20 / 20

v1 of this paper gave 30 of 50 points to hand computation and roughly 5 to privacy. The unit's distinctive claim — that a student knows what a dataset may be used to say, and will refuse to publish a re-identifying table — was worth 10% of the grade. v2 moves 10 points out of A/B and into C, adds an equivalence-class counting item (C3) and a stakeholder-refusal item (C4), and drops the duplicated "what does sd add" prompt from A2. Hand computation is still assessed here and four more times formatively (L07, L11, L16, L22 paper checks).

## The key

`Unit-3-Assessment-Answer-Key.md` — same folder, **gitignored and teacher-only** (this repo is public, so no answer key is ever committed). Full worked solutions, per-item point allocations, common wrong answers, and marking traps. Every number verified computationally.

Because the key is not in the repo, it is not on the school Drive either yet — copy it there if you want it available away from the Mac mini.

## Marking for evidence, not just for a grade

Marks go in the gradebook as a total. The same marks should also go into an item-level capture sheet, because a total tells you nothing you can reteach from.

Item map and capture sheet (per-item points, strand tags, LO tags):

```
~/Projects/compmath-program-assessment/u3-evidence/U3-Assessment-Item-Map.csv
~/Projects/compmath-program-assessment/u3-evidence/U3-Assessment-Capture-Sheet.csv
```

Analysis, one command after the sheet is filled:

```
python3 ~/Projects/compmath-program-assessment/u2-evidence/u2_item_analysis.py \
  ~/Projects/compmath-program-assessment/u3-evidence/U3-Assessment-Capture-Sheet.csv
```

It prints item difficulty, strand means, students below 60%, and a ranked reteach queue. Items at p ≥ 0.95 are flagged as giving no information; items at p ≤ 0.35 are flagged as a teaching problem before an item problem.

## Known item properties

- **C3 and C4** carry the most diagnostic weight on the paper. Report them separately even if everything else is pooled.
- **B1** lands exactly on an integer k, so the interpolation weight is zero. Students who interpolate correctly and students who notice the zero both get full credit — do not treat "12 with no interpolation" as a shortcut.
- **A2** accepts either variance convention as long as the student states which one.
