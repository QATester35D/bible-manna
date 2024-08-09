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
        # self.usgsEarthquakeApi = requests.get(earthquakeURL+params)

    def getBibleData(self, urlRemainder, theJSON):
        #pass in remainder of URL for the desired query
        #urlRemainder looks similar to: /v1/bibles
        #Need to build url = "https://api.scripture.api.bible/v1/bibles"
        url=
        headers = {'api-key': API_KEY}
        response = requests.request("GET", url, headers=headers)
        theJSON = json.loads(response.content)
        print(response.text)
        r=self.usgsEarthquakeApi
        if r.status_code != 200:
            print ("Problem connecting with USGS Earthquake API at https://earthquake.usgs.gov/earthquakes.")
            exit
        earthquakeList = []
        try:
            theJSON = json.loads(r.content)
        except:
            theJSON = None
                
        if not theJSON or 'type' not in theJSON :
            print('==== Failure To Retrieve ====')
            print(r.content)


################################################################
# All Bibles
url = "https://api.scripture.api.bible/v1/bibles"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)
################################################################
# Get a specific Bible
# The Holy Bible, American Standard Version - 06125adad2d5898a-01
# bibleId='06125adad2d5898a-01'
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)
################################################################
# Get all books
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books"



# /v1/bibles/{bibleId}/books/{bookId}/chapters
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/GEN/chapters"
print("Retrieving all chapters from Genesis.")
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.2"
headers = {'api-key': API_KEY}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)
print("\n")

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