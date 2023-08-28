from PIL import Image
from typing import List
import os
import fpdf
from reportlab.pdfgen import canvas

tempDir = './temp/'
tempFilePath = './temp/tempFile'

def makeTempDir():
    os.makedirs(tempDir)
    open(tempFilePath, 'w+').close()

def cleanTempDir():
    os.remove(tempFilePath)
    os.removedirs(tempDir)

def inchesToMm(num):
    return num * 25.4

def mmToInches(num):
    return num / 25.4

def assemblePDF(images: List[Image.Image], width: int, height: int, margin: int, bgColor: str, cardHeight, cardWidth, fileName):
    pdf = fpdf.FPDF(orientation='L',unit='mm', format=[height, width])
    x = 0
    y = 0
    for image in images:
        if(x > width + cardWidth + margin/2):
            y += cardHeight + margin/2
            x = 0
        if(y > height + cardHeight + margin/2):
            pdf.add_page()
            y = 0
        pdf.image(image, x, y, cardWidth, cardHeight)
    pdf.output('output/'+fileName+'.pdf', 'F')