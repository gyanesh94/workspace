import zipfile
import os

zf = zipfile.ZipFile('test.zip', mode='w')
zf.write("untitled folder")
zf.close()

os.rename("test.zip", "test.cbz")
