##########################################################################################
# Helper file that contains the following:
#  - Dictionary of every book in the Bible with a 3 letter abbreviation and the full name
#  - A List of 3 letter abbreviated translations
#  - Dictionary of Bible translations containing a 3 letter abbreviation and the full name
#  - Two methods: one to find the desired Book name and one to find the desired translation name
##########################################################################################
booksInBible={
    "GEN":"Genesis",
    "EXO":"Exodus",
    "LEV":"Leviticus",
    "NUM":"Numbers",
    "DEU":"Deuteronomy",
    "JOS":"Joshua",
    "JDG":"Judges",
    "RUT":"Ruth",
    "1SA":"1 Samuel",
    "2SA":"2 Samuel",
    "1KI":"1 Kings",
    "2KI":"2 Kings",
    "1CH":"1 Chronicles",
    "2CH":"2 Chronicles",
    "EZR":"Ezra",
    "NEH":"Nehemiah",
    "EST":"Esther",
    "JOB":"Job",
    "PSA":"Psalms",
    "PRO":"Proverbs",
    "ECC":"Ecclesiastes",
    "SNG":"Song of Songs",
    "ISA":"Isaiah",
    "JER":"Jeremiah",
    "LAM":"Lamentations",
    "EZK":"Ezekiel",
    "DAN":"Daniel",
    "HOS":"Hosea",
    "JOL":"Joel",
    "AMO":"Amos",
    "OBA":"Obadiah",
    "JON":"Jonah",
    "MIC":"Micah",
    "NAM":"Nahum",
    "HAB":"Habakkuk",
    "ZEP":"Zephaniah",
    "HAG":"Haggai",
    "ZEC":"Zechariah",
    "MAL":"Malachi",
    "MAT":"Matthew",
    "MRK":"Mark",
    "LUK":"Luke",
    "JHN":"John",
    "ACT":"Acts",
    "ROM":"Romans",
    "1CO":"1 Corinthians",
    "2CO":"2 Corinthians",
    "GAL":"Galatians",
    "EPH":"Ephesians",
    "PHP":"Philippians",
    "COL":"Colossians",
    "1TH":"1 Thessalonians",
    "2TH":"2 Thessalonians",
    "1TI":"1 Timothy",
    "2TI":"2 Timothy",
    "TIT":"Titus",
    "PHM":"Philemon",
    "HEB":"Hebrews",
    "JAS":"James",
    "1PE":"1 Peter",
    "2PE":"2 Peter",
    "1JN":"1 John",
    "2JN":"2 John",
    "3JN":"3 John",
    "JUD":"Jude",
    "REV":"Revelation"
}

translations=["ASV","AKJV","BRG","EHV","ESV","ESVUK","GNV","GW","ISV",
              "JUB","KJV","KJ21","LEB","MEV","NASB","NASB1995","NET",
              "NIV","NIVUK","NKJV","NLT","NLV","NOG","NRSV","NRSVUE","WEB","YLT"]

bibleTranslations={
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

def findBibleBookName (bibleBookAbbrev):
    #If abbrev is mixed case, check for a length of 3 (3=abbrev), then make value all uppercase
    if len(bibleBookAbbrev) == 3:
        bibleBookAbbrev=bibleBookAbbrev.upper()
    for k, v in booksInBible.items():
        if k == bibleBookAbbrev:
            return v
    return None #if value not found

def findBibleTranslationName (bibleTranslationAbbrev):
    #If abbrev is mixed case, check for a length of 3 (3=abbrev), then make value all uppercase
    if len(bibleTranslationAbbrev) == 3:
        bibleTranslationAbbrev=bibleTranslationAbbrev.upper()
    for k, v in bibleTranslations.items():
        if k == bibleTranslationAbbrev:
            return v
    return None #if value not found