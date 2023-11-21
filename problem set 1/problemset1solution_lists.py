# problemset1solution_lists.py

# 1a. create target locations

import random

target = [ (random.randint(1,2000), random.randint(1,1000)) for i in range(100) ]

# 1b. create observer response locations

def perturb(p, xlim=(1,2000), ylim=(1,1000)):
    px = p[0] + random.gauss(mu=0, sigma=10)
    py = p[1] + random.gauss(mu=0, sigma=10)
    px = max(min(px,xlim[1]),xlim[0])
    py = max(min(py,ylim[1]),ylim[0])
    return round(px), round(py)

response = [ perturb(t) for t in target ]

# 1c. create response times

rt = [ 0.1 + random.gauss(mu=0, sigma=1)**2 for t in target ]

# 1d. find response errors

import math

def dist(p, q):
    return math.sqrt( (p[0]-q[0])**2 + (p[1]-q[1])**2 )

err = [ dist(target[i], response[i]) for i in range(len(target)) ]

# alternative solution:
err = [ dist(a, b) for a, b in zip(target, response) ]

# 1e. find mean error

def mean(x):
    return sum(x)/len(x)

err_mean = mean(err)

# 1f. find mean response error on fast and slow response trials

import statistics
rt_median = statistics.median(rt)

err_low = []
err_high = []
for i, r in enumerate(rt):
    if r < rt_median:
        err_low.append(err[i])
    else:
        err_high.append(err[i])

mean_low = mean(err_low)
mean_high = mean(err_high)

# alternative, more concise solution using list comprehensions:

err_low = [ e for (e,r) in zip(err,rt) if r < rt_median ]
mean_low = mean(err_low)

err_high = [ e for (e,r) in zip(err,rt) if r >= rt_median ]
mean_high = mean(err_high)

# 2. define a function that returns target locations

def randpos(n=100, xmax=2000, ymax=1000):
    return [ (random.randint(1,xmax), random.randint(1,ymax)) for i in range(n) ]
