# U1 L11 — Calculator v2 — Step-by-Step Directions

Computational Mathematics     Name: __________________________     Partner: __________________________

This sheet walks you through every step of the U1 L11 lab. Follow it in order. Each
step says what to do, why you are doing it, and what "finished" looks like. Do not
skip ahead — the order matters, because each part depends on the one before it.

By the end you will have a calculator that does unit conversions and refuses bad
input safely.

---

## PART 0 — OPEN YOUR CALCULATOR REPO

**What you are doing:** getting your project open, up to date, and proven to work
before you change a single line.

**Step 0.1 — Check where you are.**

Open the terminal in your VS Code workspace and type:

    pwd

`pwd` prints your current folder. You need to be inside your home folder before
you can move anywhere, so this tells you what "here" currently is.

**Step 0.2 — Move into the repo.**

    cd ~

    cd ~/compmath-lab

The `~` character means "my home folder." If your clone is somewhere else (a
different folder name, or inside a `Documents` or `Desktop` folder), run `cd ~`
first and then use `ls` to look around until you find the folder that contains
`calculator.py` and `test_calculator.py`. The repo folder is called
`compmath-lab`.

**Why this matters:** every command after this one has to run from inside the repo
folder. If you are one folder too high or too low, `git` and `python3` will
complain that the files do not exist — and that error looks like a broken repo
when it is really just a wrong working folder.

**Step 0.3 — Pull any work you pushed from another machine.**

    git pull

`git pull` downloads the newest version of the code from GitHub into your
computer. If you worked on a different computer, or you pushed something before
class ended, this brings it back so you do not build on top of an old copy.

**Why this matters:** `git pull` before you edit prevents the single most common
mess in this project — you build a new feature, then discover the pull request
had conflicts because half the work already existed. Pull first, edit second.

**Step 0.4 — Prove the calculator still works.**

    python3 test_calculator.py

You should see four checks pass and a final line that says 4/4 passing.

**What "finished" looks like:** 4/4 passing.

**If it is not 4/4:** stop and fix that before you touch anything else. Today's
conversions and guardrails are built on top of the four tests from U1 L08. If a
test is failing, you cannot tell whether your new code broke it or it was already
broken — so clear the baseline first. Two of the four failures have known fixes:

- Test 1 (bad input crashes) — `get_number()` needs a `try` / `except` around
  `float(raw)` so a bad word re-asks instead of crashing the program.
- Test 2 (divide by zero) — `divide()` needs to check `b == 0` before dividing.

---

## PART 1 — ADD THE CONVERSIONS

**What you are doing:** bringing the unit-conversion functions you already wrote
in U1 L09 into the calculator, and giving each one its own menu choice.

**Step 1.1 — Open the file you are editing.**

    code calculator.py

Or open it from the Explorer panel on the left side of VS Code. You are editing
one file today: `calculator.py`.

**Step 1.2 — Copy your seven conversion functions in.**

From your converter lab (U1 L09), copy these seven functions into
`calculator.py`, placing them below the `divide()` function and above `main()`:

- `c_to_f` — Celsius to Fahrenheit
- `f_to_c` — Fahrenheit to Celsius
- `c_to_k` — Celsius to Kelvin
- `km_to_miles` — kilometres to miles
- `miles_to_km` — miles to kilometres
- `kg_to_lbs` — kilograms to pounds
- `lbs_to_kg` — pounds to kilograms

**Why copy instead of retype:** these functions were already tested in U1 L09.
Retyping them from memory is how small errors get in — a wrong constant, a
missing multiply, a sign dropped. Copying is a professional habit, not laziness.

**Step 1.3 — Fix the `f_to_c` formula before you paste.**

The correct Fahrenheit-to-Celsius formula is:

    return (f - 32) * 5 / 9

The U1 L09 starter shipped with the `- 32` missing, which produces a wrong answer
with no error message at all. If you copied that version verbatim, 212 F will
report 117.78 instead of 100.0 — and nothing will tell you it is wrong.

**Why this matters:** this is the exact failure this whole unit keeps returning
to — code that runs cleanly and returns a number that is quietly false. A program
that produces no error is not the same as a program that produces a right answer.

**Step 1.4 — Add the conversion constants near the top of the file.**

Put these two lines just under the `MENU` string, with the other module-level
values:

    KM_PER_MILE = 1.609344

    KG_PER_LB = 0.45359237

Use these in the conversion functions rather than typing the number into the
formula. Constants at the top are one place to fix, are named for what they mean,
and make the formula readable.

**Step 1.5 — Extend the menu string.**

Your menu currently lists choices 1 through 4 plus `q`. Extend it to eleven
choices:

    MENU = """
    Choose an operation:
      1) add (+)
      2) subtract (-)
      3) multiply (*)
      4) divide (/)
      5) Fahrenheit -> Celsius
      6) Celsius -> Fahrenheit
      7) Celsius -> Kelvin
      8) km -> miles
      9) miles -> km
     10) kg -> lbs
     11) lbs -> kg
      q) quit
    """

**Step 1.6 — Update the valid-choice check.**

The line that rejects bad menu input currently reads:

    if choice not in ("1", "2", "3", "4"):

It must now read:

    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"):

and the message should say `Please pick 1-11, or q.`

**Why this matters:** forget this line and typing `5` prints "Please pick 1, 2, 3,
4, or q" and loops back. The program does not crash, so it survives a careless
read — it just silently never offers the new features.

**Step 1.7 — Wire each conversion into `main()`, BEFORE the second-number prompt.**

This is the single most important step in Part 1. In `main()`, right after the line
that reads the first number, insert the single-number branches:

    # single-number operations: one input, one conversion
    if choice in ("5", "6", "7"):
        celsius = f_to_c(a) if choice == "5" else a
        if is_below_absolute_zero(celsius):
            print(f"{celsius:.2f} C is below absolute zero — refusing.")
            continue
        if choice == "5":
            result = celsius
        elif choice == "6":
            result = c_to_f(a)
        else:
            result = c_to_k(a)
        print(f"Result: {result}")
        continue
    if choice in ("8", "9", "10", "11"):
        if choice == "8":
            result = km_to_miles(a)
        elif choice == "9":
            result = miles_to_km(a)
        elif choice == "10":
            result = kg_to_lbs(a)
        else:
            result = lbs_to_kg(a)
        print(f"Result: {result}")
        continue

(The `is_below_absolute_zero` call is Part 2 — if you have not written that
function yet, leave that inner `if` out for now and add it in Part 2.)

**Why this must come before the second prompt:** every conversion takes exactly
ONE number. Choices 1 through 4 take two. If your new branches sit *below* the
line `b = get_number("Second number: ")`, then selecting Celsius-to-Kelvin asks
you for a second number you do not need, and it uses that second number for
nothing. The program will not crash and will not error — it will just ask a
nonsense question, which is exactly why it survives careless reading.

**Why each branch ends with `continue`:** `continue` jumps back to the top of the
`while True` loop, printing a fresh menu. Without it, execution falls through to
the `b = get_number(...)` line and you are back in the same trap.

**Step 1.8 — Run it and check the conversions work.**

    python3 calculator.py

Then check each one of these. Type the menu number, then the input:

| Menu | Function | Type this | Result should be |
| --- | --- | --- | --- |
| 5 | f_to_c | 212 | 100.0 |
| 5 | f_to_c | 32 | 0.0 |
| 5 | f_to_c | -40 | -40.0 |
| 6 | c_to_f | 100 | 212.0 |
| 7 | c_to_k | 25 | 298.15 |
| 8 | km_to_miles | 10 | 6.2137119223733395 |
| 9 | miles_to_km | 5 | 8.04672 |
| 10 | kg_to_lbs | 70 | 154.3235835294143 |
| 11 | lbs_to_kg | 154 | 69.85322498000001 |

**About the long decimals:** those are correct, not a bug. Ten kilometres really
is 6.2137119223733395 miles. If the display is ugly, the fix is to format the
output — for example `print(f"Result: {result:.2f}")` — not to round the constant
inside the formula. Rounding the constant changes the answer.

**Step 1.9 — Confirm the original tests still pass.**

    python3 test_calculator.py

Still 4/4. If a test broke, you almost certainly moved or deleted something in
`divide()` or `get_number()` — put it back before going further.

---

## PART 2 — ADD THE GUARDRAILS

**What you are doing:** making the calculator refuse input that would produce a
meaningless or impossible result. These come from the plan you wrote in U1 L10.

**Step 2.1 — Add the two limits as named constants.**

Put these near the top of the file, under `MENU`:

    MAX_VALUE = 1e15

    ABSOLUTE_ZERO_C = -273.15

**Why these numbers:** past about 10^15, floating-point arithmetic starts losing
whole numbers, so a "result" would be a lie rather than a number. And -273.15 C
is absolute zero — the coldest physically possible temperature. A calculator that
returns a temperature below it is reporting physics that cannot exist.

**Step 2.2 — Write the overflow checker.**

    def is_too_big(n):
        return abs(n) > MAX_VALUE

`abs()` matters: a calculator that accepts a billion but rejects minus a billion
is not guarding anything. Both directions are equally out of bounds.

**Step 2.3 — Write the Kelvin-floor checker.**

    def is_below_absolute_zero(celsius_value):
        return celsius_value < ABSOLUTE_ZERO_C

**Step 2.4 — Put the overflow guard inside `get_number()`.**

`get_number()` is the one function every single number passes through. Putting
the check there means all eleven menu choices inherit it automatically, with no
extra code. Your `get_number()` should look like this:

    def get_number(prompt):
        while True:
            raw = input(prompt)
            try:
                value = float(raw)
            except ValueError:
                print(f"'{raw}' is not a number. Try again.")
                continue
            if is_too_big(value):
                print("absurdly large — refusing to compute. Try again.")
                continue
            return value

**Why here and not in the menu:** this is the defensive-programming habit —
**validate before you compute.** A check sitting in one menu branch protects
exactly one menu choice; the next person to add choice 12 forgets the check. A
check in `get_number()` protects every path through the program forever. One
small checker function beats scattering `if` statements everywhere.

**Step 2.5 — Wire the Kelvin floor into the temperature branches.**

The check goes inside the `if choice in ("5", "6", "7"):` block from Step 1.7.
Look closely at the first line of that block:

    celsius = f_to_c(a) if choice == "5" else a

**This is the Fahrenheit trap, and it is the hardest thing in today's lab.**

For choice 5 the user types a Fahrenheit number. For choices 6 and 7 they type a
Celsius number. So the bound has to be checked on a **Celsius** value. If you
compare the raw input against -273.15, then -300 F gets refused — but -300 F is
a perfectly valid temperature, equal to -184.4 C. Your guardrail would be
"working" loudly while rejecting real temperatures.

So: convert first (for choice 5), then check, then decide whether to print.

**Why convert-then-check rather than check-then-convert:** you cannot know
whether a Fahrenheit input is below absolute zero until you have converted it.
The order is forced.

**Step 2.6 — Test both guardrails against these exact cases.**

| What you type | What must happen |
| --- | --- |
| 1000000000000000 (exactly 10^15) | allowed — computes normally |
| 1000000000000001 (10^15 + 1) | refused, asks again |
| 1e16 | refused, asks again |
| -1000000000000000 | allowed — abs() means negatives are judged on size |
| -273.15 then choice 7 | allowed, Result: 0.0 |
| -273.16 then choice 7 | refused, message about absolute zero |
| -300 then choice 7 | refused, message about absolute zero |
| -300 then choice 5 (Fahrenheit) | ALLOWED — Result: -184.44444444444446 |
| -500 then choice 5 (Fahrenheit) | refused, message shows -295.56 C |

The fourth-from-last row is the one that catches the trap. If your calculator
refuses -300 Fahrenheit, your bound is running on the wrong scale.

**Step 2.7 — Re-run the original tests.**

    python3 test_calculator.py

4/4. A passing test suite is necessary but not sufficient — the four tests do not
know anything about conversions or guardrails. Your real check is the table above.

---

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

    git status

    git diff

Read the diff. It is your last chance to catch a mistake — a function pasted
twice, a line deleted by accident, a `continue` missing. Ten seconds here saves
a broken push.

**Step 4.2 — Commit.**

    git add calculator.py

    git commit -m "add unit conversions and overflow/Kelvin guardrails"

`git add` stages the file. `git commit` records a named snapshot. The commit
message should say what the change *does*, not "stuff" or "update" — a future
reader sees only the message.

**Step 4.3 — Push.**

    git push

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
| `python3: command not found` | wrong machine or wrong terminal | use the Codespace terminal, not a local one |
