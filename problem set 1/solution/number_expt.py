# number_expt.py  Solution to problem set 1: number judgements

import random
import numpy as np
from psychopy import visual, sound, event, core
from psychopy.hardware import keyboard

# set task parameters
ntrials = 100   # number of trials
stimdur = 0.5   # stimulus duration (seconds)
refnum = 30     # number of reference dots
testrange = (20, 40, 2)  # range of number of test dots
stimsize = 200  # size of stimulus square (pixels)
pausedur = 0.5  # pause duration (seconds)
filename = 'data.txt'

# create window, fixation point, dot
win = visual.Window(units='pix')
fixpt = visual.Circle(win=win, radius=2)
dot = visual.Circle(win=win, radius=5)

# create keyboard, mouse, timer, and sound objects
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False)
timer = core.Clock()

# draw one stimulus
def drawdots(count, left):
    xy = np.random.randint(low=-stimsize/2, high=(stimsize/2)+1, size=(count,2)).astype(np.float64)
    xy[:,0] += 0.75*stimsize*(-1 if left else 1)
    for i in range(count):
        dot.setPos(xy[i,:])
        dot.draw()

# write header to data file
with open(filename, 'a') as f:
    f.write('\n#trial,testpos,refnum,testnum,respleft,resptest,rt\n')

# run trials
for trial in range(ntrials):

    # choose stimulus properties
    testleft = random.choice([True, False])
    testnum = random.randrange(start=testrange[0], stop=testrange[1]+1, step=testrange[2])

    # draw stimulus
    drawdots(count=refnum, left=not testleft)
    drawdots(count=testnum, left=testleft)
    fixpt.draw()
    win.flip()
    core.wait(stimdur)

    # clear stimulus
    fixpt.draw()
    win.flip()

    # get observer's response
    timer.reset()
    key = kb.waitKeys(keyList=['1','2','q'], waitRelease=False)[0]
    rt = timer.getTime()

    # process response
    if key=='q': break
    respleft = key == '1'            # chose left side?
    resptest = respleft == testleft  # chose test stimulus?

    # write line to data file
    with open(filename, 'a') as f:
        f.write(f'{trial+1},{1 if testleft else 2},{refnum},{testnum},{1 if respleft else 2},{int(resptest)},{rt:.3f}\n')

    # pause before next trial
    core.wait(pausedur)

win.close()
