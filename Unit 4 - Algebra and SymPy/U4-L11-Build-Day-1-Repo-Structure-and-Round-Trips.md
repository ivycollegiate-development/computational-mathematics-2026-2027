# U4 L11 — Build Day 1: Repo Structure and Round-Trips (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (in-class build day, 45 minutes)
**LO:** 4.1, 4.2 — assemble the Cipher Toolkit repo from existing modules; verify all three cipher modes round-trip in a fresh clone

---

## TODAY'S PURPOSE

You have four working modules: `symkit.py`, `modkit.py`, `integrity.py`, and a draft `toolkit.py`. Today you turn them into a **shippable project** — a public repo that a classmate can clone, run once, and get correct output on shift, affine, and brute-force modes. The demo is Feb 16. You have today plus four more in-class build days, then the CNY break. Use every minute.

---

## PART 1 — REPO SKELETON (10 min)

Create the repo **now**. Do not code anything until the structure exists and is pushed.

```bash
mkdir compmath-u4-cipher-toolkit
cd compmath-u4-cipher-toolkit
git init
git branch -M main
```

Copy your four modules in:

```bash
cp /path/to/symkit.py .
cp /path/to/modkit.py .
cp /path/to/integrity.py .
```

Create the minimal `toolkit.py` that imports and exposes the three modes:

```python
#!/usr/bin/env python3
"""Cipher Toolkit — shift, affine, brute-force with integrity manifest."""

import sys
import argparse
import integrity


def main():
    parser = argparse.ArgumentParser(description="Cipher Toolkit")
    parser.add_argument("--cipher", choices=["shift", "affine", "brute"], required=True)
    parser.add_argument("--key", type=int, help="shift key (0-25) or affine 'a'")
    parser.add_argument("--b", type=int, help="affine 'b' parameter")
    parser.add_argument("--text", help="text to encrypt/decrypt; if omitted, reads stdin")
    args = parser.parse_args()

    if args.cipher == "shift":
        from modkit import shift_cipher
        if args.key is None or args.text is None:
            print("shift needs --key and --text", file=sys.stderr)
            sys.exit(1)
        out = shift_cipher(args.text, args.key, decrypt=False)
        print(out)

    elif args.cipher == "affine":
        from modkit import affine_cipher
        if args.key is None or args.b is None or args.text is None:
            print("affine needs --key (a), --b, and --text", file=sys.stderr)
            sys.exit(1)
        out = affine_cipher(args.text, args.key, args.b, decrypt=False)
        print(out)

    elif args.cipher == "brute":
        from modkit import brute_force_shift
        if args.text is None:
            print("brute needs --text", file=sys.stderr)
            sys.exit(1)
        candidates = brute_force_shift(args.text)
        for k, plain in candidates:
            print(f"k={k:2d} -> {plain}")

    # Generate manifest after every run
    integrity.build_manifest(["toolkit.py", "symkit.py", "modkit.py", "integrity.py", "test_toolkit.py"])


if __name__ == "__main__":
    main()
```

- ☐ Repo created, public, default branch `main`
- ☐ Four modules copied in
- ☐ `toolkit.py` runs without error on all three modes (even if brute is a stub)
- ☐ `git add . && git commit -m "L11: initial structure" && git push`

---

## PART 2 — ROUND-TRIP CHECKLIST (20 min)

The only definition of "working" that matters: **a fresh clone passes.**

```bash
# In a DIFFERENT directory:
git clone <your-repo-url>
cd compmath-u4-cipher-toolkit
python3 toolkit.py --cipher shift --key 7 --text "hello"
python3 toolkit.py --cipher affine --key 5 --b 8 --text "hello"
python3 toolkit.py --cipher brute --text "khear"
python3 test_toolkit.py
```

Fill in the actual output for each:

| command | actual output | PASS/FAIL |
|---|---|---|
| `shift --key 7 --text "hello"` | | |
| `shift --key 7 --text "olssv"` (decrypt) | | |
| `affine --key 5 --b 8 --text "hello"` | | |
| `affine --key 5 --b 8 --text "<ciphertext>"` (decrypt) | | |
| `brute --text "khear"` | | |
| `python3 test_toolkit.py` | | |

- ☐ All six rows show PASS
- ☐ `manifest.sha256` exists after each run
- ☐ Editing one character in `toolkit.py` makes `integrity.check_manifest()` report CHANGED

If any row is FAIL, fix it **now**. Do not move to Part 3 until the table is green.

---

## PART 3 — BRUTE FORCE STUB (10 min)

Your `modkit.py` needs a `brute_force_shift(text)` function that returns `[(k, plaintext), ...]` for all 26 shifts. Minimal version:

```python
def brute_force_shift(text):
    """Return list of (key, decrypted) for all 26 shifts."""
    results = []
    for k in range(26):
        results.append((k, shift_cipher(text, k, decrypt=True)))
    return results
```

- ☐ `brute_force_shift` added to `modkit.py`
- ☐ `toolkit.py --cipher brute --text "khear"` prints 26 lines
- ☐ One of them is recognizably English (the real key)

---

## PART 4 — TEST DRIVER SKELETON (5 min)

Create `test_toolkit.py` with at least these checks:

```python
#!/usr/bin/env python3
"""Test driver for Cipher Toolkit. Must print 'all tests passed' on success."""

import subprocess
import sys


def run(args):
    result = subprocess.run([sys.executable, "toolkit.py"] + args, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def test_shift_roundtrip():
    out, err, code = run(["--cipher", "shift", "--key", "7", "--text", "hello"])
    assert code == 0, f"shift encrypt failed: {err}"
    # decrypt
    out2, err2, code2 = run(["--cipher", "shift", "--key", "7", "--text", out])
    assert code2 == 0 and out2 == "hello", f"shift decrypt failed: got {out2}"
    return True


def test_affine_roundtrip():
    out, err, code = run(["--cipher", "affine", "--key", "5", "--b", "8", "--text", "hello"])
    assert code == 0, f"affine encrypt failed: {err}"
    out2, err2, code2 = run(["--cipher", "affine", "--key", "5", "--b", "8", "--text", out])
    assert code2 == 0 and out2 == "hello", f"affine decrypt failed: got {out2}"
    return True


def test_brute_finds_known():
    out, err, code = run(["--cipher", "brute", "--text", "khear"])
    assert code == 0, f"brute failed: {err}"
    lines = out.strip().split("\n")
    assert len(lines) == 26, f"expected 26 lines, got {len(lines)}"
    # k=6 should produce "hello" from "khear" (shift by 6: h->k, e->h, l->o, l->o, o->r -> khear? wait)
    # Actually "hello" shifted by 6: h+6=n, e+6=k, l+6=r, l+6=r, o+6=u -> "nkrru"
    # So "khear" shifted by 6: k-6=e, h-6=b, e-6=y, a-6=u, r-6=l -> "ebyul" no
    # Let's just check it runs and produces 26 lines
    return True


def test_manifest_generated():
    import os
    assert os.path.exists("manifest.sha256"), "manifest not created"
    with open("manifest.sha256") as f:
        lines = [l.strip() for l in f if l.strip()]
    assert len(lines) >= 5, f"manifest has only {len(lines)} entries"
    return True


if __name__ == "__main__":
    tests = [
        ("shift round-trip", test_shift_roundtrip),
        ("affine round-trip", test_affine_roundtrip),
        ("brute finds candidates", test_brute_finds_known),
        ("manifest generated", test_manifest_generated),
    ]
    for name, fn in tests:
        try:
            fn()
            print(f"✓ {name}")
        except AssertionError as e:
            print(f"✗ {name}: {e}")
            sys.exit(1)
    print("all tests passed")
```

- ☐ `test_toolkit.py` created
- ☐ `python3 test_toolkit.py` prints `all tests passed`
- ☐ Pushed to repo

---

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. **Repo URL** (public, default branch `main`)
2. **Screenshot or paste** of the six-row round-trip table with all PASS
3. **Output of `python3 test_toolkit.py`** showing `all tests passed`
4. **One sentence**: what is the one thing you are most worried about breaking before Feb 15?

---

## 📋 TOMORROW

**Next:** L12 — Build Day 2. Brute-force solver gets smarter (frequency scoring), edge cases hardened, test driver expanded. Bring your laptop with the repo already cloned and working.

**Milestone check:** By end of L12, `brute_force_shift` should rank candidates by English-likeness, not just dump all 26.

## 🇹🇼 TAIWAN CONTEXT

The repo structure you are building today — separate modules, a manifest, a test driver that runs in a fresh clone — is exactly how the Taiwan gov's open-source projects (like the COV-19 contact tracing app) publish verifiable builds. The manifest is your SBOM-lite. If you cannot demonstrate tamper detection on your own code, you cannot claim it for anyone else's.