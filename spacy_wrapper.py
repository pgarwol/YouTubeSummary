import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_stopwords
from spacy.lang.pl.stop_words import STOP_WORDS as pl_stopwords


class Spacy:
    models = {
        "pl": {"model": "pl_core_news_md", "stopwords": pl_stopwords},
        "en": {"model": "en_core_web_md", "stopwords": en_stopwords},
    }

    def __init__(self, lang: str):
        lang = lang.lower()
        if isinstance(lang, str) and lang in ["pl", "en"]:
            self.nlp = spacy.load(self.models[lang]["model"], disable="ner")
            self.stopwords = self.models[lang]["stopwords"]

        def __repr__(self):
            return f"{self.nlp}"
