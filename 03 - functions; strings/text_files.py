# text_files.py  Creating text files

import os, random, time

# on startup, PsychoPy's current working directory is in its own
# application folder, so we'll cd to someplace else before creating
# the data file
os.chdir('/Users/rfm/Desktop')

# check current directory
os.getcwd()

# open the file
f = open('data.txt', 'a')   # could also provide a full path, e.g., '/Users/rfm/data.txt'
# 'a' = if the file exists, append to it
# 'w' = if the file exists, overwrite it
# 'r' = read

# write some lines to the file
for i in range(100):
    randnum = random.uniform(0, 1)  # returns a random number
    sampletime = time.time()        # returns seconds since start of January 1, 1970 ("the epoch")
    f.write(f'{i+1:3d}, {randnum:.2f}, {sampletime:.9f}\n')

# close the file
f.close()
