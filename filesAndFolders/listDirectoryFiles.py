# List Directory Files to a text files

import os
import re

basePath = "./"
listFolderPath = "./list/"
listFileName = "list.txt"


def directoryWithinDirectory():
    for i in os.listdir(basePath):
        path = os.path.join(basePath, i)
        if os.path.isdir(path):
            os.chdir(path)
            file = open(os.path.join(listFolderPath, i + ".txt"), "w")
            text = ""
            for j in os.listdir(path):
                if j != ".DS_Store":
                    text = text + j + "\n"
            text = text.strip()
            file.write(text)
            file.close()


def listDirectory():
    text = ""
    for fileName in os.listdir(basePath):
        filePath = os.path.join(basePath, fileName)
        if os.path.isdir(filePath) or filePath == ".DS_Store":
            continue
        # fileName = re.sub(r'_|-', ' ', fileName)
        fileName = re.sub(r'  +', ' ', fileName)
        fileName = fileName.strip()
        text = text + fileName + "\n"
    listFile = open(os.path.join(listFolderPath, "New List.txt"), "w")
    listFile.write(text)
    listFile.close()


def listDirectoryWithinDirectories(directory):
    print directory
    text = ""
    for fileName in os.listdir(directory):
        filePath = os.path.join(directory, fileName)
        if fileName == ".DS_Store":
            continue
        if os.path.isdir(filePath):
            listDirectory(filePath)
            continue
        text = text + fileName + "\n"
    if text != "":
        listFile = open(os.path.join(listFolderPath, listFileName), "a")
        listFile.write(text)
        listFile.close()

directoryWithinDirectory()
