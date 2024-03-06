from language_models import lang_models
import spacy


class Spacy:
    def __init__(self, lang: str):
        lang = lang.lower()
        if isinstance(lang, str) and lang in lang_models.keys():
            self.nlp = spacy.load(lang_models[lang]["model"], disable="ner")
            self.stopwords = lang_models[lang]["stopwords"]

        def __repr__(self):
            return f"{self.nlp}"
