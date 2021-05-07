import requests
import json


def split_lyrics(lyr):
    verses = lyr.split("\n\n")

    joined_verses = []

    while len(verses) > 0:
        joined_verse = ""
        verse_count = 0

        while True:
            v = verses[verse_count:]
            if len(verses[verse_count:]) == 0:
                break

            verse_to_be_added = verses[verse_count:][0]

            if (len(joined_verse) + len(verse_to_be_added)) + len("\n\n") > 2048:
                break

            joined_verse = (joined_verse + "\n\n" + verse_to_be_added).strip()
            verse_count = verse_count + 1

        verses = verses[verse_count:]
        joined_verses.append(joined_verse)

    return joined_verses


#song = "https://some-random-api.ml/lyrics?title={0}".format(input("Song? ")).replace(" ", "%20")

request_url = "https://some-random-api.ml/lyrics?title=you%20should%20be%20sad"

print("## Request URL ##")
print(request_url)
response = requests.get(request_url)

jsonResponse = json.loads(response.text)

print("## Unsplit Lyrics ##")
print(jsonResponse['lyrics'])

print("## Split Lyrics ##")
verseArray = split_lyrics(jsonResponse['lyrics'])

for verse in verseArray:
    print(verse)
    print("\n\n--\n\n")