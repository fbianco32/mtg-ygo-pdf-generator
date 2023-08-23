import PyPDF2
from PIL import Image, ImageFile
import urllib.request
import time
import requests as req
import json

ImageFile.LOAD_TRUNCATED_IMAGES=True
baseUrl = 'https://api.scryfall.com/cards/'
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
            faces = getFaces(getCardBySetAndNumber(cardInfo[1], cardInfo[2]))
            for face in faces:
                time.sleep(1.0 - ((time.time() - starttime) % 1.0))
                cardImages.append(getCardImageByFace(face))
                print("Loaded card: " + fullCardname)
    return cardImages

def getCardInfo(fullCardname):
    return [fullCardname.split("(")[0].split(" ", 1)[1].rsplit(" ", 1)[0], fullCardname.split("(")[1].split(")")[0].lower(), fullCardname.split(")")[1].split(" ")[1]]

def getCardBySetAndNumber(setCode, collectorsNumber):
    card = json.loads(req.get(baseUrl + setCode + "/" + collectorsNumber).text)
    return card

def getFaces(card): 
    if 'card_faces' in card:
        return card['card_faces']
    else:
        return [card]

def getCardImageByFace(face):
    urllib.request.urlretrieve((face['image_uris']['normal']), 'C:\\Users\Felipe Bianco\Desktop\\temp')
    img = Image.open('C:\\Users\Felipe Bianco\Desktop\\temp')
    img.getdata()
    return img

generatePdfFromCardArray()