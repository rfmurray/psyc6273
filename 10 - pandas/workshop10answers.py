# workshop10answers.py  Lecture 10 workshop answers

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv('keeling.csv', comment='"', delimiter=',', header=None,
                 usecols=[3,6], names=['time','co2'] )

# eliminate missing measurements
df = df[df['co2']>0]

# 1. Use the column of keeling.csv where the time of each CO2 measurement is
# given by a decimal number: the integer part is the year, and the fractional
# part measures progress through the year, e.g., midway through 1965 has
# a value of 1965.5. Group the measurements approximately by month (assume
# that each month lasts 1/12 of the year), and plot the average CO2 concentration
# for each month, averaged over all years.

# add year and month columns
df['year'] = np.floor(df['time']).astype(int)
df['month'] = np.ceil(12*(df['time'] - df['year'])).astype(int)
df.loc[df['month']==0,'month'] = 1

# find average CO2 concentration by month
s2 = df.groupby('month')['co2'].mean()

# plot results
plt.plot(s2.index,s2,'ro')
plt.xlabel('month')
plt.ylabel('CO2 concentration (ppm)')
plt.show()
