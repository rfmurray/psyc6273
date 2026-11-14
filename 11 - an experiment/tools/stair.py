# psychtools.py  Module containing tools for psychological experiments

import math, random

# staircase class
class Stair:
    
    def __init__(self, up=1, down=3, levels=[ i for i in range(10) ]):
        self.countLimits = [up, down]
        self.levels = levels
        self.count = [0, 0]
        self.stimk = round(len(levels)/2)
    
    def stim(self):
        return self.levels[self.stimk]
    
    def response(self, correct):
        
        self.count[correct] += 1
        
        if self.count[0] >= self.countLimits[0]:
            self.stimk = min( self.stimk+1, len(self.levels)-1 )
            self.count = [0, 0]
            
        elif self.count[1] >= self.countLimits[1]:
            self.stimk = max( self.stimk-1, 0 )
            self.count = [0, 0]
    
    def __repr__(self):
        return f'Stair(countlimits={self.countLimits}, levels={self.levels}, count={self.count}, stimk={self.stimk})'

# staircase holder class
class StairHolder:
    
    def __init__(self):
        self.stairlist = []
        self.stairk = None
    
    def add(self, stair):
        self.stairlist.append(stair)
    
    def stim(self):
        self.stairk = random.randint(0,len(self.stairlist)-1)
        return self.stairlist[self.stairk].stim()
    
    def response(self, correct):
        self.stairlist[self.stairk].response(correct)
    
    def __repr__(self):
        s = f'StairHandler(stairk={self.stairk})\n'
        for x in self.stairlist:
            s += f'  {x}\n'
        return s
