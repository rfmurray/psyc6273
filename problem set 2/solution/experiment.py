import random
import numpy as np
from psychopy import visual, core, event
from psychopy.hardware import keyboard
import tools

ntrials = 200           # number of trials
angle = 5               # gabor orientation left or right of vertical (degrees)
wavelength = 16         # gabor wavelength (pixels)
scale = 10              # gabor scale constant (pixels)
noisesd = 0.20          # noise standard deviation
contrasts = [0.02, 0.04, 0.06, 0.08, 0.16]  # signal contrasts
imsize = 128            # image size (pixels)
predur = 0.5            # inter-trial interval
stimdur = 0.5           # stimulus duration
fname = 'data.txt'

# create psychopy objects
win = visual.Window(units='pix', fullscr=True)
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False)
timer = core.Clock()
image = visual.ImageStim(win=win, size=(imsize,imsize))

# create gabors
gabor_right = tools.gabor(angle=-angle, wavelength=wavelength, scale=scale, size=imsize)
gabor_left  = tools.gabor(angle= angle, wavelength=wavelength, scale=scale, size=imsize)

# write header
with open(fname, 'a') as f:
    f.write('trial,contrast,angle,stimleft,respleft,correct,rt\n')

for trial in range(ntrials):

    # choose stimulus properties
    stimleft = random.choice([True, False])
    stimangle = angle if stimleft else -angle
    contrast = random.choice(contrasts)
    
    # create stimulus
    gabor = gabor_left if stimleft else gabor_right
    noise = np.random.normal(scale=noisesd, size=gabor.shape)
    stimulus = contrast * gabor + noise
    image.setImage(np.flipud(stimulus))

    # show stimulus
    core.wait(predur)
    image.draw()
    win.flip()
    core.wait(stimdur)
    win.flip()
    
    # get subject's response
    t1 = timer.getTime()
    keys = kb.waitKeys(keyList=['f', 'j', 'escape'])
    rt = timer.getTime() - t1
    win.flip()
    
    # process response
    if 'escape' in keys: break
    respleft = 'f' in keys
    correct = respleft == stimleft
    tools.beep(freq = 880 if correct else 440)
    
    # save data from this trial
    with open(fname, 'a') as f:
        f.write(f'{trial+1},{contrast:.4f},{stimangle:.2f},{int(stimleft)},{int(respleft)},{int(correct)},{rt:.4f}\n')

win.close()
