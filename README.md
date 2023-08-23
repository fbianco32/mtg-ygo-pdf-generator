# mtg-ygo-pdf-generator

## Usage

# Yugioh:
    Go to YGOProDeck, create decklists with all the cards to print, export the lists as YDK, and save them in /ydkInput
    Run YDKPreparer.py
    This will output a ygoInput.txt file
    Place that file in /input
    Run YGOPdfGen.py
    This will output the PDF file

# Magic: The Gathering:
    (Recommended): Go to Moxfield and create a list with all the cards to print
    (Recommended): Export as XMAGE .dck file
    (Recommended): Change the extension of the file to .txt
    Place the .txt file in /input and rename it to mtgInput.txt
    Run MTGPdfGen.py
    This will output the PDF file