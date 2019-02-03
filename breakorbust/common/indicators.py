import numpy as np

class Indicators():
    def __init__(self):
        pass
    
    def mean(self, state):
        m = np.mean(state)
        return m


    def median(self, state):
        m = np.median(state)
        return m
    
    def atr(self, state):
        highatr = max(state)
        lowatr = min(state)
        atr = highatr - lowatr
        return atr  
    
    def bandr(self, state):
    
        black = []
        red = []
        for i in state:
            if i >= 2:
                black.append(i)
            else:
                red.append(i)
        blackper = len(black) / len(state)
        redper = len(red) / len(state)
        return blackper, redper