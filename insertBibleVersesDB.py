import os
import mysql.connector

################################################
# Database connection to a MySQL database
################################################
mydb = mysql.connector.connect(user='root', password='root', database='biblemanna')
cur = mydb.cursor()

################################################
# Process through all the text files
################################################
folderName="c:\\Temp\\BibleCleanFiles\\"
 
# iterate over files in the directory
for filename in os.listdir(folderName):
    fullName = os.path.join(folderName, filename)
    if os.path.isfile(fullName):  # checking if it is a file
        print("Processing file",fullName)
        bibleTranslation=filename[0:3]
        origFile = open(fullName, encoding="utf-8") #open original file
        bibleVerses = origFile.readlines()
        for dataRow in bibleVerses:
            dr=dataRow.split(",",3)
            dr[3]=dr[3][:-1]
            books=dr[0]
            chapters=dr[1]
            verses=dr[2]
            passage=dr[3]
            ################################################
            # Inserting values
            ################################################
            # columns: bibleTranslation, books, chapters, verses, passage
            sql = "INSERT INTO bible_data (bibleTranslation, books, chapters, verses, passage) VALUES (%s, %s, %s, %s, %s)"
            # val = ("NIV","1 Chronicles",1,1,"¹ Adam, Seth, Enosh, ")
            val = (bibleTranslation, books, chapters, verses, passage)
            cur.execute(sql, val)
            mydb.commit()

        print("Done with file",fullName)
        origFile.close()
        