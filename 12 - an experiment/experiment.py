import sys, random, datetime
import numpy as np
from psychopy import visual, core, event
from psychopy.hardware import keyboard

# sys.path.append('tools')
from stimuli import gabor, beep
from stair import StairHolder, Stair
from characterize import CharLum
from util import getID

ntrials = 200           # number of trials
angle = 5               # gabor orientation left or right of vertical (degrees)
wavelength = 16         # gabor wavelength (pixels)
scale = 10              # gabor scale constant (pixels)
noisesd = 0.20          # noise standard deviation
contrasts = 0.05 * (1.2**np.array(range(10)))  # signal contrasts
bglum = 50              # background luminance
imsize = 128            # image size (pixels)
predur = 0.5            # inter-trial interval
stimdur = 0.5           # stimulus duration

# get participant ID
subject = getID()
fname = f'data/data_{subject}.txt'

# load display characterization data
char = CharLum('tools/charlum.pkl')

# create psychopy objects
win = visual.Window(units='pix', color=char.lum2grey(bglum), fullscr=True)
kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False)
pausemsg = visual.TextStim(win=win, text='\n\n\n\n\nPress any key to begin.', height=50, color=0.8, wrapWidth=1000)

# create gabors
gabor_right = np.flipud(gabor(angle=-angle, wavelength=wavelength, scale=scale, size=imsize))
gabor_left  = np.flipud(gabor(angle= angle, wavelength=wavelength, scale=scale, size=imsize))
image = visual.ImageStim(win=win, size=(imsize,imsize))

# create staircases
stair = StairHolder()
stair.add(Stair(up=1, down=2, levels=contrasts))
stair.add(Stair(up=1, down=3, levels=contrasts))

# write data file header
with open(fname, 'a') as f:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f'\n# {timestamp}\n')
    f.write('trial,contrast,angle,stimleft,respleft,correct,rt\n')

# show stimuli and pause before starting
stim_left = char.lum2grey(bglum*(1+0.5*gabor_left))
image.setImage(stim_left)
image.pos = (-imsize,0)
image.draw()
stim_right = char.lum2grey(bglum*(1+0.5*gabor_right))
image.setImage(stim_right)
image.pos = (imsize,0)
image.draw()
image.pos = (0,0)
pausemsg.draw()
win.flip()
kb.waitKeys()
win.flip()
core.wait(1)

for trial in range(ntrials):

    # choose stimulus properties
    stimleft = random.choice([True, False])
    stimangle = angle if stimleft else -angle
    contrast = stair.stim()
    
    # create stimulus
    gabor = gabor_left if stimleft else gabor_right
    noise = np.random.normal(scale=noisesd, size=gabor.shape)
    stimulus = bglum*(1 + contrast * gabor + noise)
    stimulus = char.lum2grey(stimulus)
    image.setImage(stimulus)

    # show stimulus
    core.wait(predur)
    image.draw()
    win.flip()
    core.wait(stimdur)
    win.flip()
    
    # get subject's response
    kb.clock.reset()
    keys = kb.waitKeys(keyList=['f', 'j', 'escape'], waitRelease=False)
    win.flip()
    
    # process response
    if 'escape' in keys: break
    rt = keys[0].rt
    respleft = 'f' in keys
    correct = respleft == stimleft
    stair.response(correct)
    beep(freq = 880 if correct else 440)
    
    # save data from this trial
    with open(fname, 'a') as f:
        f.write(f'{trial+1},{contrast:.4f},{stimangle:.2f},{int(stimleft)},{int(respleft)},{int(correct)},{rt:.4f}\n')

    # pause every 100 trials
    if (trial+1) % 100 == 0 and (trial+1) != ntrials:
        pausemsg.text = 'Take a short break if you would like to.\n\nPress any key to continue.'
        pausemsg.draw()
        win.flip()
        kb.waitKeys()
        win.flip()

win.close()
