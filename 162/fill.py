HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    needed_spaces = column_length - len(str(value))
    return needed_spaces * fill_char + str(value)
