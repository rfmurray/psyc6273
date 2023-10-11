# testbank.py  Test bank for biweekly quizzes

# 1. Create a list x that contains the numbers 1 to 10.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Set a variable y equal to the following elements or sublists of x. Where
# possible, write your code so that it works for any length of x, e.g., it still
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

# 5. Use a list comprehension to create a list that contains the
# squares of the integers 1 to 20.

x = [ i**2 for i in range(1,21) ]

# 6. Use a list comprehension to make a list of 200 simulated reaction
# times. Make the reaction times normally distributed, with a mean of
# 0.75 and a standard deviation of 0.25.

import random
rt = [ random.gauss(mu=0.75, sigma=0.25) for i in range(200) ]

# 7. Create a list with 100 elements. Each element of the list is a tuple
# with two elements. The first element of each tuple is a random number
# from the interval [0,1). The second element of each tuple is a random
# number drawn from the interval [0,1), with the constraint that the second
# element is greater than the first element.

import random
ulist = [ random.uniform(0,1) for i in range(100) ]
x = [ (u,random.uniform(u,1)) for u in ulist ]

# 8. Define a function randt(n, u, v) that returns an n-tuple of random
# floating point numbers between u and v. Give u a default value of 0,
# and v a default value of 1.

import random

def randt(n, u=0, v=1):
    x = [ random.uniform(u,v) for i in range(n) ]
    return tuple(x)

