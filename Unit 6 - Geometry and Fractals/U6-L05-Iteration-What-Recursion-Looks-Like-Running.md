# U6 L05 — Iteration: What Recursion Looks Like When You Watch It Run

**Date:** Friday, April 16, 2027
**Unit:** 6 — Geometry and Fractals
**Type:** Machine lesson (45 minutes)
**LO:** 6.4 — write the same algorithm iteratively and recursively, and measure
what recursion costs

---

**Laptop today.** The point of today is to *watch* recursion work, because a
recursive function is invisible until you print from inside it.

**The security lens, up front.** Recursive descent appears constantly in parsing
— reading a log file, walking a directory tree, decoding nested JSON. A
recursive parser with no depth limit is a denial-of-service bug waiting for a
deeply nested input. You will build one on Monday. Today you learn what the
stack actually costs.

## PART 1 — THE SAME ALGORITHM, TWICE (12 min)

Type both. They do the same thing. That is the point.

```python
def countdown_iter(n):
    steps = []
    while n > 0:
        steps.append(n)
        n -= 1
    return steps

def countdown_rec(n, steps=None):
    if steps is None:
        steps = []
    if n <= 0:
        return steps
    steps.append(n)
    return countdown_rec(n - 1, steps)
```

The `steps=None` line is a **default argument**, and it is doing real work: the
list is created on the first call and then carried down every level. Without it
each level would build its own list and return one. This idiom appears in
production code constantly and it is worth being able to read it cold.

- ☐  You typed both
- ☐  You can say what the `n <= 0` line is doing and why it comes **before**
     the append
- ☐  In `countdown_rec`, what is the value of `steps` at the deepest call?
     ______

## PART 2 — THE EVIDENCE (10 min)

Real output, copied from a run:

```text
n = 5
  iterative: [5, 4, 3, 2, 1]
  recursive: [5, 4, 3, 2, 1]
  same? True
n = 5
  iterative: [5, 4, 3, 2, 1]
  recursive: [5, 4, 3, 2, 1]
  same? True
```

(The loop runs twice because the driver loops over `(5, 5)`. That is not a bug
in your recursion; that is a bad test loop I wrote, and noticing it is worth a
mark.)

- ☐  The two lists are identical. **What has this proved, and what has it not
     proved?** ______
- ☐  Write one input where the two would *disagree*: ______

## PART 3 — COST, MEASURED (14 min)

Real output, factorial both ways:

```text
factorial 1..10, recursive vs iterative
   1         1         1  match=True
   2         2         2  match=True
   3         6         6  match=True
   4        24        24  match=True
   5       120       120  match=True
   6       720       720  match=True
   7      5040      5040  match=True
   8     40320     40320  match=True
   9    362880    362880  match=True
  10   3628800   3628800  match=True
```

Identical results, ten times. Now the part that matters — **how many function
calls**:

```text
fib_rec(20) = 6765  function calls made = 21891
fib_iter(20) = 6765  loop passes = 20
```

Same answer. 6765 either way. But the recursive version made **21,891 calls**
and the iterative one made **20 loop passes** to get there.

- ☐  Why does naive recursive Fibonacci do so much extra work? In one
     sentence: ______
- ☐  Estimate: at `n = 25`, roughly how many calls? Use the pattern: ______
- ☐  Now write the recursive Fibonacci that **remembers** its answers
     (memoisation — pass a dict down, check it before recursing). How many
     calls does it make? Type it and run it: ______

Here is the real answer, so you can check yourself against it:

```text
n 10 value 55 calls 19
n 20 value 6765 calls 39
n 25 value 75025 calls 49
n 50 value 12586269025 calls 99
n 100 value 354224848179261915075 calls 199
```

**It is `2n - 1`, not `n + 1`.** Most people — including me on the first
draft — write down `n + 1` and it is wrong. Every *recomputed* value costs one
call, and every *memo hit* also costs one call even though it does no work.
There are `n` distinct values and about `n - 1` lookups, and the lookups are
real calls. From 21,891 calls at `n = 20` down to 39 is the win; the last factor
of two is the price of not checking before you recurse.

## PART 4 — WHERE IT ACTUALLY EXPLODES (9 min)

Real output:

```text
  ack(2, 1) =      5   calls =      14
  ack(2, 2) =      7   calls =      27
  ack(2, 3) =      9   calls =      44
  ack(3, 2) =     29   calls =     541
```

Look at the last two. The arguments barely changed and the call count went from
**44 to 541**.

- ☐  Python's default recursion limit is 1000. Estimate how deep you can go
     with `ack(3, 3)` before it blows up: ______
- ☐  **Do not actually run it.** Explain what you expect to see: ______
- ☐  The security question, and answer it properly: a JSON parser that
     recurses once per nesting level, fed a payload nested 2000 deep, what
     happens to the *server*, and what is the one-line fix? ______

**Next:** L06, Mon Apr 19 — we put recursion and iteration side by side on
paper, and you write the defense of when each one is right.

## TURN IN — Recursion and Iteration Checklist

1. Both versions of `countdown` in your repo, plus the memoised Fibonacci
2. Real output pasted: the factorial table, the fib call count, the ack table
3. Memoised Fibonacci's call count at `n = 20` — the number, not a claim
4. One sentence on why naive recursion is slow, in your own words
5. Your answer to the JSON-nesting question, naming the actual fix

## 🇹🇼 TAIWAN CONTEXT

The JSON-depth case is not a thought experiment. Stack-overflow crashes from
unbounded recursion have taken down production services over deeply nested
structured input, and the fix is always the same and always unglamorous: check
the depth, refuse with a clear error, and never let the exception be a raw
`RecursionError` traceback presented to a caller as though it were data. Same
principle as the U6 L02 `slope`: **a refused measurement must be loud, and it
must be labelled as a refusal.**
