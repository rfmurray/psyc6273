import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# define gamma function that maps greylevel to luminance
def gammafn(x, k, g0, gamma, delta):
    
    low = x<g0
    high = x>255
    ok = ~(low|high)
    
    y = np.empty(x.shape)
    y[low] = delta
    y[high] = k+delta
    y[ok] = k * np.power((x[ok]-g0)/(255-g0), gamma) + delta
    return y

# define inverse of gamma function
def gammainv(y, k, g0, gamma, delta):
    
    low = y<delta
    high = y>k+delta
    ok = ~(low|high)
    
    x = np.empty(y.shape)
    x[low] = g0
    x[high] = 255
    x[ok] = (255-g0) * np.power((y[ok]-delta)/k, 1/gamma) + g0
    return x

# load calibration data
data = np.loadtxt('caldata.txt', delimiter=',')
grey = data[:,0]
lum = data[:,1]

# show calibration data
plt.plot(grey,lum,'ro')
plt.xlabel('greylevel')
plt.ylabel('luminance (cd/m^2)')
plt.show()

# make sum-of-squares fit of gamma function to calibration data
k0 = max(lum)-min(lum)
g00 = 0
gamma0 = 2.2
delta0 = min(lum)
popt, _ = optimize.curve_fit(gammafn, grey, lum, p0 = (k0, g00, gamma0, delta0))

# show calibration data with fit
plt.plot(grey,lum,'ro')
gg = np.linspace(min(grey),max(grey),50)
plt.plot(gg, gammafn(gg,*popt),'r-')
plt.xlabel('greylevel')
plt.ylabel('luminance (cd/m^2)')
plt.show()

# create a luminance image
from matplotlib import image
im_raw = image.imread('gabor.jpg')
lummax = 100
im_lum = lummax * (im_raw/255)

# show the image
plt.imshow(im_lum, cmap='Greys')
plt.show()

# the calibration results to the image
im_grey = gammainv(im_lum, *popt)

# show the modified image
plt.imshow(im_grey, cmap='Greys')
plt.show()
