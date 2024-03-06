from lda import LDA
from helpers import remove_brackets_content, xml_to_str, detect_lang
import datetime
from enum import Enum
from pytube.exceptions import AgeRestrictedError, VideoUnavailable
from typing import Tuple
from pytube import YouTube, Caption
from language_models import supported_languages, LanguageUnsupportedException
from langdetect import detect


class Movie:
    def __init__(self, url: str) -> None:
        self.url = url
        try:
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
        except VideoUnavailable:
            self.status = Status.NEGATIVE_VIDEO_UNAVAILABLE
            return

        try:
            yt.bypass_age_gate()

            caption_str, self.language = self.get_proper_captions(yt=yt)
            self.caption = remove_brackets_content(caption_str)
            self.status = Status.POSITIVE

        except LanguageUnsupportedException:
            self.status = Status.NEGATIVE_LANG_UNSUPPORTED
        except IndexError:
            self.status = Status.NEGATIVE_NO_CAPTIONS
        except AgeRestrictedError:
            self.status = Status.NEGATIVE_AGE_RESTRICTED
        except VideoUnavailable:
            self.status = Status.NEGATIVE_VIDEO_UNAVAILABLE

    def __repr__(self):
        return f"""
{150*'-'}
Author:                    {self.author}
Title | Url:               {self.title} | {self.url}
Thumbnail:                 {self.thumbnail}
Length | Views | Rating:   {self.length} | {self.views} | {self.rating}
Tags:                      {self.tags}
{150*'-'}"""

    def get_proper_captions(self, yt: YouTube):
        potential_country_codes = {}
        potential_country_codes.update(
            {
                "Auto-generated": next(
                    (
                        key.code
                        for key in yt.captions.keys()
                        if key.code.startswith("a.")
                    ),
                    None,
                )
            }
        )
        potential_country_codes.update({"Title": detect(self.title)})
        potential_country_codes.update({"First": list(yt.captions.keys())[0].code})
        print(
            f"""
{150*'-'}
Sugested language codes:
Title: {potential_country_codes["Title"]},
Auto-generated: {potential_country_codes["Auto-generated"]}
First: {potential_country_codes["First"]}
{150*'-'}"""
        )

        #  CODES IMPORTANCE:
        #  Auto-generated > Title > First
        for code in potential_country_codes.values():
            if code:
                chosen_code = code
                break
        else:
            chosen_code = None

        caption_xml = yt.captions[chosen_code].xml_captions
        caption_str = xml_to_str(caption_xml)
        if chosen_code.startswith("a."):
            chosen_code = chosen_code[2:]

        if chosen_code not in supported_languages:
            raise LanguageUnsupportedException

        return caption_str, chosen_code


class Status(Enum):
    POSITIVE = "Positive"
    NEGATIVE_AGE_RESTRICTED = "Content is age restricted."
    NEGATIVE_NO_CAPTIONS = "Content does not contain captions."
    NEGATIVE_LANG_UNSUPPORTED = "Language of this content is not supported."
    NEGATIVE_VIDEO_UNAVAILABLE = "This video is unavailable."
