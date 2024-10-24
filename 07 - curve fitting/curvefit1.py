# curvefit1.py  Curve fitting with scipy.optimize.curve_fit

import numpy as np
from scipy import stats, optimize
from matplotlib import pyplot as plt

# 1. linear regression (least-squares), method 1

x = np.linspace(0, 10, num=21)
y = 5*x + 1
y = y + np.random.normal(scale=4.0, size=x.shape)

plt.plot(x, y, 'ro')
plt.show()

r = stats.linregress(x, y)
print(r.slope, r.intercept)

plt.plot(x, y, 'ro')
plt.plot(x, r.slope*x + r.intercept, 'k-')
plt.show()

# 2. linear regression (least-squares), method 2

x = np.linspace(0, 10, num=21)
y = 5*x + 1
y = y + np.random.normal(scale=4.0, size=x.shape)

plt.plot(x, y, 'ro')
plt.show()

def f(u, m, b):
    return m*u + b

popt, _ = optimize.curve_fit(f, x, y, p0=(1,0))
print(popt)

plt.plot(x, y, 'ro')
plt.plot(x, f(x, *popt), 'k-')
plt.show()

# normally if we wanted to do linear regression, we'd use method 1 above,
# instead of method 2, because method 1 is simpler. however, understanding
# method 2 allows us to easily move on to nonlinear regression (method 3).

# 3. nonlinear regression (least-squares)

x = np.linspace(0, 10, num=21)
y = 4*(x-5)**2 + 2
y = y + np.random.normal(scale=4.0, size=x.shape)

plt.plot(x, y, 'ro')
plt.show()

def f(u, a, b, c):
    return a*(u-b)**2 + c

popt, _ = optimize.curve_fit(f, x, y, p0=(1,0,0))
print(popt)

plt.plot(x, y, 'ro')
xx = np.linspace(min(x), max(x), num=100)
plt.plot(xx, f(xx, *popt), 'k-')
plt.show()
