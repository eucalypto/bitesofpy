from collections import defaultdict


def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    word_indices = defaultdict(list)
    for index, word in enumerate(words):
        word_indices[word].append(index)

    return sorted([occurrences[0]
                   for occurrences in word_indices.values()
                   if len(occurrences) > 1])


def _get_duplicate_indices(words):
    """
    This is the official solution. It is shorter and is slightly different.
    """
    duplicate_words = {word for word in words if words.count(word) > 1}
    return sorted([words.index(word) for word in duplicate_words])
