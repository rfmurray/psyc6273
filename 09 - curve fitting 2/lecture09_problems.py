# lecture09_problems.py  Lecture 9 workshop problems

# 1. Revise your solution to problem 2 in the posted problems for lecture 7.
# Allow the function bsort to take an additional, optional input argument called
# 'key'. Assign key a default value of None. Revise the function bsort so that it
# uses the key argument like the sort() function for built-in lists, as
# illustrated in lecture 7 in functions.py. That is, if the user passes an
# argument key=f, then the list is sorted based on whether f(x[i]) > f(x[i+1]),
# instead of whether x[i] > x[i+1].

# 2. Create a list of ten 3-tuples using your solution to lecture 7's problem 1.
# Use your solution to problem 1 (in this problem set) to sort this list, based
# on the sum of the numbers in each 3-tuple. That is, the 3-tuple with the lowest
# sum comes first, and the 3-tuple with the highest sum comes last. (Hint: the
# function sum() returns the sum of the elements in a tuple.)

# 3. If you solved problem 3 for lecture 7 using the function optimize.curve_fit()
# that we covered in that lecture, which does least-square curve fitting, then
# write a new solution that uses the function optimize.minimize() that we covered in
# this lecture. To do this, you will need to write your own error function that
# calculates the sum-of-squares error. If you solve the problem this way, your
# solution is more flexible, as you can change the error function so that it
# uses an error measure other than the sum-of-squares error.

