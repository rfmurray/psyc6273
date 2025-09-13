# chapter04_code_section4p6.py

from psychopy import visual, core
import move

win = visual.Window(units='pix')
targetdot = visual.Circle(win=win, fillColor='red', radius=25)

timer = core.Clock()
time = 0

move.init()

while time < 10:
    time = timer.getTime()
    targetx, targety = move.getPos(time)
    targetdot.setPos((targetx, targety))
    targetdot.draw()
    win.flip()

win.close()
