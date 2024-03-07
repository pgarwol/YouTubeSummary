import re
from io import StringIO
from typing import Optional, List
from html.parser import HTMLParser


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, data: str) -> None:
        self.text.write(data)

    def get_data(self) -> str:
        return self.text.getvalue()


def replace_invalid_chars(
    content: str,
    invalid_chars: Optional[List[str]] = None,
    replacement: Optional[str] = None,
) -> str:
    """
    Replaces specified invalid characters in a string with a replacement character.

    Parameters:
    - content (str): The input string to be processed.
    - invalid_chars (Optional[List[str]]): List of invalid characters to be replaced (default: [" ", "|"]).
    - replacement (Optional[str]): The character to replace invalid characters with (default: "_").

    Returns:
    str: The string with invalid characters replaced.
    """
    if invalid_chars is None:
        invalid_chars = [" ", "|"]
    if replacement is None:
        replacement = "_"

    for char in invalid_chars:
        content = content.replace(char, replacement)
    return content


def convert_nones(content: str | list) -> str | list:
    """
    Converts None or empty content to a default value ("-").

    Parameters:
    - content (str | list): The content to be processed.

    Returns:
    str | list: The processed content with None or empty values replaced by "-".
    """
    if not content:
        return "-"
    else:
        return content


def remove_square_brackets(content: str) -> str:
    """
    Removes content within square brackets and the brackets themselves from a string.

    Parameters:
    - content (str): The input string to be processed.

    Returns:
    str: The string with square brackets and their contents removed.
    ```
    """
    cleared_content = re.sub(r"\[[^\]]*\]", "", content)
    return cleared_content


def xml_to_str(xml_repr: str) -> str:
    """
    Converts an XML representation to a plain string by removing [] tags and newlines.

    Parameters:
    - xml_repr (str): The XML representation to be processed.

    Returns:
    str: The resulting plain string.
    """
    str_repr = strip_tags(xml_repr).replace("\n", " ")
    return str_repr


def strip_tags(html: str) -> str:
    """
    Removes HTML tags from a string.

    Parameters:
    - html (str): The HTML string to be processed.

    Returns:
    str: The string with HTML tags removed.
    """
    parser = Parser()
    parser.feed(html)
    return parser.get_data()
