# curvefit2.py  Curve fitting with scipy.optimize.minimize

import numpy as np
from scipy import optimize, stats
from matplotlib import pyplot as plt

# 1. minimize a function of one variable

# make a function to minimize
minfn = lambda x : 5 + (x-1) ** 2

# find the input value that minimizes it
res = optimize.minimize_scalar(minfn, bounds=(-10,10))
print(res)

# show results
xx = np.linspace(-3,3,100)
plt.plot(xx,minfn(xx))
plt.plot(res.x,res.fun,'ro')
plt.show()


# 2. minimize a function of two variables

# make a function to minimize
minfn = lambda p : (p[0]-1)**2 + (p[1]-2)**2

# minimize it
res = optimize.minimize(minfn, x0=(0,0), method='Nelder-Mead')
print(res)


# 3. least-squares curve fitting

# make some data to fit
dx = np.linspace(-np.pi,np.pi,20);
dy = 1 + 0.5*np.sin(dx) + np.random.normal(size=dx.shape, scale=0.1)

# make the fitting function
fitfn = lambda x, a, b, c : a + b*np.sin(x-c)

# make the error function (sum-of-squares)
# (see steps1.py for a step-by-step construction of this function)
errfn = lambda p : ( ( fitfn(dx,p[0],p[1],p[2]) - dy ) ** 2 ).sum()

# minimize the error function
res = optimize.minimize(errfn, x0=(0,1,0), method='Nelder-Mead')
print(f'fit: y = ({res.x[0]:.2f}) + ({res.x[1]:.2f}) * sin( x - ({res.x[2]:.2f}) )')

# plot data and fitted function
plt.plot(dx,dy,'ro');
xx = np.linspace(-np.pi,np.pi,100)
plt.plot(xx,fitfn(xx,res.x[0],res.x[1],res.x[2]),'k-')
plt.show()

# alternative: recall that we can also use optimize.curve_fit() for
# sum-of-squares curve fitting


# 4. improve the fit by making several tries with different inital guesses

# we'll use the data, fitting function, and error function from the previous section

# make several fits
errmin = np.inf
pmin = []
for i in range(20):
    
    # make a fit from a random starting point
    pinit = ( 2*np.random.randn(1), 2*np.random.rand(1), -np.pi + 2*np.pi*np.random.rand(1) )
    res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
    
    # compare error to best so far
    err = errfn(res.x)
    if err < errmin:
        pmin = res.x
        errmin = err

# report results of fit
print(f'fit: y = ({pmin[0]:.2f}) + ({pmin[1]:.2f}) * sin( x - ({pmin[2]:.2f}) )')

# plot data and fitted function
plt.plot(dx,dy,'ro');
xx = np.linspace(-np.pi,np.pi,100)
plt.plot(xx,fitfn(xx,pmin[0],pmin[1],pmin[2]),'k-')
plt.show()


# 5. maximum-likelihood parameter estimation

# make some data to fit
d = np.random.normal(size=20, loc=5.0, scale=2.0)

# make the error function
# errfn = lambda p : -stats.norm.pdf(d, loc=p[0], scale=p[1]).prod()
errfn = lambda p : -np.log( stats.norm.pdf(d, loc=p[0], scale=p[1]) ).sum()
# - scipy.stats.norm.pdf(x, loc=mu, scale=sigma) is the probability density
#   of a sample with value x from a normal distribution with mean mu
#   and standard deviation sigma

# minimize the error function
res = optimize.minimize(errfn, x0=(4,1), method='Nelder-Mead')

# report results of fit
print(f'fit: mu = {res.x[0]:.2f}, sigma = {res.x[1]:.2f}')

# compare to closed-form expressions
d.mean()
d.std()


# 6. maximum-likelihood curve fitting

# make some psychometric data to fit
stimlev = np.array([ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50 ])
ntrials = np.array([   20,   20,   20,   20,   20,   20,   20,   20,   20,   20 ])
ncorrect = np.array([  10,   11,   10,   12,   14,   15,   14,   18,   19,   20 ])

# make the fitting function
# - stats.norm.cdf(x,loc,scale) is a function of x that increases smoothly
#   from 0 to 1. loc shifts it left or right, and scale makes it
#   steeper or shallower.
fitfn = lambda x, p : 0.5 + 0.5*stats.norm.cdf(x,loc=p[0],scale=p[1])

# make the error function (negative log likelihood)
# (see steps2.py for a step-by-step construction of this function)
# - stats.binom.pmf(k, n, p) is the probability of having k successes
#   out of n independent trials, when the probability of each success is p
errfn = lambda p : -np.log( stats.binom.pmf(ncorrect,ntrials,fitfn(stimlev,p)) ).sum()

# minimize the error function
res = optimize.minimize(errfn, x0=(0.5,1), method='Nelder-Mead')

# report results of fit
print(f'fit: p = 0.5 + 0.5*stats.norm.cdf(x, {res.x[0]:.2f}, {res.x[1]:.2f})')
print(f'75% threshold: {res.x[0]:.2f}')

# plot data and fitted function
plt.plot(stimlev,ncorrect/ntrials,'ro')
xx = np.linspace(0,0.6,100)
plt.plot(xx,fitfn(xx,res.x))
plt.xlabel('stimulus level')
plt.ylabel('proportion correct')
plt.show()
