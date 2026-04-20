import spacy
def load_text(path):
    with open(path,"r",encoding="utf-8") as f:
        text = f.read()
    
    return text

nlp = spacy.load("en_core_web_sm")
doc = nlp(load_text(r"NLP/read.txt"))

for ent in doc.ents:
    print(ent.text,ent.label_)