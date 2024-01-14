import os
import pandas as pd

class GenericList(): 
    name = ""
    type = ""
    dataframe = None 
    dataframeColumns = ['id', 'name', 'expected']

    def __init__(self, name):
        self.name = name
        self.dataframe = pd.DataFrame(columns = self.dataframeColumns)

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setDataframeIds(self, ids):
        if all(isinstance(item, str) for item in ids):
            self.dataframe['id'] = ids
    
    def setDataframeNames(self, names):
        if all(isinstance(item, str) for item in names):
            self.dataframe['name'] = names
    
    def setDataframeExpecteds(self, expecteds):
        if all(isinstance(item, int) for item in expecteds):
            self.dataframe['expected'] = expecteds

    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getDataframe(self):
        return self.dataframe
    
    def save(self):
        self.dataframe.to_csv("./output/" + self.name+'.csv', index=False, header=True)

        