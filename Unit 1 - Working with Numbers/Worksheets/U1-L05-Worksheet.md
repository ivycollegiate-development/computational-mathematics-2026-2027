# U1 L05 — Reflection Worksheet: Trust Nothing the User Types

Names: ___________________________  Date: ____

Paper first, terminal after. Parts 1 and 2 are done in your notebook; the terminal parts come with the class.

## Part 1 — Reconstruct U1 L04 (10 min)

Answer in your own words before we go over anything.

1. What does `input()` hand your program, no matter what the user types?

   _________________________________________________________________________

   _________________________________________________________________________

2. Why did `age = int(input("Age: "))` need the `int()` around it?

   _________________________________________________________________________

3. We typed `banana` into the age calculator. What was the error called, exactly?

   _________________________________________________________________________

4. `int("  42  ")` worked but `int("4 2")` crashed. What was the difference?

   _________________________________________________________________________

   _________________________________________________________________________

Now the sentence the whole part is for — write it in your own words:

   _________________________________________________________________________

## Part 2 — What else could go wrong? (15 min)

In your group, list bad inputs for a program that asks for a number. Push past the obvious three.


| # | Bad input (something a user might actually type) | What happens? |
|------------|--------------------------------------------------|---------------|
| 1 |                                            |                         |
| 2 |                                            |                         |
| 3 |                                            |                         |
| 4 |                                            |                         |
| 5 |                                            |                         |
| 6 |                                            |                         |

The rule you are building toward — a validator answers three questions about every value:


| Validator question | How I would check it, in Python |
|--------------------|---------------------------------|
| Is it the right TYPE?                 |                                                         |
| Is it in RANGE?                       |                                                         |
| Is it the right UNIT?                 |                                                         |

## Part 3 — The functions we know (15 min)

Predict first, then test in the REPL and correct yourself.


| Expression | My prediction | What Python actually gives | What type is that? |
|------------|---------------|----------------------------|--------------------|
| `int("3.7")`            |                         |                        |       |
| `float("3.7")`          |                         |                        |       |
| `7 / 2`                 |                         |                        |       |
| `7 // 2`                |                         |                        |       |
| `7 % 2`                 |                         |                        |       |
| `1 / 3`                 |                         |                        |       |
| `Fraction(1, 3)`        |                         |                        |       |
| `0.1 + 0.2 == 0.3`      |                         |                        |       |

Where does `Fraction` come from, and why is it exact where `1 / 3` is not?

   _________________________________________________________________________

   _________________________________________________________________________

## Part 4 — The terminal (10 min)

For each: what does it do, and what happens if you skip it?


| Command | What it does | Why it matters here |
|------------|--------------|---------------------|
| `pwd`                                            |                                      |                                    |
| `cd ~`                                            |                                      |                                    |
| `cd ~/computational-mathematics-2026-2027`        |                                      |                                    |
| `ls`                                              |                                      |                                    |
| `git pull`                                        |                                      |                                    |

## Part 5 — Journal (last 5 min)

Which input from Part 2 is the most dangerous, and why?

   _________________________________________________________________________

   _________________________________________________________________________

What is the ONE rule you will apply to every program you write from here on?

   _________________________________________________________________________

## TURN IN

- ☐  Parts 1–5 answered in your notebook, in your own words.
- ☐  Screenshot to the Classroom assignment by 11:59 PM tonight showing: your Part 3 REPL outputs, your Part 4 terminal outputs, and the successful `git push`.

Keep the notebook — the U1 L11 calculator lab is graded on exactly this.
