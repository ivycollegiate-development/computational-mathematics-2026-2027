# U2 L09 — Worksheet: What Makes Data Real?

Names: ___________________________  Date: ____

Starts on paper, ends in the terminal. No coding until late.

## Part 1 — Reconstruct last week (10 min)


| Question | My answer |
|------------|------------|
| The three things every honest chart needs                       |                                               |
| Why did `plt.show()` not do anything useful in the terminal?     |                                               |
| What does `savefig()` do, and where did your file end up?         |                                               |

Now the sentence the whole part is for, in your own words:

   _________________________________________________________________________

## Part 2 — Provenance chain: who, why, how, when (15 min)

Pick a dataset you know — the weather report, a video game leaderboard, a class survey, a fitness app on your phone. Build its chain.


| Question | My dataset |
|------------|------------|
| **Who** collected it?   |                                                                |
| **Why** did they?       |                                                                |
| **How** did they collect it? |                                                            |
| **When** did they collect it? |                                                           |

Would you trust this dataset? It depends on what — say what.

   _________________________________________________________________________

## Part 3 — Is our data real? (15 min)

We have been using `u2_student_performance_data.csv`: 1,000 rows of students with study hours, sleep, GPA, and absence rate.

- Do 1,000 real students' records with this many personal columns seem likely to be sitting in a public CSV?

   _________________________________________________________________________

- If I told you a program generated these rows from random ranges, what clues would you look for **in the file itself**?

   _________________________________________________________________________

Open the file and scroll. Write at least two clues that support "synthetic" and two that support "real."


| Clue I found in the file | Points to synthetic or real? |
|--------------------------|------------------------------|

Your call, defended:

   _________________________________________________________________________

## Part 4 — How can you tell? (10 min)

The provenance checklist. For each question, write what it catches.


| Checklist question | What it catches |
|--------------------|-----------------|
| Is there a source named?                 |                                                    |
| Do the rows contradict themselves?       |                                                    |
| Are the numbers *too* clean?             |                                                    |
| Is it surprisingly complete?            |                                                    |
| Does the date fit the story?             |                                                    |

If our data is synthetic, what are we then allowed to *claim* from our charts?

   _________________________________________________________________________

   _________________________________________________________________________

## Part 5 — Journal (last 5 min)

- Where did our performance data come from, and why does that matter for the charts I made last week?

   _________________________________________________________________________

- Name one real-world dataset you use, or that is used on you. Its provenance chain — and what you would have to *believe* to trust it:

   _________________________________________________________________________

- One rule I will apply to every dataset from here on:

   _________________________________________________________________________

## Part 6 — Push

- ☐  `journal-$(whoami).md` created in `~/compmath-u2-data-lab`, Part 5 answered, `git push` confirmed.

## TURN IN

- ☐  Parts 1–5 complete, including your defended call on whether the data is real.
- ☐  Screenshot to the Classroom assignment by 11:59 PM tonight showing: your `ls data` output with the dataset files visible, your journal answers open in VS Code, and the successful `git push`.

Keep the checklist. Every chart you build from here on gets a provenance line under it.
