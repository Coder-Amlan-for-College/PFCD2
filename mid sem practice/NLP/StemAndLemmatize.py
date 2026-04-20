from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
from textblob import TextBlob,Word

stopwords = stopwords.words('english')
text = """Natural Language Processing enables machines to understand and process human languages.
It is a fascinating field with numerous applications, such as chatbots and language translation."""
blob = TextBlob(text)
stems = []
ps = PorterStemmer()
for word in blob.words:
    stems.append(ps.stem(word))

wnl = WordNetLemmatizer()
lems = []
for word in blob.words:
    lems.append(wnl.lemmatize(word))

filter_words = []
for word in blob.words:
    if word not in stopwords:
        filter_words.append(word)

print(f"Stems:{stems}\n\nLemmatize:{lems}\n\nFilter:{filter_words}\n\n")