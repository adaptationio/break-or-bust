#import sys, os

#sys.path.append('..')  
import numpy as np
from ..common import DataTransforms
#from utilities import DataGrabber
import torch
import numpy
class Player():
    def __init__(self):
        self.balance = 1000
        self.reward = 0
        self.bet = False
        self.multiply = 1
        
    def update(self, m_price):
        pass
        

    def action_user(self, m_price):
        #print(len)
        #self.update(m_price)
        x = input('bet, hold?:')
        x = str(x)
        if x == "bet":
            self.bet = True
        elif x == "hold":
            self.bet = False
        else:
            pass

    def action(self, m_price, action):
        #print(len)
        #self.update(m_price)
        x = action
        x = int(x)
        if x == 0:
            self.bet = True
            self.multiply = 1
        elif x == 1:
            self.bet = False
        elif x == 2:
            self.bet = True
            self.multiple = 2
        elif x == 3:
            self.bet = True
            self.multiple = 3
            
        else:
            pass
    
    

    def details(self, m_price):
        pass
        return
        


    def render(self):
        pass


