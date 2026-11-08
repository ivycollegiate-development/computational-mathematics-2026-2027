# Unit 2 Formula Sheet — Computational Mathematics

**Allowed on all Unit 2 assessments.** This is a reference, not a cheat sheet — you still need to know *when* and *why* to use each piece.

---

## CHART TYPE DECISION TABLE

| Question | Chart | x-axis | y-axis | Key Function |
|----------|-------|--------|--------|--------------|
| How does ONE numeric variable change over time/sequence? | Line plot | Numeric / Date | Numeric | `plt.plot(x, y)` |
| Compare categories? | Bar chart | Categories | Numeric | `plt.bar(cats, vals)` |
| Relationship between TWO numeric variables? | Scatter plot | Numeric | Numeric | `plt.scatter(x, y)` |
| Distribution of ONE numeric variable? | Histogram | Bins (auto) | Count / Frequency | `plt.hist(data)` |

---

## MATPLOTLIB FIGURE LIFECYCLE (MEMORIZE THIS ORDER)

```python
plt.figure()                                    # 1. NEW FIGURE — every chart
# ... plotting calls (plot, bar, scatter, hist) ...
plt.title("Descriptive Title — Audience Aware") # 2. Title
plt.xlabel("X Axis Label (units)")              # 3. X label
plt.ylabel("Y Axis Label (units)")              # 4. Y label
plt.ylim(bottom=0)                              # 5. HONEST AXIS — REQUIRED for bar charts
plt.legend()                                    # 6. If multiple series (needs label= on each)
plt.tight_layout()                              # 7. Prevents label cutoff
plt.savefig("filename.png", dpi=150, bbox_inches="tight")  # 8. SAVE BEFORE SHOW!
plt.clf()                                       # 9. Clean up for next chart
# plt.show()                                    # 10. Optional, LAST
```

---

## KEY MATPLOTLIB ARGUMENTS

| Function | Common Args | What They Do |
|----------|-------------|--------------|
| `plt.plot(x, y)` | `marker="o"`, `linestyle="--"`, `color="steelblue"`, `label="Name"` | Line + markers, dashed, color, legend entry |
| `plt.bar(cats, vals)` | `color=["#c0392b", "#27ae60"]`, `edgecolor="white"`, `width=0.6` | Per-bar colors, white borders, narrower bars |
| `plt.scatter(x, y)` | `s=50` (size), `alpha=0.6` (transparency), `c="red"` (color) | Dense data: small `s` + low `alpha` |
| `plt.hist(data)` | `bins=15`, `edgecolor="white"` | 15 bins, white borders between bars |

---

## CSV PIPELINE (MEMORIZE THIS PATTERN)

```python
import csv

# 1. READ + STRIP COMMENT LINES
with open("data.csv", newline="") as f:
    lines = [ln for ln in f if not ln.startswith("#")]
rows = list(csv.DictReader(lines))
# rows = list of OrderedDict — every value is a STRING

# 2. CONVERT WITH TRY/EXCEPT
def to_float(v):
    try: return float(v)
    except (ValueError, TypeError): return None

def to_int(v):
    try: return int(v)
    except (ValueError, TypeError): return None

# 3. SANITY BOUNDS = DOMAIN KNOWLEDGE (impossible values)
SANITY = {
    "phishing_reports": (0, 100),
    "failed_logins": (0, 5000),
    "phishing_clicks": (0, 100),
    "login_success_rate": (0.0, 1.0),
    "Age": (10, 22),
    "Overall GPA": (0.0, 4.0),
}

clean = []
dropped = {"blank": 0, "impossible": 0, "unparseable": 0}

for r in rows:
    drop_reason = None
    for col, (lo, hi) in SANITY.items():
        if r[col] == "":
            drop_reason = f"blank {col}"
            dropped["blank"] += 1
            break
        val = to_float(r[col])  # or to_int
        if val is None:
            drop_reason = f"unparseable {col}"
            dropped["unparseable"] += 1
            break
        if not (lo <= val <= hi):
            drop_reason = f"impossible {col}={val}"
            dropped["impossible"] += 1
            break
        r[col] = val  # convert in place
    if drop_reason:
        print(f"Dropped: {drop_reason}")
        continue
    clean.append(r)

# 4. AUDIT ASSERT (catches double-count / lost rows)
rows_in = len(rows)
rows_out = len(clean)
rows_dropped = sum(dropped.values())
assert rows_in == rows_out + rows_dropped, "Count mismatch"
```

---

## SANITY BOUNDS vs STATISTICAL OUTLIERS

| Sanity Bounds | Statistical Outliers (1.5×IQR) |
|---------------|--------------------------------|
| Domain knowledge: "GPA 9.0 is impossible on a 4.0 scale" | This dataset's distribution |
| Auditable: anyone reads the dict and agrees/disagrees | Depends on sample |
| Keeps surprising but possible (GPA 0.5 = real student) | May flag real extremes in small samples |
| Rejects impossible (GPA 9.0) | Rejects "surprising" values |

**Rule:** Use sanity bounds for cleaning. Keep the thin tail — it's usually the signal.

---

## PROVENANCE STATEMENT TEMPLATE

> "Cleaned **[N]** raw rows to **[M]** rows by dropping **[K]** rows: **[X]** blank **[col]**, **[Y]** impossible **[col]**, **[Z]** unparseable **[col]**; **[bias note if any — e.g., dropped rows were disproportionately low-GPA students]**."

**Always include:** raw count, clean count, dropped count, reasons by column, bias check.

---

## HONEST AXIS RULE

| Chart Type | Y-Axis Must Start at 0? |
|------------|------------------------|
| **Bar chart** | **YES** — `plt.ylim(bottom=0)` |
| Line plot | OK to zoom (shows change, not ratio) |
| Scatter plot | Usually 0 is natural |
| Histogram | Usually 0 is natural |

**If you don't start at 0 on a bar chart, you are visually lying.** A 5% difference looks like 50%.

---

## k-ANONYMITY CHECKLIST (before publishing)

- ☐ No group < 5 in any published chart/table
- ☐ Sensitive dates redacted: use "mid-October", "day 14", not "Oct 14"
- ☐ Aggregate small groups before publishing
- ☐ Internal version (security team) keeps detail; public version suppresses

---

## CORRELATION ≠ CAUSATION

When you see a trend between X and Y:

1. **Third variable?** (e.g., "attack day" drives both phishing AND failed logins)
2. **Direction unknown?** (X→Y, Y→X, or Z→X,Y)
3. **Say:** "X and Y move together; a third factor may drive both."

---

## VERB DRILL (ANSWER THE VERB)

| Verb | Answer Format |
|------|---------------|
| **What** / **Name** / **List** | Value, word, or list |
| **What happens** | Actual error/behavior (NOT the fix!) |
| **Why** | Complete sentence |
| **Rewrite** | New version for the stated audience |
| **Trace** | Step-by-step execution with values |

---

## COMMON EXCEPTIONS

| Code | Exception | When |
|------|-----------|------|
| `float("")` | `ValueError` | Blank string |
| `float("N/A")` | `ValueError` | Non-numeric text |
| `float(None)` | `TypeError` | None value |
| `int("3.5")` | `ValueError` | Float string to int |
| `csv.DictReader` on comment line | Silent corruption | Header becomes `# Mental health survey...` |

---

## QUICK DEBUG CHECKLIST

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Blank PNG | `savefig` after `show()` | Move `savefig` before `show()` |
| Overlapping x-ticks | Too many dates | `plt.xticks(dates[::5], rotation=45)` |
| Legend missing entry | Missing `label=` on that series | Add `label="Name"` to plot call |
| Bars same color | `color="red"` (string) | Use `color=["red", "blue"]` (list) |
| Assert fails | Double-count or lost row | Check `break` in every `if`, `continue` skips append |
| Average seems high | Dropped blank GPA = dropped strugglers | Check missingness pattern; report in provenance |