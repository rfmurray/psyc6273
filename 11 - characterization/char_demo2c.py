import numpy as np
from matplotlib import image
from psychopy import visual, core
import charlib

# create a luminance image
im_raw = image.imread('gabor.jpg')
lummax = 100
im_lum = lummax * (im_raw/255)

# apply the characterization results to the image
char = charlib.CharLum(fname='charlum.pkl')
im_unit = char.lum2unit(im_lum)

# show the image using psychopy
win = visual.Window(units='pix', colorSpace='rgb255', color=128, fullscr=True)
imStim = visual.ImageStim(win, units='pix', image=im_unit, size=im_unit.shape[1::-1])
imStim.draw()
win.flip()
core.wait(2)
win.close()
