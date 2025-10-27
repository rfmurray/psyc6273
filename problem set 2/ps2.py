# ps2.py  Module to support solutions to problem set 2

import numpy as np

coef = {}

def init(tau=1):
    coef['ampx'] = np.random.uniform(0.2,1,3)
    coef['ampy'] = np.random.uniform(0.2,1,3)
    coef['phasex'] = np.random.uniform(0,2*np.pi,3)
    coef['phasey'] = np.random.uniform(0,2*np.pi,3)
    coef['tau'] = tau
    coef['freq'] = np.array([1, 2, 3])

def randpos(t):
    x = sum( coef['ampx'] * np.sin( (2*np.pi*coef['freq']*t/coef['tau']) - coef['phasex'] ) )
    y = sum( coef['ampy'] * np.sin( (2*np.pi*coef['freq']*t/coef['tau']) - coef['phasey'] ) )
    return np.array((x,y))
