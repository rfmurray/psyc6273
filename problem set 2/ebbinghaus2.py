# ebbinghaus2.py  Experiment to measure the strength of the Ebbinghaus illusion (version 2)

import math
import numpy as np
from psychopy import visual, event, data, core
from psychopy.hardware import keyboard

# set stimulus properties
ntrials = 100              # number of trials
radius_small = 20          # radius of smaller surrounding circles
radius_large = 40          # radius of larger surrounding circles
radius_reference = 30      # radius of reference circle
radius_pattern = 100       # radius of pattern of surrounding circles
offsetx = 200              # distance from centre of screen to reference and test circles
fgcolor = (-1,-1,-1)       # foreground colour
bgcolor = (0,0,0)          # background colour
stimdur = 1.0              # stimulus duration
filename = 'data.txt'      # data file name

# open window
win = visual.Window(size=[], units='pix', color=bgcolor, waitBlanking=True, fullscr=True)

# create keyboard and mouse objects
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False, newPos=[0,0])

# calculate stimulus coordinates
theta = 2*np.pi*np.arange(6)/6
theta.shape = 6,1
pos_centre = np.array([[0.0,0.0]])
pos_centre = np.vstack((pos_centre,radius_pattern * np.hstack((np.cos(theta),np.sin(theta)))))
pos_left = pos_centre - np.array([[offsetx,0]])
pos_right = pos_centre + np.array([[offsetx,0]])

# create arrays of radii
radii_reference = np.tile(radius_large,reps=(7,1))
radii_reference[0] = radius_reference
radii_test = np.tile(radius_small,reps=(7,1))

# create circle
circle = visual.Circle(win=win,fillColor=fgcolor)

# draw stimulus
def draw(radii_left, radii_right):
    for i in range(pos_centre.shape[0]):
        circle.setPos(pos_left[i,:])
        circle.setRadius(radii_left[i])
        circle.draw()
        circle.setPos(pos_right[i,:])
        circle.setRadius(radii_right[i])
        circle.draw()

# create staircase
stair = data.StairHandler(startVal=radius_reference, nUp=1, nDown=1, stepType='lin', stepSizes=1, nTrials=math.inf, applyInitialRule=False)

# create clock for reaction times
clock = core.Clock()

# open data file
datafile = open(filename,'a')

# run trials
for t in range(ntrials):
    
    # set test circle radius
    radius_test = stair.next()
    radii_test[0] = radius_test

    # choose test stimulus position
    test_right = np.random.choice((True,False))

    # show stimulus
    if test_right:
        draw(radii_reference, radii_test)
    else:
        draw(radii_test, radii_reference)
    win.flip()
    core.wait(stimdur)
    win.flip()
    clock.reset(newT=0)
    
    # get subject's response
    key = kb.waitKeys(keyList=['left', 'right', 'q'],waitRelease=False)[0]
    rt = clock.getTime()
    if key.name=='q':
        break
    response_right = key.name=='right'
    response_test = response_right == test_right
    
    # update staircase
    stair.addResponse(response_test)
    
    # record trial
    datafile.write(f'{t:d},{radius_reference:d},{radius_test:d},{test_right:d},{response_test:d},{rt:.3f}\n')
    
    # pause before next trial
    core.wait(0.5)

# shut down
datafile.close()
win.close()
