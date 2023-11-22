# workshop8b_answers.py  Lecture 8 workshop problems

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


# solution 1. fit a straight line using an objective function that we define ourselves

# define a line
fitfn = lambda x, p : p[0]*x + p[1]

# define the sum-of-squares error function
errfn = lambda p : (( co2 - fitfn(time,p) ) ** 2).sum()

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


# solution 2. fit a smoothly increasing curve, ignoring seasonal oscillations

# let's try a second-order polynomial
fitfn = lambda x, p : p[0]*(x**2) + p[1]*x + p[2]

# define the sum-of-squares error function
errfn = lambda p : (( co2 - fitfn(time,p) ) ** 2).sum()

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


# solution 3. fit a smoothly increasing curve, with sinusoidal variations

# define a second-order polynomial plus sinusoidal variation with a period of one year
fitfn = lambda x, p : p[0]*(x**2) + p[1]*x + p[2] + p[3]*np.sin(2*np.pi*x-p[4])

# define the sum-of-squares error function
errfn = lambda p : (( co2 - fitfn(time,p) ) ** 2).sum()

# same initial guess as before, plus arbitrary parameters for sinusoid
m = (co2[-1]-co2[0]) / (time[-1]-time[0])
b = co2[0] - m*time[0]
pinit = (0, m, b, 5, 0)

# find parameters of best fit
res = optimize.minimize(errfn, x0=pinit, method='Nelder-Mead')
print(res)

# plot fit
plotit()
plt.plot(time,fitfn(time,res.x),'g-',label='parabola+sinusoid')
plt.legend(loc='upper left')
plt.show()
