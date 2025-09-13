# chapter04_code_section4p7.py

from psychopy import visual, event
from psychopy.hardware import keyboard

win = visual.Window(units='pix')
line = visual.Line(win=win, start=(-10, 0), end=(10,0),
    lineWidth=5, color='white')

kb = keyboard.Keyboard()
mouse = event.Mouse(visible=False, newPos=[0,0])

while True:    

    mousex, mousey = mouse.getPos()
    line.setPos((mousex, mousey))
    line.ori = 0
    line.draw()
    line.ori = 90
    line.draw()
    win.flip()
    
    keys = kb.getKeys(keyList=['q'], waitRelease=False)
    if len(keys)>0: break

win.close()
