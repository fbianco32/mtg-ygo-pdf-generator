import Utils
import MTGCardService
import YGOCardService


try:
    Utils.makeTempDir()
    #Debug
    images = MTGCardService.getCardsFromFile('./input/mtgInput.txt')
    Utils.assemblePDF(images, 210, 297, 5, '#13160d', 63, 88, True, 'mtgOutput') # A4

    images = YGOCardService.getCardsFromFile('./input/ygoInput.txt')
    Utils.assemblePDF(images, 59, 86, 0, '#60647f', 59, 86, False, 'ygoOutput') # 1 card per page
except BaseException as e:
    print("An error has occured, info: " + str(e))
    raise e
finally:
    Utils.cleanTempDir()