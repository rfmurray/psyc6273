# chapter04_code_section4p8.py

from psychopy import visual, sound, event, core
from psychopy.hardware import keyboard
import move

# set task parameters
ntrials = 40    # number of trials
trialdur = 10   # trial duration (seconds)

# create window, dot, and line segment
win = visual.Window(units='pix')
targetdot = visual.Circle(win=win, fillColor='red', radius=25)
line = visual.Line(win=win, start=(-10, 0), end=(10,0),
    lineWidth=5, color='white')

# create keyboard, mouse, timer, and sound objects
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False, newPos=[0,0])
timer = core.Clock()
# beep = sound.Sound(value=440, secs=0.1, volume=1)

# initialize data record
time = 0
data = []

# run trials
for trial in range(ntrials):

    timer.reset()
    time = 0
    frame = 0
    
    # create a new random trajectory for this trial
    move.init()

    # loop for one trial
    # beep.play()
    while time < trialdur:

        # draw target dot
        time = timer.getTime()
        targetx, targety = move.getPos(time)
        targetdot.setPos((targetx, targety))
        targetdot.draw()

        # draw tracking cursor
        mousex, mousey = mouse.getPos()
        line.setPos((mousex, mousey))
        line.ori = 0
        line.draw()
        line.ori = 90
        line.draw()
        win.flip()
    
        # record time and positions
        data.append([trial, frame, time, targetx, targety, mousex, mousey])

        # check for quit key
        keys = kb.getKeys(keyList=['q'], waitRelease=False)
        if keys: break

        # update frame number
        frame += 1
        
    # check for quit key
    if keys: break

    # show blank screen and pause briefly before starting next trial
    win.flip()
    core.wait(1)
    
win.close()
