##############################################################################################
# This script uses the meaningless project/package (https://pypi.org/project/meaningless/)
# This also imports my helper file
# Note that if a method fails, it is probably because you are trying to access a Book that is
# not available for that translation (some translations only offer the New Testament books)
##############################################################################################
from meaningless import JSONDownloader
from meaningless import json_file_interface
from meaningless import YAMLDownloader, YAMLExtractor
from meaningless import WebExtractor
import bibleMannaHelperFile
import time

class bibleManna:
    def __init__(self,book,chapter,verse):
        self.book = book
        self.chapter = chapter
        self.verse = verse

    def getVerseForSpecificTranslation(self,translation):
        bible = WebExtractor(translation)
        passage = bible.get_passage(self.book,self.chapter,self.verse) #Like: 'Ecclesiastes', 1, 2
        print(translation + " Translation: " + passage)

    def getVerseForAllTranslations(self):  
        for i, value in enumerate(bibleMannaHelperFile.translations, start=00):
            if i == 0:
                print("Looking up Bible verse: " + self.book + " " + str(self.chapter) + ":" + str(self.verse))
            bible = WebExtractor(value)
            passage = bible.get_passage(self.book,self.chapter,self.verse) #Like: 'Ecclesiastes', 1, 2
            print(value + " Translation: " + passage)

    def getAndWriteAllTranslations(self,folderFileName):
        fileName=folderFileName+".txt"
        f = open(fileName, "w")
        f.write("Translations for "+ self.book + " " + str(self.chapter) + ":" + str(self.verse) +"\n")
        for i, value in enumerate(bibleMannaHelperFile.translations, start=00):
            if i == 0:
                print("Looking up Bible verse: " + self.book + " " + str(self.chapter) + ":" + str(self.verse))
            bible = WebExtractor(value)
            passage = bible.get_passage(self.book,self.chapter,self.verse) #Like: 'Ecclesiastes', 1, 2
            #beginning of passage contains the verse number as a superscript which can't be written as is to a text file, so dropping
            if self.verse != 1:
                verseLen=len(str(self.verse))
                passage=passage[verseLen:]
            valueToWrite=value + " Translation: " + passage
            print(valueToWrite)
            f.write(valueToWrite+"\n")
        f.close()

class bibleManyVerses(bibleManna):
    def __init__(self, book, chapter, verse, chapter_end, passage_end):
        super().__init__(book, chapter, verse)
        self.chapter_end=chapter_end
        self.passage_end=passage_end

    def getMultiVersesForAllTranslations(self):
        book=self.book
        chapter_from=self.chapter
        passage_from=self.verse
        chapter_to=self.chapter_end
        passage_to=self.passage_end
        for i, value in enumerate(bibleMannaHelperFile.translations, start=00):
            if i == 0:
                print("Looking up Bible verse: "+book+" "+str(chapter_from)+":"+str(passage_from)+"-"+str(chapter_to)+":"+str(passage_to))
            bible = WebExtractor(value)
            # passage = bible.get_passage('Ecclesiastes', 1, 2)
            passage = bible.get_passage_range(book, chapter_from, passage_from, chapter_to, passage_to)
            print(value + " Translation: " + passage)

##########################################################################################
# Examples of calling some of these methods
##########################################################################################
# Bring back a specified verse for a specific Bible translation
####################################################################
# bm=bibleManna('Genesis', 22, 2)
# bm.getVerseForSpecificTranslation("NIV")

####################################################################
# Bring back ALL the translations for a single Bible verse
####################################################################
# bm=bibleManna('Genesis', 22, 2)
# bm.getVerseForAllTranslations()
# time.sleep(1)

# ####################################################################
# # Bring back ALL the translations for a range of Bible verses
# ####################################################################
# bmv=bibleManyVerses('Genesis', 22, 20, 2, 22)
# bmv.getMultiVersesForAllTranslations()

# #########################################################################################
# # Bring back ALL the translations for a single Bible verse and write them to a text file
# #########################################################################################
# bm=bibleManna('1 John', 2, 20)
# folderFileName="C:\\Temp\\Bible\\BibleAllTranslations\\AllTranslationsForBibleVerse.txt"
# bm.getAndWriteAllTranslations(folderFileName) #Bring back ALL the translations for a single verse and write it to a text file
# time.sleep(1)
