# matplotlib_demo.py  Basic plot types and plot formatting

import numpy as np
import matplotlib.pyplot as plt

# line plot
d1 = np.random.randn(100).cumsum()
plt.plot(d1)
plt.show()
plt.plot(d1, color='r', marker='o', linestyle='--')
plt.show()
plt.plot(d1, 'ro--')
plt.show()
# some colours: r g b c m y k w
# some markers: . o v s
# some line styles: - -- -. :
# - see help for plt.plot for others

# line plot with error bars
x = np.arange(10)
d2 = np.random.randn(x.size)
err = 0.5*np.random.rand(x.size)
plt.errorbar(x=x, y=d2, yerr=err, capsize=5)
plt.show()

# histogram
d3 = np.random.randn(500)
plt.hist(d3, bins=20, color='g')
plt.show()

# scatterplot
dx = np.arange(30)
dy = dx + np.random.randn(dx.size)
dotsize = np.random.randint(10,100,size=dx.size)
plt.scatter(dx, dy, s=dotsize)
plt.show()

# bar plot
plt.bar(x=(1,2,3), height=(5,10,8))
plt.xticks(ticks=(1,2,3), labels=['first', 'second', 'third'])
plt.show()

# formatting: title, axis labels, legend, ticks, text, saving to disk
plt.plot(np.random.randn(20).cumsum(), color='r', label='random walk 1')
plt.plot(np.random.randn(20).cumsum(), color='g', label='random walk 2')
plt.plot(np.random.randn(20).cumsum(), color='b', label='random walk 3')
plt.title('three random walks')
plt.xlabel('time')
plt.ylabel('position')
plt.legend(loc='upper right')
plt.xlim(0,25)
plt.ylim(-10,10)
plt.xticks(np.arange(0,25,5))
plt.yticks(np.arange(-10,11,2))
plt.text(1,-8,'steps are normally distributed',family='helvetica',fontsize=12)
plt.savefig('testfig.png', dpi=300, bbox_inches='tight')
plt.show()
