import os
import urllib.request
from collections import Counter, deque

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    # Convert: deque(list) -> set to profit from hashed O(1) lookup
    stopwords = set(get_words(stopwords_file))
    words_non_filtered = get_words(harry_text)
    words = deque()
    for word in words_non_filtered:
        word = word.lower()
        word = strip_non_alphanumeric(word)
        # add empty string to filtered words, so we don't have to filter
        # it separately.
        stopwords.add("")
        if word in stopwords:
            continue
        words.append(word)
    count = Counter(words)
    return count.most_common()[0]


def strip_non_alphanumeric(text: str) -> str:
    return "".join(char
                   for char in text
                   if char.isalnum())


def get_words(filename) -> deque:
    """
    Return list of words in the file with the name "filename"
    """
    words = deque()
    with open(filename) as file:
        for line in file.readlines():
            for word in line.split():
                words.append(word)
    return words


def test():
    # print(get_words(stopwords_file))
    # print(get_words(harry_text))
    print(strip_non_alphanumeric("2234 uiaern ;.iaren ;j uiae"))
    print(get_harry_most_common_word())
