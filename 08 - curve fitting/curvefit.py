# curvefit.py  Curve fitting

import numpy as np
from scipy import stats, optimize
from matplotlib import pyplot as plt

# 1. linear regression (least-squares), method 1

x = np.linspace(0, 10, num=21)
y = 5*x + 1
y = y + np.random.normal(scale=4.0, size=x.shape)

r = stats.linregress(x, y)
print(r.slope, r.intercept)

plt.plot(x, y, 'ro')
xx = np.linspace(min(x), max(x), num=100)
plt.plot(xx, r.slope*xx + r.intercept, 'k-')
plt.show()

# 2. linear regression (least-squares), method 2

x = np.linspace(0, 10, num=21)
y = 5*x + 1
y = y + np.random.normal(scale=4.0, size=x.shape)

def f(u, m, b):
    return m*u + b

popt, _ = optimize.curve_fit(f, x, y, p0=(1,0))
print(popt)

plt.plot(x, y, 'ro')
xx = np.linspace(min(x), max(x), num=100)
plt.plot(xx, f(xx, *popt), 'k-')
plt.show()

# 3. nonlinear regression (least-squares)

x = np.linspace(0, 10, num=21)
y = 4*(x-5)**2 + 2
y = y + np.random.normal(scale=4.0, size=x.shape)

def f(u, a, b, c):
    return a*(u-b)**2 + c

popt, _ = optimize.curve_fit(f, x, y, p0=(1,0,0))
print(popt)

plt.plot(x, y, 'ro')
xx = np.linspace(min(x), max(x), num=100)
plt.plot(xx, f(xx, *popt), 'k-')
plt.show()
