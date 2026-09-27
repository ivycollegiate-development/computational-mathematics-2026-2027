# U4 L05 — Modular Arithmetic: The Algebra Underneath the Cipher

**Date:** Jan 11 (Mon)
**LO:** do arithmetic in `Z_n`, find modular inverses, and explain why Fermat's little theorem makes public-key cryptography possible.

Everything so far this unit has been real algebra: `x` is a number, somewhere,
unbounded. Today `x` stops being a number and becomes a **position on a clock**.
`2 + 4` is not `6` anymore. It is wherever the hour hand lands.

This is the day the algebra becomes useful for something you would actually
build.

## PART 1 — WHY `(-3) % 5` IS NOT `-3` (12 min, code-along)

Start with the surprise, because everything else follows from it.

```python
print((-3) % 5)      # 2
print(-3 % 5)        # 2
print(3 % 5)         # 3
print(15 % 5)        # 0
print(15.5 % 5)      # 0.5
```

The rule, stated once: **`a % n` is the unique value in `[0, n)` that is
congruent to `a`.** Not "how much is left over" in the way you said it in
primary school. It always lands in `[0, n)`, so it is never negative.

Confirm with SymPy, which makes the modulus explicit rather than implied:

```python
from sympy import Mod, symbols, simplify
x = symbols('x')
print(Mod(-3, 5))                 # 2
print(simplify(Mod(x + 7, 3) - Mod(x + 7, 3)))   # 0
print((x + 7) % 3 == Mod(x + 7, 3))              # True, symbolically
```

- ☐  On a 12-hour clock, what is `(9 - 4) % 12` and what is `(4 - 9) % 12`?
     ______
- ☐  Why does that asymmetry matter? One sentence. ______

That asymmetry is the whole reason modular arithmetic is not just "clock
arithmetic done fussy." Going backwards is genuinely different from going
forwards, and most of today's cipher work lives in going backwards.

## PART 2 — ARITHMETIC IN `Z_n` (15 min)

Modular arithmetic satisfies all the usual rules, and the reason is worth
stating: **you can reduce at any point, because reduction is compatible with
the operations.** Watch it work.

```python
def z(a, n):
    """Reduce a into [0, n)."""
    return a % n

n = 7
# addition and multiplication are closed and associative: order does not matter
print([z(z(2+3, n) + 5, n), z(2 + z(3+5, n), n)])    # [3, 3]
print([z(2*3, n), z((2*5)*(3*5), n), z(2*5, n)*z(3*5, n) % n])
# negatives still behave
print([z(-1, n), z(-1*2, n), z(z(-1, n)*2, n)])
```

Record what you observe:

| property | holds in Z_7? | what would break it |
|---|---|---|
| commutativity of `+` | | |
| associativity of `+` | | |
| distributivity of `*` over `+` | | |
| a multiplicative identity `1` | | |
| every element has a multiplicative inverse | | |

**That last row is where it all falls apart.** In ordinary arithmetic every
nonzero number has a reciprocal. In `Z_7`, `2 × 4 = 8 ≡ 1`, so 2 has an inverse.
But `2 × 0 = 0`, so **0 has no inverse, and no other number can give it one.**
The set of *invertible* elements is smaller than the set of nonzero elements,
and that gap is the entire basis of modern cryptography.

```python
from sympy import factorint
import math
for n in (7, 26, 91, 100, 97):
    invs = [a for a in range(1, n) if math.gcd(a, n) == 1]
    print("n=%-4d factors=%-16s invertible=%d of %d" % (n, factorint(n), len(invs), n-1))
```

Use `math.gcd`, **not** `pow(a, -1, n)`, when you are counting. `pow(a, -1, n)`
raises on a non-invertible `a`, so the loop would die on `n = 26` at `a = 2` and
you would learn nothing about the rest. A scan should not crash on the very
thing it is scanning for.

- ☐  Which of those five `n` is the interesting one for a cipher alphabet, and
     why? ______
- ☐  Look at the factorizations. What is the pattern connecting "has an inverse"
     to the factorization? ______

`91 = 7 × 13` is the answer to the first. It has 72 invertible elements out of
90, and any `a` divisible by 7 or 13 is dead as a multiplier. `100 = 2² × 5²`
is the extreme case. **Pick a modulus with no small factors and your cipher
stops falling apart.**

## PART 3 — INVERSES AND FERMAT'S LITTLE THEOREM (20 min)

`pow(a, -1, n)` computes the modular inverse. When it raises `ValueError`, `a`
has none — and that exception is the security check.

```python
print(pow(3, -1, 26))    # 9  -- because 3*9 = 27 = 1 (mod 26)
try:
    pow(13, -1, 26)      # 13 shares a factor with 26
except ValueError as exc:
    print("no inverse:", exc)
print([a for a in range(26) if (3*a) % 26 == 2])   # [18]
```

That last line is **solving a congruence**, and it is the exact analogue of
`solve` from L04 — a linear equation, in a ring with 26 elements. Notice that
`3⁻¹ = 9` and then `9 × 2 = 18`, same as the algebra you already know.

**Fermat's little theorem.** If `p` is prime and `a` is not divisible by `p`,
then

```
a^(p-1) ≡ 1  (mod p)
```

Check it for `p = 5`:

```python
print([pow(a, 4, 5) for a in range(1, 5)])    # [1, 1, 1, 1]
```

- ☐  Run it for `p = 7`. Do you get all ones? ______
- ☐  Now run it for `p = 8`, which is **not** prime. What happens, and which `a`
     breaks it? ______

The `p = 8` case is the theorem telling you that primality is doing real work.
And primality is exactly what is expensive to establish — which is the whole
game:

```python
from sympy import isprime, factorint
print(isprime(2**7 - 1), factorint(2**7 - 1))    # True {127: 1}
print(isprime(2**11 - 1), factorint(2**11 - 1))  # False {23: 1, 89: 1}
print(isprime(2**13 - 1), factorint(2**13 - 1))  # True {8191: 1}
```

- ☐  `2^11 - 1 = 23 × 89`. How many factors did you have to try to find that,
     and how big is `2^11 - 1`? ______
- ☐  Why does *one* big factor found quickly matter more than the size of the
     number? ______

**Write this sentence in your own words:** a public key is easy to *use* and
hard to *invert*, because inverting means factoring a very large number.

## PART 4 — BUILD `modkit` (25 min)

New module, `modkit.py`. This is the engine of the Unit 4 project, so it gets a
real docstring and real error handling.

```python
"""modkit.py — modular arithmetic helpers for the Unit 4 cipher toolkit.

Q1: Why must every function validate n > 1? What breaks at n = 1?
Q2: Why do we use pow(a, -1, n) instead of a / a in reverse?
Q3: What does a ValueError from pow(a, -1, n) actually tell an attacker?
Q4: Why is 'is the modulus prime' a different question from 'is the modulus
    large'? Which one actually protects the cipher?
Q5: Which function here would be worst to ship broken, and what breaks first?
"""

import math
from sympy import factorint, isprime

try:
    from sympy import Mod
except ImportError:
    raise SystemExit("SymPy is not installed here. Tell me — do not pip install anything.")


def validate_modulus(n):
    """Return n if it is a usable modulus, else raise ValueError explaining why."""
    if not isinstance(n, int) or n < 2:
        raise ValueError("modulus must be an integer >= 2, got %r" % (n,))
    return n


def shift_cipher(text, k, n=26, decrypt=False):
    """Shift each a-z letter by k within Z_n. Non-letters pass through."""
    validate_modulus(n)
    k = -k % n if decrypt else k % n
    out = []
    for ch in text:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord('a') + k) % n + ord('a')))
        else:
            out.append(ch)
    return "".join(out)


def affine_cipher(text, a, b, n=26, decrypt=False):
    """Affine cipher on a-z letters. Requires gcd(a, n) == 1 to be invertible.

    Encrypts each letter p as (a*p + b) % n.
    Decrypts by solving p = a_inv * (c - b) % n.
    Raises ValueError from pow(a, -1, n) if a is not invertible.
    """
    validate_modulus(n)
    if decrypt:
        a_inv = pow(a, -1, n)      # ValueError when gcd(a, n) != 1
        return "".join(
            chr(((ord(c) - ord('a') - b) * a_inv) % n + ord('a'))
            if "a" <= c <= "z" else c
            for c in text
        )
    return "".join(
        chr(((ord(c) - ord('a')) * a + b) % n + ord('a'))
        if "a" <= c <= "z" else c
        for c in text
    )


def modulus_report(n):
    """Report the factorization, primality, and invertibility count of n."""
    validate_modulus(n)
    invertible = sum(1 for a in range(1, n) if math.gcd(a, n) == 1)
    return {
        "n": n,
        "factors": factorint(n),
        "is_prime": bool(isprime(n)),
        "invertible_count": invertible,
        "invertible_fraction": round(invertible / (n - 1), 3),
    }
```

Round-trip it:

```python
import modkit

for msg in ["attackatdawn", "hello world", "the quick brown fox"]:
    ct = modkit.affine_cipher(msg, 7, 3)
    back = modkit.affine_cipher(ct, 7, 3, decrypt=True)
    print("%-22s -> %-22s -> %s  %s" % (msg, ct, back, "OK" if back == msg else "FAIL"))

for n in (7, 26, 91, 100, 97):
    r = modkit.modulus_report(n)
    print("%-4d prime=%-6s invertible=%-4d factors=%s" % (r["n"], r["is_prime"], r["invertible_count"], r["factors"]))
```

Correct output for the first block — **every row must end in `OK`**. A `FAIL`
means your encrypt and decrypt are not inverses, and the bug is almost always a
sign or a misplaced `% n`:

```
attackatdawn          -> tmmtvdtmwtpg        -> attackatdawn        OK
hello world           -> axeeh phkew         -> hello world         OK
the quick brown fox   -> max jnbvd ukhpg yhq -> the quick brown fox OK
```

And the decryption failure you are asked to test produces exactly this — a
named error, not garbage:

```
ValueError: base is not invertible for the given modulus
```

- ☐  Every round trip returns `OK`
- ☐  `modkit.affine_cipher("hi", 13, 3, decrypt=True)` raises `ValueError`
      rather than producing garbage — test it and paste the message
- ☐  `modulus_report` never divides by zero for any `n >= 2`

## PART 5 — THE ATTACK, WRITTEN OUT (8 min)

You now have enough to break the shift cipher, which is a Caesar cipher. Do the
arithmetic, not the code, and record it.

Ciphertext: `dwwdfndwgdzq`

1. Try **all 26** shifts by hand, or write a loop, and find the one that
   produces readable English. Plaintext: ______
2. Why does that work with **zero** information about the key? ______
3. Your `affine_cipher` with `a = 7, b = 3` is harder — but only
   **12 × 26 = 312** keys, because `modulus_report(26)` told you only 12 values
   of `a` are invertible. How would you break it, and how many tries? ______
4. Now scale: an affine cipher over a 97-letter alphabet. How many invertible
   `a` values? ______
5. **The important question:** what is the first thing you should *not* do when
   a company tells you a cipher uses a modulus of 100? ______

## TURN IN (Google Classroom, due 11:59 PM tonight)

1. `modkit.py` and your round-trip test, pushed
2. Your **Part 2 property table** with all five rows filled in, including the
   one where the answer is "no"
3. Your **Part 3 answers**, with the `p = 8` failure named
4. Your **Part 5 five answers** — especially #5, in your own words
5. One paragraph: the public key sentence from Part 3, written as if explaining
   it to a classmate who has never heard of factoring

**Part 2's fourth row and Part 5's fifth answer are the graded ones.** The rest
is bookkeeping. A student who can say precisely *why* `0` has no inverse, and
what that means for a cipher, has understood the unit.

## 📋 PREVIEW OF TOMORROW

**Next:** L06, Tue Jan 12 — paper. **Midterm consolidation block, day 1.** Units 1
through 4 on paper, cold, timed. Bring your Unit 3 break pages and your Unit 4
error log; you will need both.

**Bring tomorrow:** pencil, notebook, your error log, and your L05 output
printed or on screen at home. No laptop in the room.

## 🇹🇼 TAIWAN CONTEXT

The shift cipher is the same idea as the **Caesar cipher** named for Julius
Caesar, and ROT13 — which is what every internet forum uses to hide spoilers —
is a shift cipher with `k = 13`, and with `n = 2`, because ROT13 applied twice
gives back the original. There is a reason it is considered security theater
rather than security, and after Part 5 you can explain that reason in one
sentence.
