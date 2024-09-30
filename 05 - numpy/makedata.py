# makedata.py  Make a file of simulated behavioural data

import numpy as np
import scipy.stats

# set parameters
ntrials = 200
stimlevels = np.linspace(-1.0, 1.0, 10)
sigma = 0.5

# make array of trial numbers
trialnum = np.arange(ntrials)+1

# choose random stimulus levels
stim = np.random.choice(stimlevels, size=ntrials)

# find theoretical proportion correct at each stimulus level; this is based
# on the parameter sigma whose value we set above
pcorrect = scipy.stats.norm.cdf(stim, loc=0.0, scale=sigma)

# use a random number generator to get statistically plausible
# correct/incorrect responses for each trial
correct = np.random.binomial(1,pcorrect)

# make up some reaction times
rt = 0.1 + (np.random.normal(size=ntrials) ** 2)

# assemble all the simulated data into a single array
data = np.column_stack((trialnum,stim,correct,rt))

# write the simulated data to a text file
np.savetxt('data.txt',data,fmt=('%3d,%7.4f,%d,%6.4f'))
