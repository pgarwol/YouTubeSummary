from handle_tags import strip_tags


def xml_to_str(xml_repr: str) -> str:
    str_repr = strip_tags(xml_repr).replace("\n", " ")
    return str_repr
