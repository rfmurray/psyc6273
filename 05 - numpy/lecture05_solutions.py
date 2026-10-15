# lecture05_solutions.py  Solutions to lecture 5 workshop problems

# Solve the following problems using the numpy module.

# 1. Create a 2D array of zeros, of size (10,20).

import numpy as np
x = np.zeros(shape=(10,20))

# 2. Create a 2D array of size (5,10), where every entry is 100.

x = np.full(shape=(10,20), fill_value=100)

# 3. Create a 2D array of random integers between 1 and 10, of size (5,5).
# hint: read the help for np.random.randint()

x = np.random.randint(low=1, high=11, size=(5,5))

# 4. Repeat problem 3, but this time specify that the values in the array
# should be of type np.int8.

x = np.random.randint(low=1, high=11, size=(5,5), dtype=np.int8)

# 5. Repeat problem 3, but this time make the array size (m,n),
# where m and n are themselves random integers between 1 and 10. That is,
# every time you create the array, it has a randomly generated size.

m = np.random.randint(low=1, high=11)
n = np.random.randint(low=1, high=11)
# or, in a single line:
m, n = np.random.randint(low=1, high=11, size=(2,))

x = np.random.randint(low=1, high=11, size=(m,n))

# 6. (a) Create a 2D array x of normally distributed random numbers, with
# mean zero and standard deviation one. Make the array size (9,9).

x = np.random.normal(size=(9,9))

# (b) Create a 2D array y that is the central 3 x 3 square
# of the array x that you created in part (a).
# hint: Use the slice operations we covered in the lecture,
# e.g., something like y = x[0:1,0:1]

y = x[3:6,3:6]

# 7. Create a 3 x 4 numpy array of random numbers from the standard
# normal distribution. Set all values less than -2 to -2, and all values
# greater than -2 to 2.

r = np.random.normal(size=(3,4))
r[r<-2] = -2
r[r>2] = 2
