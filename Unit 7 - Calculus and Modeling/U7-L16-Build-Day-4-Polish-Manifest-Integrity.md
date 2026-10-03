# U7 L16 — Build Day 4: Polish, Manifest, Integrity

**Unit:** 7 — Calculus and Modeling
**Type:** Machine lesson (45 minutes)
**LO:** 7.5 — verify a submitted artifact is reproducible and internally
consistent

---

**Laptop today.** The analyzer is due. Today you prove it is the thing you
think it is, and you find out what a hash is actually *for*.

## PART 1 — REPRODUCIBILITY FIRST (12 min)

Before any polish, the artifact must do the same thing on someone else's
machine. In order of severity:

- ☐  Does it run from a clean shell, in a different directory? ______
- ☐  Does it depend on the file path you happened to use? ______
- ☐  Does it read anything it does not create? ______
- ☐  Would it work if the CSV rows were in a different order? ______
- ☐  Does the output depend on dictionary iteration order? ______

That last one bites in Python more than students expect. A report that iterates
a `dict` and prints the results is deterministic on one Python version and
potentially not on another. If any output ordering matters to your defense,
**sort the keys explicitly.**

```python
thresholds = {"k=2": 2.0, "k=3": 3.0}
series = [1.0] * 8

def evaluate(series, k):
    return {"caught": [], "false": []}

for k in sorted(thresholds):
    row = evaluate(series, thresholds[k])
    print(k, row["caught"], row["false"])
```

Real output — note the keys come out in sorted order regardless of the order
they were written into the dict:

```text
k=2 [] []
k=3 [] []
```

- ☐  Add that sort, then re-run and diff against your previous output. Did
     anything change? ______

## PART 2 — THE MANIFEST (12 min)

A manifest says what is in the deliverable and proves it has not changed since
you finished it.

```python
import hashlib, os

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

# point this at YOUR project directory before running
os.chdir("/Users/pauljonessr/.hermes/cache/scratch/u67run")

for name in sorted(os.listdir(".")):
    if name.startswith("u7_") and name.endswith(".py"):
        print("%-24s %s" % (name, sha256(name)[:16]))
```

- ☐  Run it. What are the first four characters of your `atkit.py` hash? ______
- ☐  **Now run it again, unchanged. Same hash?** ______
- ☐  **Add a comment to `atkit.py` — a blank line, nothing else. What happens?**
     ______
- ☐  So what is the hash sensitive to, and what is it *for*? ______

For reference, here is what mine printed on two consecutive runs, against
real files in my project directory:

```text
u7_a.py                  3693c970cb642958
u7_b.py                  13c4f9db91a79161
u7_c.py                  499f626b4b938c9e
u7_d.py                  0ca47f1232d9b1f2
--- rerun (should be identical) ---
u7_a.py                  3693c970cb642958
u7_b.py                  13c4f9db91a79161
u7_c.py                  499f626b4b938c9e
u7_d.py                  0ca47f1232d9b1f2
```

Identical, as it must be. Note what the first sixteen characters are actually
doing there: they are a **display abbreviation**, not the hash. The real digest
is 64 hex characters. Showing 16 means collisions are more likely than they
need to be — fine for a human sanity check, and worth saying so rather than
letting the reader assume the short form is a complete fingerprint.

**The lesson is the difference between integrity and intent.** A hash proves a
file has not changed *since you hashed it*. It does not prove the code is
correct, does not prove you wrote it, and does not prove it does what its
README claims. A tampered file with a matching hash is a perfectly consistent
lie.

- ☐  So what would you need, to catch a *deliberately altered* file? ______
- ☐  And a hash recorded **in the repository** makes that possible, because an
     attacker who edits the code would have to edit the recorded hash too. So
     is committing the manifest sufficient? ______

It is sufficient only if the history is public and append-only. It is not
sufficient if you can rewrite both in one commit — which is exactly the state
you are in on a personal project with one author. Say so honestly in the
README rather than implying a guarantee you do not have.

- ☐  Write that caveat in one sentence: ______

## PART 3 — THE INTEGRITY CHECK THAT ACTUALLY MATTERS (12 min)

Hashes are cheap and mostly decorative. This check is the one that catches real
problems, and it is the same theme as Unit 4's Cipher Toolkit.

- ☐  **Does the code in the repo match the code that produced the numbers in
     your defense?** Re-run every number and compare: ______
- ☐  **Do the numbers in your defense appear anywhere in the program output, or
     did you type them in by hand?** ______
- ☐  If you typed them by hand, that is a defect. Fix it by having the program
     print them, and paste the output. Which numbers were typed? ______
- ☐  **Is the threshold in the code the same number as the threshold in your
     defense?** ______

That last pair is the classic and it has bitten every project-based course:
the code says `k = 3`, the write-up says "3.0", the slides say "about 3", and a
reader cannot tell which is authoritative. **One source of truth.** The
constants live in the code; the prose refers to them; the output prints them.

- ☐  Name every number that appears in your defense and where it comes from:
     ______
- ☐  Which of those is currently from memory rather than from the program?
     ______

## PART 4 — POLISH (9 min)

- ☐  The `SystemExit` guard message — read it as a user who has never seen the
       code. Is it clear, and does it avoid "pip install"? ______
- ☐  Every error message: does it say what went wrong **and** what to do? ______
- ☐  The README: can someone who has never met you run this in five minutes?
       ______
- ☐  Variable names: would you be embarrassed to show this to the demo? ______
- ☐  One last full run, timed. How long does it take? ______

## TURN IN — Build Day 4 Checklist

1. `manifest.py`, run, with its output in the README
2. A note in the README about what the hash does **not** prove
3. Every defense number traceable to program output — zero hand-typed figures
4. A `THRESHOLDS` / `MIN_POINTS` block that is the single source of truth
5. Explicitly sorted iteration anywhere output order could vary
6. `test_atkit.py` extended with one deliberately-broken-function test
7. A clean-shell run performed from a different directory, logged

## 🇹🇼 TAIWAN CONTEXT

Part 2's caveat is not pedantry, and the local context makes it sharper.
Hashes and manifests are routinely cited locally as evidence that an artifact
"has not been tampered with," and that inference is usually wrong in a way that
matters: a single-author artifact with a self-recorded hash proves only that it
has not been edited **since that author last ran the tool**. If the concern is
genuine integrity, the effective controls are external — a published digest in a
place the author does not control, a review, or a signature from a separate key
that never sits in the repository. Locally this is the same lesson as the
supply-chain discussion in Unit 4: the check has to live somewhere the party
being checked cannot quietly edit.

Part 3's number-provenance rule is the cheapest real improvement available to
any project and is almost never done. A defense where every figure is printed by
the program can be re-verified by the reader in a minute, and a defense with
hand-typed figures cannot be verified at all — not because they are wrong, but
because there is no way to tell. **Anything you cannot regenerate, you cannot
defend**, and the cost of generating it is one afternoon.

**Next:** L17, Tue May 25 — paper. Final defense revision.
