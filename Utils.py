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

def assemblePDF(images: List[Image.Image], width: float, height: float, margin: float, bgColor: str, cardWidth, cardHeight, hasCardback, fileName):
    pdf = fpdf.FPDF(orientation='L', unit = 'mm', format=(int(height), int(width)))
    x = margin
    y = margin
    bg = Image.new('RGB', (width,height), bgColor)
    cardback = Image.open('input/cardback.jpg')
    if(hasCardback):
        pdf.add_page() # First page with cardbacks
        pdf.image(bg,0,0,width,height, 'jpeg')
        while(y + cardHeight + margin <= height):
            pdf.image(cardback, x, y, cardWidth, cardHeight)
            x += cardWidth + margin
            if(x + cardWidth + margin >= width):
                y += cardHeight + margin
                x = margin
        y = margin

    pdf.add_page() # Start adding cards
    pdf.set_line_width(0.2)
    pdf.set_draw_color(hex_to_rgb(invert(bgColor)))
    pdf.image(bg,0,0,width,height, 'jpeg')
    for image in images:
        if(x + cardWidth + margin > width):
            y += cardHeight + margin
            x = margin
        if(y + cardHeight + margin > height):
            pdf.add_page()
            pdf.image(bg,0,0,width,height, 'jpeg')
            y = margin
        drawCutGuides(pdf, x, y, margin, cardWidth, cardHeight)
        pdf.image(image, x, y, cardWidth, cardHeight)
        x += cardWidth + margin
    pdf.output('output/'+fileName+'.pdf', 'F')

def invert(color_to_convert): 
    table =  str.maketrans('0123456789abcdef', 'fedcba9876543210')
    return '#' + color_to_convert[1:].lower().translate(table).upper()

def drawCutGuides(pdf, x, y, margin, cardWidth, cardHeight):
    pdf.line(x,y,x-margin,y)
    pdf.line(x,y,x,y-margin)
    pdf.line(x+cardWidth,y,x+cardWidth+margin,y)
    pdf.line(x+cardWidth,y,x+cardWidth,y-margin)
    pdf.line(x,y+cardHeight,x-margin,y+cardHeight)
    pdf.line(x,y+cardHeight,x,y+cardHeight+margin)
    pdf.line(x+cardWidth,y+cardHeight,x+cardWidth+margin,y+cardHeight)
    pdf.line(x+cardWidth,y+cardHeight,x+cardWidth,y+cardHeight+margin)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))