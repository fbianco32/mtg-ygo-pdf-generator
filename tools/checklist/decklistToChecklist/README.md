# Decklist To Checklist

# What is this?
This tool was made to create excel spreadsheets from decks with the purpose of tracking expected cards vs received cards.
It creates a single spreadsheet combining all input decks no matter the deck type.

# Usage
* Run ChecklistGenerator.py  
* Follow the instructions in the console  

## WARININGS
* Modifing the spreadsheet in any other way than using the dropdowns may render it useless for turning it into a missing decklist with the Checklist To Decklist
* There must not be any two deckslist (regardless of the TCG type) with the same file name. This is because each decklists gets its own sheet name based on the file name and excel spreadsheets doesn't allow two sheets with the same name.

## TODO
* Move the fetching of YGO card names to the YGO service
* Remove hardcoded colors and columns in the styles adjustment of the sheets
