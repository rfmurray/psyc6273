# testbank.py  Test bank for biweekly quizzes

# 1. Create a list x that contains the numbers 1 to 10.
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 2. Set a variable y equal to the following sublists of x. Where possible,
# write your code so that it works for any length of x, e.g., it still
# works if x has 20 elements rather than 10.

# the first five elements of x
y = x[:5]

# the last element of x
y = x[-1]

# every second element of x, starting with the first element
y = x[::2]

# every third element of x, starting with the second element
y = x[1::3]

# the first three elements of x and the last three elements of x
y = x[:3] + x[-3:]

# the first five elements of x, repeated ten times, i.e., the list
# [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ... ], with ten repetitions
y = 10 * x[:5]

# the smallest element of x, repeated a number of times equal to
# the largest element of x
y = max(x) * [ min(x) ]

# 3. Change the list x as follows.

# set the first element to zero
x[0] = 0

# delete the fourth and fifth elements of x
del x[3:5]

# delete the first occurrence of the largest element of x
x.remove(max(x))

# append the value 11 to the end of x
x.append(11)

# append the first three elements of x to the end of x
x.extend(x[0:3])

# sort the elements of x
x.sort()

# 4. Create a tuple z that contains the numbers 1, 2, and 3,
# in that order, repeated five times.

z = 5 * ( 1, 2, 3 )

