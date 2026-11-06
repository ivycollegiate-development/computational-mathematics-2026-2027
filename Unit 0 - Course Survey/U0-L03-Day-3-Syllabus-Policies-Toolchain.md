# U0 L03 — Day 3: Syllabus, Policies & Toolchain Setup (TECH)

**Unit:** 0 — Course Survey
**Type:** Machine (first Codespaces session, 45 minutes)
**LO:** navigate Google Classroom, launch Codespaces, understand grading policy, run first `hello.py`

---

## TODAY'S PURPOSE

First hands-on tech day. You will not write real code yet — you will set up the environment you'll use all year, and understand how this class is graded.

---

## PART 1 — SYLLABUS HIGHLIGHTS (10 min)

**Key policies (full syllabus on Classroom):**

| policy | detail |
|--------|--------|
| **Grading** | 40% projects (7), 30% assessments (7), 20% daily work, 10% reflection journal |
| **Late work** | -10% per day, max 3 days. Extensions = email *before* deadline. |
| **AI use** | Allowed for explanation, not for writing your code. `git blame` shows what you typed. |
| **Collaboration** | Discuss ideas freely. Code you submit must be typed by you. Pair programming = two keyboards, one driver at a time. |
| **Academic honesty** | Copying = zero on assignment + parent meeting. Second offense = course failure. |

**The journal:** One entry per lesson (paper or digital). "What I did, what broke, what I learned." Not graded for correctness — graded for *existence and honesty*.

---

## PART 2 — GOOGLE CLASSROOM (5 min)

- Join class: **code on board**
- Stream = announcements. Classwork = assignments by unit.
- Due times: **23:59 Taipei** (not your local time if you're traveling).

---

## PART 3 — GITHUB CODESPACES (25 min)

**This is your development environment for the year. No local Python install required.**

1. Go to `github.com/ivycollegiate-development/computational-mathematics-2026-2027`
2. Click **Code → Codespaces → Create codespace on main**
3. Wait 60–90 seconds for the container to build
4. You now have: VS Code in browser, Python 3.11, `git`, `pytest`, `matplotlib`, `sympy`, `numpy`, `pandas`

**Verify it works:**

```bash
python3 --version
git --version
python3 -c "import sympy, matplotlib, pandas, numpy; print('all packages OK')"
```

**Your first program:**

Create `hello.py`:
```python
#!/usr/bin/env python3
"""First program — verify the environment works."""

name = input("Your name: ")
print(f"Hello, {name}. Welcome to Computational Mathematics 2026-2027.")
```

Run it: `python3 hello.py`

**Commit and push (practice):**
```bash
git add hello.py
git commit -m "U0 L03: first hello.py"
git push
```

---

## PART 4 — CLASSROOM ASSIGNMENT (5 min)

Open the **U0 L03** assignment on Classroom.

**Turn in:** Screenshot showing:
1. `python3 hello.py` running with your name
2. `git push` confirmation with your commit message

---

## TURN IN (Google Classroom, due 23:59 tonight)

Screenshot as described above.

---

## 📋 TOMORROW

**Next:** U0 L04 — Pre-Assessment & Icebreaker Coding. A short paper diagnostic, then a fun REPL exploration.

---

## 🇹🇼 TAIWAN CONTEXT

Codespaces is the great equalizer — every student gets the same Linux container, same Python, same packages, regardless of whether they're on a school Chromebook, a MacBook, or a borrowed laptop. This is how Taiwan's MOEA sandbox and g0v hackathons run: identical environments so "it works on my machine" is never an excuse.