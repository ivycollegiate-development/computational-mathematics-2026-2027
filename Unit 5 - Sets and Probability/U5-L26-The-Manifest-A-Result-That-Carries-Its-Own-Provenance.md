# U5 L26 — The Manifest: A Result That Carries Its Own Provenance

**Date:** Wednesday, March 24, 2027
**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.10 — emit a self-describing result manifest; separate a result from
the context that makes it interpretable

---

## TODAY'S PURPOSE

Your `shape_report` returns a dictionary of numbers. It is a good dictionary.
It is also, on its own, **unusable**, and the reason is not a bug:

> `ev: 5047.48`

That line is not a finding. It is half a finding. The other half is: an expected
loss per year, for a two-asset model, over 200,000 simulated years, with a
fixed seed, under these five assumptions, whose simulation is within 0.4% of the
closed form. **A reader given only the first half cannot check, reproduce,
challenge, or act on it.** They can only nod.

Today you build the other half. The **manifest** is the block of output that
travels with every number your project reports, and it is the deliverable an
assessor reads before they read anything else.

## PART 1 — WHAT YOU HAVE, AND WHAT IT LACKS (8 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def shape_report(groups, seed=20270326, years=200000):
    """Return the headline statistics for a grouped threat model."""
    raise NotImplementedError("students: you have this from L18")

# what the manifest has to add:
#   population  -- who this is about
#   period      -- per what interval
#   seed        -- so the run is reproducible
#   n_years     -- so the tolerance is computable
#   assumptions -- the words the code cannot enforce
#   method      -- simulation, closed form, or both agreeing
```

- ☐  Which of the six missing items is the most important, and why: ______
- ☐  Which one can the **code** supply, and which can only a human supply:
      ______
- ☐  Which one would you have to *invent* if you had not thought of it today,
      and what would the invention have looked like: ______

That last one is the real hazard. `period` and `population` are the two fields
most likely to be written from imagination, because a plausible-looking period
is easy to type and impossible to derive. The manifest is not an honesty test —
it is a structure that makes an unstated field **visible as unstated**, which is
what stops it being filled in silently.

## PART 2 — BUILD IT (15 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random

ASSET_VALUE = {"file-server": 12000, "staff-inboxes": 3000}

def at_least_one(ls):
    """P(at least one of these likelihoods fires), by repeated inclusion-exclusion."""
    if not ls:
        return F(0)
    p = ls[0]
    for q in ls[1:]:
        p = p + q - p * q
    return p

def shape_report(groups, seed=20270326, years=200000):
    """Simulate `years` of the grouped model; return the headline statistics."""
    if years <= 0:
        raise ValueError("years must be positive")
    rng = Random(seed)
    assets = list(groups)
    values = {a: max(v for _, v in groups[a]) for a in assets}
    losses = []
    for _ in range(years):
        total = 0
        for a in assets:
            p = F(1)
            for q, _ in groups[a]:
                p = p * (1 - q)
            if rng.random() < float(1 - p):
                total += values[a]
        losses.append(total)
    n = len(losses)
    ev = F(sum(losses), n)
    worst = max(losses)
    p_worst = F(sum(1 for L in losses if L == worst), n)
    tail = [L for L in losses if L > 0]
    return {
        "ev": ev,
        "ev_float": round(float(ev), 2),
        "p_any_loss": F(sum(1 for L in losses if L > 0), n),
        "mean_loss_given_loss": round(float(F(sum(tail), len(tail))), 2),
        "worst_case": worst,
        "p_worst_case": round(float(p_worst), 6),
        "n_years": n,
        "seed": seed,
        "n_assets": len(assets),
        "independence_assumed": "within-asset threats independent; asset charged once per year",
    }

groups = {"file-server": [(F(3, 20), 12000), (F(2, 10), 12000)],
          "staff-inboxes": [(F(4, 10), 3000)]}
for k, v in shape_report(groups).items():
    print("%-24s %s" % (k, v))
```

Real output:

```
ev                       1009497/200
ev_float                 5047.48
p_any_loss               118257/200000
mean_loss_given_loss     8536.47
worst_case               15000
p_worst_case             0.12833
n_years                  200000
seed                     20270326
n_assets                 2
independence_assumed     within-asset threats independent; asset charged once per year
```

- ☐  `ev` is an exact `Fraction`, `1009497/200`, and `ev_float` is its rounded
      form. Why keep both: ______
- ☐  `p_worst_case` is `0.12833` — a worst case of 15,000 in 12.8% of years.
      **Is 15,000 really the "worst case"?** Given the model, what is the
      theoretical maximum, and does the simulation ever reach it: ______

That second checkbox has a sharp answer and it is the kind of thing that gets
missed in review. The maximum here is 15,000 — both assets — and 12.8% of years
reach it, because `p_any_loss` is 0.59 overall and the two assets are charged
independently, so hitting both is common rather than rare. **The worst case is
not rare, which is exactly what makes it the number to plan against.** A
"worst case" that occurred once in 200,000 years would be a curiosity; one that
occurs in one year in eight is the design case.

## PART 3 — THE MANIFEST (15 min)

Now the part that changes what the output *means*.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

CLOSED_FORM = F(8, 25) * 12000 + F(2, 5) * 3000

def manifest(report, population, period, model_version, reviewer):
    """Wrap a shape_report in its own provenance. Refuses to invent fields."""
    if not population:
        raise ValueError("manifest requires a population. If there is none, say so explicitly.")
    if not period:
        raise ValueError("manifest requires a period. 'per year' is a legitimate answer.")
    if not model_version:
        raise ValueError("manifest requires a model version, so a stale number is identifiable")
    ev = report["ev_float"]
    closed = float(CLOSED_FORM)
    dev = abs(ev - closed) / closed
    return {
        "RESULT": {
            "expected_annual_loss": ev,
            "p_any_loss": round(float(report["p_any_loss"]), 4),
            "worst_case": report["worst_case"],
            "p_worst_case": report["p_worst_case"],
        },
        "SCOPE": {
            "population": population,
            "period": period,
            "n_assets": report["n_assets"],
            "currency": "USD",
        },
        "PROVENANCE": {
            "model_version": model_version,
            "method": "Monte Carlo, 200000 years, fixed seed",
            "seed": report["seed"],
            "n_years": report["n_years"],
            "closed_form_expected_loss": closed,
            "simulation_deviation_from_closed_form": round(dev, 5),
            "tolerance": 0.01,
            "within_tolerance": dev < 0.01,
        },
        "ASSUMPTIONS": {
            "independence": report["independence_assumed"],
            "impact_distribution": "deterministic, no spread",
            "horizon": "one year, resets each year",
            "shared_assets": "charged at most once per year (L20 fix in place)",
        },
        "NOT_MODELLED": [
            "likelihood drift over time",
            "correlated threats across assets",
            "recovery time and its effect on revenue",
            "the backup scenario (no post-mitigation values supplied)",
        ],
        "REVIEW": {
            "prepared_by": reviewer,
            "status": "draft -- not reviewed",
        },
    }

m = manifest(shape_report(groups),
             population="12-person consultancy, own file server and staff inboxes",
             period="per year",
             model_version="riskkit 1.2.0",
             reviewer="your name here")
for section, fields in m.items():
    print("== %s ==" % section)
    if isinstance(fields, list):
        for item in fields:
            print("   - %s" % item)
        print()
        continue
    for k, v in fields.items():
        print("   %-42s %s" % (k, v))
    print()
```

Real output:

```
== RESULT ==
   expected_annual_loss                       5047.48
   p_any_loss                                 0.5913
   worst_case                                 15000
   p_worst_case                               0.12833

== SCOPE ==
   population                                 12-person consultancy, own file server and staff inboxes
   period                                     per year
   n_assets                                   2
   currency                                   USD

== PROVENANCE ==
   model_version                              riskkit 1.2.0
   method                                     Monte Carlo, 200000 years, fixed seed
   seed                                       20270326
   n_years                                    200000
   closed_form_expected_loss                  5040.0
   simulation_deviation_from_closed_form      0.00148
   tolerance                                  0.01
   within_tolerance                           True

== ASSUMPTIONS ==
   independence                               within-asset threats independent; asset charged once per year
   impact_distribution                        deterministic, no spread
   horizon                                    one year, resets each year
   shared_assets                              charged at most once per year (L20 fix in place)

== NOT_MODELLED ==
   - likelihood drift over time
   - correlated threats across assets
   - recovery time and its effect on revenue
   - the backup scenario (no post-mitigation values supplied)

== REVIEW ==
   prepared_by                                your name here
   status                                     draft -- not reviewed
```

Four sections, and each one does a job the raw number cannot.

**`SCOPE`** is the half-sentence the number was missing. `expected_annual_loss:
5047.48` is now `5047.48 per year, for a 12-person consultancy, in USD`. Same
number, and now it can be checked against an actual organisation.

**`PROVENANCE`** makes the result reproducible and self-checking. A fixed seed
means the reader can re-run and get the same number. The deviation from the
closed form is 0.00149 against a stated tolerance of 0.01, and the manifest
**computes that comparison and records the verdict** — so a future run that
breaks the implementation will announce it rather than requiring someone to
notice.

**`ASSUMPTIONS` and `NOT_MODELLED`** are the two sections that do the honest
work, and they point in opposite directions. `ASSUMPTIONS` says what the model
believes. `NOT_MODELLED` says what the model has no opinion about — and note
the last entry: the backup scenario from Tuesday's Part 3, written down as
absent rather than quietly estimated. **A manifest that lists what it does not
know is worth more than one that sounds complete**, because a reader can act on
a stated gap and can only ignore a confident-sounding paragraph.

**`REVIEW`** with `status: draft -- not reviewed` is the field that costs you
nothing and saves you from the worst outcome in this entire project: a number
that escapes before anyone has read it.

- ☐  The three `ValueError` guards in `manifest`: why refuse to build a
      manifest with a missing `population` rather than defaulting to "unknown"
      or to a guess: ______
- ☐  `NOT_MODELLED` has four entries. Add **two more** from your own model's
      known weaknesses: ______
- ☐  `simulation_deviation_from_closed_form: 0.00148`. Change the seed. Does the
      deviation stay inside tolerance, and what does that tell you about the
      tolerance: ______
- ☐  Which section would you most want an external reader to challenge, and
      which is the one you are least able to defend: ______

## PART 4 — WIRE IT UP (7 min)

- ☐  `manifest()` in `riskkit.py`, with all three guards
- ☐  A `--manifest` flag, or simply a `main()` that prints the manifest
- ☐  **`riskkit.py` refuses to run a report without a population** — no default
      string, no empty string, no "unknown". If the caller has not supplied it,
      the program stops. That is the L20 lesson in a different costume.
- ☐  Paste the real manifest output into the README as a fenced block
- ☐  Run it live; the README's copy must match byte for byte

## PART 5 — CLOSE (5 min)

- ☐  Manifest emits all six sections
- ☐  Three guards present and testable — write one test that each guard fires
- ☐  README carries the real output
- ☐  **In writing, one sentence: what does a manifest do that the number alone
      cannot?** ______

## TURN IN — The Manifest

1. `riskkit.py` with `manifest()` and its three guards
2. The three guard tests
3. The live manifest output, pasted into the README
4. Your sentence from Part 5
5. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 📋 PREVIEW OF THURSDAY

**Next:** L27, Thu Mar 25 — **paper, and the hardest conversation in the unit.**
I am going to hand you a plausible, well-presented, wrong model from someone
else's organisation and ask you to find the error. You will not be given a bug
in the code. You will be given a **number** that is wrong, and your job will be
to find the assumption that produced it.

**Bring Thursday:** your manifest, and the one-page argument from Tuesday.

## 🇹🇼 TAIWAN CONTEXT

`NOT_MODELLED` is the section with the most direct institutional counterpart, and
it is the one a reader in this ecosystem will look for first. The ROC national
CERT's post-incident review format requires the reviewer to state explicitly
which contributing factors were assessed and which were outside the scope of the
review — and the reason is that an unstated scope reads as a complete
assessment. A review that examined the firewall configuration and says nothing
about credential hygiene is read, by anyone who has not been told otherwise, as
a review that found the firewall configuration and nothing else wrong.

The Ministry of Digital Affairs' framework makes the same demand of smaller
organisations' self-assessments, and its guidance is unusually direct that
"no incidents observed" is a statement about the observation window rather than
about the absence of risk. That is precisely the `n_years` and `period` pair in
your `SCOPE` block: a model that reports `p_any_loss` over 200,000 *simulated*
years is reporting about a simulation, and the manifest says so in `PROVENANCE`
rather than leaving the reader to assume the figure describes the organisation's
actual history.

The related field is the one nobody adds: the **calibration population**. Your
likelihoods of `3/20` and `2/10` are judgements about a population that the
manifest currently does not name. When a reader in Taiwan asks where a figure
was calibrated, the answer in the CERT's methodology is a named comparison set —
same sector, similar size, same exposure profile — and a figure without one is
treated as uncalibrated rather than merely rough. Add a `CALIBRATION` block to
your manifest with a field you must fill in by hand, and a note on what evidence
would justify the values. It is the one field the code cannot supply, which is
why it is the one that matters most.
