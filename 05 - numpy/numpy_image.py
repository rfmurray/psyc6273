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
xy = np.arange(0, n) - midn
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
imgrey(gabormat, 'gabor (contrast)', vmin=-1, vmax=1)

# add noise to the gabor
stimmat = gabormat + np.random.normal(loc=0, scale=0.5, size=gabormat.shape)
imgrey(stimmat, 'noisy gabor (contrast)', vmin=-1, vmax=1)

# convert to positive-valued luminances that we could show on a calibrated monitor
bglum = 100               # background luminance
signal_contrast = 0.50    # Weber contrast = (foreground - background)/background
signalmat = signal_contrast * gabormat  # this works because the max value in gabormat is 1.0
noisemat = np.random.normal(loc=0, scale=0.2, size=signalmat.shape)
stimmat = signalmat + noisemat
lummat = bglum*(1 + stimmat)
imgrey(lummat, 'noisy gabor (luminance)', vmin=0, vmax=200)

# going back a few steps, here's how rotate values in the coordinate matrices
theta = 10 * (np.pi/180)  # 10 degrees, converted to radians
xrmat = np.cos(theta)*xmat - np.sin(theta)*ymat
yrmat = np.sin(theta)*xmat + np.cos(theta)*ymat

# if we make an image using these rotated coordinate matrices, then the image is rotated
wavelength = 8
cosmat = np.cos(2*np.pi*xrmat/wavelength)
imgrey(cosmat, 'cosine wave (rotated)')
