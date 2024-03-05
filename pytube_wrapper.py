from lda import LDA
from helpers import remove_brackets_content, xml_to_str, detect_lang
import datetime
from pytube import YouTube, Caption
from langdetect import detect


class Movie:
    def __init__(self, url: str) -> None:
        self.url = url
        yt = YouTube(self.url)
        self.title = yt.title
        self.author = yt.author
        self.thumbnail = yt.thumbnail_url
        self.length = str(datetime.timedelta(seconds=yt.length))
        self.views = yt.views
        self.rating = yt.rating
        self.tags = ", ".join(yt.keywords)

        self.info = {
            "Title": self.title,
            "Author": self.author,
            "Thumbnail": self.thumbnail,
            "URL": self.url,
            "Length": self.length,
            "Views": self.views,
            "Rating": self.rating,
            "Tags": self.tags,
        }
        try:
            yt.bypass_age_gate()

            caption_str = self.get_proper_captions(yt=yt)
            self.caption = remove_brackets_content(caption_str)
        except Exception as e:
            print(e)
            self.caption = None

    def __repr__(self):
        return f"""
{150*'-'}
Author:                    {self.author}
Title | Url:               {self.title} | {self.url}
Thumbnail:                 {self.thumbnail}
Length | Views | Rating:   {self.length} | {self.views} | {self.rating}
Tags:                      {self.tags}
{150*'-'}"""

    def get_proper_captions(self, yt: YouTube) -> str | None:
        lang_code = str
        found = False
        lang_from_title = detect(self.title)
        lang_code_automatic = next(
            (key.code for key in yt.captions.keys() if key.code.startswith("a")), None
        )
        print(
            f"""
Sugested language codes:
Title: {lang_from_title},
Automatic: {lang_code_automatic}
"""
        )
        #  Automatic captions > captions detected from title
        chosen_code = lang_code_automatic if lang_code_automatic else lang_from_title
        caption_xml = yt.captions[chosen_code].xml_captions
        caption_str = xml_to_str(caption_xml)

        return caption_str
