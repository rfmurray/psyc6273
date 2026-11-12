# lecture07_solutions2.py  Solutions to lecture 7 workshop problems, part two

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, stats

# 3. The Keeling curve shows the atmospheric concentration of carbon dioxide
# from 1958 to the present. This data posted on github, under topic 07, in
# the file keeling.csv. Fit a curve to a plot of the interpolated
# concentration (column 7) versus the decimal year (column 4).
# Experiment with various kinds of curves. You may find it helpful to start
# with a simple kind of curve, such as a straight line, and once you have
# that fit working, add more parameters to capture additional features of
# the data, such as nonlinearity and sinusoidal oscillation.
# 
# You'll need to examine the data file first, to see how what parameters
# to use when loading it. For example, what character indicates a comment
# line that doesn't contain data? 
# You may also need to preprocess the data file, for example by removing
# negative values that correspond to missing measuremnets.

# load data
data = np.loadtxt(fname='keeling.csv', comments='"', delimiter=',')
time = data[:,3]
co2 = data[:,6]

# eliminate missing measurements
f = co2 > 0
time = time[f]
co2 = co2[f]

# plot data
def plotit():
    plt.plot(time,co2,'r-',label='measurements')
    plt.xlabel('year')
    plt.ylabel('CO2 (ppm)')

plotit()
plt.show()


# solution 1. fit a straight line using an objective function that we define ourselves

# define a line
def fitfn(x, p):
    return p[0]*x + p[1]

# define the sum-of-squares error function
def errfn(p):
    return (( co2 - fitfn(time,p) ) ** 2).sum()

# make an initial guess as to the parameters; straight line through first
# and last data points
m = (co2[-1]-co2[0]) / (time[-1]-time[0])  # slope
b = co2[0] - m*time[0]                     # y-intercept
pinit = (m, b)

# find parameters of best fit
res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
print(res)

# plot fit
plotit()
plt.plot(time,fitfn(time,res.x),'k-',label='linear fit')
plt.legend(loc='upper left')
plt.show()

# if we were only interested in a linear fit, and weren't doing this as the
# first step of solving a more complex problem, we could just use standard
# linear regression, available in Python as stats.linregress(). this function
# finds the best linear sum-of-squares fit in one line of code.
res = stats.linregress(time, co2)
plotit()
plt.plot(time, res.intercept + res.slope*time,'k-',label='linear fit')
plt.legend(loc='upper left')
plt.show()


# solution 2. fit a smoothly increasing curve, ignoring seasonal oscillations

# let's try a second-order polynomial
def fitfn(x, p):
    return p[0]*(x**2) + p[1]*x + p[2]

# define the sum-of-squares error function
def errfn(p):
    return (( co2 - fitfn(time,p) ) ** 2).sum()

# make an initial guess as to the parameters
m = (co2[-1]-co2[0]) / (time[-1]-time[0])
b = co2[0] - m*time[0]
pinit = (0, m, b)

# find parameters of best fit
res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
print(res)

# plot fit
plotit()
plt.plot(time,fitfn(time,res.x),'k-',label='parabola')
plt.legend(loc='upper left')
plt.show()

# alternative: we can also use optimize.curve_fit(), which fits a nonlinear
# function using sum-of-squares error
def fitfn(x, a, b, c):
    return a*(x**2) + b*x + c
phat, _ = optimize.curve_fit(fitfn, time, co2, p0=pinit)
plotit()
plt.plot(time,fitfn(time,phat[0],phat[1],phat[2]),'k-',label='parabola')
plt.legend(loc='upper left')
plt.show()

# another alternative: we can also use numpy's Polynomial class, which
# fits a polynomial using a sum-of-squares error
pfit = np.polynomial.polynomial.Polynomial.fit(time, co2, deg=2)
plotit()
plt.plot(time,pfit(time),'k-',label='parabola')
plt.legend(loc='upper left')
plt.show()


# solution 3. fit a smoothly increasing curve, with sinusoidal variations

# define a second-order polynomial plus sinusoidal variation with a period of one year
def fitfn(x, p):
    return p[0]*(x**2) + p[1]*x + p[2] + p[3]*np.sin(2*np.pi*x-p[4])

# define the sum-of-squares error function
def errfn(p):
    return ((co2 - fitfn(time,p))**2).sum()

# same initial guess as before, plus arbitrary parameters for sinusoid
m = (co2[-1]-co2[0]) / (time[-1]-time[0])
b = co2[0] - m*time[0]
pinit = (0, m, b, np.random.uniform(1, 5), np.random.uniform(0, 2*np.pi))

# find parameters of best fit
res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
print(res)

# plot fit
plotit()
plt.plot(time, fitfn(time,res.x), 'g-', label='parabola+sinusoid')
plt.legend(loc='upper left')
plt.show()
