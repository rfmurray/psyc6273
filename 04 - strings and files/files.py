# files.py  Saving and loading variables to and from disk files

# method 1: text files

import os, random, time

# cd to someplace where we can save a file
os.chdir('/Users/rfm/Desktop')

# open the file
f = open('data.txt', 'a')   # could also provide a full path, e.g., '/Users/rfm/Desktop/data.txt'
# 'a' = if the file exists, append to it
# 'w' = if the file exists, overwrite it
# 'r' = read

# write a header
f.write('# trial,rand,time\n')

# write some lines to the file
for i in range(100):
    randnum = random.uniform(0, 1)  # returns a uniformly distributed random number between 0 and 1
    sampletime = time.time()        # returns seconds since start of January 1, 1970 ("the epoch")
    f.write(f'{i+1:3d}, {randnum:.2f}, {sampletime:.9f}\n')

# close the file
f.close()

# alternative: close file automatically

with open('data.txt', 'a') as f:
    f.write('# trial,rand,time\n')
    for i in range(100):
        randnum = random.uniform(0, 1)
        sampletime = time.time()
        f.write(f'{i+1:3d}, {randnum:.2f}, {sampletime:.9f}\n')

# we'll see how to load a text file when we cover the numpy module

# method 2: pickle files

import pickle

# create some variables
# - here we're using lists, but the variables could be integers, strings,
#   numpy arrays, etc.
list1 = [ 1, 2.5, True, None ]
list2 = [ 3.0, 3.1, 3.2, 3.3 ]

# save variables to a pickle file
f = open('data.pkl','wb')
pickle.dump(list1, f)
pickle.dump(list2, f)
f.close()

# load variables from a pickle file
f = open('data.pkl','rb')
l1 = pickle.load(f)
l2 = pickle.load(f)
f.close()

# same thing, but more concise and error-proof
with open('data.pkl', 'wb') as f:
    pickle.dump(list1, f)
    pickle.dump(list2, f)

with open('data.pkl', 'rb') as f:
    l1 = pickle.load(f)
    l2 = pickle.load(f)
