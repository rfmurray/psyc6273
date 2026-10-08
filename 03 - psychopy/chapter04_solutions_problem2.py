# chapter04_solutions_problem2.py

import random
from psychopy import visual, sound, core
from psychopy.hardware import keyboard

ntrials = 40

win = visual.Window(units='pix')
dot = visual.Circle(win=win, fillColor='white', radius=25)
kb = keyboard.Keyboard()
timer = core.Clock()
highbeep = sound.Sound(value=440, secs=0.1, volume=0.3)
lowbeep = sound.Sound(value=220, secs=0.1, volume=0.3)

data = []

for trial in range(ntrials):

    prepause = random.uniform(2, 4)
    core.wait(prepause)
    
    leftdot = random.uniform(0,1) < 0.5
    if leftdot:
        dot.setPos((-100,0))
    else:
        dot.setPos((100,0))
    
    dot.draw()
    win.flip()
    
    t1 = timer.getTime()
    keys = kb.waitKeys(keyList=['1', '2', '0'])
    rt = timer.getTime() - t1
    win.flip()
    
    if '0' in keys: break
    
    leftresponse = '1' in keys
    correct = leftdot == leftresponse
    if correct:
        highbeep.play()
    else:
        lowbeep.play()
    
    data.append([trial, prepause, leftdot, leftresponse, rt])

win.close()
