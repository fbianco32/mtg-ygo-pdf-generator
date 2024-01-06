import Utils
import PDFService


try:
    Utils.makeTempDir()
    #Debug
    # images = MTGCardService.getCardsFromFile(2117)
    # PDFService.assemblePDF(images, 73, 98, 5, '#13160d', 63, 88, False, 'mtgOutput') # A4

    # images = YGOCardService.getCardsFromFile(2133)
    # PDFService.assemblePDF(images, 210, 297, 5, '#60647f', 59, 86, False, 'ygoOutput') # 1 card per page
    PDFService.hideAllCutGuides(5, 59, 86, '#60647f','YgoCbOutput.pdf')
    PDFService.hideAllCutGuides(5, 59, 86, '#60647f','YgoNoCbOutput.pdf')
    PDFService.hideAllCutGuides(5, 63, 88, '#121003','MtgCbOutput.pdf')
    PDFService.hideAllCutGuides(5, 63, 88, '#121003','MtgNoCbOutput.pdf')
except BaseException as e:
    print("An error has occured, info: " + str(e))
    raise e
finally:
    Utils.cleanTempDir()