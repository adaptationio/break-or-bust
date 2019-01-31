import numpy as np

class Indicators():
    def __init__(self):
        pass
    
    def average_diff(self, state):
    
        new_state = []
        for i in range(len(state)):
            new_state.append(state[i][0])
        new_state = np.mean(new_state)
        return new_state


    def median_diff(self, state):
        new_state = []
        for i in range(len(state)):
            new_state.append(state[i][0])
        new_state = np.median(new_state)
        return new_state
    
    def atr(self, state):
        stateatr = []
        for i in range(len(state)):
            stateatr.append(state[i][1])
            stateatr.append(state[i][2])
        highatr = max(stateatr)
        lowatr = min(stateatr)
        atr = highatr - lowatr
        return atr  
    
    def average_vol(self, state):
    
        new_state = []
        for i in range(len(state)):
            new_state.append(state[i][4])
        new_state = np.mean(new_state)
        return new_state