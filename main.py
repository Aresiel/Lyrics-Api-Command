import requests
import json


def splitLyrics(lyr):
    verseIndices = []
    lastIndex = 0

    # Find where the different verses begin.
    while True:
        nextIndex = lyr.find("\n\n", lastIndex+1)

        if nextIndex == -1:
            break

        lastIndex = nextIndex
        verseIndices.append(nextIndex)

    

    return lyr


response = requests.get(
    "https://some-random-api.ml/lyrics?title=you%20should%20be%20sad")

jsonResponse = json.loads(response.text)

lyricsArray = splitLyrics(jsonResponse['lyrics'])