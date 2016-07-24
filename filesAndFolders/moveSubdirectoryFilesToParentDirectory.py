# unzip zip files in a directory
# move all files from child directory to root directory
# zip all folders in a directory to their zip

import os
import subprocess

rootPath = "/Users/gyanesh/Downloads/New Folder With Items"


def moveFile():
    for directory in os.listdir(rootPath):
        basePath = os.path.join(rootPath, directory)
        if os.path.isdir(basePath):
            done = []
            check = map(lambda x: os.path.join(basePath, x), os.listdir(basePath))
            while check:
                path = check.pop()
                if path in done:
                    continue
                done.append(path)
                if os.path.isdir(path):
                    for tempPath in os.listdir(path):
                        tempPath = os.path.join(path, tempPath)
                        if tempPath not in done and tempPath not in check:
                            check.append(tempPath)
                if os.path.isfile(path) and (path.endswith(".jpg") or path.endswith(".png")):
                    subprocess.call(["mv", path, basePath], shell=False)


def moveDirectory():
    pass


def unzipFiles():
    for file in os.listdir(rootPath):
        filePath = os.path.join(rootPath, file)
        if os.path.isfile(filePath) and filePath.endswith(".zip"):
            newFilePath = os.path.join(rootPath, os.path.splitext(file)[0])
            subprocess.call(["unzip", "-q", filePath, "-d", newFilePath], shell=False)


def zipFiles():
    for dirname in os.listdir(rootPath):
        dirPath = os.path.join(rootPath, dirname)
        if os.path.isdir(dirPath):
            zipName = os.path.join(rootPath, dirname + ".cbz")
            os.chdir(rootPath)
            subprocess.call(["zip", zipName, "-qr", dirname], shell=False)

# unzipFiles()
# moveFile()

# zipFiles()
