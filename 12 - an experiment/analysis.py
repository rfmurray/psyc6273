import numpy as np
import pandas as pd
from scipy import stats, optimize
import matplotlib.pyplot as plt

# load data and group by signal contrast
df = pd.read_csv('data/data_rfm.txt', comment='#')
dfg = df.groupby('contrast')['correct'].agg(ncorrect='sum', ntrial='count', pcorrect='mean')
dfg.reset_index(inplace=True)
dfg['stderr'] = (dfg['pcorrect']*(1-dfg['pcorrect'])/dfg['ntrial'])**0.5
print(df)
print(dfg)

# find the maximum-likelihood fit of the normal cdf

def fitfn(x, mu, sigma):
    return 0.5 + 0.5*stats.norm.cdf(x, mu, sigma)

def errfn(p):
    return -stats.binom.logpmf(dfg['ncorrect'], dfg['ntrial'], fitfn(dfg['contrast'], p[0], p[1])).sum()

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
plt.errorbar(dfg['contrast'], dfg['pcorrect'], yerr=dfg['stderr'], fmt='ro')
plt.xlabel('signal contrast', fontsize=18)
plt.ylabel('proportion correct', fontsize=18)
plt.xlim(0, xmax)
plt.ylim(-0.1, 1.1)
plt.show()
