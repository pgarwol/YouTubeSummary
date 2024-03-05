import re
from io import StringIO
from html.parser import HTMLParser
from textblob import TextBlob


def replace_invalid_chars(content: str, symbol: str = "_") -> str:
    return content.replace(" ", symbol).replace("|", symbol)


def convert_nones(content: str | list):
    if not content:
        return "-"
    else:
        return content


def remove_brackets_content(content: str) -> str:
    cleared_content = re.sub(r"\[[^\]]*\]", "", content)
    return cleared_content


def xml_to_str(xml_repr: str) -> str:
    str_repr = strip_tags(xml_repr).replace("\n", " ")
    return str_repr


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, data):
        self.text.write(data)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def detect_lang(text: str) -> str:
    lang = TextBlob(text)
    detected_lang = lang.detect_language()
    print("siemson")
    return detected_lang
