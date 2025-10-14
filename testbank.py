# testbank.py  Test bank for biweekly quizzes

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
# - integer, float, Boolean, NoneType

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

# use a for loop to print the integers from 0 to 19
for x in range(20):
    print(x)

# use a while loop to get a sample from the normal distribution
# with mean 0 and standard deviation 1, but ensure that the
# sample has a value between -2 and 2
import random
while True:
    x = random.gauss(0, 1)
    if x>=-2 and x<=2:
        break

# use psychopy to create a mouse object
from psychopy import event
mouse = event.Mouse()

# read the current mouse position from a mouse object
x, y = mouse.getPos()

# use psychopy to create a keyboard object
from psychopy.hardware import keyboard
kb = keyboard.Keyboard()

# check what keyboard keys have been pressed
keys = kb.getKeys(waitRelease=False)

# use an f-string to report the value of math.pi to four decimal places
import math
print(f'The approximate value of pi is {math.pi:.4f}.')

# use zip() to print pairs of corresponding values from the lists [1,2,3] and ['a','b','c']
list1 = [1,2,3]
list2 = ['a','b','c']
for v1, v2 in zip(list1, list2):
    print(v1, v2)

# get a sample from a Bernoulli random variable with probability of success 0.75
import random
b = int(random.uniform(0,1) < 0.75)

# Create a 5 x 3 numpy array called z, filled with zeros.
z = np.zeros(shape=(5,3))

# Create a 4 x 5 numpy array called z, filled with samples from
# the standard normal distribution (i.e., mean=0, standard deviation=1).
z = np.random.normal(loc=0.0, scale=1.0, size=(4,5))

# Create a 1D numpy array that contains the numbers 10, 20, 30.
z = np.array([ 10, 20, 30 ])

# Create a numpy array called z, that contains 10 samples, evenly spaced
# between 20 and 50.
z = np.linspace(start=20, stop=50, num=10)

# Find the shape of the numpy array z.
z.shape

# Create a function called 'addit' that takes two arguments, a and b, and
# returns their sum. Give argument b a default value of 10.
def addit(a, b=10):
    return a+b

# Use a list comprehension to a list of the squares of integers from 0 to 9
[x**2 for x in range(10)]

# Suppose x and y are 1D numpy arrays of the same size. Use matplotlib.pyplot
# to plot y against x, using a red line to connect the data points.
import matplotlib.pyplot as plt
plt.plot(x, y, 'r-')
plt.show()
