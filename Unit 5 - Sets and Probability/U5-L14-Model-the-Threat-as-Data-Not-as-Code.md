# U5 L14 — Model the Threat as Data, Not as Code

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.9 — represent a threat model as validated data; attach a provenance
field to every parameter and enforce it in code

---

## TODAY'S PURPOSE

`riskkit.py` has arithmetic. What it does not have is **a threat model**, and
without one the arithmetic is a calculator.

Today you enter three threats. The assignment is not the numbers — you will
change the numbers on Thursday and the model should not care. The assignment is
the **shape of the record**: every threat carries a likelihood, an impact, and
a string saying where that likelihood came from. Code that refuses to load a
threat without that string is code that cannot produce an undefended number.

## PART 1 — THE RECORD (12 min)

A threat is a dict. Five fields, and the last two are the ones that matter.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

THREATS = [
    {"id": "T-phish", "name": "credential phishing wave",
     "likelihood": F(4, 10), "impact": 3000,
     "likelihood_source": "ROC CERT advisory volume, 3-year mean",
     "impact_source": "one workstation rebuild + 4 staff-hours of reset support"},
    {"id": "T-ransom", "name": "ransomware via remote desktop exposure",
     "likelihood": F(3, 20), "impact": 45000,
     "likelihood_source": "analyst judgement: RDP exposed on 6 of 9 hosts",
     "impact_source": "no tested backup; figure is rebuild + 11 days downtime"},
    {"id": "T-doxs", "name": "directory data exposure from misconfigured share",
     "likelihood": F(2, 10), "impact": 12000,
     "likelihood_source": "share is world-readable; 3 of 3 scans confirmed",
     "impact_source": "notification, counsel, and 2 staff-days of response"},
]
for t in THREATS:
    print("%-9s %-46s p=%-5s impact=%s" % (t["id"], t["name"], t["likelihood"], t["impact"]))
print("ids unique:", len({t["id"] for t in THREATS}) == len(THREATS))
print("likelihoods in range:", all(0 <= t["likelihood"] <= 1 for t in THREATS))
```

Real output:

```
T-phish   credential phishing wave                       p=2/5   impact=3000
T-ransom  ransomware via remote desktop exposure         p=3/20  impact=45000
T-doxs    directory data exposure from misconfigured share p=1/5   impact=12000
ids unique: True
likelihoods in range: True
```

Two invariants, both cheap: ids unique, likelihoods in `[0, 1]`. Those will be
`ValueError`s in a moment, not `print` statements — this run is the
demonstration, the loader is the tool.

Read `T-ransom`'s `likelihood_source` again: **"analyst judgement: RDP exposed on
6 of 9 hosts."** That is the honest version and it is still a judgement. The
metadata does not claim the number is a measurement. It claims where the guess
was made, which is the only claim you can actually support.

- ☐  Which of your three sources is closest to a measurement, and which is
      furthest? ______
- ☐  For `T-phish`, what population and what period is the "3-year mean"
      measured over? ______ (If you cannot answer this, the string is not
      finished.)

## PART 2 — THE LOADER THAT REFUSES BAD DATA (12 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

REQUIRED = ("id", "name", "likelihood", "impact", "likelihood_source", "impact_source")

def load_threats(records):
    """Validate a list of threat dicts and return them as a list of dicts.

    Raises ValueError on a missing field, a blank source string, a likelihood
    outside [0, 1], a non-integer impact, or a duplicate id.
    """
    seen = set()
    for i, r in enumerate(records):
        missing = [k for k in REQUIRED if k not in r]
        if missing:
            raise ValueError("threat %d is missing %s" % (i, ", ".join(missing)))
        for k in ("likelihood_source", "impact_source"):
            if not str(r[k]).strip():
                raise ValueError("threat %r has a blank %s" % (r["id"], k))
        if not (0 <= r["likelihood"] <= 1):
            raise ValueError("threat %r: likelihood must be in [0, 1], got %r" % (r["id"], r["likelihood"]))
        if not isinstance(r["impact"], int) or r["impact"] < 0:
            raise ValueError("threat %r: impact must be a non-negative int" % (r["id"],))
        if r["id"] in seen:
            raise ValueError("duplicate threat id %r" % (r["id"],))
        seen.add(r["id"])
    return list(records)

good = {"id": "T-x", "name": "example", "likelihood": F(1, 2), "impact": 100,
        "likelihood_source": "s", "impact_source": "i"}
print("good record loads:", load_threats([good])[0]["id"])
for bad, label in [
    ({"id": "T-y", "name": "n", "likelihood": F(1, 2), "impact": 1,
      "likelihood_source": "", "impact_source": "i"}, "blank source"),
    ({"id": "T-x", "name": "n", "likelihood": F(1, 2), "impact": 1,
      "likelihood_source": "s", "impact_source": "i"}, "duplicate id"),
]:
    try:
        load_threats([good, bad])
    except ValueError as exc:
        print("%-14s -> ValueError: %s" % (label, exc))
```

Real output:

```
good record loads: T-x
blank source     -> ValueError: threat 'T-y' has a blank likelihood_source
duplicate id     -> ValueError: duplicate threat id 'T-x'
```

That first check is the one I want you to argue with me about. **A blank
`likelihood_source` is a hard error**, and some of you will think that is
pedantic because a threat with no source is just a threat with a default. It is
not. A threat whose provenance field is empty is a threat whose number will be
quoted in a paragraph with no sentence in it explaining where it came from, and
that paragraph is the artifact this project is graded on.

- ☐  Argue against the blank-source check in one sentence. Then say why you
      changed your mind: ______
- ☐  Why must `impact` be an `int` and not a `float`? What goes wrong with a
      float impact of 45000.5 that would not go wrong with an int: ______
- ☐  The id check uses a `set`. What would happen with a `list` instead, and
      why is that a worse failure than a crash: ______

## PART 3 — DERIVE THE BOOKS (10 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

def two_outcome(likelihood, impact):
    """A one-year book for a threat: it happens (cost) or it does not (zero)."""
    if not (0 <= likelihood <= 1):
        raise ValueError("likelihood must be a probability, got %r" % (likelihood,))
    return [(likelihood, -impact), (1 - likelihood, 0)]

def threat_ev(threat):
    return sum(p * v for p, v in two_outcome(threat["likelihood"], threat["impact"]))

THREATS = [
    {"id": "T-phish", "name": "credential phishing wave", "likelihood": F(4,10), "impact": 3000},
    {"id": "T-ransom", "name": "ransomware via remote desktop", "likelihood": F(3,20), "impact": 45000},
    {"id": "T-doxs", "name": "directory data exposure", "likelihood": F(2,10), "impact": 12000},
]
for t in THREATS:
    book = two_outcome(t["likelihood"], t["impact"])
    print("%-9s EV %-8s worst %s" % (t["id"], threat_ev(t), min(v for _, v in book)))
try:
    two_outcome(F(3, 2), 100)
except ValueError as exc:
    print("ValueError:", exc)
```

Real output:

```
T-phish   EV -1200    worst -3000
T-ransom  EV -6750    worst -45000
T-doxs    EV -2400    worst -12000
ValueError: likelihood must be a probability, got Fraction(3, 2)
```

Read the two columns against each other. `T-ransom` has the largest expected
loss at −6,750 and by L12's arguments the **smallest** fraction of a small
budget it can consume. It is the threat that would end the budget.

- ☐  Rank the three by EV. Rank them by worst case. Where do the two rankings
      differ: ______
- ☐  Which of the three would you fund first if you could only fund one, and
      which statistic did you use: ______
- ☐  `T-ransom`'s likelihood is `3/20` and its impact is 45,000. The whole
      expected loss is 6,750 dollars a year. **Is that a reason to think
      ransomware is not a serious risk here?** One sentence, and the honest
      answer is the interesting part: ______

## PART 4 — BUILD IT (8 min)

Add to `riskkit.py`:

- ☐  `REQUIRED_FIELDS` and `load_threats(records)` exactly as in Part 2
- ☐  `two_outcome(likelihood, impact)` and `threat_ev(threat)`
- ☐  `model_report(threats)` returning a dict with `n_threats`, `total_ev`,
      `worst_single_loss`, and `undocumented` — a count of records whose
      `likelihood_source` is a string of the analyst's own name or the word
      "guess". It should be 0, and if it is not, the report says so
- ☐  Tests: the three refusals from Part 2, plus a positive load of the three
      threats from Part 1 with their full six fields
- ☐  Docstrings stating the validation contract

- ☐  Why does `undocumented` exist as a *number in the report* rather than as a
      `ValueError`? ______

## PART 5 — CLOSE (3 min)

- ☐  `riskkit.py` loads the three threats and produces a report
- ☐  You can state, in one sentence, what the `likelihood_source` field buys you
- ☐  **In writing: the `likelihood_source` string for the one threat in your
      personal model you are least sure about, phrased so that a reader would
      understand what you did and would not be able to accuse you of
      pretending.** This is graded.

## TURN IN — The Threat Model as Data

1. `riskkit.py` with `load_threats`, `two_outcome`, `threat_ev`, `model_report`,
   and the tests
2. The Part 1, Part 2, and Part 3 outputs, run live
3. Your uncertainty sentence from Part 5
4. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

The provenance field is a regulatory expectation now, not a stylistic one, and
this is where the ROC's guidance is unusually specific. The
Ministry of Digital Affairs' cybersecurity framework and the incident-reporting
obligations that flow from it both require that an organization's risk
assessment be **documented and reviewable** — not that the numbers be right,
which nobody can verify from outside, but that the reasoning behind them be
recoverable by someone who was not there. A risk register whose likelihood
column is a bare number cannot be reviewed, because a reviewer has nothing to
attach their objection to.

The national CERT's published risk methodology makes the same point about
likelihood calibration: a figure is defensible when it is stated as *calibrated
against observed incidents in a named population and period*. That phrasing
*is* your `likelihood_source` field. `T-phish`'s "ROC CERT advisory volume,
3-year mean" is defensible in that form; "phishing is common" is not, because a
reviewer cannot ask which population, which period, or which denominator, and a
statement that cannot be questioned cannot be reviewed.

This is also why `undocumented` belongs in the report as a number rather than an
exception. An exception stops the run. A number in a report gets read. For a
project whose main grading criterion is *the sentence that accompanies the
model*, a report that reports its own unprovenanced parameters is doing the work
the prose cannot.
