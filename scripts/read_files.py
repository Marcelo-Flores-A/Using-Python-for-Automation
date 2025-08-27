# read the file "inputFile.txt" specifying "r" for read-only persmission
inputFile = open("inputFile.txt" , "r")

for line in inputFile:
    line_split = line.split() # line.split splits the lines in the sections divided by blank spaces and return an array of those sections
    if line_split[2] == "P":
        print(line.strip()) # strip() method removes from begining and end of string the followng: blank spaces, tabs and new lines

# print the content of the already read file
''' print(inputFile.read()) '''

# Best practice: close the file to prevent unintented file changes.
inputFile.close()