from typing import List, Dict
from unidecode import unidecode
from spacy_wrapper import Spacy
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
import pyLDAvis.lda_model
import numpy as np


class LDA:
    n_topics = 10

    def __init__(self, content: str, lang: str):
        self.content = content
        self.lang = lang
        self.tokens = tokenize(content=self.content, lang=self.lang)
        self.model = LatentDirichletAllocation(
            n_components=self.n_topics,
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
        self.learn_model()

    def learn_model(self) -> dict:
        W = self.model.fit_transform(self.tfidf)
        H = self.model.components_
        num_words = 10
        vocab = np.array(self.vectorizer.get_feature_names_out())
        top_words = lambda t: [vocab[i] for i in np.argsort(t)[: -num_words - 1 : -1]]
        topic_words = [top_words(t) for t in H]
        topics_dict = {num: topic_words for num, topic_words in enumerate(topic_words)}

        vis_data = pyLDAvis.lda_model.prepare(
            self.model, self.tfidf, self.vectorizer, R=self.n_topics, mds="tsne"
        )
        pyLDAvis.save_html(vis_data, "./lda_result.html")
        print("Result stored in lda_result.html")
        return topics_dict


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
