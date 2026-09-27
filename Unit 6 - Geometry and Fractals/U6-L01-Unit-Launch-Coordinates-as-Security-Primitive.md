# U6 L01 — Unit Launch: Coordinates as a Security Primitive

**Date:** Monday, April 12, 2027
**Unit:** 6 — Geometry and Fractals
**Type:** Paper lesson (45 minutes)
**LO:** 6.1 — explain why a position on a plane is a *fact about a system*, and
read coordinates as evidence rather than as homework

---

**No laptop today.** Pencil, ruler, and graph paper. Everything today is a
claim you make and a claim you support.

We open this unit in April, four months in, with a subject that looks like it
belongs to a different class. Here is why it does not.

A security system is a set of things in *positions*. Firewalls have positions.
Servers have positions. Sensors have positions. An attacker who wants to know
where something is does geometry — the same geometry you did in eighth grade,
done carefully instead of quickly. When we get to fractals in two weeks, that
will pay off too: the reason a detector built on a naive fractal measure fails
is a geometric mistake, not a statistical one.

## PART 1 — A POINT IS AN ASSERTION (12 min)

A coordinate is not a description. It is a **claim that a thing is here**, and
like every claim, it is either true, false, or unverified.

Write each of these as a claim about a system, not a statement about maths.

1. The camera is at `(0, 0)`. What has to be true for that to be a useful fact?

   Claim: ______________________________________

2. The camera is at `(0, 0)` and the door is at `(30, 40)`.

   How far apart are they, and how confident are you in that number?

   Distance = ______  confidence: ______

3. Someone moves the camera and **does not update** the record.

   What is the name of the failure in the sentence "the door is at `(30, 40)`"?

   The sentence is now: ______________________

The third one is the whole lesson. The coordinates did not change. The *truth*
about the coordinates changed, and nothing in the coordinate system noticed.
This is a stale-state bug wearing a geometry costume, and you have already met
it in Unit 4 with a key that was rotated without being updated.

- ☐  In one sentence: why is a coordinate *evidence* and not *truth*?

## PART 2 — DRAW THE SYSTEM (15 min)

On the axes below, place **six nodes of a small network**. Use these rules:

- ☐  Two of them are on the same vertical line
- ☐  Two of them are on the same horizontal line
- ☐  One is inside the convex hull of the others (not on the edge)
- ☐  One pair is exactly at distance 5 from each other
- ☐  None of them is at the origin

Then, for **each** node, write down one question you would need answered before
you trusted that coordinate.

| node | coordinate I drew | what must be verified before I trust it |
|------|-------------------|------------------------------------------|
| A | | |
| B | | |
| C | | |
| D | | |
| E | | |
| F | | |

Now pick the **one** node whose coordinate would be the most damaging to get
wrong, and say why.

- ☐  The node that matters most: ______ because ______

## PART 3 — SCALE, AND WHY IT LIES (12 min)

A coordinate is meaningless without a unit, and the unit is a decision someone
made.

Read these two and fill the table:

| the claim | what it assumes about scale | what breaks if the assumption is wrong |
|---|---|---|
| "the sensor moved 3 units" | | |
| "the sensor moved 3 metres" | | |
| "the anomaly is at distance 0.02" | | |
| "the two devices are within 0.5%" | | |

- ☐  Which of these four would you sign your name to? ______
- ☐  Which one is a *derived* number rather than a measured one? ______
- ☐  Here is the trap: a **small** number and a **precise** number are
     different things. Give an example of a number that is precise and wrong.
     ______

That last row is the one that costs money. `0.0001` has four decimal places and
could still be a guess. Precision is a property of how you wrote the number.
Accuracy is a property of the world.

## PART 4 — THE UNIT IN ONE SENTENCE (6 min)

Before you leave, finish this in writing, in one sentence each:

- Geometry gives you ______, and it does not give you ______.
- A number in this class is always ______.

## 🇹🇼 TAIWAN CONTEXT

Coordinate and geospatial data has a specific local shape: national road and
address data in Taiwan uses WGS84, and the working projections in common use
are TWD97 (TMPA) for western Taiwan and TM2 for the east. Same numbers,
different reference frame — a point measured in one and plotted in the other
lands tens to hundreds of metres away. A monitoring system that mixes the two
produces an alert about a device that never moved. **The frame is part of the
coordinate**, and forgetting that is a real incident class, not a textbook
trick.

**Next:** L02, Tue Apr 13 — distance, midpoint, and slope by hand. Pencil
again, and we will not open a terminal until Wednesday.
