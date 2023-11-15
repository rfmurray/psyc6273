import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

class CalLum:
    
    def __init__(self, fname=''):
        super(CalLum, self).__init__()
        self.grey = None   # greylevels (rgb) from calibration
        self.lum = None    # luminances from calibration
        self.popt = None   # fitted gamma function parameters
        if fname:
            self.load(fname)
    
    def fit(self, grey=None, lum=None):

        if not grey is None:
            self.grey = grey

        if not lum is None:
            self.lum = lum

        p0 = [self.lum.max()-self.lum.min(), 0, 2, self.lum.min()]
        self.popt, _ = optimize.curve_fit(self.gammafn, self.grey, self.lum, p0=p0)
    
    def plot(self):
        if not self.popt is None:
            xx = np.arange(256)
            plt.plot(xx, self.grey2lum(xx), 'r-', label='fit')
        plt.plot(self.grey, self.lum, 'bo', label='measurements')
        plt.xlabel('greylevel')
        plt.ylabel('luminance')
        plt.legend(loc='upper left')
        plt.show()
    
    def lum2grey(self, lum, roundit=True):
        g = self.gammainv(lum,*self.popt)
        return g.round() if roundit else g
    
    def grey2lum(self, grey):
        return self.gammafn(grey,*self.popt)
    
    def gammafn(self, x, k, g0, gamma, delta):
        
        low = x<g0
        high = x>255
        ok = ~(low|high)
        
        y = np.empty(x.shape)
        y[low] = delta
        y[high] = k+delta
        y[ok] = k * np.power((x[ok]-g0)/(255-g0), gamma) + delta
        
        return y
    
    def gammainv(self, y, k, g0, gamma, delta):
        
        low = y<delta
        high = y>k+delta
        ok = ~(low|high)
        
        x = np.empty(y.shape)
        x[low] = g0
        x[high] = 255
        x[ok] = (255-g0) * np.power((y[ok]-delta)/k, 1/gamma) + g0
        
        return x
    
    def save(self, fname='cal.pickle'):
        with open(fname, 'wb') as f:
            pickle.dump(self.grey, f)
            pickle.dump(self.lum, f)
            pickle.dump(self.popt, f)
    
    def load(self, fname='cal.pickle'):
        with open(fname, 'rb') as f:
            self.grey = pickle.load(f)
            self.lum = pickle.load(f)
            self.popt = pickle.load(f)
    
    def __repr__(self):
        if not self.popt is None:
            return f'k = {self.popt[0]:.2f}, g0 = {self.popt[1]:.2f}, gamma = {self.popt[2]:.2f}, delta = {self.popt[3]:.2f}'
        else:
            return 'no fit available'
