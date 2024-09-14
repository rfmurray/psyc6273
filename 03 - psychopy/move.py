# move.py

import numpy as np

coef = {}

def init(amp=100, tau=10):
    coef['ampx'] = np.random.uniform(0.2,1,3)
    coef['ampy'] = np.random.uniform(0.2,1,3)
    coef['phasex'] = np.random.uniform(0,2*np.pi,3)
    coef['phasey'] = np.random.uniform(0,2*np.pi,3)
    coef['amp'] = amp
    coef['tau'] = tau
    coef['freq'] = np.array([1, 2, 3])

def getPos(t):
    x = coef['amp'] * sum( coef['ampx'] * np.sin( (2*np.pi*coef['freq']*t/coef['tau']) - coef['phasex'] ) )
    y = coef['amp'] * sum( coef['ampy'] * np.sin( (2*np.pi*coef['freq']*t/coef['tau']) - coef['phasey'] ) )
    return x, y
