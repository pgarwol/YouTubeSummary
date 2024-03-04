import datetime
from lda import LDA
from pytube import YouTube
from handle_captions import xml_to_str


class YT:
    def __init__(self, url: str, caption_lang: str) -> None:
        self.url = url
        yt = YouTube(self.url)
        self.title = yt.title
        self.author = yt.author
        self.thumbnail = yt.thumbnail_url
        self.length = str(datetime.timedelta(seconds=yt.length))
        self.views = yt.views
        self.rating = yt.rating
        self.tags = yt.keywords

        self.info = {
            'Title': self.title,
            'Author': self.author,
            'Thumbnail': self.thumbnail,
            'Length': self.length,
            'Views': self.views,
            'Rating': self.rating,
            'Tags': self.tags
        }
        
        try:
            yt.bypass_age_gate()
            caption_xml = yt.captions[caption_lang].xml_captions
            caption_str = xml_to_str(caption_xml)
            self.caption = caption_str
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
