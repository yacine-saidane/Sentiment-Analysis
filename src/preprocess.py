import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

NEG = {"no", "not", "nor", "never", "don", "didn", "doesn", "isn", "wasn",
       "aren", "weren", "couldn", "wouldn", "shouldn", "won", "hasn",
       "haven", "hadn", "ain", "mustn", "needn", "shan", "mightn"}
STOP_ALL = set(stopwords.words("english")) #Stop words are extremely common words in English that don't carry much emotional or topic weight—words like "the", "is", "at", "which", and "on".
STOP_KEEP = STOP_ALL - NEG
LEM = WordNetLemmatizer()  #A lemmatizer squishes words down to their root form

def clean(text, stop="none", lemmatize=True):
    text = re.sub(r"<.*?>", " ", text).lower()
    text = text.replace("won't", "will not").replace("can't", "can not")
    text = re.sub(r"n't\b", " not", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = text.split()
    if stop == "all":
        tokens = [t for t in tokens if t not in STOP_ALL]
    elif stop == "keep_neg":
        tokens = [t for t in tokens if t not in STOP_KEEP]
    if lemmatize:
        tokens = [LEM.lemmatize(t) for t in tokens]
    return " ".join(t for t in tokens if len(t) > 1)