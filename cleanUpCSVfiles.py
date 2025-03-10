##############################################################################################
# This script is necessary because the CSV files created with the meaningless CSVDownloader()
# creates files that are messy, span multiple lines typically, and have other data that
# is not relevant (creation info). This script processes through each text file to clean them
# up in order to then be read to insert into the database.
##############################################################################################
import os
import time

# folderName="c:\\Temp\\BibleTempFiles"
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
                    print("Something went wrong, working with file",filename,"expected next line to start with the bookname.")
                    print("Data row is:",dataRow)
                    print("lineToKeep is:",lineToKeep)
            elif dataRow[0:bookNameLength] != bookName:
                    if lineToKeep[-1] == "\n":
                        lineToKeep = lineToKeep[:-1]
                    lineToKeep=lineToKeep+" "+dataRow
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

        #Write the last line from the file
        if lineToKeep != None:
            dr=lineToKeep.split(",English") #end of data to discard
            tempLine=dr[0]
            if tempLine[-2] == "\n":
                tempLine = tempLine[:-2]
            if tempLine[-1] != "\"":
                tempLine = tempLine + "\""
            newFile.write(tempLine + "\n")

        dr=tempLine=lineToKeep=dataRow=None
        print("Done, created new file",newFileName)
        origFile.close()
        newFile.close()
