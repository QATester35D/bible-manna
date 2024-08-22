
import os
import time
import mysql.connector

################################################
# Database connection to a MySQL database
################################################
mydb = mysql.connector.connect(user='root', password='root', database='biblemanna')
cur = mydb.cursor()

#Retrieve the books written to the database
cur.execute("SELECT DISTINCT books from bible_data")
result = cur.fetchall()
for i in result:
    print(i)
