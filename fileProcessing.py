##############################################################################################
# Process through the text files for each Bible book and insert that data into the database.
##############################################################################################
import os
import time

folderName="c:\\Temp\\BibleCleanFiles\\"
 
# iterate over files in the directory
for filename in os.listdir(folderName):
    fullName = os.path.join(folderName, filename)
    # checking if it is a file
    if os.path.isfile(fullName):
        print("Processing file",fullName)
        origFile = open(fullName, encoding="utf-8") #open original file
        bibleVerses = origFile.readlines()
        startOfFile=True #starting with the very first row
        for dataRow in bibleVerses:
            dr=dataRow.split(",",3)
            dr[3]=dr[3][:-1]
            time.sleep(1)

        print("Done with file",fullName)
        origFile.close()
