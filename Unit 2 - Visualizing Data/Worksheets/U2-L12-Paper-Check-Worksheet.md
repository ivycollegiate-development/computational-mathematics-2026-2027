# U2 L12 — Paper Check: Relationships and Clean Data

Names: ___________________________  Date: Oct 23

Closed notes. 20 minutes, then swap, grade with the key, and correct every miss in a second color. Next week the project builds on everything this checks.

## 1: The check

Section A — Reading relationships

1. Name the three relationship types a scatter plot can show:

______________________________  ______________________________  ______________________________

2. In a scatter with alpha=0.4, what does a DARKER region of dots mean?

_________________________________________________________________________

3. Your scatter shows study hours and GPA rising together. Your partner says "studying causes the GPA." Give one OTHER explanation that fits the same picture.

_________________________________________________________________________

4. Why do we set s=10 and alpha=0.4 when plotting 1,000 students, but not for 6 class averages?

_________________________________________________________________________

Section B — Cleaning rules

5. A cell is blank. Name the two choices you have and one tradeoff of each.

_________________________________________________________________________

_________________________________________________________________________

6. Why is a GPA of 9 rejected by sanity bounds while a GPA of 0.5 is kept?

_________________________________________________________________________

7. Why does to_float return None instead of letting the crash happen?

_________________________________________________________________________

8. Your cleaning drops 50 of 1,000 rows. What does that quietly change about every chart you build afterward?

_________________________________________________________________________

Section C — Predict the output

9. What does plt.clf() do between two plots — and what goes wrong with your second savefig if you skip it?

_________________________________________________________________________

10. csv.DictReader gives you an Age value of "14". What type is it, and what must happen before it can be compared to a sanity bound?

_________________________________________________________________________

Section D — One fix-it (2 points)

11. This cleaner has two bugs. Name both:

   SANITY = {"Overall GPA": (0.0, 4.0)}

   rows = list(csv.DictReader(f))       # f is the raw file

   for r in rows:

       gpa = float(r["Overall GPA"])

       if not (0.0 <= gpa <= 4.0):

           rows.remove(r)

Bug 1: ______________________________________________________________

Bug 2: ______________________________________________________________

## 2: Swap and grade

Graded by: ___________________________  Score: ________ / 14

## 3: Corrections

For each miss, correct it in a second color and write one line: what I had in my head vs what is true.

_________________________________________________________________________

_________________________________________________________________________

_________________________________________________________________________

## 4: Look ahead — the project

Monday is histograms; Wednesday the project launches — three visualizations built from a real dataset, with cleaning you do yourself.

Write the one-sentence provenance statement you would make for the student-performance dataset, including how many rows it had before and after cleaning:

_________________________________________________________________________

_________________________________________________________________________

Predict: which is more dangerous to a chart — a blank cell or an impossible value? Defend your choice.

_________________________________________________________________________

_________________________________________________________________________

## Hand-in

☐  Check sheet completed, graded by partner, corrections in a second color.

☐  Photo of the corrected check sheet submitted to the Classroom assignment by 11:59 PM tonight.

Keep the sheet — it is your study guide for the unit project and assessment.
