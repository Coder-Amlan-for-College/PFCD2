from textblob import Word

word = Word("Good")

synonyms = set()

for syn in word.synsets:
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

print(synonyms)