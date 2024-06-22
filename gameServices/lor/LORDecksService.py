import os
import csv
from pathlib import Path

from gameServices.DeckService import DeckService


class LORDecksService(DeckService):

    def prepareDecks() -> int:
        cardCount = 0
        cards = []

        for fname in (Path.cwd()/'lorInput').iterdir():
            cardCount, cards = prepare_csv_deck(cardCount, cards, fname) if fname.suffix=='.csv' else  prepare_txt_deck(cardCount, cards, fname)  

        with open(Path.cwd()/'input'/'lorInput.txt', 'w+') as outfile:
            outfile.writelines(cards)
                
        return cardCount

def prepare_txt_deck(cardCount, cards, fname):
    with open(fname,'r') as infile:
        for line in infile.readlines():
            if line[-1] != '\n':
                line += '\n'
            cards.append(line)
            cardCount += int(line.split(" ")[0])
    return cardCount, cards

def prepare_csv_deck(cardCount, cards, fname):
    with open(fname,'r') as infile:
        rows = csv.reader(infile) 
        col_names = list(next(rows))
        idxs = {"name" : col_names.index("name"),
                "set" : col_names.index("Set"),
                "code" : col_names.index("Collector Number")}
        for row in rows: #arranca de la linea 2 porque ya hicimos next()
            name = row[idxs["name"]]
            set = row[idxs["set"]]
            code = row[idxs["code"]]
            card = f"1 {name} ({set}) {code}"
            cards.append(card+'\n')
            cardCount+=1
    return cardCount, cards
