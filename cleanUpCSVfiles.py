##############################################################################################
# This script is necessary because the CSV files created with the meaningless CSVDownloader()
# creates files that are messy and span multiple lines typically, and have other data that
# is not relevant (creation info)
##############################################################################################
import os
import time

folderName="c:\\Temp\\Bible"
newFolderName="c:\\Temp\\BibleCleanFiles\\"
 
# iterate over files in the directory
for filename in os.listdir(folderName):
    fullName = os.path.join(folderName, filename)
    # checking if it is a file
    if os.path.isfile(fullName):
        print("Cleaning up file",fullName)
        fileNameLength=len(filename)
        bookName=filename[4:-4] #stripping off the translation abbreviation and the file extension
        bookNameLength=len(bookName)
        newFileName=newFolderName+filename
        origFile = open(fullName, encoding="utf-8") #open original file
        newFile=open(newFileName,"a", encoding="utf-8") #open new file to create

        prevLine=""
        newLine=True
        lineToKeep=None
        bibleVerses = origFile.readlines()
        startOfFile=True #starting with the very first row
        for dataRow in bibleVerses:
            if startOfFile:
                if dataRow.startswith("Book,Chapter"): #Discarding line 1 - all the files have this beginning line
                    startOfFile=False
                    startingConcatenation=True
                    continue

            if startingConcatenation:
                if dataRow[0:bookNameLength] == bookName:
                    lineToKeep=dataRow
                    startingConcatenation=False
                else:
                    print("Something went wrong, expected next line to start with the bookname.")
                    print("Data row is:",dataRow)
                    print("lineToKeep is:",lineToKeep)
            elif dataRow[0:bookNameLength] != bookName:
                    lineToKeep=lineToKeep+dataRow
            else:
                    dr=lineToKeep.split(",English") #end of data to discard
                    tempLine=dr[0]
                    if tempLine[-2] == "\n":
                        tempLine = tempLine[:-2]
                    if tempLine[-1] != "\"":
                        tempLine = tempLine + "\""
                    newFile.write(tempLine + "\n")
                    #start next line to write
                    lineToKeep=""
                    lineToKeep=dataRow

        print("Done, created new file",newFileName)
        origFile.close()
        newFile.close()
