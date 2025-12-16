import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats, optimize

# load data and group by signal contrast
df = pd.read_csv('data.txt')
dfg = df.groupby('contrast')['correct'].agg(['sum', 'count', 'mean'])
dfg.reset_index(inplace=True)

# find the maximum-likelihood fit of the normal cdf

def fitfn(x, mu, sigma):
    return 0.5 + 0.5*stats.norm.cdf(x, mu, sigma)

def errfn(p):
    return -stats.binom.logpmf(dfg['sum'], dfg['count'], fitfn(dfg['contrast'], p[0], p[1])).sum()

res = optimize.minimize(errfn, x0=(dfg['contrast'].mean(),0.2), method='Nelder-Mead')
mu_hat, sigma_hat = res.x
print(f'fit: p = 0.5 + 0.5*stats.norm.cdf(x, {mu_hat:.3f}, {sigma_hat:.3f})')
print(f'75% threshold: {mu_hat:.3f}')

# plot data and fit
xmax = 1.1*dfg['contrast'].max()
xx = np.linspace(0,xmax,100)
plt.plot(xx,fitfn(xx, mu_hat, sigma_hat))
plt.plot([mu_hat, mu_hat],[-0.1, 1.1], 'k--')
plt.text(mu_hat+0.005, 0, f'75% threshold = {mu_hat:.3f}')
plt.plot(dfg['contrast'], dfg['mean'], 'ro')
plt.xlabel('signal contrast', fontsize=18)
plt.ylabel('proportion correct', fontsize=18)
plt.xlim(0, xmax)
plt.ylim(-0.1, 1.1)
plt.show()
