# numpy_concat.py  Combining numpy arrays into larger arrays

import numpy as np

# make some 2D arrays
x = np.zeros((3,4))
y = np.ones((3,4))

# combine 2D arrays
np.hstack((x,y))  # horizontally
np.vstack((x,y))  # vertically
np.dstack((x,y))  # in depth

# as above, but specify the axis in an argument
np.concatenate((x,y), axis=0)  # combine along an existing axis
np.concatenate((x,y), axis=1)
np.stack((x,y), axis=2)        # combine along a new axis

# make some 1D arrays
u = np.zeros(4)
v = np.ones(4)

# combine 1D arrays
np.vstack((u,v))         # vertically, as rows
np.hstack((u,v))         # horizontally, as rows (result is 1D)
np.column_stack((u,v))   # horizontally, as columns
