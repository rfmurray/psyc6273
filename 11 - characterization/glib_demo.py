import numpy as np
import glib

# create a gamma function object
f = glib.GammaObj(p = [80, 5, 2.1, 2])

# convert some greylevels to luminance
grey = np.random.randint(low=5, high=255, size=10)
lum = f.gamma(grey)

# convert the luminances back to greylevels
grey2 = f.gammainv(lum)

# check that gamma() and gammainv() are inverses
maxdiff = abs(grey - grey2).max()
print(maxdiff)
