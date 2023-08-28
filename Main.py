import Utils
import MTGCardService
import YGOCardService
import YGOYdkService
import CustomCardService

def main():
    try:
        Utils.makeTempDir()
        option = input('Choose game: [Y]GO/[M]TG/[C]ustom\n').lower()
        width = input('Enter page Width (mm): \n')
        height = input('Enter page Height (mm): \n')
        margin = input('Enter Margin between cards (mm): \n')
        if(option == 'y'):
            print('Move YDK files to input folder, then press [ENTER] to continue')
            print('(The YDKs should be exported directly from YGOProDeck, saved as .ydk)')
            input('(Go to your YGOProDeck deck > More > Download YDK or, in the deckbuilder, Export > To .ydk Deck file)')
            print('Preparing YDK')
            YGOYdkService.prepareYDKs()
            input('YDK prepared. Press [ENTER] to continue')
            print('Fetching card images...')
            images = YGOCardService.getCardsFromFile('./input/ygoInput.txt')
            print('Assembling PDF...')
            Utils.assemblePDF(images, width, height, margin, '#60647f', 59, 86, 'ygoOutput') # bgColor for mtg is always gray, dpi for YGO is always 187
            print('Done! PDF can be found in ./output/ygoOutput.pdf')
        elif(option == 'm'):
            print('Move decklist file to input folder, rename it to "mtgInput.txt", then press [ENTER] to continue')
            print('(The decklist should be in Moxfield\'s export format, saved as .txt)')
            input('(Go to your Moxfield deck > Export > Copy full list and save that to a .txt file)')
            print('Fetching cards...')
            images = MTGCardService.getCardsFromFile('./input/mtgInput.txt')
            print('Assembling PDF...')
            Utils.assemblePDF(images, width, height, margin, '#13160d', 63, 88, 'mtgOutput') # bgColor for mtg is always black, dpi for MTG is always 196
           # images[0].save('output/mtgOutput.pdf', "PDF", save_all=True, append_images=images[1:], dpi=(196,196))
            print('Done! PDF can be found in ./output/mtgOutput.pdf')
        elif(option == 'c'):
            input('Move card images to input folder, then press [ENTER] to continue')
            print('Fetching cards...')
            images = CustomCardService.getCardsFromFile('./input/custom/')
            dpi = int(input('Enter images DPI: '))
            print('Assembling PDF...')
            images[0].save('output/customOutput.pdf', "PDF", save_all=True, append_images=images[1:], dpi=(dpi,dpi))
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