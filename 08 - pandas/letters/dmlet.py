# dmlet.py  Find thresholds in a dot matrix letter identification task

import numpy as np
import pandas as pd
from scipy import optimize, stats
from matplotlib import pyplot as plt

# load data file
df = pd.read_csv('dmlet.txt', header=None, sep='\s+',
                 comment='%', skip_blank_lines=True)
df.columns = ['trial', 'matchtrial', 'siglet', 'sigcst', 'noisevar',
              'seedu', 'seedn', 'resplet', 'correct', 'rt']

# count trials and correct responses for each signal and noise value
df2 = df.groupby(['noisevar','sigcst'])['correct']
df2 = df2.agg(ncorrect='sum', ntrials='count')
df2.reset_index(inplace=True)  # make indices into data columns

# do the same thing in one line
#df2 = df.groupby(['noisevar','sigcst'])['correct'].agg(ncorrect='sum', ntrials='count').reset_index()

# find a threshold
def threshold(x, plot=True):
    
    def fitfn(u, mu, sigma):
        return (1/26) + (25/26)*stats.norm.cdf(u,mu,sigma)
        
    def errfn(p):
        return -stats.binom.logpmf(x['ncorrect'], x['ntrials'], fitfn(x['sigcst'],p[0],p[1])).clip(-100,np.inf).sum()
    
    xinit = (x['sigcst'].median(), 0.1)
    res = optimize.minimize(errfn, x0=xinit, method='Nelder-Mead')
    thresh = res.x[0]
    print(res.message)
    
    if plot:
        xx = np.linspace(0, 1, 100)
        yy = fitfn(xx,res.x[0],res.x[1])
        plt.plot(xx,yy,'k-')
        plt.plot(x['sigcst'],x['ncorrect']/x['ntrials'],'o')
        plt.xlabel('signal contrast')
        plt.ylabel('proportion correct')
    
    return thresh

# find the threshold for each noise level
s3 = df2.groupby(['noisevar']).apply(threshold, include_groups=False, plot=True)
plt.show()
df3 = s3.reset_index(name='thresh')

# plot squared thresholds vs noise level
plt.plot(df3['noisevar'], df3['thresh']**2, 'ro-')
plt.xlim((0,0.042))
plt.ylim((0,0.40))
plt.xlabel('noise variance')
plt.ylabel('threshold squared')
plt.show()
