# dmlet.py  Find thresholds in a dot matrix letter identification task

import numpy as np
import pandas as pd
from scipy import optimize, stats
from matplotlib import pyplot as plt

# load data file
df = pd.read_csv('dmlet.txt', header=None, delim_whitespace=True,
                 comment='%', skip_blank_lines=True)
df.columns = ['trial', 'matchtrial', 'siglet', 'sigcst', 'noisevar',
              'seedu', 'seedn', 'resplet', 'correct', 'rt']

# count trials and correct responses for each signal and noise value
df2 = df.groupby(['noisevar','sigcst'])['correct']
df2 = df2.agg(ncorrect='sum', ntrials='count')
df2.reset_index(inplace=True)  # make indices into data columns

# find a threshold
def threshold(x, plot=True):
    
    fitfn = lambda u, mu, sigma : (1/26) + (25/26)*stats.norm.cdf(u,mu,sigma)
    logclip = lambda v : np.log(np.maximum(v, 1e-9))
    errfn = lambda p : -logclip( stats.binom.pmf(x['ncorrect'], x['ntrials'], fitfn(x['sigcst'],p[0],p[1])) ).sum()
    
    xinit = (x['sigcst'].median(), 0.1)
    res = optimize.minimize(errfn, x0=xinit, method='Nelder-Mead')
    thresh = res.x[0]
    print(res.message)
    
    if plot:
        xx = np.linspace(0,1,100)
        yy = fitfn(xx,res.x[0],res.x[1])
        plt.plot(xx,yy,'k-')
        plt.plot(x['sigcst'],x['ncorrect']/x['ntrials'],'o')
        plt.xlabel('signal contrast')
        plt.ylabel('proportion correct')
    
    return thresh

# find the threshold for each noise level
s3 = df2.groupby(['noisevar']).apply(threshold, plot=True)
plt.show()
df3 = pd.DataFrame(s3, columns=['thresh'])
df3.reset_index(inplace=True)

# plot squared thresholds vs noise level
plt.plot(df3['noisevar'], df3['thresh']**2, 'ro-')
plt.xlim((0,0.042))
plt.ylim((0,0.40))
plt.xlabel('noise variance')
plt.ylabel('threshold squared')
plt.show()
