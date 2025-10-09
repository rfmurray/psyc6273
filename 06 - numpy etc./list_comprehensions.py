# list_comprehensions.py

# make a list of strings
strlist = ['abc', 'defghi', 'jklmnop', 'qrstuvwxyz']

# we'd like to make a list that contains the lengths of these strings

# method 1: a for loop
numlist = []
for x in strlist:
    numlist.append(len(x))

# method 2: a list comprehension
numlist = [len(x) for x in strlist]

# next, make a list that contains the lengths of these strings, but only
# for the strings that are more than three characters long
numlist = [len(x) for x in strlist if len(x) > 3]

# alternatively, make a list of the strings in the original list that
# are more than three characters long
shortlist = [x for x in strlist if len(x) > 3]

# get a list of 100 samples from a Bernoulli random variable
import random
def coinflip(p=0.5):
    return int(random.uniform(0,1) < p)

[coinflip(p=0.2) for t in range(100)]

# general form: [ f(varname) for [varname] in [iterable] if [conditon] ]
# - the function f is optional
# - the condition is optional
