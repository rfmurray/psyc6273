import numpy as np
from psychopy import visual
from psychopy.hardware import keyboard

win = visual.Window(units='pix')
kb = keyboard.Keyboard()  # press any key to end the demo

# we'll show a greyscale n x n pixel image
n = 200
im = visual.ImageStim(win=win, size=(n,n))

# to anticipate, the demos below show that
# - for a 2D array with size (n,n),  -1 is black and 1 is white
# - for a 3D array with size (n,n,3), 0 is black and 1 is white
# - we cannot show a 3D array with size (n,n,1)

# first, we show a 2D array with size (n,n). the array has value -1 in the
# leftmost column, and increases linearly to +1 in the rightmost column. we show
# this array as an image on the left side of the window. the resulting image is black
# at the left, and ramps smoothly to white at the right.
mat = np.tile(np.linspace(-1,1,n),(n,1))
im.pos = (-(n+20),0)
im.image = mat
im.draw()

# next, we make the array 3D, with size (n,n,1), and show it in the centre of the
# window. this doesn't work, and much of the resulting image is random pixels.
mat.shape = (n,n,1)
im.pos = (0,0)
im.image = mat
im.draw()

# finally, we replicate the array three times to have size (n,n,3), and show it
# on the right side of the window. this image is black in its left half, where the
# array values range from -1 to 0. in its right half, where values range from 0 to 1,
# it smoothly ramps from black to white.
mat = np.tile(mat,(1,1,3))
im.pos = (n+20,0)
im.image = mat
im.draw()

win.flip()
kb.waitKeys(waitRelease=False)
win.close()
