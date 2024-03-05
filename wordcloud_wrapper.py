from helpers import replace_invalid_chars
from typing import List
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def save_wordcloud(wc: WordCloud, name: str = "wordcloud", ext: str = "jpg") -> str:
    save_path = f"{replace_invalid_chars(name)}.{ext}"
    wc.to_file(save_path)
    print(f"Word cloud stored in {save_path}")
    return save_path


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
