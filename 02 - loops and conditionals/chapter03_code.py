# chapter03_code.py  Loops and conditionals

# 3.2 Loops

# the for loop
for k in [1, 2, 3, 4]:
    print(k**2)

# another for loop
for k in [1, 2, 3, 4]:
    print('powers of', k)
    print(k**2)
    print(k**3)
    print(k**4)
print('end of routine')

# a for loop with a dummy variable
for x in [1, 2, 3]:
    print('Hello, world!')

# for loops with other kinds of sequences as iterables

for i in (10, 20, 30):
    print(i**2)

for c in 'here':
    print(c)

# the range() iterable
for u in range(100):
    print(u**2)

# the while loop
k = 1
while k**3 < 500:
    k = k + 1

# an outline of the tracking experiment

ntrials = 40
trial_duration = 10

for trial_number in range(ntrials):
    
    elapsed_time = 0
    
    while elapsed_time < trial_duration:
        # - update the position of target dot on the screen
        # - check the mouse position and update the position of
        #   the tracking cursor
        # - check the clock and get a new value for elapsed_time
        pass
        
    # save the data from this trial to a file

# 3.3 Conditionals

# the if statement
x = 2
if x < 0:
    print('x is negative')
elif x < 1:
    print('x is positive, but less than one')
elif x < 10:
    print('x is between one and ten')
else:
    print('x is ten or greater')

# more examples of if statements

if x < 0:
    print('x is negative')

if x < 0:
    print('x is negative')
elif x > 10:
    print('x is ten or greater')

if x < 0:
    print('x is negative')
else:
    print('x is non-negative')

# comparison operators
# - these operations generate Boolean values
# - normally we make them part of other statements, like if or elif,
#   instead of running them by themselves like this
x < 0     # less than
x > 0     # greater than
x <= 0    # less than or equal to
x >= 0    # greater than or equal to
x == 0    # equal to
x != 0    # not equal to

# more examples of using comparison operators

dot_radius = 5
if dot_radius > 20:
    pass

x = 1
y = 2
if x <= y:
    pass

if 20*x >= pow(y,2):
    pass

# logical operators

dot_radius = 4.2

if dot_radius > 5 and dot_radius < 10:
    print('The dot is medium-sized')

if dot_radius <= 5 or dot_radius >= 10:
    print('The dot is not medium-sized')

if not dot_radius > 0:
    print('Invalid value for dot radius')

# 3.4 Modules

# the math module

import math

x = 10 * math.cos(math.pi/4)
y = math.log(100)
r = math.sqrt(x**2 + y)

# the random module

import random

g = random.gauss(0, 1)
u = random.uniform(-5, 5)
k = random.randint(1, 10)

# 3.5 Continue and break

# generating random numbers without outliers

import random

mean = 0
std = 2.5

angles = []
while True:
    r = random.gauss(mean, std)
    if r < mean - 2*std or r > mean + 2*std:
        continue
    angles.append(r)
    if len(angles) == 100:
        break

# a simpler version of the above loop
angles = []
while len(angles) < 100:
    r = random.gauss(mean, std)
    if abs(r-mean) <= 2*std:
        angles.append(r)

# 3.6 A sorting algorithm

# sort a list
x = [1, 4, 2, 3, 8, 9, 5]
x.sort()

# bubblesort

import random

x = []
for i in range(100):
    x.append(random.randint(1,20))  # make a list of random numbers
print(x)

while True:
    
    # make a pass through the list and count the number of switches
    switches = 0
    for i in range(len(x)-1):
        
        if x[i] > x[i+1]:  # switch these two elements if necessary
            tmp = x[i]
            x[i] = x[i+1]
            x[i+1] = tmp
            switches = switches + 1
    
    if switches == 0:  # if no switches, then the list is sorted
        break

print(x)  # show the sorted list

# tuple assignment
a, b, c = (10, 20, 30)
a, b, c = 10, 20, 30
x[i], x[i+1] = x[i+1], x[i]

# incrementing a counter
switches = switches + 1
switches += 1

# more assignment operators
switches -= 5
switches *= 8
switches /= 16
switches **= 2

# a shorter bubblesort
while True:
    switches = 0
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            switches += 1
    
    if switches == 0:
        break

