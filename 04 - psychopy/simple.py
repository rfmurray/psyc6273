# simple.py

from psychopy import visual, core

# open a full-screen window
mainwin = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create and draw a circle object
stim = visual.Circle(win=mainwin, fillColor='black', lineColor=None, radius=25)
stim.draw()

# switch front and back buffers
mainwin.flip()

# pause
core.wait(1)

# close the full-screen window
mainwin.close()
