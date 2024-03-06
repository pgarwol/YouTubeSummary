from language_models import lang_models
from helpers import replace_invalid_chars
from typing import List
from wordcloud import WordCloud


def create_wordcloud(words: List[str], lang: str) -> WordCloud:
    wordcloud_params = {
        "width": 1100,
        "height": 800,
        "background_color": "white",
        "max_words": 200,
        "collocations": True,
        "min_font_size": 12,
        "font_path": r"fonts\static\RobotoSlab-SemiBold.ttf",
        "stopwords": lang_models[lang]["stopwords"],
    }
    wordcloud = WordCloud(**wordcloud_params).generate(" ".join(words))
    return wordcloud


def save_wordcloud(
    wordcloud: WordCloud, filename: str = "wordcloud", ext: str = "jpg"
) -> str:
    save_path = f"{replace_invalid_chars(filename)}.{ext}"
    wordcloud.to_file(save_path)
    return save_path
