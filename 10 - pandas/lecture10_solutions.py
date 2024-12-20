# lecture10_solutions.py  Solutions to lecture 10 workshop problems

# 1. Use pandas and the Keeling curve dataset provided in lecture 7
# to plot the average atmospheric CO2 concentration by month, averaging
# over all years in the dataset. You can use column 2 of the dataset,
# which gives an integer 1-12 that encodes the month of each measurement.
# 
# Check the help text for pd.read_csv to find what arguments that will
# make it read the Keeling dataset correctly.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('keeling.csv', comment='"', delimiter=',', header=None,
                 usecols=[0,1,6], names=['year','month','co2'] )

# eliminate missing measurements
df = df[df['co2']>0]

# find average CO2 concentration by month
s = df.groupby('month')['co2'].mean()

# plot results
plt.plot(s.index,s,'ro')
plt.xlabel('month')
plt.ylabel('CO2 concentration (ppm)')
plt.show()

# 2. Repeat problem 1, but now suppose that column 2 is not available.
# Instead, suppose you only have column 4, which gives the date of the
# measurement as a floating point number. The integer part of the number
# is the year (e.g., 1965), and the fractional part measures progress
# through the year (e.g., 1965.5 is halfway through 1965). Assume that each
# month lasts for 1/12 of the year.
# 
# Suggestion: convert the fractional part of the year to an integer
# that encodes the month, at which point you can use your solution to
# problem 1.

# load data
df = pd.read_csv('keeling.csv', comment='"', delimiter=',', header=None,
                 usecols=[3,6], names=['time','co2'] )
df = df[df['co2']>0]

# add year and month columns
df['year'] = np.floor(df['time']).astype(int)
df['month'] = np.ceil(12*(df['time'] - df['year'])).astype(int)

# add month column with an alternate, more direct approach that uses a less
# obvious numpy function (np.modf)
df['month'] = np.ceil(12*np.modf(df['time'])[0]).astype(int)

# from this point on we can use the same code as in problem 1

# find average CO2 concentration by month
s = df.groupby('month')['co2'].mean()

# plot results
plt.plot(s.index,s,'ro')
plt.xlabel('month')
plt.ylabel('CO2 concentration (ppm)')
plt.show()
