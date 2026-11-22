# U3 L05 — Lab: Range, Variance, and Standard Deviation — Follow-Along Sheet

Name: ___________________________  Date: ____   Period: ____

Work top to bottom in your terminal, one step at a time. Change each ☐ to ☑ as you finish that step. Record your own output in the blanks — nothing on this sheet gives you the answer, and every value here is checked against your screen.

## BEFORE CLASS: GitHub Repo Access (5 min — do this FIRST)

**6 students need to CREATE a GitHub account** (exact username, school email):
- ysato27
- pman27
- mkuo27
- eshin27
- atsai27
- atachibana27

☐  Open an incognito tab → `github.com/signup`
☐  Username = your roster ID above (exact match, no extra characters)
☐  Email = your ICA school email
☐  Verify the email link GitHub sends

**12 students have PENDING INVITES** (accept at `github.com/notifications`):
- schen27, pjones, slee27, shuang27, rliu27, rchen27
- pman26, mkuo28, ilin27, ghuang27, eshin28, elin27

☐  Accept the invite for `compmath-u3-stats-lab-<your-ID>_student`

**After accounts are created + invites accepted**, teacher adds you as a collaborator — then all 24 repos are ready to clone.

## 0: Set up

☐  Go to the lab folder and print where you landed:  cd ~/compmath-u3-stats-lab   then   pwd   →  path = ______________________

☐  Read every non-empty line into raw:  raw = [line.strip() for line in f if line.strip()]

☐  Convert to numbers, skipping comment lines:  donations = [float(line) for line in raw if not line.startswith("#")]

☐  Filter the one extreme value, then print both counts:  clean = [d for d in donations if d < 5000]   print(len(donations), len(clean))

| List | How many values |
| --- | --- |
| donations | ______________ |
| clean | ______________ |

## 1: Range

☐  Compute both ranges and the ratio:  r_all = max(donations) - min(donations)   r_clean = max(clean) - min(clean)   print(f"ratio: {r_all / r_clean:.1f}x")

| Quantity | Your value |
| --- | --- |
| range with outlier | ______________ |
| range clean | ______________ |
| ratio r_all / r_clean | ______________ x |

☐  Why is the range the worst of the spread measures? Say how many values it looks at and what it cannot see.

_____________________________________________________________________

☐  Two datasets can have identical ranges and nothing else in common. Describe such a pair, then say what it proves about the range.

_____________________________________________________________________

## 2: Variance by hand

☐  Before any code, work the six paper values 25  40  50  60  75  100 by hand. Find the mean first, to two decimals:

mean = ______________________

☐  Subtract the mean from each value, then square each result. Fill the table:

| Value | Deviation | Deviation squared |
| --- | --- | --- |
| 25 | ______________ | ______________ |
| 40 | ______________ | ______________ |
| 50 | ______________ | ______________ |
| 60 | ______________ | ______________ |
| 75 | ______________ | ______________ |
| 100 | ______________ | ______________ |

☐  Add the squared deviations, then divide that sum by 6:

| Quantity | Your value |
| --- | --- |
| sum of squared deviations | ______________ |
| population variance | ______________ |

☐  Every deviation you wrote is positive. Explain what squaring bought you, and why averaging the raw deviations would have collapsed to zero.

_____________________________________________________________________

## 3: Variance in code

☐  Write it once, exactly as the lab gives it — no statistics library, no pandas:  def variance_of(values):  m = sum(values) / len(values)   total = sum((v - m) * (v - m) for v in values)   return total / len(values)

☐  Run it on both lists and on the same six paper values:

| Set | Variance |
| --- | --- |
| clean | ______________ |
| all 200 | ______________ |
| [25, 40, 50, 60, 75, 100] | ______________ |

☐  The third row is your method check against section 2. Write what a mismatch would tell you:

_____________________________________________________________________

☐  Print the ratio and record it:  print(f"{variance_of(donations) / variance_of(clean):.0f}x")   →  variance ratio = ______________________ x

☐  Explain that ratio in your own words, then say why the variance distorts harder than the standard deviation will. Use the word squaring.

_____________________________________________________________________

## 4: Standard deviation

☐  Variance is in dollars squared, which nobody can picture. Record the unit the standard deviation comes back in:

stdev unit = ______________________

☐  Un-square your own function:  def stdev_of(values): return variance_of(values) to the power 0.5   then run it on both lists and print sd_all / sd_clean

| Quantity | Your value |
| --- | --- |
| stdev clean | ______________ |
| stdev all | ______________ |
| ratio sd_all / sd_clean | ______________ x |

☐  One outlier made the variance ratio enormous and the stdev ratio far smaller. Explain the gap between the two.

_____________________________________________________________________

## 5: The standard deviation as a ruler

☐  Use your own functions, not numbers copied from anyone. Compute the center, the ruler, and the one-sd window  low, high = mean - sd, mean + sd  for the clean list, then fill in your four values:

| Quantity | Your value |
| --- | --- |
| mean_of(clean) | ______________ |
| stdev_of(clean) | ______________ |
| low | ______________ |
| high | ______________ |

☐  Count what lands inside the window and print the share:  inside = sum(1 for d in clean if low <= d <= high)   print(f"{inside}/{len(clean)} = {100*inside/len(clean):.0f}%")

| Result | Your value |
| --- | --- |
| inside | ______________ of 199 |
| inside as a percent | ______________ % |

☐  The empirical rule predicts roughly 68% for a normal, symmetric distribution. Compare your percent with 68% — is this data more clustered or less, and what about its shape causes that?

_____________________________________________________________________

☐  Put the outlier back and describe the all-data set the same way, mean ± stdev:

mean of all = ______________________

stdev of all = ______________________

☐  Read that pair aloud. What happened to the meaning of the number a typical donation sits near?

_____________________________________________________________________

## 6: All four, side by side

☐  Write spread.py holding mean_of, median_of, variance_of and stdev_of, then loop over ("all 200", donations) and ("clean 199", clean) printing a header row and one formatted row per set. Copy your own run into both tables below.

☐  Make spread.py load its own data at the top: open data/u3_donations.txt, strip blank lines, skip lines starting with #, convert to float, then build clean with d < 5000. It must run with `python3 spread.py` from the repo root — variables from step 0 do not exist when you run the file.

| Set | Mean | Median |
| --- | --- | --- |
| all 200 | ____________ | ____________ |
| clean 199 | ____________ | ____________ |

| Set | Range | Std dev |
| --- | --- | --- |
| all 200 | ____________ | ____________ |
| clean 199 | ____________ | ____________ |

☐  Two of those four columns are robust and two are not. Name the two robust columns:

robust: ______________________  and  ______________________

☐  What makes a column robust? Define it in terms of one extreme value moving the number or not moving it.

_____________________________________________________________________

☐  A donor gets to see the mean plus exactly one more number. Which column do you show, and why is it not the range?

_____________________________________________________________________

## 7: Why spread can beat the center

☐  Two classes both average 80: one with sd 3, one with sd 15. Two students are absent from the second class — can you predict their scores? Say why that mean describes a typical student so badly.

_____________________________________________________________________

☐  A model's error is reported as mean absolute error. What does one huge outlier do to that average, and what would you report beside it?

_____________________________________________________________________

☐  The median cannot see an extreme value. Which of this lab's four measures can? Name it and say why.

_____________________________________________________________________

## 8: Save and push

☐  git add spread.py

☐  git commit -m "U3 L05 range, variance, and standard deviation over donations"

☐  git push   →  Paste the push URL GitHub printed:

_____________________________________________________________________

## 9: Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment.

☐  Put these four numbers from your own run in the push message:

mean of all 200 = ______________________

standard deviation of all 200 = ______________________

standard deviation with the outlier removed = ______________________

percent of clean values within one sd of the mean = ______________________

☐  Keep the terminal open for a spot-check. Due 11:59 PM.