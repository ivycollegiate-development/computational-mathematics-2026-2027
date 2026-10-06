# U5 L23 — Final Rehearsal, Then the Build

**Unit:** 5 — Sets and Probability
**Type:** Paper lesson (final rehearsal, 50 minutes)
**LO:** 5.1–5.10 — one end-to-end scenario, then assemble the unit's artefact

---

**Paper for the first half, laptop for the second.** That is the only split day
in the unit, and it is deliberate: the scenario is the exam, and the build is
the project, and they are graded separately and you should not practise either
one in the wrong register.

## PART 1 — THE SCENARIO (25 minutes, closed book)

One organisation, one question, everything the unit has to offer. Write it as if
you are the analyst and the reader is the operations manager, who will act on
what you write.

> A twelve-person consultancy runs its own file server and staff inboxes. Last
> quarter a contractor's laptop was compromised and used to send invoices to
> three clients. Recovery took nine days and cost 40,000 dollars. A scan last
> week found the file share readable by any account on the corporate network.
>
> The manager asks: **"Should we spend 5,000 a year on a backup, or is that
> over-insurance?"**

- ☐  **S1.** List the threats. Three or four is right. ______
- ☐  **S2.** For each, give a likelihood **with its population and period** and an
      impact, and say in one clause where the likelihood came from. ______
- ☐  **S3.** Which threats hit the same asset, and therefore cannot be counted
      independently? ______
- ☐  **S4.** Compute the expected annual loss, exactly, with the shared asset
      handled the L20 way. Show the work. ______
- ☐  **S5.** The 9-day recovery is the best incident data you have. What is
      wrong with using a single incident to set a likelihood? ______
- ☐  **S6.** The manager reads your EV and says the backup costs more than the
      expected loss, so skip it. Write the **one sentence** that answers them
      correctly — and note that the expected loss you computed is not the right
      quantity for this decision, and say what is. ______
- ☐  **S7.** Write the paragraph that goes with the number. Three sentences
      minimum. This is the graded item. ______
- ☐  **S8.** Name the assumption you are least able to defend, and what
      evidence would fix it. ______

- ☐  **S9 (self-marking, 5 minutes).** Which of S1–S8 would you most want back
      if the page were graded and you could change one? ______
- ☐  **S10.** The thing that would most improve S7 specifically: ______

## PART 2 — THE BUILD (25 minutes, laptop)

You have four files. Assemble the project. This is the artefact.

```
compmath-u5-risk-simulator/
├── README.md          ← today
├── setkit.py          (L03, L04)
├── contingency.py     (L06, L08)
└── riskkit.py         (L10, L12, L14, L16, L18, L20)
```

- ☐  **`README.md`.** This is the graded document, more than the code is. It
      must contain, in this order:

  1. **What this models**, in three sentences, naming the population and the
     period
  2. **How to run it**, including the exact command and the fact that it needs
     only the standard library and SymPy
  3. **The output**, with your real `shape_report` output pasted in, not
     described
  4. **Every assumption**, as a table: assumption, value, provenance, and what
     breaks if it is wrong
  5. **The limits**, in the two sentences from your L15 spec
  6. **The known bug that was fixed** — the L20 double-count, what it did, by
     how much, and what test now kills it

- ☐  **`riskkit.py` imports cleanly** and every function has a docstring stating
      its units and its assumptions
- ☐  **Every test passes.** Run the whole suite live and paste the output into
      the README
- ☐  **No dead code.** If a function is no longer called after the L20 fix,
      either delete it or explain in the README why it stays
- ☐  The README's section 3 and section 6 must be **true**, verified by running
      it, not by describing it

## TURN IN — Final Rehearsal and Build

1. Part 1 photographed in full, self-marked
2. `README.md` committed-ready in the repo (do not commit it — hand it to me)
3. Full test output pasted into the README
4. Your error log, complete for the whole unit

**The README is the deliverable.** Anyone who reads your repository will read
the README and run nothing. If they read it and cannot tell what you assumed and
why, the code behind it does not help them.

## 📋 PREVIEW OF U5 L24

**Next:** L24, Mar 22 — back to the machine, and the day we take the bug from
L20 and *watch it happen in your own model*. You will run the naive aggregator
and the fixed one side by side, confirm the gap is exactly the shared-exposure
credit, and then commit the correct version. After U5 L24 the double-count is
closed.

**Bring U5 L24:** the repository, the README, and any test you are unsure about.

## 🇹🇼 TAIWAN CONTEXT

The scenario is the shape of what the ROC national CERT's SME advisory programme
exists for, and the reason it keeps returning to backups is that S6 is the
decision almost every small organisation gets wrong. The manager compares a
certain 5,000 against an *expected* loss and concludes the backup is
over-insurance. The comparison is between two different kinds of quantity, and
the expected loss is the wrong one: the contractor compromise in the scenario
produced nine days of downtime for a twelve-person consultancy, and a
twelve-person consultancy that is down nine days does not bill for nine days.
The expected value of that is not the cost of nine days; it is the cost of nine
days times a likelihood nobody measured, and the likelihood is the number the
manager is treating as an argument *against* spending.

The national CERT's guidance on this is unusually blunt about the shape of the
error: expected-value reasoning systematically under-protects organisations
whose failure mode is existential, because averaging across many years conceals
the year that ends the business. The Ministry of Digital Affairs' framework for
smaller organisations asks for a worst-credible-case assessment precisely
because the median year is not the year that matters, and because an
organisation that has never tested a restore does not know what its worst case
is.

S8 is the honest version of that. The evidence that would most improve the model
is not a better likelihood — it is a **tested restore with a measured time**,
because that converts an assumption into an observation and turns a projected
nine days into a number somebody actually measured. That is a two-day job for a
twelve-person consultancy, and it is worth more to the risk picture than any
amount of additional modelling.
