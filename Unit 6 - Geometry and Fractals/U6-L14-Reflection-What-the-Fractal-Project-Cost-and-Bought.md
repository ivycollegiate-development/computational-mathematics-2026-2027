# U6 L14 — Reflection: What the Fractal Project Cost and Bought

**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.1–6.7 — assess your own work and the unit's ideas in writing

---

**No laptop.** Pencil. Your project is done. Today is about looking at it.

This is the last reflective lesson of the year — the unit ends tomorrow. So
this is a whole-unit assessment as much as a project one.

## PART 1 — THE IDEA, IN YOUR OWN WORDS (10 min)

No notes. If you need notes, that is the answer.

1. In one sentence, what is a **fractal**? ______
2. In one sentence, what does a **fractal dimension** measure? ______
3. Give the Koch curve's dimension, exactly: ______
4. Give the Sierpinski triangle's dimension, exactly: ______
5. Why is Koch's `log2(3)` not an integer, and what would an integer have
   meant? ______
6. Box counting: describe the method in two sentences. ______
7. Why does box counting overestimate a solid circle? ______

- ☐  How many of the seven did I get without notes? ______ / 7
- ☐  The ones I needed notes for: ______

## PART 2 — AUDIT THE PROJECT (15 min)

Be your own worst reviewer. This is the part that is worth points.

Your detector misclassified four of eight cases. Answer honestly:

1. Which misclassification would you have shipped if you had not been asked to
   find it? ______
2. **The circle scoring 1.79 is a systematic error, not noise.** In one
   paragraph, explain the mechanism: ______________________________________
   ______________________________________________________________________
3. Is there a **cheap fix** for the circle problem, or is it fundamental to box
   counting? Justify whichever you claim. ______
4. The random-noise cases: is there a cheap fix? ______
5. **Which of your four misclassifications could you have caught by looking at
   the answer rather than the method?** ______

Question 5 is the one that generalises. A detector that says "STRUCTURED" for
a solid circle is not a subtle failure; it is a failure you would spot by
printing the top two or three cases and *looking at them*. How much of your
review time was numerical and how much was visual? ______

## PART 3 — THE UNIT, HONESTLY (10 min)

6. Which idea from this unit will still matter to you in a year? ______
7. Which one will you have forgotten? ______
8. Name one thing you believed at the start of April that you no longer
   believe: ______
9. The unit opened by saying **a coordinate is a claim, not a truth**. Has that
   changed how you read any number? ______
10. Name a real security system you have interacted with this month whose
    output you now read differently: ______

Numbers 9 and 10 are the real test of the unit. If you cannot name a specific
number you now read more carefully, the geometry did not land.

## PART 4 — THE ERROR LOG, WHOLE UNIT (10 min)

Open the **Geometry Error Log** — every entry since April 12.

- ☐  Total errors logged: ______
- ☐  By tag:

| tag | count |
|---|---|
| sign | |
| subtraction order | |
| formula | |
| float form | |
| careless | |
| off-by-one | |
| base case | |
| recursion depth | |
| measurement | |
| threshold | |
| reasoning | |
| recall | |

- ☐  Most common tag: ______
- ☐  Most expensive tag: ______ (the one that cost the most time)
- ☐  Which tag do you think you will still be making in five years? ______
- ☐  **Write one sentence to yourself** about the tag you will still be making.
     This is the sentence that will work.

## 错误日誌最後一題

用一句話寫給五年後的自己，關於你最常犯的那一類錯誤：

______________________________________________________________________

## 🇹🇼 TAIWAN CONTEXT

The idea in Part 2.5 — that some failures are visible if you print the results
and look — is the most transferable thing in this unit, and it has a
particularly sharp local edge. In a SOC or an operations centre, the standard
practice of eyeballing a sample of what an alert fired on is not busywork; it is
how you discover that a rule is systematically misfiring on a benign pattern.
A tool that fires reliably on both the true case and a common innocent case is
not telling you two things. It is telling you one thing badly, and the second
signal is noise you generated yourself. Every serious detection review I know of
builds in the "print three examples and actually look at them" step, because it
catches more real problems than any additional tuning.

**Next:** L15, Apr 30 — demo day and unit wrap. Bring your laptop, your
one-page defense, and your error log.
