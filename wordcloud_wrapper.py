from wordcloud import WordCloud
from typing import List
import matplotlib.pyplot as plt


def save_wordcloud(wc: WordCloud, name: str = "wordcloud", ext: str = "jpg"):
    wc.to_file(f"./{replace_spaces(name)}.{ext}")
    print(f"Result stored in {replace_spaces(name)}.{ext}")


def create_wordcloud(words: List[str]):
    all_words_str = " ".join(words)

    wordcloud_params = {
        "width": 1000,
        "height": 600,
        "background_color": "white",
        "max_words": 200,
        "collocations": False,
    }
    wordcloud = WordCloud(**wordcloud_params).generate(all_words_str)
    return wordcloud


def replace_spaces(content: str, symbol: str = "_") -> str:
    return content.replace(" ", symbol)
