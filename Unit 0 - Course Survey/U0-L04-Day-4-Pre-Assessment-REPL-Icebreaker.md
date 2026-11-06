# U0 L04 — Day 4: Pre-Assessment & REPL Icebreaker (PAPER + TECH)

**Unit:** 0 — Course Survey
**Type:** Paper (diagnostic) + Machine (REPL exploration, 45 minutes)
**LO:** complete a no-stakes math/programming diagnostic; explore Python REPL as a calculator

---

## TODAY'S PURPOSE

Last day of Unit 0. A short paper diagnostic (not graded, not returned) so I know where the class stands on Day 1 of Unit 1. Then your first real REPL session — just exploring, no assignment.

---

## PART 1 — PRE-ASSESSMENT (20 min)

**Materials:** Printed diagnostic (10 questions, 15 minutes). No calculator, no phone, no neighbor.

**Topics covered (all review from prior math):**
1. Solve for x: `3x - 7 = 14`
2. Evaluate: `(-2)^3 + 4 * 5`
3. Convert: 3.5 hours = ____ minutes
4. Which is larger: `2/3` or `0.66`?
5. `10^3 * 10^4 = 10^?`
6. If `f(x) = 2x + 1`, what is `f(5)`?
7. Order of operations: `8 + 2 * 5 - 3^2`
8. What is `15 % 4` in Python? (modulo/remainder)
9. True/False: `0.1 + 0.2 == 0.3` in most programming languages
10. One sentence: what does a loop do?

**Instructions:** Write your name. Do your best. Guess if unsure. Hand in when done. This does not affect your grade — it affects *how I teach Unit 1*.

---

## PART 2 — REPL ICEBREAKER (25 min)

Open your Codespace. Type `python3` and hit Enter. You're in the REPL (Read-Eval-Print Loop).

**Try these, one at a time. Predict what happens before you hit Enter.**

```python
# Arithmetic
2 + 3
10 - 4
5 * 6
20 / 4
20 // 4        # integer division
20 % 6         # modulo (remainder)
2 ** 10        # exponentiation

# Variables
x = 7
y = 3
x + y
x * y
x ** y

# Types
type(7)
type(7.0)
type("hello")
type(True)

# Strings
"hello" + "world"
"ha" * 3
"hello"[1]
"hello"[1:4]

# The famous float gotcha
0.1 + 0.2
0.1 + 0.2 == 0.3

# Math module
import math
math.sqrt(16)
math.pi
math.e
```

**No assignment.** Just play. Type things. Break things. The REPL doesn't bite — it just prints errors.

---

## PART 3 — WHAT YOU JUST DID (5 min)

The REPL is your **scratchpad for the year**.
- Every lesson that says "Machine" starts with the REPL
- Every bug you wonder about — test it in the REPL first
- `import this` shows the Zen of Python (try it)

---

## TURN IN

**Pre-assessment paper** — handed in before REPL time. Nothing else to submit.

---

## 📋 NEXT CLASS

**Unit 1 L01:** Working with Numbers — REPL, types, operators, first functions. Bring your Codespace ready.

---

## 🇹🇼 TAIWAN CONTEXT

The no-stakes diagnostic is standard practice in Taiwan's adaptive learning programs — the data shapes the pacing, not the grade. The REPL-first approach mirrors how the Industrial Technology Research Institute (ITRI) onboards new engineers: *play with the tool before you build with it*. If you can't explore it, you can't trust it.