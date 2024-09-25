# random_walk.py

import random, math
from psychopy import visual, event, sound
from psychopy.hardware import keyboard

# open window and create objects
win = visual.Window(units='pix', fullscr=True)
mouse = event.Mouse(visible=False)
kb = keyboard.Keyboard()
beep = sound.Sound(value=220, secs=0.1, volume=1)

# initialize lists of dots
list1 = []
list2 = []

while True:

    # maybe add a type 1 dot
    if random.uniform(0, 1) < 0.005:
        dot = visual.Circle(win=win, pos=(-50,0), radius=20, color='red', lineColor='black', lineWidth=2)
        list1.append(dot)
    
    # maybe add a type 2 dot
    if random.uniform(0, 1) < 0.005:
        dot = visual.Circle(win=win, pos=(50,0), radius=20, color='yellow', lineColor='black', lineWidth=2)
        list2.append(dot)
    
    # process type 1 dots
    for dot in list1:
        dot.pos = (dot.pos[0] + random.gauss(0,2), dot.pos[1] + random.gauss(0,2))
        dot.draw()
    
    # process type 2 dots
    for dot in list2:
        dot.pos = (dot.pos[0] + random.gauss(0,2), dot.pos[1] + random.gauss(0,2))
        dot.draw()
    
    # remove dots that have collided
    for dot1 in list1:
        for dot2 in list2:
            dx = dot1.pos[0] - dot2.pos[0]
            dy = dot1.pos[1] - dot2.pos[1]
            dist = math.sqrt(dx**2 + dy**2)
            if dist <= 0.9*(dot1.radius + dot2.radius):
                beep.play()
                list1.remove(dot1)
                list2.remove(dot2)
                
#                dot1.name = 'delete'
#                dot2.name = 'delete'
    
#    list1 = [dot for dot in list1 if dot.name != 'delete']
#    list2 = [dot for dot in list2 if dot.name != 'delete']
    
    win.flip()
    
    # check for quit key
    keys = kb.getKeys(keyList='q')
    if keys: break

win.close()
