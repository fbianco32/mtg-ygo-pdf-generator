import os
import csv
from pathlib import Path

from gameServices.DeckService import DeckService

IGNORED_LINES = [
    "",
    "SIDEBOARD:",
    "ATTRACTIONS:",
    "STICKERS:"
]

class CustomDecksService(DeckService):
    def prepareDecks() -> int:
        cardCount = 0
        cards = []

        for _ in (Path.cwd()/'input/custom').iterdir():
            cardCount += 1  
                
        return cardCount
