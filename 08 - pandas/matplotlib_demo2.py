# matplotlib_demo2.py  Managing figures and axes

import numpy as np
import matplotlib.pyplot as plt

# 1. create a figure window and axes; plot
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(np.random.randn(20).cumsum(), color='r')
plt.show()


# 2. create a figure window and axes
fig1 = plt.figure()
ax1 = fig1.add_subplot()

# create another
fig2 = plt.figure()
ax2 = fig2.add_subplot()

# choose a specific figure; plot
plt.figure(fig1)
plt.plot(np.random.randn(20).cumsum(), color='r')

# choose another figure; plot
plt.figure(fig2)
plt.hist(np.random.randn(50), color='r')

# alternatively, specify the axes where the plot should go
ax1.plot(np.random.randn(20).cumsum(), color='k')
ax2.hist(np.random.randn(50), color='k')

plt.show()


# 3. create a figure and three axes
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

# plot on the axes
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3*np.random.randn(30))
ax3.plot(np.random.randn(20).cumsum(), 'ko--')

plt.show()


# 4. create a figure and four axes
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

# plot on the axes
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(100), bins=50, color='k', alpha=0.5)

# no space between axes
plt.subplots_adjust(wspace=0, hspace=0)

plt.show()
