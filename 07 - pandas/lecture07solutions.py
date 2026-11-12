# lecture07solutions.py  Solutions to lecture 7 problems

# 1. On github I've posted a file of psychophysical data, dmlet.txt, from
# an experiment on letter identification. On each trial, a randomly chosen
# letter was shown in some level of Gaussian noise. The noise level is indicated
# in column 5. Whether the participant gave the correct response or not
# is indicated by 0 (incorrect) or 1 (correct) in column 9. Find the proportion
# of correct responses in each level of Gaussian noise.

import numpy as np
import pandas as pd

# load data file
df = pd.read_csv('dmlet.txt', header=None, sep='\s+',
                 comment='%', skip_blank_lines=True)
df.columns = ['trial', 'matchtrial', 'siglet', 'sigcst', 'noisevar',
              'seedu', 'seedn', 'resplet', 'correct', 'rt']

# find proportion correct for each noise level
df2 = df.groupby('noisevar')['correct'].mean()
print(df2)
