# text_files.py  Creating text files

import os, random, time

# on startup, PsychoPy's current working directory is in its own
# application folder, so we'll cd to someplace else before creating
# the data file
os.chdir('/Users/rfm/Desktop')

# open the file
f = open('data.txt', 'a')
# 'a' = if the file exists, append to it
# 'w' = if the file exists, overwrite it
# 'r' = read

# write some lines to the file
for i in range(100):
    randnum = random.uniform(0, 1)
    sampletime = time.time()
    f.write(f'{i+1:3d}, {randnum:.2f}, {sampletime:.9f}\n')

# close the file
f.close()
