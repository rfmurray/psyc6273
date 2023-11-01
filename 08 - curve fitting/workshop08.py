# workshop08.py  Lecture 8 workshop problems

# The Keeling curve shows the atmospheric concentration of carbon dioxide
# from 1958 to the present. This data is given in the accompanying file
# keeling.csv. Fit a curve (choose any curve you think might make a good fit)
# to the interpolated concentration (seventh column) versus the decimal year
# (fourth column). Plot the data and the fitted curve.

# If you would like suggestions about how to do this, here are some steps
# you could take.

# 1. Use np.loadtxt() to load the data from keeling.csv. Note that the data
# file uses an unusual comment character, and has comma-separated values.
# In the resulting array, keep just the two columns that you will need.

# 2. If you plot the data, you will see that there are some missing values,
# indicated by negative CO2 concentrations. Use boolean indexing to remove
# these rows.

# 3. Often a good approach to a complex problem is to start with a simplified
# version. The data is clearly not linear, but try starting with a linear
# fit anyway, i.e., y = m*x + b.

# 4. Next try improving the fit by using a more flexible fitting function.
# Try a second-order polynomial: y = a*(x**2) + b*x + c. Whether your fitting
# routine works or not might depend on your initial guess as to the
# parameters, so try something that's at least in the right ballpark.
# For example, you could set a=0, and b and c to the values for
# a straight line through the first and last data points.


You could
# use an initial guess with a=0, and the other two parameters initialized
# as in the linear fit.

# 5. Now try also fitting the annual variation that is evident in the data.
# Fit a second-order polynomial plus sinusoidal variation with a period of
# one year: y = a*(x**2) + b*x + c + d*np.sin(2*np.pi*x-e).
# Parameter d controls the amplitude of the sine wave, and e controls
# the phase, i.e., at what time during the year the curve peaks.
