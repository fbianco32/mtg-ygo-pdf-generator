from PIL import Image, ImageFile
import urllib.request
import Utils
import requests as req
import json
import os
from pathlib import Path

ImageFile.LOAD_TRUNCATED_IMAGES=True
baseUrl = 'https://api.lorcana-api.com'

def getCardsFromFile(totalCards):
    cardImages = []
    cardCount = 0
    with open(Path.cwd()/'input'/'lorInput.txt', 'r') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        fullCardname = line.rstrip()
        amount = fullCardname.split(" ")[0]
        name = getCardName(fullCardname)
        face = getFace(getCardByname(name))
        faceImages = [getCardImageByFace(face)]
        for i in range (int(amount)):
            for faceImg in faceImages:
                cardImages.append(faceImg)
                cardCount += 1
        print("Loaded card: " + fullCardname + ", " + str(round(((cardCount/totalCards)*100), 2)) +"% done")
    return cardImages

def getCardName(fullCardname):
    name = fullCardname.split(" ")[1:]
    return_name=""
    for space in name:
        if space != name [-1]:
            space=space+ " "
        return_name+=space
    return return_name


def getCardByname(name):
    card = json.loads(req.get(baseUrl + "/cards/fetch?search=name~" + name).text)
    return card
excludedLayouts = ["flip", "adventure", "split"]

def getFace(card): 
   return card[0]["Image"]

def getCardImageByFace(name):
    urllib.request.urlretrieve((name), Utils.getTempFilePath())
    img = Image.open(Utils.getTempFilePath())
    img.getdata() ## Genuinamente no tengo idea por que pero hacer eso hace que la resolucion sea buena, sin esto es terrible (sleep no funciona)
    return img