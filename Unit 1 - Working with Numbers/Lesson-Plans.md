# Unit 1 — Working with Numbers (Ch 1)

**Duration:** ~3-4 weeks
**Project:** Calculator with Guardrails
**Rhythm:** M-W-F coding · T-Th reflection

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
| Day | Topic | Format |
|-----|-------|--------|
| M | REPL crash course, variables, basic math ops | Code-along |
| T | Reflection: "What's the difference between `3/2` and `3//2`?" + journal | Discussion |
| W | User input, type conversion, string → number | Code-along |
| Th | Unplugged: Input validation flowchart | Paper activity |
| F | Lab: Simple calculator (no guardrails yet) | Lab time |

### Week 2: Loops + Error Handling
| Day | Topic | Format |
|-----|-------|--------|
| M | `while` loops for continuous calculation, `try/except` | Code-along |
| T | Case study: Therac-25 and what happens when input isn't validated | Discussion |
| W | Unit conversion functions | Code-along |
| Th | Reflection: "What inputs could break your calculator?" — write test cases | Journal |
| F | Lab: Add error handling to calculator | Lab time |

### Week 3: Project Work
| Day | Topic | Format |
|-----|-------|--------|
| M | Stretch concepts: types of numbers (Fraction, Decimal) | Mini-lesson |
| T | Peer review: swap calculators, try to break each other's | Pair activity |
| W | Project work | Lab time |
| Th | Reflection: "What's the most surprising thing your code can't handle?" | Journal |
| F | Project due + showcase | Presentations |

---

## Old Materials Recycled

| Resource | From | New Home |
|----------|------|----------|
| Basic math operations REPL worksheet | v0.200 Sprit Project | Unit 1 Worksheets/ |
| Comparison operators activity | v0.200 (same source) | Unit 1 Worksheets/ |

## Assessment

- Weekly 5-question quiz (Friday, last 10 min)
- Project rubric: validates input (30%), handles edge cases (30%), core functionality (30%), stretch (10%)
- T-Th reflection entries graded on thoughtfulness (check/check-plus/check-minus)