import json
import numpy as np
from sklearn import preprocessing
import csv
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

class DataTransforms():
    """data transforms"""
    def __init__(self):
        self.love = True
    

    def data_converted(self, data):
        data_converted  = []
        for i in data:
            data_converted.append([i['mid']['c'], i['mid']['h'], i['mid']['l'], i['mid']['o']])
            #data_converted.append([i['volume'], i['time'],i['mid']['c'], i['mid']['h'], i['mid']['l'], i['mid']['o']])
        return data_converted
    
    def jsontolist(self, path):
        with open(path) as f:
            data = json.load(f)
        return data

    def flatten(self, data):
        old_data = data
        new_data = np.array([])
        for i in range(len(old_data)):
            m = np.array(old_data[i][0][0])
            n = np.array(old_data[i][0][1])
            o = np.array(old_data[i][0][2], dtype=np.float)
            k = np.concatenate((m, n, o), axis=None)
        return k

    def flatten_split(self, data):
        old_data = data
        x = list()
        y = list()
        for i in range(len(old_data)):
            con = np.concatenate((old_data[i][0]), axis=None)
            con[0].tolist()
            x.append(con)
            y.append(old_data[i][1])

        return x, y

    def normalize(self, x):
        normalized = preprocessing.normalize(x)
        return normalized

    def normalize_split(self, x, y):
        normalized_x = preprocessing.normalize(x)
        normalized_y = preprocessing.normalize(y)
        return normalized_x, normalized_y

    def scaled(self, x):
        scaled = preprocessing.scale(x)
        return scaled

    def flatten_full(self, data):
        old_data = data
        x = list()
        for i in range(len(old_data)):
            con = np.concatenate((old_data[i][0]), axis=None)
            con = np.concatenate((con, old_data[i][1]), axis=None)
            con[0].tolist()
            x.append(con)
        return x
    
    def tocsv(self, x, path):
        with open(path, "a", newline='') as fp:
            wr = csv.writer(fp, dialect='excel')
            for i in range(len(x)):
                wr.writerow(x[i])
    def tocsv_single(self, x, path):
        with open(path, "a", newline='') as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(x)
    
    def process_data(self, data):
        data = self.jsontolist(data)
        x, y = self.flatten_split(data)
        x, y = self.toarray(x, y)
        x = self.normalize(x)
        return x, y

    def loader_prepare_split(self, x, y):
        data = np.zeros((len(y), 2, len(x[0])))
        for i in range(len(y)):
            data[i][0] = x[i]
            data[i][1] = y[i]
        return data


    def loader_prepare(self, data):
        new_data = np.zeros((len(data), 2, 1))
        for i in range(len(data)):
            new_data[i][0][0] = data[i][0]
            new_data[i][1][0] = data[i][1]
        return new_data

    def totensor(self, data):
        data = torch.from_numpy(data)
        return data

    def batcher(self, x, y, batch_size):
        x_data = list()
        y_data = list()
        for i in range(batch_size):
            num = np.random.choice(1, len(y))
            x_data.append(x[num])
            y_data.append(y[num])
        x_data = np.array(x_data, dtype=np.float32)
        y_data = np.array(y_data, dtype=int)
        return x_data, y_data

    def toarray(self, x):
        x = np.array(x, dtype=np.float32)
        return x

            


#test = DataTransforms()
#test_data = test.process_data('data/2018-10-11.trained.json')
#test.tocsv(test_data, 'test_data.csv')
#test_data = test.jsontolist('data/2018-10-11.trained.json')
#x_data, y_data = test.flatten_split(test_data)
#x_data = np.array([x_data], dtype=np.float32)
#y_data = np.array([y_data])
#test.tocsv(x, 'test_data.csv')
#data_prepared = test.loader_prepare_split(x_data, y_data)
#tensored = test.totensor(data_prepared)
#test_data = test.loader_prepare(test_data)
#print(x_data[0])
#print(data_prepared[0][0][0])
#train_loader = torch.utils.data.DataLoader(dataset=tensored, 
                                           #batch_size=64, 
                                           #shuffle=True)

#print(len(tensored[0][0]))
