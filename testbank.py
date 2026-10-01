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

# Suppose x is a list. Briefly explain why x.append(10).append(20)
# does not append the numbers 10 and 20 to the end of x.
# 
# A: The append() method modifies a list in place. The call to
# x.append(10) appends 10 to x, but it returns the value None, not
# the modified list. Thus the call to append(20) tries to extend
# None, and this causes an error.

# define a new list y that contains elements 2 to 5 of list x,
# with numbering starting at zero
y = x[2:6]  # note that the number 6 is not a typo

# Suppose x is a list with 10 elements. Do x[2:] and x[2:len(x)]
# return the same elements of the list? Briefly explain why or why not.
# 
# A: Yes, they do return the same elements.
# 
# x[2:] returns elements starting with element 2 and continuing
# to the end of the list.
# 
# x[2:len(x)] is the same as x[2:10], and this returns elements 2
# through 9. Because element numbering starts with zero, element 9
# is the last element, and so again we get elements from 2 to the
# end of the list.

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
