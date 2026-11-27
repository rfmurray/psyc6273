# problemset2_analysis.py  Analysis of data from Posner cueing task

import pandas as pd
import matplotlib.pyplot as plt

# load trial-by-trial data
df = pd.read_csv('data.txt')

# find proportion correct and response time for each cue type
df2 = df.groupby('cueValid')[['correct', 'rt']].mean().reset_index()

# convert cue validity code (0 or 1) to a string ('invalid' or 'valid')
def num2str(k):
    return ['invalid', 'valid'][k]
df2['cueValidStr'] = df2['cueValid'].apply(num2str)

# plot the results
fig, ax = plt.subplots(1, 2, figsize=(12,5))
ax[0].bar(df2.cueValidStr, df2.correct)
ax[1].bar(df2.cueValidStr, df2.rt)
ax[0].set_ylabel('proportion correct', fontsize=18)
ax[1].set_ylabel('response time (s)', fontsize=18)
plt.show()
