def replace_invalid_chars(content: str, symbol: str = "_") -> str:
    return content.replace(" ", symbol).replace("|", symbol)


def convert_nones(content: str | list):
    if not content:
        return "-"
    else:
        return content
