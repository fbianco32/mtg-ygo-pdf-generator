import os
import sys
from urllib.request import Request, urlopen
import json 
from GenericListGenerator import GenericListGenerator
import pandas as pd
from DeckTypes import YGO
from GenericList import GenericList
sys.path.insert(0,"..")

class YGOHandler(GenericListGenerator): 
  
    input_folder = ""
    file_extension = ".ydk"
    BASE_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

    def __init__(self, input_folder):
        self.input_folder = input_folder
        self.type = YGO

    def getDecklists(self): 
        decklists = []
        for file in os.listdir(self.input_folder):
            if file.endswith(self.file_extension):
                decklist = dict()
                with open(os.path.join(self.input_folder, file), encoding='utf-8') as f:
                    lines = f.read().splitlines() 
                    lines = [ x for x in lines if x.isdigit() ]
                    #using pandas for calculating quantity of cards
                    cleanDecklist = pd.Series(lines).value_counts().to_frame() 
                    cleanDecklist = cleanDecklist.reset_index()
                    cleanDecklist.columns = ['id', 'expected']
                    #setting decklist data
                    decklist["name"] = os.path.splitext(f'{file}')[0]
                    decklist["type"] = self.type
                    decklist["dataframe"] = cleanDecklist
                    decklists.append(decklist)
        
        #getting each card name
        print("Fetching cards names")
        for decklist in decklists:
            for ind in decklist["dataframe"].index:
                decklist["dataframe"].at[ind,'name'] = self.getCardNameById(decklist["dataframe"]['id'][ind])

        return decklists


    def transformDecklistsToGenericLists(self, decklists): 
        genericLists = []
        for decklist in decklists:
            genericList = GenericList(decklist["name"])
            genericList.setType(decklist["type"])
            decklist["dataframe"]["id"] = decklist["dataframe"]["id"].map(str)
            genericList.setDataframeIds(decklist["dataframe"]["id"])
            genericList.setDataframeNames(decklist["dataframe"]["name"])
            genericList.setDataframeExpecteds(decklist["dataframe"]["expected"])
            genericLists.append(genericList)
        self.setGenricLists(genericLists)
             
    def getCardNameById(self, id):
        url = self.BASE_URL + f'?id={id}'
        req = Request(url, headers={'User-Agent' : "Magic Browser"}) #header to bypass bot detection in api
        response = urlopen(req) 
        data_json = json.loads(response.read()) 
        name = data_json["data"][0]["name"]
        return name

        