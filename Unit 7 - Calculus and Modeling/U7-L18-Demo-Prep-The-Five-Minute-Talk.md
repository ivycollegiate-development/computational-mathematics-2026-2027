# U7 L18 — Demo Prep: The Five-Minute Talk

**Unit:** 7 — Calculus and Modeling
**Type:** Paper lesson (45 minutes)
**LO:** 7.5 — deliver a five-minute technical talk with a live run

---

**No laptop for the writing.** Bring the talk and, at the end, the laptop for a
live run. The U7 L20 demo has one hard rule: **the program must run in front of
people.** A slide deck about a working thing is a worse demo than a working
thing.

## PART 1 — THE RUN, PLANNED (15 min)

Decide these before L20, not during.

- ☐  1. **What exactly will you type on screen?** Write the literal commands:
     ______
- ☐  2. **What is the one line of output you want the audience to see?** ______
- ☐  3. **Will you run on the development data or something else?** ______
- ☐  4. **What happens if the CSV path is wrong on the demo machine?** Your
     answer: ______
- ☐  5. **What happens if there is no network / a different working directory?**
     ______

Questions 4 and 5 are the difference between a demo that works and a demo where
you spend ninety seconds apologising. The mitigation for both is boring and
works every time: **have the exact command written on a card, with an absolute
path, and have already run it in that room.** If a thing can go wrong on demo
day, it will go wrong on demo day, and the response is preparation rather than
improvisation.

- ☐  6. Do you have a **fallback** if the live run fails — a saved output file
     you can show? ______
- ☐  7. What is the single most impressive thing your program does, and is it
     the thing you will show? ______

Question 7 is a real strategic question, not a vanity one. The most impressive
capability is often the hardest to demonstrate reliably, and the thing you show
should be the thing that survives a bad projector and a nervous presenter.
Usually that is the guard refusing to answer, because it is short, it always
works, and it makes the point better than the happy path does.

## PART 2 — THE TALK, DRY RUN (15 min)

Stand up. Say it out loud to an empty room, or to one person. Timed.

- ☐  Round 1, no stopping: ______ seconds
- ☐  Where did you speed up? ______
- ☐  Where did you trail off or add "um"? ______
- ☐  Round 2, with the talk in front of you: ______ seconds
- ☐  Did the live run fit inside 5 minutes? ______
- ☐  If not, what did you cut — the talk or the run? ______

Speaking it aloud is not optional and it is the only way to find the things the
page hides. Written, a 900-word defense feels like five minutes. Spoken at
speed, it is eight. Everyone is wrong about this until they measure, and
measuring is the entire content of this lesson.

- ☐  8. The sentence you would most like to skip is in section ______
- ☐  9. Read it aloud five times until it does not need skipping. Now it is
     ______ words, and it is the best sentence in your talk. Confirm: ______

## PART 3 — THE AUDIENCE (10 min)

- ☐  10. What does the audience already know? ______
- ☐  11. What is the **one** thing they must remember in an hour? ______
- ☐  12. What question do you most want to be asked, and how do you invite it?
     ______
- ☐  13. What question do you most dread? ______
- ☐  14. Write your one-sentence answer to 13. ______

Question 12 has a technique worth using: state the limitation prominently *before*
someone asks, and the room will almost always take the opening you gave them. The
questions that follow are chosen by the audience, and the opening is a
generous thing to do for them.

## PART 4 — ERROR LOG (5 min)

- ☐  Record slips
- ☐  Tags: **pacing**, **demo failure**, **audience**, **opening**
- ☐  Newest tag: ______

## 🇹🇼 TAIWAN CONTEXT

Questions 4 and 5 are worth more than they look, because of a local
specificity: **the demo machine will not be your machine.** Classrooms and
labs here frequently run Windows on a restricted account with a different Python
installation, a different path separator, and no write access to the directory
you practised in. A demo that depends on `~/projects/...` or on a file you
created in your own home directory will fail on a machine where the user cannot
write to their home. Practise on the actual demo machine, or bring the data file
on removable media along with an absolute path that you have verified on that
machine.

The deeper habit is worth naming, because it generalises well beyond demos: **a
result you cannot reproduce on someone else's setup is a result you have not
finished producing.** The same applies to the analysis itself — a threshold
calibrated on one machine's floating-point behaviour and re-run elsewhere is
part of what L15's near-constant guard was about. The five-minute demo is
simply the smallest honest test of reproducibility available, and it is a test
everyone passes on their own laptop and then fails in the room.

**Next:** L19 — paper. Whole-year reflection.
