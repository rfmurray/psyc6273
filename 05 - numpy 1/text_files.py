# text_files.py  Creating text files

import os, random, time

# cd to someplace where we can save a data file
os.chdir('/Users/rfm/Desktop')

# open the file
f = open('data.txt', 'a')   # could also provide a full path, e.g., '/Users/rfm/data.txt'
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
    f.write('# end of data file\n')


