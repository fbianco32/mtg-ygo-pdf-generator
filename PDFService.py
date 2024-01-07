import Utils
from PIL import Image
from typing import List
import fpdf
import fitz

def assemblePDF(images: List[Image.Image], width: float, height: float, margin: float, bgColor: str, cardWidth, cardHeight, hasCardback, hasCutGuides, fileName):
    pdf = fpdf.FPDF(orientation='L', unit = 'mm', format=(int(height), int(width)))
    x = margin
    y = margin
    bg = Image.new('RGB', (width,height), bgColor)
    if(hasCardback):
        cardback = Image.open('input/cardback.jpg')
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
    pdf.set_draw_color(Utils.hex_to_rgb(Utils.invert(bgColor)))
    pdf.image(bg,0,0,width,height, 'jpeg')
    for image in images:
        if(x + cardWidth + margin > width):
            y += cardHeight + margin
            x = margin
        if(y + cardHeight + margin > height):
            pdf.add_page()
            pdf.image(bg,0,0,width,height, 'jpeg')
            y = margin
        if(hasCutGuides):
            drawCutGuides(pdf, x, y, margin, cardWidth, cardHeight)
        pdf.image(image, x, y, cardWidth, cardHeight)
        x += cardWidth + margin
    pdf.output('output/'+fileName+'.pdf', 'F')

def hideAllCutGuides(margin, cardWidth, cardHeight, bgColor, fileName):
    pdf = fitz.open(Utils.getPath('pdfInput', fileName))
    for page in pdf:
        hideCutGuides(page, margin, margin, margin, cardWidth, cardHeight, bgColor)
    pdf.save(Utils.getPath('output', 'NoCut' + fileName))


def drawCutGuides(pdf, x, y, margin, cardWidth, cardHeight):
    pdf.line(x,y,x-margin,y)
    pdf.line(x,y,x,y-margin)
    pdf.line(x+cardWidth,y,x+cardWidth+margin,y)
    pdf.line(x+cardWidth,y,x+cardWidth,y-margin)
    pdf.line(x,y+cardHeight,x-margin,y+cardHeight)
    pdf.line(x,y+cardHeight,x,y+cardHeight+margin)
    pdf.line(x+cardWidth,y+cardHeight,x+cardWidth+margin,y+cardHeight)
    pdf.line(x+cardWidth,y+cardHeight,x+cardWidth,y+cardHeight+margin)

def hideCutGuides(page, x, y, margin, cardWidth, cardHeight, bgColor):
    color = Utils.rgb_to_percent(Utils.hex_to_rgb(bgColor))
    bounds = page.bound()
    page.draw_rect(fitz.Rect(bounds.x0,bounds.y0,bounds.x1,(y/25.4)*72), color, color)
    page.draw_rect(fitz.Rect(bounds.x0,bounds.y0,(x/25.4)*72,bounds.y1), color, color)
    page.draw_rect(fitz.Rect(bounds.x0,(((y+cardHeight)/25.4)*72),bounds.x1,bounds.y1), color, color)
    page.draw_rect(fitz.Rect((((x+cardWidth)/25.4)*72),bounds.y0,bounds.x1,bounds.y1), color, color)
