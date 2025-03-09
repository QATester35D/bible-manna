# bible-manna
Bible for the soul.

Project: To utilize various Bible API's to retrieve a variety of Bible verses and by specific translations or bringing back the verse(s) for ALL the translations for comparison. I use this in many ways and in particular for my own Bible studying. 

*Note: This is a work in progress. Everything developed works, but each script functions to perform specific tasks. 
 - The initial task was to retrieve an entire Bible writing each book to it's own text file, cleanup the text files as there are many structural issues with the data that is returned, and then load each book in a database. All this has been completed.
 - Additionally the Strong's numbers will be extracted from the German Luther Bible 1912 with Strong's numbers (the only one available to me that contains the Strong's numbers) and they are stored in a separate table.
 - Finally another script (Class and methods) will be developed to generate trivia questions.

The main file written for bringing back verse(s) is this one using the python package called Meaningless
which is only used in this script. Note: the reference "Meaningless" they used, is based on Ecclesiastes 1 - "Everything Is Meaningless" - "The words of the Teacher, son of David, king in Jerusalem"

bibleMannaVerses.py - I wrote a couple of classes and methods to bring back combinations of:
- get a single verse
- get multiple verses
- retrieve all the available Bible translations to this package, for the specified verse(s)
- write the results to a text file 

*There are 27 different translations available (see the bibleMannaHelperFile.py)

I did some other work in other files (see below) where I retrieve entired the entire Bible one book at a time and saved it as a csv file. Then processed through the book to remove the various special characters and cleanup lines so I could use the text in an effective way. I then processed through the csv files and inserted them into a MySQL database I created so one translation of the Bible I have in a database. With the verses in a database I can do various queries.

Files:
bibleBooks.py - this script contains dictionaries of the books in the Bible, the various Bible translations and a method to identify which one is being passed in.

bibleDataStrong.py - this retrieves the Strong's data values for the "German Luther Bible 1912" translation as it is the only translation available to me that includes the Strong's numbers. I process through each book in the Bible extracting the Strong's numbers for each verse in the Bible.

bibleGateway.py - this has methods that use the api.bible API to retrieve a specified Bible Translation and write the Bible to a text file by Book.

cleanUpCSVfiles.py - the csv files created have a bunch of formatting issues and extra data. This script cleans up the files for later use.

insertBibleVersesDB.py - this inserts passage by passage, for each book in the Bible into the database for later use.

retrieveBooksFromDB.py - this is the start of a script that then extracts data from the database using SQL statements.