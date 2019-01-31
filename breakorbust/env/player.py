#import sys, os

#sys.path.append('..')  
import numpy as np
from ..common import DataGrabber
#from utilities import DataGrabber
import torch
import numpy
class Player():
    def __init__(self):
        self.balance = 1000
        self.reward = 0
        
    def update(self, m_price):
        pass
        

    def action_user(self, m_price):
        #print(len)
        #self.update(m_price)
        x = input('buy, hold?:')
        x = str(x)
        if x == "bet":
            pass
        elif x == "hold":
            pass
        else:
            pass

    def action(self, m_price, action):
        #print(len)
        #self.update(m_price)
        x = action
        x = int(x)
        if x == 0:
            pass
        elif x == 1:
            pass
        elif x == 2:
            pass
        elif x == 3:
            pass
        else:
            pass
    
    

    def details(self, m_price):
        pass
        return
        


    def render(self):
        pass


