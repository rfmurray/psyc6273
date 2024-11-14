# problemset1_solution.py  The Poggendorff illusion

import math, random
from psychopy import visual, event, core, sound
from psychopy.hardware import keyboard

ntrials = 40                   # number of trials
angles = [-60, 30, 0, 30, 60]   # line angles
widths = [50, 100, 150]         # occluder widths
line_length = 250               # length of line
mousek = 5                      # scale factor for mouse position

# open window and create objects
win = visual.Window(units='pix', fullscr=True)
line1 = visual.Line(win=win, lineWidth=5, start=(0,0), lineColor='white')
line2 = visual.Line(win=win, lineWidth=5, start=(0,0), lineColor='white')
rect = visual.Rect(win=win, fillColor='lightgray')
timer = core.Clock()
beep = sound.Sound(value=440, secs=0.1, volume=1)
mouse = event.Mouse(visible=False)
kb = keyboard.Keyboard()

# write header
filename = 'data.txt'
with open(filename, 'a') as f:
    f.write(f'# trial,angle,width,yoffset,rt\n')

# run trials
for trial in range(ntrials):
    
    # choose line angle and occluder width
    angle = random.choice(angles)
    width = random.choice(widths)
    
    # set line endpoints
    linex = line_length * math.cos(math.radians(angle))
    liney = line_length * math.sin(math.radians(angle))
    line1.end = (-linex, -liney)
    line2.end = (linex, liney)
    
    # set occluder width
    rect.size = (width, 500)
    
    # randomize mouse position
    inity = random.choice([-200, 200])
    mouse.setPos((0, mousek*inity))
    
    t1 = timer.getTime()
    while True:
        
        # check mouse and set line position
        mousex, mousey = mouse.getPos()
        yoffset = mousey/mousek
        line2.pos = (0, yoffset)
        
        # show stimuli
        line1.draw()
        line2.draw()
        rect.draw()
        win.flip()
        
        # check for keyboard response
        keys = kb.getKeys(['space', 'q'], waitRelease=False)
        if keys:
            rt = timer.getTime() - t1
            beep.play()
            break
    
    if 'q' in keys: break
    
    # record trial data
    with open(filename, 'a') as f:
        f.write(f'{trial},{angle},{width},{yoffset:.3f},{rt:.3f}\n')
    
    win.flip()
    core.wait(1)

win.close()
