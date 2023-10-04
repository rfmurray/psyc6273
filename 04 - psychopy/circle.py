# circle.py  PsychoPy demonstration: circular patterns

import math
from psychopy import visual, event, core

# open a full-screen window
win = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create two dots
dot1 = visual.Circle(win, radius=25, fillColor=(1,1,1), lineColor=None, pos=(  0,0))
dot2 = visual.Circle(win, radius=25, fillColor=(1,1,1), lineColor=None, pos=(100,0))

# set orbit parameters
radius = 200
frequency = 0.5

# create a mouse object
# - this shouldn't matter, but I've found that if you create the mouse
#   before creating the circle object, the mouse cursor stays visible.
mouse = event.Mouse(visible=False)

# create a clock
clock = core.Clock()

# loop indefinitely
while True:
    
    # set position of dot 2
    theta = 2 * math.pi * frequency * clock.getTime()
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    dot2.setPos((x,y))
    
    # draw dots
    dot1.draw()
    dot2.draw()
    win.flip()

    # check mouse
    if mouse.getPressed()[0]:
        break
    
# close the full-screen window
win.close()
