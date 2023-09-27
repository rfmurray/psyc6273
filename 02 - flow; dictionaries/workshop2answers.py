# workshop2answers.py  Lecture 2 workshop problems

# Add code below the following comments, to solve the stated problems.

# 1. Use a for loop to create a list that contains the squares of the
# integers 1 to 20.

x = []
for i in range(1,21):
    x.append(i**2)


# 2. Repeat problem 1, using a while loop instead of a for loop.

x = []
i = 1
while i<=20:
    x.append(i**2)
    i += 1


# 3. Repeat problem 1, using a list comprehension instead of a for loop.

x = [ i**2 for i in range(1,21) ]


# 4. Rank the solutions in problems 1 to 3 from best to worst. Explain
# your ranking.

# The list comprehension is best, the for loop is next, and the while loop is
# worst. The list comprehension accomplishes the task in a single, easily
# understood line. The for loop is ok, since we're repeating a task a
# known number of times, but it takes several lines to do it. The while loop
# is worst, since it requires us to manage the i variable ourselves.


# 5. (a) Use a list comprehension to make a list of 200 simulated reaction
# times in a perceptual experiment. Make the reaction times normally distributed,
# with a mean of 0.75 and a standard deviation of 0.25.
# (b) Count the number of reaction times less than 0.25.
# (c) Count the number of reaction times less than 0.25 or greater than 1.25.

# (a)
import random
rt = [ random.gauss(mu=0.75, sigma=0.25) for i in range(200) ]

# (b)
n1 = len([ x for x in rt if x<0.25 ])

# (c)
n2 = len([ x for x in rt if x<0.25 or x>1.25 ])


# 6. Create a list with 100 elements. Each element of the list is a tuple
# with two elements. The first element of each tuple is a random number
# from the interval [0,1). The second element of each tuple is a random
# number drawn from the interval [0,1), with the constraint that the second
# element is greater than the first element. (So actually the second element
# is a sample from [x,1), where x is the first element.)

# There are many ways of doing this.

# One straightforward approach is to use a for loop.

import random

x = []
for i in range(100):
    u = random.uniform(0,1)
    v = random.uniform(u,1)
    x.append((u,v))

# To be more concise, we can use a list comprehension to generate the first
# elements of the tuples, and another list comprehension to generate the
# full list of tuples.

ulist = [ random.uniform(0,1) for i in range(100) ]
x = [ (u,random.uniform(u,1)) for u in ulist ]

# Or even more concisely, but with some loss of readability, we can combine
# the previous two lines into a single line.


