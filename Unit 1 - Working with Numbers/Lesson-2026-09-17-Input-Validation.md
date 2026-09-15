# U1 — Reflection: Trust Nothing the User Types

**LO:** explain why unchecked user input is dangerous, and lay out the validation rules a program needs.

Today is a discussion + paper day. No code required.

## PART 1 — OPENING PROVOCATION (10 min)

On the board: a calculator that accepts `hello` where a number belongs.

Run yesterday's `age-calculator.py` and type `banana` again. It dies.

Question on the board: **whose fault is the crash — the user, or the program?**

Everyone writes a one-line answer before we discuss.

## PART 2 — "WHAT ELSE COULD GO WRONG?" (15 min)

In small groups, list every bad input you can think of for a program that asks for
a number. Push past the obvious first three:

- empty input (just pressing Enter)
- spaces, letters, symbols, punctuation
- a number that is absurdly large
- a number that is negative, or absurdly small
- units that don't match what the program expects
- two numbers where the program wants one

Each group posts its top three on the board, and we sort them into "crashes" versus
"quietly wrong answers."

## PART 3 — THE DEFENCE: VALIDATE BEFORE YOU COMPUTE (10 min)

Introduce the rule the rest of the unit turns on: **never trust user input.**

Check it before you use it. That check has a name — *validation*. Name the two
outcomes a check can have: reject it, or repair it.

Preview tomorrow's tool: `try/except`.

## PART 4 — CASE STUDY: THERAC-25 (15 min)

Read the Therac-25 summary in pairs. In 1985–87 a radiation therapy machine delivered
massive overdoses because a numeric overflow slipped past the software's checks on the
operator's typed entry. Six patients were injured; several died.

Discuss, then answer in your notes:

- Where exactly did the validation fail?
- Who was responsible — the operator, the programmer, the hospital? Defend your answer.
- What would "validate before you compute" have looked like here, concretely?

## PART 5 — VALIDATION FLOWCHART (15 min) — TURN IN

On paper, draw the flowchart for a program that asks the user for a number:

    ask → convert → did it work? → yes: use it
                                 → no: print a message, ask again → repeat until `q`

Label each decision point with what would happen there *without* the check.
Turn the flowchart in at the end of class.

## PART 6 — JOURNAL (last 5 min)

`journal-0917-<yourname>.md` in your workspace — unique name, same convention as
Wednesday's (`journal-0917-mei.md`). Answer in 2-3 sentences:

- Which input from PART 2 is the most dangerous, and why?
- What is the one rule you will apply to every program you write from here on?
