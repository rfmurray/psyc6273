# workshop1answers.py Lecture 1 workshop problems, with solutions

# Add code below the following comments, to solve the stated problems.

# 1. Create a list x that contains the numbers 1 to 10.
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 2. Set a variable y equal to the following sublists of x. Where possible,
# write your code so that it works for any length of x, e.g., it still
# works if x has 20 elements rather than 10.

# 2a. the first element of x
y = x[0]

# 2b. the first five elements of x
y = x[:5]

# 2c. the last element of x
y = x[-1]

# 2d. the last five elements of x
y = x[-5:]

# 2e. every second element of x, starting with the first element
y = x[::2]

# 2f. every third element of x, starting with the second element
y = x[1::3]

# 2g. all the elements of x, in reverse order
y = x[::-1]

# 2h. every second element of x, counting back from the last element
y = x[::-2]

# 2i. the first three elements of x and the last three elements of x
y = x[:3] + x[-3:]

# 2j. the first five elements of x, repeated ten times, i.e., the list
#    [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ... ], with ten repetitions
y = 10 * x[:5]

# 2k. the largest element of x, repeated five times
y = 5 * [ max(x) ]

# 2l. the smallest element of x, repeated a number of times equal to
#     the largest element of x
y = max(x) * [ min(x) ]

