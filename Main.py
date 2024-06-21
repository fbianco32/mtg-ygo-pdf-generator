import Utils
from gameServices.CardService import CardService
from gameServices.DeckService import DeckService
from gameServices.custom.CustomCardService import CustomCardService
from gameServices.digimon.DGMCardService import DGMCardService
from gameServices.digimon.DGMDecksService import DGMDecksService
from gameServices.lor.LORCardService import LORCardService
from gameServices.lor.LORDecksService import LORDecksService
from gameServices.mtg.MTGCardService import MTGCardService
from gameServices.mtg.MTGDecksService import MTGDecksService
from gameServices.ygo.YGOCardService import YGOCardService
from gameServices.ygo.YGOYdkService import YGOYdkService
from Utils import texts as texts
import PDFService
import argparse


def walkthrough(deckService: DeckService, cardService: CardService, **kwargs):
    option = kwargs['option']
    print(texts[option]['moveToInput'])
    print(texts[option]['howToExport'])
    input(texts[option]['howToExport2'])
    print(texts[option]['preparing'])
    cardCount = deckService.prepareDecks()
    if cardCount == 0:
        print('No valid decks found, aborting')
        return
    print(f"Found {cardCount} unique cards")
    input(texts[option]['prepared'])
    if option != 'c':
        print('Fetching card images...')
        images = cardService.getCardsFromFile(cardCount)
    print('Assembling PDF...')
    PDFService.assemblePDF(
        images,
        kwargs['pageWidth'],
        kwargs['pageHeight'],
        kwargs['margin'],
        texts[option]['color'],
        int(texts[option]['width']) if kwargs['cardWidth'] == "" else kwargs['cardWidth'],
        int(texts[option]['height']) if kwargs['cardHeight'] == "" else kwargs['cardHeight'],
        kwargs['hasCardback'],
        kwargs['hasCutGuides'],
        texts[option]['outputName']
        )
    print(texts[option]['done'])

def main():
    try:
        args = {}
        option = input('Choose game: [Y]GO/[M]TG/[D]igimon/[L]orcana/[C]ustom\n').lower()
        args['option'] = option
        args['pageWidth'] = int(input('Enter page Width (mm): \n'))
        args['pageHeight'] = int(input('Enter page Height (mm): \n'))
        args['cardWidth'] = (input('Enter card Width (mm) ([Enter] for automatic size): \n'))
        args['cardHeight'] = (input('Enter card Height (mm) ([Enter] for automatic size): \n'))
        args['margin'] = int(input('Enter Margin between cards (mm): \n'))
        args['hasCardback'] = False
        args['hasCutGuides'] = False
        cardbackOption = input('Do you want to add a cardback? ([Y][N])\n')
        if(cardbackOption.lower() == 'y'):
            input('Move the cardback.jpg file to input folder, then press [ENTER] to continue\n')
            args['hasCardback'] = True
        cutGuidesOption = input('Do you want to add cut guides? ([Y][N])\n')
        if(cutGuidesOption.lower() == 'y'):
            args['hasCutGuides'] = True
        game_switch(**args)
    except BaseException as e:
        print("An error has occured, info: ")
        raise(e)
    finally:
        Utils.cleanTempDir()


def game_switch(**kwargs):
    option = kwargs['option']
    if option == 'y':
        walkthrough(YGOYdkService, YGOCardService, **kwargs)
    elif option == 'm':
        walkthrough(MTGDecksService, MTGCardService, **kwargs)
    elif option == 'd':
        walkthrough(DGMDecksService, DGMCardService, **kwargs)
    elif option == 'l':
        walkthrough(LORDecksService, LORCardService, **kwargs)
    elif option == 'c':
        walkthrough(None, CustomCardService, **kwargs)
    else:
        print('Invalid Game')
        return


def args():
    argument_parser = argparse.ArgumentParser(description='Create a PDF of your decks')
    oneline = argument_parser.add_argument(
        "--one-line", "-o",
        action='store_true',
        required=False,
        default=False,
        help="Use the command-line with no input prompts"
    )
    if oneline.const:
        options = argument_parser.add_argument_group()
        game = options.add_argument(
            "-g", "--game",
            choices=["d", "l", "m", "c", "y"],
            required=True,
            dest="option",
        )
        page_width = options.add_argument(
            "--page-width", "-pw", "--pw",
            type=int,
            required=True,
            dest="pageWidth",
        )
        page_height = options.add_argument(
            "--page-height", "-ph", "--ph",
            type=int,
            required=True,
            dest="pageHeight",
        )
        card_width = options.add_argument(
            "--card-width", "-cw", "--cw",
            required=False,
            default="",
            type=str,
            dest="cardWidth",
        )
        card_height = options.add_argument(
            "--card-height", "-ch", "--ch",
            required=False,
            default="",
            type=str,
            dest="cardHeight",
        )
        margin = options.add_argument(
            "--margin", "-m",
            default=0,
            type=int,
            required=False,
            dest="margin",
        )
        has_cardback = options.add_argument(
            "--hasCardback",
            default=False,
            action='store_true',
            dest="hasCardback",
        )
        has_cutguides = options.add_argument(
            "--hasCutGuides",
            default=False,
            action='store_true',
            dest="hasCutGuides",
        )
    return argument_parser.parse_args()


if __name__ == "__main__":
    Utils.makeTempDir()
    Utils.makeDirsIfNotExists()
    arguments = args()
    if arguments.one_line:
        dictionary = vars(arguments)
        game_switch(**dictionary)

    else:
        main()

