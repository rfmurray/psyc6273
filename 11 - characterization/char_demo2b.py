from psychopy import visual
import charlib

# open main window
win = visual.Window(units='pix', colorSpace='rgb255', color=128, fullscr=True)

# make measurements to test characterization fit
char = charlib.CharLum(win=win, fname='charlum.pkl', realphot=False)
results = char.test()
win.close()

# show results of test
char.testplot(*results)
