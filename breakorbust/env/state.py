import numpy as np
#from utilities import DataGrabber
import torch
f#rom .player import Player
from ..common import DataGrabber
import numpy
import random
#from ..common import DataGrabber
class BustaBitSim():
    def __init__(self):
        self.love = 14
        #self.player = Player()
        self.actions = [1,2,3,4]
        #self.count = [1440, 2880]
        self.data_grabber = DataGrabber()
        self.state = None
        self.state_full = None
        self.state_current = None
        self.price = None
        self.count = 0
        self.diff = 0
        self.load = True
    
    def make_episode(self):
        if self.load == True:
            self.state_full = self.data_grabber.load_state_2()
        else:
            self.state_full = self.data_grabber.process_to_array()


    def make_current_state(self, count):
        start = (0+count)
        end = (1440+count)
        self.state = self.state_full[start:end]
        return self.state

    def get_price(self):
        self.state_current = self.state[-1:]
        self.price = self.state_current[0][0]
    
    def get_diff(self):
        self.state_current = self.state[-1:]
        self.diff = self.state_current[0][1]

    def step(self, action):
        
        self.count += 1
        
        self.player.action(self.price, action)
        self.make_current_state(self.count)
        self.reward = 0
        #if self.count == 96:
            #print(self.reward)
        state = self.state_maker()
        done = self.done(self.count)
        
        return state, self.reward, done


    def reset(self):
        self.count = 0
        self.make_episode()
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

    def reward2(self):

        return self.player.reward
    
    def done(self, count):
        if count == 10000:
            
            return True
        else:
            return False 

    def difference(self, state):
        new_state = []
        r = 1440
        for i in range(1440):
            before = state[i][0]
            b = i+1
            after = state[b][0]
            diff = after - before
        
            new_state.append([after, diff])
        return new_state

