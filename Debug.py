import Utils
import MTGCardService


try:
    Utils.makeTempDir()
    
    #Debug
    images = MTGCardService.getCardsFromFile('./input/mtgInput.txt')
    Utils.assemblePDF(images, 297, 210, 5, '#13160d', 63, 88, 'mtgOutput') # bgColor for mtg is always black, dpi for MTG is always 196
except BaseException as e:
    print("An error has occured, info: " + str(e))
    raise e
finally:
    Utils.cleanTempDir()