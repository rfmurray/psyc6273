# lecture07_solutions1.py  Solutions to lecture 7 workshop problems, part one

# Some problems will require tools from earlier lectures, such as lists and
# loops. This will be the case in workshop problems from now on.

# 1. Define a function randt(n, u, v) that returns an n-tuple of random
# floating point numbers between u and v. Give u a default value of 0,
# and v a default value of 1. (Hint: you could first create a list,
# using a for loop or a list comprehension, and then convert it to a tuple
# using tuple().)

import random

def randt(n, u=0, v=1):
    x = [ random.uniform(u,v) for i in range(n) ]
    return tuple(x)

# 2. Create a function bsort(x) that uses the bubblesort algorithm from
# lecture 2 to sort a list x. You can just copy and paste the code from
# the readings for lecture 2 into the function.

def bsort(x):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                sorted = False

# test it
x = [ random.uniform(0,1) for i in range(10) ]
bsort(x)
