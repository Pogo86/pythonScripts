"""
    Takes the images in the 'OriginalImages' Folder and resizes them to the desired size
"""

import os
from PIL import Image
from rembg import remove

#Functions

# Global Variables
# Where the original files are saved
originalFileDirectory  = '/Users/rich/git/pythonScripts/photoEditing/originalImages'
# Where to save the resized Images
saveDirectory = '/Users/rich/git/pythonScripts/photoEditing/removeBackground/savedImages'
# File Count
fileCount = 0


os.chdir(originalFileDirectory)                                     # Sets the directory to where the original files are saved
for file in os.listdir(originalFileDirectory):                      # For each file in the directory
    im = Image.open(f'{originalFileDirectory}/{file}')              # Open the image
    fileName = file.split('.')[0]
    output = remove(im)
    output.save(f'{saveDirectory}/{fileName}.png')
    fileCount += 1                                                      # Increments the file count

print(f'------- {fileCount} Files Saved -------')
