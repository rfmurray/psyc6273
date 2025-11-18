import numpy as np
import imageio.v3 as iio
from psychopy import visual, core

# we read an image; the result is a numpy array; observe that it consists of
# integers in the range 0-255.
im = iio.imread('fechner.jpg')
print(im)
print(im.dtype)
print(im.min(), im.max())

# visual.ImageStim() expects an image in the range 0-1, so if we show
# the image in its current format, we'll get a completely white image.
# (try it and see, by commenting out the next two lines of code.)

# instead, we'll convert the image to floating point, and then divide by
# 255 to map it to the range 0-1.
im = im.astype(np.float64)/255

# iio.imread reads the image upside down, so we'll flip it vertically.
im = np.flip(im, axis=0)

# now we can show the image with ImageStim; note that the 'size' argument to
# ImageStim expects the size in the order (width, height), whereas the 'shape'
# property of a numpy array gives the size in the order (height, width), so
# we have to switch the order.
win = visual.Window(units='pix')
img = visual.ImageStim(win, image=im, size=(im.shape[1], im.shape[0]))
img.draw()
win.flip()
core.wait(2)

# in problem set 2, you'll make and show noisy gabor patterns. the gabor has
# the range -1 to 1, so you'll also have to map it to the range 0-1. to keep
# this demo simple, I'll just use a sample of white Gaussian noise, clipped
# so that it's limited to the range -1 to 1.
noise = np.random.normal(loc=0, scale=0.5, size=(256,256)).clip(-1,1)

# here's how we can map the range [-1,1] to [0,1]
noise = (noise+1)/2
print(noise)
print(noise.dtype)
print(noise.min(), noise.max())

# now we can show the noise image; here I also show a more concise way of switching
# the order of height and width.
img = visual.ImageStim(win, image=noise, size=noise.shape[1::-1])
img.draw()
win.flip()
core.wait(2)

win.close()
