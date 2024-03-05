from spacy_wrapper import Spacy
from typing import List, Tuple
import numpy as np
import pyLDAvis.lda_model
from unidecode import unidecode
from pyLDAvis import prepared_data_to_html
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer


class LDA:
    _N_TOPICS = 3

    def __init__(self, content: str, lang: str):
        self.content = content
        self.lang = lang
        self.tokens = tokenize(content=self.content, lang=self.lang)
        self.model = LatentDirichletAllocation(  # TODO: Fine Tuning
            n_components=self._N_TOPICS,
            max_iter=177,
            learning_method="online",
            learning_offset=104.73684210526315,
            learning_decay=0.631578947368421,
            batch_size=370,
            doc_topic_prior=0.7631578947368421,
            topic_word_prior=0.6684210526315789,
            n_jobs=-1,
        )
        self.vectorizer = TfidfVectorizer()
        self.tfidf = self.vectorizer.fit_transform(self.tokens)
        self.html, self.topics = self.learn_model()

    def learn_model(self) -> Tuple[str, dict]:
        W = self.model.fit_transform(self.tfidf)
        H = self.model.components_
        num_words = 10
        vocab = np.array(self.vectorizer.get_feature_names_out())
        top_words = lambda t: [vocab[i] for i in np.argsort(t)[: -num_words - 1 : -1]]
        topic_words = [top_words(t) for t in H]
        topics_dict = {num: topic_words for num, topic_words in enumerate(topic_words)}

        vis_data = pyLDAvis.lda_model.prepare(
            self.model, self.tfidf, self.vectorizer, R=7, mds="tsne"
        )
        lda_html = prepared_data_to_html(vis_data)
        return lda_html, topics_dict


def tokenize(content: str, lang: str) -> List[str]:
    spacy = Spacy(lang=lang)
    doc = spacy.nlp(content)
    tokens = [
        unidecode(token.lemma_).lower()
        for token in doc
        if token.lemma_.lower() not in spacy.stopwords
        and token.text.isalpha()
        and token.pos_ == "NOUN"
        and len(token.lemma_) > 2
    ]
    return tokens
