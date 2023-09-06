# lists.py  Lists and tuples

# 1. Variables and basic mathematical operations

x = 3.0
y = 4.0

z = x + y
z = x - y
z = x * y
z = x / y
z = x ** y
z = ( x + y ) * y

import math

z = math.sin(x)
z = math.pi
z = math.log(x)
z = math.exp(x)

# 2. Data types

# float
x = 3.1415
type(x)
y = 0.0
type(y)

# int
y = 0
type(y)

# bool
x = True
type(x)
y = False
type(y)

# complex
x = 1 + 2j
type(x)

# Containers are objects that can contain other objects. Examples
# include sequences (e.g., lists), mappings (e.g., dictionaries),
# and sets.
# 
# A sequence has numbered elements, starting with zero. Lists, tuples,
# and strings are all examples of sequences.

# 3. Common sequence operations

# - index

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # a list

x[0]   # elements are numbered starting at zero
x[1]
x[-1]  # negative integers count backwards from end of sequence
x[-5]

s = 'the quick brown fox'  # a string

s[0]
s[1]
s[-1]
s[-5]

# - slice

x[0:3]  # first index is inclusive, second is exclusive
x[2:4]

# omitted indices default to beginning or end of sequence
x[:3]
x[5:]
x[:]

# negative indices count back from end of sequence
x[4:-3]
x[-3:-1]
x[-3:0]  # result is empty when first index is after second index
x[-3:]
x[:-4]

# step size

x[0:10:2]
x[::2]
x[8:3:-1]   # negative step sizes go backwards through the sequence;
x[0:10:-2]  # with a negative step size, second index should be lower
            # than first
x[::-2]
x[5::-2]
x[:5:-2]

# Why is the first index inclusive, and the second index exclusive?
# I don't think there's any really good motivation for this. Two attempts
# at answers that people sometimes give:
# 
#   (1) x equals x[:5] + x[5:]
#   (2) len( x(2:5) ) is 5-2 = 3
# 
# Probably the real answer is that Python's indexing system is a
# byproduct of the fact that the most common version of Python 
# (i.e., CPython) is implemented in C language, where this kind of
# inclusive-exclusive indexing does make sense.

# - addition and multiplication

a = [1, 2, 3] + [4, 5, 6]  # concatenates sequences of the same type
b = 3 * [1, 2, 3]
c = 4 * [None]

# - membership

64 in [32, 64, 128, 256]  # True
65 in [32, 64, 128, 256]  # False

'ct' in 'cacti'  # for strings, 'in' checks for a substring

# - length, minimum, and maximum

min(x)
max(x)
len(x)

max(2, 3, 4)  # can pass multiple arguments instead of a sequence
min(2, 3, 4)

# 4. Lists

# - lists are one kind of sequence (as we saw above)
# - lists are mutable; you can change their contents
# - you can use all the above sequence operations on lists
# - lists also have their own specific methods
# - list(x) makes copies of elements in list x (or sequence x?)

# - item assignment

x = [1, 2, 3]
x[1] = 5
x[10] = 5  # error; can't assign to a position that doesn't exist

# small detour: value and reference

x = [1, 2, 3]
y = x      # y is assigned by reference, not by value
x[0] = 10
x
y          # so if we change x, then we change y as well

y[0] = 1000
x          # and we if change y, we change x as well
y

x = [100, 200, 300]  # here we reassign x, but not y
x
y                      # so y retains its previous value

# slicing returns a copy, not the original sequence
# i.e., y is assigned by value, not reference
y = x[0:3]
y[0] = 10
x
y
x[:]  # returns the whole sequence, but a copy, not the original

# - assigning to slices

x[0:3] = [1, 2, 3]
x[0:3] = [1, 2, 3, 4, 5]  # can change number of elements
x[1:1] = [20, 20, 20]     # can insert elements

# - deleting elements and slices; also see remove() and pop() methods below

del x[3]
del x[3:5]

x[3:5] = []

# - list methods

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # a list

# adding elements
x.append(11)              # appends value; changes x in place
x.extend([100, 200, 300]) # appends multiple values
x.insert(5,100)           # inserts 100 as element 5

# removing elements
x.remove(5)   # removes first occurrence of 5 from x; error if not present
y = x.pop()   # returns last element of x, and removes it from x
y = x.pop(5)  # returns element 5 of x, and removes it from x

              # x.append(y) and x.pop() give a stack; 
              # x.append(y) and x.pop(0) give a queue

x.clear()     # x is changed to []; similar to x[:] = [] ( vs. x = [] )
              # (Q: what if we do these various operations after y = x? what happens to x?)

# finding elements
x.index(5)    # returns index of first instance of 5; error if not present
x.count(5)    # counts occurrences of 5
y = x.copy()  # make a separate copy; similar to y = x[:], y = list(x)

# reordering elements
x.sort()        # sorts list in place
y = sorted(x)   # returns a sorted copy of x, and leaves x unchanged

# 3. Tuples

# - tuples are another kind of sequence
# - tuples are immutable; you can't change their contents

x = (1, 2, 3)
x = 1, 2, 3           # parentheses are optional
x = ()                # empty tuple
x = tuple([1, 2, 3])  # tuple() is a type, not a function
x = tuple('abc')
x = tuple()           # empty tuple

# we can use all the sequence operations from section 1 above on tuples

x[1]        # can use indices
x[1:3]      # can use slices; result is a tuple

x = 42,             # single element; same as x = (42,);
                    # different from x = 42 and x = (42)
x = 3 * ( 40 + 2 )  # compare
x = 3 * ( 40 + 2, )

# but we can't do list-specific operations on tuples

x[0] = 10    # error
x.append(5)  # error

