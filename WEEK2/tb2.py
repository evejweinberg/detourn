import sys
from textblob import TextBlob
import codecs
from collections import Counter


# filedata = codecs.open(sys.argv[1], 'r', 'utf-8')
# read or write, and what encoding, use utf-8
filedata = codecs.open('medium.txt', 'r', 'utf-8')
text = filedata.read()


blob = TextBlob(text)

# get all the words
blob.words


# get the noun phrases
phrases = blob.noun_phrases
for phrase in phrases:
    print phrase

print "///////////////////////////////"
# find the most common phrases
counter = Counter(phrases)
most_common = counter.most_common(10)
for item in most_common:
    print item



# find lines that contain the most common phrases...
most_common = [w[0] for w in most_common]
for line in text.split('\n'):
    for phrase in most_common:
        if phrase.lower() in line.lower():
            print line


# READ MORE ABOUT IT:
# http://textblob.readthedocs.io/en/dev/
# text.encode('utf8')
