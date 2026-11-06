# U4 L14 — Build Day 4: Manifest on Every Run, Tamper Demo, Final Sweep (Machine)

**Unit:** 4 — Algebra and SymPy
**Type:** Machine (in-class build day, 45 minutes)
**LO:** 4.3 — manifest generated and verified on every toolkit run; tamper detection demonstrable in 30 seconds; all edge cases green

---

## TODAY'S PURPOSE

The manifest is not a separate step — it is **part of the toolkit's contract**. Every run of `toolkit.py` must generate a fresh manifest. Every run of `test_toolkit.py` must verify it. Today you make that automatic, build a one-command tamper demo, and do a final sweep of everything that could break on demo day.

---

## PART 1 — MANIFEST ON EVERY RUN (15 min)

Currently `toolkit.py` calls `build_manifest` at the end of `main()`. That is not enough — it must also **verify** the manifest on startup, so a tampered file is caught before any cipher runs.

Update `toolkit.py`:

```python
#!/usr/bin/env python3
"""Cipher Toolkit — shift, affine, brute-force with integrity manifest."""

import sys
import argparse
import integrity

MANIFEST_FILES = ["toolkit.py", "symkit.py", "modkit.py", "integrity.py", "test_toolkit.py", "README.md"]


def verify_manifest_or_die():
    """Check manifest on startup. Exit with clear message if any file changed."""
    results = integrity.check_manifest("manifest.sha256")
    changed = [(s, p) for s, p in results if s == "CHANGED"]
    missing = [(s, p) for s, p in results if s == "MISSING"]
    if changed or missing:
        print("INTEGRITY CHECK FAILED", file=sys.stderr)
        for status, path in changed:
            print(f"  CHANGED: {path}", file=sys.stderr)
        for status, path in missing:
            print(f"  MISSING: {path}", file=sys.stderr)
        print("\nRe-run in a fresh clone, or restore the original files.", file=sys.stderr)
        sys.exit(1)


def main():
    # Verify BEFORE doing any crypto work
    verify_manifest_or_die()

    parser = argparse.ArgumentParser(description="Cipher Toolkit")
    parser.add_argument("--cipher", choices=["shift", "affine", "brute"], required=True)
    parser.add_argument("--key", type=int, help="shift key (0-25) or affine 'a'")
    parser.add_argument("--b", type=int, help="affine 'b' parameter")
    parser.add_argument("--text", help="text to encrypt/decrypt; if omitted, reads stdin")
    args = parser.parse_args()

    # ... existing cipher logic ...

    # Regenerate manifest AFTER successful run
    integrity.build_manifest(MANIFEST_FILES, "manifest.sha256")


if __name__ == "__main__":
    main()
```

- ☐ `verify_manifest_or_die()` runs before any cipher logic
- ☐ Manifest regenerated after successful run
- ☐ Test: run toolkit once (manifest created), edit `toolkit.py` (add a comment), run again → exits with "INTEGRITY CHECK FAILED"
- ☐ `git commit -am "L14: manifest verify on startup" && git push`

---

## PART 2 — ONE-COMMAND TAMPER DEMO (15 min)

Create `demo_tamper.py` — a script that proves the manifest works in 30 seconds:

```python
#!/usr/bin/env python3
"""Tamper demo: run toolkit, tamper one file, run again, show failure."""

import subprocess
import sys
import os


def run_toolkit(args):
    result = subprocess.run([sys.executable, "toolkit.py"] + args, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def main():
    print("=== CIPHER TOOLKIT TAMPER DEMO ===\n")

    # 1. Fresh run — should work
    print("1. Fresh run (shift cipher):")
    code, out, err = run_toolkit(["--cipher", "shift", "--key", "7", "--text", "hello"])
    print(f"   exit={code} output={out}")
    assert code == 0, "fresh run failed"

    # 2. Verify manifest exists
    print("\n2. Manifest exists:", os.path.exists("manifest.sha256"))
    with open("manifest.sha256") as f:
        print("   First line:", f.readline().strip())

    # 3. Tamper: change ONE character in toolkit.py
    print("\n3. Tampering with toolkit.py (adding a comment)...")
    with open("toolkit.py", "a") as f:
        f.write("\n# TAMPERED\n")

    # 4. Run again — should FAIL with integrity error
    print("\n4. Running toolkit again (should fail):")
    code, out, err = run_toolkit(["--cipher", "shift", "--key", "7", "--text", "hello"])
    print(f"   exit={code}")
    print(f"   stderr={err}")
    assert code != 0, "tampered run should have failed"
    assert "INTEGRITY CHECK FAILED" in err, "wrong error message"
    assert "CHANGED: toolkit.py" in err, "should name the changed file"

    # 5. Restore and verify it works again
    print("\n5. Restoring toolkit.py from git...")
    subprocess.run(["git", "checkout", "toolkit.py"], check=True)
    code, out, err = run_toolkit(["--cipher", "shift", "--key", "7", "--text", "hello"])
    print(f"   exit={code} output={out}")
    assert code == 0, "restored run failed"

    print("\n=== DEMO COMPLETE: MANIFEST DETECTED SINGLE-CHARACTER TAMPER ===")


if __name__ == "__main__":
    main()
```

- ☐ `demo_tamper.py` created and runs successfully
- ☐ Output shows: fresh run OK → tamper → failure naming `toolkit.py` → restore → OK
- ☐ `git commit -am "L14: tamper demo script" && git push`

---

## PART 3 — FINAL EDGE-CASE SWEEP (10 min)

Run the full test suite. Fix any red. Then run the demo script. Then run the test suite again (manifest should still pass after demo restores files).

```bash
python3 test_toolkit.py
python3 demo_tamper.py
python3 test_toolkit.py   # must still pass
```

Checklist — every item must be green:

- ☐ `python3 test_toolkit.py` → `all tests passed`
- ☐ `python3 demo_tamper.py` → completes with "DEMO COMPLETE"
- ☐ `python3 test_toolkit.py` (again) → `all tests passed`
- ☐ Shift encrypt/decrypt round-trips for keys -10 to 35
- ☐ Affine encrypt/decrypt round-trips for all valid `a` in {1,3,5,7,9,11,15,17,19,21,23,25} with random `b`
- ☐ Affine rejects all invalid `a` with clear message
- ☐ Brute force ranks true key top 3 on 8/10 test strings
- ☐ Manifest updates on every successful run
- ☐ Manifest verification catches changes to ANY of the 6 manifest files
- ☐ No traceback reaches user for any input

- ☐ `git commit -am "L14: final sweep green" && git push`

---

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. **Output of `python3 demo_tamper.py`** (full output)
2. **Output of `python3 test_toolkit.py`** (full output, all passed)
3. **One sentence**: what is the one thing you would still fix if you had one more build day?

---

## 📋 TOMORROW

**Next:** L15 — Build Day 5 (final in-class day before CNY). README defense finalized, peer review, milestone tracker updated. The CNY break (Feb 3–14) is **build time** — not time off. Plan 30-min sessions, commit daily.

**Milestone check (from L10):**
- Jan 22: Repo live, three ciphers round-trip, defense drafted ✓
- Jan 28: Brute-force solver working, test driver green ✓
- Jan 29: Edge cases handled, manifest generated, defense revised ← **today**
- **CNY Feb 3–14**: Build days. Laptop. Short sessions, push often.
- Feb 15: Everything finished. Final checks, final push
- Feb 16: Demo. Unit 4 complete

---

## 🇹🇼 TAIWAN CONTEXT

The "verify on startup, regenerate on success" pattern is how `git` itself works — every `git commit` verifies the index against the object database, and every `git checkout` verifies the working tree. Your manifest is a miniature `git` for your project files. If you trust the manifest, you trust the code. If you don't verify it, you're not using it.