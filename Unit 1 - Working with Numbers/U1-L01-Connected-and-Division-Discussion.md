# U1 L01 — Getting Connected + Discussion: `/` vs `//`

**Unit 1 · Tuesday (Discussion day)**

## Plan

- **First half (~20 min):** Finish Sept 7 work — everyone connected to GitHub and Codespaces
- **Second half (~20 min):** Short discussion — `/` vs `//`

---

## Part 1: Getting Connected (first ~20 minutes)

Work in your VS Code workspace (https://vscode.ivycollegiate.org/). Complete each check below in your own environment:

1. ☐ I can log into my GitHub account (in the workspace browser)
2. ☐ I have accepted the Classroom assignment invite (check school Gmail)
3. ☐ I have opened my repo in a Codespace (it loads, not stuck spinning)
4. ☐ I ran `python3 --version` in the Codespace terminal

**Exit check:** Raise your hand when all four are done — I'll come verify your Codespace is live.

---

## Part 2: Discussion — What's the difference between `3/2` and `3//2`? (~20 minutes)

Type both into your Codespace terminal:

```
>>> 3 / 2
>>> 3 // 2
```

### Talk about (pick 2-3, don't rush all of them):

1. **What did each one print? Why?**
   - `/` always gives a `float`, `//` chops off the decimal part (floor division).

2. **When would you actually want `//`?**
   - Splitting people into teams, pages of results, whole items only — "you can't have half a person."

3. **What about negative numbers?** Try it:
   ```
   >>> -7 // 2
   ```
   - It floors *down*, not just "drops the decimal." Surprising!

4. **Why does Python even have two ways to divide?**
   - The security lens: Therac-25 and Ariane 5 both involved numbers being converted/wrong. Choosing the *right* kind of division is a small version of the same idea — picking the tool that matches what the data really means.

### Journal (last 5 minutes)

Create a file in your home directory called `journal-0908.md` (in VS Code: File → New File → save as `journal-0908.md`) and write 2-3 sentences:
- One situation where `//` is the *correct* choice, and one where `/` is.
- Which one do you think is more dangerous if you pick the wrong one? Why?

---

## TURN IN — SCREENSHOT (due 11:59 PM tonight)

One screenshot showing, in order:
1. `pwd`
2. `git clone`
3. `ls`
4. the `/` vs `//` outputs

Submit the screenshot to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

**Grading note (for me):** No automated check exists or applies here — students clone my repo, so nothing lands on GitHub to grade. Screenshot = participation evidence; spot-check 2-3 students' live screens during the exit-check walk to cover the gameability gap. First CI-gradable check lands with the Calculator project (grade.yml pattern from password-strength-lab).
