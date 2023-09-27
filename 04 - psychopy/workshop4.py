# workshop4.py  Lecture 4 workshop problems

# Write Python scripts that use the PsychoPy package to solve the following
# problems. These are more substantial than the workshop problems for previous
# lectures, so you may want to write the solutions in separate .py files.

# 1. Write a script that tests an observer's ability to centre a small circle
# in large circle. The large circle appears at a fixed location on the
# the screen. The small circle tracks the position of the mouse cursor.
# When the user clicks the mouse, the trial ends, and the program prints
# the difference in pixels between the centre positions of the two
# circles.

# 2. If we view a stimulus moving in one direction for ten or twenty seconds,
# then afterwards a stationary stimulus at the same retinal location appears
# to move in the opposite direction. This is called a motion aftereffect.
# 
# Write a script to demonstrate this effect, as follows. Show a sine wave
# grating, and redraw it on every frame, with a gradually increasing value
# of the 'phase' property that controls the position of the bright and dark
# bars of the grating. This will cause the bars to move. When the user
# presses a key, stop the motion, i.e., stop increasing the phase. Then
# the user can see whether they perceive a motion aftereffect.
# 
# Optionally, if the user presses a key again, then start the motion again.
# Allow the user to toggle between a moving and stationary grating, to
# view the motion aftereffect repeatedly.
# 
# Also provide some way for the user to exit the program, e.g., click the
# mouse or press Q.
