# problemset1solution_numpy.py

# 1a. create target locations

import numpy as np

ntrial = 100

x = np.random.randint(low=1, high=2000+1, size=ntrial)
y = np.random.randint(low=1, high=1000+1, size=ntrial)
target = np.column_stack((x,y))

# or the same thing in one line:
target = np.random.randint((1,1), (2000+1, 1000+1), size=(ntrial,2))

# 1b. create observer response locations

response = target + np.random.normal(loc=0, scale=10, size=target.shape)
response[:,0] = response[:,0].clip(1,2000)
response[:,1] = response[:,1].clip(1,1000)
response = response.round()

# or the same thing in two lines:
response = target + np.random.normal(loc=0, scale=10, size=target.shape)
response = response.clip((1,1),(2000,1000)).round()

# 1c. create response times

rt = 0.1 + np.random.normal(loc=0, scale=1, size=ntrial)**2

# 1d. find response errors

err = np.sqrt( ((target-response)**2).sum(axis=1)  )

# 1e. find mean error

err.mean()

# 1f. find mean error on fast and slow response trials

rt_median = np.median(rt)
err_low = err[rt < rt_median].mean()
err_high = err[rt >= rt_median].mean()

# 2. define a function that returns target locations

def randpos(n=100, xmax=2000, ymax=1000):
    x = np.random.randint(low=1, high=xmax+1, size=n)
    y = np.random.randint(low=1, high=ymax+1, size=n)
    return np.column_stack((x,y))
 
