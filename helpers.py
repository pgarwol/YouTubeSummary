def replace_invalid_chars(content: str, symbol: str = "_") -> str:
    return content.replace(" ", symbol).replace('|', symbol)
