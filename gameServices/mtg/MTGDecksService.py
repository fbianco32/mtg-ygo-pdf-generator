import os
import Utils
from pathlib import Path

IGNORED_LINES = [
    "",
    "SIDEBOARD:",
    "ATTRACTIONS:",
    "STICKERS:"
]

def prepareMTGDecks() -> int:
    cardCount = 0
    cards = []

    for fname in (Path.cwd()/'mtgInput').iterdir():
        cardCount, cards = prepare_txt_deck(cardCount, cards, fname)

    with open(Path.cwd()/'input'/'mtgInput.txt', 'w+') as outfile:
        outfile.writelines(cards)
            
    return cardCount

def prepare_txt_deck(cardCount, cards, fname):
    with open(fname,'r') as infile:
        for line in infile.readlines():
            if(line.rstrip() not in IGNORED_LINES):
                if line[-1] != '\n':
                    line += '\n'
                cards.append(line)
                cardCount += 1
    return cardCount, cards