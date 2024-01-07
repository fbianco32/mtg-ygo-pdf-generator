from typing import List
import shutil
from pathlib import Path

def getTempDir() -> str:
    return Path.cwd()/'temp'

def getTempFilePath() -> str:
    return Path.cwd()/'temp'/'tempFile'

def makeTempDir():
    Path.mkdir(getTempDir(),exist_ok=True)
 
def makeDirsIfNotExists():
    Path.mkdir(Path.cwd()/'input',exist_ok=True)
    Path.mkdir(Path.cwd()/'output',exist_ok=True)
    Path.mkdir(Path.cwd()/'mtgInput',exist_ok=True)
    Path.mkdir(Path.cwd()/'ydkInput',exist_ok=True)
    Path.mkdir(Path.cwd()/'digimonInput',exist_ok=True)


def cleanTempDir():
    shutil.rmtree(getTempDir())

def inchesToMm(num):
    return num * 25.4

def mmToInches(num):
    return num / 25.4

def invert(color_to_convert): 
    table =  str.maketrans('0123456789abcdef', 'fedcba9876543210')
    return '#' + color_to_convert[1:].lower().translate(table).upper()

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_percent(values):
    valuesOut = []
    for value in values:
        valuesOut.append(value/255)
    return valuesOut
