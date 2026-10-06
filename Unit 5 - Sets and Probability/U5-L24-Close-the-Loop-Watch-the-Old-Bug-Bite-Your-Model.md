# U5 L24 — Close the Loop: Watch the Old Bug Bite Your Own Model

**Unit:** 5 — Sets and Probability
**Type:** Machine lesson (45 minutes)
**LO:** 5.4, 5.9 — demonstrate the L20 over-count in the project's own threat
model; retire the naive aggregator; add the regression test that guards the fix

---

## TODAY'S PURPOSE

On L20 you fixed a bug in an abstract pair of threats hitting a 5,400 asset.
Today that bug runs against **your model**, with your numbers, and you will see
it produce a specific wrong figure.

Then you delete it. Not comment it out — delete it, so it cannot come back and
so the next person reading the repository cannot mistake it for a working
alternative.

## PART 1 — THE MODEL AS IT NOW STANDS (10 min)

Two assets. The `file-server` is **one asset worth 12,000** — and two separate
threats can destroy it. That is the whole situation, and it is unremarkable:
ransomware and a world-readable share both destroy the same file server.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

ASSET_VALUE = {"file-server": 12000, "staff-inboxes": 3000}
THREATS = [
    {"id": "T-ransom", "likelihood": F(3, 20), "asset": "file-server"},
    {"id": "T-doxs",   "likelihood": F(2, 10), "asset": "file-server"},
    {"id": "T-phish",  "likelihood": F(4, 10), "asset": "staff-inboxes"},
]
for t in THREATS:
    print("%-9s %-13s p=%-5s" % (t["id"], t["asset"], t["likelihood"]))
print("two threats, one asset:", [t["id"] for t in THREATS if t["asset"] == "file-server"])
print("asset values:", ASSET_VALUE)
```

Real output:

```
T-ransom  file-server   p=3/20 
T-doxs    file-server   p=1/5  
T-phish   staff-inboxes p=2/5  
two threats, one asset: ['T-ransom', 'T-doxs']
asset values: {'file-server': 12000, 'staff-inboxes': 3000}
```

- ☐  In one sentence, why does a second threat on the same asset not double the
      loss: ______
- ☐  Note that the impacts are now a property of the **asset**, not the threat.
      Where did the threat-level impact field go, and was that a loss of
      information: ______

## PART 2 — THE OLD BUG, RUNNING (12 min)

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")
from random import Random

ASSET_VALUE = {"file-server": 12000, "staff-inboxes": 3000}
THREATS = [
    {"id": "T-ransom", "likelihood": F(3, 20), "asset": "file-server"},
    {"id": "T-doxs",   "likelihood": F(2, 10), "asset": "file-server"},
    {"id": "T-phish",  "likelihood": F(4, 10), "asset": "staff-inboxes"},
]

def simulate_year_v1(rng, threats):
    """v1, the L20 bug. Charges the shared asset once per threat that hits it."""
    total = 0
    for t in threats:
        if rng.random() < float(t["likelihood"]):
            total += ASSET_VALUE[t["asset"]]
    return total

def simulate_year_v3(rng, threats):
    """v3, the fix. Each asset is charged at most once per year."""
    hit = set()
    for t in threats:
        if rng.random() < float(t["likelihood"]):
            hit.add(t["asset"])
    return sum(ASSET_VALUE[a] for a in hit)

for name, fn in (("v1 naive", simulate_year_v1), ("v3 grouped", simulate_year_v3)):
    rng = Random(20270317)
    losses = [fn(rng, THREATS) for _ in range(200000)]
    print("%-11s empirical EV %s" % (name, round(float(F(sum(losses), len(losses))), 1)))
```

Real output:

```
v1 naive    empirical EV 5419.4
v3 grouped  empirical EV 5059.9
```

**5,419 versus 5,060.** A 360-dollar overstatement in your own model, on a
project whose whole purpose is to produce a number someone will act on. In
percentage terms it is 7% — comfortably inside the range where a reader sees a
plausible number and moves on.

- ☐  The gap is 360 (approximately — the two runs are samples, so the gap
      wobbles slightly). What is the **exact** gap, and what formula produces
      it: ______
- ☐  7% of the total. If your report's headline number carried a ±7% error, would
      anyone notice: ______
- ☐  **Now the important question:** the v1 number is *larger*. The old bug
      makes the risk look **worse** than it is. In a programme with a budget to
      spend, which direction of error is the survivable one, and why: ______

That last checkbox is the uncomfortable one and it is worth real marks. A
conservative error gets an organisation to spend money it perhaps did not need.
A non-conservative error — an under-count — leaves a real exposure in place, and
the whole asymmetry of harm sits on the other side. **v1 errs in the direction
that looks responsible, which is exactly why it would survive review indefinitely
if nobody wrote the L20 test.** The failure mode of a conservative bug is that it
costs money; the failure mode of an optimistic one is that it costs the
organisation.

## PART 3 — THE EXACT ARITHMETIC (12 min)

The simulation is noisy. The closed form is not, and you want both — the
simulation to check the implementation, the closed form to state the number.

```python
try:
    from fractions import Fraction as F
except ImportError:
    raise SystemExit("fractions is in the standard library — something is wrong with this Python. Tell me.")

ASSET_VALUE = {"file-server": 12000, "staff-inboxes": 3000}
THREATS = [
    {"id": "T-ransom", "likelihood": F(3, 20), "asset": "file-server"},
    {"id": "T-doxs",   "likelihood": F(2, 10), "asset": "file-server"},
    {"id": "T-phish",  "likelihood": F(4, 10), "asset": "staff-inboxes"},
]

def at_least_one(ls):
    if not ls:
        return F(0)
    p = ls[0]
    for q in ls[1:]:
        p = p + q - p * q
    return p

def expected_loss_v3(threats):
    groups = {}
    for t in threats:
        groups.setdefault(t["asset"], []).append(t["likelihood"])
    return sum(at_least_one(ls) * ASSET_VALUE[a] for a, ls in groups.items())

def expected_loss_v1(threats):
    return sum(t["likelihood"] * ASSET_VALUE[t["asset"]] for t in threats)

print("closed form v3:", expected_loss_v3(THREATS))
print("v1 closed form (naive sum):", expected_loss_v1(THREATS))
print("v1 overstates by:", expected_loss_v1(THREATS) - expected_loss_v3(THREATS))
print("the credit v1 drops:", F(3, 20) * F(2, 10) * 12000)
print()
print("v3 agrees with the simulation to:",
      round(abs(5059.9 - float(expected_loss_v3(THREATS))), 2), "dollars")
print("v1 disagrees with the simulation by:",
      round(abs(5419.4 - float(expected_loss_v1(THREATS))), 2), "dollars")
print()
print("P(file-server fires) exactly:", at_least_one([F(3, 20), F(2, 10)]))
print("P(staff-inboxes fires) exactly:", at_least_one([F(4, 10)]))
print("and 8/25 * 12000 + 2/5 * 3000 =", F(8, 25) * 12000 + F(2, 5) * 3000)
```

Real output:

```
closed form v3: 5040
v1 closed form (naive sum): 5400
v1 overstates by: 360
the credit v1 drops: 360

v3 agrees with the simulation to: 19.9 dollars
v1 disagrees with the simulation by: 19.4 dollars
P(file-server fires) exactly: 8/25
P(staff-inboxes fires) exactly: 2/5
and 8/25 * 12000 + 2/5 * 3000 = 5040
```

Three lines worth reading twice.

**`the credit v1 drops: 360` matches `v1 overstates by: 360` exactly.** The
overstatement is not a mystery. It is `P(ransom) × P(share) × value(file
server)` — the shared-exposure credit, computed in one line, and equal to the
entire error. When you find a bug this clean, that is the strongest evidence
that you have found the *cause* and not merely a discrepancy.

**Both v1 and v3 sit within about 20 dollars of their respective closed forms**,
in opposite directions from the 360 gap. The simulation agrees with each
implementation. **Neither simulation can tell you which implementation is
right** — that came from the shared-asset reasoning on L20, not from the code.

**`P(file-server fires) = 8/25`, not `1/4`.** The naive sum is
`3/20 + 2/10 = 7/20`, which is larger than the true value because it counts the
"both fire" years twice. Exact: `3/20 + 2/10 − (3/20)(2/10) = 77/400 = 8/25`.
Same bug, one level down — the L04 lesson reappearing inside the fix.

- ☐  Verify `8/25` by hand: ______
- ☐  The file server fires `8/25` of years, not `1/4`. What is the difference in
      expected loss, and does it match what you computed above: ______
- ☐  Why could the simulation never catch this? Answer in one sentence: ______

## PART 4 — RETIRE THE BUG (8 min)

- ☐  **Delete** `expected_loss_v1` and `simulate_year_v1` from `riskkit.py`. Not
      commented out, not kept "for reference." Deleted.
- ☐  Add the regression test that would have caught it *before* U5 L24:

```python
# kill switch: two threats on one asset must cost the asset once
def test_shared_asset_charged_once():
    threats = [
        {"id": "A", "likelihood": F(3, 20), "asset": "file-server"},
        {"id": "B", "likelihood": F(2, 10), "asset": "file-server"},
    ]
    naive = sum(t["likelihood"] * ASSET_VALUE[t["asset"]] for t in threats)
    correct = expected_loss_v3(threats)
    assert naive != correct, "the naive sum must differ, or this test proves nothing"
    assert correct == F(8, 25) * 12000
```

- ☐  The first assertion is the one that matters. A test that passes for the
      wrong reason is worse than no test — write one line saying why the
      negative assertion is there: ______
- ☐  Update the README's "known bug" section with **your** numbers: the naive
      total, the correct total, the gap, and the formula for the gap
- ☐  Run the full suite, paste the output, confirm everything passes

## PART 5 — CLOSE (3 min)

- ☐  The naive functions are gone from the file
- ☐  The regression test exists, passes, and would have failed on L19's code
- ☐  **In writing, one sentence: what other number in your model was computed
      the naive way before this week, and how you now know?** ______

## TURN IN — Closing the Loop

1. `riskkit.py` with the bug deleted and the regression test added
2. The Part 1, Part 2, and Part 3 outputs, run live
3. Updated README section 6 with your real numbers
4. Your sentence from Part 5
5. **No pip installs.** Standard library and SymPy only. Tell me if something is
   missing.

## 🇹🇼 TAIWAN CONTEXT

The direction-of-error question in Part 2 is not a hypothetical. Institutional
risk figures are routinely revised in the conservative direction, because a
number that justifies spending is harder to challenge than one that does not,
and because a team reporting a larger risk has a stronger position in the next
budget conversation than a team reporting a smaller one. The result is a
systematic drift upward in reported exposure that no single report is wrong
enough to catch.

The national CERT's post-incident review practice is explicit on this because it
has had to correct for it: the review recomputes the impact from the asset
register rather than from the sum of incident cost estimates, precisely because
the sum drifts conservative, and it states the recomputed figure alongside the
original with the discrepancy explained. The Ministry of Digital Affairs'
reporting guidance makes the same requirement — impact assessed at asset level,
incident figures reconciled rather than accumulated.

The asymmetry is the real argument, and it is the one worth carrying into your
defence. **A conservative error is noticed, because someone notices you spent
money on a risk that did not materialise. An optimistic error is not noticed,
because nothing happens until the year it was wrong about arrives, and by then
the decision has already been made and the money has already been spent
elsewhere.** The double-count that survived four tests is the same failure in
miniature: it produced a larger number, it looked responsible, and it would
have been defended rather than questioned. That is why your README documents it
in section 6 rather than quietly deleting it — a reader needs to know the number
in section 3 was once different, and by how much, or they cannot judge whether
the current figure is trustworthy.
