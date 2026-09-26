# U2 L18 — Project Final Push: Polish and Submit

**LO:** finish the Unit 2 project to a submittable standard — three correct charts, honest analysis, clean code — and submit it.

Today is the last working day on the project. You are not building anything new.
You are taking what you have and making it **correct, complete, and honest** — then
submitting it.

## PART 0 — OPEN YOUR REPO AND AUDIT YOURSELF (first 15 minutes)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
ls
python3 project.py
```

Now grade yourself honestly against the rubric. Tick a box only if it is **true**,
not if it is nearly true:

**Data integrity:**

- ☐  `project.py` runs start to finish with **no error output**
- ☐  It prints the row count **before and after** cleaning
- ☐  I can state exactly how many rows I dropped and why
- ☐  The dates parse into chronological order (the timeline is not scrambled)

**The three required charts:**

- ☐  `timeline.png` exists, has a title, and both axis labels
- ☐  `weekday.png` exists, has a title, and both axis labels
- ☐  `histogram.png` exists, has a title, and both axis labels
- ☐  I chose the histogram's bin count **on purpose** and can say why
- ☐  Every chart's code has a one-line comment saying what it shows

**Analysis (`analysis.md`):**

- ☐  One paragraph per chart — three paragraphs total
- ☐  Each paragraph names the audience and the one thing they should notice
- ☐  Each paragraph contains **one honest limitation**
- ☐  I did not claim anything the chart does not actually show

**The honesty audit — do this last, and do it seriously.** Look at each of your
three charts and ask:

- Does my y-axis start at zero? If not, do I **say why** somewhere in `analysis.md`?
- Did I drop any rows that would have made my story less dramatic? If so, why was
  dropping them correct — and did I say so?
- Is there anything in my data I chose not to plot? A careful reader would notice.
  Say so yourself, before they ask.

An honest limitation is not a weakness in your write-up. It is the sentence that
tells your reader you understood your own data.

## PART 1 — FIX WHAT IS ACTUALLY WRONG (main work block, ~40 min)

Work in this order. Do not skip to polish while something is still broken.

1. **Does it run?** No error, no blank PNG, no missing chart. Fix this before
   anything else — a chart that does not exist cannot be polished.
2. **Are the numbers true?** Re-read your cleaning code. If you skipped a row
   because of a parsing error, is that row actually malformed, or did your parser
   just not understand a valid value? These are different bugs and only one of them
   is acceptable.
3. **Do the labels tell the truth?** A y-axis label that says "attacks" when the
   column is `failed_logins` is a lie in a chart title. Rename the label.
4. **Now** polish: colors, `plt.tight_layout()`, readable font sizes.

If a chart is missing, say so in `analysis.md` and explain what you tried. A
documented gap is honest work. A silent gap is a lie.

## PART 2 — FINAL SUBMISSION (last 20 min)

Push your finished work:

```bash
cd ~/compmath-u2-data-lab
git add project.py analysis.md
git add timeline.png weekday.png histogram.png
git commit -m "final: three visualizations with analysis"
git push
```

Then open or update your Pull Request on github.com (Contribute → Open pull
request). If you already opened one on U2 L16, **update it** — do not open a
second one.

Before you submit, verify on github.com that all of this is actually visible:

- ☐  `project.py` opens and is the version you just pushed
- ☐  all three PNGs are visible in the repo, and each one renders
- ☐  `analysis.md` shows all three paragraphs
- ☐  the Pull Request page shows your latest commit

## TURN IN — PULL REQUEST LINK (due 11:59 PM tonight)

One submission showing, in order:
1. your completed self-audit checklist, with the honesty audit answered in writing
2. your final `git push` confirmation
3. your updated Pull Request page on github.com, with the latest commit visible

Submit the PR link to this assignment on Google Classroom.
Keep the terminal open — spot-checks.

(Password prompt = Personal Access Token, not your GitHub password.)

**Next:** U2 L19 — Reflection: Unit 2 Wrap (https://github.com/ivycollegiate-development/computational-mathematics-2026-2027/blob/main/Unit%202%20-%20Visualizing%20Data/U2-L19-Reflection-Unit-2-Wrap-What-Makes-A-Secure-Visualization.md)
