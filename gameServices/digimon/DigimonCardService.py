import json
from time import sleep

from PIL import Image
import Utils
import shutil
from pathlib import Path

import requests


BASE_URL = "https://digimoncard.app/assets/images/cards/"
IMAGE_EXTENSION = ".webp"


def getCardsFromFileHighQuality(totalCards):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
  }
  allCards = json.loads(requests.post("https://digimoncard.dev/data.php", headers=headers).text)
  cardImages = []
  cardCount = 0
  with open(Path.cwd()/'input'/'digimonInput.txt', 'r') as f:
    lines = f.readlines()
    f.close()
  for index, line in enumerate(lines):
    cardImages.append(getCardByIdHighQuality(line.rstrip(), allCards))
    cardCount += 1
    print("Loaded card: " + line.rstrip() + ", " + str(round(((cardCount / totalCards) * 100), 2)) + "% done")
  return cardImages

def getCardByIdHighQuality(id, allCards):
  cardVersionImageUrls = [card.get("imageUrl") for card in allCards if id == card.get("cardid")]
  print("card: ", cardVersionImageUrls[-1])
  response = requests.get(cardVersionImageUrls[-1], stream=True, headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
  })
  print("response: ", response)
  print("raw: ", response.raw)
  with open(Utils.getTempFilePath(), 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
  del response
  img = Image.open(Utils.getTempFilePath())
  img.getdata()  ## Genuinamente no tengo idea por que pero hacer eso hace que la resolucion sea buena, sin esto es terrible (sleep no funciona)
  return img

def getCardsFromFile(totalCards):
  cardImages = []
  cardCount = 0
  with open(Path.cwd()/'input'/'digimonInput.txt', 'r') as f:
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