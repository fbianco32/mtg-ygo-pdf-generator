import os
from strategies.YGOStrategy import YGOHandler
from DeckTypes import YGO, MTG, DIGIMON


typeDirectoryInputPaths = {
    YGO: './input/YGO',
    MTG: './input/MTG',
    DIGIMON: './input/DIGIMON'
}

def createYGOHandler(type):
    return YGOHandler(typeDirectoryInputPaths.get(type))
def createMTGHandler(type):
    return
def createDIGIMONHandler(type):
    return
def default():
    return None

handlerSwitch = {
    YGO: createYGOHandler(YGO),
    MTG: createMTGHandler(MTG),
    DIGIMON: createDIGIMONHandler(DIGIMON),
}

def getHandler(type):
    return handlerSwitch.get(type, default)


def main():
    handlers = []
    for type in typeDirectoryInputPaths:
        #print(typeDirectoryInputPaths.get(type))
        if os.listdir(typeDirectoryInputPaths.get(type)) != []:
            handlers.append(getHandler(type))
    
    for handler in handlers:
        print(handler.input_folder)
        decklists = handler.getDecklists()
        print(decklists)
        genericDecklists = handler.transformDecklistsToGenericLists(decklists)
        # handler.saveLists(genericDecklists)




        

if __name__ == "__main__":
    main()