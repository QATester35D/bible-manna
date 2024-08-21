# bible-manna
Bible for the soul.

This is another of my projects for Python programming. 

Project: To utilize various Bible API's to retrieve a variety of Bible verses and by specific translations or bringing back the verse(s) for ALL the translations for comparison.

Requirements: Initial approach is to use the meaningless API because it has extractor methods to output
the various books of the bible. Unfortunately they don't have an export to create a text file so I'm exporting in CSV format. There is also a lot of extra data with each line in the bible and they wrap lines over multiple lines, so I have to process through each each line, merge lines correctly and then strip off the data I don't need.

Main Programming structures: API calls, file handling and MySQL database queries

Output:
1. The first output is to create the CSV files using the API calls.
2. The second output is modifying the data in the file a little bit and saving as a text file.
3. Reading each text file and inserting the data into the MySQL database I created.