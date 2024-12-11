import glob, pickle, random
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from psychopy import visual, core, event
from psychopy.hardware import minolta

class CharLum:
    
    def __init__(self, win=None, fname='', realphot=True):
        super(CharLum, self).__init__()
        self.grey = None   # greylevels (rgb255) used for characterization
        self.lum = None    # luminance characterization measurements
        self.param = None  # fitted gamma function parameters
        self.phot = []     # photometer object
        self.realphot = realphot  # flag whether to use real or simulated photometer
        self.win = win     # window to use for characterization measurements
        self.rect = None if (self.win is None) else visual.Rect(self.win, width=400, height=400, units='pix', colorSpace='rgb255')  # rectangle to use for characterization measurements
        if fname: self.load(fname)
    
    def photopen(self, port=None):
        'open connection to photometer'
        if self.realphot:
            if port is None: port = glob.glob('/dev/tty.usbserial*')[0]
            self.phot = minolta.LS100(port)
    
    def photclose(self):
        'close connection to photometer'
        if self.realphot:
            del self.phot
            self.phot = []
    
    def getlum(self, grey=None):
        'measure luminance of test patch'
        return self.phot.getLum() if self.realphot else self.simlum(grey)
    
    def simlum(self, grey):
        'calculate a simulated luminance measurement'
        return 5.0 + 100.0 * (grey/255.0)**2.2 + random.gauss(mu=0, sigma=1)
    
    def showsquare(self, grey=255, waitkey=False):
        'show square test patch'
        if self.win is None: return
        self.rect.fillColor = grey
        self.rect.draw()
        self.win.flip()
        if waitkey:
            event.waitKeys()
    
    def measure(self):
        'measure luminance of a series of greylevels'
    
        self.photopen()
        
        self.grey = np.linspace(0, 255, 10, dtype=np.uint8)
        self.grey = np.random.permutation(self.grey)
        self.lum = np.full(self.grey.shape, np.nan)
        
        self.showsquare(grey=200, waitkey=self.realphot)
        
        for i, g in enumerate(self.grey):
            self.showsquare(grey=g)
            core.wait(0.5)
            self.lum[i] = self.getlum(grey=g)
        
        k = np.argsort(self.grey)
        self.grey = self.grey[k]
        self.lum = self.lum[k]
        
        self.photclose()
    
    def fit(self):
        'fit gamma function to characterization data'
        p0 = [self.lum.max()-self.lum.min(), 0, 2.2, self.lum.min()]
        bounds = (np.array((0, 0, -np.inf, 0)), np.array((np.inf, 255, np.inf, np.inf)))
        self.param, _ = optimize.curve_fit(self.gammafn, self.grey, self.lum, p0=p0, bounds=bounds)
    
    def plot(self):
        'plot characterization data and fitted gamma function'
        if not self.param is None:
            xx = np.arange(256)
            plt.plot(xx, self.grey2lum(xx), 'r-', label='fit')
        plt.plot(self.grey, self.lum, 'bo', label='measurements')
        plt.xlabel('greylevel', fontsize=18)
        plt.ylabel('luminance (cd/m$^2$)', fontsize=18)
        plt.legend(loc='upper left', frameon=False)
        plt.show()
    
    def test(self):
        'test lum2grey and grey2lum mappings with fitted parameters'
        
        self.photopen()
        self.showsquare(grey=200, waitkey=self.realphot)
        
        # check lum2grey mapping
        lum1 = np.linspace(self.param[3], self.param[0]+self.param[3], 10)
        lum1 = np.random.permutation(lum1)
        grey1 = self.lum2grey(lum1)
        lum_meas1 = np.full(lum1.shape, np.nan)
        for i, g in enumerate(grey1):
            self.showsquare(grey=g)
            core.wait(0.5)
            lum_meas1[i] = self.getlum(grey=g)
        
        # check grey2lum mapping
        grey2 = np.linspace(0, 255, 10).round()
        grey2 = np.random.permutation(grey2)
        lum2 = self.grey2lum(grey2)
        lum_meas2 = np.full(lum2.shape, np.nan)
        for i, g in enumerate(grey2):
            self.showsquare(grey=g)
            core.wait(0.5)
            lum_meas2[i] = self.getlum(grey=g)
        
        self.photclose()
        
        return lum1, lum_meas1, lum2, lum_meas2
    
    def testplot(self, lum1, lum_meas1, lum2, lum_meas2):
        
        # plot results
        fig, ax = plt.subplots(1, 2, figsize=(12,6))
        ax[0].plot(lum1, lum_meas1, 'ro')
        ax[1].plot(lum2, lum_meas2, 'ro')
        ax[0].set_title('test of lum2grey', fontsize=18)
        ax[1].set_title('test of grey2lum', fontsize=18)
        mx = 1.1 * np.concatenate([ lum1, lum_meas1, lum2, lum_meas2 ]).max()
        for x in ax:
            x.plot([ 0, mx ],[ 0, mx ],'k:')
            x.set_aspect('equal','box')
            x.set_xlabel('requested luminance (cd/m$^2$)', fontsize=18)
            x.set_ylabel('measured luminance (cd/m$^2$)', fontsize=18)
            x.set_xlim(0,mx)
            x.set_ylim(0,mx)
        
        plt.show()
    
    def lum2grey(self, lum, roundit=True):
        'convert luminance to greylevel'
        g = self.gammainv(lum, *self.param)
        return g.round() if roundit else g
    
    def grey2lum(self, grey):
        'convert greylevel to luminance'
        return self.gammafn(grey, *self.param)
    
    def lum2unit(self, lum):
        return self.grey2unit(self.lum2grey(lum, roundit=False))

    def unit2lum(self, unit):
        return self.grey2lum(self.unit2grey(unit))

    def grey2unit(self, g):
        return -1.0 + 2.0*(g/255.0)

    def unit2grey(self, u, roundit=True):
        g = 255.0 * (u+1.0)/2.0
        return g.round() if roundit else g

    def gammafn(self, x, k, g0, gamma, delta):
        'gamma function'
        
        low = x<g0
        high = x>255
        ok = ~(low|high)
        
        y = np.empty(x.shape)
        y[low] = delta
        y[high] = k+delta
        y[ok] = k * np.power((x[ok]-g0)/(255-g0), gamma) + delta
        
        return y
    
    def gammainv(self, y, k, g0, gamma, delta):
        'inverse gamma function'
        
        low = y<delta
        high = y>k+delta
        ok = ~(low|high)
        
        x = np.empty(y.shape)
        x[low] = g0
        x[high] = 255
        x[ok] = (255-g0) * np.power((y[ok]-delta)/k, 1/gamma) + g0
        
        return x
    
    def save(self, fname='charlum.pkl'):
        'save characterization data and fitted parameters'
        with open(fname, 'wb') as f:
            pickle.dump(self.grey, f)
            pickle.dump(self.lum, f)
            pickle.dump(self.param, f)
    
    def load(self, fname='charlum.pkl'):
        'load characterization data and fitted parameters'
        with open(fname, 'rb') as f:
            self.grey = pickle.load(f)
            self.lum = pickle.load(f)
            self.param = pickle.load(f)
    
    def __repr__(self):
        'provide string representation of object'
        if not self.param is None:
            return f'k = {self.param[0]:.2f}, g0 = {self.param[1]:.2f}, gamma = {self.param[2]:.2f}, delta = {self.param[3]:.2f}'
        else:
            return 'no fit available'
