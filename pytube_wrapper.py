from lda import LDA
from helpers import remove_square_brackets, xml_to_str
from pytube.exceptions import AgeRestrictedError, VideoUnavailable
from language_models import LanguageUnsupportedException, check_lang_support
import datetime
from enum import Enum
from typing import Tuple
from langdetect import detect
from pytube import YouTube


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

        print(self.__repr__())

        try:
            yt.bypass_age_gate()

            captions, self.language = self.get_proper_captions(yt=yt)
            self.captions = remove_square_brackets(captions)
            self.status = Status.POSITIVE

        except LanguageUnsupportedException:
            self.status = Status.NEGATIVE_LANG_UNSUPPORTED
        except NoCaptionsException:
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
Tags:                      {self.tags}"""

    def get_proper_captions(self, yt: YouTube) -> Tuple[str, str]:
        """
        Fetches and processes captions, handling language detection and support.

        Parameters:
        - yt (YouTube): The YouTube video object.

        Returns:
        Tuple[str, str]: Processed captions and detected language code.
        """
        language_code = captions_code = self.get_captions_code(yt=yt)

        if captions_code.startswith("a."):
            language_code = captions_code[2:]
            if not check_lang_support(language=language_code):
                raise LanguageUnsupportedException

        captions_xml = yt.captions[captions_code].xml_captions
        captions = xml_to_str(captions_xml)

        return captions, language_code

    def get_captions_code(self, yt: YouTube) -> str:
        """
        Determines the appropriate captions code based on available options.

        Parameters:
        - yt (YouTube): The YouTube video object.

        Returns:
        str: The selected captions code.
        """
        captions_codes = {}
        try:
            captions_codes.update({"First": list(yt.captions.keys())[0].code})
        except IndexError:
            raise NoCaptionsException

        captions_codes.update(
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
        captions_codes.update({"Title": detect(self.title)})

        print(
            f"""{150*'-'}
Sugested language codes:
First: {captions_codes["First"]},
Auto-generated: {captions_codes["Auto-generated"]},
Title: {captions_codes["Title"]}
{150*'-'}"""
        )
        if captions_codes["Auto-generated"]:
            return captions_codes["Auto-generated"]
        elif captions_codes["Title"]:
            return captions_codes["Title"]
        else:
            return captions_codes["First"]


class Status(Enum):
    POSITIVE = "Positive"
    NEGATIVE_AGE_RESTRICTED = "Content is age restricted."
    NEGATIVE_NO_CAPTIONS = "Content does not contain captions."
    NEGATIVE_LANG_UNSUPPORTED = "Language of this content is not supported."
    NEGATIVE_VIDEO_UNAVAILABLE = "This video is unavailable."


class NoCaptionsException(Exception):
    def __init__(self, message="Content does not contain captions."):
        self.message = message
        super().__init__(self.message)
