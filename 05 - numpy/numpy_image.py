# numpy_image.py  Making image matrices with numpy

import numpy as np
from matplotlib import pyplot as plt

# make (x,y) coordinate matrices
n = 128
midn = np.floor(n/2)
xy = np.arange(-midn, midn)
xmat, ymat = np.meshgrid(xy, -xy)

# show coordinate matrices
def imgrey(x, title=''):
    plt.imshow(x, cmap='gray')
    plt.colorbar()
    plt.title(title)
    plt.show()
imgrey(xmat, 'x coordinates')
imgrey(ymat, 'y coordinates')

# make a matrix encoding distance from the origin
dmat = np.sqrt(xmat**2 + ymat**2)
imgrey(dmat, 'distance from origin')

# make a sine wave image
wavelength = 8
sinemat = np.sin(2*np.pi*xmat/wavelength)
imgrey(sinemat, 'sine wave')

# make a Gaussian window
sigma = 10
windowmat = np.exp( -(dmat**2)/(2*np.pi*(sigma**2)) )
imgrey(windowmat, 'gaussian')

# make a Gabor
gabormat = windowmat * sinemat
imgrey(gabormat, 'gabor')
