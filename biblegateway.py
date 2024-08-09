import requests
import json
import time
import urllib.request, urllib.parse, urllib.error
from collections import defaultdict

API_KEY = 'c0688c91b5867edc8faf256a9ee319ca'

url = "https://api.scripture.api.bible/v1/bibles"
headers = {'api-key': 'c0688c91b5867edc8faf256a9ee319ca'}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
# print(response.text)

# The Holy Bible, American Standard Version - 06125adad2d5898a-01
# bibleId='06125adad2d5898a-01'
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books"
# /v1/bibles/{bibleId}/books/{bookId}/chapters
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/books/GEN/chapters"
print("Retrieving all chapters from Genesis.")
# url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.2"
headers = {'api-key': 'c0688c91b5867edc8faf256a9ee319ca'}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)
print("\n")

# /v1/bibles/{bibleId}/passages/{passageId}
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/passages/GEN.1.1-GEN.1.2"
headers = {'api-key': 'c0688c91b5867edc8faf256a9ee319ca'}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print("Retrieving passages.")
print(response.text)


#  /v1/bibles/06125adad2d5898a-01/search?query=discouraged&limit=10&sort=relevance
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/search?query=discouraged&limit=10&sort=relevance"
headers = {'api-key': 'c0688c91b5867edc8faf256a9ee319ca'}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)


#                                      /v1/bibles/{bibleId}/chapters/{chapterId}/verses
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/chapters/GEN.1/verses"
headers = {'api-key': 'c0688c91b5867edc8faf256a9ee319ca'}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)


# /v1/bibles/{bibleId}/verses/{verseId}
url = "https://api.scripture.api.bible/v1/bibles/06125adad2d5898a-01/verses/GEN.1.1"
headers = {'api-key': 'c0688c91b5867edc8faf256a9ee319ca'}
response = requests.request("GET", url, headers=headers)
theJSON = json.loads(response.content)
print(response.text)


time.sleep(1)