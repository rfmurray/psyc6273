
import random
from psychopy import visual, core

win = visual.Window(units='pix')

wavelength = 20  # pixels
grating = visual.GratingStim(win=win, mask='gauss', size=100, pos=[0,0], sf=1/wavelength)

for t in range(10):
    grating.ori = random.uniform(-10,10)  # orientation in degrees
    grating.pos = random.uniform(-200, 200), random.uniform(-200, 200)  # (x, y) position in pixels
    grating.draw()
    win.flip()
    core.wait(0.5)

win.close()
