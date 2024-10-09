# files.py  Saving and loading variables to and from disk files

# method 1: pickle

import pickle

# create some variables
# - here we're using dictionaries, but the variables could be integers,
#   strings, numpy arrays, etc.
dict1 = { 'a' : 1, 'b' : 2, 'c' : 3 }
dict2 = { 'x' : 100, 'y': 200 }

# save variables to a pickle file
f = open('data.pkl','wb')
pickle.dump(dict1, f)
pickle.dump(dict2, f)
f.close()

# load variables from a pickle file
f = open('data.pkl','rb')
d1 = pickle.load(f)
d2 = pickle.load(f)
f.close()

# same thing, but more concise and error-proof
with open('data.pkl', 'wb') as f:
    pickle.dump(dict1, f)
    pickle.dump(dict2, f)

with open('data.pkl', 'rb') as f:
    d1 = pickle.load(f)
    d2 = pickle.load(f)

# method 2: numpy

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
