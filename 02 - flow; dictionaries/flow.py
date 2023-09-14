# flow.py  Flow control: conditionals and loops

# 1. if-elif-else

x = 3

if x==1:
    print('first case')

elif x==2:
    print('second case')

elif x==3:
    print('third case')

else:
    print('other case')
    print(x)

# can have one 'if' clause, then zero or more 'elif' clauses, then zero or
# one 'else' clauses

# statements with the same level of indentation are grouped together
# under the if, else, or elif clause. note that you can't mix spaces
# and tabs for indentation.


# boolean expressions

import random
x = random.random()  # uniform random number generator on interval [0,1)
print(x)
if x > 0.1 and not x > 0.9:
    print('not too extreme')

# logical operators: and, or, not
# 
# arithmetic operators: >, <, >=, <=, ==, !=
# 
# grouping for order of operations: ( )

x = random.random()
print(x)
if x > 0.1 and not ( x >= 0.4 and x <= 0.6 ):
    print('in the required range')


# 2. for loop

for x in [1, 2, 3]:    # iterate over a list
    print(x)

for x in (1, 2, 3):    # iterate over a tuple
    print(x)

expt = dict(subject='jfk', date='14-jan-1960', condition='valid')
for k in expt:         # iterate over keys in a dictionary
    print(k, expt[k])

for x in range(10):    # iterate over a range of numbers (0...9)
    print(x)

v = ('a', 'b', 'c', 'd', 'e')
for i, x in enumerate(v):    # iterate over a tuple, but provide
    print(i, x)              # an index variable as well

# in python terminology, all these things that we can put at the end of
# a for statement (list, tuple, dictionary, range(), enumerate(), etc.)
# are examples of "iterables", i.e., things we can iterate over.


# 3. while loop

# get a sample from a limited range of the normal distribution
x = -10
while x < -2 or x > 2:
    x = random.gauss(0,1)

print(x)

# alternative approach, using the break statement
while True:
    x = random.gauss(0,1)
    if x > -2 and x < 2:
        break

print(x)

# alternative approach, using the continue statement

while True:
    x = random.gauss(0,1)
    if x<= -2 or x >= 2:
        continue
    
    # can have additional processing here, e.g., check whether x passes
    # an additional test
    y = x ** 2 + 1
    if y > 2:
        break

print(x, y)


# we use a for loop when we know at the outset how many times we'll
# need to go through the loop. for example, we usually know the number
# of trials we'll run in an experiment.
# 
# we use a while loop when we'll know when we're done with a loop, but
# not necessarily how many times it will take. for example, a participant
# in an experiment may press several keys before they press a key that
# is an allowed response.


# 4. list comprehension

import math

x = [i for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) if math.sin(i)>0]
x = [i for i in range(100) if math.sin(i)>0]
x = [i for i in range(100)]
x = [i**2 for i in range(100) if math.sin(i)>0]
x = [i**2 for i in range(10)]

# we can select elements of one list, based on the values of elements of
# another list. you'll use this feature in problem set 1.
x = [ random.gauss(0,1) for i in range(100) ]
y = [ random.gauss(0,1) for i in range(100) ]
z = [ x[i] for i in range(100) if y[i]>0 ]


# 5. an example that uses several topics from this lecture: the bubblesort algorithm

# get a list of random numbers
import random
x = [random.random() for i in range(20)]  # use a list comprehension
print(x)

# loop until list is sorted
keep_sorting = True
while keep_sorting:   # not sure how many iterations, so we use a while loop
    
    # step through elements of list    
    keep_sorting = False;
    for i in range(len(x)-1):   # here we know how many iterations, so we use
                                # a for loop. note that we can put loops
                                # within loops.
        
        # are these two elements in the wrong order?
        if x[i] > x[i+1]:       # use an if statement to check a condition.
                                # note that we can put an if statement
                                # within a loop.
            
            # switch order of two elements
            tmp = x[i]
            x[i] = x[i+1]      # everything indented by the same amount is
            x[i+1] = tmp       # part of the if clause
            
            # shortcut
            # x[i], x[i+1] = x[i+1], x[i]

            # record that not all elements were in order            
            keep_sorting = True

# show sorted list
print(x)

