from abc import ABC, abstractmethod 

class GenericListGenerator(ABC): 
  
    @abstractmethod
    def getDecklists(self): 
        pass
  
    @abstractmethod
    def transformDecklistsToGenericLists(self): 
        pass

    def saveLists(self):
        pass