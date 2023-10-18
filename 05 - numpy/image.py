# image.py  Making image matrices with numpy

import numpy as np
from matplotlib import pyplot as plt

# make (i,j) coordinate matrices
n = 128
imat = np.fromfunction( lambda i, j: i, shape=(n,n) )
jmat = np.fromfunction( lambda i, j: j, shape=(n,n) )

# show coordinate matrices
def imgrey( x ):
    plt.imshow(x, cmap='gray')
    plt.colorbar()
    plt.show()
imgrey(imat)
imgrey(jmat)

# make (x,y) coordinate matrices
midn = np.floor(n/2)
xmat =   jmat - midn
ymat = -(imat - midn)
imgrey(xmat)
imgrey(ymat)

# alternative method of creating coordinate matrices: np.meshgrid()
xy = np.linspace(-midn,midn-1,n)
xmat, ymat = np.meshgrid(xy,-xy)
imgrey(xmat)
imgrey(ymat)

# make a matrix encoding distance from the origin
dmat = np.sqrt(xmat**2 + ymat**2)
imgrey(dmat)

# make a sine wave image
wavelength = 8
sinemat = np.sin(2*np.pi*xmat/wavelength)
imgrey(sinemat)

# make a Gaussian window
sigma = 10
windowmat = np.exp( -(dmat**2)/(2*np.pi*(sigma**2)) )
imgrey(windowmat)

# make a Gabor
gabormat = windowmat * sinemat
imgrey(gabormat)

# combine the above code into a function
def gabor(wavelength=8, sigma=10, shape=(128,128)):
    xmat =   np.fromfunction(lambda i, j: j, shape=shape) - np.floor(shape[1]/2)
    ymat = -(np.fromfunction(lambda i, j: i, shape=shape) - np.floor(shape[0]/2))
    dmat = np.sqrt(xmat**2 + ymat**2)
    sinemat = np.sin(2*np.pi*xmat/wavelength)
    windowmat = np.exp(-(dmat**2)/(2*np.pi*sigma**2))
    return windowmat * sinemat

im = gabor(shape=(128,256), wavelength=16, sigma=16)
imgrey(im)
