
import stair

# create a staircase object, i.e., an instance of the staircase class
s = stair.Stair(up=1, down=2, levels=[ x for x in range(0,51,5) ])

# show the current state of the object
s

# get the current stimulus level
s.stim()

# suppose that we ran a trial with this stimulus level, and the observer
# gave the correct response; now we report to the object that the
# response was correct (i.e., True)
s.response(True)

# show the current state again; note that it has changed
s

# do it again: get the current stimulus level; now report an incorrect
# response (i.e., False); show the current state again
s.stim()
s.response(False)
s

# and again; note that the state changes again
s.stim()
s.response(True)
s
