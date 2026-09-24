# U2 L12 — Paper Check: Relationships and Clean Data

**LO:** demonstrate, on paper, mastery of scatter plots and data cleaning from U2 L10–L11 before the unit project.

No electronics today. Monday you clean data (U2 L11); Wednesday histograms; then the
project. Today's paper check makes sure scatter-plot reading and the
cleaning rules from this week are solid before everything builds on them.
20 minutes of check, then swap, correct, and one forward look at the project.

## PART 1 — THE CHECK (20 min, closed notes)

Answer on the check sheet. One point each unless marked.

**Section A — Reading relationships.** (from U2 L10)

1. Name the three relationship types a scatter plot can show.
2. In a scatter with `alpha=0.4`, what does a *darker region* of dots mean?
3. Your scatter shows study hours and GPA rising together. Your partner says
   "studying causes the GPA." Give one *other* explanation that fits the same
   picture.
4. Why do we set `s=10` and `alpha=0.4` when plotting 1,000 students, but not
   for 6 class averages?

**Section B — Cleaning rules.** (from U2 L11)

5. A cell is blank. Name the two choices you have and one tradeoff of each.
6. Why is a GPA of 9 rejected by sanity bounds while a GPA of 0.5 is kept?
7. Why does `to_float` return `None` instead of letting the crash happen?
8. Your cleaning drops 50 of 1,000 rows. What does that quietly change about
   every chart you build afterward?

**Section C — Predict the output.** (from U2 L10–L11)

9. What does `plt.clf()` do between two plots — and what goes wrong with your
   second `savefig` if you skip it?
10. `csv.DictReader` gives you an Age value of `"14"`. What type is it, and
    what must happen before it can be compared to a sanity bound?

**Section D — One fix-it.** (2 points)

11. This cleaner has two bugs. Name both:

```python
SANITY = {"Overall GPA": (0.0, 4.0)}
rows = list(csv.DictReader(f))       # f is the raw file
for r in rows:
    gpa = float(r["Overall GPA"])
    if not (0.0 <= gpa <= 4.0):
        rows.remove(r)
```

(Hint: think about what `float()` does on a blank cell, and what removing
items from a list does to a `for` loop over that same list.)

## PART 2 — SWAP AND GRADE (10 min)

Trade papers with your partner. Using the key I project, mark each answer and
write the score at the top. Both names go on the paper you graded.

## PART 3 — CORRECTIONS (15 min)

Take your own paper back. Correct every miss **in a different color**, and
for each miss write one line: *what I had in my head* vs *what is true*. A
corrected miss is worth more than a lucky guess.

## PART 4 — WHAT THE CHECK TELLS US (10 min, class discussion)

Hands up by section: which section was hardest? We re-teach the top one on
the board, using your actual wrong answers, before the project starts.

## PART 5 — LOOK AHEAD: THE PROJECT (10 min, in pairs)

Wednesday is histograms; Friday the project launches — three visualizations
built from a real dataset, with cleaning you do yourself. In your notes:

- Your project chart must survive the question "where did this data come
  from?" Write the one-sentence provenance statement you would make for the
  student-performance dataset, including how many rows it had before and
  after cleaning.
- Predict: which is more dangerous to a chart — a blank cell or an impossible
  value? Defend your choice; we compare answers Wednesday.

## TURN IN — PAPER (collected at the end of class)

One check sheet with: your Part 1 answers, your partner's grading marks, and
your corrections in a second color. Hand it in before you leave.

Submit a photo of the corrected check sheet to this assignment on Google
Classroom by 11:59 PM tonight.
Keep the sheet — it is your study guide for the unit project and assessment.

Next: U2-L13-Histograms-And-Distributions.md