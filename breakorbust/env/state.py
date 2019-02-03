import numpy as np
#from utilities import DataGrabber
import torch
from ..player import Player
from ..common import DataGrabber
import numpy
import random
#from ..common import DataGrabber
class BustaBitSim():
    def __init__(self):
        self.love = 14
        self.player = Player()
        self.actions = [1,2,3,4]
        self.data_grabber = DataGrabber()
        self.state = None
        self.state_full = None
        self.state_current = None
        self.count = 0
        self.diff = 0
        self.load = True
    
    def make_episode(self):
        self.state_full = np.load('data/game10000000.npy')

    def make_current_state(self, count):
        start = (0+count+self.rand)
        end = (1001+count+self.rand)
        self.state = self.state_full[start:end]
        return self.state

    def get_state(self):
        self.state_current = self.state[-1]

    def step(self, action):
        self.count += 1
        self.player.action(self.state_current, action)
        self.make_current_state(self.count)
        reward = 0
        #if self.count == 1001:
            #print(self.reward)
        state = self.state_maker()
        done = self.done(self.count)
        
        return state, reward, done


    def reset(self):
        self.count = 0
        self.make_episode()
        self.rand = np.random.random_integers(len(self.state_full / 10 * 9))
        self.state = self.make_current_state(self.count)
        state = self.state_maker()
        return state

    def render(self):
        print('test')


    def state_maker(self):
        #user = self.player.details(self.price)
        #market = self.state_over_time(self.state)
        count = np.array([self.count])
        state = self.data_grabber.flatten(market, user, count)

        return state

    def reward(self):

        return self.player.reward
    
    def done(self, count):
        if count == 10000:
            
            return True
        else:
            return False 


