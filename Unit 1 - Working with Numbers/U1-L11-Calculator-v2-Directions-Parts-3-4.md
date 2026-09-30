# U1 L11 — Calculator v2 — Step-by-Step Directions — Parts 3 and 4

Computational Mathematics     Name: __________________________     Partner: __________________________

## PART 3 — PAIR CODE REVIEW

**What you are doing:** reading someone else's guardrail code and trying to break
it. This is a real skill, and it is the same skill a security reviewer uses.

**Step 3.1 — Get their code.**

Either swap screens, or open your partner's repository on github.com and read
their `calculator.py` directly. Read the file; do not just look at the file names.

**Step 3.2 — Find the guardrail implementations.**

Search their file for `is_too_big`, `is_below_absolute_zero`, `MAX_VALUE`, and
`ABSOLUTE_ZERO_C`. Find out:

- Which bound did your partner enforce, and how?
- Where exactly did they put the check — inside `get_number()`, or in the menu
  branch?
- Do they check the bound on a Celsius value or a raw Fahrenheit value?

**Step 3.3 — Try to break it.**

Write down one specific input that would still sneak past their guardrail. Ideas
to try:

- A negative number with a huge magnitude — does their check use `abs()`?
- Exactly 10^15, or 10^15 minus 1 — where is the boundary, and is it where they
  said it was?
- The word "infinity" — does `float()` accept it, and what happens next?
- A Fahrenheit temperature below -459.67, which is below absolute zero once
  converted?
- A number like `1e400`, which overflows to `inf` in Python.

Then actually go run their code and try it. Report what really happened, not what
you predicted.

**Step 3.4 — Write the review.**

- One specific compliment. "Looks good" is not a review. Name the thing: "your
  check is in `get_number()` so all eleven choices get it for free."
- One specific suggestion. Point at a line and say what you would change and why.

**Why this is graded as a review and not as a compliment exchange:** the skill
being practised is reading unfamiliar code, forming a hypothesis about where it
breaks, and testing that hypothesis. A vague compliment exercises none of it.

---

## PART 4 — SAVE YOUR WORK

**Step 4.1 — Look at what changed.**

```bash
git status
git diff
```

Read the diff. It is your last chance to catch a mistake — a function pasted
twice, a line deleted by accident, a `continue` missing. Ten seconds here saves
a broken push.

**Step 4.2 — Commit.**

```bash
git add calculator.py
git commit -m "add unit conversions and overflow/Kelvin guardrails"
```

`git add` stages the file. `git commit` records a named snapshot. The commit
message should say what the change *does*, not "stuff" or "update" — a future
reader sees only the message.

**Step 4.3 — Push.**

```bash
git push
```

If it asks for a password, that is a **Personal Access Token**, not your GitHub
password. GitHub turned off password authentication for pushes in 2021. If you
do not have a token yet, ask — do not guess, and do not paste a token into chat.

**What "finished" looks like:** the push succeeds, and github.com shows your
commit on the repository page.

---

## MILESTONE — CALCULATOR v2

You are done when all four of these are true:

- All 4 original tests pass (`python3 test_calculator.py` → 4/4 passing).
- All seven conversions work from the menu and match the table in Step 1.8.
- Both guardrails are live: 10^16 is refused, and -300 C is refused while
  -300 F is allowed.
- Your work is committed and pushed.

---

## TURN IN — PULL REQUEST LINK (due Oct 4, 11:59 PM)

**Step 5.1 — Push your final version.** Do this after Part 4, and again if you
made any last changes.

**Step 5.2 — Open or update your Pull Request.**

On github.com, open your repository, go to the Pull requests tab, and use
Contribute → Open pull request. If you already opened a PR for v1, update that
same one — do not open a second PR for the same work.

**Step 5.3 — Submit the PR link** to this assignment on Google Classroom.

One PR covers v1 and v2. One link, submitted once.

---

## EARLY FINISHERS — PICK ONE

- **Safe mode toggle:** add a setting so that when it is ON the calculator
  refuses every operation whose inputs violate your bounds, and when it is OFF it
  only warns and computes anyway. This is a real design decision — what is the
  default, and why?
- **Guardrail test cases:** add cases to `test_calculator.py` that deliberately
  try to sneak past your own guardrails. A test that tries `1e16` and expects a
  refusal is worth more than a test that checks `1 + 1`.

---

## TROUBLESHOOTING

| Symptom | Cause | Fix |
| --- | --- | --- |
| Typing 5 says "Please pick 1, 2, 3, 4, or q" | the valid-choice tuple was not extended | fix the `not in (...)` line to list 1 through 11 |
| A conversion asks for a second number | the branch sits below `b = get_number(...)` | move the single-input branches above the second prompt, then `continue` |
| Overflow message prints but the number is still used | the check is in the menu branch, after the input | move it into `get_number()` so every path inherits it |
| -300 Fahrenheit is refused | the bound ran on a Fahrenheit value | convert to Celsius first, then check |
| Warning prints, then a Result line still follows | the branch is missing its `continue` | add `continue` after the warning |
| 212 Fahrenheit gives 117.78 | `f_to_c` was copied without the `- 32` | fix the formula to `(f - 32) * 5 / 9` |
| Tests pass but the menu has nothing new | functions were pasted but not wired to choices | add the menu lines, the choice tuple, and the branches |
| `fatal: not a git repository` | you are in the wrong folder | `cd ~` then `cd ~/compmath-lab` |
| `python3: command not found` | wrong machine or wrong terminal | use the VS Code terminal, not your local Mac |
