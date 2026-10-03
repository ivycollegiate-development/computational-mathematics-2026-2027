# U6 L06 — Reflection: Recursion vs Iteration, Side by Side

**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.4 — defend a choice between two implementations of the same algorithm,
in writing, with evidence

---

**No laptop.** Pencil. the U6 L07 numbers are in front of you as your own
working.

Two implementations. Same answers. Very different costs. Today you argue about
which one to ship — because that is the actual job.

## PART 1 — THE EVIDENCE ON THE TABLE (10 min)

From Friday, copied from a real run:

| algorithm | result at n=20 | work done |
|---|---|---|
| iterative Fibonacci | 6765 | 20 loop passes |
| naive recursive | 6765 | **21,891 function calls** |
| memoised recursive | 6765 | **39 function calls** |

| algorithm | result | calls |
|---|---|---|
| `ack(2, 1)` | 5 | 14 |
| `ack(2, 2)` | 7 | 27 |
| `ack(2, 3)` | 9 | 44 |
| `ack(3, 2)` | 29 | 541 |

- ☐  In the first table, which implementation would you ship for a job that
     runs a million times a day? ______
- ☐  Which would you ship if the input were a *tree of unknown depth*? ______
- ☐  Those two answers are different. Why is that not a contradiction? ______

## PART 2 — THE REAL ARGUMENT (15 min)

The honest answer to "recursion or iteration" is **it depends on the shape of
the problem**, and you should be able to state the shape. Fill this in.

| the problem looks like… | use | because |
|---|---|---|
| a flat list of N things | | |
| a tree (files in folders) | | |
| a string of N characters | | |
| nested parentheses | | |
| a grid you have to search | | |
| a JSON document of unknown depth | | |

Now write the rule you will actually use, as a single sentence you could give
a colleague:

> **Use ______ when ______. Use ______ when ______.**

- ☐  My rule: ______
- ☐  What is the *worst* case for each? ______

## PART 3 — THE THIRD OPTION (12 min)

There is a third approach and it is the one professional code uses most: **make
the recursion produce data, and let an iterative function consume it.**

Think about a directory tree. Recursion is natural for *finding* the files
because the structure nests. But once you have the list, everything after that —
sorting, filtering, reporting — is iterative, because it is operating on a flat
list.

Draw this on the axes or in the space below, and label the boundary:

1. Where does the recursion **stop**?
2. Where does the iterative part **begin**?
3. What is the type that crosses the boundary? ______

```text
recursive phase                    iterative phase
(returns a flat list of paths)     (sort, filter, report)
                |
                v
        the list is the contract
```

- ☐  Why is "a flat list" such a good boundary? One sentence: ______
- ☐  This is the single most useful structural idea in the unit. Name a
     situation in a job you have had — or a job you want — where this same
     split applies: ______

## PART 4 — THE HONEST LIMIT (8 min)

- ☐  Where does the *recursive* version have an advantage you cannot argue
     away? ______
- ☐  Write one sentence you would put in a code review, rejecting a recursive
     implementation: ______
- ☐  Write one sentence you would put in a code review, *approving* a
     recursive implementation over an iterative one: ______

Those two sentences are the deliverable. They are what a professional writes.

## 🇹🇼 TAIWAN CONTEXT

The "flat list is the contract" idea is how large-scale log and network
analysis actually gets done, and it is worth seeing the shape outside the
classroom. Taiwan's national CERT incident feeds, and the traffic-analysis work
that supports them, all follow this shape: walk the structure recursively
because it nests (a directory, an incident's affected hosts, a pcap's packet
tree), flatten to a list, then do all the counting and comparison iteratively
because list operations are fast and vectorisable in the standard library and
recursion is not. The recursive part is where you *discover* things; the
iterative part is where you *decide* things. Keeping those two phases separate
is what makes the decision step testable.

**Next:** L07, Tue Apr 20 — laptop, and we build an actual fractal with the
`deco` pattern. Everything so far has been preparation for recursion that
earns its keep.
