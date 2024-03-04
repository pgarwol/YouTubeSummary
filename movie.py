from dataclasses import dataclass, field


@dataclass
class Movie:
    url: str
    title: str
    caption: str

    def __repr__(self):
        return f"{self.title} ({self.url})"
