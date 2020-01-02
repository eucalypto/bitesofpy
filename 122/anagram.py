def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    # return true if sorted()
    def sort_letters(word):
        return sorted(list(letter.lower() for letter in word if letter.isalnum()))

    if sort_letters(word1) == sort_letters(word2):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_anagram('rail safety', 'fairy tales'))
