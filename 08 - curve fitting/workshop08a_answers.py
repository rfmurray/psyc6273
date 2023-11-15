# workshop8a_answers.py  Lecture 8 workshop problems

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, stats

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


# solution 1. fit a straight line

r = stats.linregress(time, co2)
print(r)

# plot fit
plotit()
plt.plot(time, r.slope*time + r.intercept, 'k-', label='linear fit')
plt.legend(loc='upper left')
plt.show()


# solution 2. fit a smoothly increasing curve, ignoring seasonal oscillations

# let's try a second-order polynomial
def fitfn(u, a, b, c):
    return a*(u**2) + b*u + c

# make an initial guess as to the parameters
m = (co2[-1]-co2[0]) / (time[-1]-time[0])
b = co2[0] - m*time[0]
pinit = (0, m, b)

# find parameters of best fit
popt, _ = optimize.curve_fit(fitfn, time, co2, p0=pinit)
print(popt)

# plot fit
plotit()
plt.plot(time, fitfn(time, *popt), 'k-', label='parabola')
plt.legend(loc='upper left')
plt.show()

# as an alternative approach, we could use numpy's Polynomial class, which
# fits a polynomial using a sum-of-squares error. the approach we took
# above is longer, but has the advantage that in the next step we can add
# a sinusoidal term, which we couldn't do with the Polynomial class.
pfit = np.polynomial.polynomial.Polynomial.fit(time, co2, deg=2)
plotit()
plt.plot(time, pfit(time), 'k-', label='parabola')
plt.legend(loc='upper left')
plt.show()


# solution 3. fit a smoothly increasing curve, with sinusoidal variations

# define a second-order polynomial plus sinusoidal variation with a period of one year
def fitfn(u, a, b, c, d, e):
    return a*(u**2) + b*u + c + d*np.sin(2*np.pi*u-e)

# same initial guess as before, plus arbitrary parameters for sinusoid
m = (co2[-1]-co2[0]) / (time[-1]-time[0])
b = co2[0] - m*time[0]
pinit = (0, m, b, 5, 0)

# find parameters of best fit
popt, _ = optimize.curve_fit(fitfn, time, co2, p0=pinit)
print(popt)

# plot fit
plotit()
plt.plot(time, fitfn(time,*popt), 'g-', label='parabola+sinusoid')
plt.legend(loc='upper left')
plt.show()
