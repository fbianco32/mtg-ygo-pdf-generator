import os

tempDir = './temp/'
tempFilePath = './temp/tempFile'

def makeTempDir():
    os.makedirs(tempDir)
    open(tempFilePath, 'w+').close()

def cleanTempDir():
    os.remove(tempFilePath)
    os.removedirs(tempDir)
