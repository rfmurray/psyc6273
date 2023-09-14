# workshop1answers.py Lecture 1 workshop problems, with solutions

# Add code below the following comments, to solve the stated problems.

# 1. Create a list x that contains the numbers 1 to 10.
x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 2. Set a variable y equal to the following sublists of x. Where possible,
# write your code so that it works for any length of x, e.g., it still
# works if x has 20 elements rather than 10.

# 2a. the first element of x
y = x[0]

# 2b. the first five elements of x
y = x[:5]

# 2c. the last element of x
y = x[-1]

# 2d. the last five elements of x
y = x[-5:]

# 2e. every second element of x, starting with the first element
y = x[::2]

# 2f. every third element of x, starting with the second element
y = x[1::3]

# 2g. all the elements of x, in reverse order
y = x[::-1]

# 2h. every second element of x, counting back from the last element
y = x[::-2]

# 2i. the first three elements of x and the last three elements of x
y = x[:3] + x[-3:]

# 2j. the first five elements of x, repeated ten times, i.e., the list
#    [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ... ], with ten repetitions
y = 10 * x[:5]

# 2k. the largest element of x, repeated five times
y = 5 * [ max(x) ]

# 2l. the smallest element of x, repeated a number of times equal to
#     the largest element of x
y = max(x) * [ min(x) ]

# 3. Change the list x as follows.

# 3a. set the first element to zero
x[0] = 0

# 3b. set the last three elements to zero
x[-3:] = 3 * [0]

# 3c. delete the fourth and fifth elements of x
del x[3:5]

# 3d. delete the first occurrence of the largest element of x
x.remove(max(x))

# 3e. delete the last element of x
x.pop()

# 3f. append the value 11 to the end of x
x.append(11)

# 3g. append the first three elements of x to the end of x
x.extend(x[0:3])

# 3h. sort the elements of x
x.sort()

# 4. Make y equal to the list x, in such a way that if you change an 
#    element of x, the corresponding element of y changes as well.
y = x

# 5. Make y equal to the list x, in such a way that if you change an
#    element of x, the corresponding element of y does not change.
y = x.copy()

# 6. Create a tuple z that contains the following elements.

# 6a. the number 50
z = (50,)

# 6b. the number 50, repeated three times
z = 3 * (50,)

# 6c. the numbers 1, 2, and 3, in that order, repeated five times
z = 5 * ( 1, 2, 3 )

