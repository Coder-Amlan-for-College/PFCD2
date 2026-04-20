from textblob.utils import strip_punc, lowerstrip

text = "Hello, World!"
print(strip_punc(text,all=True))
print(lowerstrip(text,all=True))
print(text)