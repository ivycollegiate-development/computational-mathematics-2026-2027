# Sep 9 — Number Operations in the REPL

**Unit 1 · Week 1 · Wednesday (Code-along day)**

Everything today happens in your VS Code workspace. No paper worksheet.

## Part 1: In your workspace (first 10 minutes)

1. Log in at https://vscode.ivycollegiate.org/ — school Google account
2. In the terminal, check where you are: `pwd` — if you're not in your home directory, `cd ~`
3. If you don't have the course repo yet:
   **git clone https://github.com/ivycollegiate-development/computational-mathematics-2026-2027.git**
4. Open it, then open `Unit 1 - Working with Numbers` → this lesson file

## Part 2: REPL time — the seven operators (~30 minutes)

Type `python3` to start the REPL, then work through each operator. Try every one.

### The operators
```
>>> 7 + 3      # addition
>>> 7 - 3      # subtraction
>>> 7 * 3      # multiplication
>>> 7 / 3      # division (always gives a float)
>>> 7 // 3     # floor division (chops off the decimal)
>>> 7 % 3      # modulo (the remainder after dividing)
>>> 7 ** 3     # exponent (7 to the power 3)
```

### Predict, then run (~20 min)
Before each line, write down what you think it prints. Then run it. Were you right?

1. `10 % 3` — what's left over when 10 is divided by 3?
2. `10 / 5` vs `10 // 5` — do they ever give the same answer?
3. `-7 // 2` — does floor division chop or floor? (Tuesday's surprise, again)
4. `2 ** 10` — how fast do powers grow?
5. `5 % 2` — what does this always give for an even number? For an odd number?

### Why % matters (the security lens)
- `x % 2 == 0` is how programs test "is this number even?" — used everywhere
- `x % 10` gives the last digit of a number; `x // 10` chops it off — that's how you process digits one at a time
- Ask: why would a bank or a checksum care about the last digit?

## Part 3: Journal (last 5 minutes)

Create `journal-0909.md` in your home directory. Write 2-3 sentences:
- One real situation where `%` (remainder) is the useful operator
- Which operator surprised you most today, and why

## Turn in — SCREENSHOT

ONE screenshot of your terminal showing, in order:
`pwd`, the course repo `ls`, and your REPL outputs from Part 2 (all seven operators, plus the predict questions).
Submit it to the Classroom assignment before 11:59 PM. Keep your terminal open — I'll spot-check live screens.
