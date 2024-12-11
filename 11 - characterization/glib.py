import numpy as np

class GammaObj:
    
    def __init__(self, p=None):
        super(GammaObj, self).__init__()
        
        if p is None:
            p = [100, 0, 2.2, 5]
        
        self.kappa = p[0]
        self.g0 = p[1]
        self.gamma_exp = p[2]
        self.delta = p[3]
    
    def gamma(self, g):
        
        low = g < self.g0
        high = g > 255
        ok = ~(low|high)
        
        y = np.empty(g.shape)
        y[low] = self.delta
        y[high] = self.kappa + self.delta
        y[ok] = self.kappa * np.power((g[ok]-self.g0)/(255-self.g0), self.gamma_exp) + self.delta
        
        return y
    
    def gammainv(self, y):
        
        low = y < self.delta
        high = y > self.kappa + self.delta
        ok = ~(low|high)
        
        x = np.empty(y.shape)
        x[low] = self.g0
        x[high] = 255
        x[ok] = (255-self.g0) * np.power((y[ok]-self.delta)/self.kappa, 1/self.gamma_exp) + self.g0
        
        return x
