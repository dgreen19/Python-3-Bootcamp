import os
from zipfile import ZipFile
from os.path import basename, join
from os import walk

with ZipFile('sampleDir.zip', 'w') as zipObj:
# zip = ZipFile('/Users/dgreen/Pictures/Wallpapers', 'w')
    for folderName, subfolders, file in walk('/Users/dgreen/Pictures/Wallpapers'):
        for filename in file:
            filePath = join(folderName, filename)
            zipObj.write(filePath, basename(filePath))