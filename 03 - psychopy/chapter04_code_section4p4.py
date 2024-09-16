# chapter04_code_section4p4.py

from psychopy import visual, core

win = visual.Window(units='pix')
targetdot = visual.Circle(win=win, fillColor='red', radius=25)

targetdot.draw()
win.flip()

core.wait(2)
win.close()
