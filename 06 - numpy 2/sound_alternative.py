# sound_alternatives.py

# method 1: psychopy.sound

from psychopy import sound

beep = sound.Sound(value=440, secs=0.1)
beep.play()

# method 2: sounddevice

# Some people find that the above method doesn't work.
# Here's an alternative.

import sounddevice as sd
import numpy as np

T = 0.1     # sound duration in seconds
f = 440     # sound frequency in Hz (cycles/second)
fs = 44100  # sample frequency in Hz (cycles/second)
t = np.linspace(0, T, int(fs*T))  # time
wave = np.sin(2*np.pi*f*t)        # amplitude

sd.play(wave, fs)
sd.wait()

# If you're just using sound for auditory feedback, anything like
# this that works on your system is fine. If you're specifically
# studying auditory stimuli, you'll need to be more careful in
# checking that you're getting the sounds you want. You can find
# a discussion of sound in PsychoPy here:
# 
#     https://www.psychopy.org/api/sound/playback.html
