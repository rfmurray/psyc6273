# curvefit3.py  More curve fitting with scipy.optimize.minimize

import random, numpy as np
from scipy import optimize, stats
from matplotlib import pyplot as plt

# 1. maximum-likelihood parameter estimation

# make some data to fit
d = np.random.normal(size=20, loc=5.0, scale=2.0)

# make the error function

# def errfn(p):
#     return -stats.norm.pdf(d, loc=p[0], scale=p[1]).prod()

# def errfn(p):
#     return -np.log( stats.norm.pdf(d, loc=p[0], scale=p[1]) ).sum()
# scipy.stats.norm.pdf(x, loc=mu, scale=sigma) is the probability density
# of a sample with value x from a normal distribution with mean mu
# and standard deviation sigma

def errfn(p):
    return -stats.norm.logpdf(d, loc=p[0], scale=p[1]).sum()

# minimize the error function
res = optimize.minimize(errfn, x0=(4,1), method='Nelder-Mead')

# report results of fit
print(f'fit: mu = {res.x[0]:.2f}, sigma = {res.x[1]:.2f}')

# compare to closed-form expressions
d.mean()
d.std()


# 2. maximum-likelihood curve fitting

# make some psychometric data to fit
stimlev = np.array([ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50 ])
ntrials = np.array([   20,   20,   20,   20,   20,   20,   20,   20,   20,   20 ])
ncorrect = np.array([  10,   11,   10,   12,   14,   15,   14,   18,   19,   20 ])

# make the fitting function
# - stats.norm.cdf(x,loc,scale) is a function of x that increases smoothly
#   from 0 to 1. loc shifts it left or right, and scale makes it
#   steeper or shallower.
def fitfn(x, p):
    return 0.5 + 0.5*stats.norm.cdf(x,loc=p[0],scale=p[1])

# make the error function (negative log likelihood)
# (see steps2.py for a step-by-step construction of this function)
# - stats.binom.pmf(k, n, p) is the probability of having k successes
#   out of n independent trials, when the probability of each success is p

#def errfn(p):
#    return -np.log( stats.binom.pmf(ncorrect,ntrials,fitfn(stimlev,p)) ).sum()

def errfn(p):
    return -stats.binom.logpmf(ncorrect,ntrials,fitfn(stimlev,p)).sum()

# minimize the error function
res = optimize.minimize(errfn, x0=(0.5,1), method='Nelder-Mead')

# report results of fit
print(f'fit: p = 0.5 + 0.5*stats.norm.cdf(x, {res.x[0]:.2f}, {res.x[1]:.2f})')
print(f'75% threshold: {res.x[0]:.2f}')

# plot data and fitted function
plt.plot(stimlev,ncorrect/ntrials,'ro')
xx = np.linspace(0,0.6,100)
plt.plot(xx,fitfn(xx,res.x))
plt.show()
