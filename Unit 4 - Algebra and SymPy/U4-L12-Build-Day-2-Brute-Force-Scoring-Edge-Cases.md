# U4 L12 — Build Day 2: Brute-Force Scoring and Edge Cases (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (in-class build day, 45 minutes)
**LO:** 4.2, 4.3 — upgrade brute force from dump-all-26 to ranked candidates; handle every edge case without tracebacks

---

## TODAY'S PURPOSE

Yesterday you had a brute-force that printed 26 lines. Today it must **rank** them so a human can pick the right one without reading all 26. You also harden every cipher against the inputs that will be thrown at it on demo day: empty strings, non-letters, degenerate keys, and the `gcd(a,26) != 1` trap.

---

## PART 1 — ENGLISH SCORING FOR BRUTE FORCE (20 min)

A raw frequency count is too noisy for short texts. Use a **bigram score** — count how many adjacent letter pairs look like English. This is 15 lines and beats frequency analysis on ciphertexts under 50 chars.

Add to `modkit.py`:

```python
# Common English bigrams (ordered pairs) — source: Norvig/Google Books
ENGLISH_BIGRAMS = {
    "th", "he", "in", "er", "an", "re", "on", "at", "en", "nd",
    "ti", "es", "or", "te", "of", "ed", "is", "it", "al", "ar",
    "st", "to", "nt", "ng", "se", "ha", "as", "ou", "io", "le",
    "ve", "co", "me", "de", "hi", "ri", "ro", "ic", "ne", "ea",
    "ra", "ce", "li", "ch", "ll", "be", "ma", "si", "om", "ur"
}


def bigram_score(text):
    """Count how many adjacent pairs are in ENGLISH_BIGRAMS. Higher = more English-like."""
    text = "".join(c.lower() for c in text if c.isalpha())
    if len(text) < 2:
        return 0
    score = 0
    for i in range(len(text) - 1):
        if text[i:i+2] in ENGLISH_BIGRAMS:
            score += 1
    return score


def brute_force_shift(text):
    """Return list of (key, plaintext, score) sorted by score DESC."""
    results = []
    for k in range(26):
        plain = shift_cipher(text, k, decrypt=True)
        results.append((k, plain, bigram_score(plain)))
    results.sort(key=lambda x: x[2], reverse=True)
    return results
```

Update `toolkit.py` brute output to show scores:

```python
elif args.cipher == "brute":
    from modkit import brute_force_shift
    if args.text is None:
        print("brute needs --text", file=sys.stderr)
        sys.exit(1)
    candidates = brute_force_shift(args.text)
    for k, plain, score in candidates:
        print(f"k={k:2d} score={score:2d} -> {plain}")
```

- ☐ `bigram_score` and updated `brute_force_shift` in `modkit.py`
- ☐ `toolkit.py` prints scored, sorted output
- ☐ Test: `python3 toolkit.py --cipher brute --text "khear"` — top result should be `k=6 score=2 -> hello` (bigrams: he, ll)
- ☐ `git commit -am "L12: bigram scoring for brute force" && git push`

---

## PART 2 — EDGE CASE HARDENING (20 min)

Every cipher must handle these without a traceback. Write the test **first**, then make it pass.

| case | input | expected behavior |
|---|---|---|
| empty string | `--text ""` | prints empty line, exit 0 |
| no letters | `--text "1234!@#$"` | prints input unchanged, exit 0 |
| shift key 0 | `--key 0` | identity (no change) |
| shift key 26 | `--key 26` | identity (mod 26) |
| shift key -1 | `--key -1` | same as key 25 |
| affine a=4 | `--key 4 --b 7` | clear error: "a=4 not invertible mod 26" |
| affine a=13 | `--key 13 --b 0` | clear error: "a=13 not invertible mod 26" |
| affine n=1 | (not user-facing) | internal: degenerate modulus handled |

**Affine error message rule:** The user must learn *what* is wrong, not *where* it crashed. `ValueError("a=4 has no inverse mod 26; choose a in {1,3,5,7,9,11,15,17,19,21,23,25}")` is good. `ValueError("pow() 2nd argument cannot be negative when 3rd argument specified")` is not.

- ☐ All eight rows tested, all behave as specified
- ☐ No traceback reaches the user for any row
- ☐ Error messages name the invalid value and the valid set
- ☐ `git commit -am "L12: edge cases hardened" && git push`

---

## PART 3 — EXPAND TEST DRIVER (5 min)

Add these tests to `test_toolkit.py`:

```python
def test_brute_ranks_correctly():
    out, err, code = run(["--cipher", "brute", "--text", "khear"])
    assert code == 0
    lines = out.strip().split("\n")
    top = lines[0]
    assert "k=6" in top and "hello" in top, f"top candidate wrong: {top}"
    # scores should be non-increasing
    scores = [int(l.split("score=")[1].split()[0]) for l in lines if "score=" in l]
    assert all(scores[i] >= scores[i+1] for i in range(len(scores)-1)), "scores not sorted"
    return True


def test_edge_cases():
    # empty
    out, err, code = run(["--cipher", "shift", "--key", "5", "--text", ""])
    assert code == 0 and out == ""
    # no letters
    out, err, code = run(["--cipher", "shift", "--key", "5", "--text", "123!@#"])
    assert code == 0 and out == "123!@#"
    # key 0
    out, err, code = run(["--cipher", "shift", "--key", "0", "--text", "hello"])
    assert code == 0 and out == "hello"
    # key 26
    out, err, code = run(["--cipher", "shift", "--key", "26", "--text", "hello"])
    assert code == 0 and out == "hello"
    # key -1
    out, err, code = run(["--cipher", "shift", "--key", "-1", "--text", "hello"])
    assert code == 0 and out == "gdkkn"
    # affine non-invertible
    out, err, code = run(["--cipher", "affine", "--key", "4", "--b", "7", "--text", "hello"])
    assert code != 0 and "invertible" in err.lower()
    return True
```

- ☐ All new tests pass
- ☐ `python3 test_toolkit.py` still prints `all tests passed`
- ☐ `git commit -am "L12: expanded test driver" && git push`

---

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. **Output of `toolkit.py --cipher brute --text "khear"`** showing top 5 lines with scores
2. **Output of each edge case** (8 rows) showing actual behavior
3. **Output of `python3 test_toolkit.py`** — all tests passed
4. **One sentence**: which edge case was hardest to handle cleanly, and why?

---

## 📋 TOMORROW

**Next:** L13 — Build Day 3. Frequency analysis as a *second* scoring signal (combine with bigrams), and the written defense (README) gets its first real draft. The manifest must verify on every run, not just on demand.

**Reminder:** CNY break starts Feb 3 (half day). You have L13, L14, L15, then the break. Use the break for polish, not first-time coding.

## 🇹🇼 TAIWAN CONTEXT

The `gcd(a,26) != 1` failure mode is not academic. The affine cipher with a non-invertible `a` is a **many-to-one** map — multiple plaintexts encrypt to the same ciphertext. This is exactly the class of bug that let the ROC's early custom encryption be broken: they chose parameters that *looked* random but had hidden structure. A cipher that refuses bad keys is honest. One that silently produces collisions is the dangerous one.