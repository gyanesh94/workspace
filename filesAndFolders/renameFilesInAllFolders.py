# Renaming the files from all directories in the given folder

import os
import re

BASE_DIR = "./"


def renameFiles():
    for musicFolderName in os.listdir(BASE_DIR):
        musicFolderPath = os.path.join(BASE_DIR, musicFolderName)
        if os.path.exists(musicFolderPath) and os.path.isdir(musicFolderPath):
            for oldName in os.listdir(musicFolderPath):
                newName = re.sub(r'^[0-9]{2,3}\.? (-|)( |)', '', oldName)
                newName = newName.strip()
                newPath = os.path.join(musicFolderPath, newName)
                oldPath = os.path.join(musicFolderPath, oldName)
                os.rename(oldPath, newPath)

renameFiles()
