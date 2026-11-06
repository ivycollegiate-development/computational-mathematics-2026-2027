# U0 L02 — Day 2: What Is Computational Mathematics? (DISCUSSION)

**Unit:** 0 — Course Survey
**Type:** Paper/Discussion (whiteboard + projector, 45 minutes)
**LO:** explain what "computational math" means; understand the year's arc; connect math to security consequences

---

## TODAY'S PURPOSE

No survey today. No computer. We talk about what this class actually is, where it's going, and why the math matters for security.

---

## PART 1 — SURVEY THEMES (5 min)

"Here is what the class looks like overall." (Aggregated, anonymous.)
- Math comfort spread
- Programming experience spread
- Security awareness — how many have seen phishing, had an account hacked, etc.
- Top curiosities

This is not a ranking. It is a map.

---

## PART 2 — WHAT IS COMP MATH? (10 min)

**Whiteboard brainstorm:** "What happens when you make math doable by a computer?"

Key ideas to surface:
- Computers are fast at arithmetic. Humans are good at strategy. Computational math is where they meet.
- Historical touch: Babbage, Lovelace, Turing — computing *was* math before it was engineering.
- The loop: **model → code → verify → interpret**. The math is in the model and the interpretation. The code is just the bridge.

---

## PART 3 — TOUR THE YEAR (10 min)

Walk through the 7 units and projects on the course README (projector).

| Unit | Focus | Project |
|------|-------|---------|
| 1 | Working with Numbers | Calculator with Guardrails |
| 2 | Visualizing Data | Visualizing Threats |
| 3 | Describing Data with Stats | Privacy-Aware Stats Dashboard |
| 4 | Algebra & SymPy | Cipher Toolkit (Math Wars) |
| 5 | Sets & Probability | Risk Simulator |
| 6 | Geometry & Fractals | Fractal Detection Models |
| 7 | Calculus & Modeling | Anomaly Trend Analyzer |

"By the end, you'll build a cipher tool and a risk simulator that a security team could actually use."

---

## PART 4 — WHY SECURITY? (10 min)

**Discussion:** "Can you think of a time bad math caused a security problem?"

Examples to have ready if they don't surface them:
- **Therac-25** — overconfidence in software, no hardware interlocks, race condition killed patients
- **Patriot missile (1991)** — floating-point rounding error accumulated over 100 hours → 600m position error → missed Scud
- **737 MAX MCAS** — single sensor, no cross-check, math assumed sensor was truth

**Takeaway:** Math isn't just about getting the right answer. It's about knowing when your answer could be weaponized.

---

## PART 5 — TOOLCHAIN PREVIEW (5 min)

Show on projector:
- Google Classroom (assignments, due dates)
- GitHub Codespaces (where we code — no local install required)
- The course repo structure

"We start coding next week. Today was about where we're going."

---

## HOMEWORK

None required. Optional: write 3 sentences about what you're most curious about this year. Drop in the box on the way out or keep it.

---

## 📋 NEXT

**Unit 1 starts next class (L01): Working with Numbers — REPL, types, operators.**

---

## 🇹🇼 TAIWAN CONTEXT

Taiwan's information security curriculum (and the national CERT's training) starts with the same premise: **the math is the attack surface.** A rounding error isn't a bug — it's a vulnerability. This class treats every computation as something that could be relied on for a security decision, so it must be verified, bounded, and honestly documented.