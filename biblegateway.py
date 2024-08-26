##############################################################################################
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

## Move this code down to the stop here section 
biblePassage=""
from bs4 import BeautifulSoup
dataStrongVerse = []

#     # for item in theJSON:
#     # biblePassage=(theJSON['data']['content'])
#     biblePassage=theJSON #temporary for dealing with files
biblePassage="'<p class=\"p\"><span data-number=\"1\" data-sid=\"GEN 1:1\" class=\"v\">1</span>Am <span data-strong=\"H7225\" class=\"w\">Anfang</span> <span data-strong=\"H1254\" class=\"w\">schuf</span> <span data-strong=\"H0430\" class=\"w\">Gott</span> <span data-strong=\"H8064\" class=\"w\">Himmel</span> und <span data-strong=\"H0776\" class=\"w\">Erde</span>. <span data-number=\"2\" data-sid=\"GEN 1:2\" class=\"v\">2</span>Und die <span data-strong=\"H0776\" class=\"w\">Erde</span> <span data-strong=\"H1961\" class=\"w\">war</span> <span data-strong=\"H8414\" class=\"w\">wüst</span> und <span data-strong=\"H0922\" class=\"w\">leer</span>, und es war <span data-strong=\"H2822\" class=\"w\">finster</span> auf der <span data-strong=\"H6440\" class=\"w\">Tiefe</span>; und der <span data-strong=\"H7307\" class=\"w\">Geist</span> <span data-strong=\"H0430\" class=\"w\">Gottes</span> <span data-strong=\"H7363\" class=\"w\">schwebte</span> <span data-strong=\"H5921\" class=\"w\">auf</span> dem <span data-strong=\"H6440\" class=\"w\">Wasser</span>. <span data-number=\"3\" data-sid=\"GEN 1:3\" class=\"v\">3</span>Und <span data-strong=\"H0430\" class=\"w\">Gott</span> <span data-strong=\"H0559\" class=\"w\">sprach</span>: Es <span data-strong=\"H1961\" class=\"w\">werde</span> <span data-strong=\"H0216\" class=\"w\">Licht</span>! und es ward <span data-strong=\"H0216\" class=\"w\>Licht</span>"

soup = BeautifulSoup(biblePassage, "html.parser")
# if os.path.exists(dataStrongFile): # Check if the file exists
#     os.remove(dataStrongFile) # If it exists, delete the file
# f = open(dataStrongFile, "a")

for link in soup.find_all('span'):
    if link.has_attr('class'):
        if link['class'][0] == 'v':
            bookChapterVerse=link.attrs['data-sid']
        if link['class'][0] == 'w':
            if link.has_attr('data-strong'):
                dataStrongHebrewWord=link.attrs['data-strong']
                # dataStrongVerse.append(link.attrs['data-strong'])
                dataStrongVerse.append(dataStrongHebrewWord)
                time.sleep(1)
#                 f.write(dataStrongHebrewWord+" ")
# f.close()

# time.sleep(1)
# ########################################################################
# ##### Bible Choices - Bible IDs
bibleId='926aa5efbc5e04e2-01' #German Luther Bible 1912 with Strong's numbers
# # bibleId='06125adad2d5898a-01' #The Holy Bible, American Standard Version - no data strong
# bibleId='685d1470fe4d5c3b-01'  #American Standard Version (Byzantine Text with Apocrypha) - New Testament only
# bibleId='de4e12af7f28f599-01'  #King James (Authorised) Version
# bibleId='de4e12af7f28f599-02'  #King James (Authorised) Version
# bibleId='9879dbb7cfe39e4d-01'   #World English Bible
# bibleId='7142879509583d59-01'   #World English Bible British Edition - 
# bibleId='72f4e6dc683324df-01'    #World English Bible Updated - 
# bibleId='32664dc3288a28df-01'    #World English Bible, American English Edition, without Strong's Numbers - 
# bibleId='f72b840c855f362c-04'    #World Messianic Bible - New Testament only
# bibleId='66c22495370cdfc0-01'    #Translation for Translators - 
# bibleId='2f0fd81d7b85b923-01'    #The English New Testament According to Family 35 - New Testament only
# bibleId='c89622d31b60c444-02'   #The Orthodox Jewish Bible
# bibleId='65bfdebd704a8324-01'   #Brenton English translation of the Septuagint
# bibleId='65eec8e0b60e656b-01'    #Free Bible Version - 
# bibleId='c315fa9f71d4af3a-01'   #Geneva Bible - 

####### Build the URL
# bibleChapterId='GEN.2'
# url = "/v1/bibles/"+bibleId
# url = "/v1/bibles/"+bibleId+"/chapters/"+bibleChapterId
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/books/GEN"
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/chapters/GEN.2"
# url = "https://api.scripture.api.bible/v1/bibles/"+bibleId+"/books"
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
# print(theJSON)

##############
# if createFile:
#     if os.path.exists(fname): # Check if the file exists
#         os.remove(fname) # If it exists, delete the file
#     f = open(fname, "a")
#     f.write(theJSON)
#     f.close()

    # dataStrongVerse.append(item.get('data-strong'))

    # for link in soup.find_all('span'):
    #     if link['class'][0] == 'w':
    #         dataStrongVerse.append(link.get('data-strong'))

    # # if soup.span['class'] == 'w':
    # #     soup.
    # # item = soup.find("span").find("data-strong")
    # # a=soup.find_all('data-strong')

# for i in theJSON["span"]:
#     if i["content"] == bibleName:
#         biblePassage=biblePassage+" "+i["data-strong"]
#         print("The Bible ID for the bible",bibleName,"is",bibleId)
#         break

# print("The specific chapter desired from this book is:",getSpecificBibleChapter)
########################################################################
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
#Need to figure out how to write out the books for the specifid Bible - specifically German Luther Bible 1912 with Strong's numbers

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

########### stop here
################################################################
################################################################
################################################################
################################################################

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

# Keyword search for passages containing the word
keywordSearch=input("What is the specific keyword you want to search for in the Bible? ")
limitOfPassagesToBringBack=input("How many total passages do you want to bring back that match the keyword? ")
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/search?query=discouraged&limit=10&sort=relevance"
url = "/v1/bibles/"+bibleId+"/search?query="+keywordSearch+"&limit="+limitOfPassagesToBringBack+"&sort=relevance"
getPassagesForKeyword=a.getBibleData(url)
print("The passage results for the keyword are as follows:",getPassagesForKeyword)
for i in getPassagesForKeyword['data']['verses']:
    verseMatch=i['text']
    print("Matching verse is:")
    print(verseMatch)

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