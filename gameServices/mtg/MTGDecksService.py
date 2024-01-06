import os
import Utils

IGNORED_LINES = [
    "",
    "SIDEBOARD:",
    "ATTRACTIONS:",
    "STICKERS:"
]

def prepareMTGDecks() -> int:
    cardCount = 0
    cards = []

    for fname in os.listdir(Utils.getPath('mtgInput')):
        with open(Utils.getPath('mtgInput', fname)) as infile:
            for line in infile.readlines():
                if(line.rstrip() not in IGNORED_LINES):
                    if line[-1] != '\n':
                        line += '\n'
                    cards.append(line)
                    cardCount += 1
    
    with open(Utils.getPath('input', 'mtgInput.txt'), 'w+') as outfile:
        outfile.writelines(cards)
            
    return cardCount