import os
import Utils

def prepareYDKs() -> int:
    cardCount = 0
    with open(Utils.getPath('input', 'ygoInput.txt'), 'w') as outfile:
        for fname in os.listdir(Utils.getPath('ydkInput')):
            with open(Utils.getPath('ydkInput', fname)) as infile:
                for line in infile:
                    if(line.strip('\n').isnumeric()):
                        outfile.write(line)
                        cardCount += 1
    return cardCount