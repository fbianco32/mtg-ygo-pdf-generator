import os
import sys
from urllib.request import urlopen 
import json 
from GenericListGenerator import GenericListGenerator
import pandas as pd
from DeckTypes import YGO
from GenericList import GenericList


sys.path.insert(0,"..")
class YGOHandler(GenericListGenerator): 
  
    genericLists = []
    input_folder = ""
    file_extension = ".ydk"
    BASE_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

    def __init__(self, input_folder):
        self.input_folder = input_folder

    def getDecklists(self): 
        decklists = []
        for file in os.listdir(self.input_folder):
            if file.endswith(self.file_extension):
                decklist = dict()
                with open(os.path.join(self.input_folder, file)) as f:
                    lines = f.read().splitlines() 
                    lines = [ x for x in lines if x.isdigit() ]
                    #using pandas for calculating quantity of cards
                    cleanDecklist = pd.Series(lines).value_counts().to_frame() 
                    cleanDecklist = cleanDecklist.reset_index()
                    cleanDecklist.columns = ['id', 'expected']
                    #setting decklist data
                    decklist["name"] = os.path.splitext(f'{file}')[0]
                    decklist["type"] = YGO
                    decklist["dataframe"] = cleanDecklist
                    decklists.append(decklist)
        return decklists


    def transformDecklistsToGenericLists(self, decklists): 
        genericLists = []
        for decklist in decklists:
            genericList = GenericList(decklist["name"])
            genericList.setType(decklist["type"])
            genericList.setDataframeIds(decklist["dataframe"]["id"])
            genericList.setDataframeExpecteds(decklist["dataframe"]["expected"])
            genericLists.append(genericList)
            #print(decklist)
        
        for genericList in genericLists:
            print("GenericList name: " + genericList.getName())
            print("GenericList type: " + genericList.getType())
            print("GenericList dataframe: ")
            print(genericList.getDataframe())

            


        
    def getCardNameById(self, id):
        response = urlopen(self.BASE_URL + f'id?={id}') 
        # storing the JSON response  
        # from url in data 
        data_json = json.loads(response.read()) 
        
        # print the json response 
        print(data_json) 

        