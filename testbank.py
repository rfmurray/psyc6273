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

