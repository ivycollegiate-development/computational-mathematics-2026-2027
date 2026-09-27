# U1 L13 — LAB: Calculator Polish + Partner Showcase

**LO:** harden your calculator against a specific attack, then defend (or break) a partner's build.

Today is the last working session before the **Unit 1 assessment on Thu Oct 8**.
Two things happen: you spend the first half fixing the one thing you named in
yesterday's journal, and the second half you try to break someone else's
calculator. The partner attack is graded — see below.

You work in **your own calculator lab repo**. No new invitations.

## PART 0 — OPEN YOUR REPO (first 5 minutes)

```bash
pwd
cd ~/compmath-lab
git pull
python3 test_calculator.py
```

- `git pull` first — grab anything from another machine.
- Confirm your tests still pass **before** you change anything.
- Bring up your journal entry from yesterday. You are fixing **one** thing.

## PART 1 — FIX YOUR ONE THING (~30 min)

Pick the single item from yesterday's list. You are not expected to finish
everything — scope is part of the grade.

The rubric, for reference:

| Row | Weight |
|---|---|
| Validates input | 30% |
| Handles edge cases | 30% |
| Core functionality | 30% |
| Stretch | 10% |

Validation and edge cases are 60% combined. If you have to choose between a
polished menu and a guardrail that actually rejects bad input, take the
guardrail.

**Then test the input that broke nothing yesterday** — the one you predicted
would break your program. Run it. Write down what actually happened.

Commit as you go:

```bash
git add -A
git commit -m "Fix: <what you fixed>"
git push
```

## PART 2 — PARTNER ATTACK (~30 min)

Swap with your partner. Their goal is to make your calculator misbehave. Yours
is to survive. **You are attacking, not breaking** — the point is to find the
edge case, not to delete their work.

Try, in this order:

1. **Wrong type** — a word instead of a number, an empty input, a huge number of digits.
2. **The bounds** — a number over `10**15`. What does your program actually print?
3. **Below absolute zero** — negative Celsius converted to Kelvin. Does your floor fire?
4. **The boundary** — the exact largest allowed number, and the exact smallest Kelvin.
5. **Division** — zero as a divisor, and zero as the dividend.
6. **Undo the math** — convert Celsius → Fahrenheit → Celsius. Do you get your original back?

### What to record

For each attempt, write down: **the input, what happened, and whether it was a
bug or correct behavior.** "Correct behavior" is a real and valuable answer.

A conversion that comes back as `32.00000000000006` instead of `32` is a
finding. Decide whether it is a bug worth fixing, and be able to justify either
call.

## PART 3 — SHOWCASE (5 min per pair)

Demonstrate to each other:

1. **The thing you fixed today** and why it was the right thing to fix.
2. **The input that did *not* break it** — from yesterday's prediction.
3. **One thing you did not fix**, and why you scoped it out.

## TURN IN — PULL REQUEST (due 11:59 PM tonight)

Open or update your Pull Request and submit the link here. Before you do, check:

- [ ] `git status` is clean — nothing uncommitted
- [ ] All tests pass
- [ ] Your README or PR description says what you fixed today
- [ ] You have **not** left debug `print()` calls scattered through the code

**Graded on the partner attack.** Write up your findings: the three most
interesting inputs you tried, what happened, and which one you consider a real
bug. Put that writeup in your PR description or a linked file in the repo. The
best submissions find a genuine edge case and explain *why* it matters — a long
list of failed attacks with no analysis scores lower than three well-explained
ones.
