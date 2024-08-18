import os

# Process through the folder
folderName="c:\\Temp\\Bible"
# fileName=get file
newFolderName="c:\\Temp\\BibleCleanFiles\\"
 
# iterate over files in the directory
for filename in os.listdir(folderName):
    fullName = os.path.join(folderName, filename)
    # checking if it is a file
    if os.path.isfile(fullName):
        #start temp code
        filename="NIV_1 Corinthians.txt"
        fullname="c:\\Temp\\Bible\\NIV_1 Corinthians.txt"
        #end temp code
        print("Cleaning up file",fullName)
        bookName=filename.s
        newFileName=newFolderName+filename
        origFile = open(fullName) #open original file
        newFile=open(newFileName,"a") #open new file to create
        bibleVerses = origFile.readlines()
        for dataRow in bibleVerses:
            # dataRow=origFile.read()
            #sample of data row:
            #Book,Chapter,Passage,Text,Language,Translation,Timestamp,Meaningless
            #1 Chronicles,1,1,"¹ Adam, Seth, Enosh, ",English,NIV,2024-08-16T15:45:34.631427-04:00,1.0.0
            # dataRow="1 Chronicles,1,1,\"¹ Adam, Seth, Enosh, \",English,NIV,2024-08-16T15:45:34.631427-04:00,1.0.0"
            dr=dataRow.split(",English") #end of data to discard
            splitTwo=dr[0].split(",",3)
            if dataRow.startswith("Book,Chapter,",1):
                continue
            elif 
            

        origFile.close()
        newFile.close()
