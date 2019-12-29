VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    def count_vowels(word):
        return len([True for letter in word if letter in VOWELS])
    words = [(word, count_vowels(word)) for word in text.split()]
    return max(words, key=lambda pair: pair[1])

