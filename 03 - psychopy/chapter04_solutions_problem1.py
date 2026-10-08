# chapter04_solutions_problem1.py

import random
from psychopy import visual, sound, core
from psychopy.hardware import keyboard

ntrials = 40

win = visual.Window(units='pix')
dot = visual.Circle(win=win, fillColor='white', radius=25)
kb = keyboard.Keyboard()
timer = core.Clock()
beep = sound.Sound(value=440, secs=0.1, volume=0.3)

data = []

for trial in range(ntrials):

    prepause = random.uniform(2, 4)
    core.wait(prepause)
    
    dot.draw()
    win.flip()
    
    t1 = timer.getTime()
    keys = kb.waitKeys(keyList=['space', 'q'])
    rt = timer.getTime() - t1
    beep.play()
    win.flip()

    if 'q' in keys: break
    
    data.append([trial, prepause, rt])

win.close()
