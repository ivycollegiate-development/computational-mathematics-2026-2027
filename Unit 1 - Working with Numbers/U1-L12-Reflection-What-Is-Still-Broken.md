# U1 L12 — Reflection: What Is Still Broken in Your Calculator?

**LO:** diagnose the remaining failure modes in your own calculator and plan the polish work for tomorrow.

Today is a paper and journal day. No coding today — tomorrow is the polish and
showcase session before the Unit 1 assessment on Oct 8, and this is where you
decide what to fix. Bring your calculator lab open on paper or in a printed
listing, because you will be reading your own code.

## PART 1 — REOPEN THE CODE (10 min)

You last touched the calculator Wednesday (U1 L11) — conversions plus the two
guardrails. Before writing anything, read your own code with fresh eyes and
answer in your notes:

- List every function you now have. Does the menu show all of them?
- What does your program do with an input that is *not* a number, after the
  `try/except` catches it? Does it ask again, or exit?
- Find the line where you check `10**15`. What exactly happens to the user when
  that check fires?

## PART 2 — THE HONEST LIST (20 min)

Most calculators have at least one thing that is not finished. Write them down
in your journal, ranked by how much they would embarrass you if a stranger ran
the program. Use the rubric vocabulary — the assessment is coming.

Typical honest answers, none of which are wrong:

| You wrote | The honest version |
|---|---|
| "My conversions all work" | "Three of six work; I never wired `kg_to_lbs` into the menu" |
| "It has guardrails" | "It rejects big numbers but silently returns `None` instead of telling the user" |
| "My tests pass" | "My 4 tests pass; I never tested a string input" |
| "I did the stretch goal" | "I skipped it" |

Then answer in your journal:

1. **Which single thing will you fix tomorrow?** One. Not three. The rubric
   rewards validated input and handled edge cases most heavily, so fix the
   thing that moves you most on those two rows.
2. **Which thing will you explicitly *not* fix?** Writing this down matters.
   It is the difference between scoping and giving up, and you will reference
   it in your showcase.
3. **What is one input that breaks your program that you have not tried?**
   Come up with it now so you can test it tomorrow. If it turns out not to
   break it, that is the better outcome — and you can say so in the showcase.

## PART 3 — SHOWCASE PLANNING (10 min)

Tomorrow you demo to a partner. Decide now:

- Who presents? Take turns — one drives, one narrates.
- What is the one thing you most want your partner to notice?
- What is the one thing you most want them to try to break?

That last one is the whole point of tomorrow. Come prepared with a specific
attack on your partner's calculator.

## TURN IN — JOURNAL ENTRY (due 11:59 PM tonight)

One journal entry containing:

1. Your honest list from Part 2, ranked.
2. The one thing you will fix tomorrow.
3. The one thing you will not fix.
4. One input that might break your program.

Photograph your journal page and submit the photo to this assignment on Google
Classroom. Handwriting is fine. No terminal today.
