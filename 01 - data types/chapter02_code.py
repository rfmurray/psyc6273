# chapter02_code.py  Data types and structures

# 2.2 Variables

# define a variable
x = 5

# see the value of a variable by typing its name at the command line
x

# define a variable with a descriptive name
dot_radius = 1.5

# try to see the value of a variable that hasn't been defined;
# this line creates an error
reaction_time

# arithmetic operations
#   addition        +
#   subtraction     -
#   multiplication  *
#   division        /
#   exponentiation  **
#   order of operations  ( )
(1/2) - (3+4)**2

# define variables with arithmetic operations
dot_radius = 1.5
dot_circumference = 2 * 3.1416 * 1.5
dot_area = 3.1416 * (1.5 ** 2)

# use one variable in the definition of other variables
dot_radius = 1.5
dot_circumference = 2 * 3.1416 * dot_radius
dot_area = 3.1416 * (dot_radius ** 2)

# 2.3 Functions

# call the absolute value function
u = abs(-10.5)

# call the power function
v = pow(2, 3)

# call the print function
print('Hello, world!')

# 2.4 Data types

# check the type of a variable
x = 5
type(x)

# check the type of another variable
y = 5.43
type(y)

# automatic selection of data types
z = (1/2) - (3+4)**2
type(z)

# the Boolean data type
b = True

# the Boolean data type, again
x = 5
b = x < 0
type(b)

# NoneType
response = None
print(response)
type(response)

# 2.5 Lists

# create a list
dot_position = [10, 20]
type(dot_position)

# more lists
some_properties = [1.5, 2, True, None, 10]
square_circles = []
trajectory = [[50, -10], [50, -15], [52, -18], [55, -20]]

# find the length of a list
n = len(trajectory)

# create a list from other variables
x = 10
y = 20
p = [x, y]

# indexing
dot_position[0]
trajectory[0]
trajectory[0][0]
trajectory[0][1]

# change an element of a list
dot_position[1] = 5

# a list method: append()
dot_position = [10, 20]
dot_position.append(30)

# another list method: extend()
primes = [2, 3, 5, 7]
primes.extend([11, 13, 17])

# compare append() and extend()

test1 = [1, 2, 3]
test1.append([4, 5, 6])
print(test1)

test2 = [1, 2, 3]
test2.extend([4, 5, 6])
print(test2)

# a mistake; remember that append() changes a list in place
list1 = [10, 20, 30]
list2 = list1.append(40)
print(list2)

# 2.6 Tuples

# create a tuple
dot_position = (10, 20)
dot_position = 10, 20
type(dot_position)

# more tuples
some_properties = (10, 20.5, True, (1, 2), [3, 4])
no_properties = ()

# index a tuple
some_properties[1]

# tuples are immutable; this generates an error
some_properties[0] = 50

# can convert a tuple to a list
x = 1, 2, 3
y = list(x)
type(y)

# can convert a list to a tuple
x = [1, 2, 3]
y = tuple(x)
type(y)

# 2.7 Strings

# create a string
instruction1 = 'Use the mouse to move the white plus sign on the screen.'
instruction2 = "Track the moving red dot as closely as you can."
type(instruction1)

# strings are immutable; generates an error
instruction1[0] = 'A'

# string methods

name = 'Target Dot'
name.upper()
name.lower()
name.replace('Target', 'Red')
name.count('D')

# 2.8 Sequences

# len() works with all kinds of sequences

x = 1, 2, 3
len(x)

instruction3 = 'The experiment is about to begin.'
len(instruction3)

# adding sequences concatenates them

x = [1, 2, 3]
y = [4, 5, 6]
z = x + y

prime1 = (2, 3, 5)
prime2 = (7, 11, 13, 17)
primes = prime1 + prime2

name1 = 'Target'
name2 = 'Dot'
name3 = 'A Red ' + name1 + ' ' + name2

# extend a tuple
primes = primes + (19, 23, 29)

# extend a tuple by one integer
primes = primes + 31     # this version generates an error
primes = primes + (31,)  # this version works

# slice a sequence
primes = [2, 3, 5, 7, 11, 13, 15, 17]
primes[0:4]

# can omit endpoints in slice notation
primes[:4]
primes[4:]
primes[:]

# a single-element slice of a list is a list
primes[0] + 10    # this line works
primes[0:1] + 10  # this line generates an error

# slicing works with all kinds of sequences, including tuples and strings

squares = 1, 4, 9, 16, 25, 36, 49
squares[3:5]

instruction4 = 'The experiment is now finished.'
instruction4[22:]

