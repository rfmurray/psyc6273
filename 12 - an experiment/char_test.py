import sys
from psychopy import visual

sys.path.append('tools')
from characterize import CharLum

win = visual.Window(units='pix')
char = CharLum(win=win, photsim=True, filename='tools/charlum.pkl')
char.test_measure()
win.close()

char.test_plot()
