# functions.py  Functions

# abstraction = saying what you will do, without giving the details of exactly
# how you will do it
# 
# - a function is called at some locations in the code, and the implementation
#   is specified elsewhere
# - this approach can make programs easier to write and to understand


# functions

def addit(a, b):
    c = a + b
    return c

addit(10, 20)

# can also do a calculation in the return statement

def addit(a, b):
    return a + b

addit(10, 20)

# can call functions using named arguments; then the order doesn't matter

addit(a=10, b=20)
addit(b=20, a=10)

# can set default values for some or all arguments
# - arguments without default values must come first

def addit(a, b=2):
    return a + b

addit(10)
addit(10,20)
addit(a=10)
addit(a=10,b=20)

# can read variables defined outside the function

x = 1
def addit(a):
    return a + x

# to change the value of variable defined outside the function, we need to
# declare it as global variable

x = 1
def addit(a):
    x += 1  # error; because we're changing x, python looks for a local variable
    return a + x

x = 1
def addit(a):
    global x
    x += 1
    return a + x

# documenting a function: docstrings and help

def addit(a, b=2):
    'returns the sum of two input arguments'
    return a + b

help(addit)

# reminder: strings with triple quotes can extend over several lines

s = """this is an illustration
of how to use triple quotes
to allow strings to extend over
multiple lines"""

print(s)

# triple-quoted strings are useful for giving extensive information about
# a function in a docstring

def addit(a, b=2):
    """returns the sum of two input arguments
    
addit(a, b=2)

This function is just for illustration."""
    return a + b

help(addit)

# lambda functions are simple one-line functions

f = lambda z : z**2

f(10)

# a function is stored in a variable, like any other value. this means we can
# pass functions as arguments to other functions.

# make a list of tuples of random numbers
import random
ulist = [ random.uniform(0,1) for i in range(10) ]
x = [ (u,random.uniform(u,1)) for u in ulist ]

# sort a list of tuples based on the second element in each tuple
def f(z):
    return z[1]
x.sort(key=f)    # we can sort a list based on any property we can define

# do the same thing with a lambda function
f = lambda z : z[1]
x.sort(key=f)

# do the same thing passing the lambda function directly as an argument
x.sort(key = lambda z : z[1])

