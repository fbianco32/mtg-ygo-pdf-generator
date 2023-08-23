import PyPDF2
from PIL import Image
import requests
from io import BytesIO
import urllib.request

baseUrl = "https://images.ygoprodeck.com/images/cards/"
baseUrl2 = ".jpg"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def generatePdfFromCardArray():
    images = getCardsFromFile('./input/ygoInput.txt')
    images[0].save(
    'output/ygoOutput.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

def getCardsFromFile(pathToFile):
    cardImages = []
    with open(pathToFile, 'r') as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        cardImages.append(getCardById(line.rstrip()))
    return cardImages


def getCardById(id):
    response = requests.get(baseUrl + id + baseUrl2, headers=headers)
    urllib.request.urlretrieve((baseUrl + id + baseUrl2), 'C:\\Users\Felipe Bianco\Desktop\\temp')
    img = Image.open('C:\\Users\Felipe Bianco\Desktop\\temp')
    return img

generatePdfFromCardArray()