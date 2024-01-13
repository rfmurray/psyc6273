# ebbinghaus1.py  Experiment to measure the strength of the Ebbinghaus illusion (version 1)

import math
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

# create reference and test circles
circle_reference = visual.Circle(win=win,radius=radius_reference,pos=(-offsetx,0),fillColor=fgcolor)
circle_test      = visual.Circle(win=win,radius=radius_reference,pos=( offsetx,0),fillColor=fgcolor)
circles = [circle_reference, circle_test]

# create surrounding circles
for i in range(6):

    # find (x,y) position    
    theta = 2*math.pi*(i/6)
    dx = radius_pattern*math.cos(theta)
    dy = radius_pattern*math.sin(theta)
    
    # create circles
    circle_large = visual.Circle(win=win,radius=radius_large,pos=(-offsetx+dx,dy),fillColor=fgcolor)
    circle_small = visual.Circle(win=win,radius=radius_small,pos=( offsetx+dx,dy),fillColor=fgcolor)
    circles.extend([circle_large, circle_small])

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
    circle_test.setRadius(radius_test)

    # show stimulus
    for c in circles:
        c.draw()
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
    
    # update staircase
    stair.addResponse(response_right)
    
    # record trial
    datafile.write(f'{t:d},{radius_reference:d},{radius_test:d},{response_right:d},{rt:.3f}\n')
    
    # pause before next trial
    core.wait(0.5)

# shut down
datafile.close()
win.close()
