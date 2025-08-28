import os
from pathlib import Path

# Dictionary that defines the structure in which the files will be orginized
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value): # values represent the string in the name of a file
    for category, suffixes in SUBDIRECTORIES.items(): # reads through the dictionary SUBDIRECTORIES
        if value in suffixes: # checks if the file name contains any of the suffixes (.pdf, .m4b, .jpeg, .png, etc...)
            return category
    return "MISC" # MISC for miscellanous files

# printing the category of a given file
print(pickDirectory(".pdf"))

# loops through all the files in the current directory to orginize them into the structure defined as SUBDIRECTORIES
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir(): # check if the item is a directory instead of a file
            continue # If so, skip to the next loop
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True: # if the picked directory doesn't exist yet, create it in the current path
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()