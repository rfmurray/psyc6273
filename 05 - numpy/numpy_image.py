# numpy_image.py  Making image matrices with numpy

import numpy as np
from matplotlib import pyplot as plt

# define a function to show greyscale images
def imgrey(x, title='', **kwargs):
    plt.imshow(x, cmap='gray', interpolation=None, **kwargs)
    plt.colorbar()
    plt.title(title)
    plt.show()

# make (x,y) coordinate matrices
n = 128
midn = np.floor(n/2)
xy = np.arange(-midn, midn)
xmat, ymat = np.meshgrid(xy, -xy)

# show coordinate matrices
imgrey(xmat, 'x coordinates')
imgrey(ymat, 'y coordinates')

# make a matrix encoding distance from the origin, in pixels
dmat = np.sqrt(xmat**2 + ymat**2)
imgrey(dmat, 'distance from origin, in pixels')

# make a cosine wave image
wavelength = 8
cosmat = np.cos(2*np.pi*xmat/wavelength)
imgrey(cosmat, 'cosine wave')

# make a Gaussian image
sigma = 10
windowmat = np.exp( -(dmat**2)/(2*np.pi*(sigma**2)) )
imgrey(windowmat, 'gaussian')

# make a cosine-phase Gabor
gabormat = windowmat * cosmat
imgrey(gabormat, 'gabor (contrast)')

# convert to positive-valued luminances that we could show on a calibrated monitor
bglum = 100        # background luminance
contrast = 0.50    # Weber contrast = (foreground - background)/background
lummat = bglum*(1 + contrast * gabormat)  # this works because the maximum value in gabormat is 1.0
imgrey(lummat, 'gabor (luminance)', vmin=0, vmax=200)

# add noise to the gabor
stimmat = contrast * gabormat + np.random.normal(loc=0, scale=0.2, size=gabormat.shape)
lummat = bglum*(1 + stimmat)
imgrey(lummat, 'noisy gabor (luminance)', vmin=0, vmax=200)
