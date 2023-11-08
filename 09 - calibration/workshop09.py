# workshop09.py  Lecture 9 workshop problems

# Luminance calibration is a good example of a task that you might want
# to do using an object with a simple interface. When you're programming an
# experiment, you'd like to be able to calibrate your stimuli, but you don't
# want to think too much about the details of how calibration is done.

# Write a Python module called calibrate.py that defines a class that
# implements the calibration routines covered in lecture 9. Write it so that
# we can use it as follows.

# 1. Fit calibration data and save the fits in a pickle file. Define the class
# so that we can use the following code. That is, unlike in the previous
# workshop problems, here the code is part of the problem, not the solution.

import calibrate            # import the calibration module

c = calibrate.CalLum()      # create a calibration object

c.fit(grey, lum)            # pass in your calibration data, and the
                            # calibration object fits a gamma function
                            # to it, and remembers the fitted parameters

c.plot()                    # plot the measurements and the fit

c.save('caldata.pickle')    # save the fitted parameters in a pickle file
                            # (see lecture 7, files.py)

# 2. At a later time (e.g., when you run an experiment), load the
# calibration data from the pickle file.

c = calibrate.CalLum()      # create a new calibration object

c.load('caldata.pickle')    # load the saved parameters

# 3. Now that the calibration parameters have been loaded, use the object
# to convert luminances to greylevels. (Here I assume that you already
# have a 2D image im_lum that contains the luminances you'd like to show.)

im_grey = c.lum2grey(im_lum)
