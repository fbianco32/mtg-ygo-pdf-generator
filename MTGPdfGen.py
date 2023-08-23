import PyPDF2

def generatePdfFromCardArray():
    images = getCardsFromFile('./input/mtgInput.txt')
    images[0].save(
    'output/mtgOutput.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

def getCardsFromFile(pathToFile):
    cardImages = []
    with open(pathToFile, 'r') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        cardname = line.rstrip()
        if(checkIfDualFaced(cardname)):
            cardImages.append(getCardByName(getBackside(cardname)))
        cardImages.append(getCardByName())
            
    return cardImages

def getCardByName():
    return

def checkIfDualFaced(cardname):
    return

def getBackside(cardname):
    return