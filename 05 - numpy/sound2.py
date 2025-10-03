import sounddevice as sd
import numpy as np

def beep(freq=440, dur=0.1, amp=1, wait=False):
    fs = 44100  # sample frequency in Hz
    t = np.linspace(0, dur, int(fs*dur))
    wave = amp * np.sin(2*np.pi*freq*t)
    sd.play(wave, fs)
    if wait:
        sd.wait()
