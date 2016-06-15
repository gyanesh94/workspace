# List Directory Files to a text files

import os

basePath = "/Volumes/Elements/dsAlgoStudy/ReelLearning/"
listFolderPath = "/Volumes/Elements/dsAlgoStudy/ReelLearning/list/"
for i in os.listdir(basePath):
    path = basePath + i
    if os.path.isdir(path):
        os.chdir(path)
        file = open(listFolderPath + i + ".txt", "w")
        text = ""
        for j in os.listdir(path):
            if j != ".DS_Store":
                text = text + j + "\n"
        text = text.strip()
        file.write(text)
        file.close()
