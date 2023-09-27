# psychopy_demo2a.py  PsychoPy demonstration: orientation discrimination

import random

# import modules from psychopy package
from psychopy import visual, event, core

# open a full-screen window
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create a sine wave grating object
grating = visual.GratingStim(win=win, mask='gauss', size=250, pos=[0,0], sf=1/40.0)

# run trials
for t in range(100):

    # show grating at a near-vertical but random orientation
    angle = random.uniform(-10,10)
    grating.ori = angle
    grating.draw()
    win.flip()
    core.wait(0.5)
    win.flip()

    # wait for a keypress response
    keys = event.waitKeys(keyList = ['lshift', 'rshift', 'q'])
    if 'q' in keys:
        break

    # pause before next trial
    core.wait(0.5)

# close the full-screen window
win.close()
