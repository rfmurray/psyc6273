# chapter03_solutions.py

# 1. Does a while loop run its indented code at least once, even if the
# test condition is false? Write a script that you can run to answer this
# question.

x = -1
while x > 0:
    print('making a pass through the loop')

# Here we see that the message is never printed. So when the test
# condition is false, the while loop does not run the indented code
# even once.

# 2. Write a for loop that creates a list that contains the integers
# from 0 to 19.

x = []
for i in range(20):
    x.append(i)

# 3. We illustrated the continue and break statements with a while loop.
# Write a script to test whether they can be used with a for loop as well.

for i in range(20):
    if i <= 10:
        continue
    print(i)
    if i >= 15:
        break

# This code prints the numbers 11 to 15, which shows that continue
# and break statements work in a for loop. The values 1 to 10 are
# not printed because of the continue statement, and values higher
# than 15 are not printed because of the break statement.

# 4. When we generated 100 random numbers, omitting outliers, we used
# a while loop. Why was this a better choice than a for loop?

# A while loop was more appropriate, because there is no fixed number
# of passes through the loop that will be needed to get the required
# list of random numbers. The number of passes will change from one run
# to another, depending on the specific random numbers that we get, and
# how many outliers need to be rejected.

# 5. Cohen’s d is a statistic that describes the effect size in a
# statistical analysis. The standard interpretation is that a value of d
# up to 0.2 is a small effect size, a value between 0.2 and 0.5 is a medium
# effect size, and a value larger than 0.5 is a large effect size. Write a
# script that assigns a random value between 0 and 1 to the variable d, and
# then prints the message 'small effect size', 'medium effect size', or
# 'large effect size' depending on the value of d.

import random
d = random.uniform(0, 1)

if d <= 0.2:
    print('small effect size')
elif d < 0.5:
    print('medium effect size')
else:
    print('large effect size')

# 6. The os module provides many functions related to your computer’s
# operating system. Investigate them as follows.
# 
# (a) Import the os module and read the help text for the functions
# os.getcwd(), os.chdir(), and os.listdir().

import os
help(os.getcwd)
help(os.chdir)
help(os.listdir)

# (b) Use os.getcwd() to find the current working directory at your Python
# console. It’s probably someplace where you don’t want to save your own files.

os.getcwd()

# In my case, running PsychoPy in macOS, the return value is
# '/Applications/PsychoPy.app/Contents/Resources'.

# (c) Use os.chdir() to change the directory to someplace on your computer
# where you would normally save a file.

os.chdir('/Users/rfm/Desktop')

# (d) Use os.listdir() to list the contents of your current working directory.

os.listdir()

# This provides a list of strings, where each string is the name of a
# file in /Users/rfm/Desktop.

# 7. In the bubblesort algorithm, why is len(x)-1 the value that we pass to
# range()?

# The list x contains len(x) elements. We want to compare elements 0 and 1,
# then elements 1 and 2, and so on up to the last pair, which is
# elements len(x)-2 and len(x)-1. Thus we want the loop variable, which
# indexes the first element of each pair, to range from 0 to len(x)-2.
# If we use range(n), then the loop variable ranges from 0 to n-1.
# So in our case we need to use range(len(x)-1).

# 8. Suppose you run a attentional experiment where one factor is the validity
# of the cue, which can be valid, invalid, or neutral, and another factor
# is the brightness of the stimulus, which can be bright or dark.
# In a crossed experimental design, all possible combinations of the two
# factors are included in the experiment. Write two nested for loops that
# create a list with all possible combinations of the two factors,
# i.e., [['valid', 'dark'], ['valid', 'bright'], ['invalid', 'dark'],
# ['invalid', 'bright'], ['neutral', 'dark'], ['neutral', 'bright']].
# Hint: assign the empty list to a variable called conditions. Make the
# outer loop step through the three values of the first factor, and make
# the inner loop step through the two values of the second factor. On each
# pass through the inner loop, append a list containing the two loop
# variables to conditions.
 
conditions = []
for c1 in ['valid', 'invalid', 'neutral']:
    for c2 in ['dark', 'bright']:
        conditions.append([c1, c2])

print(conditions)
