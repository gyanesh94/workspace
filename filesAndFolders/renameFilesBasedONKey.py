# Renaming the files for a given extension in a directory based the name of the file

import os
from renameFilesBasedONKeyConfig import *
import logging

logging.basicConfig(filename=LOGGING_FILE_NAME, format=LOGGING_MESSAGE_FORMAT, datefmt=LOGGING_DATE_FORMAT, level=logging.DEBUG)
nameMapping = {}


def getNameMapping():
    if not os.path.exists(NAME_FILE_PATH):
        logging.error("{file} doesn't exist".format(file=NAME_FILE_PATH))
        return False

    with open(NAME_FILE_PATH, 'r') as nameData:
        for line in nameData.readlines():
            if line.strip() == "":
                continue
            lineArray = line.split(SPLIT_CONDITION, 1)
            if len(lineArray) < 2:
                continue
            key = lineArray[0].strip()
            name = lineArray[1].strip()
            name = name.replace("/", " ").replace("#", " ").replace("$", " ").replace("\\", " ").replace("'", " ").replace('"', " ").replace("\n", " ")
            if key in nameMapping:
                logging.warn("{key} is duplicate while creating nameMapping".format(key=key))
            else:
                if ADD_KEY_TO_NAME:
                    nameMapping[key] = "{key} {name}{extension}".format(key=key, name=name, extension=EXTENSION)
                else:
                    nameMapping[key] = "{name}{extension}".format(name=name, extension=EXTENSION)

    return True


def makeUniqueNameList():
    flag = getNameMapping()
    if not flag:
        exit()
    text = ""
    for key, name in nameMapping.iteritems():
        text = text + name.replace(EXTENSION, "") + "\n"
    with open(NAME_FILE_PATH, "w") as file:
        file.write(text)


def renameFiles():
    flag = getNameMapping()
    if not flag:
        exit()
    for i in os.listdir(BASE_PATH):
        filePath = BASE_PATH + i
        baseName, extension = os.path.splitext(i)
        if baseName in nameMapping and os.path.isfile(filePath) and extension == EXTENSION:
            os.rename(filePath, BASE_PATH + nameMapping[baseName])
        else:
            logging.error("mapping id not present for {key}".format(key=i))

renameFiles()
