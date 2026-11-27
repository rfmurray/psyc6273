# problemset2_solution.py  Posner cueing task

import random
from psychopy import visual, event, core, sound
from psychopy.hardware import keyboard

ntrials = 100    # number of trials
pvalid = 0.80    # probability of valid cue
cuedur = 0.10    # cue duration
isi = 0.50       # inter-stimulus interval between cue and grating
stimdur = 0.50   # stimulus duration (grating)
stimangle = 5    # stimulus orientation (degrees left or right of vertical)
iti = 1.00       # inter-trial interval
distance = 300   # distance of stimuli from fixation point

# open window and create objects
win = visual.Window(units='pix', fullscr=True)
fixpoint = visual.Circle(win=win, radius=5, fillColor='white')
grating = visual.GratingStim(win=win, sf=1/20, size=100, mask='gauss')
cue = visual.Rect(win=win, width=100, height=120, lineWidth=5, lineColor='white')
highbeep = sound.Sound(value=440, secs=0.1, volume=1)
lowbeep = sound.Sound(value=220, secs=0.1, volume=1)
beeps = [lowbeep, highbeep]
timer = core.Clock()
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False)

# get stimulus position from integer 1 to 4
def getxy(k):
    if k==1:
        xy = [distance, 0]
    elif k==2:
        xy = [0, distance]
    elif k==3:
        xy = [-distance, 0]
    else:
        xy = [0, -distance]
    return xy

# draw a stimulus
def drawStim(drawFixpoint=True, drawCue=False, drawGrating=False, dur=0):
    if drawFixpoint: fixpoint.draw()
    if drawCue: cue.draw()
    if drawGrating: grating.draw()
    win.flip()
    if dur>0: core.wait(dur)

# write header to file
filename = 'data.txt'
with open(filename, 'a') as f:
    f.write('trial,cueValid,cuePos,stimLeft,stimPos,responseLeft,correct,rt\n')

# pause with fixation point before starting
drawStim(dur=2)

# run trials
for trial in range(ntrials):

    # set grating orientation
    angle = random.choice([-stimangle, stimangle])
    grating.ori = angle
    stimLeft = angle < 0
    
    # set grating position
    stimPos = random.randint(1, 4)
    grating.pos = getxy(stimPos)
    
    # set cue position
    cueValid = random.uniform(0, 1) < pvalid
    if cueValid:
        cuePos = stimPos
    else:
        cues = [1, 2, 3, 4]
        cues.remove(stimPos)
        cuePos = random.choice(cues)
    cue.pos = getxy(cuePos)
    
    # show stimuli
    drawStim(drawCue=True, dur=cuedur)
    drawStim(dur=isi)
    drawStim(drawGrating=True, dur=stimdur)
    drawStim(dur=0)
    
    # get reponse
    t1 = timer.getTime()
    keys = kb.waitKeys(keyList=['1', '2', '0'], waitRelease=False)
    rt = timer.getTime() - t1
    if '0' in keys: break
    responseLeft = '1' in keys
    
    # play feedback
    correct = stimLeft == responseLeft
    beeps[correct].play()
    
    # record trial data
    with open(filename, 'a') as f:
        f.write(f'{trial+1},{cueValid:d},{cuePos},{stimLeft:d},{stimPos},{responseLeft:d},{correct:d},{rt:.3f}\n')
    
    # pause between trials
    core.wait(iti)

win.close()
