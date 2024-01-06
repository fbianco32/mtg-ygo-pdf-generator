import os
import Utils
from pathlib import Path

def prepareYDKs() -> int:
    cardCount = 0
    with open(Path.cwd()/'input'/'ygoInput.txt', 'w') as outfile:
        for fname in (Path.cwd()/'ydkInput').iterdir():
            with open(fname,'r') as infile:
                for line in infile:
                    if(line.strip('\n').isnumeric()):
                        outfile.write(line)
                        cardCount += 1
    return cardCount