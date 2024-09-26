# text_file.py

import os
os.chdir('/Users/rfm/Desktop')

with open('data.txt', 'a') as f:
    f.write('kermit was here\n')
