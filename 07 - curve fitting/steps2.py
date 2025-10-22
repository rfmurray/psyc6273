# steps2.py  Maximum likelihood fit of a curve to a psychometric function, in steps

import numpy as np
from scipy import optimize, stats

# make some psychometric data to fit
stimlev = np.array([ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50 ])
ntrials = np.array([   20,   20,   20,   20,   20,   20,   20,   20,   20,   20 ])
ncorrect = np.array([  10,   11,   10,   12,   14,   15,   14,   18,   19,   20 ])

# here's the function we're going to fit to the data
def fitfn(x, p):
    return 0.5 + 0.5*stats.norm.cdf(x,loc=p[0],scale=p[1])

# here's a guess for the parameters
pguess = (0.10, 0.20)

# what's the probability of a correct response at the lowest stimulus
# level, according to these values of mu and sigma?
fitfn(stimlev[0], pguess)

# what's the probability of getting the observed number of correct
# responses at the lowest stimulus level, according to these parameters?
stats.binom.pmf(ncorrect[0], ntrials[0], fitfn(stimlev[0],pguess))

# what are the probabilities of correct responses at *all* the stimulus
# levels, according to these values of mu and sigma?
fitfn(stimlev, pguess)

# what are the probabilities of getting the observed numbers of correct
# responses at *all* the stimulus levels, according to these values of mu
# and sigma?
stats.binom.pmf(ncorrect, ntrials, fitfn(stimlev,pguess))

# what's the joint probability of all these observed numbers of correct
# responses, according to these values of mu and sigma?
stats.binom.pmf(ncorrect, ntrials, fitfn(stimlev,pguess)).prod()

# the number resulting from the previous line was *very* small, so we
# might be concerned about underflow errors, i.e., results being rounded
# down to zero. so we'll deal with the logarithm of the probability
# instead.
np.log( stats.binom.pmf(ncorrect, ntrials, fitfn(stimlev,pguess)) ).sum()

# forget about our guess for the parameters, and make the line above
# into a function of a variable p (which is a two-element array). our goal
# is to find the value of p that maximizes this function.

# def errfn(p):
#     return np.log( stats.binom.pmf(ncorrect, ntrials, fitfn(stimlev,p)) ).sum()

def errfn(p):
    return stats.binom.logpmf(ncorrect, ntrials, fitfn(stimlev,p)).sum()

# we don't have a Python function that finds the maximum of a function, but
# we do have one that finds the minimum. we'll add a negative sign to the
# function defined just above. maximizing the above function is the same as
# minimizing the one with a negative sign added.
def errfn(p):
    return -stats.binom.logpmf(ncorrect, ntrials, fitfn(stimlev,p)).sum()

# use scipy.optimize.minimize to find the value of p that minimizes this function
res = optimize.minimize( errfn, x0=(0.20, 0.20), method='Nelder-Mead')

# these are the maxium likelihood estimates of the parameters
phat = res.x
