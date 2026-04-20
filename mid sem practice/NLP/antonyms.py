from textblob import Word

word = Word("Good")

antonyms = set()
for syn in word.synsets:
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())

print(antonyms)
