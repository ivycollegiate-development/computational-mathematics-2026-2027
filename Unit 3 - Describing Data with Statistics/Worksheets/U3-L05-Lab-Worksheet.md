# U3 L05 — Lab: Range, Variance, and Standard Deviation — Follow-Along Sheet

Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal. Change each ☐ to ☑ as you finish that step. Everything you record here comes off your own screen — nothing on this sheet tells you the answer. No statistics library and no pandas: you write the formulas.


## 0: Set up


☐  Go to the lab repo:  cd ~/compmath-u3-stats-lab   then  pwd  →

☐  Load donations and build clean the same way you did in L03.

☐  Record what it prints:  ______________________  donations,  ______________________  clean


## 1: Range


☐  Compute r_all and r_clean and the ratio between them. Record:  with outlier ______________________   clean ______________________   ratio ______________________x

☐  Why is the range the worst possible measure of spread? Name what it ignores.

☐  Describe two datasets with the same range and completely different data:


## 2: Variance by hand first


Do the six paper-day numbers 25 40 50 60 75 100 on paper before you write any code. Mean:


| Value | Deviation from the mean | Deviation squared |
| --- | --- | --- |
| 25.00 | ______________ | ______________ |
| 40.00 | ______________ | ______________ |
| 50.00 | ______________ | ______________ |
| 60.00 | ______________ | ______________ |
| 75.00 | ______________ | ______________ |
| 100.00 | ______________ | ______________ |



☐  Sum of the squared deviations: ______________________     Divide by 6 → population variance:

☐  Now write variance_of() and run it on clean and on all. Record:  clean ______________________   all

☐  Check your function against your paper work on the six numbers. Record what it returns: ______________________  (it must match your own arithmetic, or the function is wrong)

☐  The full data’s variance is thousands of times the clean variance. Explain that ratio in your own words:

☐  Why does the variance distort MORE than the standard deviation will?


## 3: Standard deviation


☐  Write stdev_of() as the square root of your own variance_of, then run it. Record:  clean ______________________   all ______________________   ratio ______________________x

☐  The variance grew by a factor of thousands and the standard deviation by a factor of tens. Explain the gap:

☐  Use the standard deviation as a ruler. Count how many of the clean values fall outside mean ± 1 sd. Record: ______________________ of 199 = ______________________ %

☐  The empirical rule predicts about 68%. Why is this number different, and what does that tell you about using the rule?

☐  With the outlier included, the typical donation becomes 716.07 ± 6330.32. Read that aloud. What has happened to the meaning of the number?


## 4: Side by side — the full description


☐  Write spread.py and run it. Copy your own output into the table:


| Set | Mean | Median | Range | Std dev |
| --- | --- | --- | --- | --- |
| all 200 | __________ | __________ | __________ | __________ |
| clean 199 | __________ | __________ | __________ | __________ |



☐  Two of those four columns are robust and two are not. Which two, and what makes a column robust?

☐  If a donor could see only ONE extra number beside the mean, which column, and why is it not the range?


## 5: Why spread can beat the center


☐  Two classes both average 80: one with sd 3, one with sd 15. Why is the second mean a worse description of a typical student?

☐  A model is reported as “mean absolute error.” What does one huge outlier do to that average, and what would you report beside it?

☐  The median cannot see an extreme value. Which of today’s measures can?


## 6: Save and push


☐  git add spread.py

☐  git commit -m "U3 L05 range, variance, and standard deviation over donations"

☐  git push   →  Paste the push URL GitHub printed:


## 7: Turn in


☐  Post a screenshot of the push confirmation line to the Classroom assignment.

☐  Put these four numbers in the push message:

1.  Mean of all 200:

2.  Standard deviation of all 200:

3.  Standard deviation with the outlier removed:

4.  Percentage of clean values within one standard deviation of the mean:

☐  Keep the terminal open for a spot-check. Due 11:59 PM tonight.
