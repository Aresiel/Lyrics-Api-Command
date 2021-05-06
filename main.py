import requests
import json

def splitLyrics(lyr):

    verses = lyr.split("\n\n")

    joinedVerses = []

    while len(verses) > 0:
        joinedVerse = ""
        verseCount = 0

        while True:
            print("verseLength " + str(len(verses[verseCount:])))
            if len(verses[verseCount:]) == 0:
              break
            
            verseToBeAdded = verses[verseCount:][0]

            if (len(joinedVerse) + len(verseToBeAdded)) > 2048:
                break

            print(verseToBeAdded)
            joinedVerse = joinedVerse + verseToBeAdded
            verseCount = verseCount + 1

        verses = verses[verseCount-1:]
        joinedVerses.append(joinedVerse)
        """print(joinedVerse)
        print(joinedVerses)
        print(verseCount)
        print("\n\n")"""

    print(verses)

    return lyr


response = requests.get(
    "https://some-random-api.ml/lyrics?title=you%20should%20be%20sad")

jsonResponse = json.loads(response.text)

lyricsArray = splitLyrics(jsonResponse['lyrics'])
