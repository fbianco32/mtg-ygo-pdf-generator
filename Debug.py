import Utils
import MTGCardService
import YGOCardService


try:
    Utils.makeTempDir()
    #Debug
    images = MTGCardService.getCardsFromFile('./input/mtgInput.txt')
    Utils.assemblePDF(images, 297, 210, 5, '#13160d', 63, 88, True, 'mtgOutput') # bgColor for mtg is always black, dpi for MTG is always 196

    images = YGOCardService.getCardsFromFile('./input/ygoInput.txt')
    Utils.assemblePDF(images, 297, 210, 5, '#60647f', 59, 86, True, 'ygoOutput') # bgColor for mtg is always gray, dpi for YGO is always 187
except BaseException as e:
    print("An error has occured, info: " + str(e))
    raise e
finally:
    Utils.cleanTempDir()