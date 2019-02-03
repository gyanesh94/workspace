# Renaming the files from all directories in the given folder

import os
import argparse

BASE_DIR = "/Users/gyanesh/Downloads/New Folder With Items"
TEXT_FILE = "/Users/gyanesh/Downloads/List.txt"

ignored = {".DS_Store"}
# folders = [x for x in os.listdir(path) if x not in ignored]


def argumentParser():
    parser = argparse.ArgumentParser(description='Rename')
    parser.add_argument('-r', action="store", default=None, dest='renameFile', help="Rename File")
    renameFile = parser.parse_args().renameFile
    return renameFile


def renameFiles():
    filesList = [x for x in os.listdir(BASE_DIR) if x not in ignored]
    newNameFile = open(TEXT_FILE, 'r')
    newNameList = newNameFile.readlines()
    renameFile = argumentParser()
    raw_input("Check Read or Print = ")
    for fileName, newFileName in zip(filesList, newNameList):
        fileNamePath = os.path.join(BASE_DIR, fileName)
        if os.path.exists(fileNamePath) and os.path.isfile(fileNamePath) and fileName != "":
            print fileName
            print newFileName
            newFileName = newFileName.strip()
            newFilePath = os.path.join(BASE_DIR, newFileName)
            if renameFile:
                os.rename(fileNamePath, newFilePath)


renameFiles()
