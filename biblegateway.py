##############################################################################################
# This is a standalone script to use an API to retrieve data from an online Bible.
# This script uses the API for api.bible 
# References: https://docs.api.bible/guides/bibles/ and https://scripture.api.bible/livedocs#/ 
##############################################################################################
import requests
import json
import time
import os
import urllib.request, urllib.parse, urllib.error
from collections import defaultdict

class BibleGetInsight:
    def __init__(self):
        # One format: https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01
        self.bibleAPIURL =  "https://api.scripture.api.bible"
        self.API_KEY = 'c0688c91b5867edc8faf256a9ee319ca'

    def getBibleData(self, urlRemainder):
        #pass in remainder of URL for the desired query; urlRemainder looks similar to: /v1/bibles
        #Need to build url = "https://api.scripture.api.bible/v1/bibles"
        url=self.bibleAPIURL+urlRemainder
        API_KEY=self.API_KEY
        headers = {'api-key': API_KEY}
        response = requests.request("GET", url, headers=headers)
        theJSON = json.loads(response.content)
        # print(response.text)
        if response.status_code != 200:
            print ("Problem connecting with api.bible API at https://api.scripture.api.bible .")
            exit
        
        try:
            theJSON = json.loads(response.content)
        except:
            theJSON = None
        
        # if not theJSON or 'type' not in theJSON :
        if not theJSON:
            print('==== Failure To Retrieve ====')
            print(response.content)
        return theJSON

# ##### Flat file work when API is down
# fname="c:\\Temp\\bibleGenesisDataStrong.txt"
# dataStrongFile="c:\\Temp\\dataStrongOnly.txt"
# createFile=True
# performFlatFileOps=False

# if performFlatFileOps:
#     f = open(fname)
#     theJSON=f.read()
#     f.close()

#     # theJSON = json.loads(f.content)

# ########################################################################
# ##### Bible Translation Choices - Bible IDs
# bibleId='926aa5efbc5e04e2-01' #German Luther Bible 1912 with Strong's numbers (in German but appears to be the only one with Strong's numbers)
# # bibleId='06125adad2d5898a-01' #The Holy Bible, American Standard Version - no data strong
# bibleId='685d1470fe4d5c3b-01'  #American Standard Version (Byzantine Text with Apocrypha) - New Testament only
bibleId='de4e12af7f28f599-01'  #King James (Authorised) Version
# bibleId='de4e12af7f28f599-02'  #King James (Authorised) Version
# bibleId='9879dbb7cfe39e4d-01'  #World English Bible
# bibleId='7142879509583d59-01'  #World English Bible British Edition - 
# bibleId='72f4e6dc683324df-01'  #World English Bible Updated - 
# bibleId='32664dc3288a28df-01'  #World English Bible, American English Edition, without Strong's Numbers - 
# bibleId='f72b840c855f362c-04'  #World Messianic Bible - New Testament only
# bibleId='66c22495370cdfc0-01'  #Translation for Translators - 
# bibleId='2f0fd81d7b85b923-01'  #The English New Testament According to Family 35 - New Testament only
# bibleId='c89622d31b60c444-02'  #The Orthodox Jewish Bible
# bibleId='65bfdebd704a8324-01'  #Brenton English translation of the Septuagint
# bibleId='65eec8e0b60e656b-01'  #Free Bible Version - 
# bibleId='c315fa9f71d4af3a-01'  #Geneva Bible - 


####### Examples of building the URLs to call. There is a bit of a hierarchy you have to call to drill down in the Bible
# bibleChapterId='GEN.2'
# url = "/v1/bibles/"+bibleId
# url = "/v1/bibles/"+bibleId+"/chapters/"+bibleChapterId
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/books"
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/books/GEN"
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/chapters/GEN.1"
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/verses/GEN.1.1"
a=BibleGetInsight()
API_KEY=a.API_KEY
headers = {'api-key': API_KEY}
#Using this site https://scripture.api.bible/livedocs#/Books/getBooks to get more parameters for data values
url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/books?include-chapters=true&include-chapters-and-sections=true"
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/verses/MAT.1.1"
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)

# Keyword search for passages containing the word
keywordSearch=input("What is the specific keyword you want to search for in the Bible? ")
limitOfPassagesToBringBack=input("How many total passages do you want to bring back that match the keyword? ")
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/search?query=discouraged&limit=10&sort=relevance"
url = "/v1/bibles/"+bibleId+"/search?query="+keywordSearch+"&limit="+limitOfPassagesToBringBack+"&sort=relevance"
getPassagesForKeyword=a.getBibleData(url)
print("The passage results for the keyword are as follows:",getPassagesForKeyword)
for i in getPassagesForKeyword['data']['verses']:
    bookVerse=i['reference']
    verseMatch=i['text']
    print("Matching verse(s) are:")
    print(f"{bookVerse} - {verseMatch}")

time.sleep(1)

########################################################################

#Get all the available Bible versions/translations
print("Retrieving all Bibles available with this API.")
bibles=a.getBibleData("/v1/bibles")

# bibleName="The Holy Bible, American Standard Version"
bibleName=input("What Bible do you want to work with (the name must be exact)? ")
#Using the Bible name, retrieve the Bible ID for it
for i in bibles["data"]:
    if i["name"] == bibleName:
        bibleId=i["id"]
        print("The Bible ID for the bible",bibleName,"is",bibleId)
        break

########################################################################
# Retrieving the specific Bible by ID - The Holy Bible, American Standard Version - 06125adad2d5898a-01
# bibleId='06125adad2d5898a-01'
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01"
url = "/v1/bibles/"+bibleId
specificBible=a.getBibleData(url)

################################################################
# Get all the books in this Bible
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books"
url = "/v1/bibles/"+bibleId+"/books"
getAllBibleBooks=a.getBibleData(url)
ctr=0
booksInGLB = []
for i in getAllBibleBooks['data']:
    print (getAllBibleBooks['data'][ctr]['id'])
    bk=getAllBibleBooks['data'][ctr]['id']
    booksInGLB.append(bk)
    ctr=ctr+1
#Find a specific Book in the Bible and get it's ID
# bibleBook="Genesis"
# bibleBook=input("What specific Bible book do you want to retrieve (provide name like Genesis): ")
# for i in getAllBibleBooks["data"]:
#     if i["name"] == bibleBook:
#         bibleBookId=i["id"]
#         break

################################################################
# Retrieve the specific book
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/GEN"
# #skipping this section of code
# for i in booksInGLB:
#     # url = "/v1/bibles/"+bibleId+"/books/"+bibleBookId
#     url = "/v1/bibles/"+bibleId+"/books/"+i
#     getSpecificBibleBook=a.getBibleData(url)
#     print("The specific book is:",getSpecificBibleBook)

################################################################
################################################################
# Get all chapters for the specified book
# /v1/bibles/{bibleId}/books/{bookId}/chapters
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/GEN/chapters"
# print("Retrieving all chapters from",bibleBook)
nbrOfBooks=len(booksInGLB) #This is a list of books like GEN, EXO, LEV, NUM
for nbrBooksCtr in range(nbrOfBooks):
    #Now retrieve each chapter out of each book one at a time
    url = "/v1/bibles/"+bibleId+"/books/"+booksInGLB[nbrBooksCtr]+"/chapters"
    getAllBibleChapters=a.getBibleData(url)
    # print("All the chapters for this book are:",getAllBibleChapters)

    # bibleChapter="20"
    # bibleChapter=input("What chapter in this book do you want? Needs to be in the expected format (like 33): ")
    nbrOfChapterInBook=len(getAllBibleChapters['data'])
    # for nbrChptsCtr in nbrOfChapterInBook:
    #     getAllBibleChapters["data"]
    #     if i["number"] == bibleChapter:
    #         bibleChapterId=i["id"] #Retrive the ID for the specified chapter
    #         break

    # url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.2"
    # Using the ID for the specified chapter, retrieve the chapter
    for nbrChptsCtr in range(nbrOfChapterInBook):
        bookNbr=nbrChptsCtr+1
        bibleChapterId=booksInGLB[nbrBooksCtr]+"."+str(bookNbr)
        url = "/v1/bibles/"+bibleId+"/chapters/"+bibleChapterId
        getSpecificBibleChapter=a.getBibleData(url)
        tempLine=getSpecificBibleChapter["data"]["content"]
        #Write the chapter to a text file
        folderName="c:\\Temp\\Bible"
        newFileName="GLB_"+booksInGLB[nbrBooksCtr]+".txt"
        newFile=open(newFileName,"a", encoding="utf-8")
        newFile.write(tempLine + "\n")
 
        print("The specific chapter desired from this book is:",getSpecificBibleChapter)

########### stop here for getting everything in a chapter

################################################################
# Bring back all verses in the specified chapter mentioned above
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.1/verses"
url = "/v1/bibles/"+bibleId+"/chapters/"+bibleChapterId+"/verses"
getVersesForChapter=a.getBibleData(url)
print("Getting all verses for the chapter:",getVersesForChapter)

################################################################
# Retrieving a range of chapters
# /v1/bibles/{bibleId}/passages/{passageId}
startingChapter=input("Provide the chapter to start retrieving from: ")
startingChapter=booksInGLB[0]+"."+startingChapter
endingChapter=input("Provide the ending chapter to end with: ")
endingChapter=booksInGLB[0]+"."+endingChapter
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/passages/GEN.1.1-GEN.1.2"
url = "/v1/bibles/"+bibleId+"/passages/"+startingChapter+"-"+endingChapter
getBibleChapterRange=a.getBibleData(url)
print("The Bible chapter range results are:",getBibleChapterRange)

# Bring back all verses in the specified chapter mentioned above
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.1/verses"
url = "/v1/bibles/"+bibleId+"/chapters/"+bibleChapterId+"/verses"
getVersesForChapter=a.getBibleData(url)
print("Getting all verses for the chapter:",getVersesForChapter)

# Retrieve the specific verse in a chapter desired
bibleVerse=input("What is the specific verse you want to retrieve for the chapter you are in (like 1 for verse 1? ")
# /v1/bibles/{bibleId}/verses/{verseId}
# url = "/v1/bibles/"+bibleId+"/verses/GEN.1.1"
url = "/v1/bibles/"+bibleId+"/verses/"+bibleChapterId+"."+bibleVerse
getSpecifiedVerse=a.getBibleData(url)
print("The specific verses requested is:",getSpecifiedVerse)
time.sleep(1)