# dmlet_minimal.py  Find thresholds in a dot matrix letter identification task

import numpy as np
import pandas as pd
from scipy import optimize, stats

# load data file
df = pd.read_csv('dmlet.txt', header=None, delim_whitespace=True,
                 comment='%', skip_blank_lines=True,
                 usecols = [3, 4, 8], names=['sigcst', 'noisevar', 'correct'])

# find a threshold
def threshold(x):
    fitfn = lambda u, mu, sigma : (1/26) + (25/26)*stats.norm.cdf(u, mu, sigma)
    logclip = lambda v : np.log(np.maximum(v, 1e-9))
    errfn = lambda p : -logclip( stats.binom.pmf(x['correct'], 1, fitfn(x['sigcst'],p[0],p[1])) ).sum()
    res = optimize.minimize(errfn, x0=(x['sigcst'].median(),0.1), method='Nelder-Mead')
    return res.x[0]

# find the threshold for each noise level
thresh = df.groupby(['noisevar']).apply(threshold)
print(thresh)
