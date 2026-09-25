import re
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text: str) -> str:
    text = str(text).lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text

def build_vectorizer():
    return TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
