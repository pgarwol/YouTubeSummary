from helpers import replace_spaces
from typing import List
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def save_wordcloud(wc: WordCloud, name: str = "wordcloud", ext: str = "jpg") -> None:
    wc.to_file(f"./outputs/{replace_spaces(name)}.{ext}")
    print(f"Word cloud stored in {replace_spaces(name)}.{ext}")


def create_wordcloud(words: List[str]) -> WordCloud:
    wordcloud_params = {
        "width": 1000,
        "height": 600,
        "background_color": "white",
        "max_words": 200,
        "collocations": False,
    }
    wordcloud = WordCloud(**wordcloud_params).generate(" ".join(words))
    return wordcloud
