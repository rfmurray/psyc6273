# number_analysis.py  Solution to problem set 1: number judgements

import numpy as np

data = np.loadtxt('data.txt', delimiter=',', skiprows=1)
testnum = data[:,3]
resptest = data[:,5]

testnums = np.unique(testnum)
ptest = np.zeros(testnums.shape)
for i, t in enumerate(testnums):
    ptest = resptest[testnum==t].mean()
    print(f'{t:.0f}  {ptest:.3f}')
