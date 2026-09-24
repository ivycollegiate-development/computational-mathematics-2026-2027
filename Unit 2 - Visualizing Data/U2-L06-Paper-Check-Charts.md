# U2 L06 — Paper Check: Charts So Far

**LO:** demonstrate, on paper, mastery of good-visualization criteria and matplotlib customization from U2 L03–L05.

No electronics today. Monday's lab (U2 L07) puts bar charts on real data;
today's paper check makes sure the fundamentals from last week are solid
before you build on them. 20 minutes of check, the rest of class we go over
it together and you correct your own paper in a different color.

## PART 1 — THE CHECK (20 min, closed notes)

Answer on the check sheet. One point each unless marked.

**Section A — Which chart?** (from U2 L03 and L05)

1. You want to show how one value changes as another increases, day by day.
   Which chart type, and why?
2. You want to compare an average score across three sleep groups. Which
   chart type?
3. You want to see whether two number columns are related. Which chart type?

**Section B — The label rule.** (from U2 L05)

4. Write the rule from L05 about what every plot must have — all three parts.
5. A chart has a title and an x-label but no y-label. What can a reader not
   tell from it?

**Section C — Predict the output.** (from U2 L05)

6. What does `plt.grid(True, alpha=0.3)` do to the grid lines?
7. In `plt.scatter(hours, gpa, s=40)`, what does `s=40` control?
8. You call `plt.savefig("c.png")` *after* `plt.show()`. What is wrong with
   the saved file, and what is the correct order?

**Section D — One fix-it.** (2 points)

9. This code has two bugs. Name both:

```python
plt.bar(["Low", "Mid", "High"], [70.2, 78.5, 83.1])
plt.title("Average Score by Sleep Group")
plt.savefig("sleep.png")
plt.legend()
```

(Hint: run it in your head — what does `legend()` show when nothing was ever
given a `label=`, and what axis has no name?)

## PART 2 — SWAP AND GRADE (10 min)

Trade papers with your partner. Using the key I project, mark each answer and
write the score at the top. Both names go on the paper you graded.

## PART 3 — CORRECTIONS (15 min)

Take your own paper back. Correct every miss **in a different color**, and
for each miss write one line: *what I had in my head* vs *what is true*. The
corrections are the point — a corrected miss is worth more than a lucky guess.

## PART 4 — WHAT THE CHECK TELLS US (10 min, class discussion)

Hands up by section: which section was hardest? We re-teach the top one on
the board before Monday's lab, using your actual wrong answers — that is
what the check is for.

## PART 5 — LOOK AHEAD: MONDAY'S LAB (10 min, in pairs)

Monday you load the real study-habits dataset and build bar charts of
categorical data. In your notes:

- What is a *categorical* column, versus a *numerical* one? Name one of each
  from the study-habits preview you saw in L05 (students, study, scores,
  sleep).
- Predict: which column from that preview would make the most useful bar
  chart, and which could a bar chart not show at all? Why?

## TURN IN — PAPER (collected at the end of class)

One check sheet with: your Part 1 answers, your partner's grading marks, and
your corrections in a second color. Hand it in before you leave.

Submit a photo of the corrected check sheet to this assignment on Google
Classroom by 11:59 PM tonight.
Keep the sheet — it is your study guide for the Unit 2 assessment.

Next: U2-L07-Lab-Bar-Charts-And-Categorical-Data.md