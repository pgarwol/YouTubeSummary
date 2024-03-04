from pytube import YouTube
from movie import Movie
from lda import LDA
from handle_captions import xml_to_str


class YT:
    def __init__(self, url: str, caption_lang: str) -> None:
        self.url = url
        yt = YouTube(self.url)
        yt.bypass_age_gate()
        #  TODO: lack of captions handling
        caption_xml = yt.captions[caption_lang].xml_captions
        caption_str = xml_to_str(caption_xml)
        self.title = yt.title
        self.caption = caption_str

    def __repr__(self):
        return f'"{self.title}" ({self.url})'
