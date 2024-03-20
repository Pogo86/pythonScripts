"""
    Takes the images in the 'OriginalImages' Folder and resizes them to the desired size
"""

import os
from PIL import Image



# Global Variables
# Where the original files are saved
originalFileDirectory  = '/Users/rich/git/pythonScripts/photoEditing/originalImages'
# Where to save the resized Images
renameFileDirectory = '/Users/rich/git/pythonScripts/fileTypeChange/savedImages'
# File Count
fileCount = 0
# Input variables

def getTypeFromUser():
    while True:
        print('What file type would you like to save as?')
        print('[j] for jpg or [p] for png')
        fileType = input().lower()
        match fileType:
            case 'j':
                return '.jpg'
            case 'p':
                return '.png'
            case _:
                print('Extention not found, please try again')
        

os.chdir(originalFileDirectory)                                     # Sets the directory to where the original files are saved
extention = getTypeFromUser()
for file in os.listdir(originalFileDirectory):                     # For each file in the directory
    fileName = file.split('.')[0]
    im = Image.open(f'{originalFileDirectory}/{file}')                  # Open the image
    im.save(f'{renameFileDirectory}/{fileName}{extention}')
    fileCount += 1                                                      # Increments the file count

print(f'------- {fileCount} Files Saved as {extention} -------')
