# mtg-ygo-pdf-generator

# Usage

* Run Main.py  
* Follow the instructions in the console  

## TODO
* Tune margin logic/bleed to extend art intelligently   
* Center Cards  
* Send requests to scryfall/ygopro in batch (idk if possible)  
* Add integration with Pokemon TCG API   
* Add data validation on user input


## TEMPLATES
Magic:
"M
73
98


5
Y

N
"
Yugioh: 
"Y
69
96


5
Y

N
"

## OneLine Execution (with examples Based on Templates)

---
To use a single command in the cmd to run the program we need to use the ``-o`` or ``--one-line`` argument,
indicating that we intend to use the One-Line execution.
the options are the following:

| Argument            | Description                                                  | Usage              | Required? | Type | Defaults |
|---------------------|--------------------------------------------------------------|--------------------|-----------|------|----------|
| -g / --game         | Used to select the game (referred inside the code as option) | -g {d, l, m, c, y} | Yes       | str  | -        |
| -pw / --page-width  | Used to define the width of the page                         | -pw <int\>         | Yes       | int  | -        |
| -ph / --page-height | Used to define the height of the page                        | -ph <int\>         | Yes       | int  | -        |
| -cw / --card-width  | Used to define card width (if not present, pw will be used)  | -cw <int\>         | No        | int  | ^pw      |
| -ch / --card-height | Used to define card height (if not present, ph will be used) | -ch <int\>         | No        | int  | ^ph      |
| -m / --margin       | Used to define the margin used                               | -m <int\>          | No        | int  | 0        |
| --hasCardback       | If present will use input/cardback.jpg                       | --hasCardback      | No        | -    | False    |
| --hasCutGuides      | If present will provide Cut Guides on the print              | --hasCutGuides     | No        | -    | False    |

### Examples
* Magic (Width: 73, Height: 98, Margin: 5, No CardBack, No CutGuide, card takes whole page)
```commandline
python3 main.py -o -g m --page-width 73 --page-height 98 -m 5
```
* Yu-Gi-Oh (Width: 69, Height: 96, Margin: 5, With CardBack, With CutGuide, card takes whole page)
```commandline
python3 main.py --one-line --game y --pw 69 --ph 96 -m 5 --hasCardback --hasCutGuides
```