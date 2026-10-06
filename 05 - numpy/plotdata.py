# plotdata.py  Analyzing data with numpy

import numpy as np
from matplotlib import pyplot as plt

# part one. boolean indexing

# define an array
x = np.array([1, 2, 3, 4, 5])

# define a boolean array (same size as x), and use it to select values from x
f = np.array([True, False, False, True, False])
y = x[f]

# define a boolean array using operators on x, and use it to select values from x
f = x > 3
y = x[f]

# same thing, but shortened to a single line
y = x[x>3]

# another example: find perfect squares between 0 and 99
x = np.arange(100)
y = x[ np.round(np.sqrt(x)) == np.sqrt(x) ]


# part two. use boolean indexing to group data

# load data
trials = np.loadtxt(fname='data.txt', comments='#', delimiter=',')

# find stimulus levels
stimlevels = np.unique(trials[:,1])

# find performance at the first stimulus level
f = trials[:,1] == stimlevels[0]
pcorrect = trials[f,2].mean()

# find performance at each stimulus level
pcorrect = np.full(stimlevels.shape, np.nan)
for i, s in enumerate(stimlevels):
    f = trials[:,1]==s
    pcorrect[i] = trials[f,2].mean()

# same thing, but more concise
pcorrect = np.full(stimlevels.shape, np.nan)
for i, s in enumerate(stimlevels):
    pcorrect[i] = trials[ trials[:,1]==s, 2 ].mean()

# plot proportion correct against stimulus level
plt.plot(stimlevels,pcorrect,'ro')
plt.show()
