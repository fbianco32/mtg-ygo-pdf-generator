from abc import ABC, abstractmethod 

class GenericListGenerator(ABC): 

    genericLists = []
    type = ""

    @abstractmethod
    def getDecklists(self): 
        pass
  
    @abstractmethod
    def transformDecklistsToGenericLists(self): 
        pass

    def setGenricLists(self, genericLists):
        self.genericLists = genericLists

    def getGenericLists(self):
        return self.genericLists
    
    def getType(self):
        return self.type
    
    def saveGenericLists(self):
        for genericList in self.genericLists:
            genericList.save()