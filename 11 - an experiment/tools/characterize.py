import os, glob, pickle, random
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from psychopy import visual, core, event

try:
    from psychopy_minolta import minolta
except:
    print('warning: psychopy_minolta module not available')

class CharLum:
    
    def __init__(self, filename='', photsim=False, port=None, win=None):

        self.grey = None        # greylevels from characterization measurements
        self.lum = None         # luminances from characterization measurements
        self.param = None       # fitted gamma function parameters
        
        self.testdata = None    # data from measurements to test fit
        
        self.phot = None        # photometer object
        self.photsim = photsim  # flag whether to simulate photometer
        self.port = port        # port to use for photometer
        
        self.win = win          # window to use for characterization
        self.rect = visual.Rect(self.win, 400, 400) if self.win else None   # rectangle to use for characterization

        if filename:
            self.filename = filename
            if os.path.isfile(self.filename):
                self.load(filename)
            else:
                print(f'warning: {filename} does not exist')
        else:
            self.filename = 'charlum.pkl'

    def photopen(self, port=None):
        'open connection to photometer'
        if self.photsim: return
        if port is None:
            port = glob.glob('/dev/tty.usbserial*')[0] if not self.port else self.port
        self.phot = minolta.LS100(port)

    def photclose(self):
        'close connection to photometer'
        if self.photsim: return
        del self.phot
        self.phot = None

    def getlum(self):
        'measure luminance of test patch'
        return self.phot.getLum()
    
    def simlum(self, grey):
        'calculate a simulated luminance measurement'
        return 5 + 100 * ((grey+1)/2)**2 + random.gauss(mu=0, sigma=1)
    
    def showsquare(self, grey=1, waitkey=False):
        'show square test patch'
        if self.win is None: return
        self.rect.fillColor = grey
        self.rect.draw()
        self.win.flip()
        if waitkey:
            event.waitKeys()
        else:
            core.wait(0.1)
    
    def measure(self):
        'measure luminance of a series of rgb levels'
    
        self.photopen()
        
        self.grey = np.linspace(-1, 1, 10)
        self.grey = np.random.permutation(self.grey)
        self.lum = np.full(self.grey.shape, np.nan)
        
        self.showsquare(grey=0.5, waitkey=True)
        
        for i, v in enumerate(self.grey):
            self.showsquare(grey=v)
            self.lum[i] = self.simlum(grey=v) if self.photsim else self.getlum()
        
        k = np.argsort(self.grey)
        self.grey = self.grey[k]
        self.lum = self.lum[k]
        
        self.photclose()
    
    def fit(self):
        'fit gamma function to characterization data'
        p0 = [self.lum.max()-self.lum.min(), 0, 2, self.lum.min()]
        bounds = (np.array((0, -1, -np.inf, 0)), np.array((np.inf, 1, np.inf, np.inf)))
        self.param, _ = optimize.curve_fit(self.gammafn, self.grey, self.lum, p0=p0, bounds=bounds)
    
    def plot(self):
        'plot characterization data and fitted gamma function'
        if not self.param is None:
            xx = np.linspace(-1,1,100)
            plt.plot(xx, self.grey2lum(xx), 'r-', label='fit')
        plt.plot(self.grey, self.lum, 'bo', label='measurements')
        plt.xlabel('greylevel')
        plt.ylabel('luminance (cd/m^2)')
        plt.legend(loc='upper left')
        plt.show()
    
    def test_measure(self):
        'test lum2grey and grey2lum mappings with fitted parameters'
        
        self.photopen()
        self.showsquare(grey=0.5, waitkey=True)
        
        # check lum2grey mapping
        lumA = np.linspace(self.param[3], self.param[0]+self.param[3], 10)
        lumA = np.random.permutation(lumA)
        greyA = self.lum2grey(lumA)
        lum_measA = np.full(lumA.shape, np.nan)
        for i, v in enumerate(greyA):
            self.showsquare(grey=v)
            lum_measA[i] = self.simlum(grey=v) if self.photsim else self.getlum()
        
        # check greylum mapping
        greyB = np.linspace(-1, 1, 10)
        greyB = np.random.permutation(greyB)
        lumB = self.grey2lum(greyB)
        lum_measB = np.full(lumB.shape, np.nan)
        for i, v in enumerate(greyB):
            self.showsquare(grey=v)
            lum_measB[i] = self.simlum(grey=v) if self.photsim else self.getlum()
        
        self.photclose()
        self.testdata = (lumA, lum_measA, lumB, lum_measB)
        
    def test_plot(self):
        
        lumA, lum_measA, lumB, lum_measB = self.testdata
        
        # plot results
        plt.subplot(1,2,1)
        plt.plot(lumA, lum_measA, 'ro')
        plt.subplot(1,2,2)
        plt.plot(lumB, lum_measB, 'ro')
        mx = 1.1*np.concatenate([lumA, lum_measA, lumB, lum_measB]).max()
        for i in range(2):
            plt.subplot(1,2,i+1)
            plt.plot([0, mx],[0, mx],'k:')
            plt.xlim(0,mx)
            plt.ylim(0,mx)
            plt.gca().set_aspect('equal', 'box')
            plt.xlabel('requested luminance (cd/m^2)')
            if i==1: plt.ylabel('measured luminance (cd/m^2)')
        
        plt.show()
    
    def lum2grey(self, lum):
        'convert luminance to greylevel'
        grey = self.gammainv(lum, *self.param)
        return grey
    
    def grey2lum(self, grey):
        'convert greylevel to luminance'
        return self.gammafn(grey, *self.param)
    
    def minlum(self):
        return self.grey2lum(np.array([0])).item()
    
    def maxlum(self):
        return self.grey2lum(np.array([255])).item()
    
    def midlum(self):
        return (self.minlum()+self.maxlum())/2
    
    def gammafn(self, x, k, g0, gamma, delta):
        'gamma function'
        
        x = np.array(x)
        low = x<g0
        high = x>1
        ok = ~(low|high)
        
        y = np.empty(x.shape)
        y[low] = delta
        y[high] = k+delta
        y[ok] = k * np.power((x[ok]-g0)/(1-g0), gamma) + delta
        
        return y
    
    def gammainv(self, y, k, g0, gamma, delta):
        'inverse gamma function'
        
        y = np.array(y)
        low = y<delta
        high = y>k+delta
        ok = ~(low|high)
        
        x = np.empty(y.shape)
        x[low] = g0
        x[high] = 1
        x[ok] = (1-g0) * np.power((y[ok]-delta)/k, 1/gamma) + g0
        
        return x
    
    def save(self, filename=None):
        'save characterization data and fitted parameters'
        if not filename:
            filename = self.filename
        with open(filename, 'wb') as f:
            pickle.dump(self.grey, f)
            pickle.dump(self.lum, f)
            pickle.dump(self.param, f)
    
    def load(self, filename=None):
        'load characterization data and fitted parameters'
        if not filename:
            filename = self.filename
        with open(filename, 'rb') as f:
            self.grey = pickle.load(f)
            self.lum = pickle.load(f)
            self.param = pickle.load(f)
    
    def __repr__(self):
        'provide string representation of object'
        if not self.param is None:
            return f'k = {self.param[0]:.2f}, g0 = {self.param[1]:.2f}, gamma = {self.param[2]:.2f}, delta = {self.param[3]:.2f}'
        else:
            return 'no fit available'
