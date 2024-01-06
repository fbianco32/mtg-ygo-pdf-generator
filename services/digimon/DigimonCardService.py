from time import sleep

from PIL import Image
import Utils
import shutil

import requests


BASE_URL = "https://images.digimoncard.io/images/cards/"
IMAGE_EXTENSION = ".jpg"

def getCardsFromFile(totalCards):
  cardImages = []
  cardCount = 0
  with open(Utils.getPath('input', 'digimonInput.txt'), 'r') as f:
    lines = f.readlines()
    f.close()
  for index, line in enumerate(lines):
    cardImages.append(getCardById(line.rstrip()))
    cardCount += 1
    print("Loaded card: " + line.rstrip() + ", " + str(round(((cardCount / totalCards) * 100), 2)) + "% done")
  return cardImages


def getCardById(id):
  response = requests.get(BASE_URL + id + IMAGE_EXTENSION, stream=True)
  with open(Utils.getTempFilePath(), 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
  del response
  img = Image.open(Utils.getTempFilePath())
  img.getdata()  ## Genuinamente no tengo idea por que pero hacer eso hace que la resolucion sea buena, sin esto es terrible (sleep no funciona)
  return img