# matplotlib_demo.py  Basic plot types and plot formatting

# matplotlib.pyplot is the main module that we'll use for plotting
# in this script. the convention is to import it as 'plt'.
import matplotlib.pyplot as plt
import numpy as np

# line plot
d1 = np.random.randn(100).cumsum()  # make some randomly increasing numbers
plt.plot(d1)  # plot the series
plt.show()    # after we plot it, we have to call plt.show() to make the window appear

# we can specify the colour, marker, and line type of the plot
# some colours: r g b c m y k w
# some markers: . o v s
# some line styles: - -- -. :
# see help for plt.plot for others
plt.plot(d1, color='r', marker='o', linestyle='--')
plt.show()

# can also combine the colour, marker, and number codes into a single string
plt.plot(d1, 'ro--')
plt.show()

# line plot with error bars
x = np.arange(10)                 # x-values
d2 = np.random.randn(x.size)      # y-values
err = 0.5*np.random.rand(x.size)  # size of the error bars
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

# title, axis labels, legend, ticks, text, saving to disk
plt.plot(np.random.randn(20).cumsum(), color='r', label='random walk 1')
plt.plot(np.random.randn(20).cumsum(), color='g', label='random walk 2') # we can include several plots on a single axis
plt.plot(np.random.randn(20).cumsum(), color='b', label='random walk 3')
plt.title('three random walks')   # title
plt.xlabel('time')                # x-axis label
plt.ylabel('position')            # y-axis label
plt.legend(loc='upper right')     # the argument is the location of the legend
plt.xlim(0,25)                    # range of the x-axis
plt.ylim(-10,10)                  # range of the y-axis
plt.xticks(np.arange(0,25,5))     # specify the locations of the x-axis ticks
plt.yticks(np.arange(-10,11,2))   # specify the locations of the y-axis ticks
plt.text(1,-8,'steps are normally distributed',family='helvetica',fontsize=12)  # place text on the plot
plt.savefig('testfig.png', dpi=300, bbox_inches='tight')  # save figure to disk in current working directory
plt.show()
