##############################################################################################
# This script uses the meaningless project/package (https://pypi.org/project/meaningless/)
# It is limited in use. Seems to really only work effectively with the NIV. It also seems to use
# the "biblegateway.com/api/" however that api is not open anymore.
#
# Note that if a method fails, it is probably because you are trying to access a Book that is
# not available for that translation (some only offer the New Testament)
##############################################################################################
# Using https://pypi.org/project/meaningless/#description 
from meaningless import JSONDownloader
from meaningless import json_file_interface
from meaningless import WebExtractor
from meaningless import CSVDownloader
import time

def getVerseForAllTranslations(book,chapter,verse):
    for i, value in enumerate(translations, start=00):
        if i == 0:
            print("Looking up Bible verse: " + book + " " + str(chapter) + ":" + str(verse))
        bible = WebExtractor(value)
        passage = bible.get_passage(book,chapter,verse) #Like: 'Ecclesiastes', 1, 2
        print(value + " Translation: " + passage)

# Put these in classes, have this class/module use inheritance
def getMultiVersesForAllTranslations(book, chapter_from, passage_from, chapter_to, passage_to):
    for i, value in enumerate(translations, start=00):
        if i == 0:
            print("Looking up Bible verse: "+book+" "+str(chapter_from)+":"+str(passage_from)+"-"+str(chapter_to)+":"+str(passage_to))
        bible = WebExtractor(value)
        # passage = bible.get_passage('Ecclesiastes', 1, 2)
        passage = bible.get_passage_range(book, chapter_from, passage_from, chapter_to, passage_to)
        print(value + " Translation: " + passage)

# Save passage result to a JSON file
def writePassageResultToJsonFile(book,chapter,verse):
    downloader = JSONDownloader()
    time.sleep(2)
    downloader.download_passage(book,chapter,verse) #Like: 'Ecclesiastes', 1, 2
    bible = json_file_interface.read('C:/Temp/Ecclesiastes.json')
    bible['Info']['Customised?'] = True
    json_file_interface.write('./Ecclesiastes.json', bible)

translations=["ASV","AKJV","BRG","EHV","ESV","ESVUK","GNV","GW","ISV",
              "JUB","KJV","KJ21","LEB","MEV","NASB","NASB1995","NET",
              "NIV","NIVUK","NKJV","NLT","NLV","NOG","NRSV","NRSVUE","WEB","YLT"]

bibleVersions={
    "ASV":"American Standard Version",
    "AKJV":"Authorized King James Version",
    "BRG":"BRG Bible",
    "EHV":"Evangelical Heritage Version",
    "ESV":"English Standard Version",
    "ESVUK":"English Standard Version Anglicised",
    "GNV":"Geneva Bible",
    "GW":"God's Word",
    "ISV":"International Standard Version",
    "JUB":"Jubilee Bible",
    "KJV":"King James Version",
    "KJ21":"21st Century King James Version",
    "LEB":"Lexham English Bible",
    "MEV":"Modern English Version",
    "NASB":"New American Standard Bible",
    "NASB1995":"New American Standard Bible 1995 Edition",
    "NET":"New English Translation",
    "NIV":"New International Version",
    "NIVUK":"New International Version UK",
    "NKJV":"New King James Version",
    "NLT":"New Living Translation",
    "NLV":"New Life Version",
    "NOG":"Names of God Bible",
    "NRSV":"New Revised Standard Version",
    "NRSVUE":"New Revised Standard Version Updated Edition",
    "WEB":"World English Bible",
    "YLT":"Young's Literal Translation of the Bible"
}

#Some calls are restricted to using the WebExtractor only
# Write to various file formats: YAML, JSON, XML, CSV

##########This one has an issue all of a sudden, seems to spawn multiple subprocesses and gets out of whack
# This one is JSON format
# writePassageResultToJsonFile('Acts', 4, 12)



####################################################################
# Bring back ALL the translations for a range of Bible verses
# *This works
####################################################################
# getMultiVersesForAllTranslations('Genesis', 1, 1, 1, 2)

####################################################################
# Bring back ALL the translations for a single Bible verse
# *This works
####################################################################
getVerseForAllTranslations('Psalms', 94, 19)

####################################################################
# booksInNewTestament=["Matthew","Mark","Luke","John","Acts","Romans",
#                 "1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians",
#                 "Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy",
#                 "Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John",
#                 "3 John","Jude","Revelation"]
# for i in booksInNewTestament:
#     downloader.download_book(i, "C:\\Temp\\Bible\\NIV_"+i+".csv")
####################################################################

# More stuff to do: finding/searching text in a book

# if __name__ == '__main__':
#     #This section would only run in a main section - this downloads each book in the Bible
#     booksInBible=["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges",
#                   "Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles",
#                   "Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes",
#                   "Song of Songs","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea",
#                   "Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah",
#                   "Haggai","Zechariah","Malachi","Matthew","Mark","Luke","John","Acts","Romans",
#                   "1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians",
#                   "Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy",
#                   "Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John",
#                   "3 John","Jude","Revelation"]
    # downloader = CSVDownloader()
    # for i in booksInBible:
    #     downloader.download_book(i, "C:\\Temp\\Bible\\NIV_"+i+".csv")
