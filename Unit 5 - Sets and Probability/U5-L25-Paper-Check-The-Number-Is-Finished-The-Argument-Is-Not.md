# U5 L25 — Paper Check: The Number Is Finished. The Argument Is Not.

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (paper check, 50 minutes)
**LO:** 5.9–5.10 — defend a completed model in prose; distinguish a number that
is correct from an argument that is sufficient

---

**No laptop.** Calculator allowed. The number is finished — you computed it
twice, closed form and simulation, and they agree. **Today we finish the
argument**, which is the half of the work that is graded and that nobody
practises.

The distinction this lesson turns on: a number can be **correct, exact,
reproducible, and still not be an answer.** A number is an input to an
argument. The argument is what you are assessed on.

## PART 1 — WHAT YOU ARE ACTUALLY BEING ASKED (8 min)

Your report contains a figure, `expected annual loss`, and a table of
assumptions. The reader sends one question back:

> "Fine. What should I do?"

- ☐  The figure is 5,047.48. Write, in one sentence, what decision that figure
      **can** support without qualification: ______
- ☐  Write, in one sentence, what it **cannot** decide on its own, and why:
      ______
- ☐  The gap between those two sentences is what this lesson is about. How many
      sentences would you estimate are needed to close it: ______

That last one has no right answer, and I want you to notice that. The honest
answer is that you cannot know until the reader says what they need — which is
why Part 3 exists and why I have asked you to write the reader's question down
before you answer it.

## PART 2 — THE FOUR THINGS A READER WILL PUSH ON (20 min)

Each of these is a real question I have been asked about models like yours.
Answer each in **two sentences maximum**. Brevity is the skill.

**P1 — "Where did 3/20 come from?"**
Your likelihood came from analyst judgement and a scan of 9 hosts.
- ☐  Answer: ______
- ☐  Is the honest answer weaker than the number suggests? ______

**P2 — "You have one incident in your history. How is that 15%?"**
- ☐  Answer: ______
- ☐  What is the honest error bar on a single observation, and how would you
      state it in a report: ______

**P3 — "Your two file-server threats are independent?"**
Both require the same world-readable share point. The independence claim in
your report is false.
- ☐  Answer: ______
- ☐  **And now the harder question:** if the threats are positively correlated,
      does the correct model give a *higher* or *lower* expected loss than the
      independent one, and by enough to matter at this scale: ______

**P4 — "What if every number in your table is wrong by a factor of two?"**
- ☐  Answer: ______
- ☐  Does the conclusion change? If not, say what that tells you about the
      precision your model actually warrants: ______

## PART 3 — THE WRONG QUESTION, HANDLED (12 min)

The reader asks:

> "Your expected loss is 5,047 a year. The backup costs 5,000 a year. The backup
> is obviously not worth it — it costs more than the risk."

Three things are wrong with that, and they are three different errors.

- ☐  **W1.** The comparison is between a certain cost and an expected cost.
      What is the error in treating them as commensurable: ______
- ☐  **W2.** Expected loss averages over years, including the one year where the
      loss is existential. For which decisions is that the wrong statistic, and
      what should replace it: ______
- ☐  **W3.** The backup does not only reduce loss frequency; it reduces loss
      *magnitude*. Does your model's 12,000 asset value represent the loss with
      or without a tested backup, and what should the model do about it: ______

- ☐  Now write the **response**, three sentences, that corrects all three
      without being condescending to the reader: ______
- ☐  Read it back. Would you be annoyed to receive it? ______

W3 is the one that will not have occurred to you, and it is the one that makes
the model useful rather than merely honest. **A model that cannot represent the
mitigation cannot inform the decision about the mitigation.** Your simulator
currently prices the world as it is and the world as it would be after the
backup, but the second is not in the data — so the model as it stands can only
tell the reader what things cost, never what the money would buy. Add the
post-mitigation scenario to the model and the comparison becomes computable
rather than rhetorical.

- ☐  In your own model: if the backup is fitted, the file-server asset value
      drops from 12,000 to what, and where does that number come from rather
      than from your imagination: ______

## PART 4 — THE WHOLE ARGUMENT, IN WRITING (10 min)

One page. No headings, no bullets. This is the graded item, and it is the
thing a reader will remember.

Constraints:
- ☐  States the number and its period and its population
- ☐  Names at least one assumption **and says what it would take to check it**
- ☐  Acknowledges a direction of possible error
- ☐  **Recommends an action** — a real one, with a cost, and not "further
      analysis is required"
- ☐  Is between 180 and 250 words

> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________
> ________________________________________________________________

- ☐  Word count: ______
- ☐  Which of the four constraints was hardest, and did you meet it: ______
- ☐  **Read it as the operations manager, not as the author.** Would you act on
      this? ______

## TURN IN — The Argument

1. Part 2, all four answers
2. Part 3's W1–W3 and the three-sentence response
3. **The one-page argument**
4. Your own word count, written on the page

**Bring U5 L26:** everything, plus your `riskkit.py`. We produce the manifest.

## 📋 PREVIEW OF U5 L26

**Next:** L26, Mar 24 — **machine day, and the deliverable.** We take
`shape_report` and make it emit a manifest: a self-describing block of output
that states the number, its period, its population, its assumptions, its
tolerance, and its own seed. The point is that a result which does not carry
its own provenance is a number, and a number with provenance is evidence.

**Bring U5 L26:** the repository, the README, the one-page argument, and a
clear head — the manifest is the thing an assessor will read first.
