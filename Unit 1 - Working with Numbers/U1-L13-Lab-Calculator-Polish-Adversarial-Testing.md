# U1 L13 — LAB: Calculator Polish + Adversarial Testing

**LO:** harden your calculator against a specific attack, then prove it survives
an attack set you could not have seen in advance.

Today is the last working session before the **Unit 1 assessment on Thu Oct 8**.
Two things happen: you spend the first half fixing the one thing you named in
yesterday's journal, and the second half you attack **your own** calculator
against a probe set generated for you at the start of class.

**Why your own calculator and not your partner's:** the probe set is generated
per student, in class, from a seed nobody else has. Reading anyone else's repo
before today gives you nothing — you would be attacking inputs that were never
in your file. The skill being graded is *adversarial thinking*, not code
theft. This also means you can be honest in your writeup: every finding is
genuinely yours.

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

## PART 2 — ADVERSARIAL PROBES (~30 min)

### Generate your attack set

Run this with **your seat number**:

```bash
python3 gen_probes.py <your seat number>
```

It writes `attack_probes.py` with a personalized list of hostile inputs:
wrong types, absurdly large numbers, exact boundary values, and division by
zero variants. Because it is generated from a per-student seed at class time,
no two probe sets are the same and none of them were knowable in advance.

- **Do not commit `attack_probes.py`** — it is already in your `.gitignore`.
- **Do not post your seed or the file.** The value is that it is unpredictable.

### Run every probe

The existing test harness already lets you script input. Build one test per
probe group against your own `calculator.py`:

- `WRONG_TYPE` — words, empty input, malformed numbers. Does it re-prompt, or
  crash?
- `HUGE` — numbers past `10**15`. What does your program actually print?
- `BOUNDARY` — the exact largest allowed number, one over, one under, and
  temperatures straddling absolute zero. Does your floor fire at the right
  place, or one step late?
- `DIV_ZERO` — `0`, `-0`, `0.0`, and a denormal like `1e-320`. All should be
  rejected, not all should crash the same way.

Then attempt each one **by hand** in the terminal. Both matter: the test tells
you what happens, the terminal run tells you what the user would see.

### What to record

For each probe: **the input, what happened, and whether it was a bug or correct
behavior.** "Correct behavior" is a real and valuable answer.

Aim to find **at least two genuine bugs**. A conversion that comes back as
`32.00000000000006` instead of `32` is a finding. Decide whether it is a bug
worth fixing, and be able to justify either call.

If your calculator survives all of them, do not stop there — write a probe
that specifically targets whatever guardrail you wrote. Break your own
defense on purpose. That is the harder skill.

## PART 3 — SHOWCASE (5 min per pair)

With your partner, take turns demonstrating:

1. **The thing you fixed today** and why it was the right thing to fix.
2. **One probe that did *not* break it** — and why you believe that is correct.
3. **One real bug you found in your own code**, or the guardrail you broke on
   purpose.

## TURN IN — PULL REQUEST (due 11:59 PM tonight)

Open or update your Pull Request and submit the link here. Before you do, check:

- [ ] `git status` is clean — nothing uncommitted
- [ ] `attack_probes.py` is **not** committed and **not** in the diff
- [ ] All original tests pass
- [ ] Your README or PR description says what you fixed today
- [ ] You have **not** left debug `print()` calls scattered through the code

**Graded on the adversarial testing.** Write up your findings: the three most
interesting probes you ran, what happened, and which one you consider a real
bug. Put that writeup in your PR description or a linked file in the repo.
The best submissions find a genuine edge case and explain *why* it matters — a
long list of failed attacks with no analysis scores lower than three
well-explained ones.

**Not graded on breaking someone else's calculator.** Nobody reads another
student's repo to do this, so there is nothing to copy, and the grade reflects
only what you found yourself.
