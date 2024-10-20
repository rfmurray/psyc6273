# lecture07_problems.py  Lecture 7 workshop problems

# Some problems will require tools from earlier lectures, such as lists and
# loops. This will be the case in workshop problems from now on.

# 1. Define a function randt(n, u, v) that returns an n-tuple of random
# floating point numbers between u and v. Give u a default value of 0,
# and v a default value of 1. (Hint: you could first create a list,
# using a for loop or a list comprehension, and then convert it to a tuple
# using tuple().)

# 2. Create a function bsort(x) that uses the bubblesort algorithm from
# lecture 2 to sort a list x. You can just copy and paste the code from
# the readings for lecture 2 into the function.

# 3. The Keeling curve shows the atmospheric concentration of carbon dioxide
# from 1958 to the present. This data posted on github, under topic 07, in
# the file keeling.csv. Fit a curve to a plot of the interpolated
# concentration (column 7) versus the decimal year (column 4).
# Experiment with various kinds of curves. You may find it helpful to start
# with a simple kind of curve, such as a straight line, and once you have
# that fit working, add more parameters to capture additional features of
# the data, such as nonlinearity and sinusoidal oscillation.
# 
# You'll need to examine the data file first, to see how what parameters
# to use when loading it. For example, what character indicates a comment
# line that doesn't contain data? 
# You may also need to preprocess the data file, for example by removing
# negative values that correspond to missing measuremnets.

