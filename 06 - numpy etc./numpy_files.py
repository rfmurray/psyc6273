
import numpy as np

# create some variables (numpy arrays)
x = np.random.normal(size=10)
y = np.random.normal(size=20)

# save a single variable to a .npy file
with open('data.npy','wb') as f:
    np.save(f,x)

# load a single variable
with open('data.npy','rb') as f:
    xx = np.load(f)

# save several variables to a .npz file
with open('data.npz','wb') as f:
    np.savez(f,var1=x,var2=y)  # keyword arguments indicate names of variables in file

# load several variables
with open('data.npz','rb') as f:
    d = np.load(f)
    xx = d['var1']  # file has to be open when we access the variable d
    yy = d['var2']
