# U3 L03 — Lab: Mean, Median, and Mode in Plain Python — Follow-Along Sheet


Name: ___________________________  Date: ____   Period: ____


Work top to bottom in your terminal. Change each ☐ to ☑ as you finish that step. Everything you record here comes off your own screen — nothing on this sheet gives you the answer, and the sheet is checked against your output, not against an answer key. Keep it on your desk all period.

## 0: Set up

☐  Open the terminal and go to the lab repo:  cd ~/compmath-u3-stats-lab

☐  Confirm where you are:  pwd   →  Path on screen:


_____________________________________________________________________


☐  Load the file into a list called donations, following the loader in PART 0 of the lab.

☐  Run it. Record what it prints:


______________________  values


## 1: The mean

☐  Build n, total, mean. Record your output:


n = ______________________


total = ______________________


mean = ______________________


☐  Compare with the paper day. Seven numbers gave a mean of 1335.71. Why is this mean so much smaller?


_____________________________________________________________________


☐  Build the clean list. Record the two means:


with the outlier ______________________


without the outlier ______________________


☐  One value out of 200 moved the mean this much. How many times bigger is the mean with it?


______________________ x


☐  Explain in one sentence, using the words sum and divide:


_____________________________________________________________________


## 2: The median

☐  Sort the data and find the middle. Is n odd or even here?


_____________________________________________________________________


☐  Record the two middle values and the median:


lower ______________________


upper ______________________


median ______________________


☐  The median here is a number no donor gave. Why is that not a problem?


_____________________________________________________________________


☐  Predict the median of the clean list first, then run it:


predicted ______________________


actual ______________________


☐  The mean moved a long way between the two lists. Write the contrast in your own words: what did the median do, and why is that the whole point?


_____________________________________________________________________


☐  Test the n % 2 branch on a 201-value list. What breaks if a median function handles only one parity?


_____________________________________________________________________


## 3: The mode

☐  Count the values. Record the three most common:


1st ______________________


2nd ______________________


3rd ______________________


☐  Record the highest frequency and the number of distinct values:


highest frequency ______________________


distinct values ______________________


☐  Does this dataset have a mode? Defend the answer — most_common always returns something, which is not the same as a mode existing:


_____________________________________________________________________


☐  When would the mode be the right answer instead? What is it actually good at describing?


_____________________________________________________________________


## 4: All three, one table

☐  Write centers.py with mean_of, median_of and mode_of, then run it. Fill in your own output:


| Set | Mean | Median |
| --- | --- | --- |
| all 200 | ________________ | ________________ |
| no outlier | ________________ | ________________ |


☐  Record: the mean fell ______________________ % and the median moved ______________________ cents.


☐  Add the parity tests at the bottom. Record both results:


5-value list ______________________


6-value list ______________________


## 5: Where each one lies

☐  Fill the table with a real example for each row, not a definition:


| Measure | What it answers | What it throws away |
| --- | --- | --- |
| Mean | ______________ | ______________ |
| Median | ______________ | ______________ |
| Mode | ______________ | ______________ |


☐  You are describing one class's test scores. Which measure do you use, and why not the other two?


_____________________________________________________________________


## 6: Save and push

☐  git add centers.py

☐  git commit -m "U3 L03 mean, median, mode functions over 200 donations"

☐  git push   →  Paste the push URL GitHub printed:


_____________________________________________________________________


## 7: Turn in

☐  Post a screenshot of the push confirmation line to the Classroom assignment.

☐  Put these three numbers in the push message:


mean of all 200 ______________________


median of all 200 ______________________


mean with the outlier removed ______________________


☐  Keep the terminal open for a spot-check. Due 11:59 PM.
