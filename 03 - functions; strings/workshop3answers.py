# workshop3.py  Lecture 3 workshop problems

# Add code below the following comments, to solve the stated problems.
# 
# Some problems will require tools from earlier lectures, such as lists and
# loops. This will be the case in workshop problems from now on.

# 1. Define a function randt(n, u, v) that returns an n-tuple of random
# floating point numbers between u and v. Give u a default value of 0,
# and v a default value of 1. (Hint: you could first create a list,
# possibly using a list comprehension, and then convert it to a tuple
# using tuple().)

import random

def randt(n, u=0, v=1):
    x = [ random.uniform(u,v) for i in range(n) ]
    return tuple(x)

# 2. Define a function randl(n, m) that returns a list with n elements,
# where each element is an m-tuple of random numbers between 0 and 1,
# created using your solution to problem 1.

def randl(n, m):
    return [ randt(m) for i in range(n) ]

# 3. Create a function bsort(x) that uses the bubblesort algorithm from
# lecture 2 to sort a list x. You can just copy and paste the code from
# lecture 2 into the function.

def bsort(x):
    # loop until list is sorted
    keep_sorting = True
    while keep_sorting:
        # step through elements of list    
        keep_sorting = False;
        for i in range(len(x)-1):
            # wrong order?
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                keep_sorting = True

# test it
x = [ random.uniform(0,1) for i in range(10) ]
bsort(x)

# 4. Revise your solution to problem 3, so that the bsort function allows
# an additional, optional input argument called 'key'. Assign key a default
# value of None. Revise the function bsort so that it uses the key argument
# like the sort() function for built-in lists, as illustrated in the lecture 3
# code in functions.py. That is, if the user passes an argument key=f, then
# the list is sorted based on whether f(x[i]) > f(x[i+1]), instead of
# whether x[i] > x[i+1].

def bsort(x, key=None):
    # loop until list is sorted
    keep_sorting = True
    while keep_sorting:
        # step through elements of list    
        keep_sorting = False;
        for i in range(len(x)-1):
            # wrong order?
            if key is None:
                flip = x[i] > x[i+1]
            else:
                flip = key(x[i]) > key(x[i+1])
            if flip:
                x[i], x[i+1] = x[i+1], x[i]
                keep_sorting = True

# test it by sorting in reverse order
x = [ random.uniform(0,1) for i in range(10) ]
f = lambda x : -x
bsort(x, key=f)

# 5. Create a list of ten 3-tuples using your solution to problem 2. Use your
# solution to problem 4 to sort this list, based on the sum of the numbers
# in each 3-tuple. That is, the 3-tuple with the lowest sum comes first, and
# the 3-tuple with the highest sum comes last. (Hint: the function sum()
# returns the sum of the elements in a tuple.)

x = randl(10, 3)
bsort(x, key=sum)

# check that the list is sorted in the order we wanted
[ sum(u) for u in x ]
