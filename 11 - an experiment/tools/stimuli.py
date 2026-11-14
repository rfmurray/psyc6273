import numpy as np
import sounddevice as sd

def gabor(wavelength=16, angle=0, phase=0, scale=10, size=128):
    "create a gabor stimulus"
    
    # create coordinate matrices
    xy = np.arange(0, size) - np.floor(size/2)
    [xmat0, ymat0] = np.meshgrid(xy, -xy)
    
    # rotate coordinate matrices
    angle = angle * np.pi/180
    xmat = np.cos(angle) * xmat0 + np.sin(angle) * ymat0
    
    # create product of sinusoid and gaussian window
    cosmat = np.cos((2*np.pi*xmat/wavelength)-phase)
    windowmat = np.exp(-(xmat0**2 + ymat0**2)/(2*(scale**2)))
    return cosmat * windowmat

def beep(freq=440, dur=0.1, amp=1, wait=False):
    "play a sinusoidal beep"
    fs = 44100  # sample frequency in Hz
    t = np.linspace(0, dur, int(fs*dur))
    wave = amp * np.sin(2*np.pi*freq*t)
    sd.play(wave, fs)
    if wait: sd.wait()
