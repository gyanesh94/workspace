# Renaming the files for a according to condition

import os
import re

BASE_DIR = ""


def renameFiles():
    if os.path.exists(BASE_DIR) and os.path.isdir(BASE_DIR):
        for oldName in os.listdir(BASE_DIR):
            newName = re.sub(r'\s+', ' ', oldName)
            newName = newName.strip()
            newPath = os.path.join(BASE_DIR, newName)
            oldPath = os.path.join(BASE_DIR, oldName)
            if os.path.isdir(oldPath):
                os.rename(oldPath, newPath)

renameFiles()
