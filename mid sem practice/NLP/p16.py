import spacy

nlp = spacy.load("en_core_web_sm")
doc1 = nlp("Romeo and Juliet")
doc2 = nlp("Comedy and Comedy")

print(doc1.similarity(doc2))