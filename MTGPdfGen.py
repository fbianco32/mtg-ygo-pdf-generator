import PyPDF2
from PIL import Image, ImageFile
import urllib.request
from mtgsdk import Card
import time

ImageFile.LOAD_TRUNCATED_IMAGES=True
starttime = time.time()

def generatePdfFromCardArray():
    images = getCardsFromFile('./input/mtgInput.txt')
    images[0].save(
    'output/mtgOutput.pdf', "PDF", save_all=True, append_images=images[1:]
)

def getCardsFromFile(pathToFile):
    cardImages = []
    with open(pathToFile, 'r') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        fullCardname = line.rstrip()
        amount = fullCardname.split(" ")[0]
        for i in range (int(amount)):
            cardInfo = getCardInfo(fullCardname)
            cardnames = getCardNames(getCardByNameAndInfo(cardInfo[0], cardInfo[1], cardInfo[2]))
            for name in cardnames:
                time.sleep(1.0 - ((time.time() - starttime) % 1.0))
                cardImages.append(getCardImageByName(name, cardInfo[1], cardInfo[2]))
                print("Loaded card: " + fullCardname)
    return cardImages

def getCardInfo(fullCardname):
    return [fullCardname.split("(")[0].split(" ", 1)[1].rsplit(" ", 1)[0], fullCardname.split("(")[1].split(")")[0], fullCardname.split(")")[1].split(" ")[1]]

def getCardByNameAndInfo(cardname, setCode, collectorsNumber):
    card = Card.where(name=cardname).where(set=setCode).where(number=collectorsNumber).all()[0]
    return card

def getCardByName(cardname):
    return Card.where(name=cardname)

def getCardNames(card: Card): 
    return card.names if card.names else [card.name]

def getCardImageByName(cardname, setCode, collectorsNumber):
    card: Card = getCardByNameAndInfo(cardname, setCode, collectorsNumber)
    urllib.request.urlretrieve((card.image_url), 'C:\\Users\Felipe Bianco\Desktop\\temp')
    img = Image.open('C:\\Users\Felipe Bianco\Desktop\\temp')
    img.getdata()
    return img

generatePdfFromCardArray()