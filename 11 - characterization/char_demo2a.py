from psychopy import visual
import charlib

# open main window
win = visual.Window(units='pix', colorSpace='rgb255', color=128, fullscr=True)

# make characterization measurements
char = charlib.CharLum(win=win, realphot=False)
char.measure()
win.close()

# fit and plot measurements
char.fit()
char.plot()

# save characterization measurements and fit
char.save('charlum.pkl')
