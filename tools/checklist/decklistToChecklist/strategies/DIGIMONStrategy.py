import os
import sys
from GenericListGenerator import GenericListGenerator
import pandas as pd
from DeckTypes import DIGIMON
from GenericList import GenericList
sys.path.insert(0,"..")

class DIGIMONHandler(GenericListGenerator): 
  
    input_folder = ""
    file_extension = ".txt"

    def __init__(self, input_folder):
        self.input_folder = input_folder
        self.type = DIGIMON

    def getDecklists(self): 
        decklists = []
        for files in os.listdir(self.input_folder):
            decklist = dict()
            with open(os.path.join(self.input_folder, files), 'r') as file:
                next(file)
                next(file)
                card_amounts = []
                card_names = []
                card_serial_codes = []
                for line in file:
                    # Split the line into tokens
                    tokens = line.strip().split()

                    # Extract the card amount, name, and serial code
                    amount = int(tokens[-1])
                    serial_code = tokens[0]
                    name = ' '.join(tokens[1:len(tokens)-1])

                    # Append the extracted values to the corresponding arrays
                    card_amounts.append(amount)
                    card_names.append(name)
                    card_serial_codes.append(serial_code)
                
                deck_dataframe = pd.DataFrame({
                    'expected': card_amounts,
                    'name': card_names,
                    'id': card_serial_codes
                })
                decklist["name"] = os.path.splitext(f'{files}')[0]
                decklist["type"] = DIGIMON
                decklist["dataframe"] = deck_dataframe
                decklists.append(decklist)
        return decklists
    
    def transformDecklistsToGenericLists(self, decklists):
        genericLists = []
        for decklist in decklists:
            genericList = GenericList(decklist["name"])
            genericList.setType(decklist["type"])
            genericList.setDataframeIds(decklist["dataframe"]["id"])
            genericList.setDataframeNames(decklist["dataframe"]["name"])
            genericList.setDataframeExpecteds(decklist["dataframe"]["expected"])
            genericLists.append(genericList)
        self.setGenricLists(genericLists)
