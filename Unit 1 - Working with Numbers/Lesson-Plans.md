# Unit 1 — Working with Numbers (Ch 1)

**Duration:** ~3-4 weeks
**Project:** Calculator with Guardrails
**Rhythm:** Coding and reflection sessions

---

## Book Topics (in order)

1. Basic math operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
2. Number types (int, float, complex, Fraction, Decimal)
3. User input and conversion
4. Iterative computation (loops for math)
5. Unit conversions (real-world application)
6. Finding factors and multiples

## Security Lens

- **Input validation** — never trust user input; what happens when you pass a string to a math function?
- **Integer overflow** — what happens with very large numbers? Python vs other languages vs real systems
- **Safe arithmetic** — why dividing by zero crashes, what a program should do instead
- **Real-world:** Therac-25 (integer overflow in radiation therapy), Ariane 5 (float-to-int conversion failure)

## Project: Calculator with Guardrails

Students build a multi-function calculator that handles:
- Basic arithmetic with input validation
- Unit conversion (temperature, distance, weight)
- Error handling for edge cases (divide by zero, invalid input, overflow)
- *Stretch:* A "safe mode" that limits operations based on context

**Codespaces repo:** Created via GitHub Classroom — private per student.

---

## Suggested Week Breakdown

### Week 1: Python Basics + Input
| Session | Topic | Format |
|-----|-------|--------|
| 1 | REPL crash course, variables, basic math ops | Code-along |
| 2 | Reflection: "What's the difference between `3/2` and `3//2`?" + journal | Discussion |
| 3 | User input, type conversion, string → number | Code-along |
| 4 | Unplugged: Input validation flowchart | Paper activity |
| 5 | Lab: Simple calculator (no guardrails yet) | Lab time |

### Week 2: Loops + Error Handling
| Session | Topic | Format |
|-----|-------|--------|
| 1 | `while` loops for continuous calculation, `try/except` | Code-along |
| 2 | Case study: Therac-25 and what happens when input isn't validated | Discussion |
| 3 | Unit conversion functions | Code-along |
| 4 | Reflection: "What inputs could break your calculator?" — write test cases | Journal |
| 5 | Lab: Add error handling to calculator | Lab time |

### Week 3: Project Work
| Session | Topic | Format |
|-----|-------|--------|
| 1 | Stretch concepts: types of numbers (Fraction, Decimal) | Mini-lesson |
| 2 | Peer review: swap calculators, try to break each other's | Pair activity |
| 3 | Project work | Lab time |
| 4 | Reflection: "What's the most surprising thing your code can't handle?" | Journal |
| 5 | Project due + showcase | Presentations |

---

## Old Materials Recycled

| Resource | From | New Home |
|----------|------|----------|
| Basic math operations REPL worksheet | v0.200 Sprit Project | Unit 1 Worksheets/ |
| Comparison operators activity | v0.200 (same source) | Unit 1 Worksheets/ |

## Assessment

- Weekly 5-question quiz (last 10 min)
- Project rubric: validates input (30%), handles edge cases (30%), core functionality (30%), stretch (10%)
- Reflection entries graded on thoughtfulness (check/check-plus/check-minus)