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

def assemblePDF(images: List[Image.Image], height: int, width: float, margin: float, bgColor: str, cardWidth, cardHeight, fileName):
    pdf = fpdf.FPDF(orientation='L', unit = 'mm', format=(int(height), int(width)))
    x = margin
    y = margin
    bg = Image.new('RGB', (width,height), bgColor)
    pdf.add_page()
    pdf.image(bg,0,0,width,height, 'jpeg')
    for image in images:
        if(x + cardWidth + margin > width):
            y += cardHeight + margin/2
            x = margin
        if(y + cardHeight + margin > height):
            pdf.add_page()
            pdf.image(bg,0,0,width,height, 'jpeg')
            y = margin
        pdf.image(image, x, y, cardWidth, cardHeight)
        x += cardWidth + margin
    pdf.output('output/'+fileName+'.pdf', 'F')