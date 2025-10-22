# steps1.py  Least-squares fit of a sinusoid to some data, in steps

import numpy as np
from scipy import optimize

# make some data to fit
dx = np.linspace(-np.pi,np.pi,20);
dy = 1 + 0.5*np.sin(dx) + np.random.normal(size=dx.shape, scale=0.1)

plt.plot(dx,dy,'ro');
plt.show()

# here's the function we're going to fit to the data; we think of this as a
# function of one variable x, with three parameters a, b, and c that change
# the position and shape of the function
def fitfn(x, a, b, c):
    return a + b*np.sin(x-c)

# here's a guess for a, b, and c
a = 1.2
b = 0.6
c = 0.1

# what's the y-value at the first data point, according to these values of a, b, and c?
fitfn(dx[0], a, b, c)

# how different is that from the true y value at the first data point?
fitfn(dx[0], a, b, c) - dy[0]

# square this, to get rid of any negative signs
(fitfn(dx[0], a, b, c) - dy[0]) ** 2

# going back a few steps, what are the y-values at *all* the data points,
# according to these values of a, b, and c?
fitfn(dx, a, b, c)

# how different are these from *all* the true y values?
fitfn(dx, a, b, c) - dy

# square this, to get rid of any negative signs
(fitfn(dx, a, b, c) - dy) ** 2

# add up these squared errors to get a single number for the error
((fitfn(dx, a, b, c) - dy) ** 2).sum()

# forget about our guesses for a, b, and c, and make the line above
# into a function of a variable p (which is a three-element array)
def errfn(p):
    return ((fitfn(dx, *p) - dy) ** 2).sum()

# use scipy.optimize.minimize to find the value of p that minimizes this function
res = optimize.minimize(errfn, x0=(0,1,0), method='Nelder-Mead')

# these are the minimum sum-of-squares estimates for a, b, and c.  done!
ahat = res.x[0]
bhat = res.x[1]
chat = res.x[2]
