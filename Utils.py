from PIL import Image
from typing import List
import os
import fpdf
import shutil


tempDir = './temp/'
tempFilePath = './temp/tempFile'

def makeTempDir():
    os.makedirs(tempDir)
    open(tempFilePath, 'w+').close()

def cleanTempDir():
    shutil.rmtree(tempDir)

def inchesToMm(num):
    return num * 25.4

def mmToInches(num):
    return num / 25.4

def assemblePDF(images: List[Image.Image], width: int, height: float, margin: float, bgColor: str, cardHeight, cardWidth, fileName):
    pdf = fpdf.FPDF(orientation='L', unit = 'mm', format=(int(height), int(width)))
    x = 0
    y = 0
    img = Image.new('RGB', (height,width), bgColor)
    img.save('temp/bg.jpeg')
    pdf.add_page()
    pdf.image('temp/bg.jpeg',0,0,width,height, 'jpeg')
    for image in images:
        if(x > width + cardWidth + margin/2):
            y += cardHeight + margin/2
            x = 0
        if(y > height + cardHeight + margin/2):
            pdf.add_page()
            y = 0
        x += cardWidth + margin
        image.save('temp/workingImage.jpg')
        pdf.image('temp/workingImage.jpg', x, y, cardWidth, cardHeight)
    pdf.output('output/'+fileName+'.pdf', 'F')