# bible-manna
Bible for the soul.

This is another of my projects for Python programming. 

Project: To utilize various Bible API's to retrieve a variety of Bible verses and by specific translations or bringing back the verse(s) for ALL the translations for comparison. I use this in many ways and in particular for my own Bible studying. The various code contains a lot of snippets to retrieve verses from various Bible translations and in some cases I write results to a text file and ultimately to a MySQL database.

Requirements: Initial approach is to use the meaningless API because it has extractor methods to output the various books of the bible. Unfortunately they don't have an export to create a text file so I'm exporting in CSV format. There is also a lot of extra data with each line in the bible and they wrap lines over multiple lines, so I have to process through each each line, merge lines correctly and then strip off the data I don't need.

Main Programming structures: API calls, file handling and MySQL database queries

Output:
bibleBooks.py - this script contains dictionaries of the books in the Bible, the various Bible translations and a method to identify which one is being passed in.

bibleDataStrong.py - this retrieves the Strong's data values for the "German Luther Bible 1912" translation as it is the only translation available to me that includes the Strong's numbers. I process through each book in the Bible extracting the Strong's numbers for each verse in the Bible.

bibleGateway.py - this has methods that use the api.bible API to retrieve a specified Bible Translation and write the Bible to a text file by Book.

bibleMeaninglessPkg.py - use the methods in a python package called Meaningless to retrieve various aspects of a Bible translation. It is used only in this script.

cleanUpCSVfiles.py - the csv files created have a bunch of formatting issues and extra data. This script cleans up the files for later use.

insertBibleVersesDB.py - this inserts passage by passage, for each book in the Bible into the database for later use.

retrieveBooksFromDB.py - this is the start of a script that then extracts data from the database using SQL statements.