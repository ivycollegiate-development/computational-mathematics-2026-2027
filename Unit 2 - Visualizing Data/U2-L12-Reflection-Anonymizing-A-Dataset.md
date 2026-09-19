# U2 L12 — Reflection: Anonymizing a Dataset

**LO:** understand what makes data personally identifiable (PII) and how to anonymize it.

Today starts on paper and ends in the terminal — you will need your workspace
for Parts 3 and 5. No charts today. Today's question: when we share a dataset,
what are we actually sharing about the people inside it?

## PART 1 — OPENING REVIEW: WHAT HAPPENED YESTERDAY (10 min)

Before anything new, let's reconstruct Wednesday's lesson (U2 L11 — Data
Integrity and Clean Data).

Answer these together before I show any code:

- What are the two choices you have for a blank cell, and what is the
  tradeoff between them?
- What is a sanity bound, and why does it reject a GPA of 9 but keep a GPA
  of 0.5?
- Why did `to_float` return `None` instead of crashing?
- Your clean CSV dropped rows. What does that quietly change about every
  chart you make from it?

Write your answers in your notes first; then we go over them as a class. By
the end of this part you should be able to say in one sentence: **cleaning
changes the sample, so every cleaning decision is a judgment call.**

## PART 2 — WHAT IS PII? (15 min)

**Personally Identifiable Information** is any data that can be tied back to a
specific person. In small groups, sort these into "obviously PII" and
"probably not PII" — then defend the hard ones:

- a student's name
- a student ID number
- home address, phone number, email
- a photo
- age, gender, grade level
- a GPA
- a list of extracurricular activities

The uncomfortable part: **a single column is rarely the danger — combinations
are.** Age + gender + ZIP code narrows a population fast. Write in your notes:
which *pair* of columns from our list, combined, would most easily identify
one student in a school of 400?

## PART 3 — LOOK AT OUR OWN DATASET (10 min)

Open your terminal and look at what you have been carrying around all week:

```bash
pwd
cd ~/compmath-u2-data-lab
head -3 data/u2_student_performance_data.csv
```

(In Codespaces use `head -3 ...` in the terminal; in VS Code just open the
file and read the first three rows.)

In your notes, classify every column of this file: direct identifier,
quasi-identifier (helps narrow someone down when combined), or harmless
attribute. Then answer:

- What does "Student ID" protect, and what does it *not* protect?
- Why is it lucky — or not — that our file has no names in it?

## PART 4 — QUASI-IDENTIFIERS AND k-ANONYMITY (15 min)

A **direct identifier** points at one person all by itself (name, ID, email).
A **quasi-identifier** is innocent alone but identifying in combination:
birth date + ZIP code + gender once narrowed the US population to an average
of a single person — that is a real published result, not a thought
experiment.

**k-anonymity** is the standard idea for defense, and the definition fits in
one line: *a dataset is k-anonymous if every combination of
quasi-identifiers appears at least k times.* In other words — any row you
point at, there are at least k−1 other rows it could have been.

In small groups, using the 4-column mental-health-style dataset I'll put on
the board (Stress_Level, Hours_Exercise, GPA, Social_Hours):

- Which columns are quasi-identifiers?
- What happens to identification risk if we round GPAs from two decimals to
  one (3.87 → 3.9)?
- What is the largest k we could honestly claim after that rounding?

Write your group's answers in your notes. The lesson: **anonymity is bought
by blurring precision, and each blur costs some usefulness.** There is no
free lunch — a fully anonymous dataset with k=1000 says almost nothing.

## PART 5 — JOURNAL: ANONYMIZING A SCHOOL DATASET (10 min)

```bash
cd ~/compmath-u2-data-lab
touch journal-1022.md
```

Open `journal-1022.md` in VS Code. Imagine the school hands you a real
dataset for a project: every student, with name, Student ID, grade, GPA,
absence rate, and activities. You want to share it publicly for a class
project. Answer in 4–5 sentences:

- Which columns do I remove entirely, and why?
- Which columns do I blur (round, bucket, or group), and by how much?
- What k would I be comfortable claiming, and what does that cost us?
- One thing I now realize I have shared, or seen shared, too casually.

## PART 6 — PUSH (last 5 min — same loop as Monday)

Your journal is already inside your repo, so push it. Type each command exactly:

```bash
cd ~/compmath-u2-data-lab
git add journal-1022.md
git commit -m "Day 1022 journal: anonymizing a dataset"
git push
```

- **Asked for a username/password?** Use your GitHub username plus your
  Personal Access Token (PAT) — never your GitHub password.
- **Success?** You should see a push confirmation line.

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. your `head -3` output from Part 3 (the dataset columns on screen)
2. your journal answers open in VS Code
3. the successful `git push`

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.
