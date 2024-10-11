# lecture06_solutions.py  Solutions to lecture 6 workshop problems

# 1. Use the numpy module to create a text file with ten lines. Each line
# is a comma-separated list of random numbers with mean zero and standard
# deviation one, shown to three decimal places.

import numpy as np
x = np.random.normal(loc=0, scale=1, size=(10,10))
np.savetxt('random.txt', x, fmt='%.3f', delimiter=',')

# 2. Create a 3 x 4 numpy array of random numbers from the standard
# normal distribution. Set all values less than -2 to -2, and all values
# greater than -2 to 2.

r = np.random.normal(size=(3,4))
r[r<-2] = -2
r[r>2] = 2

# 3. Create a dictionary with keys x, y, and z. The value for each entry
# is a 3 x 4 numpy array of random numbers from the standard normal
# distribution. Change the current working to your desktop, and save this
# dictionary in a pickle file called xyz.pkl.

d = { 'x' : np.random.normal(size=(3,4)),
      'y' : np.random.normal(size=(3,4)),
      'z' : np.random.normal(size=(3,4)) }

import os, pickle

os.chdir('/Users/rfm/Desktop')  # use the path to your desktop here

with open('xyz.pkl', 'wb') as f:
    pickle.dump(d, f)

# 4. From the pickle file you created in the previous problem, load the
# dictionary into a variable called 'data'.

with open('xyz.pkl', 'rb') as f:
    data = pickle.load(f)

# 5. Use numpy operations to create a 256 x 256 image of a dot with
# radius 32 pixels. Show the image in a matplotlib window.

# create coordinate matrices
n = 128
midn = np.floor(n/2)
xy = np.arange(-midn, midn)
xmat, ymat = np.meshgrid(xy, -xy)

# create matrix with distance from origin
dmat = np.sqrt(xmat**2 + ymat**2)

# create dot image; approach 1
radius = 32
im = np.zeros(shape=dmat.shape)
im[dmat<=32] = 1

# create dot image; approach 2
im = int(dmat<=32) 

# show the dot image
import matplotlib.pyplot as plt
plt.imshow(im, cmap='gray')
plt.show()
