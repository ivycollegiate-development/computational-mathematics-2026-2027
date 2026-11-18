#!/usr/bin/env python3
"""Evidence audit for the Computational Mathematics program.

Emits the numbers cited in "Computational Mathematics Program — Rigor and
Innovativeness Assessment" so that any reader can regenerate them from the
repository instead of trusting the prose.

Every counting rule that the assessment depends on is a named constant below.
If a definition changes, it must change here, in one place, and the resulting
diff is the record of it.

Usage:
    python3 audit/audit.py              # writes audit/evidence.csv, audit/summary.md
    python3 audit/audit.py --print      # summary to stdout only

Standard library only. Run from anywhere inside the repository.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Definitions. These are the rules the assessment cites.
# --------------------------------------------------------------------------

# A lesson file is a Markdown file that sits directly in a unit directory and
# is named U<unit>-L<number><optional letter>-<title>.md. Lesson files in
# _archive/ are not lessons: they are superseded drafts.
LESSON_RE = re.compile(r"^U(?P<unit>\d+)-L(?P<num>\d+)(?P<suffix>[a-z]?)-.*\.md$")

# A unit directory is "Unit <n> - <title>" at the repository root.
UNIT_RE = re.compile(r"^Unit (\d+) - .+$")

# Excluded subtrees. Anything here is counted separately and never in the
# denominators below, because it is not taught material.
EXCLUDED_DIRS = {"_archive", ".git"}

# Token sets. Matching is case-insensitive substring search on the whole file.
# A lesson counts for a metric if ANY token in the set is present, except where
# a metric is defined as requiring ALL (see has_learning_objective, which looks
# for a heading-shaped marker, not a bare mention).
TOKENS = {
    # Hand-derivation instruction: the student works the item without code
    # before touching the keyboard.
    "hand_derivation": [
        "by hand",
        "hand-deriv",
        "by-hand",
        "without code",
        "no code",
        "no calculator",
        "on paper",
        "paper and pencil",
        "manually",
    ],
    # A numeric checkpoint: the lesson asks the student to state or check a
    # specific number, as opposed to a qualitative "does it work?".
    "numeric_checkpoint": [
        "checkpoint",
        "check yourself",
        "expected output",
        "sanity check",
        "check:",
        "verify:",
    ],
    # A closed-note paper check used as a graded item.
    "paper_check": ["paper check"],
    # Differentiation or intervention in the written lesson.
    "differentiation": ["differentiat", "reteach", "re-teach", "scaffold"],
    # Error, failure and epistemic-honesty content.
    "epistemic": [
        "false positive",
        "confound",
        "provenance",
        "wrong yardstick",
        "failure mode",
        "what is still broken",
        "error log",
        "source of error",
    ],
    # The security / privacy / forensic thread.
    "security_thread": [
        "privacy",
        "pii",
        "anonymi",
        "suppression",
        "generaliz",
        "hashing",
        "modular arithmetic",
        "forensic",
        "threat model",
        "base rate",
    ],
}

# Structural headers the assessment cites as inconsistently present.
# Each is matched as a heading-ish marker at the start of a line, so that a
# passing mention in prose ("we have no rubric for this") does not count.
# Matched at the start of a line. The lessons use a bold inline label
# ("**LO:** ...") rather than a heading, so both forms are accepted and a
# passing mention inside prose does not count.
HEADER_MARKERS = {
    "objective": r"^\*\*LO:|^#{1,6}\s*(\*\*)?\s*(learning\s+)?objectives?\b",
    "materials": r"^\*\*Materials?:|^#{1,6}\s*(\*\*)?\s*materials?\b",
    "time": r"^\*\*(estimated\s+)?time\b|^#{1,6}\s*(\*\*)?\s*(time|duration|timing)\b",
    "differentiation_header": r"^\*\*Differentiat|^#{1,6}\s*(\*\*)?\s*differentiation\b",
    "homework": r"^\*\*Homework|^#{1,6}\s*(\*\*)?\s*(homework|assignment)\b",
    "rubric": r"^\*\*Rubric|^#{1,6}\s*(\*\*)?\s*rubrics?\b",
}


@dataclass
class FileRecord:
    path: str
    kind: str
    unit: str | None
    words: int
    flags: dict = field(default_factory=dict)


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / ".git").exists():
            return parent
    sys.exit("not inside a git repository")


def classify(rel: Path) -> tuple[str, str | None]:
    """Return (kind, unit) for a repo-relative path."""
    parts = rel.parts
    unit = None
    unit_match = UNIT_RE.match(parts[0]) if parts else None
    if unit_match:
        unit = unit_match.group(1)

    if EXCLUDED_DIRS & set(parts[:-1]):
        return "archive" if "_archive" in parts else "other", unit
    if len(parts) == 2 and LESSON_RE.match(parts[1]):
        return "lesson", unit
    if len(parts) >= 3 and parts[1] == "Worksheets":
        if "Answer-Key" in parts[-1] or "answer-key" in parts[-1].lower():
            return "answer_key", unit
        return "worksheet", unit
    if len(parts) >= 3 and parts[1] == "Assessments":
        if "Answer-Key" in parts[-1]:
            return "answer_key", unit
        if parts[-1] == "README.md":
            return "readme", unit
        return "assessment", unit
    if len(parts) == 2 and parts[1] == "Lesson-Plans.md":
        return "planning", unit
    if len(parts) == 1:
        return "planning", None
    return "other", unit


def has_header(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE) is not None


def audit_file(root: Path, rel: Path) -> FileRecord | None:
    kind, unit = classify(rel)
    if kind == "other":
        return None
    text = (root / rel).read_text(encoding="utf-8", errors="ignore")
    low = text.lower()
    flags = {}
    for name, tokens in TOKENS.items():
        flags[name] = any(tok in low for tok in tokens)
    for name, pattern in HEADER_MARKERS.items():
        flags[name] = has_header(text, pattern)
    # "built around a paper check" is a title-level fact, not a keyword hit:
    # the lesson is named for the instrument it consists of.
    flags["paper_check_titled"] = "paper-check" in rel.name.lower()
    return FileRecord(
        path=str(rel),
        kind=kind,
        unit=unit,
        words=len(text.split()),
        flags=flags,
    )


def git_commit_count(root: Path) -> int | None:
    try:
        out = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=root, capture_output=True, text=True, check=True,
        )
        return int(out.stdout.strip())
    except (subprocess.CalledProcessError, ValueError):
        return None


def git_head(root: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root, capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except subprocess.CalledProcessError:
        return None


SUMMARY_METRICS = [
    # (column label, kind it applies to, flag name)
    ("lesson files", "lesson", None),
    ("worksheet files", "worksheet", None),
    ("answer keys", "answer_key", None),
    ("unit assessment papers", "assessment", None),
    ("lessons with a learning-objective header", "lesson", "objective"),
    ("lessons with a Materials header", "lesson", "materials"),
    ("lessons with a Time header", "lesson", "time"),
    ("lessons with a Differentiation header", "lesson", "differentiation_header"),
    ("lessons with a Homework header", "lesson", "homework"),
    ("lessons with a Rubric header", "lesson", "rubric"),
    ("lessons with hand-derivation instruction", "lesson", "hand_derivation"),
    ("lessons with a numeric checkpoint", "lesson", "numeric_checkpoint"),
    ("lessons built around a paper check (in title)", "lesson", "paper_check_titled"),
    ("lessons mentioning a paper check", "lesson", "paper_check"),
    ("lessons addressing differentiation/intervention", "lesson", "differentiation"),
    ("lessons with error/failure content", "lesson", "epistemic"),
    ("lessons carrying the security/privacy thread", "lesson", "security_thread"),
]


def build_summary(records: list[FileRecord]) -> list[tuple[str, int, int, float]]:
    rows = []
    for label, kind, flag in SUMMARY_METRICS:
        if flag is None:
            n = sum(1 for r in records if r.kind == kind)
            total = n
        else:
            n = sum(1 for r in records if r.kind == kind and r.flags.get(flag))
            total = sum(1 for r in records if r.kind == kind)
        pct = (n / total * 100) if total else 0.0
        rows.append((label, n, total, pct))
    return rows


def build_per_unit(records: list[FileRecord]) -> dict[str, dict[str, int]]:
    units: dict[str, dict[str, int]] = {}
    for r in records:
        if r.kind != "lesson" or r.unit is None:
            continue
        u = units.setdefault(r.unit, {"lessons": 0, "words": 0, "paper_check": 0,
                                      "hand_derivation": 0, "numeric_checkpoint": 0})
        u["lessons"] += 1
        u["words"] += r.words
        for flag in ("paper_check", "hand_derivation", "numeric_checkpoint"):
            if r.flags.get(flag):
                u[flag] += 1
    return dict(sorted(units.items(), key=lambda kv: int(kv[0])))


def write_csv(path: Path, records: list[FileRecord]) -> None:
    flag_names = sorted({k for r in records for k in r.flags})
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["path", "kind", "unit", "words", *flag_names])
        for r in sorted(records, key=lambda r: (r.kind, r.path)):
            w.writerow([r.path, r.kind, r.unit or "", r.words,
                        *[int(bool(r.flags.get(k))) for k in flag_names]])


def write_markdown(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--print", dest="to_stdout", action="store_true",
                    help="print the summary instead of writing files")
    args = ap.parse_args()

    root = repo_root()
    md_files = [
        p.relative_to(root)
        for p in sorted(root.rglob("*.md"))
        if ".git" not in p.parts
    ]
    records = [r for r in (audit_file(root, rel) for rel in md_files) if r]

    summary = build_summary(records)
    per_unit = build_per_unit(records)
    commits = git_commit_count(root)
    head = git_head(root)

    out = []
    out.append("# Evidence audit — Computational Mathematics")
    out.append("")
    out.append(f"Repository HEAD: `{head}`")
    out.append(f"Commits on HEAD: {commits}")
    out.append(f"Markdown files scanned: {len(records)}")
    out.append("")
    out.append("| Metric | Count | Denominator | Percent |")
    out.append("|---|---:|---:|---:|")
    for label, n, total, pct in summary:
        out.append(f"| {label} | {n} | {total} | {pct:.1f}% |")
    out.append("")
    out.append("| Unit | Lessons | Words | Paper checks | Hand derivation | Numeric checkpoints |")
    out.append("|---|---:|---:|---:|---:|---:|")
    for unit, v in per_unit.items():
        out.append(f"| {unit} | {v['lessons']} | {v['words']} | {v['paper_check']} "
                   f"| {v['hand_derivation']} | {v['numeric_checkpoint']} |")
    out.append("")
    out.append("Definitions are the constants in `audit/audit.py`; change them there, "
               "not in prose.")

    if args.to_stdout:
        print("\n".join(out))
        return

    write_csv(root / "audit" / "evidence.csv", records)
    write_markdown(root / "audit" / "summary.md", out)
    print("\n".join(out))
    print()
    print(f"wrote {root / 'audit' / 'evidence.csv'}")
    print(f"wrote {root / 'audit' / 'summary.md'}")


if __name__ == "__main__":
    main()
