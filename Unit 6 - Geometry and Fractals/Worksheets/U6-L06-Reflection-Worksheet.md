# U6 L06 — Reflection: Recursion vs Iteration, Side by Side

Names: ___________________________  Date: Apr 19

Closed notes. Pencil. 45 minutes. Two implementations of the same algorithm, same answers, very different costs. You are arguing for which one ships, in writing, with evidence.

## 1: The evidence on the table

**Section A — Fibonacci, copied from a real run.**

| ----------------------- | ------------------ | ------------------------- |
| ------------------- | -------- | --------------------- |
| naive recursive     | 6765     | 21,891 function calls |
| memoised recursive  | 6765     | 39 function calls     |

**Section B — Ackermann.**

| --------------- | ---------- | ---------- |
| -------------- | -------- | -------- |
| `ack(2, 2)`    | 7        | 27       |
| `ack(2, 3)`    | 9        | 44       |
| `ack(3, 2)`    | 29       | 541      |

**Section C — Read the tables.**

1. Which implementation would you ship for a job that runs a million times a day? _______

2. Which would you ship if the input were a tree of unknown depth? _______

3. Those two answers are different. Why is that not a contradiction? _______

## 2: The real argument

**Section A — Fill the table.** For each shape of problem, name the approach and the reason.

| ------------------------------------ | ---------- | ----------- |
| -------------------------------- | -------- | -------- |
| a tree (files in folders)        |          |          |
| a string of N characters         |          |          |
| nested parentheses               |          |          |
| a grid you have to search        |          |          |
| a JSON document of unknown depth |          |          |

**Section B — The rule.** One sentence you could hand to a colleague:

> **Use __________ when __________. Use __________ when __________.**

4. Write that rule: _______

5. What is the worst case for each approach? _______

## 3: The third option

Recursion produces the data; an iterative function consumes it. For a directory tree, recursion is natural for *finding* the files because the structure nests. Once you have the list, sorting, filtering, and reporting are iterative, because they operate on a flat list.

```
recursive phase                    iterative phase
(returns a flat list of paths)     (sort, filter, report)
                |
                v
        the list is the contract
```

**Section A — Mark the boundary.** Draw the split on the axes below and label it.

6. Where does the recursion **stop**? _______

7. Where does the iterative part **begin**? _______

8. What is the type that crosses the boundary? _______

**Section B — Why this is the useful idea.**

9. Why is "a flat list" such a good boundary? One sentence: _______

10. Name a situation in a job you have had, or a job you want, where this same split applies: _______

## 4: The honest limit

**Section A — Both directions.**

11. Where does the recursive version have an advantage you cannot argue away? _______

12. Write one sentence you would put in a code review rejecting a recursive implementation: _______

13. Write one sentence you would put in a code review approving a recursive implementation over an iterative one: _______

Those two sentences are the deliverable.

___

**TURN IN** — This sheet, with sentences 12 and 13 written out in full.
