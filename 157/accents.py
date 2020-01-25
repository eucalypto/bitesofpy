import unicodedata as ud


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return {char for char in text.lower() if ud.decomposition(char) != ''}
