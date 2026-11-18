# Evidence audit

Every count cited in `Computational Mathematics Program — Rigor and
Innovativeness Assessment` is produced here, from the repository, by one
script with no dependencies outside the standard library.

Purpose: the assessment should not contain a number that a reader cannot
regenerate. If a figure in the document and a figure in this output disagree,
the output is right and the document is stale.

## Run it

```bash
python3 audit/audit.py           # writes evidence.csv and summary.md, prints the summary
python3 audit/audit.py --print   # summary to stdout, writes nothing
```

Output is deterministic for a given commit. The summary records the commit it
was generated from, so a citation can name both the script and the SHA.

## What counts

The rules live as constants at the top of `audit.py`. Changing a definition
means changing it there, in one place, and the diff is the record of the
change. In summary:

- **A lesson file** is a Markdown file sitting directly in a `Unit <n> - <title>`
  directory, named `U<unit>-L<number><optional letter>-<title>.md`. Files in
  `_archive/` are superseded drafts and are excluded from every denominator.
- **A worksheet** is a file under `Worksheets/` that is not an answer key.
- **An answer key** has `Answer-Key` in the filename.
- **Header metrics** (objective, materials, time, differentiation, homework,
  rubric) match a bold inline label or a heading at the start of a line —
  `**LO:**`, `**Materials:**`, `**Estimated time:**` and similar. A passing
  mention in prose does not count.
- **Content metrics** (hand derivation, numeric checkpoint, paper check, error
  and failure content, security and privacy thread) are case-insensitive token
  matches over the whole file, with the token list in `TOKENS`. A lesson counts
  once per metric regardless of how many tokens hit.
- Consequence worth stating plainly: content metrics measure *presence of
  language*, not occurrence of practice. A lesson that says "do this by hand"
  counts the same as one that builds a twenty-minute hand-derivation sequence
  around it. These numbers bound the design; they say nothing about delivery.

## Files

- `evidence.csv` — one row per file: path, kind, unit, word count, and a 0/1
  column per metric.
- `summary.md` — aggregate table plus a per-unit breakdown, headed by the
  commit SHA.
