import glob, pickle
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib import image
from psychopy import visual, core

# define the gamma function that we'll fit to luminance measurements
def gamma(x, k, g0, gamma_exp, delta):
    
    low = x<g0
    high = x>255
    ok = ~(low|high)
    
    y = np.empty(x.shape)
    y[low] = delta
    y[high] = k+delta
    y[ok] = k * np.power((x[ok]-g0)/(255-g0), gamma_exp) + delta
    
    return y

# define the inverse of the gamma function, which is what we'll use
# in experiments after the characterization is done
def gammainv(y, k, g0, gamma_exp, delta):
    
    low = y<delta
    high = y>k+delta
    ok = ~(low|high)
    
    x = np.empty(y.shape)
    x[low] = g0
    x[high] = 255
    x[ok] = (255-g0) * np.power((y[ok]-delta)/k, 1/gamma_exp) + g0
    
    return x

# load characterization data
with open('char_measurements.pkl', 'rb') as f:
    grey = pickle.load(f)
    lum = pickle.load(f)

# fit the gamma function to the measurements
pinit = [lum.max()-lum.min(), 0, 2, lum.min()]
bounds = (np.array((0, 0, -np.inf, 0)), np.array((np.inf, 255, np.inf, np.inf)))
param, _ = optimize.curve_fit(gamma, grey, lum, p0=pinit, bounds=bounds)

# define a function that maps greylevel to luminance
def grey2lum(g):
    return gamma(g, param[0], param[1], param[2], param[3])

# plot the measurements and the fit
xx = np.arange(256)
plt.plot(xx, grey2lum(xx), 'r-', label='fit')
plt.plot(grey, lum, 'bo', label='measurements')
plt.xlabel('greylevel')
plt.ylabel('luminance')
plt.legend(loc='upper left', frameon=False)
plt.show()

# define a function that maps luminance to greylevel
def lum2grey(lum):
    return gammainv(lum, param[0], param[1], param[2], param[3])

# plot the inverse
xx = np.linspace(param[3], param[0]+param[3], 100)
plt.plot(xx, lum2grey(xx), 'r-', label='fit')
plt.plot(lum, grey, 'bo', label='measurements')
plt.xlabel('luminance')
plt.ylabel('greylevel')
plt.legend(loc='upper left', frameon=False)
plt.show()

# create a luminance image
im_raw = image.imread('gabor.jpg')
print(im_raw.shape)
lummax = 100
im_lum = lummax * (im_raw/255)

# show the image in a matplotlib window
plt.imshow(im_lum, vmin=0, vmax=lummax, cmap='Greys_r')
plt.show()

# apply the characterization results to the image
im_grey = lum2grey(im_lum)

# show the image using psychopy
win = visual.Window(units='pix')
im_unit = -1 + 2*(im_grey/255)
imStim = visual.ImageStim(win, units='pix', image=im_unit, size=im_grey.shape[1::-1])
imStim.draw()
win.flip()
core.wait(2)
win.close()
