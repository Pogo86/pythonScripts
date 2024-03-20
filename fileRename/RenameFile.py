"""
    Takes the images in the 'OriginalImages' Folder and saves them witht he new name in the 
"""
import os
from PIL import Image

# Global Variables
# Where the original files are saved
originalFileDirectory  = '/Users/rich/git/pythonScripts/photoEditing/originalImages'
# Where to save the renamed Images
renameFileDirectory = '/Users/rich/git/pythonScripts/fileRename/savedImages'
# File Count
fileCount = 0

# Functions
def getNewName():
    while True:                                             # Loop untill a valid name is given
        print('What would you like to name the files?')     
        newName = input().title()                               # Gets file name from user and capitlazes first letter of each word
        if newName == '':                                       # Checks a file name has been given
            print('Please enter a file name')                       # If no name given askes again
        else:                                                   # If a file name has been given
            return ''.join(newName.split())                         # Returns the file name with any whitespace removed


# Main 
fileName = getNewName()
os.chdir(originalFileDirectory)                                         # Sets the directory to where the original files are saved
for file in os.listdir(originalFileDirectory):                              # For each file in the directory
    extention = file.split('.')[-1]                                         # Gets the original file type
    im = Image.open(f'{originalFileDirectory}/{file}')                      # Open the image
    im.save(f'{renameFileDirectory}/{fileName}{fileCount}.{extention}')     # Saves the file in the new directory with the new name and a number
    fileCount += 1                                                          # Increments the file count

print(f'------- {fileCount} Files Saved as {fileName} -------')
