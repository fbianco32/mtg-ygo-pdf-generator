from PIL import Image
import urllib.request
import Utils

baseUrl = "https://images.ygoprodeck.com/images/cards/"
baseUrl2 = ".jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def getCardsFromFile(pathToFile):
    cardImages = []
    with open(pathToFile, 'r') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        cardImages.append(getCardById(line.rstrip()))
        print("Loaded card: " + line.rstrip())
    return cardImages


def getCardById(id):
    urllib.request.urlretrieve((baseUrl + id + baseUrl2), Utils.tempFilePath)
    img = Image.open(Utils.tempFilePath)
    img.getdata() ## Genuinamente no tengo idea por que pero hacer eso hace que la resolucion sea buena, sin esto es terrible (sleep no funciona)
    return img