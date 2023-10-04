# pong.py  PsychoPy demonstration: pong

from psychopy import visual, event
from psychopy.hardware import keyboard

# open a full-screen window
win = visual.Window(size=[], units='pix', color=(-1,-1,-1), fullscr=True)
winLim = win.size/4

# create a keyboard object
kb = keyboard.Keyboard()

# get currently pressed keys
def keysDown(keylist=[]):
    keys = kb.getKeys(keylist, waitRelease=False, clear=False)
    kb.getKeys(keylist, waitRelease=True, clear=True)
    return [ k.name for k in keys ]

# create rectangle objects for paddles
padoffset = 0.8 * winLim[0]
padheight = 100
pad = [ visual.Rect(win, width=20, height=padheight, fillColor=(1,1,1), lineColor=None, pos=(-padoffset,0)),
        visual.Rect(win, width=20, height=padheight, fillColor=(1,1,1), lineColor=None, pos=( padoffset,0)) ]
padKeys = [ ('w','s'), ('u','j') ]

# create a circle object for the ball
ball = visual.Circle(win, radius=10, fillColor=(1,1,1), lineColor=None, pos=(0,0) )
ballVec = [ 2, 2 ]
ballAccel = 1.05
ballMid = True

# create a mouse object
mouse = event.Mouse(visible=False)

# loop indefinitely
f = 0
while True:
    f += 1

    # check keyboard
    keys = keysDown()
    if 'q' in keys:
        break

    # update and draw paddles
    for i in range(2):
        x, y = pad[i].pos
        if padKeys[i][0] in keys: y += 10
        if padKeys[i][1] in keys: y -= 10
        y = max(min(y,winLim[1]),-winLim[1])
        pad[i].setPos((x,y))
        pad[i].draw()
    
    # update and draw ball
    ballPos = ball.pos
    ballPos[0] += ballVec[0]
    ballPos[1] += ballVec[1]
    for i in range(2):
        if ballPos[i] < -winLim[i]:
            ballPos[i] = -winLim[i]
            ballVec[i] = -ballVec[i]
        elif ballPos[i] > winLim[i]:
            ballPos[i] = winLim[i]
            ballVec[i] = -ballVec[i]
    ball.setPos(ballPos)
    ball.draw()
    
    # check for collision between ball and paddle
    if ballVec[0] < 0 and ballPos[0] < -padoffset+10 and abs( ballPos[1] - pad[0].pos[1] ) < padheight/2:
        ballVec[0] = -ballVec[0]
    elif ballVec[0] > 0 and ballPos[0] > padoffset-10 and abs( ballPos[1] - pad[1].pos[1] ) < padheight/2:
        ballVec[0] = -ballVec[0]
    
    # see if we need to change the ball colour
    if ballMid:
        if ballPos[0] < -padoffset or ballPos[0] > padoffset:
            ballMid = False
            ball.setColor((1,-1,-1))
    else:
        if ballPos[0] > -padoffset and ballPos[0] < padoffset:
            ballMid = True
            ball.setColor((1,1,1))

    # switch front and back buffers
    win.flip()

    # speed up ball    
    if f % 60 == 0:
        ballVec[0] *= ballAccel
        ballVec[1] *= ballAccel

# close the full-screen window
win.close()
