import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_stopwords
from spacy.lang.pl.stop_words import STOP_WORDS as pl_stopwords
from spacy.lang.nl.stop_words import STOP_WORDS as nl_stopwords
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stopwords
from spacy.lang.de.stop_words import STOP_WORDS as de_stopwords
from spacy.lang.es.stop_words import STOP_WORDS as es_stopwords
from spacy.lang.it.stop_words import STOP_WORDS as it_stopwords


class Spacy:
    models = {
        "pl": {"model": "pl_core_news_md", "stopwords": pl_stopwords},
        "en": {"model": "en_core_web_md", "stopwords": en_stopwords},
        "nl": {"model": "nl_core_news_md", "stopwords": nl_stopwords},
        "fr": {"model": "fr_core_news_md", "stopwords": fr_stopwords},
        "de": {"model": "de_core_news_md", "stopwords": de_stopwords},
        "es": {"model": "es_core_news_md", "stopwords": es_stopwords},
        "it": {"model": "it_core_news_md", "stopwords": it_stopwords},
    }

    def __init__(self, lang: str):
        lang = lang.lower()
        if isinstance(lang, str) and lang in self.models.keys():
            self.nlp = spacy.load(self.models[lang]["model"], disable="ner")
            self.stopwords = self.models[lang]["stopwords"]

        def __repr__(self):
            return f"{self.nlp}"
