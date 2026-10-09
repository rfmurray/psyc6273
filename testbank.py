# testbank.py  Test bank for biweekly tests

# calculate 2 to the power of 8 in two different ways
pow(2, 8)
2 ** 8

# calculate the absolute value of the variable x
abs(x)

# print the message "Press any key to begin" to the console
print('Press any key to begin')

# check the data type of the variable x
type(x)

# name four basic data types in Python that store one unit
# of information, such as a number
# 
# A: integer, float, Boolean, NoneType

# create a list called x with the elements 10, 20, and 30
x = [10, 20, 30]

# create a list called x with four sublists, each of which
# contains two integers
x = [[50, -10], [50, -15], [52, -18], [55, -20]]

# find the length of the list x
len(x)

# assign the second element of x to a variable a
a = x[1]

# change the second element of x to 20
x[1] = 20

# add a new integer to the end of list x
x.append(50)

# extend the list x with a new list [1, 2, 3]
x.extend([1, 2, 3])

# define a new list y that contains elements 2 to 5 of list x,
# with numbering starting at zero
y = x[2:6]  # note that the number 6 is not a typo

# convert a list x to to a tuple, and then back to a list
x = tuple(x)
x = list(x)

# create a string called s
s = 'Use the mouse to move the white plus sign on the screen.'

# convert the string s to uppercase and lowercase
s_upper = s.upper()
s_lower = s.lower()

# replace the word "mouse" with "trackpad" in the string s
s = s.replace('mouse', 'trackpad')

# count the number of occurrences of the lowercase letter 'e' in string s
s.count('e')

# define a string variable s by concatenating two strings
s = 'abc' + 'def'

# write code that creates an empty list and then uses a for loop to
# append the integers from 0 to 19 to the list
x = []
for k in range(20):
    x.append(k)

# use a while loop to find the first integer whose cube is
# greater than 10000
i = 0
while i**3 <= 10000:
    i = i + 1

print(i)

# write code that prints the word ‘negative’ if a variable x is less
# than zero, prints ‘zero’ if x equals zero, and prints ‘positive’ otherwise
if x<0:
    print('negative')
elif x==0:
    print('zero')
else:
    print('positive')
    
# import the math module and assign the logarithm of 100 to variable x
import math
x = math.log(100)

# import the random module and assign a sample from the standard
# normal distribution (mean=0, std=1) to the variable x
import random
x = random.gauss(0, 1)

# open a new psychopy window
from psychopy import visual
win = visual.Window()

# create a psychopy keyboard object
from psychopy.hardware import keyboard
kb = keyboard.Keyboard()

# create a psychopy mouse object
from psychopy import event
mouse = event.Mouse()

# create a psychopy clock object
from psychopy import core
timer = core.Clock()

# create a 4 x 5 numpy array filled with zeros
import numpy as np
x = np.zeros(shape=(3,4))

# create a 4 x 5 numpy array filled with samples from the normal distribution
# with mean zero and standard deviation one
import numpy as np
x = np.random.normal(loc=0.0, scale=1.0, size=(4,4))
