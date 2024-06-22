import os
import Utils
from pathlib import Path

from gameServices.DeckService import DeckService

class DGMDecksService(DeckService):

  def prepareDecks() -> int:
    cardCount = 0

    with open(Path.cwd()/'input'/'digimonInput.txt', 'w') as outfile:
      for fname in (Path.cwd()/'digimonInput').iterdir():
        with open(fname, 'r') as infile:
          next(infile)
          next(infile)
          for line in infile:
            textInLine = line.split()
            quantity = int(textInLine[-1])
            id = textInLine[0]
            for i in range(quantity):
              outfile.writelines(id+"\n")
              cardCount += 1
    return cardCount