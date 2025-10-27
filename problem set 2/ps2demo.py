# ps2demo.py  Show how to use ps2 module

from psychopy import core
import ps2

# initialize random position generator
ps2.init(tau=5)
# - every time you call this function, it creates a new random trajectory,
#   which is read out by the randpos() function used below. so you should
#   call init() at the beginning of each trial in your experiment.
# - the tau argument controls the speed of the trajectory. larger values
#   create slower trajectories.

# create a timer
clock = core.Clock()
t = clock.getTime()

# loop for five seconds
while t < 5.0:
    
    # get and print coordinates
    t = clock.getTime()
    x, y = ps2.randpos(t)
    print(x, y)
    # notice that the coordinates range approximately in the range -1 to 1,
    # so depending on what units you use for your PsychoPy window (e.g., pixels),
    # you may have to multiply the coordinates by a constant to give them
    # the right scale
    
    # if you're running this code in PsychoPy's Coder view, you may have to add
    # a short pause at the end of the loop to keep the program from freezing
    core.wait(0.1)
