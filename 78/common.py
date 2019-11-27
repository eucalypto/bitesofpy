from functools import reduce


def common_languages(programmers: dict):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    language_sets = (set(languages)
                     for languages in programmers.values())

    return reduce(set.intersection, language_sets)


if __name__ == '__main__':
    common_languages({1: "c", 2: "c"})
