from PIL import Image
from typing import List
import os
import fpdf
import shutil

def getTempDir() -> str:
    return getPath('temp')

def getTempFilePath() -> str:
    return getPath('temp', 'tempFile')

def makeTempDir():
    makeDirIfNotExists(getTempDir())
    open(getTempFilePath(), 'w+').close()

def makeDirsIfNotExists():
    makeDirIfNotExists(getPath('input'))
    makeDirIfNotExists(getPath('output'))
    makeDirIfNotExists(getPath('mtgInput'))
    makeDirIfNotExists(getPath('ydkInput'))

def makeDirIfNotExists(path):
    if not os.path.exists(path):
        os.makedirs(path)

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

def getPath(*path) -> str:
    return os.path.abspath(os.path.join(*path))