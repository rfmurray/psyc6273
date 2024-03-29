# psychopy_demo1.py  PsychoPy demonstration: mouse tracking

# import modules from psychopy package
from psychopy import visual, event

# open a full-screen window
mainwin = visual.Window(size=[], units='pix', waitBlanking=True, fullscr=True)

# create a circle object
stim = visual.Circle(win=mainwin, fillColor='black', lineColor=None, radius=25)

# create a mouse object
# - this shouldn't matter, but I've found that if you create the mouse
#   before creating the circle object, the mouse cursor stays visible.
mouse = event.Mouse(visible=False, newPos=[0,0])

# loop indefinitely
while True:

    # get mouse position
    x, y = mouse.getPos()

    # adjust mouse position
    # - may need to use and adjust this for your own operating system
    # x += mainwin.size[0]/4
    # y += mainwin.size[1]/4

    # set circle position and draw it
    stim.setPos((x,y))
    stim.draw()

    # switch front and back buffers
    mainwin.flip()

    # check for mouse click
    if mouse.getPressed()[0]:
        break

    # check for keypress
    keys = event.getKeys()
    if 'q' in keys:
        break

# close the full-screen window
mainwin.close()
