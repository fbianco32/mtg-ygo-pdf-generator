import Utils
from gameServices.mtg import MTGDecksService, MTGCardService
from gameServices.ygo import YGOCardService, YGOYdkService
from gameServices.custom import CustomCardService
import PDFService
from gameServices.digimon import DigimonDecksService, DigimonCardService


def main():
    try:
        Utils.makeTempDir()
        Utils.makeDirsIfNotExists()
        option = input('Choose game: [Y]GO/[M]TG/[D]igimon/[C]ustom\n').lower()
        width = int(input('Enter page Width (mm): \n'))
        height = int(input('Enter page Height (mm): \n'))
        margin = int(input('Enter Margin between cards (mm): \n'))
        hasCardback = False
        cardbackOption = input('Do you want to add a cardback? ([Y][N])\n')
        if(cardbackOption.lower() == 'y'):
            input('Move the cardback.jpg file to input folder, then press [ENTER] to continue\n')
            hasCardback = True
        if(option == 'y'):
            print('Move YDK files to input folder, then press [ENTER] to continue')
            print('(The YDKs should be exported directly from YGOProDeck, saved as .ydk)')
            input('(Go to your YGOProDeck deck > More > Download YDK or, in the deckbuilder, Export > To .ydk Deck file)\n')
            print('Preparing YDK')
            cardCount = YGOYdkService.prepareYDKs()
            if cardCount == 0:
                print('No valid decks found, aborting')
                return
            print(f"Found {cardCount} unique cards")
            input('YDK prepared. Press [ENTER] to continue')
            print('Fetching card images...')
            images = YGOCardService.getCardsFromFile(cardCount)
            print('Assembling PDF...')
            PDFService.assemblePDF(images, width, height, margin, '#60647f', 59, 86, hasCardback, 'ygoOutput') # bgColor for mtg is always gray, dpi for YGO is always 187
            print('Done! PDF can be found in ./output/ygoOutput.pdf')
        elif(option == 'm'):
            print('Move decklist files to mtgInput folder, then press [ENTER] to continue')
            print('(The decklists should be in Moxfield\'s export format, saved as .txt)')
            input('(Go to your Moxfield deck > Export > Copy full list and save that to a .txt file)\n')
            cardCount = MTGDecksService.prepareMTGDecks()
            if cardCount == 0:
                print('No valid decks found, aborting')
                return
            print(f"Found {cardCount} unique cards")
            input('MTG decks prepared. Press [ENTER] to continue')
            print('Fetching cards...')
            images = MTGCardService.getCardsFromFile(cardCount)
            print('Assembling PDF...')
            PDFService.assemblePDF(images, width, height, margin, '#13160d', 63, 88, hasCardback, 'mtgOutput') # bgColor for mtg is always black, dpi for MTG is always 196
            print('Done! PDF can be found in ./output/mtgOutput.pdf')
        elif (option == 'd'):
            print('Move decklist files to input folder, then press [ENTER] to continue')
            print('(The decklists should be in digimoncard.io export format, saved as .txt)')
            input('(Go to your digimoncard.io deck > Export > Copy full list and save that to a .txt file)\n')
            cardCount = DigimonDecksService.prepareDigimon()
            if cardCount == 0:
                print('No valid decks found, aborting')
                return
            print(f"Found {cardCount} unique cards")
            input('Digimon decks prepared. Press [ENTER] to continue')
            print('Fetching cards...')
            images = DigimonCardService.getCardsFromFile(cardCount)
            print('Assembling PDF...')
            PDFService.assemblePDF(images, width, height, margin, '#13160d', 63, 88, hasCardback,
                                   'digimonOutput')  # bgColor for mtg is always black, dpi for MTG is always 196
            print('Done! PDF can be found in ./output/digimonOutput.pdf')
        elif(option == 'c'):
            input('Move card images to input folder, then press [ENTER] to continue\n')
            print('Fetching cards...')
            images = CustomCardService.getCardsFromFile('./input/custom/')
            cardWidth = int(input('Enter card width in mm: \n'))
            cardHeight = int(input('Enter card height in mm: \n'))
            bgColor = input('Enter page background color in hex (#1234AB): \n')
            print('Assembling PDF...')
            PDFService.assemblePDF(images, width, height, margin, bgColor, cardWidth, cardHeight, hasCardback, 'customOutput')
            print('Done! PDF can be found in ./output/customOutput.pdf')
        else:
            print('Invalid Game')
    except BaseException as e:
        print("An error has occured, info: ")
        raise(e)
    finally:
        Utils.cleanTempDir()

    
if __name__ == "__main__":
    main()