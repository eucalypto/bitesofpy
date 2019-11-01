import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    lines = []
    with open(DICTIONARY, mode="r") as file:
        lines = file.readlines()
    return [line.strip()
            for line in lines]


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    return sum([LETTER_SCORES[letter]
                for letter in word.upper()
                if letter in LETTER_SCORES.keys()])


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    return max(words, key=calc_word_value)


if __name__ == '__main__':
    print(calc_word_value("a"))
