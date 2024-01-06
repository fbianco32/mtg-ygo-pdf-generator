from PIL import Image, ImageFile
import urllib.request
import Utils
import requests as req
import json
import os

ImageFile.LOAD_TRUNCATED_IMAGES=True
baseUrl = 'https://api.scryfall.com/cards/'

def getCardsFromFile(totalCards):
    cardImages = []
    cardCount = 0
    with open(Utils.getPath('../../input', 'mtgInput.txt'), 'r') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        fullCardname = line.rstrip()
        amount = fullCardname.split(" ")[0]
        for i in range (int(amount)):
            cardInfo = getCardInfo(fullCardname)
            faces = getFaces(getCardBySetAndNumber(cardInfo[1], cardInfo[2]))
            for face in faces:
                cardImages.append(getCardImageByFace(face))
                cardCount += 1
                print("Loaded card: " + fullCardname + ", " + str(round(((cardCount/totalCards)*100), 2)) +"% done")
    return cardImages

def getCardInfo(fullCardname):
    name = fullCardname.rsplit("(", 1)[0].split(" ", 1)[1].rsplit(" ", 1)[0]
    set = fullCardname.rsplit("(", 1)[1].split(")")[0].lower()
    code = fullCardname.rsplit(")", 1)[1].split(" ")[1].split("*")[0]
    return [name, set, code]

def getCardBySetAndNumber(setCode, collectorsNumber):
    card = json.loads(req.get(baseUrl + setCode + "/" + collectorsNumber).text)
    return card

excludedLayouts = ["flip", "adventure", "split"]

def getFaces(card): 
    if(card['layout'] not in excludedLayouts):
        if 'card_faces' in card:
            return card['card_faces']
        else:
            return [card]
    else:
        return [card]

def getCardImageByFace(face):
    urllib.request.urlretrieve((face['image_uris']['normal']), Utils.getTempFilePath())
    img = Image.open(Utils.getTempFilePath())
    img.getdata() ## Genuinamente no tengo idea por que pero hacer eso hace que la resolucion sea buena, sin esto es terrible (sleep no funciona)
    return img