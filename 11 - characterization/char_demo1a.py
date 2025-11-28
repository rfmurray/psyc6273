import glob, pickle
import numpy as np
from psychopy import visual, core, event
from psychopy.hardware import minolta

# choose whether to use a real or simulated photometer
realphot = False

# define the gamma function that we'll fit to luminance measurements
def gamma(x, k, g0, gamma_exp, delta):
    
    low = x<g0
    high = x>255
    ok = ~(low|high)
    
    y = np.empty(x.shape)
    y[low] = delta
    y[high] = k+delta
    y[ok] = k * np.power((x[ok]-g0)/(255-g0), gamma_exp) + delta
    
    return y

# if we're using a real photometer, then open the connection to it
if realphot:
    port = glob.glob('/dev/tty.usbserial*')[0]
    phot = minolta.LS100(port)

# choose the greylevels 0-255 that we'll show
grey = np.linspace(0, 255, 10, dtype=np.uint8)
grey = np.random.permutation(grey)
lum = np.full(grey.shape, np.nan)

# open the main window and define the test rectangle
win = visual.Window(units='pix', colorSpace='rgb255', color=128, fullscr=True)
rect = visual.Rect(win=win, width=400, height=400, units='pix', colorSpace='rgb255')

#  show the rectangle so that the user can aim the photometer
rect.fillColor = 200
rect.draw()
win.flip()
if realphot:
    event.waitKeys()

# step through greylevels
for i, g in enumerate(grey):
    
    # show the greylevel
    rect.fillColor = g
    rect.draw()
    win.flip()
    
    # measure the luminance (with a real or simulated photometer)
    if realphot:
        lum[i] = phot.getLum()
    else:
        lum[i] = gamma(g, 95, 10, 2.2, 5)
        core.wait(0.5)

# close the window and photometer
win.close()
if realphot:
    del phot

# save the characterization data
with open('char_measurements.pkl', 'wb') as f:
    pickle.dump(grey, f)
    pickle.dump(lum, f)
