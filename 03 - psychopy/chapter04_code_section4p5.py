# chapter04_code_section4p5.py

import math
from psychopy import visual, core

win = visual.Window(units='pix')
targetdot = visual.Circle(win=win, fillColor='red', radius=25)

timer = core.Clock()
time = 0

while time < 10:
    time = timer.getTime()
    targetx = 100 * math.sin(3*time)
    targety = 0
    targetdot.setPos((targetx, targety))
    targetdot.draw()
    win.flip()

win.close()
