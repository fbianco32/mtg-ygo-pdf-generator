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
            idColumn = self.dataframe['id']
            newIdColumn = idColumn.apply(ids)
            self.dataframe['id'] = newIdColumn
    
    def setDataframeNames(self, names):
        if all(isinstance(item, str) for item in names):
            self.dataframe['names'] = names
    
    def setDataframeExpecteds(self, expecteds):
        if all(isinstance(item, str) for item in expecteds):
            expectedColumn = self.dataframe['expected']
            newExpectedColumn = expectedColumn.apply(expecteds)
            self.dataframe['expected'] = newExpectedColumn

    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getDataframe(self):
        return self.dataframe

        