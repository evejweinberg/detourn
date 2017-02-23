from textblob import TextBlob

sentence = 'this is a cool sentence'
blob = TextBlob(sentence)

print blob.noun_phrases
