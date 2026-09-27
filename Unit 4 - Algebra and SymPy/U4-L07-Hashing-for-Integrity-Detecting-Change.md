# U4 L07 — Hashing for Integrity: Detecting Change (Full Lab)

**Date:** Jan 13 (Wed)
**LO:** use a hash to detect that data changed, build a verifiable manifest, and explain what a hash does and does not prove.

Yesterday you found out what you do not know. Today we build the second half of
the Unit 4 story, and it is the half that answers a question you have probably
been circling since Unit 2: **how do you know a file is the one you think it
is?**

Modular arithmetic gave you ciphers — hiding data. Hashing gives you
**integrity** — proving data is unchanged. Same unit, opposite direction.

## PART 1 — WHAT A HASH IS (12 min, code-along)

A hash takes any input and produces a fixed-length output. In Python that is
one line in the standard library — no install, no SymPy.

```python
import hashlib

def digest(text):
    """Return the hex SHA-256 digest of a string."""
    return hashlib.sha256(text.encode()).hexdigest()

print(len(digest("hello")))                 # 64 characters, always
print(digest("hello"))
print(digest("hello") == digest("hello"))  # True - deterministic
```

- ☐  Run it on `"hello"` and `"Hello"`. One character of case changed. How much
     of the digest changed? ______
- ☐  Change one character in the middle of a 500-character string. What
     fraction of the 64 output characters changed? ______

**Almost all of them.** That is the *avalanche effect*, and it is the entire
engineering goal of a hash function. A tiny change in input should scramble
the whole output. Here are four hashes of four nearly identical strings:

```
sha256("0")[:8] = 5feceb66
sha256("1")[:8] = 6b86b273
sha256("2")[:8] = d4735e3a
sha256("3")[:8] = 4e074085
```

One digit in, sixteen completely different hex characters out.

- ☐  What would it mean if a change to the input changed only a few of the output
     characters? What attack does that enable? ______

If a small change produced a small change, an attacker could forge a modified
file that still passes the check. The avalanche is what makes the check
meaningful.

## PART 2 — BUILD THE INTEGRITY CHECKER (20 min)

`hashlib` is a standard library module, so this works anywhere. Create
`integrity.py`:

```python
"""integrity.py — detect change in data files with SHA-256.

Q1: What does a matching hash prove, and what does it NOT prove?
Q2: Why must the file be read in binary mode, not text mode?
Q3: What is the difference between a manifest and a signature?
Q4: Why can an attacker who can WRITE a file also change the manifest?
Q5: What does a hash chain add over a plain list of hashes?
"""

import hashlib
import os


def file_digest(path, chunk=8192):
    """SHA-256 of a file, read in binary chunks so it works on any size."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for block in iter(lambda: fh.read(chunk), b""):
                h.update(block)
    except OSError as exc:
        raise ValueError("cannot read %r: %s" % (path, exc))
    return h.hexdigest()


def build_manifest(paths, out_path="manifest.txt"):
    """Write one '<digest>  <path>' line per file. Returns the manifest as text."""
    lines = []
    for p in sorted(paths):
        lines.append("%s  %s" % (file_digest(p), p))
    body = "\n".join(lines) + "\n"
    with open(out_path, "w") as fh:
        fh.write(body)
    return body


def check_manifest(manifest_path="manifest.txt"):
    """Return a list of (status, path) for every entry in the manifest."""
    results = []
    with open(manifest_path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            expected, path = line.split("  ", 1)
            if not os.path.exists(path):
                results.append(("MISSING", path))
            elif file_digest(path) == expected:
                results.append(("OK", path))
            else:
                results.append(("CHANGED", path))
    return results
```

Now make it real:

```python
import os
import integrity

os.makedirs("data", exist_ok=True)
rows = [
    "2026-01-05,09:14,alice,login,ok",
    "2026-01-05,09:16,bob,login,fail",
    "2026-01-05,09:20,alice,export,ok",
]
for i, row in enumerate(rows, 1):
    with open("data/log_%d.csv" % i, "w") as fh:
        fh.write(row + "\n")

paths = ["data/log_%d.csv" % i for i in range(1, 4)]
print(integrity.build_manifest(paths))
print("---")
for status, path in integrity.check_manifest():
    print("%-8s %s" % (status, path))
```

Now **tamper with it** and re-check. Change **exactly one character** in
`log_2.csv` — the `f` in `fail` to an `F` — and run `check_manifest()` again.
One character, not two.

| file | digest before (first 12) | status before | digest after | status after |
|---|---|---|---|---|
| `log_1.csv` | | | | |
| `log_2.csv` | | | | |
| `log_3.csv` | | | | |

Observed on this machine, for reference:

```
# before tampering
OK       data/log_1.csv
OK       data/log_2.csv
OK       data/log_3.csv

# after changing ONE character in log_2.csv
OK       data/log_1.csv   c631fec0c200
CHANGED  data/log_2.csv   4bb5e7daa670    (was 03126db3b6a2)
OK       data/log_3.csv   a9a6e3b7abb5
```

- ☐  Which file changed status, and what is the new digest prefix? ______
- ☐  Compare the old and new digest of `log_2.csv`. **How many of the 64 hex
     characters stayed the same?** ______

Zero is the answer, and that is the point. One character of damage scrambled
all sixty-four. The other two files are untouched, which is what makes this
usable for real triage: you learn **which** file changed, not just that
something did.

## PART 3 — THE HASH CHAIN (15 min)

A flat manifest has one weakness worth fixing: an attacker who can edit a
file can also edit the manifest. Chaining removes that, because each record
commits to everything before it.

```python
def chain(records):
    """Fold a list of records into one chained digest.

    Each step hashes the previous digest together with the new record, so
    changing record 2 changes the final digest even if record 3 is untouched.
    """
    h = "0" * 16
    for r in records:
        h = hashlib.sha256((h + r).encode()).hexdigest()[:16]
    return h


good = ["a", "b", "c"]
bad  = ["a", "x", "c"]
print(chain(good))    # 67448d983cd331c9
print(chain(bad))     # db9ee42c67d1b601
```

- ☐  Both are 16 hex characters. How many possibilities for the second record
     does that leave an attacker who knows the format? ______
- ☐  Chaining protects the *order and contents*. What does it still not
     prevent? ______

The answer to the second blank is the honest limitation: an attacker who can
recompute the whole chain can still produce a valid chain over false data. This
is what a **signature** is for — and a signature needs a private key, which a
hash does not have.

- ☐  State the difference in one sentence: a hash proves the data has not
     changed **since someone wrote the hash down**; a signature proves **who**
     wrote it. What does the first fail to establish? ______

## PART 4 — WHAT A HASH DOES NOT PROVE (10 min, discussion, write it down)

This is the graded intellectual content of the lesson, and it is a security
idea, not a Python one.

A hash is a **one-way function**. Three claims people make that are all false:

| claim | true? | why not |
|---|---|---|
| "the hash is encrypted" | | |
| "you can decrypt a hash to get the data back" | | |
| "matching hashes mean the data is correct" | | |

Fill in the **why not** column yourself:

- ☐  claim 1: ______
- ☐  claim 2: ______
- ☐  claim 3: the hash proves the bytes are **unchanged**, not **correct**.
     So what happens if the data was wrong *before* it was hashed? ______

That last one is the entire distinction. Integrity is not accuracy. A file full
of lies, hashed honestly, has a perfectly valid digest and will pass every
check you have. **The manifest tells you nothing changed. It cannot tell you
anything was true.**

- ☐  A log file where an attacker has both write access and the manifest. Can
     you detect the tampering with hashing alone? Yes / No, because ______

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. `integrity.py` pushed, with its five-question docstring answered
2. Your **Part 2 output before tampering and after tampering**, both pasted
3. Your **Part 4 table**, all three claims answered with a reason
4. One paragraph: the difference between integrity and authenticity, written
   for someone who has never heard the word "signature"

**Part 4 is the graded part.** Producing a working manifest is a five-minute
task with a working answer online. Knowing that hashing cannot establish who
wrote the data is the thing that separates a student who has used a hash from
a student who understands one.

## 📋 PREVIEW OF TOMORROW

**Next:** L08, Thu Jan 14 — paper, and the day your error log gets used. We take
the Unit 4 algebra errors you have been collecting since L02, classify them by
root cause, and find out whether you have one habit causing most of them.

**Bring tomorrow:** your error log, your L06 diagnostic, and your six-day plan.
Pencils. No laptop.

## 🇹🇼 TAIWAN CONTEXT

This exact pattern is how package managers and container registries work: they
publish a manifest of digests, and a pull fails loudly if any file's digest does
not match what the manifest promised. It is also, in weaker form, how Taiwan's
national ID card checksum digit works — the last digit is not part of your ID
number's meaning, it is there so a mistyped digit fails a modular check instead
of silently becoming a different person. That is the modular arithmetic from
Monday, used as an error detector, which is a third thing modular arithmetic
does after ciphers and ciphers' inverses.
