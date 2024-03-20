"""
    Takes the images in the 'OriginalImages' Folder and resizes them to the desired size
"""

import os
from PIL import Image

#Functions
# Resize Function
def resize(image, maximumWidth, maximumHeight):
    width,height = image.size                               # Gets the width and height from the image
    if width < maximumWidth and height < maximumHeight:     # If the height and width are smaller than the maximum
        print('Image Not Resized Smaller Than Maximum')         # Error message logged   
        return image                                            # Return the original image
    elif width >= height:                                   # If the image width is grater than the height
        ratio = height / width                                  # Sets the ratio of height to width
        newHeight = int(ratio * maxWidth)                       # Calculates the new height
        return image.resize((maximumWidth,newHeight))           # Returns the resized image
    else:                                                   # If the images height is grater than the width
        ratio = width / height                                  # Serts the ratio of width to height
        newWidth = int(ratio * maxHeight)                       # Calculates the new width
        return image.resize((newWidth,maxHeight))               # Returns the resized image


# Global Variables
# Where the original files are saved
originalFileDirectory  = '/Users/rich/git/pythonScripts/photoEditing/originalImages'
# Where to save the resized Images
resizedFileDirectory = '/Users/rich/git/pythonScripts/photoEditing/resizeImages/resizedImages'
# File Count
fileCount = 0
# Input variables
# Maximum File Width
maxWidth = int(input('What is the Maximum Width in px? : '))
# Maximum File Height
maxHeight = int(input('What is the Maximum Height in px? : '))

os.chdir(originalFileDirectory)                                     # Sets the directory to where the original files are saved
for file in os.listdir(originalFileDirectory):                      # For each file in the directory
    im = Image.open(f'{originalFileDirectory}/{file}')                  # Open the image
    resizedImage = resize(im,maxWidth,maxHeight)                        # Run the resize Function
    resizedImage.save(f'{resizedFileDirectory}/Resized_{file}')         # Save the resized file in thje resized Directory
    fileCount += 1                                                      # Increments the file count

print(f'------- {fileCount} Files Saved -------')
