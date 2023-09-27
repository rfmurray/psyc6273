# psychopy_demo2b.py  PsychoPy demonstration: an almost-complete experiment

import random

# import modules from psychopy package
from psychopy import visual, event, core, sound

# set stimulus properties
anglelist = [ i for i in range(10) ]  # list of grating angles (degrees)
wavelength = 40.0           # sine wave wavelength (pixels)
stimsize = 250.0            # stimulus size (pixels)
stimdur = 0.5               # stimulus duration (seconds)
bgcolor = (0,0,0)           # background colour (range is -1 to 1)

# open a full-screen window
win = visual.Window(size=[], units='pix', color=bgcolor, waitBlanking=True, fullscr=True)

# create a sine wave grating object
grating = visual.GratingStim(win=win, mask='gauss', size=stimsize, pos=[0,0], sf=1/wavelength)

# turn off mouse cursor
mouse = event.Mouse(visible=False)

# function to show the grating
def showGrating(theta):
    grating.ori = theta  # note an unusual effect here: grating and win are
    grating.draw()       # not declared as global variables, but still we're
    win.flip()           # able to change their values and states in this
    core.wait(stimdur)   # function, because they are mutable data types
    win.flip()

# function to get a keypress response
responseCodes = { 'lshift' : False, 'rshift' : True, 'q' : None }
def getResponse():
    keys = event.waitKeys(keyList=responseCodes.keys())
    return responseCodes[keys[0]]

# function to play feedback beeps
beeps = { False : sound.Sound(value='C', octave=4, secs=0.1, volume=0.5),
          True  : sound.Sound(value='C', octave=5, secs=0.1, volume=0.3),
          'done' : sound.Sound(value='C', octave=3, secs=0.5, volume=0.5) }
def playBeep(beepkey):
    beeps[beepkey].seek(0)  # rewind to beginning of sound
    beeps[beepkey].play()   # play() doesn't pause while sound plays
    core.wait(beeps[beepkey].duration)  # so we'll add a pause

# open data file
f = open('data.txt', 'a')

# run trials
for t in range(100):

    # choose grating orientation
    angle = random.choice(anglelist)
    stimright = random.choice([True, False])
    if not stimright:
        angle = -angle

    # show grating
    showGrating(angle)

    # wait for a keypress response
    respright = getResponse()
    if respright is None:
        break

    # give auditory feedback
    correct = respright==stimright
    playBeep(correct)

    # write trial information to data file
    f.write(f'{t+1:3d},{angle:6.2f},{stimright:d},{respright:d},{correct:d}\n')

    # pause before next trial
    core.wait(0.5)

# play end beep
playBeep('done')

# close the full-screen window
win.close()

# close the data file
f.close()
