import sys
from psychopy import visual

sys.path.append('tools')
from characterize import CharLum

win = visual.Window(units='pix')
char = CharLum(win=win, photsim=True, filename='tools/charlum.pkl')
char.measure()
win.close()

char.fit()
print(char)
char.save()
char.plot()
