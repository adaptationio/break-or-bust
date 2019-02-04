import hashlib
import time
import math
import numpy as np

#Define the starting object Hash
class NumberGen():
    def __init__(self):
        self.hashobj = hashlib.sha256('Hello World'.encode('utf-8'))


    def to_array(self, games, save=True):
        game_array = []
        # Looperino starting here
        for i in range(games):
            self.hashobj = hashlib.sha256(self.hashobj.hexdigest().encode('utf-8'))
            intversion = int(self.hashobj.hexdigest()[0:13], 16) # Javascript Original | parseInt(hash.slice(0,52/4),16);
        # Check if Divisible by 101, if yes put out immediately 1 so users loose (1% house edge)
            if (intversion % 101 == 0):
                number = 1.00
            else:
                b = 4503599627370496 # Javascript Original | Math.pow(2,52);
                number = math.floor((100 * b - intversion) / (b - intversion)) / 100
            #print(number) ### PLEASE PLEASE if doing bigger tests comment this out! 20x speed increase
            game_array.append(number)
        if save:
            np.save('data/game'+str(games)+'.npy', game_array)
        return game_array

    def gen(self):
        self.hashobj = hashlib.sha256(self.hashobj.hexdigest().encode('utf-8'))
        intversion = int(self.hashobj.hexdigest()[0:13], 16) # Javascript Original | parseInt(hash.slice(0,52/4),16);
        # Check if Divisible by 101, if yes put out immediately 1 so users loose (1% house edge)
        if (intversion % 101 == 0):
            number = 1.00
        else:
            b = 4503599627370496 # Javascript Original | Math.pow(2,52);
            number = math.floor((100 * b - intversion) / (b - intversion)) / 100
        return number


#test = NumberGen()

#number = test.to_array(100000000)



    