from typing import List
import shutil
from pathlib import Path


texts = {
    'y': {
        'moveToInput': "Move the YDK files to input folder, then press [ENTER] to continue",
        'howToExport': "(The YDKs should be exported directly from YGOProDeck, saved as .ydk)",
        'howToExport2': "(Go to your YGOProDeck deck > More > Download YDK or, in the deckbuilder, Export > To .ydk Deck file)\n",
        'preparing': "Preparing YDKs",
        'prepared': "YDK prepared. Press [ENTER] to continue",
        'done': "Done! PDF can be found in ./output/ygoOutput.pdf",
        'color': "#60647f",
        'width': "59",
        'height': "86",
        'outputName': "ygoOutput",
    },
    'm': {
        'moveToInput': "Move decklist files to mtgInput folder, then press [ENTER] to continue",
        'howToExport': "(The decklists should be in Moxfield\'s export format, saved as .txt)",
        'howToExport2': "(Go to your Moxfield deck > Export > Copy full list and save that to a .txt file)\n",
        'preparing': "Preparing decks",
        'prepared': "MTG decks prepared. Press [ENTER] to continue",
        'done': "Done! PDF can be found in ./output/mtgOutput.pdf",
        'color': "#13160d",
        'width': "63",
        'height': "88",
        'outputName': "mtgOutput",
    },
    'l': {
        'moveToInput': "Move decklist files to lorInput folder, then press [ENTER] to continue",
        'howToExport': "#TODO: IMPORT INSTRUCTIONS",
        'howToExport2': "#TODO: IMPORT INSTRUCTIONS\n",
        'preparing': "Preparing decks",
        'prepared': "Lorcana decks prepared. Press [ENTER] to continue",
        'done': "Done! PDF can be found in ./output/lorOutput.pdf",
        'color': "#13160d",
        'width': "63",
        'height': "88",
        'outputName': "lorOutput",
    },
    'd': {
        'moveToInput': "Move decklist files to dgmInput folder, then press [ENTER] to continue",
        'howToExport': "(The decklists should be in digimoncard.app export format, saved as .txt)",
        'howToExport2': "(Go to your digimoncard.app deck > Export > Copy full list and save that to a .txt file)\n",
        'preparing': "Preparing decks",
        'prepared': "Digimon decks prepared. Press [ENTER] to continue",
        'done': "Done! PDF can be found in ./output/dgmOutput.pdf",
        'color': "#13160d",
        'width': "63",
        'height': "88",
        'outputName': "dgmOutput",
    },
    'c': {
        'moveToInput': "Move card images to input folder, then press [ENTER] to continue\n",
        'howToExport': "(The cards should be in .PNG format)",
        'howToExport2': "\n",
        'preparing': "Preparing cards",
        'prepared': "",
        'done': "Done! PDF can be found in ./output/customOutput.pdf",
        'color': "#13160d",
        'width': "63",
        'height': "88",
        'outputName': "customOutput",
    }
}

def getTempDir() -> str:
    return Path.cwd()/'temp'

def getTempFilePath() -> str:
    return Path.cwd()/'temp'/'tempFile'

def makeTempDir():
    Path.mkdir(getTempDir(),exist_ok=True)
 
def makeDirsIfNotExists():
    Path.mkdir(Path.cwd()/'input',exist_ok=True)
    Path.mkdir(Path.cwd()/'output',exist_ok=True)
    Path.mkdir(Path.cwd()/'mtgInput',exist_ok=True)
    Path.mkdir(Path.cwd()/'ydkInput',exist_ok=True)
    Path.mkdir(Path.cwd()/'dgmInput',exist_ok=True)

def cleanTempDir():
    shutil.rmtree(getTempDir())


def invert(color_to_convert): 
    table =  str.maketrans('0123456789abcdef', 'fedcba9876543210')
    return '#' + color_to_convert[1:].lower().translate(table).upper()

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_percent(values):
    valuesOut = []
    for value in values:
        valuesOut.append(value/255)
    return valuesOut
