import requests
import json
import time
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
        print(response.text)
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

########################## Main program logic ##########################
a=BibleGetInsight()
API_KEY=a.API_KEY

#Get all the available Bible versions/translations
bibles=a.getBibleData("/v1/bibles")

bibleName="The Holy Bible, American Standard Version"
for i in bibles["data"]:
    if i["name"] == bibleName:
        bibleId=i["id"]
        break

########################################################################
# Get a specific Bible - The Holy Bible, American Standard Version - 06125adad2d5898a-01
# bibleId='06125adad2d5898a-01'
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01"
url = "/v1/bibles/"+bibleId
specificBible=a.getBibleData(url)

################################################################
# Get all books
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books"
url = "/v1/bibles/"+bibleId+"/books"
getAllBibleBooks=a.getBibleData(url)

bibleBook="Genesis"
for i in getAllBibleBooks["data"]:
    if i["name"] == bibleBook:
        bibleBookId=i["id"]
        break

################################################################
# Get a specific book
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/GEN"
url = "/v1/bibles/"+bibleId+"/books/"+bibleBookId
getSpecificBibleBook=a.getBibleData(url)

################################################################
# Get all chapters for a specific book
# /v1/bibles/{bibleId}/books/{bookId}/chapters
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/GEN/chapters"
url = "/v1/bibles/"+bibleId+"/books/"+bibleBookId+"/chapters"
getAllBibleChapters=a.getBibleData(url)
bibleChapter="20"
for i in getAllBibleChapters["data"]:
    if i["number"] == bibleChapter:
        bibleChapterId=i["id"]
        break

print("Retrieving all chapters from",bibleBook)
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.2"
# Get a specific book
url = "/v1/bibles/"+bibleId+"/books/"+bibleBookId+"/chapters/"+bibleChapterId
getSpecificBibleChapter=a.getBibleData(url)

######### Pick up here
# /v1/bibles/{bibleId}/passages/{passageId}
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/passages/GEN.1.1-GEN.1.2"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print("Retrieving passages.")
print(response.text)


#  /v1/bibles/06125adad2d5898a-01/search?query=discouraged&limit=10&sort=relevance
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/search?query=discouraged&limit=10&sort=relevance"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)


#                                      /v1/bibles/{bibleId}/chapters/{chapterId}/verses
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.1/verses"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)


# /v1/bibles/{bibleId}/verses/{verseId}
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/verses/GEN.1.1"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)


time.sleep(1)