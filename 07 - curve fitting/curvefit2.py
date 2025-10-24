# curvefit2.py  Curve fitting with scipy.optimize.minimize

import random, numpy as np
from scipy import optimize, stats
from matplotlib import pyplot as plt

# 1. minimize a function of one variable

# make a function to minimize
def minfn(x):
    return 5 + (x-1) ** 2

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
def minfn(p):
    return (p[0]-1)**2 + (p[1]-2)**2

# minimize it
res = optimize.minimize(minfn, x0=(0,0), method='Nelder-Mead')
print(res)


# 3. least-squares curve fitting

# make some data to fit
dx = np.linspace(-np.pi,np.pi,20)
dy = 1 + 0.5*np.sin(dx) + np.random.normal(size=dx.shape, scale=0.1)

plt.plot(dx,dy,'ro');
plt.show()

# make the fitting function
def fitfn(x, a, b, c):
    return a + b*np.sin(x-c)

# make the error function (sum-of-squares)
# (see steps1.py for a step-by-step construction of this function)
def errfn(p):
    return ( ( fitfn(dx,*p) - dy ) ** 2 ).sum()

# minimize the error function
res = optimize.minimize(errfn, x0=(0,1,0), method='Nelder-Mead')
print(f'fit: y = ({res.x[0]:.2f}) + ({res.x[1]:.2f}) * sin( x - ({res.x[2]:.2f}) )')

# plot data and fitted function
plt.plot(dx,dy,'ro');
xx = np.linspace(-np.pi,np.pi,100)
plt.plot(xx,fitfn(xx,*res.x),'k-')
plt.show()

# alternative: recall that we can also use optimize.curve_fit() for
# sum-of-squares curve fitting


# 4. improve the fit by making several tries with different inital guesses

# we'll use the data, fitting function, and error function from the previous section

# make several fits
errmin = np.inf
pmin = np.nan
for i in range(20):
    
    # make a fit from a random starting point
    pinit = ( random.gauss(0,2), random.uniform(0,2), random.uniform(-np.pi, np.pi) )
    res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
    
    # compare error to best so far
    if res.fun < errmin:
        pmin = res.x
        errmin = res.fun

# report results of fit
print(f'fit: y = ({pmin[0]:.2f}) + ({pmin[1]:.2f}) * sin( x - ({pmin[2]:.2f}) )')

# plot data and fitted function
plt.plot(dx,dy,'ro');
xx = np.linspace(-np.pi,np.pi,100)
plt.plot(xx,fitfn(xx,*pmin),'k-')
plt.show()
