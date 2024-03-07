from language_models import lang_models
from helpers import replace_invalid_chars
from typing import List
from pathlib import Path
from wordcloud import WordCloud


def create_wordcloud(words: List[str], lang: str) -> WordCloud:
    """
    Creates a word cloud based on a list of words.

    Parameters:
    - words (List[str]): List of words to generate the word cloud.
    - lang (str): Language code for stopwords and other parameters.

    Returns:
    WordCloud: The generated WordCloud object.
    """
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
) -> Path:
    """
    Saves a WordCloud object to an image file.

    Parameters:
    - wordcloud (WordCloud): The WordCloud object to be saved.
    - filename (str): The base filename for the saved image (default: "wordcloud").
    - ext (str): The file extension for the saved image (default: "jpg").

    Returns:
    Path: The path to the saved image file.
    """
    save_path = Path(f"{replace_invalid_chars(filename)}.{ext}")
    wordcloud.to_file(save_path)
    return save_path
