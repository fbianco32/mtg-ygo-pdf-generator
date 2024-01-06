from time import sleep

from PIL import Image
import Utils
import shutil
from pathlib import Path

import requests


BASE_URL = "https://images.digimoncard.io/images/cards/"
IMAGE_EXTENSION = ".jpg"

def getCardsFromFile(totalCards):
  cardImages = []
  cardCount = 0
  with open(Path.cwd()/'input'/'digimonInput.txt', 'r') as f:
    lines = f.readlines()
    f.close()
  for index, line in enumerate(lines):
    if index and index % 15 == 0:
      print("---- 10 Seconds sleep, digimon.io has a rate limit of 15 cards every 10 seconds ----")
      sleep(10)
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