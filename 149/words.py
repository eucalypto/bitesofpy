def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    starting_with_number = sorted(
        [word for word in words if word[0].isdigit()],
        key=str.casefold)
    not_starting_with_number = sorted(
        [word for word in words if not word[0].isdigit()],
        key=str.casefold)
    return not_starting_with_number + starting_with_number
