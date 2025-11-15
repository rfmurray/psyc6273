# dmlet_minimal.py  Find thresholds in a dot matrix letter identification task

import numpy as np
import pandas as pd
from scipy import optimize, stats

# load data file
df = pd.read_csv('dmlet.txt', header=None, sep='\s+',
                 comment='%', skip_blank_lines=True,
                 usecols = [3, 4, 8], names=['sigcst', 'noisevar', 'correct'])

# find a threshold
def threshold(x):
    
    def fitfn(u, mu, sigma):
        return (1/26) + (25/26)*stats.norm.cdf(u,mu,sigma)
        
    def errfn(p):
        return -stats.binom.logpmf(x['correct'], 1, fitfn(x['sigcst'],p[0],p[1])).clip(-100,np.inf).sum()

    res = optimize.minimize(errfn, x0=(x['sigcst'].median(), 0.1), method='Nelder-Mead')
    return res.x[0]

# find the threshold for each noise level
thresh = df.groupby(['noisevar']).apply(threshold, include_groups=False)
print(thresh)
