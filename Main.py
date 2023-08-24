import Utils
import MTGCardService
import YGOCardService
import YGOYdkService
import sys

def main():
    try:
        Utils.makeTempDir()
        option = input('Choose game: [Y]GO/[M]TG\n')
        if(option == 'Y'):
            input('Move YDK files to input folder, then press [ENTER] to continue')
            print('Preparing YDK')
            YGOYdkService.prepareYDKs()
            input('YDK prepared. Move ./output/ygoInput.txt to ./input/ygoInput.txt then press [ENTER] to continue')
            print('Fetching card images...')
            images = YGOCardService.getCardsFromFile('./input/ygoInput.txt')
            print('Assembling PDF...')
            images[0].save('output/ygoOutput.pdf', "PDF", save_all=True, append_images=images[1:])
            print('Done! PDF can be found in ./output/ygoOutput.pdf')
        elif(option == 'M'):
            print('Move decklist file to input folder, rename it to "mtgInput.txt", then press [ENTER] to continue')
            print('(The decklist should be in XMAGE .dck format, with the extension changed to .txt)')
            input('(Its recommended to make a big list with all cards and export via moxfield > xmage.dck)')
            print('Fetching cards...')
            images = MTGCardService.getCardsFromFile('./input/mtgInput.txt')
            print('Assembling PDF...')
            images[0].save('output/mtgOutput.pdf', "PDF", save_all=True, append_images=images[1:])
            print('Done! PDF can be found in ./output/mtgOutput.pdf')
        else:
            print('Invalid Game')
    except BaseException as e:
        print("An error has occured, info: " + str(e))
    finally:
        Utils.cleanTempDir()

    
if __name__ == "__main__":
    main()