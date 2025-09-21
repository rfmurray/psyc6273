# chapter04_solutions_problem3.py

import random
from psychopy import visual, sound, core
from psychopy.hardware import keyboard

ntrials = 40
stimdur = 0.5

win = visual.Window(units='pix')
line = visual.Line(win=win, start=(-10, 0), end=(10,0), lineWidth=5, color='white')
kb = keyboard.Keyboard()
timer = core.Clock()
highbeep = sound.Sound(value=440, secs=0.1, volume=0.3)
lowbeep = sound.Sound(value=220, secs=0.1, volume=0.3)

data = []

for trial in range(ntrials):
    
    core.wait(0.5)
    
    angle = random.uniform(85, 95)
    line.ori = angle
    line.draw()
    win.flip()
    core.wait(stimdur)
    win.flip()
    
    t1 = timer.getTime()
    keys = kb.waitKeys(keyList=['1', '2', '0'])
    rt = timer.getTime() - t1
    
    if '0' in keys: break
    
    leftangle = angle <= 90
    leftresponse = '1' in keys
    correct = leftangle == leftresponse
    if correct:
        highbeep.play()
    else:
        lowbeep.play()
    
    data.append([trial, leftangle, leftresponse, rt])

win.close()
