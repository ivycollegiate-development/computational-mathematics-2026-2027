# U1 L07 — Worksheet: Safe vs Unsafe Arithmetic

Names: ___________________________  Date: ____

Paper and discussion day. Your only terminal work is the journal and the self-check at the end.

## Part 1 — Reconstruct Friday (10 min)


| Question | My answer |
|------------|------------|
| What does `try` do?                                               |                                                                      |
| What does `except ValueError:` catch?                              |                                                                      |
| Why did we put the `try/except` inside a loop instead of around the whole program? |                                   |
| Crash vs quietly wrong answer — which is easier to find, and why? |                                                                      |

   _________________________________________________________________________

## Part 2 — Safe or unsafe (15 min)

Sort each behavior, then defend the borderline ones.


| # | What the calculator does | Safe or unsafe? | Why? |
|------------|--------------------------|-----------------|------------|
| 1 | A calculator that crashes when you type a word                              |                 |                                            |
| 2 | A calculator that asks again when you type a word                           |                 |                                            |
| 3 | A calculator that divides by zero and prints `inf`                          |                 |                                            |
| 4 | A calculator that refuses to divide by zero and explains why                |                 |                                            |
| 5 | A program that accepts any number, even one bigger than all the money on Earth |             |                                            |
| 6 | A program that checks the input is in range *before* doing the math        |                 |                                            |

Which of these is the program being honest with the user, and which is it just hiding a problem?

   _________________________________________________________________________

   _________________________________________________________________________

## Part 3 — What is defensive programming? (15 min)

1. In your own words:

   _________________________________________________________________________

   _________________________________________________________________________

2. **The journal question.** Pick ONE of these three and defend it in 2–3 sentences. There is no single right answer; the reasoning is what is graded.

   ☐  `try/except`  ☐  type conversion  ☐  input validation

   _________________________________________________________________________

   _________________________________________________________________________

3. Compare with your partner: did they fix `get_number()` the same way you did? What was different?

   _________________________________________________________________________

## Part 4 — The impossible question (10 min)

- Can you list every input a user might type? (Remember Part 2 of L05.) Why or why not?

   _________________________________________________________________________

- If you cannot list every input, what should the program do with the ones you did not expect?

   _________________________________________________________________________

- Where does the line sit between "the program is safe" and "the program is less unsafe"?

   _________________________________________________________________________

One sentence you would be willing to say out loud:

   _________________________________________________________________________

## Part 5 — Journal (last 15 min)

Tighten your Part 3 answer into 3–5 sentences: which tool matters most, and why.

   _________________________________________________________________________

   _________________________________________________________________________

Is a completely crash-proof program possible? What did today's discussion change about your first answer?

   _________________________________________________________________________

   _________________________________________________________________________

## TURN IN

- ☐  Journal file open with your Part 3 and Part 5 answers.
- ☐  `python3 self_check.py` run locally, and the score in front of you.
- ☐  Screenshot to the Classroom assignment by 11:59 PM tonight showing: your journal file, and the successful `git push`.

Keep the journal — Monday's calculator v2 lab is graded on this vocabulary.
