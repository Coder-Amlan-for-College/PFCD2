from textblob import Word,TextBlob

word = Word("hello")
print(word.spellcheck()[:3])
print(word.correct())

text = "It was really a good movie. But the popcorn was really bad"
blob = TextBlob(text)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)